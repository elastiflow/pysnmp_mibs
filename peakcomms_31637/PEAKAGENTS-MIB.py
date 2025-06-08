# SNMP MIB module (PEAKAGENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKAGENTS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:01 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(peakNode,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "peakNode")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

peakAgents = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 100)
)
if mibBuilder.loadTexts:
    peakAgents.setRevisions(
        ("2016-10-10 09:00",
         "2016-08-24 09:00",
         "2016-07-25 09:00",
         "2016-05-23 09:00",
         "2016-04-27 09:00",
         "2016-04-14 09:00",
         "2016-04-04 09:00",
         "2016-03-11 09:00",
         "2016-03-02 09:00",
         "2015-12-03 09:00",
         "2015-10-21 09:00",
         "2015-09-24 09:00",
         "2015-09-22 09:00",
         "2015-09-17 09:00",
         "2015-09-15 09:00",
         "2015-07-17 12:00",
         "2015-04-28 12:00",
         "2015-03-07 12:00",
         "2015-01-23 12:00",
         "2014-12-28 12:00",
         "2014-07-31 09:00",
         "2014-07-18 09:00",
         "2014-07-16 09:00",
         "2014-06-17 09:00",
         "2014-06-13 09:00",
         "2014-05-29 09:00",
         "2014-05-23 09:00",
         "2014-04-28 09:00",
         "2014-04-14 09:00",
         "2014-03-06 09:00",
         "2014-02-07 09:00",
         "2014-01-07 09:00",
         "2013-12-18 12:00",
         "2013-10-10 12:00",
         "2013-10-03 12:00",
         "2013-09-12 12:00",
         "2013-08-20 12:00",
         "2013-06-25 12:00",
         "2013-05-21 12:00",
         "2013-05-14 12:00",
         "2013-04-05 12:00",
         "2013-04-04 12:00",
         "2013-02-20 12:00",
         "2013-01-02 12:00",
         "2012-12-11 12:00",
         "2012-10-29 12:00",
         "2012-09-27 12:00",
         "2012-07-30 12:00",
         "2012-07-03 12:00",
         "2012-05-24 12:00",
         "2012-03-30 12:00",
         "2012-03-16 12:00",
         "2012-03-05 12:00",
         "2012-02-15 12:00",
         "2012-01-31 12:00",
         "2012-01-20 12:00",
         "2011-12-09 12:00",
         "2011-12-08 12:00",
         "2011-11-30 12:00",
         "2011-11-24 12:00",
         "2011-11-01 12:00",
         "2011-08-03 12:00",
         "2011-07-27 12:00",
         "2011-06-30 12:00",
         "2011-06-10 12:00",
         "2011-05-05 12:00",
         "2011-03-23 12:00",
         "2011-03-07 12:00",
         "2011-01-05 12:00",
         "2010-12-09 12:00",
         "2010-12-08 12:00",
         "2010-11-17 12:00",
         "2010-10-04 12:00",
         "2010-08-19 12:00",
         "2010-08-18 12:00",
         "2010-08-06 13:00",
         "2010-06-25 09:00",
         "2010-06-21 09:00",
         "2010-06-02 10:00",
         "2010-05-19 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

p7000_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 0)
)
if mibBuilder.loadTexts:
    p7000_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7000_Agent.setStatus(
        "current"
    )

p7000W_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1)
)
if mibBuilder.loadTexts:
    p7000W_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7000W_Agent.setStatus(
        "current"
    )

p7000_140MHZ_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2)
)
if mibBuilder.loadTexts:
    p7000_140MHZ_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7000_140MHZ_Agent.setStatus(
        "current"
    )

p7000W_140MHz_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3)
)
if mibBuilder.loadTexts:
    p7000W_140MHz_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7000W_140MHz_Agent.setStatus(
        "current"
    )

p7020SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 4)
)
if mibBuilder.loadTexts:
    p7020SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7020SA_Agent.setStatus(
        "current"
    )

p7020_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5)
)
if mibBuilder.loadTexts:
    p7020_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7020_Agent.setStatus(
        "current"
    )

p7020_140MHz_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6)
)
if mibBuilder.loadTexts:
    p7020_140MHz_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7020_140MHz_Agent.setStatus(
        "current"
    )

p7000i_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 7)
)
if mibBuilder.loadTexts:
    p7000i_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7000i_Agent.setStatus(
        "current"
    )

p7000SM = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8)
)
if mibBuilder.loadTexts:
    p7000SM.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7000SM.setStatus(
        "current"
    )

p7000i_1a_1b_5a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 10)
)
if mibBuilder.loadTexts:
    p7000i_1a_1b_5a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7000i_1a_1b_5a_Agent.setStatus(
        "current"
    )

p7000_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 15)
)
if mibBuilder.loadTexts:
    p7000_5_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7000_5_Agent.setStatus(
        "current"
    )

p7001_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1000)
)
if mibBuilder.loadTexts:
    p7001_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7001_Agent.setStatus(
        "current"
    )

p7001_140MHz_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1001)
)
if mibBuilder.loadTexts:
    p7001_140MHz_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7001_140MHz_Agent.setStatus(
        "current"
    )

p7001S1_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1002)
)
if mibBuilder.loadTexts:
    p7001S1_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001S1_Agent.setStatus(
        "current"
    )

p7001_P701_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1003)
)
if mibBuilder.loadTexts:
    p7001_P701_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001_P701_Agent.setStatus(
        "current"
    )

p7001D_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1004)
)
if mibBuilder.loadTexts:
    p7001D_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7001D_Agent.setStatus(
        "current"
    )

p7001D_140MHz_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1005)
)
if mibBuilder.loadTexts:
    p7001D_140MHz_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7001D_140MHz_Agent.setStatus(
        "current"
    )

p7003A_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1006)
)
if mibBuilder.loadTexts:
    p7003A_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7003A_Agent.setStatus(
        "current"
    )

p7007S_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1007)
)
if mibBuilder.loadTexts:
    p7007S_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7007S_Agent.setStatus(
        "current"
    )

p7010_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1008)
)
if mibBuilder.loadTexts:
    p7010_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7010_Agent.setStatus(
        "current"
    )

p7011_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1009)
)
if mibBuilder.loadTexts:
    p7011_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7011_Agent.setStatus(
        "current"
    )

p7012_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1010)
)
if mibBuilder.loadTexts:
    p7012_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7012_Agent.setStatus(
        "current"
    )

p7021C_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1011)
)
if mibBuilder.loadTexts:
    p7021C_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7021C_Agent.setStatus(
        "current"
    )

p7021SO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1012)
)
if mibBuilder.loadTexts:
    p7021SO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7021SO_Agent.setStatus(
        "current"
    )

p7035_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1013)
)
if mibBuilder.loadTexts:
    p7035_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7035_Agent.setStatus(
        "current"
    )

p7701_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1014)
)
if mibBuilder.loadTexts:
    p7701_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7701_Agent.setStatus(
        "current"
    )

p5003_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1015)
)
if mibBuilder.loadTexts:
    p5003_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p5003_Agent.setStatus(
        "current"
    )

ibdh340_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1016)
)
if mibBuilder.loadTexts:
    ibdh340_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh340_Agent.setStatus(
        "current"
    )

ibdh340_ATT_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1017)
)
if mibBuilder.loadTexts:
    ibdh340_ATT_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh340_ATT_Agent.setStatus(
        "current"
    )

ibdh1225_10b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1018)
)
if mibBuilder.loadTexts:
    ibdh1225_10b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1225_10b_Agent.setStatus(
        "current"
    )

p7701SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1019)
)
if mibBuilder.loadTexts:
    p7701SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7701SA_Agent.setStatus(
        "current"
    )

p7007_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1020)
)
if mibBuilder.loadTexts:
    p7007_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7007_Agent.setStatus(
        "current"
    )

p7001_1d_7_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1021)
)
if mibBuilder.loadTexts:
    p7001_1d_7_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001_1d_7_Agent.setStatus(
        "current"
    )

p7001R_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1026)
)
if mibBuilder.loadTexts:
    p7001R_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001R_Agent.setStatus(
        "current"
    )

ibdh3003_10b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1028)
)
if mibBuilder.loadTexts:
    ibdh3003_10b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh3003_10b_Agent.setStatus(
        "current"
    )

ibdh342_1db_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1030)
)
if mibBuilder.loadTexts:
    ibdh342_1db_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh342_1db_Agent.setStatus(
        "current"
    )

ibdh1072_1db_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1031)
)
if mibBuilder.loadTexts:
    ibdh1072_1db_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1072_1db_Agent.setStatus(
        "current"
    )

ibdh1172_1db_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1032)
)
if mibBuilder.loadTexts:
    ibdh1172_1db_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1172_1db_Agent.setStatus(
        "current"
    )

p7001_1d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1033)
)
if mibBuilder.loadTexts:
    p7001_1d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001_1d_Agent.setStatus(
        "current"
    )

ibdh2001_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1035)
)
if mibBuilder.loadTexts:
    ibdh2001_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh2001_Agent.setStatus(
        "current"
    )

ibdh2001_10a_11_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1036)
)
if mibBuilder.loadTexts:
    ibdh2001_10a_11_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh2001_10a_11_Agent.setStatus(
        "current"
    )

ibdh1225SM_10b_15SM_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1037)
)
if mibBuilder.loadTexts:
    ibdh1225SM_10b_15SM_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1225SM_10b_15SM_Agent.setStatus(
        "current"
    )

p7001DSA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1038)
)
if mibBuilder.loadTexts:
    p7001DSA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001DSA_Agent.setStatus(
        "current"
    )

ibdh2001_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1039)
)
if mibBuilder.loadTexts:
    ibdh2001_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh2001_10a_Agent.setStatus(
        "current"
    )

ibdh2001_11i_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1042)
)
if mibBuilder.loadTexts:
    ibdh2001_11i_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh2001_11i_Agent.setStatus(
        "current"
    )

p7701EDC_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1043)
)
if mibBuilder.loadTexts:
    p7701EDC_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7701EDC_Agent.setStatus(
        "current"
    )

ibdh340_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1044)
)
if mibBuilder.loadTexts:
    ibdh340_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh340_10a_Agent.setStatus(
        "current"
    )

pbd2001sl_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1045)
)
if mibBuilder.loadTexts:
    pbd2001sl_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbd2001sl_Agent.setStatus(
        "current"
    )

p7025bse_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1046)
)
if mibBuilder.loadTexts:
    p7025bse_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7025bse_Agent.setStatus(
        "current"
    )

p7007XH_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1047)
)
if mibBuilder.loadTexts:
    p7007XH_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7007XH_Agent.setStatus(
        "current"
    )

ibdh3000_2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1049)
)
if mibBuilder.loadTexts:
    ibdh3000_2_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh3000_2_Agent.setStatus(
        "current"
    )

ibdh1095_10b_SM_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1050)
)
if mibBuilder.loadTexts:
    ibdh1095_10b_SM_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1095_10b_SM_Agent.setStatus(
        "current"
    )

ibdh1225_10b_SM_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1051)
)
if mibBuilder.loadTexts:
    ibdh1225_10b_SM_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1225_10b_SM_Agent.setStatus(
        "current"
    )

p7001R_1SD_7_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1052)
)
if mibBuilder.loadTexts:
    p7001R_1SD_7_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001R_1SD_7_Agent.setStatus(
        "current"
    )

ibdh3003_10a_11c_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1055)
)
if mibBuilder.loadTexts:
    ibdh3003_10a_11c_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh3003_10a_11c_Agent.setStatus(
        "current"
    )

p7003CSNb_1d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1056)
)
if mibBuilder.loadTexts:
    p7003CSNb_1d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7003CSNb_1d_Agent.setStatus(
        "current"
    )

p7025A_1d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1057)
)
if mibBuilder.loadTexts:
    p7025A_1d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7025A_1d_Agent.setStatus(
        "current"
    )

p7003A_1d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1058)
)
if mibBuilder.loadTexts:
    p7003A_1d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7003A_1d_Agent.setStatus(
        "current"
    )

ibdh4004_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1059)
)
if mibBuilder.loadTexts:
    ibdh4004_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh4004_10a_Agent.setStatus(
        "current"
    )

p7011B_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1060)
)
if mibBuilder.loadTexts:
    p7011B_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7011B_Agent.setStatus(
        "current"
    )

ibdh450ST_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1061)
)
if mibBuilder.loadTexts:
    ibdh450ST_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh450ST_10a_Agent.setStatus(
        "current"
    )

p7021A_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1062)
)
if mibBuilder.loadTexts:
    p7021A_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7021A_Agent.setStatus(
        "current"
    )

p7003A_1b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1063)
)
if mibBuilder.loadTexts:
    p7003A_1b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7003A_1b_Agent.setStatus(
        "current"
    )

p7007SD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1064)
)
if mibBuilder.loadTexts:
    p7007SD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7007SD_Agent.setStatus(
        "current"
    )

ibdh1070_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1065)
)
if mibBuilder.loadTexts:
    ibdh1070_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1070_10a_Agent.setStatus(
        "current"
    )

ibdh4001_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1066)
)
if mibBuilder.loadTexts:
    ibdh4001_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh4001_10a_Agent.setStatus(
        "current"
    )

p7021RC_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1068)
)
if mibBuilder.loadTexts:
    p7021RC_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7021RC_Agent.setStatus(
        "current"
    )

p7021CD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1070)
)
if mibBuilder.loadTexts:
    p7021CD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7021CD_Agent.setStatus(
        "current"
    )

p7001D_1d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1071)
)
if mibBuilder.loadTexts:
    p7001D_1d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001D_1d_Agent.setStatus(
        "current"
    )

p7021SD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1072)
)
if mibBuilder.loadTexts:
    p7021SD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7021SD_Agent.setStatus(
        "current"
    )

p7012SV_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1073)
)
if mibBuilder.loadTexts:
    p7012SV_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7012SV_Agent.setStatus(
        "current"
    )

ibdh1095_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1074)
)
if mibBuilder.loadTexts:
    ibdh1095_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1095_10a_Agent.setStatus(
        "current"
    )

p7035A_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1075)
)
if mibBuilder.loadTexts:
    p7035A_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7035A_Agent.setStatus(
        "current"
    )

p7025A_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1076)
)
if mibBuilder.loadTexts:
    p7025A_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7025A_Agent.setStatus(
        "current"
    )

ibdh424_10dSO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1077)
)
if mibBuilder.loadTexts:
    ibdh424_10dSO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh424_10dSO_Agent.setStatus(
        "current"
    )

ibdh2001_10cSO_11a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1078)
)
if mibBuilder.loadTexts:
    ibdh2001_10cSO_11a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh2001_10cSO_11a_Agent.setStatus(
        "current"
    )

p7010BSI_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1079)
)
if mibBuilder.loadTexts:
    p7010BSI_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7010BSI_Agent.setStatus(
        "current"
    )

ibdh1070SI_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1080)
)
if mibBuilder.loadTexts:
    ibdh1070SI_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh1070SI_Agent.setStatus(
        "current"
    )

pbd1970_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1081)
)
if mibBuilder.loadTexts:
    pbd1970_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbd1970_Agent.setStatus(
        "current"
    )

pbd2020_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1082)
)
if mibBuilder.loadTexts:
    pbd2020_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbd2020_Agent.setStatus(
        "current"
    )

p7001D_1b_7_15SM2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1089)
)
if mibBuilder.loadTexts:
    p7001D_1b_7_15SM2_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7001D_1b_7_15SM2_Agent.setStatus(
        "current"
    )

ibdh340_10b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 1096)
)
if mibBuilder.loadTexts:
    ibdh340_10b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibdh340_10b_Agent.setStatus(
        "current"
    )

p7002_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2000)
)
if mibBuilder.loadTexts:
    p7002_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    p7002_Agent.setStatus(
        "current"
    )

p7002W_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2001)
)
if mibBuilder.loadTexts:
    p7002W_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    p7002W_Agent.setStatus(
        "current"
    )

p7002_140MHz_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2002)
)
if mibBuilder.loadTexts:
    p7002_140MHz_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    p7002_140MHz_Agent.setStatus(
        "current"
    )

p7006_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2003)
)
if mibBuilder.loadTexts:
    p7006_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7006_Agent.setStatus(
        "current"
    )

p7006_1b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2004)
)
if mibBuilder.loadTexts:
    p7006_1b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7006_1b_Agent.setStatus(
        "current"
    )

p7008_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2005)
)
if mibBuilder.loadTexts:
    p7008_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7008_Agent.setStatus(
        "current"
    )

p7013_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2006)
)
if mibBuilder.loadTexts:
    p7013_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7013_Agent.setStatus(
        "current"
    )

p7013_140MHz_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2007)
)
if mibBuilder.loadTexts:
    p7013_140MHz_Agent.setProductRelease("Peak Communications Ltd. release 1.4")
if mibBuilder.loadTexts:
    p7013_140MHz_Agent.setStatus(
        "current"
    )

p7014_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2008)
)
if mibBuilder.loadTexts:
    p7014_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7014_Agent.setStatus(
        "current"
    )

p7014_1b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2009)
)
if mibBuilder.loadTexts:
    p7014_1b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7014_1b_Agent.setStatus(
        "current"
    )

p7022C_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2010)
)
if mibBuilder.loadTexts:
    p7022C_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7022C_Agent.setStatus(
        "current"
    )

p7022SO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2011)
)
if mibBuilder.loadTexts:
    p7022SO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7022SO_Agent.setStatus(
        "current"
    )

p7702_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2012)
)
if mibBuilder.loadTexts:
    p7702_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7702_Agent.setStatus(
        "current"
    )

p5006_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2013)
)
if mibBuilder.loadTexts:
    p5006_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p5006_Agent.setStatus(
        "current"
    )

p7022SD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2014)
)
if mibBuilder.loadTexts:
    p7022SD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7022SD_Agent.setStatus(
        "current"
    )

p7002W_1b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2015)
)
if mibBuilder.loadTexts:
    p7002W_1b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002W_1b_Agent.setStatus(
        "current"
    )

p7702SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2020)
)
if mibBuilder.loadTexts:
    p7702SA_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    p7702SA_Agent.setStatus(
        "current"
    )

p7002DW_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2023)
)
if mibBuilder.loadTexts:
    p7002DW_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002DW_Agent.setStatus(
        "current"
    )

p7013_140MHz_ATT_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2026)
)
if mibBuilder.loadTexts:
    p7013_140MHz_ATT_Agent.setProductRelease("Peak Communications Ltd. release 1.3")
if mibBuilder.loadTexts:
    p7013_140MHz_ATT_Agent.setStatus(
        "current"
    )

pbu2000_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2027)
)
if mibBuilder.loadTexts:
    pbu2000_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2000_Agent.setStatus(
        "current"
    )

ibuh137_10b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2029)
)
if mibBuilder.loadTexts:
    ibuh137_10b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh137_10b_Agent.setStatus(
        "current"
    )

p7018A_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2030)
)
if mibBuilder.loadTexts:
    p7018A_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    p7018A_Agent.setStatus(
        "current"
    )

p7127B_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2032)
)
if mibBuilder.loadTexts:
    p7127B_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7127B_Agent.setStatus(
        "current"
    )

p7006BS_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2033)
)
if mibBuilder.loadTexts:
    p7006BS_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7006BS_Agent.setStatus(
        "current"
    )

p7013_13SA_14SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2034)
)
if mibBuilder.loadTexts:
    p7013_13SA_14SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7013_13SA_14SA_Agent.setStatus(
        "current"
    )

ibuh3000_10a_13_14_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2035)
)
if mibBuilder.loadTexts:
    ibuh3000_10a_13_14_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh3000_10a_13_14_Agent.setStatus(
        "current"
    )

ibuh1970_10b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2036)
)
if mibBuilder.loadTexts:
    ibuh1970_10b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh1970_10b_Agent.setStatus(
        "current"
    )

pbu3000_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2037)
)
if mibBuilder.loadTexts:
    pbu3000_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu3000_Agent.setStatus(
        "current"
    )

ibuh184_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2038)
)
if mibBuilder.loadTexts:
    ibuh184_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh184_10a_Agent.setStatus(
        "current"
    )

pbu2000SBE_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2040)
)
if mibBuilder.loadTexts:
    pbu2000SBE_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2000SBE_Agent.setStatus(
        "current"
    )

p7702EUC_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2042)
)
if mibBuilder.loadTexts:
    p7702EUC_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7702EUC_Agent.setStatus(
        "current"
    )

p7002R_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2046)
)
if mibBuilder.loadTexts:
    p7002R_5_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002R_5_Agent.setStatus(
        "current"
    )

p7002R_1SD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2047)
)
if mibBuilder.loadTexts:
    p7002R_1SD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002R_1SD_Agent.setStatus(
        "current"
    )

ibuh6725SD2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2048)
)
if mibBuilder.loadTexts:
    ibuh6725SD2_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh6725SD2_Agent.setStatus(
        "current"
    )

ibuh140_10b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2049)
)
if mibBuilder.loadTexts:
    ibuh140_10b_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh140_10b_Agent.setStatus(
        "current"
    )

p7006B_1a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2050)
)
if mibBuilder.loadTexts:
    p7006B_1a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7006B_1a_Agent.setStatus(
        "current"
    )

p7002R_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2051)
)
if mibBuilder.loadTexts:
    p7002R_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002R_Agent.setStatus(
        "current"
    )

ibuh7025_10a_13_14_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2053)
)
if mibBuilder.loadTexts:
    ibuh7025_10a_13_14_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh7025_10a_13_14_Agent.setStatus(
        "current"
    )

ibuh2000_10b_11e_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2055)
)
if mibBuilder.loadTexts:
    ibuh2000_10b_11e_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibuh2000_10b_11e_Agent.setStatus(
        "current"
    )

pbu2000_5_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2056)
)
if mibBuilder.loadTexts:
    pbu2000_5_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2000_5_10a_Agent.setStatus(
        "current"
    )

pbu2000_10a_11e_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2058)
)
if mibBuilder.loadTexts:
    pbu2000_10a_11e_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2000_10a_11e_Agent.setStatus(
        "current"
    )

p7002_1c_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2059)
)
if mibBuilder.loadTexts:
    p7002_1c_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002_1c_Agent.setStatus(
        "current"
    )

p7127A_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2060)
)
if mibBuilder.loadTexts:
    p7127A_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7127A_Agent.setStatus(
        "current"
    )

p7006ST2_1a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2062)
)
if mibBuilder.loadTexts:
    p7006ST2_1a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7006ST2_1a_Agent.setStatus(
        "current"
    )

pbu2000_5_11e_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2066)
)
if mibBuilder.loadTexts:
    pbu2000_5_11e_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2000_5_11e_Agent.setStatus(
        "current"
    )

p7022RASD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2067)
)
if mibBuilder.loadTexts:
    p7022RASD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7022RASD_Agent.setStatus(
        "current"
    )

p7006DST2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2068)
)
if mibBuilder.loadTexts:
    p7006DST2_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7006DST2_Agent.setStatus(
        "current"
    )

ibu137_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2069)
)
if mibBuilder.loadTexts:
    ibu137_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ibu137_3a_Agent.setStatus(
        "current"
    )

pbu2000_10a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2075)
)
if mibBuilder.loadTexts:
    pbu2000_10a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2000_10a_Agent.setStatus(
        "current"
    )

pbu107SG_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2076)
)
if mibBuilder.loadTexts:
    pbu107SG_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu107SG_Agent.setStatus(
        "current"
    )

pbu117SG_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2077)
)
if mibBuilder.loadTexts:
    pbu117SG_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu117SG_Agent.setStatus(
        "current"
    )

p7002R_5a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2084)
)
if mibBuilder.loadTexts:
    p7002R_5a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002R_5a_Agent.setStatus(
        "current"
    )

pbu2750_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2088)
)
if mibBuilder.loadTexts:
    pbu2750_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2750_Agent.setStatus(
        "current"
    )

pbu3100_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2089)
)
if mibBuilder.loadTexts:
    pbu3100_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu3100_Agent.setStatus(
        "current"
    )

pbu2900_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2090)
)
if mibBuilder.loadTexts:
    pbu2900_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2900_Agent.setStatus(
        "current"
    )

pbu2830_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2091)
)
if mibBuilder.loadTexts:
    pbu2830_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    pbu2830_Agent.setStatus(
        "current"
    )

p7002D_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2093)
)
if mibBuilder.loadTexts:
    p7002D_5_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    p7002D_5_Agent.setStatus(
        "current"
    )

p7002D_5a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2094)
)
if mibBuilder.loadTexts:
    p7002D_5a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002D_5a_Agent.setStatus(
        "current"
    )

p7002D_1_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2095)
)
if mibBuilder.loadTexts:
    p7002D_1_5_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002D_1_5_Agent.setStatus(
        "current"
    )

p7002D_1_5a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2096)
)
if mibBuilder.loadTexts:
    p7002D_1_5a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002D_1_5a_Agent.setStatus(
        "current"
    )

p7002_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2097)
)
if mibBuilder.loadTexts:
    p7002_5_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002_5_Agent.setStatus(
        "current"
    )

p7002_5a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2098)
)
if mibBuilder.loadTexts:
    p7002_5a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002_5a_Agent.setStatus(
        "current"
    )

p7002_1a_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2099)
)
if mibBuilder.loadTexts:
    p7002_1a_5_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002_1a_5_Agent.setStatus(
        "current"
    )

p7002_1a_5s_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2100)
)
if mibBuilder.loadTexts:
    p7002_1a_5s_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    p7002_1a_5s_Agent.setStatus(
        "current"
    )

p7002_1a_5b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 2101)
)
if mibBuilder.loadTexts:
    p7002_1a_5b_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    p7002_1a_5b_Agent.setStatus(
        "current"
    )

ptr50_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3000)
)
if mibBuilder.loadTexts:
    ptr50_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    ptr50_Agent.setStatus(
        "current"
    )

ptr50_1e_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3001)
)
if mibBuilder.loadTexts:
    ptr50_1e_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    ptr50_1e_Agent.setStatus(
        "current"
    )

ptr50_1c_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3002)
)
if mibBuilder.loadTexts:
    ptr50_1c_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    ptr50_1c_Agent.setStatus(
        "current"
    )

rtr50_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3003)
)
if mibBuilder.loadTexts:
    rtr50_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    rtr50_Agent.setStatus(
        "current"
    )

ptr50_6_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3004)
)
if mibBuilder.loadTexts:
    ptr50_6_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    ptr50_6_Agent.setStatus(
        "current"
    )

ptr50_1d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3005)
)
if mibBuilder.loadTexts:
    ptr50_1d_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    ptr50_1d_Agent.setStatus(
        "current"
    )

ptr50_1d_6SU_12SU_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3006)
)
if mibBuilder.loadTexts:
    ptr50_1d_6SU_12SU_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ptr50_1d_6SU_12SU_Agent.setStatus(
        "current"
    )

ptr50_1d_6SD_12SD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 3007)
)
if mibBuilder.loadTexts:
    ptr50_1d_6SD_12SD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ptr50_1d_6SD_12SD_Agent.setStatus(
        "current"
    )

tlth137_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5018)
)
if mibBuilder.loadTexts:
    tlth137_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    tlth137_3a_Agent.setStatus(
        "current"
    )

tlth6725_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5019)
)
if mibBuilder.loadTexts:
    tlth6725_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth6725_Agent.setStatus(
        "current"
    )

tlth600_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5020)
)
if mibBuilder.loadTexts:
    tlth600_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth600_3a_Agent.setStatus(
        "current"
    )

tlthsi3_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5022)
)
if mibBuilder.loadTexts:
    tlthsi3_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlthsi3_Agent.setStatus(
        "current"
    )

tlth742_3d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5023)
)
if mibBuilder.loadTexts:
    tlth742_3d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth742_3d_Agent.setStatus(
        "current"
    )

tlth137_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5026)
)
if mibBuilder.loadTexts:
    tlth137_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth137_Agent.setStatus(
        "current"
    )

tlth5844SA_13SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5027)
)
if mibBuilder.loadTexts:
    tlth5844SA_13SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth5844SA_13SA_Agent.setStatus(
        "current"
    )

tlth6724SAa_13SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5028)
)
if mibBuilder.loadTexts:
    tlth6724SAa_13SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth6724SAa_13SA_Agent.setStatus(
        "current"
    )

tlth1003_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5029)
)
if mibBuilder.loadTexts:
    tlth1003_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1003_Agent.setStatus(
        "current"
    )

tlth1003_3c_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5030)
)
if mibBuilder.loadTexts:
    tlth1003_3c_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1003_3c_Agent.setStatus(
        "current"
    )

tlth5844SA_3d_13SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5032)
)
if mibBuilder.loadTexts:
    tlth5844SA_3d_13SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth5844SA_3d_13SA_Agent.setStatus(
        "current"
    )

tltr2750_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5033)
)
if mibBuilder.loadTexts:
    tltr2750_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr2750_3a_Agent.setStatus(
        "current"
    )

tlth13761SA_13SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5034)
)
if mibBuilder.loadTexts:
    tlth13761SA_13SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth13761SA_13SA_Agent.setStatus(
        "current"
    )

tltr1000SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5035)
)
if mibBuilder.loadTexts:
    tltr1000SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr1000SA_Agent.setStatus(
        "current"
    )

tltr13761SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5036)
)
if mibBuilder.loadTexts:
    tltr13761SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr13761SA_Agent.setStatus(
        "current"
    )

tlth1004_3e_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5038)
)
if mibBuilder.loadTexts:
    tlth1004_3e_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1004_3e_Agent.setStatus(
        "current"
    )

tltr1000SD_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5039)
)
if mibBuilder.loadTexts:
    tltr1000SD_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr1000SD_Agent.setStatus(
        "current"
    )

tlth184SR_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5040)
)
if mibBuilder.loadTexts:
    tlth184SR_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth184SR_Agent.setStatus(
        "current"
    )

tlth672_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5041)
)
if mibBuilder.loadTexts:
    tlth672_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth672_Agent.setStatus(
        "current"
    )

tltr1002SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5042)
)
if mibBuilder.loadTexts:
    tltr1002SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr1002SA_Agent.setStatus(
        "current"
    )

tltr5578SI_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5043)
)
if mibBuilder.loadTexts:
    tltr5578SI_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr5578SI_Agent.setStatus(
        "current"
    )

tlth3100_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5044)
)
if mibBuilder.loadTexts:
    tlth3100_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth3100_Agent.setStatus(
        "current"
    )

tlth180_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5045)
)
if mibBuilder.loadTexts:
    tlth180_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth180_Agent.setStatus(
        "current"
    )

tlth2001SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5046)
)
if mibBuilder.loadTexts:
    tlth2001SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth2001SA_Agent.setStatus(
        "current"
    )

tltr742_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5047)
)
if mibBuilder.loadTexts:
    tltr742_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr742_Agent.setStatus(
        "current"
    )

tlth127_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5048)
)
if mibBuilder.loadTexts:
    tlth127_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth127_3a_Agent.setStatus(
        "current"
    )

tlth642ST_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5049)
)
if mibBuilder.loadTexts:
    tlth642ST_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth642ST_Agent.setStatus(
        "current"
    )

tlth1000ST_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5050)
)
if mibBuilder.loadTexts:
    tlth1000ST_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1000ST_Agent.setStatus(
        "current"
    )

tltr3100_3eSP_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5051)
)
if mibBuilder.loadTexts:
    tltr3100_3eSP_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr3100_3eSP_Agent.setStatus(
        "current"
    )

tlth790_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5052)
)
if mibBuilder.loadTexts:
    tlth790_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth790_3a_Agent.setStatus(
        "current"
    )

tltr742_3a_13_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5053)
)
if mibBuilder.loadTexts:
    tltr742_3a_13_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr742_3a_13_Agent.setStatus(
        "current"
    )

tltr184_3a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5054)
)
if mibBuilder.loadTexts:
    tltr184_3a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr184_3a_Agent.setStatus(
        "current"
    )

tltr572SD2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5055)
)
if mibBuilder.loadTexts:
    tltr572SD2_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr572SD2_Agent.setStatus(
        "current"
    )

tltr1003_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5057)
)
if mibBuilder.loadTexts:
    tltr1003_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr1003_Agent.setStatus(
        "current"
    )

tlth1000ST2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5059)
)
if mibBuilder.loadTexts:
    tlth1000ST2_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1000ST2_Agent.setStatus(
        "current"
    )

tltr2225_3d_4_5aSI_5bSI_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5060)
)
if mibBuilder.loadTexts:
    tltr2225_3d_4_5aSI_5bSI_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr2225_3d_4_5aSI_5bSI_Agent.setStatus(
        "current"
    )

tlth2225_3d_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5061)
)
if mibBuilder.loadTexts:
    tlth2225_3d_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth2225_3d_Agent.setStatus(
        "current"
    )

tlth1000ST2a_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5062)
)
if mibBuilder.loadTexts:
    tlth1000ST2a_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1000ST2a_Agent.setStatus(
        "current"
    )

tltr2225SD2_3d_4_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5063)
)
if mibBuilder.loadTexts:
    tltr2225SD2_3d_4_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr2225SD2_3d_4_Agent.setStatus(
        "current"
    )

tlthsi9_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5069)
)
if mibBuilder.loadTexts:
    tlthsi9_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlthsi9_Agent.setStatus(
        "current"
    )

tlth1000SA2_13_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5078)
)
if mibBuilder.loadTexts:
    tlth1000SA2_13_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tlth1000SA2_13_Agent.setStatus(
        "current"
    )

tltr1000SA2_13SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5079)
)
if mibBuilder.loadTexts:
    tltr1000SA2_13SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr1000SA2_13SA_Agent.setStatus(
        "current"
    )

tltr1004SI_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5080)
)
if mibBuilder.loadTexts:
    tltr1004SI_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr1004SI_Agent.setStatus(
        "current"
    )

tltrsi3_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5081)
)
if mibBuilder.loadTexts:
    tltrsi3_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltrsi3_Agent.setStatus(
        "current"
    )

tltr101SG_15SG_16SG_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 5083)
)
if mibBuilder.loadTexts:
    tltr101SG_15SG_16SG_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    tltr101SG_15SG_16SG_Agent.setStatus(
        "current"
    )

rcu100hh_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6000)
)
if mibBuilder.loadTexts:
    rcu100hh_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu100hh_Agent.setStatus(
        "current"
    )

rcu100_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6001)
)
if mibBuilder.loadTexts:
    rcu100_Agent.setProductRelease("Peak Communications Ltd. release 1.2")
if mibBuilder.loadTexts:
    rcu100_Agent.setStatus(
        "current"
    )

rcu1800_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6002)
)
if mibBuilder.loadTexts:
    rcu1800_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu1800_Agent.setStatus(
        "current"
    )

rcu1400_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6004)
)
if mibBuilder.loadTexts:
    rcu1400_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu1400_Agent.setStatus(
        "current"
    )

rcu1600_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6007)
)
if mibBuilder.loadTexts:
    rcu1600_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu1600_Agent.setStatus(
        "current"
    )

rcu1401ST_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6008)
)
if mibBuilder.loadTexts:
    rcu1401ST_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu1401ST_Agent.setStatus(
        "current"
    )

rcu50PO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6009)
)
if mibBuilder.loadTexts:
    rcu50PO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu50PO_Agent.setStatus(
        "current"
    )

rcuh200_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6011)
)
if mibBuilder.loadTexts:
    rcuh200_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcuh200_Agent.setStatus(
        "current"
    )

rcu50SP_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6012)
)
if mibBuilder.loadTexts:
    rcu50SP_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu50SP_Agent.setStatus(
        "current"
    )

rcu50_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6013)
)
if mibBuilder.loadTexts:
    rcu50_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu50_Agent.setStatus(
        "current"
    )

rcu50PO_10PO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6015)
)
if mibBuilder.loadTexts:
    rcu50PO_10PO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu50PO_10PO_Agent.setStatus(
        "current"
    )

rcuh100SO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6016)
)
if mibBuilder.loadTexts:
    rcuh100SO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcuh100SO_Agent.setStatus(
        "current"
    )

rcu1402_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6017)
)
if mibBuilder.loadTexts:
    rcu1402_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu1402_Agent.setStatus(
        "current"
    )

rcu50PO_10PO_11PO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6018)
)
if mibBuilder.loadTexts:
    rcu50PO_10PO_11PO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu50PO_10PO_11PO_Agent.setStatus(
        "current"
    )

rcu50_8_10aSP_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6019)
)
if mibBuilder.loadTexts:
    rcu50_8_10aSP_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu50_8_10aSP_Agent.setStatus(
        "current"
    )

rcuh100_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6024)
)
if mibBuilder.loadTexts:
    rcuh100_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcuh100_Agent.setStatus(
        "current"
    )

rcu52_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6025)
)
if mibBuilder.loadTexts:
    rcu52_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcu52_Agent.setStatus(
        "current"
    )

rcuh50_11SO_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 6026)
)
if mibBuilder.loadTexts:
    rcuh50_11SO_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    rcuh50_11SO_Agent.setStatus(
        "current"
    )

d600_8SB1_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8000)
)
if mibBuilder.loadTexts:
    d600_8SB1_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    d600_8SB1_Agent.setStatus(
        "current"
    )

d600_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8001)
)
if mibBuilder.loadTexts:
    d600_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    d600_Agent.setStatus(
        "current"
    )

dbu200_6b_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8002)
)
if mibBuilder.loadTexts:
    dbu200_6b_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    dbu200_6b_Agent.setStatus(
        "current"
    )

ilah2150mt_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8003)
)
if mibBuilder.loadTexts:
    ilah2150mt_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ilah2150mt_Agent.setStatus(
        "current"
    )

ilah2150mr_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8004)
)
if mibBuilder.loadTexts:
    ilah2150mr_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ilah2150mr_Agent.setStatus(
        "current"
    )

upc7000_2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8005)
)
if mibBuilder.loadTexts:
    upc7000_2_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7000_2_Agent.setStatus(
        "current"
    )

upc7001_2_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8006)
)
if mibBuilder.loadTexts:
    upc7001_2_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2_5_Agent.setStatus(
        "current"
    )

upc7001_2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8008)
)
if mibBuilder.loadTexts:
    upc7001_2_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2_Agent.setStatus(
        "current"
    )

upc7002_2_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8010)
)
if mibBuilder.loadTexts:
    upc7002_2_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7002_2_5_Agent.setStatus(
        "current"
    )

ilah1450sm_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8011)
)
if mibBuilder.loadTexts:
    ilah1450sm_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ilah1450sm_Agent.setStatus(
        "current"
    )

upc7002_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8012)
)
if mibBuilder.loadTexts:
    upc7002_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7002_5_Agent.setStatus(
        "current"
    )

ilahl2150_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8013)
)
if mibBuilder.loadTexts:
    ilahl2150_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ilahl2150_Agent.setStatus(
        "current"
    )

dms_rf_u_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8014)
)
if mibBuilder.loadTexts:
    dms_rf_u_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dms_rf_u_Agent.setStatus(
        "current"
    )

upc7001_2c_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8015)
)
if mibBuilder.loadTexts:
    upc7001_2c_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2c_5_Agent.setStatus(
        "current"
    )

upc7001_2_7_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8017)
)
if mibBuilder.loadTexts:
    upc7001_2_7_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2_7_5_Agent.setStatus(
        "current"
    )

mpmEmulator_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8018)
)
if mibBuilder.loadTexts:
    mpmEmulator_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    mpmEmulator_Agent.setStatus(
        "current"
    )

ilah240_10a_13_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8019)
)
if mibBuilder.loadTexts:
    ilah240_10a_13_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ilah240_10a_13_Agent.setStatus(
        "current"
    )

upc7001_2_7_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8020)
)
if mibBuilder.loadTexts:
    upc7001_2_7_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2_7_Agent.setStatus(
        "current"
    )

upc7001_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8021)
)
if mibBuilder.loadTexts:
    upc7001_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_Agent.setStatus(
        "current"
    )

upc7003_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8022)
)
if mibBuilder.loadTexts:
    upc7003_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7003_Agent.setStatus(
        "current"
    )

dbu200_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8023)
)
if mibBuilder.loadTexts:
    dbu200_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dbu200_Agent.setStatus(
        "current"
    )

upc7004_2_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8025)
)
if mibBuilder.loadTexts:
    upc7004_2_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7004_2_5_Agent.setStatus(
        "current"
    )

upc7004_2a_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8026)
)
if mibBuilder.loadTexts:
    upc7004_2a_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7004_2a_5_Agent.setStatus(
        "current"
    )

dbu200_6_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8027)
)
if mibBuilder.loadTexts:
    dbu200_6_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    dbu200_6_Agent.setStatus(
        "current"
    )

upc7002_2_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8028)
)
if mibBuilder.loadTexts:
    upc7002_2_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7002_2_Agent.setStatus(
        "current"
    )

s8SA_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8029)
)
if mibBuilder.loadTexts:
    s8SA_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    s8SA_Agent.setStatus(
        "current"
    )

upc7001_2a_7_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8030)
)
if mibBuilder.loadTexts:
    upc7001_2a_7_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2a_7_Agent.setStatus(
        "current"
    )

upc7001_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8031)
)
if mibBuilder.loadTexts:
    upc7001_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_5_Agent.setStatus(
        "current"
    )

dlah200_6_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8032)
)
if mibBuilder.loadTexts:
    dlah200_6_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dlah200_6_Agent.setStatus(
        "current"
    )

dlah200_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8033)
)
if mibBuilder.loadTexts:
    dlah200_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dlah200_Agent.setStatus(
        "current"
    )

ilahl_1750_10a_13_14_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8034)
)
if mibBuilder.loadTexts:
    ilahl_1750_10a_13_14_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    ilahl_1750_10a_13_14_Agent.setStatus(
        "current"
    )

dla200_6_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8035)
)
if mibBuilder.loadTexts:
    dla200_6_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dla200_6_Agent.setStatus(
        "current"
    )

dla200_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8036)
)
if mibBuilder.loadTexts:
    dla200_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dla200_Agent.setStatus(
        "current"
    )

upc7004_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8037)
)
if mibBuilder.loadTexts:
    upc7004_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7004_5_Agent.setStatus(
        "current"
    )

upc7002_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8041)
)
if mibBuilder.loadTexts:
    upc7002_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7002_Agent.setStatus(
        "current"
    )

isulh08_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8043)
)
if mibBuilder.loadTexts:
    isulh08_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    isulh08_Agent.setStatus(
        "current"
    )

upc7004_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8044)
)
if mibBuilder.loadTexts:
    upc7004_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    upc7004_Agent.setStatus(
        "current"
    )

upc7002_5_11st_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8045)
)
if mibBuilder.loadTexts:
    upc7002_5_11st_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7002_5_11st_Agent.setStatus(
        "current"
    )

dbuh200_9_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8048)
)
if mibBuilder.loadTexts:
    dbuh200_9_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dbuh200_9_Agent.setStatus(
        "current"
    )

dbuh200_6_9_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8049)
)
if mibBuilder.loadTexts:
    dbuh200_6_9_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    dbuh200_6_9_Agent.setStatus(
        "current"
    )

upc7000_2_11_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8050)
)
if mibBuilder.loadTexts:
    upc7000_2_11_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7000_2_11_Agent.setStatus(
        "current"
    )

upc7001_2d_5_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8051)
)
if mibBuilder.loadTexts:
    upc7001_2d_5_Agent.setProductRelease("Peak Communications Ltd. release 1.1")
if mibBuilder.loadTexts:
    upc7001_2d_5_Agent.setStatus(
        "current"
    )

isb001_Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 31637, 100, 8052)
)
if mibBuilder.loadTexts:
    isb001_Agent.setProductRelease("Peak Communications Ltd. release 1.0")
if mibBuilder.loadTexts:
    isb001_Agent.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKAGENTS-MIB",
    **{"peakAgents": peakAgents,
       "p7000-Agent": p7000_Agent,
       "p7000W-Agent": p7000W_Agent,
       "p7000-140MHZ-Agent": p7000_140MHZ_Agent,
       "p7000W-140MHz-Agent": p7000W_140MHz_Agent,
       "p7020SA-Agent": p7020SA_Agent,
       "p7020-Agent": p7020_Agent,
       "p7020-140MHz-Agent": p7020_140MHz_Agent,
       "p7000i-Agent": p7000i_Agent,
       "p7000SM": p7000SM,
       "p7000i-1a-1b-5a-Agent": p7000i_1a_1b_5a_Agent,
       "p7000-5-Agent": p7000_5_Agent,
       "p7001-Agent": p7001_Agent,
       "p7001-140MHz-Agent": p7001_140MHz_Agent,
       "p7001S1-Agent": p7001S1_Agent,
       "p7001-P701-Agent": p7001_P701_Agent,
       "p7001D-Agent": p7001D_Agent,
       "p7001D-140MHz-Agent": p7001D_140MHz_Agent,
       "p7003A-Agent": p7003A_Agent,
       "p7007S-Agent": p7007S_Agent,
       "p7010-Agent": p7010_Agent,
       "p7011-Agent": p7011_Agent,
       "p7012-Agent": p7012_Agent,
       "p7021C-Agent": p7021C_Agent,
       "p7021SO-Agent": p7021SO_Agent,
       "p7035-Agent": p7035_Agent,
       "p7701-Agent": p7701_Agent,
       "p5003-Agent": p5003_Agent,
       "ibdh340-Agent": ibdh340_Agent,
       "ibdh340-ATT-Agent": ibdh340_ATT_Agent,
       "ibdh1225-10b-Agent": ibdh1225_10b_Agent,
       "p7701SA-Agent": p7701SA_Agent,
       "p7007-Agent": p7007_Agent,
       "p7001-1d-7-Agent": p7001_1d_7_Agent,
       "p7001R-Agent": p7001R_Agent,
       "ibdh3003-10b-Agent": ibdh3003_10b_Agent,
       "ibdh342-1db-Agent": ibdh342_1db_Agent,
       "ibdh1072-1db-Agent": ibdh1072_1db_Agent,
       "ibdh1172-1db-Agent": ibdh1172_1db_Agent,
       "p7001-1d-Agent": p7001_1d_Agent,
       "ibdh2001-Agent": ibdh2001_Agent,
       "ibdh2001-10a-11-Agent": ibdh2001_10a_11_Agent,
       "ibdh1225SM-10b-15SM-Agent": ibdh1225SM_10b_15SM_Agent,
       "p7001DSA-Agent": p7001DSA_Agent,
       "ibdh2001-10a-Agent": ibdh2001_10a_Agent,
       "ibdh2001-11i-Agent": ibdh2001_11i_Agent,
       "p7701EDC-Agent": p7701EDC_Agent,
       "ibdh340-10a-Agent": ibdh340_10a_Agent,
       "pbd2001sl-Agent": pbd2001sl_Agent,
       "p7025bse-Agent": p7025bse_Agent,
       "p7007XH-Agent": p7007XH_Agent,
       "ibdh3000-2-Agent": ibdh3000_2_Agent,
       "ibdh1095-10b-SM-Agent": ibdh1095_10b_SM_Agent,
       "ibdh1225-10b-SM-Agent": ibdh1225_10b_SM_Agent,
       "p7001R-1SD-7-Agent": p7001R_1SD_7_Agent,
       "ibdh3003-10a-11c-Agent": ibdh3003_10a_11c_Agent,
       "p7003CSNb-1d-Agent": p7003CSNb_1d_Agent,
       "p7025A-1d-Agent": p7025A_1d_Agent,
       "p7003A-1d-Agent": p7003A_1d_Agent,
       "ibdh4004-10a-Agent": ibdh4004_10a_Agent,
       "p7011B-Agent": p7011B_Agent,
       "ibdh450ST-10a-Agent": ibdh450ST_10a_Agent,
       "p7021A-Agent": p7021A_Agent,
       "p7003A-1b-Agent": p7003A_1b_Agent,
       "p7007SD-Agent": p7007SD_Agent,
       "ibdh1070-10a-Agent": ibdh1070_10a_Agent,
       "ibdh4001-10a-Agent": ibdh4001_10a_Agent,
       "p7021RC-Agent": p7021RC_Agent,
       "p7021CD-Agent": p7021CD_Agent,
       "p7001D-1d-Agent": p7001D_1d_Agent,
       "p7021SD-Agent": p7021SD_Agent,
       "p7012SV-Agent": p7012SV_Agent,
       "ibdh1095-10a-Agent": ibdh1095_10a_Agent,
       "p7035A-Agent": p7035A_Agent,
       "p7025A-Agent": p7025A_Agent,
       "ibdh424-10dSO-Agent": ibdh424_10dSO_Agent,
       "ibdh2001-10cSO-11a-Agent": ibdh2001_10cSO_11a_Agent,
       "p7010BSI-Agent": p7010BSI_Agent,
       "ibdh1070SI-Agent": ibdh1070SI_Agent,
       "pbd1970-Agent": pbd1970_Agent,
       "pbd2020-Agent": pbd2020_Agent,
       "p7001D-1b-7-15SM2-Agent": p7001D_1b_7_15SM2_Agent,
       "ibdh340-10b-Agent": ibdh340_10b_Agent,
       "p7002-Agent": p7002_Agent,
       "p7002W-Agent": p7002W_Agent,
       "p7002-140MHz-Agent": p7002_140MHz_Agent,
       "p7006-Agent": p7006_Agent,
       "p7006-1b-Agent": p7006_1b_Agent,
       "p7008-Agent": p7008_Agent,
       "p7013-Agent": p7013_Agent,
       "p7013-140MHz-Agent": p7013_140MHz_Agent,
       "p7014-Agent": p7014_Agent,
       "p7014-1b-Agent": p7014_1b_Agent,
       "p7022C-Agent": p7022C_Agent,
       "p7022SO-Agent": p7022SO_Agent,
       "p7702-Agent": p7702_Agent,
       "p5006-Agent": p5006_Agent,
       "p7022SD-Agent": p7022SD_Agent,
       "p7002W-1b-Agent": p7002W_1b_Agent,
       "p7702SA-Agent": p7702SA_Agent,
       "p7002DW-Agent": p7002DW_Agent,
       "p7013-140MHz-ATT-Agent": p7013_140MHz_ATT_Agent,
       "pbu2000-Agent": pbu2000_Agent,
       "ibuh137-10b-Agent": ibuh137_10b_Agent,
       "p7018A-Agent": p7018A_Agent,
       "p7127B-Agent": p7127B_Agent,
       "p7006BS-Agent": p7006BS_Agent,
       "p7013-13SA-14SA-Agent": p7013_13SA_14SA_Agent,
       "ibuh3000-10a-13-14-Agent": ibuh3000_10a_13_14_Agent,
       "ibuh1970-10b-Agent": ibuh1970_10b_Agent,
       "pbu3000-Agent": pbu3000_Agent,
       "ibuh184-10a-Agent": ibuh184_10a_Agent,
       "pbu2000SBE-Agent": pbu2000SBE_Agent,
       "p7702EUC-Agent": p7702EUC_Agent,
       "p7002R-5-Agent": p7002R_5_Agent,
       "p7002R-1SD-Agent": p7002R_1SD_Agent,
       "ibuh6725SD2-Agent": ibuh6725SD2_Agent,
       "ibuh140-10b-Agent": ibuh140_10b_Agent,
       "p7006B-1a-Agent": p7006B_1a_Agent,
       "p7002R-Agent": p7002R_Agent,
       "ibuh7025-10a-13-14-Agent": ibuh7025_10a_13_14_Agent,
       "ibuh2000-10b-11e-Agent": ibuh2000_10b_11e_Agent,
       "pbu2000-5-10a-Agent": pbu2000_5_10a_Agent,
       "pbu2000-10a-11e-Agent": pbu2000_10a_11e_Agent,
       "p7002-1c-Agent": p7002_1c_Agent,
       "p7127A-Agent": p7127A_Agent,
       "p7006ST2-1a-Agent": p7006ST2_1a_Agent,
       "pbu2000-5-11e-Agent": pbu2000_5_11e_Agent,
       "p7022RASD-Agent": p7022RASD_Agent,
       "p7006DST2-Agent": p7006DST2_Agent,
       "ibu137-3a-Agent": ibu137_3a_Agent,
       "pbu2000-10a-Agent": pbu2000_10a_Agent,
       "pbu107SG-Agent": pbu107SG_Agent,
       "pbu117SG-Agent": pbu117SG_Agent,
       "p7002R-5a-Agent": p7002R_5a_Agent,
       "pbu2750-Agent": pbu2750_Agent,
       "pbu3100-Agent": pbu3100_Agent,
       "pbu2900-Agent": pbu2900_Agent,
       "pbu2830-Agent": pbu2830_Agent,
       "p7002D-5-Agent": p7002D_5_Agent,
       "p7002D-5a-Agent": p7002D_5a_Agent,
       "p7002D-1-5-Agent": p7002D_1_5_Agent,
       "p7002D-1-5a-Agent": p7002D_1_5a_Agent,
       "p7002-5-Agent": p7002_5_Agent,
       "p7002-5a-Agent": p7002_5a_Agent,
       "p7002-1a-5-Agent": p7002_1a_5_Agent,
       "p7002-1a-5s-Agent": p7002_1a_5s_Agent,
       "p7002-1a-5b-Agent": p7002_1a_5b_Agent,
       "ptr50-Agent": ptr50_Agent,
       "ptr50-1e-Agent": ptr50_1e_Agent,
       "ptr50-1c-Agent": ptr50_1c_Agent,
       "rtr50-Agent": rtr50_Agent,
       "ptr50-6-Agent": ptr50_6_Agent,
       "ptr50-1d-Agent": ptr50_1d_Agent,
       "ptr50-1d-6SU-12SU-Agent": ptr50_1d_6SU_12SU_Agent,
       "ptr50-1d-6SD-12SD-Agent": ptr50_1d_6SD_12SD_Agent,
       "tlth137-3a-Agent": tlth137_3a_Agent,
       "tlth6725-Agent": tlth6725_Agent,
       "tlth600-3a-Agent": tlth600_3a_Agent,
       "tlthsi3-Agent": tlthsi3_Agent,
       "tlth742-3d-Agent": tlth742_3d_Agent,
       "tlth137-Agent": tlth137_Agent,
       "tlth5844SA-13SA-Agent": tlth5844SA_13SA_Agent,
       "tlth6724SAa-13SA-Agent": tlth6724SAa_13SA_Agent,
       "tlth1003-Agent": tlth1003_Agent,
       "tlth1003-3c-Agent": tlth1003_3c_Agent,
       "tlth5844SA-3d-13SA-Agent": tlth5844SA_3d_13SA_Agent,
       "tltr2750-3a-Agent": tltr2750_3a_Agent,
       "tlth13761SA-13SA-Agent": tlth13761SA_13SA_Agent,
       "tltr1000SA-Agent": tltr1000SA_Agent,
       "tltr13761SA-Agent": tltr13761SA_Agent,
       "tlth1004-3e-Agent": tlth1004_3e_Agent,
       "tltr1000SD-Agent": tltr1000SD_Agent,
       "tlth184SR-Agent": tlth184SR_Agent,
       "tlth672-Agent": tlth672_Agent,
       "tltr1002SA-Agent": tltr1002SA_Agent,
       "tltr5578SI-Agent": tltr5578SI_Agent,
       "tlth3100-Agent": tlth3100_Agent,
       "tlth180-Agent": tlth180_Agent,
       "tlth2001SA-Agent": tlth2001SA_Agent,
       "tltr742-Agent": tltr742_Agent,
       "tlth127-3a-Agent": tlth127_3a_Agent,
       "tlth642ST-Agent": tlth642ST_Agent,
       "tlth1000ST-Agent": tlth1000ST_Agent,
       "tltr3100-3eSP-Agent": tltr3100_3eSP_Agent,
       "tlth790-3a-Agent": tlth790_3a_Agent,
       "tltr742-3a-13-Agent": tltr742_3a_13_Agent,
       "tltr184-3a-Agent": tltr184_3a_Agent,
       "tltr572SD2-Agent": tltr572SD2_Agent,
       "tltr1003-Agent": tltr1003_Agent,
       "tlth1000ST2-Agent": tlth1000ST2_Agent,
       "tltr2225-3d-4-5aSI-5bSI-Agent": tltr2225_3d_4_5aSI_5bSI_Agent,
       "tlth2225-3d-Agent": tlth2225_3d_Agent,
       "tlth1000ST2a-Agent": tlth1000ST2a_Agent,
       "tltr2225SD2-3d-4-Agent": tltr2225SD2_3d_4_Agent,
       "tlthsi9-Agent": tlthsi9_Agent,
       "tlth1000SA2-13-Agent": tlth1000SA2_13_Agent,
       "tltr1000SA2-13SA-Agent": tltr1000SA2_13SA_Agent,
       "tltr1004SI-Agent": tltr1004SI_Agent,
       "tltrsi3-Agent": tltrsi3_Agent,
       "tltr101SG-15SG-16SG-Agent": tltr101SG_15SG_16SG_Agent,
       "rcu100hh-Agent": rcu100hh_Agent,
       "rcu100-Agent": rcu100_Agent,
       "rcu1800-Agent": rcu1800_Agent,
       "rcu1400-Agent": rcu1400_Agent,
       "rcu1600-Agent": rcu1600_Agent,
       "rcu1401ST-Agent": rcu1401ST_Agent,
       "rcu50PO-Agent": rcu50PO_Agent,
       "rcuh200-Agent": rcuh200_Agent,
       "rcu50SP-Agent": rcu50SP_Agent,
       "rcu50-Agent": rcu50_Agent,
       "rcu50PO-10PO-Agent": rcu50PO_10PO_Agent,
       "rcuh100SO-Agent": rcuh100SO_Agent,
       "rcu1402-Agent": rcu1402_Agent,
       "rcu50PO-10PO-11PO-Agent": rcu50PO_10PO_11PO_Agent,
       "rcu50-8-10aSP-Agent": rcu50_8_10aSP_Agent,
       "rcuh100-Agent": rcuh100_Agent,
       "rcu52-Agent": rcu52_Agent,
       "rcuh50-11SO-Agent": rcuh50_11SO_Agent,
       "d600-8SB1-Agent": d600_8SB1_Agent,
       "d600-Agent": d600_Agent,
       "dbu200-6b-Agent": dbu200_6b_Agent,
       "ilah2150mt-Agent": ilah2150mt_Agent,
       "ilah2150mr-Agent": ilah2150mr_Agent,
       "upc7000-2-Agent": upc7000_2_Agent,
       "upc7001-2-5-Agent": upc7001_2_5_Agent,
       "upc7001-2-Agent": upc7001_2_Agent,
       "upc7002-2-5-Agent": upc7002_2_5_Agent,
       "ilah1450sm-Agent": ilah1450sm_Agent,
       "upc7002-5-Agent": upc7002_5_Agent,
       "ilahl2150-Agent": ilahl2150_Agent,
       "dms-rf-u-Agent": dms_rf_u_Agent,
       "upc7001-2c-5-Agent": upc7001_2c_5_Agent,
       "upc7001-2-7-5-Agent": upc7001_2_7_5_Agent,
       "mpmEmulator-Agent": mpmEmulator_Agent,
       "ilah240-10a-13-Agent": ilah240_10a_13_Agent,
       "upc7001-2-7-Agent": upc7001_2_7_Agent,
       "upc7001-Agent": upc7001_Agent,
       "upc7003-Agent": upc7003_Agent,
       "dbu200-Agent": dbu200_Agent,
       "upc7004-2-5-Agent": upc7004_2_5_Agent,
       "upc7004-2a-5-Agent": upc7004_2a_5_Agent,
       "dbu200-6-Agent": dbu200_6_Agent,
       "upc7002-2-Agent": upc7002_2_Agent,
       "s8SA-Agent": s8SA_Agent,
       "upc7001-2a-7-Agent": upc7001_2a_7_Agent,
       "upc7001-5-Agent": upc7001_5_Agent,
       "dlah200-6-Agent": dlah200_6_Agent,
       "dlah200-Agent": dlah200_Agent,
       "ilahl-1750-10a-13-14-Agent": ilahl_1750_10a_13_14_Agent,
       "dla200-6-Agent": dla200_6_Agent,
       "dla200-Agent": dla200_Agent,
       "upc7004-5-Agent": upc7004_5_Agent,
       "upc7002-Agent": upc7002_Agent,
       "isulh08-Agent": isulh08_Agent,
       "upc7004-Agent": upc7004_Agent,
       "upc7002-5-11st-Agent": upc7002_5_11st_Agent,
       "dbuh200-9-Agent": dbuh200_9_Agent,
       "dbuh200-6-9-Agent": dbuh200_6_9_Agent,
       "upc7000-2-11-Agent": upc7000_2_11_Agent,
       "upc7001-2d-5-Agent": upc7001_2d_5_Agent,
       "isb001-Agent": isb001_Agent}
)
