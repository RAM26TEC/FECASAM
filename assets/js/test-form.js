/**
 * FECASAM 2026 - Form Testing Suite
 * Script de pruebas automatizadas para el formulario de inscripción
 */

// ============================================
// CONFIGURACIÓN DE PRUEBAS
// ============================================

const TEST_CONFIG = {
    delayBetweenTests: 500,
    showProgressInConsole: true,
    stopOnFirstError: false
};

// ============================================
// CASOS DE PRUEBA
// ============================================

const testCases = {
    validCases: [
        {
            name: 'Inscripción válida con DNI',
            data: {
                fullName: 'Juan Carlos Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'juan.perez@gmail.com',
                phone: '987654321',
                origin: 'Lima, Perú',
                category: 'expositor-alpacas',
                comments: 'Primera vez participando',
                terms: true
            },
            expectedResult: 'success'
        },
        {
            name: 'Inscripción válida con RUC',
            data: {
                fullName: 'María Elena Torres García',
                documentType: 'ruc',
                documentNumber: '20123456789',
                email: 'maria.torres@empresa.com',
                phone: '999888777',
                origin: 'Cusco, Perú',
                category: 'expositor-artesania',
                comments: '',
                terms: true
            },
            expectedResult: 'success'
        },
        {
            name: 'Inscripción válida con Carné de Extranjería',
            data: {
                fullName: 'Carlos Alberto Rodríguez',
                documentType: 'ce',
                documentNumber: 'C001234567',
                email: 'carlos.rodriguez@hotmail.com',
                phone: '966555444',
                origin: 'Arequipa, Perú',
                category: 'visitante',
                comments: 'Interesado en conocer la feria',
                terms: true
            },
            expectedResult: 'success'
        },
        {
            name: 'Inscripción válida con Pasaporte',
            data: {
                fullName: 'Ana Sofía Mendoza Cruz',
                documentType: 'passport',
                documentNumber: 'ABC123456',
                email: 'ana.mendoza@yahoo.com',
                phone: '955444333',
                origin: 'Puno, Perú',
                category: 'investigador',
                comments: 'Investigación sobre camélidos sudamericanos',
                terms: true
            },
            expectedResult: 'success'
        }
    ],
    
    invalidCases: [
        {
            name: 'Nombre muy corto',
            data: {
                fullName: 'AB',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'nombre completo debe tener al menos 3 caracteres',
            expectedResult: 'error'
        },
        {
            name: 'Nombre con números',
            data: {
                fullName: 'Juan123 Pérez',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'nombre solo debe contener letras',
            expectedResult: 'error'
        },
        {
            name: 'DNI inválido (menos de 8 dígitos)',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '1234567',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'DNI debe tener exactamente 8 dígitos',
            expectedResult: 'error'
        },
        {
            name: 'DNI inválido (más de 8 dígitos)',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '123456789',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'DNI debe tener exactamente 8 dígitos',
            expectedResult: 'error'
        },
        {
            name: 'RUC inválido (menos de 11 dígitos)',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'ruc',
                documentNumber: '2012345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'RUC debe tener exactamente 11 dígitos',
            expectedResult: 'error'
        },
        {
            name: 'Email inválido (sin @)',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'testtest.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'correo electrónico válido',
            expectedResult: 'error'
        },
        {
            name: 'Email inválido (sin dominio)',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'correo electrónico válido',
            expectedResult: 'error'
        },
        {
            name: 'Teléfono muy corto',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '12345',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'teléfono válido',
            expectedResult: 'error'
        },
        {
            name: 'Sin tipo de documento',
            data: {
                fullName: 'Juan Pérez López',
                documentType: '',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedError: 'seleccionar un tipo de documento',
            expectedResult: 'error'
        },
        {
            name: 'Sin categoría',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: '',
                terms: true
            },
            expectedError: 'Seleccione una categoría',
            expectedResult: 'error'
        },
        {
            name: 'Sin aceptar términos',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: false
            },
            expectedError: 'aceptar los términos y condiciones',
            expectedResult: 'error'
        }
    ],
    
    edgeCases: [
        {
            name: 'Nombre con acentos y ñ',
            data: {
                fullName: 'José María Núñez Pérez',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'jose.nunez@gmail.com',
                phone: '987654321',
                origin: 'Cusco',
                category: 'visitante',
                terms: true
            },
            expectedResult: 'success'
        },
        {
            name: 'Email con caracteres especiales válidos',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'juan.perez+test@gmail.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedResult: 'success'
        },
        {
            name: 'Teléfono con exactamente 9 dígitos',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'Lima',
                category: 'visitante',
                terms: true
            },
            expectedResult: 'success'
        },
        {
            name: 'Procedencia muy larga',
            data: {
                fullName: 'Juan Pérez López',
                documentType: 'dni',
                documentNumber: '12345678',
                email: 'test@test.com',
                phone: '987654321',
                origin: 'San Juan de Lurigancho, Lima Metropolitana, Lima, Perú, América del Sur',
                category: 'visitante',
                terms: true
            },
            expectedResult: 'success'
        }
    ]
};

// ============================================
// RESULTADOS DE PRUEBAS
// ============================================

const testResults = {
    total: 0,
    passed: 0,
    failed: 0,
    errors: [],
    details: []
};

// ============================================
// FUNCIONES DE UTILIDAD
// ============================================

/**
 * Llenar el formulario con datos de prueba
 */
function fillForm(testData) {
    const form = document.getElementById('registrationForm');
    if (!form) {
        throw new Error('Formulario no encontrado');
    }
    
    // Llenar campos de texto
    if (testData.fullName !== undefined) {
        const input = form.querySelector('[name="fullName"]');
        if (input) input.value = testData.fullName;
    }
    
    if (testData.documentType !== undefined) {
        const select = form.querySelector('[name="documentType"]');
        if (select) select.value = testData.documentType;
    }
    
    if (testData.documentNumber !== undefined) {
        const input = form.querySelector('[name="documentNumber"]');
        if (input) input.value = testData.documentNumber;
    }
    
    if (testData.email !== undefined) {
        const input = form.querySelector('[name="email"]');
        if (input) input.value = testData.email;
    }
    
    if (testData.phone !== undefined) {
        const input = form.querySelector('[name="phone"]');
        if (input) input.value = testData.phone;
    }
    
    if (testData.origin !== undefined) {
        const input = form.querySelector('[name="origin"]');
        if (input) input.value = testData.origin;
    }
    
    if (testData.category !== undefined) {
        const select = form.querySelector('[name="category"]');
        if (select) select.value = testData.category;
    }
    
    if (testData.comments !== undefined) {
        const textarea = form.querySelector('[name="comments"]');
        if (textarea) textarea.value = testData.comments;
    }
    
    if (testData.terms !== undefined) {
        const checkbox = form.querySelector('[name="terms"]');
        if (checkbox) checkbox.checked = testData.terms;
    }
}

/**
 * Limpiar el formulario
 */
function clearForm() {
    const form = document.getElementById('registrationForm');
    if (form) {
        form.reset();
    }
}

/**
 * Crear FormData desde datos de prueba
 */
function createFormData(testData) {
    const formData = new FormData();
    
    for (const [key, value] of Object.entries(testData)) {
        if (key === 'terms') {
            if (value) {
                formData.append(key, 'on');
            }
        } else {
            formData.append(key, value);
        }
    }
    
    return formData;
}

/**
 * Esperar un tiempo determinado
 */
function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Imprimir resultado de prueba en consola
 */
function logTestResult(testName, passed, message = '') {
    const icon = passed ? '✓' : '✗';
    const color = passed ? 'color: #22c55e' : 'color: #ef4444';
    const prefix = passed ? 'PASS' : 'FAIL';
    
    console.log(`%c${icon} ${prefix}: ${testName}`, `${color}; font-weight: bold;`);
    
    if (message) {
        console.log(`  → ${message}`);
    }
}

/**
 * Imprimir resumen de resultados
 */
function printSummary() {
    console.log('\n' + '='.repeat(60));
    console.log('%c📊 RESUMEN DE PRUEBAS', 'font-size: 16px; font-weight: bold; color: #8B5E3C;');
    console.log('='.repeat(60));
    console.log(`Total de pruebas: ${testResults.total}`);
    console.log(`%c✓ Aprobadas: ${testResults.passed}`, 'color: #22c55e; font-weight: bold;');
    console.log(`%c✗ Fallidas: ${testResults.failed}`, 'color: #ef4444; font-weight: bold;');
    console.log(`%cÉxito: ${((testResults.passed / testResults.total) * 100).toFixed(1)}%`, 
                testResults.failed === 0 ? 'color: #22c55e; font-weight: bold;' : 'color: #f59e0b; font-weight: bold;');
    console.log('='.repeat(60) + '\n');
    
    if (testResults.failed > 0) {
        console.log('%c❌ PRUEBAS FALLIDAS:', 'color: #ef4444; font-weight: bold;');
        testResults.errors.forEach((error, index) => {
            console.log(`${index + 1}. ${error}`);
        });
    }
}

// ============================================
// EJECUTAR PRUEBAS
// ============================================

/**
 * Ejecutar una prueba individual
 */
async function runTest(testCase, category) {
    testResults.total++;
    
    try {
        clearForm();
        await wait(100);
        
        // Crear FormData para validación
        const formData = createFormData(testCase.data);
        
        // Importar función de validación del main.js
        if (typeof validateRegistrationForm === 'undefined') {
            throw new Error('Función validateRegistrationForm no está disponible');
        }
        
        const errors = validateRegistrationForm(formData);
        
        // Verificar resultado esperado
        if (testCase.expectedResult === 'success') {
            if (errors.length === 0) {
                testResults.passed++;
                testResults.details.push({
                    name: testCase.name,
                    category: category,
                    status: 'passed'
                });
                logTestResult(testCase.name, true, 'Validación correcta');
                return true;
            } else {
                testResults.failed++;
                const errorMsg = `${testCase.name} - Esperaba éxito pero obtuvo errores: ${errors.join(', ')}`;
                testResults.errors.push(errorMsg);
                testResults.details.push({
                    name: testCase.name,
                    category: category,
                    status: 'failed',
                    error: errorMsg
                });
                logTestResult(testCase.name, false, `Errores inesperados: ${errors[0]}`);
                return false;
            }
        } else if (testCase.expectedResult === 'error') {
            if (errors.length > 0) {
                // Verificar que el error esperado esté presente
                const expectedErrorFound = errors.some(error => 
                    error.toLowerCase().includes(testCase.expectedError.toLowerCase())
                );
                
                if (expectedErrorFound) {
                    testResults.passed++;
                    testResults.details.push({
                        name: testCase.name,
                        category: category,
                        status: 'passed'
                    });
                    logTestResult(testCase.name, true, `Error detectado correctamente: ${errors[0]}`);
                    return true;
                } else {
                    testResults.failed++;
                    const errorMsg = `${testCase.name} - Error esperado: "${testCase.expectedError}", pero obtuvo: "${errors[0]}"`;
                    testResults.errors.push(errorMsg);
                    testResults.details.push({
                        name: testCase.name,
                        category: category,
                        status: 'failed',
                        error: errorMsg
                    });
                    logTestResult(testCase.name, false, `Error incorrecto: ${errors[0]}`);
                    return false;
                }
            } else {
                testResults.failed++;
                const errorMsg = `${testCase.name} - Esperaba error pero la validación pasó`;
                testResults.errors.push(errorMsg);
                testResults.details.push({
                    name: testCase.name,
                    category: category,
                    status: 'failed',
                    error: errorMsg
                });
                logTestResult(testCase.name, false, 'No se detectó el error esperado');
                return false;
            }
        }
        
    } catch (error) {
        testResults.failed++;
        const errorMsg = `${testCase.name} - Error en ejecución: ${error.message}`;
        testResults.errors.push(errorMsg);
        testResults.details.push({
            name: testCase.name,
            category: category,
            status: 'failed',
            error: errorMsg
        });
        logTestResult(testCase.name, false, `Error: ${error.message}`);
        return false;
    }
}

/**
 * Ejecutar todas las pruebas
 */
async function runAllTests() {
    console.clear();
    console.log('%c🧪 FECASAM 2026 - PRUEBAS DE FORMULARIO', 'font-size: 18px; font-weight: bold; color: #8B5E3C; background: #F5E6D3; padding: 10px;');
    console.log('Iniciando suite de pruebas...\n');
    
    // Resetear resultados
    testResults.total = 0;
    testResults.passed = 0;
    testResults.failed = 0;
    testResults.errors = [];
    testResults.details = [];
    
    // Pruebas válidas
    console.log('%c✅ CASOS VÁLIDOS', 'font-size: 14px; font-weight: bold; color: #22c55e; margin-top: 10px;');
    console.log('─'.repeat(60));
    for (const testCase of testCases.validCases) {
        await runTest(testCase, 'valid');
        await wait(TEST_CONFIG.delayBetweenTests);
        
        if (TEST_CONFIG.stopOnFirstError && testResults.failed > 0) break;
    }
    
    // Pruebas inválidas
    console.log('\n%c❌ CASOS INVÁLIDOS', 'font-size: 14px; font-weight: bold; color: #ef4444;');
    console.log('─'.repeat(60));
    for (const testCase of testCases.invalidCases) {
        await runTest(testCase, 'invalid');
        await wait(TEST_CONFIG.delayBetweenTests);
        
        if (TEST_CONFIG.stopOnFirstError && testResults.failed > 0) break;
    }
    
    // Casos límite
    console.log('\n%c⚠️  CASOS LÍMITE', 'font-size: 14px; font-weight: bold; color: #f59e0b;');
    console.log('─'.repeat(60));
    for (const testCase of testCases.edgeCases) {
        await runTest(testCase, 'edge');
        await wait(TEST_CONFIG.delayBetweenTests);
        
        if (TEST_CONFIG.stopOnFirstError && testResults.failed > 0) break;
    }
    
    // Imprimir resumen
    printSummary();
    
    // Limpiar formulario al final
    clearForm();
    
    return testResults;
}

/**
 * Ejecutar una prueba específica por nombre
 */
async function runTestByName(testName) {
    console.clear();
    console.log(`%c🔍 Ejecutando prueba: ${testName}`, 'font-size: 14px; font-weight: bold; color: #3b82f6;');
    
    const allTests = [
        ...testCases.validCases,
        ...testCases.invalidCases,
        ...testCases.edgeCases
    ];
    
    const testCase = allTests.find(t => t.name.toLowerCase().includes(testName.toLowerCase()));
    
    if (!testCase) {
        console.log('%c✗ Prueba no encontrada', 'color: #ef4444; font-weight: bold;');
        return;
    }
    
    const category = testCases.validCases.includes(testCase) ? 'valid' :
                     testCases.invalidCases.includes(testCase) ? 'invalid' : 'edge';
    
    await runTest(testCase, category);
}

// ============================================
// EXPORTAR FUNCIONES
// ============================================

// Hacer disponibles las funciones globalmente
window.FormTests = {
    runAllTests,
    runTestByName,
    testCases,
    testResults
};

// ============================================
// AUTO-EJECUTAR AL CARGAR
// ============================================

console.log('%c📋 Script de pruebas cargado correctamente', 'color: #22c55e; font-weight: bold;');
console.log('%cEjecuta las siguientes funciones:', 'color: #666;');
console.log('  • FormTests.runAllTests() - Ejecutar todas las pruebas');
console.log('  • FormTests.runTestByName("nombre") - Ejecutar una prueba específica');
console.log('  • FormTests.testCases - Ver casos de prueba disponibles');
console.log('  • FormTests.testResults - Ver resultados de la última ejecución\n');
