CREATE QUERY detectPattern() FOR GRAPH YourGraphName {
  TYPEDEF TUPLE <VERTEX<Account> nodeA, VERTEX<Account> muleAccount1, VERTEX<Account> muleAccount2, VERTEX<Account> nodeB> ResultTuple;
  SetAccum<VERTEX<Account>> @@muleAccounts;
  ListAccum<ResultTuple> @@results;

  // Select all accounts with AccountType = 'XA' as potential Node A and Node B
  NodeSet = {Account.*};
  NodeASet = SELECT s FROM NodeSet:s WHERE s.AccountType == 'XA';
  NodeBSet = SELECT s FROM NodeSet:s WHERE s.AccountType == 'XA';

  // Iterate over all pairs of Node A and Node B
  FOREACH nodeA IN NodeASet DO
    FOREACH nodeB IN NodeBSet DO
      IF nodeA != nodeB THEN
        // First hop to any Mule Account (AccountType = 'IA')
        FirstHop = SELECT tgt
                   FROM nodeA -(Transacting:e1)-> :tgt
                   WHERE tgt.AccountType == 'IA';
        ACCUM @@muleAccounts.clear(), @@muleAccounts += tgt;

        // Iterate over Mule Accounts to find second hop to Node B
        FOREACH muleAccount1 IN @@muleAccounts DO
          SecondHop1 = SELECT tgt
                       FROM muleAccount1 -(Transacting:e2)-> nodeB:tgt
                       WHERE tgt.AccountType == 'XA';

          // For each unique pair of Mule Accounts
          FOREACH muleAccount2 IN @@muleAccounts WHERE muleAccount1 != muleAccount2 DO
            SecondHop2 = SELECT tgt
                         FROM muleAccount2 -(Transacting:e2)-> nodeB:tgt
                         WHERE tgt.AccountType == 'XA';

            // If both hops reach Node B, add the result
            IF SecondHop1.size() > 0 AND SecondHop2.size() > 0 THEN
              @@results += ResultTuple(nodeA, muleAccount1, muleAccount2, nodeB);
            END;
          END;
        END;
      END;
    END;
  END;

  PRINT @@results;
}
