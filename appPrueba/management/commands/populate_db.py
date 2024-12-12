from django.core.management.base import BaseCommand
#from .models import Product, Category
from ...models import Product, Category
class Command(BaseCommand):
    help = 'Popula la base de datos con datos de ejemplo'

    def handle(self, *args, **options):
        # Crea las categorías
        categorias = [
            {'name': 'Reparación de Hardware'},
            {'name': 'Instalación de Software'},
            {'name': 'Mantenimiento Preventivo'},
            {'name': 'Configuración de Redes'},
            {'name': 'Asesoramiento y Consultoría'},
            {'name': 'Formación y Capacitación'}
        ]

        # Crea los productos para cada categoría
        productos = [
            [
                {'name': 'Reparación de discos duros', 'description': 'Reparación de discos duros para recuperar datos y mejorar la velocidad del sistema.', 'price': 100, 'image': 'reparacion_discos_duros.jpg'},
                {'name': 'Reparación de tarjetas gráficas', 'description': 'Reparación de tarjetas gráficas para mejorar la calidad de la imagen y el rendimiento del sistema.', 'price': 150, 'image': 'reparacion_tarjetas_graficas.jpg'},
                {'name': 'Reparación de fuentes de poder', 'description': 'Reparación de fuentes de poder para garantizar la estabilidad y seguridad del sistema.', 'price': 120, 'image': 'reparacion_fuentes_poder.jpg'},
                {'name': 'Reparación de placas base', 'description': 'Reparación de placas base para mejorar la velocidad y estabilidad del sistema.', 'price': 180, 'image': 'reparacion_placas_base.jpg'},
                {'name': 'Reparación de memoria RAM', 'description': 'Reparación de memoria RAM para mejorar la velocidad y capacidad del sistema.', 'price': 90, 'image': 'reparacion_memoria_ram.jpg'}
            ],
            [
                {'name': 'Instalación de sistemas operativos (Windows, macOS, Linux)', 'description': 'Instalación de sistemas operativos para mejorar la estabilidad y seguridad del sistema.', 'price': 100, 'image': 'instalacion_sistemas_operativos.jpg'},
                {'name': 'Instalación de software de oficina (Microsoft Office, LibreOffice)', 'description': 'Instalación de software de oficina para mejorar la productividad y eficiencia.', 'price': 150, 'image': 'instalacion_software_oficina.jpg'},
                {'name': 'Instalación de software de seguridad (antivirus, firewall)', 'description': 'Instalación de software de seguridad para proteger el sistema de amenazas.', 'price': 120, 'image': 'instalacion_software_seguridad.jpg'},
                {'name': 'Instalación de software de diseño gráfico (Adobe Creative Cloud)', 'description': 'Instalación de software de diseño gráfico para mejorar la creatividad y productividad.', 'price': 180, 'image': 'instalacion_software_diseno_grafico.jpg'}
            ],
            [
                {'name': 'Limpieza de virus y malware', 'description': 'Limpieza de virus y malware para proteger el sistema de amenazas.', 'price': 100, 'image': 'limpieza_virus_malware.jpg'},
                {'name': 'Actualización de software y drivers', 'description': 'Actualización de software y drivers para mejorar la estabilidad y seguridad del sistema.', 'price': 150, 'image': 'actualizacion_software_drivers.jpg'},
                {'name': 'Verificación de discos duros y memoria RAM', 'description': 'Verificación de discos duros y memoria RAM para mejorar la velocidad y capacidad del sistema.', 'price': 120, 'image': 'verificacion_discos_duros_memoria_ram.jpg'},
                {'name': 'Configuración de respaldo de datos', 'description': 'Configuración de respaldo de datos para proteger los datos importantes.', 'price': 180, 'image': 'configuracion_respaldo_datos.jpg'}
            ],
            [
                {'name': 'Configuración de routers y módems', 'description': 'Configuración de routers y módems para mejorar la velocidad y estabilidad de la conexión a Internet.', 'price': 100, 'image': 'configuracion_routers_modems.jpg'},
                {'name': 'Configuración de redes Wi-Fi', 'description': 'Configuración de redes Wi-Fi para mejorar la velocidad y estabilidad de la conexión a Internet.', 'price': 150, 'image': 'configuracion_redes_wifi.jpg'},
                {'name': 'Configuración de redes cableadas', 'description': 'Configuración de redes cableadas para mejorar la velocidad y estabilidad de la conexión a Internet. Esto incluye la configuración de switches, routers y otros dispositivos de red para garantizar una conexión segura y estable.', 'price': 120, 'image': 'configuracion_redes_cableadas.jpg'},
                {'name': 'Configuración de redes cableadas', 'description': 'Configuración de redes cableadas para mejorar la velocidad y estabilidad de la conexión a Internet.', 'price': 120, 'image': 'configuracion_redes_cableadas.jpg'},
                {'name': 'Configuración de servidores y clientes', 'description': 'Configuración de servidores y clientes para mejorar la velocidad y estabilidad de la conexión a Internet.', 'price': 180, 'image': 'configuracion_servidores_clientes.jpg'}
            ],
            [
                {'name': 'Asesoramiento sobre hardware y software', 'description': 'Asesoramiento sobre hardware y software para mejorar la eficiencia y productividad.', 'price': 100, 'image': 'asesoramiento_hardware_software.jpg'},
                {'name': 'Consultoría sobre seguridad informática', 'description': 'Consultoría sobre seguridad informática para proteger el sistema de amenazas.', 'price': 150, 'image': 'consultoria_seguridad_informatica.jpg'},
                {'name': 'Consultoría sobre redes y comunicaciones', 'description': 'Consultoría sobre redes y comunicaciones para mejorar la velocidad y estabilidad de la conexión a Internet.', 'price': 120, 'image': 'consultoria_redes_comunicaciones.jpg'},
                {'name': 'Asesoramiento sobre soluciones de respaldo de datos', 'description': 'Asesoramiento sobre soluciones de respaldo de datos para proteger los datos importantes.', 'price': 180, 'image': 'asesoramiento_soluciones_respaldo_datos.jpg'}
            ],
            [
                {'name': 'Cursos de formación en hardware y software', 'description': 'Cursos de formación en hardware y software para mejorar la eficiencia y productividad.', 'price': 100, 'image': 'cursos_formacion_hardware_software.jpg'},
                {'name': 'Talleres de capacitación en seguridad informática', 'description': 'Talleres de capacitación en seguridad informática para proteger el sistema de amenazas.', 'price': 150, 'image': 'talleres_capacitacion_seguridad_informatica.jpg'},
                {'name': 'Cursos de formación en redes y comunicaciones', 'description': 'Cursos de formación en redes y comunicaciones para mejorar la velocidad y estabilidad de la conexión a Internet.', 'price': 120, 'image': 'cursos_formacion_redes_comunicaciones.jpg'},
                {'name': 'Cursos de formación en soluciones de respaldo de datos', 'description': 'Cursos de formación en soluciones de respaldo de datos para proteger los datos importantes.', 'price': 180, 'image': 'cursos_formacion_soluciones_respaldo_datos.jpg'}
            ]
        ]

        # Crea las categorías y productos
        for i, categoria in enumerate(categorias):
            categoria_obj = Category.objects.get_or_create(name=categoria['name'])[0]
            for producto in productos[i]:
                Product.objects.get_or_create(
                    name=producto['name'],
                    description=producto['description'],
                    price=producto['price'],
                    image=producto['image'],
                    category=categoria_obj
                )
