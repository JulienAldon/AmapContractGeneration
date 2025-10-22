from src import generate_contract_template
import io

def test_generate_custom_shipments():
    with open('tests/files/test_template.odt', 'rb') as f:
        template = io.BytesIO(f.read())
    
    document = generate_contract_template.create_document_from_template(template)
    informations = {
        'contract_type': 'Porc-Agneau', 
        'contract_season': 'Hiver-2025',
        'shipment_number': '1',
        'custom_shipment': 'true',
        'productor_name': 'Dominique',
        'productor_address': 'oui',
        'productor_payment': 'DESFARGES',
        'referer_email': 'julien.aldon@gmail.com',
        'referer_name': 'julien',
        'contract_date_start': '2025-03-12',
        'contract_date_end': '2025-04-11',
        'custom_shipment': True,
        'shipments': ['2023-10-10', '2024-10-10', '2024-11-10', '2024-12-10'],
        'products': [
            {'name': 'Porc-Agneau Petit', 'price': '13€', 'pricekg': '10€', 'weight':'1.5kg à 1.7kg', 'unit': 'panier', 'format': 'recurrent'}, 
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
        ]
    }
    generate_contract_template.generate_contract_template(document, informations)

    document.save('tests/output/test_custom_shipments.odt')

def test_generate_basic_shipments():
    with open('tests/files/test_template.odt', 'rb') as f:
        template = io.BytesIO(f.read())
    
    document = generate_contract_template.create_document_from_template(template)
    informations = {
        'contract_type': 'Porc-Agneau', 
        'contract_season': 'Hiver-2025',
        'shipment_number': '1',
        'custom_shipment': 'true',
        'productor_name': 'Dominique',
        'productor_address': 'oui',
        'productor_payment': 'DESFARGES',
        'referer_email': 'julien.aldon@gmail.com',
        'referer_name': 'julien',
        'contract_date_start': '2025-03-12',
        'contract_date_end': '2025-04-11',
        'custom_shipment': False,
        'shipments': ['2023-10-10', '2024-10-10', '2024-11-10', '2024-12-10'],
        'products': [
            {'name': 'Porc-Agneau Petit', 'price': '13€', 'pricekg': '10€', 'weight':'1.5kg à 1.7kg', 'unit': 'panier', 'format': 'recurrent'}, 
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
        ]
    }
    generate_contract_template.generate_contract_template(document, informations)

    document.save('tests/output/test_generate_basic_shipments.odt')

def test_generate_custom_shipments_with_oneshot():
    with open('tests/files/test_template.odt', 'rb') as f:
        template = io.BytesIO(f.read())
    
    document = generate_contract_template.create_document_from_template(template)
    informations = {
        'contract_type': 'Porc-Agneau', 
        'contract_season': 'Hiver-2025',
        'shipment_number': '1',
        'custom_shipment': 'true',
        'productor_name': 'Dominique',
        'productor_address': 'oui',
        'productor_payment': 'DESFARGES',
        'referer_email': 'julien.aldon@gmail.com',
        'referer_name': 'julien',
        'contract_date_start': '2025-03-12',
        'contract_date_end': '2025-04-11',
        'custom_shipment': True,
        'shipments': ['2023-10-10', '2024-10-10', '2024-11-10', '2024-12-10'],
        'products': [
            {'name': 'Porc-Agneau Petit', 'price': '13€', 'pricekg': '10€', 'weight':'1.5kg à 1.7kg', 'unit': 'panier', 'format': 'recurrent'}, 
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Tranches de foie', 'price': '15€', 'pricekg': '12€', 'weight':'150 grammes', 'unit': 'grammes', 'format': 'oneshot'},
            {'name': 'Boudin', 'price': '15€', 'pricekg': '12€', 'weight':'200 grammes', 'unit': 'grammes', 'format': 'oneshot'}
        ]
    }
    generate_contract_template.generate_contract_template(document, informations)

    document.save('tests/output/test_generate_custom_shipments_with_oneshot.odt')

def test_generate_basic_shipments_with_oneshot():
    with open('tests/files/test_template.odt', 'rb') as f:
        template = io.BytesIO(f.read())
    
    document = generate_contract_template.create_document_from_template(template)
    informations = {
        'contract_type': 'Porc-Agneau', 
        'contract_season': 'Hiver-2025',
        'shipment_number': '1',
        'custom_shipment': 'true',
        'productor_name': 'Dominique',
        'productor_address': 'oui',
        'productor_payment': 'DESFARGES',
        'referer_email': 'julien.aldon@gmail.com',
        'referer_name': 'julien',
        'contract_date_start': '2025-03-12',
        'contract_date_end': '2025-04-11',
        'custom_shipment': False,
        'shipments': ['2023-10-10', '2024-10-10', '2024-11-10', '2024-12-10'],
        'products': [
            {'name': 'Porc-Agneau Petit', 'price': '13€', 'pricekg': '10€', 'weight':'1.5kg à 1.7kg', 'unit': 'panier', 'format': 'recurrent'}, 
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Porc-Agneau Moyen', 'price': '17€', 'pricekg': '9€', 'weight':'2.5kg à 2.7kg', 'unit': 'panier', 'format': 'recurrent'},
            {'name': 'Tranches de foie', 'price': '15€', 'pricekg': '12€', 'weight':'150 grammes', 'unit': 'grammes', 'format': 'oneshot'},
            {'name': 'Boudin', 'price': '15€', 'pricekg': '12€', 'weight':'200 grammes', 'unit': 'grammes', 'format': 'oneshot'}
        ]
    }
    generate_contract_template.generate_contract_template(document, informations)

    document.save('tests/output/test_generate_basic_shipments_with_oneshot.odt')


def main():
    test_generate_custom_shipments()
    test_generate_basic_shipments()
    test_generate_basic_shipments_with_oneshot()
    test_generate_custom_shipments_with_oneshot()

if __name__ == "__main__":
    main()
