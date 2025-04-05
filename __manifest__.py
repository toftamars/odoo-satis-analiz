{
    'name': 'Satis Analiz',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Satış analizleri için özel modül',
    'description': """
        Bu modül satış analizleri için özel raporlar ve analizler sunar.
        Özellikler:
        - Detaylı satış raporları
        - Müşteri analizleri
        - Ürün performans analizleri
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_analysis_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
} 