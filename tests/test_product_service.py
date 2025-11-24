# tests/test_product_service.py

import sys
import os
# Agrega la carpeta del servicio al path para poder importar main.py
sys.path.append(os.path.join(os.path.dirname(__file__), "../product-service"))

from fastapi.testclient import TestClient
import main  # main.py del servicio

def test_health_endpoint():
    client = TestClient(main.app)
    response = client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "product-service"

