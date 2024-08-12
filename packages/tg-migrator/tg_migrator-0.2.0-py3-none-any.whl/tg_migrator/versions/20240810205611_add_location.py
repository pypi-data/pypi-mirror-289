"""Migration: add location"""
                       
"""
version id: 20240810205611_add_location.py 
"""

def upgrade():
    ddl_upgrade = """
    DROP JOB tg_migrator_upgrade_20240810205611
    CREATE  SCHEMA_CHANGE JOB tg_migrator_upgrade_20240810205611 {
        ADD VERTEX Location (PRIMARY_ID id STRING) WITH primary_id_as_attribute="true";
       
    }
    RUN SCHEMA_CHANGE JOB tg_migrator_upgrade_20240810205611
    """
    return ddl_upgrade

def downgrade():
    ddl_downgrade = """
    DROP JOB tg_migrator_downgrade_20240810205611
    CREATE  SCHEMA_CHANGE JOB tg_migrator_downgrade_20240810205611  {
        DROP VERTEX Location;
        
    }
    RUN SCHEMA_CHANGE JOB tg_migrator_downgrade_20240810205611 
    """
    return ddl_downgrade
                
                
                