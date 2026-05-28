# Contexto del Proyecto: FECASAM 2026 Landing Page

## 1. Visión General
Desarrollar una Landing Page profesional para "FECASAM 2026" (Feria Exposición de Camélidos Sudamericanos, Agropecuarios y Artesanales) en Macusani, Puno. La web debe superar el estándar de `alpacafiestaperu.com`, enfocándose en la identidad de Carabaya como "Capital Alpaquera del Mundo".

## 2. Stack Tecnológico
- **Backend:** Laravel 11 (PHP 8.2+)
- **Frontend:** React.js con Inertia.js (para una experiencia SPA con rutas de Laravel).
- **Estilos:** Tailwind CSS (Diseño responsive y moderno).
- **Base de Datos:** MySQL (Gestión de inscripciones y libro de reclamaciones).
- **IDE:** Visual Studio Code.

## 3. Información Clave (Extraída de las Bases)
- **Evento:** XXXI FECASAM 2026.
- **Fecha:** 22 al 30 de agosto de 2026.
- **Lugar:** Campo Ferial Julio Enrique Barreda Aragón, Macusani, Carabaya, Puno.
- **Datos Técnicos para Infografías:** - Fibra de alpaca: Sostenible y de alta suavidad.
  - Carne de camélidos: 24.1% proteína, 3.3 mg hierro, 0.05% colesterol (Saludable y orgánica).
  - Población: Perú tiene el 89% de la población mundial de camélidos.

## 4. Estructura de la Landing Page
### A. Componentes React:
- **HeroSection:** Video de fondo (glaciares/alpacas) + CTA de inscripción.
- **ResourceSection:** 5 botones de descarga (PDF Programa, Bases Concurso, Ruta Paqochañan, Catálogo Expositores, Manual Biotecnología).
- **RegistrationForm:** Formulario vinculado a la base de datos (Nombre, DNI/RUC, Procedencia, Categoría).
- **FloatingContact:** Burbujas flotantes de WhatsApp y Messenger (usando `react-icons`).

## 5. Requisitos Funcionales y Legales
### Gestión de Almacenamiento:
- **Inscripciones:** Almacenadas en tabla `registrations`. Implementar validación en `RegistrationRequest` de Laravel.
- **Admin:** Ruta protegida para exportar inscritos a Excel (Librería: `Maatwebsite/Laravel-Excel`).

### Cumplimiento Normativo (Perú):
- **Libro de Reclamaciones Virtual:**
  - Componente de formulario estandarizado según INDECOPI.
  - Generación de código de seguimiento correlativo (Ej: R-2026-001).
  - Almacenamiento en tabla `complaints`.
  - Envío automático de copia por correo al usuario (Laravel Mail).

## 6. Guía de Estilo (UI/UX)
- **Paleta:** Tonos tierra (Marrón Alpaca #8B5E3C), Blanco Hueso (#F5F5F5) y Oro Andino para acentos en botones.
- **Interacciones:** Framer Motion para entradas suaves al hacer scroll.
- **Iconografía:** Uso de `lucide-react` para archivos y `react-icons` para redes sociales.

## 7. Instrucciones para Copilot
- Cuando genere controladores, usar **Inertia::render** para devolver las vistas de React.
- Priorizar el uso de clases de Tailwind para el diseño.
- Asegurar que todos los formularios incluyan protección **CSRF** y validación de lado del servidor.