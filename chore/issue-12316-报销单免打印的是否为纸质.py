import ListUtils

if __name__ == '__main__':
    docCodes = []
    with open("/Users/vicoko/workspace/pycharm/scavenger/chore/12316", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            docCodes.append("'{}'".format(line.split()[1]))

    for codeList in ListUtils.partition(docCodes, 1000):
        sql = '''UPDATE ea_document_1178518358079496194 AS ed
SET
    is_paper           = FALSE,
    last_modified_by   = -1,
    last_modified_date = '2022-11-02 00:00:00'
WHERE
        ed.id IN (
        SELECT DISTINCT (document_id)
        FROM
            ea_document_field_value_1178518358079496194 AS edfv
        WHERE
                edfv.field_id IN (SELECT eff.id
                                  FROM
                                      ea_form                      AS ef
                                          INNER JOIN ea_form_field AS eff ON ef.id = eff.form_id
                                  WHERE
                                        ef.code IN ('EXPENSE_REPORT', 'OTHER_ATTACHMENT')
                                    AND ef.is_deleted = FALSE
                                    AND ef.tenant_id = '1178518358079496194'
                                    AND eff.code = 'DOC_CODE'
                                    AND eff.is_deleted = FALSE
                                    AND eff.tenant_id = '1178518358079496194')
          AND   edfv.value IN ({})
          AND   edfv.is_deleted = FALSE
    );'''.format(','.join(codeList))
        print(sql)
        print('\n')

