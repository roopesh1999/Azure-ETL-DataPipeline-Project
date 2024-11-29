USE gold_db
GO
CREATE OR ALTER PROC CreateSqlServerlessViewGold @view_name NVARCHAR(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)
    SET @statement = N'CREATE OR ALTER VIEW ' + @view_name + ' AS 
        SELECT
            *
        FROM
            OPENROWSET(
                BULK ''https://etldatalakegen2roopesh.dfs.core.windows.net/gold-layer/SalesLT/' + @view_name + '/'',
                FORMAT = ''DELTA''
        ) AS [result]
    '
EXEC (@statement)

END
GO
