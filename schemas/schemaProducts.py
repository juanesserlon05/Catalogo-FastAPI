from typing import Optional
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="Producto", min_length=5, max_length=30)
    description: str = Field(default="Descripcion del producto", min_length=10, max_length=300)
    category:str = Field(default="Clean", min_length=2, max_length=20)
    units: int = Field(le=2022)

    # Configuracion de la documentacion
    class Config:
        model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "id": 1,
                        "name": "producto",
                        "description": "Descripcion del producto",
                        "category": "Categoría del producto",
                        "units": 0
                    }
                ]
            }
        }
