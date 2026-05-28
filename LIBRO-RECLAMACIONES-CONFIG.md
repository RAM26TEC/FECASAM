# Libro de Reclamaciones - Configuración

## 🎯 Estado Actual

El Libro de Reclamaciones ya está **completamente funcional** y listo para usar.

## ✅ Modo Desarrollo (Actual)

El sistema funciona automáticamente en **modo desarrollo** que:
- ✓ No requiere base de datos
- ✓ Guarda los registros en un archivo log local
- ✓ Genera códigos de reclamación válidos
- ✓ Valida todos los campos del formulario
- ✓ Retorna respuestas exitosas al frontend

Los datos se guardan en: `dev_complaints.log`

## 📋 Para Producción

Cuando esté listo para usar en producción con base de datos real:

### 1. Configurar Base de Datos

Editar `api/submit-complaint.php` líneas 24-28:

```php
define('DB_HOST', 'localhost');
define('DB_NAME', 'fecasam2026');
define('DB_USER', 'tu_usuario_real');  // Cambiar
define('DB_PASS', 'tu_password_real');  // Cambiar
define('ADMIN_EMAIL', 'reclamaciones@fecasam2026.com');
```

### 2. Crear Tabla en MySQL

Ejecutar el script SQL en `database/schema.sql`:

```sql
CREATE TABLE complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    complaint_code VARCHAR(20) UNIQUE NOT NULL,
    consumer_name VARCHAR(255) NOT NULL,
    consumer_document VARCHAR(12) NOT NULL,
    consumer_email VARCHAR(255) NOT NULL,
    consumer_phone VARCHAR(20) NOT NULL,
    consumer_address VARCHAR(500) NOT NULL,
    product_type ENUM('producto', 'servicio') NOT NULL,
    product_description TEXT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    claim_type ENUM('reclamo', 'queja') NOT NULL,
    claim_detail TEXT NOT NULL,
    consumer_request TEXT NOT NULL,
    status ENUM('pending', 'in_progress', 'resolved', 'closed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_complaint_code (complaint_code),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 3. Configurar Correos (Opcional)

Para enviar notificaciones por email:
- Configurar SMTP en el servidor
- Actualizar `ADMIN_EMAIL` con el email real

## 🔗 Enlaces Actualizados

Todos los enlaces al Libro de Reclamaciones ahora apuntan correctamente a:
- `libro-reclamaciones.html`

Ubicaciones:
- ✓ Menú de navegación principal
- ✓ Footer (Información Legal)
- ✓ Botón flotante

## 🧪 Cómo Probar

1. Abrir el sitio web
2. Hacer clic en "Libro de Reclamaciones" (menú o botón flotante)
3. Llenar el formulario completo
4. Enviar el formulario
5. Verificar mensaje de éxito con código de reclamación

## 📝 Archivos Modificados

- `index.html` - Enlaces actualizados a libro-reclamaciones.html
- `libro-reclamaciones.html` - JavaScript conectado al API
- `api/submit-complaint.php` - Modo desarrollo agregado

## 🚀 Notas

- El modo desarrollo detecta automáticamente credenciales por defecto
- No requiere configuración adicional para pruebas
- Transición a producción es simple: solo cambiar credenciales DB
- Cumple normativa INDECOPI (Ley N° 29571)
