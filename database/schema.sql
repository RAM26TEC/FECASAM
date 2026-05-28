-- ============================================
-- FECASAM 2026 - Database Schema
-- MySQL 5.7+ / MariaDB 10.3+
-- ============================================

-- Create database
CREATE DATABASE IF NOT EXISTS fecasam2026 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE fecasam2026;

-- ============================================
-- TABLE: registrations
-- Almacena las inscripciones al evento
-- ============================================

CREATE TABLE IF NOT EXISTS registrations (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    registration_code VARCHAR(50) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    document_type ENUM('dni', 'ruc', 'ce', 'passport') NOT NULL,
    document_number VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    origin VARCHAR(255) NOT NULL,
    category ENUM(
        'expositor-alpacas',
        'expositor-llamas',
        'expositor-artesania',
        'expositor-gastronomia',
        'visitante',
        'investigador',
        'prensa'
    ) NOT NULL,
    comments TEXT,
    status ENUM('pending', 'confirmed', 'cancelled') DEFAULT 'confirmed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_email (email),
    INDEX idx_document (document_number),
    INDEX idx_category (category),
    INDEX idx_created_at (created_at),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- TABLE: complaints
-- Libro de Reclamaciones Virtual
-- Conforme a INDECOPI
-- ============================================

CREATE TABLE IF NOT EXISTS complaints (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    complaint_code VARCHAR(50) UNIQUE NOT NULL,
    
    -- Consumer Information
    consumer_name VARCHAR(255) NOT NULL,
    consumer_document VARCHAR(20) NOT NULL,
    consumer_email VARCHAR(255) NOT NULL,
    consumer_phone VARCHAR(20) NOT NULL,
    consumer_address TEXT NOT NULL,
    
    -- Product/Service Information
    product_type ENUM('producto', 'servicio') NOT NULL,
    product_description TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    
    -- Claim Information
    claim_type ENUM('reclamo', 'queja') NOT NULL,
    claim_detail TEXT NOT NULL,
    consumer_request TEXT NOT NULL,
    
    -- Response
    response TEXT,
    response_date DATETIME,
    responded_by VARCHAR(100),
    
    -- Status
    status ENUM('pending', 'in_progress', 'resolved', 'closed') DEFAULT 'pending',
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_complaint_code (complaint_code),
    INDEX idx_consumer_email (consumer_email),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- TABLE: contact_messages
-- Mensajes de contacto general
-- ============================================

CREATE TABLE IF NOT EXISTS contact_messages (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    status ENUM('unread', 'read', 'replied') DEFAULT 'unread',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_email (email),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- TABLE: admin_users
-- Usuarios administrativos
-- ============================================

CREATE TABLE IF NOT EXISTS admin_users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role ENUM('super_admin', 'admin', 'moderator') DEFAULT 'moderator',
    is_active BOOLEAN DEFAULT TRUE,
    last_login DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_username (username),
    INDEX idx_email (email),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- TABLE: activity_log
-- Registro de actividades del sistema
-- ============================================

CREATE TABLE IF NOT EXISTS activity_log (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED,
    action VARCHAR(100) NOT NULL,
    description TEXT,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_user_id (user_id),
    INDEX idx_action (action),
    INDEX idx_created_at (created_at),
    
    FOREIGN KEY (user_id) REFERENCES admin_users(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- SAMPLE DATA (for testing)
-- ============================================

-- Insert a test admin user (password: admin123)
-- In production, change this password immediately!
INSERT INTO admin_users (username, email, password_hash, full_name, role) VALUES
('admin', 'admin@fecasam2026.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'Administrador FECASAM', 'super_admin');

-- ============================================
-- VIEWS FOR REPORTING
-- ============================================

-- View: Registrations summary by category
CREATE OR REPLACE VIEW registrations_by_category AS
SELECT 
    category,
    COUNT(*) as total,
    SUM(CASE WHEN status = 'confirmed' THEN 1 ELSE 0 END) as confirmed,
    SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) as cancelled
FROM registrations
GROUP BY category;

-- View: Daily registration statistics
CREATE OR REPLACE VIEW daily_registrations AS
SELECT 
    DATE(created_at) as date,
    COUNT(*) as total,
    COUNT(DISTINCT email) as unique_emails
FROM registrations
GROUP BY DATE(created_at)
ORDER BY date DESC;

-- View: Complaints summary
CREATE OR REPLACE VIEW complaints_summary AS
SELECT 
    claim_type,
    status,
    COUNT(*) as total,
    AVG(DATEDIFF(response_date, created_at)) as avg_response_days
FROM complaints
GROUP BY claim_type, status;

-- ============================================
-- STORED PROCEDURES
-- ============================================

DELIMITER //

-- Generate unique registration code
CREATE PROCEDURE generate_registration_code(OUT new_code VARCHAR(50))
BEGIN
    DECLARE code_exists INT DEFAULT 1;
    DECLARE year_prefix VARCHAR(4);
    DECLARE random_suffix VARCHAR(4);
    
    SET year_prefix = YEAR(NOW());
    
    WHILE code_exists = 1 DO
        SET random_suffix = LPAD(FLOOR(RAND() * 10000), 4, '0');
        SET new_code = CONCAT('FECA-', year_prefix, '-', random_suffix);
        
        SELECT COUNT(*) INTO code_exists 
        FROM registrations 
        WHERE registration_code = new_code;
    END WHILE;
END//

-- Generate unique complaint code
CREATE PROCEDURE generate_complaint_code(OUT new_code VARCHAR(50))
BEGIN
    DECLARE code_exists INT DEFAULT 1;
    DECLARE year_prefix VARCHAR(4);
    DECLARE random_suffix VARCHAR(4);
    
    SET year_prefix = YEAR(NOW());
    
    WHILE code_exists = 1 DO
        SET random_suffix = LPAD(FLOOR(RAND() * 10000), 4, '0');
        SET new_code = CONCAT('R-', year_prefix, '-', random_suffix);
        
        SELECT COUNT(*) INTO code_exists 
        FROM complaints 
        WHERE complaint_code = new_code;
    END WHILE;
END//

DELIMITER ;

-- ============================================
-- EVENTS (Automated tasks)
-- ============================================

-- Enable event scheduler
SET GLOBAL event_scheduler = ON;

-- Auto-cleanup old unconfirmed registrations (optional)
DELIMITER //

CREATE EVENT IF NOT EXISTS cleanup_old_pending_registrations
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
BEGIN
    DELETE FROM registrations 
    WHERE status = 'pending' 
    AND created_at < DATE_SUB(NOW(), INTERVAL 30 DAY);
END//

DELIMITER ;

-- ============================================
-- PERMISSIONS
-- ============================================

-- Create application user (adjust credentials)
-- CREATE USER IF NOT EXISTS 'fecasam_app'@'localhost' IDENTIFIED BY 'secure_password_here';
-- GRANT SELECT, INSERT, UPDATE ON fecasam2026.registrations TO 'fecasam_app'@'localhost';
-- GRANT SELECT, INSERT, UPDATE ON fecasam2026.complaints TO 'fecasam_app'@'localhost';
-- GRANT SELECT, INSERT ON fecasam2026.contact_messages TO 'fecasam_app'@'localhost';
-- GRANT SELECT, INSERT ON fecasam2026.activity_log TO 'fecasam_app'@'localhost';
-- FLUSH PRIVILEGES;

-- ============================================
-- INDEXES FOR PERFORMANCE
-- ============================================

-- Add composite indexes for common queries
CREATE INDEX idx_registration_status_date ON registrations(status, created_at);
CREATE INDEX idx_complaint_status_date ON complaints(status, created_at);

-- ============================================
-- BACKUP REMINDER
-- ============================================

-- Remember to set up regular backups!
-- Example cron job for daily backup:
-- 0 2 * * * mysqldump -u root -p fecasam2026 > /backup/fecasam2026_$(date +\%Y\%m\%d).sql

SELECT 'Database schema created successfully!' as message;
