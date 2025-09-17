# Auto-generated MCP wrappers
from fastmcp import FastMCP
from typing import List
from tooluniverse.execute_function import ToolUniverse

mcp = FastMCP('ToolUniverse MCP', stateless_http=True)
engine = ToolUniverse()
engine.load_tools()

@mcp.tool()
def get_joint_associated_diseases_by_HPO_ID_list(
    HPO_ID_list: List[str], 
    limit: int, 
    offset: int
) -> dict:
    """
    根据HPO ID列表获取关联的疾病信息
    
    Args:
        HPO_ID_list: HPO表型ID列表
        limit: 返回结果数量限制
        offset: 结果偏移量
    
    Returns:
        包含关联疾病信息的字典
    """
    diseases = engine.run_one_function({
        "name": "get_joint_associated_diseases_by_HPO_ID_list",
        "arguments": {
            "HPO_ID_list": HPO_ID_list,
            "limit": limit,
            "offset": offset
        }
    })
    return {"associated_diseases": diseases}


@mcp.tool()
def get_phenotype_by_HPO_ID(id: str) -> dict:
    """
    根据HPO ID获取表型信息
    
    Args:
        id: HPO表型ID
    
    Returns:
        包含表型信息的字典
    """
    return engine.run_one_function({
        "name": "get_phenotype_by_HPO_ID",
        "arguments": {
            "id": id
        }
    })


@mcp.tool()
def get_HPO_ID_by_phenotype(
    query: str, 
    limit: int, 
    offset: int
) -> dict:
    """
    根据表型查询获取HPO ID
    
    Args:
        query: 表型查询字符串
        limit: 返回结果数量限制
        offset: 结果偏移量
    
    Returns:
        包含HPO ID信息的字典
    """
    return engine.run_one_function({
        "name": "get_HPO_ID_by_phenotype",
        "arguments": {
            "query": query,
            "limit": limit,
            "offset": offset
        }
    })


@mcp.tool()
def OpenTargets_get_associated_targets_by_disease_efoId(efoId: str) -> dict:
    """
    根据疾病EFO ID获取关联的靶点信息
    
    Args:
        efoId: 疾病的EFO标识符
    
    Returns:
        包含关联靶点信息的字典
    """
    return engine.run_one_function({
        "name": "OpenTargets_get_associated_targets_by_disease_efoId",
        "arguments": {
            "efoId": efoId
        }
    })


@mcp.tool()
def OpenTargets_get_diseases_phenotypes_by_target_ensembl(ensemblId: str) -> dict:
    """
    根据靶点Ensembl ID获取关联的疾病和表型信息
    
    Args:
        ensemblId: 靶点的Ensembl标识符
    
    Returns:
        包含关联疾病和表型信息的字典
    """
    return engine.run_one_function({
        "name": "OpenTargets_get_diseases_phenotypes_by_target_ensembl",
        "arguments": {
            "ensemblId": ensemblId
        }
    })


@mcp.tool()
def OpenTargets_target_disease_evidence(
    efoId: str, 
    ensemblId: str
) -> dict:
    """
    获取靶点与疾病之间的证据信息
    
    Args:
        efoId: 疾病的EFO标识符
        ensemblId: 靶点的Ensembl标识符
    
    Returns:
        包含靶点-疾病证据信息的字典
    """
    return engine.run_one_function({
        "name": "OpenTargets_target_disease_evidence",
        "arguments": {
            "efoId": efoId,
            "ensemblId": ensemblId
        }
    })


@mcp.tool()
def OpenTargets_get_associated_phenotypes_by_disease_efoId(efoId: str) -> dict:
    """
    根据疾病EFO ID获取关联的表型信息
    
    Args:
        efoId: 疾病的EFO标识符
    
    Returns:
        包含关联表型信息的字典
    """
    return engine.run_one_function({
        "name": "OpenTargets_get_associated_phenotypes_by_disease_efoId",
        "arguments": {
            "efoId": efoId
        }
    })


@mcp.tool()
def OpenTargets_get_disease_id_description_by_name(diseaseName: str) -> dict:
    """
    根据疾病名称获取疾病ID和描述信息
    
    Args:
        diseaseName: 疾病名称
    
    Returns:
        包含疾病ID和描述信息的字典
    """
    return engine.run_one_function({
        "name": "OpenTargets_get_disease_id_description_by_name",
        "arguments": {
            "diseaseName": diseaseName
        }
    })

def run_server():
    mcp.run(transport='streamable-http', host='127.0.0.1', port=8000)

def run_claude_desktop():
    print("Starting ToolUniverse MCP server...")
    mcp.run(transport='stdio')
