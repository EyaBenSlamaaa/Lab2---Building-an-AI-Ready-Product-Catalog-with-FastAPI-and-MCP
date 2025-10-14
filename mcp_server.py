# mcp_server.py
import sys
from pathlib import Path
from typing import List
from fastmcp import FastMCP
from main import products_db  # assuming products_db is a list of Product objects

# Ensure project root is in the Python path
sys.path.append(str(Path(__file__).parent))

# Initialize FastMCP
mcp = FastMCP(name="Product Catalog MCP Server")

@mcp.tool()
def list_products() -> List[dict]:
    """List all available products with their ID, name, price, and description."""
    return [product.model_dump() for product in products_db]

@mcp.tool()
def get_product(product_id: int) -> dict:
    """Retrieve details of a specific product by its ID."""
    for product in products_db:
        if product.id == product_id:
            return product.model_dump()
    return {"error": "Product not found"}

if __name__ == "__main__":
    print("Starting MCP server ...")
    mcp.run()  # No host/port arguments
