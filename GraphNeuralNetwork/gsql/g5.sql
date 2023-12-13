CREATE QUERY detectPattern(VERTEX<Account> nodeA, VERTEX<Account> nodeB) FOR GRAPH YourGraphName {
  TYPEDEF TUPLE <VERTEX<Account> nodeA, VERTEX<Account> muleAccount1, VERTEX<Account> muleAccount2, VERTEX<Account> nodeB> ResultTuple;
  ListAccum<VERTEX<Account>> @@muleAccounts;
  SetAccum<VERTEX<Account>> @@uniqueMuleAccounts;
  ListAccum<ResultTuple> @@results;

  // Start from Node A with AccountType = 'XA'
  Start = SELECT s FROM {nodeA:s} WHERE s.AccountType == 'XA';

  // First hop to any Mule Account (AccountType = 'IA')
  FirstHop = SELECT tgt
             FROM Start:s -(Transacting:e1)-> :tgt
             WHERE tgt.AccountType == 'IA';

  // Second hop to Node B from these Mule Accounts
  SecondHop = SELECT src, tgt
              FROM FirstHop:src -(Transacting:e2)-> nodeB:tgt
              WHERE tgt.AccountType == 'XA';

  // Collect all paths
  FOREACH path IN SecondHop DO
    @@muleAccounts += path.src;
    @@uniqueMuleAccounts += path.src;
  END;

  // Find distinct Mule Accounts and pair them
  FOREACH muleAccount1 IN @@uniqueMuleAccounts DO
    FOREACH muleAccount2 IN @@muleAccounts DO
      IF muleAccount1 != muleAccount2 THEN
        @@results += ResultTuple(nodeA, muleAccount1, muleAccount2, nodeB);
      END;
    END;
  END;

  PRINT @@results;
}
