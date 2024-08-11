"""Migration: adding new vertex"""
                       
"""
version id: versions/20240810001920_adding_new_vertex.py 
"""

def upgrade():
    ddl_upgrade = """
    DROP JOB tg_migrator_upgrade_20240810001920
    CREATE  SCHEMA_CHANGE JOB tg_migrator_upgrade_20240810001920 {
        ADD VERTEX test (PRIMARY_ID id STRING) WITH primary_id_as_attribute="true";
        
    }
    RUN SCHEMA_CHANGE JOB tg_migrator_upgrade_20240810001920
    """
    return ddl_upgrade

def downgrade():
    ddl_downgrade = """
    DROP JOB tg_migrator_downgrade_20240810001920
    CREATE  SCHEMA_CHANGE JOB tg_migrator_downgrade_20240810001920  {
        DROP VERTEX test;
        
    }
    RUN SCHEMA_CHANGE JOB tg_migrator_downgrade_20240810001920 
    """
    return ddl_downgrade
                
                
                