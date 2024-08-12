"""Migration: creating socail graph"""
                       
"""
version id: 20240810204221_creating_socail_graph.py 
"""

def upgrade():
    ddl_upgrade = """
    DROP JOB tg_migrator_upgrade_20240810204221
    CREATE  SCHEMA_CHANGE JOB tg_migrator_upgrade_20240810204221 {
        ADD VERTEX Person (PRIMARY_ID id STRING, name STRING) WITH primary_id_as_attribute="true";
        
    }
    RUN SCHEMA_CHANGE JOB tg_migrator_upgrade_20240810204221
    """
    return ddl_upgrade

def downgrade():
    ddl_downgrade = """
    DROP JOB tg_migrator_downgrade_20240810204221
    CREATE  SCHEMA_CHANGE JOB tg_migrator_downgrade_20240810204221  {
        DROP VERTEX Person;
    }
    RUN SCHEMA_CHANGE JOB tg_migrator_downgrade_20240810204221 
    """
    return ddl_downgrade
                
                
                