# 🧪 Guía de Pruebas - Formulario de Inscripción FECASAM 2026

## 📋 Descripción

Suite completa de pruebas automatizadas para validar el formulario de inscripción de FECASAM 2026. Incluye pruebas unitarias y una interfaz visual interactiva.

## 🚀 Formas de Ejecutar las Pruebas

### 1. **Interfaz Visual (Recomendado)**

Abre el archivo `test-formulario.html` en tu navegador:

```bash
# Desde la raíz del proyecto
start test-formulario.html
```

**Características:**
- ✅ Interfaz gráfica moderna y responsive
- ✅ Visualización en tiempo real de resultados
- ✅ Ejecución selectiva de categorías de pruebas
- ✅ Consola integrada con logs detallados
- ✅ Estadísticas y métricas de cobertura

**Botones disponibles:**
- 🎯 **Ejecutar Todas las Pruebas**: Corre el suite completo
- ✔️ **Solo Casos Válidos**: Pruebas de datos correctos
- ❌ **Solo Casos Inválidos**: Pruebas de validación de errores
- ⚠️ **Solo Casos Límite**: Pruebas de casos extremos
- 🗑️ **Limpiar**: Resetear resultados

### 2. **Consola del Navegador**

Abre `index.html` en el navegador y ejecuta en la consola:

```javascript
// Ejecutar todas las pruebas
FormTests.runAllTests()

// Ejecutar una prueba específica
FormTests.runTestByName("DNI inválido")

// Ver casos de prueba disponibles
FormTests.testCases

// Ver resultados de la última ejecución
FormTests.testResults
```

## 📊 Casos de Prueba Incluidos

### ✅ Casos Válidos (4 pruebas)

1. **Inscripción válida con DNI**
   - Valida formato DNI de 8 dígitos
   - Email y teléfono válidos
   - Todos los campos requeridos

2. **Inscripción válida con RUC**
   - Valida formato RUC de 11 dígitos
   - Para empresas/organizaciones

3. **Inscripción válida con Carné de Extranjería**
   - Formato alfanumérico
   - Entre 9-12 caracteres

4. **Inscripción válida con Pasaporte**
   - Formato internacional
   - Hasta 12 caracteres

### ❌ Casos Inválidos (11 pruebas)

1. **Nombre muy corto** - Menos de 3 caracteres
2. **Nombre con números** - Contiene caracteres no alfabéticos
3. **DNI inválido** - Menos o más de 8 dígitos
4. **RUC inválido** - No tiene 11 dígitos exactos
5. **Email sin @** - Formato incorrecto
6. **Email sin dominio** - Incompleto
7. **Teléfono muy corto** - Menos de 9 dígitos
8. **Sin tipo de documento** - Campo requerido vacío
9. **Sin categoría** - Campo requerido vacío
10. **Sin aceptar términos** - Checkbox no marcado
11. **Procedencia muy corta** - Menos de 3 caracteres

### ⚠️ Casos Límite (4 pruebas)

1. **Nombre con acentos y ñ** - Caracteres especiales del español
2. **Email con caracteres especiales** - Plus addressing (+)
3. **Teléfono exacto** - Exactamente 9 dígitos
4. **Procedencia muy larga** - Texto extenso

## 📈 Métricas de Cobertura

Las pruebas cubren:

- ✅ **Validación de nombres** (formato, longitud, caracteres)
- ✅ **Validación de documentos** (DNI, RUC, CE, Pasaporte)
- ✅ **Validación de email** (formato RFC 5322)
- ✅ **Validación de teléfono** (formato peruano)
- ✅ **Validación de campos requeridos**
- ✅ **Validación de términos y condiciones**
- ✅ **Casos límite y caracteres especiales**

## 🛠️ Estructura de Archivos

```
/
├── test-formulario.html      # Interfaz visual de pruebas
├── assets/
│   └── js/
│       ├── main.js            # Lógica principal del formulario
│       └── test-form.js       # Suite de pruebas automatizadas
└── GUIA-PRUEBAS.md           # Este archivo
```

## 🔍 Interpretación de Resultados

### Estados de Prueba

| Estado | Icono | Significado |
|--------|-------|-------------|
| ⚪ Pendiente | `○` | No ejecutada |
| 🔵 Ejecutando | `⟳` | En proceso |
| ✅ Aprobada | `✓` | Pasó correctamente |
| ❌ Fallida | `✗` | No pasó validación |

### Colores en la Interfaz

- 🟢 **Verde**: Resultados positivos, pruebas aprobadas
- 🔴 **Rojo**: Errores, pruebas fallidas
- 🟡 **Amarillo**: Advertencias, casos límite
- 🔵 **Azul**: Información general, prueba en ejecución

## 🎯 Interpretación de Estadísticas

```
Total de Pruebas: 19
Aprobadas: 19
Fallidas: 0
Tasa de Éxito: 100%
```

- **Total**: Suma de todas las pruebas ejecutadas
- **Aprobadas**: Pruebas que pasaron correctamente
- **Fallidas**: Pruebas que no cumplieron expectativas
- **Tasa de Éxito**: Porcentaje de aprobación (meta: 100%)

## 🐛 Depuración de Errores

Si una prueba falla:

1. **Revisar el mensaje de error** en la interfaz o consola
2. **Verificar el código de validación** en `main.js` (función `validateRegistrationForm`)
3. **Comprobar los datos de prueba** en `test-form.js`
4. **Ejecutar la prueba específica** individualmente:
   ```javascript
   FormTests.runTestByName("nombre de la prueba")
   ```

## 📝 Agregar Nuevas Pruebas

Para agregar una nueva prueba, edita `assets/js/test-form.js`:

```javascript
// En la sección correspondiente (validCases, invalidCases, edgeCases)
{
    name: 'Nombre descriptivo de la prueba',
    data: {
        fullName: 'Valor de prueba',
        documentType: 'dni',
        documentNumber: '12345678',
        email: 'test@test.com',
        phone: '987654321',
        origin: 'Lima',
        category: 'visitante',
        comments: '',
        terms: true
    },
    expectedResult: 'success' // o 'error'
    // Si esperas error:
    expectedError: 'texto del error esperado'
}
```

## ✅ Checklist de Validación

Antes de publicar a producción, asegúrate de que:

- [ ] Todas las pruebas pasan (100% success rate)
- [ ] Se validan correctamente los 4 tipos de documentos
- [ ] Los mensajes de error son claros y en español
- [ ] La validación funciona en tiempo real en el formulario
- [ ] Se manejan correctamente los caracteres especiales (ñ, acentos)
- [ ] Los campos requeridos están marcados correctamente
- [ ] El checkbox de términos es obligatorio

## 🚨 Errores Comunes y Soluciones

### Error: "Función validateRegistrationForm no está disponible"
**Solución**: Asegúrate de que `main.js` esté cargado antes de `test-form.js`

### Error: "Formulario no encontrado"
**Solución**: Verifica que exista un elemento con `id="registrationForm"` en el HTML

### Las pruebas no se ejecutan
**Solución**: Abre la consola del navegador (F12) y verifica si hay errores de JavaScript

## 📞 Soporte

Para reportar problemas o sugerencias:
- Revisa los logs en la consola del navegador
- Verifica que estés usando una versión moderna del navegador
- Comprueba que todos los archivos JS estén en su lugar

## 🎓 Buenas Prácticas

1. **Ejecuta las pruebas después de cada cambio** en la lógica de validación
2. **Mantén la tasa de éxito al 100%** antes de hacer commits
3. **Agrega pruebas nuevas** cuando encuentres bugs
4. **Documenta casos especiales** en los comentarios del código
5. **Revisa periódicamente** que las validaciones sigan los estándares actuales

---

**Última actualización:** Mayo 2026  
**Versión:** 1.0.0  
**Compatibilidad:** Navegadores modernos (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
