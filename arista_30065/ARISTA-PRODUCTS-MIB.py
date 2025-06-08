# SNMP MIB module (ARISTA-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-PRODUCTS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaModules,
 aristaProducts) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaModules",
    "aristaProducts")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
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

aristaProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 2, 1)
)
if mibBuilder.loadTexts:
    aristaProductsMIB.setRevisions(
        ("2024-12-23 00:00",
         "2024-10-07 00:00",
         "2024-08-12 00:00",
         "2024-07-31 00:01",
         "2024-07-15 00:02",
         "2024-05-03 00:00",
         "2024-05-01 00:02",
         "2024-05-01 00:00",
         "2024-03-22 00:00",
         "2024-01-30 00:00",
         "2024-01-22 00:00",
         "2024-01-19 00:05",
         "2024-01-19 00:04",
         "2024-01-19 00:03",
         "2024-01-19 00:02",
         "2024-01-19 00:01",
         "2024-01-19 00:00",
         "2024-01-12 04:18",
         "2024-01-12 04:17",
         "2024-01-12 04:15",
         "2024-01-12 00:01",
         "2024-01-11 00:02",
         "2024-01-11 00:01",
         "2024-01-11 00:00",
         "2023-12-08 00:00",
         "2023-10-19 00:00",
         "2023-10-10 00:00",
         "2023-09-08 00:00",
         "2023-08-28 00:00",
         "2023-08-09 00:02",
         "2023-08-08 00:01",
         "2023-08-07 00:00",
         "2023-08-06 00:00",
         "2023-08-05 00:00",
         "2023-08-04 00:00",
         "2023-08-03 00:01",
         "2023-08-02 00:02",
         "2023-08-01 00:00",
         "2023-07-25 00:00",
         "2023-06-19 00:00",
         "2023-06-15 00:02",
         "2023-06-15 00:01",
         "2023-06-15 00:00",
         "2023-05-11 00:00",
         "2023-05-08 00:00",
         "2023-04-06 00:00",
         "2023-04-04 00:00",
         "2023-03-23 00:01",
         "2023-03-07 00:01",
         "2023-02-10 00:01",
         "2023-01-30 00:00",
         "2023-01-12 00:02",
         "2023-01-12 00:01",
         "2023-01-12 00:00",
         "2022-09-22 00:00",
         "2022-09-20 00:00",
         "2022-08-25 00:00",
         "2022-08-24 00:00",
         "2022-08-23 00:00",
         "2022-08-03 00:00",
         "2022-07-22 00:00",
         "2022-05-16 00:00",
         "2022-04-15 12:05",
         "2022-04-15 12:04",
         "2022-04-15 12:03",
         "2022-04-15 12:02",
         "2022-04-15 12:01",
         "2022-04-15 12:00",
         "2022-04-15 11:59",
         "2022-04-15 11:58",
         "2022-04-15 11:57",
         "2022-04-15 11:56",
         "2022-04-15 11:55",
         "2022-04-15 11:54",
         "2022-04-15 11:53",
         "2022-04-15 11:52",
         "2022-04-15 11:51",
         "2022-04-15 11:50",
         "2022-04-15 11:49",
         "2022-04-15 11:48",
         "2022-04-15 11:47",
         "2022-04-15 11:46",
         "2022-04-15 11:45",
         "2022-04-15 11:44",
         "2022-04-15 11:43",
         "2022-04-15 11:42",
         "2022-04-15 11:41",
         "2022-04-15 11:40",
         "2022-04-05 00:00",
         "2022-04-01 00:00",
         "2022-02-08 00:00",
         "2022-02-02 00:05",
         "2022-02-02 00:04",
         "2022-02-02 00:03",
         "2022-02-02 00:02",
         "2022-02-02 00:01",
         "2021-11-17 00:04",
         "2021-11-17 00:03",
         "2021-11-17 00:02",
         "2021-11-17 00:01",
         "2021-11-17 00:00",
         "2021-11-11 00:00",
         "2021-10-08 00:00",
         "2021-09-09 00:00",
         "2021-09-08 00:00",
         "2021-08-24 00:01",
         "2021-08-24 00:00",
         "2021-06-24 00:00",
         "2021-06-17 00:00",
         "2021-06-02 00:00",
         "2021-06-01 00:00",
         "2021-05-30 00:00",
         "2021-05-03 00:01",
         "2021-05-03 00:00",
         "2021-03-25 00:01",
         "2021-03-25 00:00",
         "2021-02-25 00:00",
         "2021-02-17 00:00",
         "2021-02-10 00:00",
         "2020-12-11 00:00",
         "2020-12-10 00:00",
         "2020-11-18 00:00",
         "2020-10-28 00:01",
         "2020-10-28 00:00",
         "2020-10-15 00:00",
         "2020-08-06 00:00",
         "2020-07-14 00:00",
         "2020-06-24 00:00",
         "2020-06-11 00:00",
         "2020-04-22 00:01",
         "2020-04-22 00:00",
         "2020-04-20 00:00",
         "2020-04-15 00:00",
         "2020-04-14 00:00",
         "2020-02-28 00:00",
         "2020-02-07 00:00",
         "2020-01-29 00:00",
         "2020-01-08 00:00",
         "2020-01-02 00:00",
         "2019-12-23 00:00",
         "2019-10-16 00:00",
         "2019-09-19 00:00",
         "2019-08-29 00:01",
         "2019-08-29 00:00",
         "2019-08-22 00:00",
         "2019-08-16 00:00",
         "2019-08-15 00:00",
         "2019-08-13 00:00",
         "2019-06-21 00:00",
         "2019-06-12 00:00",
         "2019-06-11 00:00",
         "2019-05-21 00:00",
         "2019-05-20 00:00",
         "2019-04-23 00:00",
         "2019-04-22 00:00",
         "2019-01-23 00:00",
         "2019-01-14 00:02",
         "2019-01-14 00:01",
         "2019-01-14 00:00",
         "2018-11-15 00:00",
         "2018-11-13 00:00",
         "2018-11-12 00:00",
         "2018-11-02 00:00",
         "2018-10-11 00:00",
         "2018-09-18 00:00",
         "2018-09-05 00:00",
         "2018-09-04 00:00",
         "2018-08-25 00:00",
         "2018-08-24 00:00",
         "2018-06-18 14:00",
         "2018-05-17 00:00",
         "2018-04-09 00:00",
         "2018-03-09 00:00",
         "2018-01-18 00:00",
         "2018-01-13 00:00",
         "2017-12-11 00:00",
         "2017-12-10 00:00",
         "2017-09-22 00:00",
         "2017-09-21 00:00",
         "2017-09-18 00:00",
         "2017-09-17 00:00",
         "2017-09-03 00:00",
         "2017-08-18 00:00",
         "2017-07-05 00:00",
         "2017-05-16 00:00",
         "2017-05-08 00:00",
         "2017-05-02 00:00",
         "2017-04-27 00:00",
         "2017-03-14 00:00",
         "2017-03-09 00:00",
         "2017-02-23 00:00",
         "2017-02-22 00:00",
         "2017-01-31 00:00",
         "2017-01-30 00:00",
         "2017-01-26 00:00",
         "2017-01-12 00:00",
         "2017-01-03 00:00",
         "2016-12-15 00:00",
         "2016-12-14 00:00",
         "2016-12-13 00:00",
         "2016-12-02 00:00",
         "2016-11-30 00:00",
         "2016-11-19 00:00",
         "2016-11-15 00:00",
         "2016-11-14 04:29",
         "2016-11-14 04:24",
         "2016-10-21 00:02",
         "2016-10-21 00:00",
         "2016-10-02 00:00",
         "2016-10-01 00:00",
         "2016-09-08 00:00",
         "2016-08-08 00:00",
         "2016-05-27 00:00",
         "2016-05-11 00:00",
         "2016-03-23 00:00",
         "2016-02-02 11:30",
         "2016-01-12 00:00",
         "2016-01-05 00:00",
         "2016-01-03 00:00",
         "2015-11-16 00:00",
         "2015-10-28 00:00",
         "2015-10-12 00:00",
         "2015-10-02 17:00",
         "2015-10-02 16:00",
         "2015-09-29 00:00",
         "2015-09-15 00:00",
         "2015-06-03 00:00",
         "2015-05-27 00:00",
         "2015-04-20 00:00",
         "2015-04-10 00:00",
         "2015-03-25 12:00",
         "2015-03-25 00:00",
         "2015-03-19 00:00",
         "2015-02-11 00:00",
         "2015-02-10 00:00",
         "2014-12-02 00:00",
         "2014-08-15 00:00",
         "2014-07-31 09:30",
         "2014-07-18 09:00",
         "2014-05-19 16:00",
         "2014-04-08 16:00",
         "2014-04-04 16:09",
         "2014-04-04 16:08",
         "2014-04-02 12:00",
         "2014-04-02 11:00",
         "2014-03-11 16:00",
         "2014-01-02 16:00",
         "2014-01-01 09:00",
         "2013-11-24 09:30",
         "2013-11-24 09:00",
         "2013-11-24 08:30",
         "2013-11-24 08:00",
         "2013-11-23 12:00",
         "2013-11-23 11:30",
         "2013-11-23 11:00",
         "2013-11-19 08:00",
         "2013-11-13 08:00",
         "2013-11-01 08:00",
         "2013-10-02 08:00",
         "2013-09-26 11:20",
         "2013-06-08 08:00",
         "2013-01-26 08:00",
         "2012-12-12 12:12",
         "2012-11-28 08:00",
         "2012-09-03 08:00",
         "2012-08-31 08:00",
         "2012-04-17 08:00",
         "2012-04-03 08:00",
         "2012-03-09 08:00",
         "2012-02-20 08:00",
         "2012-02-01 08:00",
         "2011-09-01 08:00",
         "2011-08-29 08:00",
         "2011-08-04 08:00",
         "2011-07-16 14:00",
         "2011-06-22 18:00",
         "2011-03-31 13:00",
         "2011-02-24 08:00",
         "2010-10-24 16:00",
         "2010-09-17 20:40",
         "2010-04-05 09:42",
         "2010-04-05 09:41",
         "2009-06-08 15:58",
         "2009-04-17 15:05",
         "2008-09-10 14:15",
         "2008-03-03 12:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaQuestoneD3020_ObjectIdentity = ObjectIdentity
aristaQuestoneD3020 = _AristaQuestoneD3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 138, 1605, 3020)
)
_AristaLY6_ObjectIdentity = ObjectIdentity
aristaLY6 = _AristaLY6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 447, 6)
)
_AristaAWE5310_ObjectIdentity = ObjectIdentity
aristaAWE5310 = _AristaAWE5310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1082, 5310)
)
_AristaAWE5510_ObjectIdentity = ObjectIdentity
aristaAWE5510 = _AristaAWE5510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1082, 5510)
)
_AristaAWE7220RP5TH2S_ObjectIdentity = ObjectIdentity
aristaAWE7220RP5TH2S = _AristaAWE7220RP5TH2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1082, 7220, 2596, 5, 1974, 2, 3282)
)
_AristaAWE7230R4TX4S_ObjectIdentity = ObjectIdentity
aristaAWE7230R4TX4S = _AristaAWE7230R4TX4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1082, 7230, 2899, 4, 1958, 4, 3282)
)
_AristaAWE7250R16S_ObjectIdentity = ObjectIdentity
aristaAWE7250R16S = _AristaAWE7250R16S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1082, 7250, 2899, 16, 3282)
)
_AristaSmallstoneD4040_ObjectIdentity = ObjectIdentity
aristaSmallstoneD4040 = _AristaSmallstoneD4040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1470, 1605, 4040)
)
_AristaRedstoneXPD2060_ObjectIdentity = ObjectIdentity
aristaRedstoneXPD2060 = _AristaRedstoneXPD2060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1788, 858, 1605, 2060)
)
_AristaCCS710P12_ObjectIdentity = ObjectIdentity
aristaCCS710P12 = _AristaCCS710P12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 710, 2129, 12)
)
_AristaCCS710P16P_ObjectIdentity = ObjectIdentity
aristaCCS710P16P = _AristaCCS710P16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 710, 2129, 16, 2129)
)
_AristaCCS720XP24ZY4_ObjectIdentity = ObjectIdentity
aristaCCS720XP24ZY4 = _AristaCCS720XP24ZY4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 24, 213, 4)
)
_AristaCCS720XP24Y6_ObjectIdentity = ObjectIdentity
aristaCCS720XP24Y6 = _AristaCCS720XP24Y6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 24, 2600, 6)
)
_AristaCCS720XP48ZC2_ObjectIdentity = ObjectIdentity
aristaCCS720XP48ZC2 = _AristaCCS720XP48ZC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 48, 207, 2)
)
_AristaCCS720XP48TXH2CS_ObjectIdentity = ObjectIdentity
aristaCCS720XP48TXH2CS = _AristaCCS720XP48TXH2CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 48, 2137, 2, 2878, 3282)
)
_AristaCCS720XP48Y6_ObjectIdentity = ObjectIdentity
aristaCCS720XP48Y6 = _AristaCCS720XP48Y6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 48, 2600, 6)
)
_AristaCCS720XP96ZC2_ObjectIdentity = ObjectIdentity
aristaCCS720XP96ZC2 = _AristaCCS720XP96ZC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 96, 207, 2)
)
_AristaCCS720XP96ZC2MS_ObjectIdentity = ObjectIdentity
aristaCCS720XP96ZC2MS = _AristaCCS720XP96ZC2MS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 858, 96, 207, 2, 972, 3282)
)
_AristaCCS720DF48Y_ObjectIdentity = ObjectIdentity
aristaCCS720DF48Y = _AristaCCS720DF48Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2952, 48, 2600)
)
_AristaCCS720DF48Y2_ObjectIdentity = ObjectIdentity
aristaCCS720DF48Y2 = _AristaCCS720DF48Y2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2952, 48, 2600, 2)
)
_AristaCCS720DF48YMS2_ObjectIdentity = ObjectIdentity
aristaCCS720DF48YMS2 = _AristaCCS720DF48YMS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2952, 48, 2600, 972, 3282, 2)
)
_AristaCCS720DF48YDC_ObjectIdentity = ObjectIdentity
aristaCCS720DF48YDC = _AristaCCS720DF48YDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2952, 48, 2600, 2957)
)
_AristaCCS720DF48YDC2_ObjectIdentity = ObjectIdentity
aristaCCS720DF48YDC2 = _AristaCCS720DF48YDC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2952, 48, 2600, 2957, 2)
)
_AristaCCS720DT24S_ObjectIdentity = ObjectIdentity
aristaCCS720DT24S = _AristaCCS720DT24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2970, 24, 3282)
)
_AristaCCS720DT24S2_ObjectIdentity = ObjectIdentity
aristaCCS720DT24S2 = _AristaCCS720DT24S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2970, 24, 3282, 2)
)
_AristaCCS720DT24SMS2_ObjectIdentity = ObjectIdentity
aristaCCS720DT24SMS2 = _AristaCCS720DT24SMS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2970, 24, 3282, 972, 3282, 2)
)
_AristaCCS720DT48S_ObjectIdentity = ObjectIdentity
aristaCCS720DT48S = _AristaCCS720DT48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2970, 48, 3282)
)
_AristaCCS720DT48S2_ObjectIdentity = ObjectIdentity
aristaCCS720DT48S2 = _AristaCCS720DT48S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2970, 48, 3282, 2)
)
_AristaCCS720DP24ZS_ObjectIdentity = ObjectIdentity
aristaCCS720DP24ZS = _AristaCCS720DP24ZS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 24, 223)
)
_AristaCCS720DP24ZS2_ObjectIdentity = ObjectIdentity
aristaCCS720DP24ZS2 = _AristaCCS720DP24ZS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 24, 223, 2)
)
_AristaCCS720DP24S_ObjectIdentity = ObjectIdentity
aristaCCS720DP24S = _AristaCCS720DP24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 24, 3282)
)
_AristaCCS720DP24S2_ObjectIdentity = ObjectIdentity
aristaCCS720DP24S2 = _AristaCCS720DP24S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 24, 3282, 2)
)
_AristaCCS720DP24SMS2_ObjectIdentity = ObjectIdentity
aristaCCS720DP24SMS2 = _AristaCCS720DP24SMS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 24, 3282, 972, 3282, 2)
)
_AristaCCS720DP48ZS_ObjectIdentity = ObjectIdentity
aristaCCS720DP48ZS = _AristaCCS720DP48ZS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 48, 223)
)
_AristaCCS720DP48ZS2_ObjectIdentity = ObjectIdentity
aristaCCS720DP48ZS2 = _AristaCCS720DP48ZS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 48, 223, 2)
)
_AristaCCS720DP48S_ObjectIdentity = ObjectIdentity
aristaCCS720DP48S = _AristaCCS720DP48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 48, 3282)
)
_AristaCCS720DP48S2_ObjectIdentity = ObjectIdentity
aristaCCS720DP48S2 = _AristaCCS720DP48S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 48, 3282, 2)
)
_AristaCCS720DP48SMS2_ObjectIdentity = ObjectIdentity
aristaCCS720DP48SMS2 = _AristaCCS720DP48SMS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 720, 2974, 48, 3282, 972, 3282, 2)
)
_AristaCCS722XPM48ZY8_ObjectIdentity = ObjectIdentity
aristaCCS722XPM48ZY8 = _AristaCCS722XPM48ZY8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 722, 4026, 48, 213, 8)
)
_AristaCCS722XPM48Y4_ObjectIdentity = ObjectIdentity
aristaCCS722XPM48Y4 = _AristaCCS722XPM48Y4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 722, 4026, 48, 2600, 4)
)
_AristaCCS755CH_ObjectIdentity = ObjectIdentity
aristaCCS755CH = _AristaCCS755CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 755, 2749)
)
_AristaCCS758CH_ObjectIdentity = ObjectIdentity
aristaCCS758CH = _AristaCCS758CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2546, 758, 2749)
)
_AristaCVX_ObjectIdentity = ObjectIdentity
aristaCVX = _AristaCVX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2682)
)
_AristavEOS_ObjectIdentity = ObjectIdentity
aristavEOS = _AristavEOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2759)
)
_AristaDCS7010T48_ObjectIdentity = ObjectIdentity
aristaDCS7010T48 = _AristaDCS7010T48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 427, 48)
)
_AristaDCS7010T48DC_ObjectIdentity = ObjectIdentity
aristaDCS7010T48DC = _AristaDCS7010T48DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 427, 48, 2957)
)
_AristaDCS7010TX48_ObjectIdentity = ObjectIdentity
aristaDCS7010TX48 = _AristaDCS7010TX48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 1958, 48)
)
_AristaDCS7010TX48C_ObjectIdentity = ObjectIdentity
aristaDCS7010TX48C = _AristaDCS7010TX48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 1958, 48, 2878)
)
_AristaDCS7010TX48CDC_ObjectIdentity = ObjectIdentity
aristaDCS7010TX48CDC = _AristaDCS7010TX48CDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 1958, 48, 2878, 2957)
)
_AristaDCS7010TX48CDCRV3_ObjectIdentity = ObjectIdentity
aristaDCS7010TX48CDCRV3 = _AristaDCS7010TX48CDCRV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 1958, 48, 2878, 2957, 2594, 3)
)
_AristaDCS7010TX48DC_ObjectIdentity = ObjectIdentity
aristaDCS7010TX48DC = _AristaDCS7010TX48DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 1958, 48, 2957)
)
_AristaDCS7020TRA48_ObjectIdentity = ObjectIdentity
aristaDCS7020TRA48 = _AristaDCS7020TRA48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 312, 48)
)
_AristaDCS7020SRG24C2_ObjectIdentity = ObjectIdentity
aristaDCS7020SRG24C2 = _AristaDCS7020SRG24C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 1349, 24, 2878, 2)
)
_AristaDCS7020TR48_ObjectIdentity = ObjectIdentity
aristaDCS7020TR48 = _AristaDCS7020TR48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 1964, 48)
)
_AristaDCS7020SR24C2_ObjectIdentity = ObjectIdentity
aristaDCS7020SR24C2 = _AristaDCS7020SR24C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 3735, 24, 2878, 2)
)
_AristaDCS7020SR32C2_ObjectIdentity = ObjectIdentity
aristaDCS7020SR32C2 = _AristaDCS7020SR32C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 3735, 32, 2878, 2)
)
_AristaDCS7048T4S_ObjectIdentity = ObjectIdentity
aristaDCS7048T4S = _AristaDCS7048T4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7048, 427, 4, 3282)
)
_AristaDCS7048TA_ObjectIdentity = ObjectIdentity
aristaDCS7048TA = _AristaDCS7048TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7048, 427, 3648)
)
_AristaDCS7050SPX448D8_ObjectIdentity = ObjectIdentity
aristaDCS7050SPX448D8 = _AristaDCS7050SPX448D8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 32, 4, 48, 1605, 8)
)
_AristaDCS7050T36_ObjectIdentity = ObjectIdentity
aristaDCS7050T36 = _AristaDCS7050T36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 36)
)
_AristaDCS7050T52_ObjectIdentity = ObjectIdentity
aristaDCS7050T52 = _AristaDCS7050T52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 52)
)
_AristaDCS7050T52SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050T52SSD = _AristaDCS7050T52SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 52, 761)
)
_AristaDCS7050T64_ObjectIdentity = ObjectIdentity
aristaDCS7050T64 = _AristaDCS7050T64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 64)
)
_AristaDCS7050T64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050T64SSD = _AristaDCS7050T64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 64, 761)
)
_AristaDCS7050TX2128_ObjectIdentity = ObjectIdentity
aristaDCS7050TX2128 = _AristaDCS7050TX2128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 2, 128)
)
_AristaDCS7050TX2128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX2128SSD = _AristaDCS7050TX2128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 2, 128, 761)
)
_AristaDCS7050TX348C8_ObjectIdentity = ObjectIdentity
aristaDCS7050TX348C8 = _AristaDCS7050TX348C8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 3, 48, 2878, 8)
)
_AristaDCS7050TX348C8SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX348C8SSD = _AristaDCS7050TX348C8SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 3, 48, 2878, 8, 761)
)
_AristaDCS7050TX48_ObjectIdentity = ObjectIdentity
aristaDCS7050TX48 = _AristaDCS7050TX48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 48)
)
_AristaDCS7050TX48SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX48SSD = _AristaDCS7050TX48SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 48, 761)
)
_AristaDCS7050TX64_ObjectIdentity = ObjectIdentity
aristaDCS7050TX64 = _AristaDCS7050TX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 64)
)
_AristaDCS7050TX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX64SSD = _AristaDCS7050TX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 64, 761)
)
_AristaDCS7050TX72_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72 = _AristaDCS7050TX72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72)
)
_AristaDCS7050TX72SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72SSD = _AristaDCS7050TX72SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 761)
)
_AristaDCS7050TX72Q_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72Q = _AristaDCS7050TX72Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 2512)
)
_AristaDCS7050TX72QSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72QSSD = _AristaDCS7050TX72QSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 2512, 761)
)
_AristaDCS7050TX96_ObjectIdentity = ObjectIdentity
aristaDCS7050TX96 = _AristaDCS7050TX96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 96)
)
_AristaDCS7050TX96SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX96SSD = _AristaDCS7050TX96SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 96, 761)
)
_AristaDCS7050TX128_ObjectIdentity = ObjectIdentity
aristaDCS7050TX128 = _AristaDCS7050TX128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 128)
)
_AristaDCS7050TX128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX128SSD = _AristaDCS7050TX128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 128, 761)
)
_AristaDCS7050Q16_ObjectIdentity = ObjectIdentity
aristaDCS7050Q16 = _AristaDCS7050Q16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2512, 16)
)
_AristaDCS7050Q16SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050Q16SSD = _AristaDCS7050Q16SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2512, 16, 761)
)
_AristaDCS7050CX332C_ObjectIdentity = ObjectIdentity
aristaDCS7050CX332C = _AristaDCS7050CX332C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 3, 32, 2878)
)
_AristaDCS7050CX332S_ObjectIdentity = ObjectIdentity
aristaDCS7050CX332S = _AristaDCS7050CX332S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 3, 32, 3282)
)
_AristaDCS7050CX332SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050CX332SSSD = _AristaDCS7050CX332SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 3, 32, 3282, 761)
)
_AristaDCS7050CX3M32S_ObjectIdentity = ObjectIdentity
aristaDCS7050CX3M32S = _AristaDCS7050CX3M32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 3, 972, 32, 3282)
)
_AristaDCS7050CX424D8_ObjectIdentity = ObjectIdentity
aristaDCS7050CX424D8 = _AristaDCS7050CX424D8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 4, 24, 1605, 8)
)
_AristaDCS7050CX440D_ObjectIdentity = ObjectIdentity
aristaDCS7050CX440D = _AristaDCS7050CX440D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 4, 40, 1605)
)
_AristaDCS7050CX4M48D8_ObjectIdentity = ObjectIdentity
aristaDCS7050CX4M48D8 = _AristaDCS7050CX4M48D8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2733, 4, 972, 48, 1605, 8)
)
_AristaDCS7050DX432S_ObjectIdentity = ObjectIdentity
aristaDCS7050DX432S = _AristaDCS7050DX432S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2966, 4, 32, 3282)
)
_AristaDCS7050DX4M32S_ObjectIdentity = ObjectIdentity
aristaDCS7050DX4M32S = _AristaDCS7050DX4M32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2966, 4, 972, 32, 3282)
)
_AristaDCS7050QX232S_ObjectIdentity = ObjectIdentity
aristaDCS7050QX232S = _AristaDCS7050QX232S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 2, 32, 3282)
)
_AristaDCS7050QX232SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX232SSSD = _AristaDCS7050QX232SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 2, 32, 3282, 761)
)
_AristaDCS7050QX32_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32 = _AristaDCS7050QX32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32)
)
_AristaDCS7050QX32SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32SSD = _AristaDCS7050QX32SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 761)
)
_AristaDCS7050QX32CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32CLSSD = _AristaDCS7050QX32CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 2745, 761)
)
_AristaDCS7050QX32S_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32S = _AristaDCS7050QX32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 3282)
)
_AristaDCS7050QX32SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32SSSD = _AristaDCS7050QX32SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 3282, 761)
)
_AristaDCS7050PX432S_ObjectIdentity = ObjectIdentity
aristaDCS7050PX432S = _AristaDCS7050PX432S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3242, 4, 32, 3282)
)
_AristaDCS7050S52_ObjectIdentity = ObjectIdentity
aristaDCS7050S52 = _AristaDCS7050S52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 52)
)
_AristaDCS7050S52SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050S52SSD = _AristaDCS7050S52SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 52, 761)
)
_AristaDCS7050S64_ObjectIdentity = ObjectIdentity
aristaDCS7050S64 = _AristaDCS7050S64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 64)
)
_AristaDCS7050S64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050S64SSD = _AristaDCS7050S64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 64, 761)
)
_AristaDCS7050SDX448D8_ObjectIdentity = ObjectIdentity
aristaDCS7050SDX448D8 = _AristaDCS7050SDX448D8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3564, 4, 48, 1605, 8)
)
_AristaDCS7050SX272Q_ObjectIdentity = ObjectIdentity
aristaDCS7050SX272Q = _AristaDCS7050SX272Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 72, 2512)
)
_AristaDCS7050SX272QSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX272QSSD = _AristaDCS7050SX272QSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 72, 2512, 761)
)
_AristaDCS7050SX2128_ObjectIdentity = ObjectIdentity
aristaDCS7050SX2128 = _AristaDCS7050SX2128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 128)
)
_AristaDCS7050SX2128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX2128SSD = _AristaDCS7050SX2128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 128, 761)
)
_AristaDCS7050SX324YC4CS_ObjectIdentity = ObjectIdentity
aristaDCS7050SX324YC4CS = _AristaDCS7050SX324YC4CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 24, 1654, 4, 2878, 3282)
)
_AristaDCS7050SX348YC8_ObjectIdentity = ObjectIdentity
aristaDCS7050SX348YC8 = _AristaDCS7050SX348YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 48, 1654, 8)
)
_AristaDCS7050SX348YC8C_ObjectIdentity = ObjectIdentity
aristaDCS7050SX348YC8C = _AristaDCS7050SX348YC8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 48, 1654, 8, 2878)
)
_AristaDCS7050SX348YC12_ObjectIdentity = ObjectIdentity
aristaDCS7050SX348YC12 = _AristaDCS7050SX348YC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 48, 1654, 12)
)
_AristaDCS7050SX348YC12SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX348YC12SSD = _AristaDCS7050SX348YC12SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 48, 1654, 12, 761)
)
_AristaDCS7050SX348C8_ObjectIdentity = ObjectIdentity
aristaDCS7050SX348C8 = _AristaDCS7050SX348C8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 48, 2878, 8)
)
_AristaDCS7050SX348C8C_ObjectIdentity = ObjectIdentity
aristaDCS7050SX348C8C = _AristaDCS7050SX348C8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 48, 2878, 8, 2878)
)
_AristaDCS7050SX396YC8_ObjectIdentity = ObjectIdentity
aristaDCS7050SX396YC8 = _AristaDCS7050SX396YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 3, 96, 1654, 8)
)
_AristaDCS7050SX64_ObjectIdentity = ObjectIdentity
aristaDCS7050SX64 = _AristaDCS7050SX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 64)
)
_AristaDCS7050SX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX64SSD = _AristaDCS7050SX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 64, 761)
)
_AristaDCS7050SX72_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72 = _AristaDCS7050SX72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72)
)
_AristaDCS7050SX72SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72SSD = _AristaDCS7050SX72SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 761)
)
_AristaDCS7050SX72Q_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72Q = _AristaDCS7050SX72Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 2512)
)
_AristaDCS7050SX72QSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72QSSD = _AristaDCS7050SX72QSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 2512, 761)
)
_AristaDCS7050SX96_ObjectIdentity = ObjectIdentity
aristaDCS7050SX96 = _AristaDCS7050SX96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 96)
)
_AristaDCS7050SX96SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX96SSD = _AristaDCS7050SX96SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 96, 761)
)
_AristaDCS7050SX128_ObjectIdentity = ObjectIdentity
aristaDCS7050SX128 = _AristaDCS7050SX128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 128)
)
_AristaDCS7050SX128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX128SSD = _AristaDCS7050SX128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 128, 761)
)
_AristaDCS7060CX232S_ObjectIdentity = ObjectIdentity
aristaDCS7060CX232S = _AristaDCS7060CX232S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 2, 32, 3282)
)
_AristaDCS7060CX556D8_ObjectIdentity = ObjectIdentity
aristaDCS7060CX556D8 = _AristaDCS7060CX556D8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 5, 56, 1605, 8)
)
_AristaDCS7060CX32C_ObjectIdentity = ObjectIdentity
aristaDCS7060CX32C = _AristaDCS7060CX32C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 32, 2878)
)
_AristaDCS7060CX32S_ObjectIdentity = ObjectIdentity
aristaDCS7060CX32S = _AristaDCS7060CX32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 32, 3282)
)
_AristaDCS7060CX32SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7060CX32SSSD = _AristaDCS7060CX32SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 32, 3282, 761)
)
_AristaDCS7060CX32SES_ObjectIdentity = ObjectIdentity
aristaDCS7060CX32SES = _AristaDCS7060CX32SES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 32, 3282, 3362)
)
_AristaDCS7060DX432_ObjectIdentity = ObjectIdentity
aristaDCS7060DX432 = _AristaDCS7060DX432_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 4, 32)
)
_AristaDCS7060DX432D_ObjectIdentity = ObjectIdentity
aristaDCS7060DX432D = _AristaDCS7060DX432D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 4, 32, 1605)
)
_AristaDCS7060DX432CRV3_ObjectIdentity = ObjectIdentity
aristaDCS7060DX432CRV3 = _AristaDCS7060DX432CRV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 4, 32, 2878, 2594, 3)
)
_AristaDCS7060DX432S_ObjectIdentity = ObjectIdentity
aristaDCS7060DX432S = _AristaDCS7060DX432S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 4, 32, 3282)
)
_AristaDCS7060DX432SBRV3_ObjectIdentity = ObjectIdentity
aristaDCS7060DX432SBRV3 = _AristaDCS7060DX432SBRV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 4, 32, 3719, 2594, 3)
)
_AristaDCS7060DX532_ObjectIdentity = ObjectIdentity
aristaDCS7060DX532 = _AristaDCS7060DX532_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 5, 32)
)
_AristaDCS7060DX564_ObjectIdentity = ObjectIdentity
aristaDCS7060DX564 = _AristaDCS7060DX564_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 5, 64)
)
_AristaDCS7060DX564E_ObjectIdentity = ObjectIdentity
aristaDCS7060DX564E = _AristaDCS7060DX564E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 5, 64, 1988)
)
_AristaDCS7060DX564S_ObjectIdentity = ObjectIdentity
aristaDCS7060DX564S = _AristaDCS7060DX564S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2966, 5, 64, 3282)
)
_AristaDCS7060X632PE_ObjectIdentity = ObjectIdentity
aristaDCS7060X632PE = _AristaDCS7060X632PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2983, 6, 32, 3255)
)
_AristaDCS7060X664DE_ObjectIdentity = ObjectIdentity
aristaDCS7060X664DE = _AristaDCS7060X664DE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2983, 6, 64, 2955)
)
_AristaDCS7060X664PE_ObjectIdentity = ObjectIdentity
aristaDCS7060X664PE = _AristaDCS7060X664PE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2983, 6, 64, 3255)
)
_AristaDCS7060PX432_ObjectIdentity = ObjectIdentity
aristaDCS7060PX432 = _AristaDCS7060PX432_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 3242, 4, 32)
)
_AristaDCS7060PX432S_ObjectIdentity = ObjectIdentity
aristaDCS7060PX432S = _AristaDCS7060PX432S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 3242, 4, 32, 3282)
)
_AristaDCS7060PX564E_ObjectIdentity = ObjectIdentity
aristaDCS7060PX564E = _AristaDCS7060PX564E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 3242, 5, 64, 1988)
)
_AristaDCS7060SX248YC6_ObjectIdentity = ObjectIdentity
aristaDCS7060SX248YC6 = _AristaDCS7060SX248YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 3741, 2, 48, 1654, 6)
)
_AristaDCS7060SX248YC6SSD_ObjectIdentity = ObjectIdentity
aristaDCS7060SX248YC6SSD = _AristaDCS7060SX248YC6SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 3741, 2, 48, 1654, 6, 761)
)
_AristaDCS7120T4S_ObjectIdentity = ObjectIdentity
aristaDCS7120T4S = _AristaDCS7120T4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7120, 427, 4, 3282)
)
_AristaDCS7124FX_ObjectIdentity = ObjectIdentity
aristaDCS7124FX = _AristaDCS7124FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 2312)
)
_AristaDCS7124FXCL_ObjectIdentity = ObjectIdentity
aristaDCS7124FXCL = _AristaDCS7124FXCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 2312, 2745)
)
_AristaDCS7124S_ObjectIdentity = ObjectIdentity
aristaDCS7124S = _AristaDCS7124S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3282)
)
_AristaDCS7124SX_ObjectIdentity = ObjectIdentity
aristaDCS7124SX = _AristaDCS7124SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3741)
)
_AristaDCS7124SXSSD_ObjectIdentity = ObjectIdentity
aristaDCS7124SXSSD = _AristaDCS7124SXSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3741, 761)
)
_AristaDCS713016G3_ObjectIdentity = ObjectIdentity
aristaDCS713016G3 = _AristaDCS713016G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 16, 2758, 3)
)
_AristaDCS713016G3S_ObjectIdentity = ObjectIdentity
aristaDCS713016G3S = _AristaDCS713016G3S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 16, 2758, 3, 3282)
)
_AristaDCS713048LB_ObjectIdentity = ObjectIdentity
aristaDCS713048LB = _AristaDCS713048LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 420)
)
_AristaDCS713048LA_ObjectIdentity = ObjectIdentity
aristaDCS713048LA = _AristaDCS713048LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 423)
)
_AristaDCS713048LS_ObjectIdentity = ObjectIdentity
aristaDCS713048LS = _AristaDCS713048LS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 437)
)
_AristaDCS713048L_ObjectIdentity = ObjectIdentity
aristaDCS713048L = _AristaDCS713048L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 589)
)
_AristaDCS713048LBA_ObjectIdentity = ObjectIdentity
aristaDCS713048LBA = _AristaDCS713048LBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 1488)
)
_AristaDCS713048LBS_ObjectIdentity = ObjectIdentity
aristaDCS713048LBS = _AristaDCS713048LBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 1502)
)
_AristaDCS713048LAS_ObjectIdentity = ObjectIdentity
aristaDCS713048LAS = _AristaDCS713048LAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 1921)
)
_AristaDCS713048E_ObjectIdentity = ObjectIdentity
aristaDCS713048E = _AristaDCS713048E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 1988)
)
_AristaDCS713048EHS_ObjectIdentity = ObjectIdentity
aristaDCS713048EHS = _AristaDCS713048EHS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 2117)
)
_AristaDCS713048G3_ObjectIdentity = ObjectIdentity
aristaDCS713048G3 = _AristaDCS713048G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 2758, 3)
)
_AristaDCS713048G3S_ObjectIdentity = ObjectIdentity
aristaDCS713048G3S = _AristaDCS713048G3S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 2758, 3, 3282)
)
_AristaDCS713048EH_ObjectIdentity = ObjectIdentity
aristaDCS713048EH = _AristaDCS713048EH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 3387)
)
_AristaDCS713048LBAS_ObjectIdentity = ObjectIdentity
aristaDCS713048LBAS = _AristaDCS713048LBAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 48, 3826)
)
_AristaDCS713096_ObjectIdentity = ObjectIdentity
aristaDCS713096 = _AristaDCS713096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96)
)
_AristaDCS713096LB_ObjectIdentity = ObjectIdentity
aristaDCS713096LB = _AristaDCS713096LB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 420)
)
_AristaDCS713096LA_ObjectIdentity = ObjectIdentity
aristaDCS713096LA = _AristaDCS713096LA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 423)
)
_AristaDCS713096LS_ObjectIdentity = ObjectIdentity
aristaDCS713096LS = _AristaDCS713096LS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 437)
)
_AristaDCS713096L_ObjectIdentity = ObjectIdentity
aristaDCS713096L = _AristaDCS713096L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 589)
)
_AristaDCS713096LBA_ObjectIdentity = ObjectIdentity
aristaDCS713096LBA = _AristaDCS713096LBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 1488)
)
_AristaDCS713096LBS_ObjectIdentity = ObjectIdentity
aristaDCS713096LBS = _AristaDCS713096LBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 1502)
)
_AristaDCS713096LAS_ObjectIdentity = ObjectIdentity
aristaDCS713096LAS = _AristaDCS713096LAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 1921)
)
_AristaDCS713096E_ObjectIdentity = ObjectIdentity
aristaDCS713096E = _AristaDCS713096E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 1988)
)
_AristaDCS713096S_ObjectIdentity = ObjectIdentity
aristaDCS713096S = _AristaDCS713096S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 3282)
)
_AristaDCS713096LBAS_ObjectIdentity = ObjectIdentity
aristaDCS713096LBAS = _AristaDCS713096LBAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 96, 3826)
)
_AristaDCS7130LBR48S6QD_ObjectIdentity = ObjectIdentity
aristaDCS7130LBR48S6QD = _AristaDCS7130LBR48S6QD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 1501, 48, 3282, 6, 3083)
)
_AristaDCS7130LBR48S6QDMD_ObjectIdentity = ObjectIdentity
aristaDCS7130LBR48S6QDMD = _AristaDCS7130LBR48S6QDMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 1501, 48, 3282, 6, 3083, 1823)
)
_AristaDCS7130B32QD_ObjectIdentity = ObjectIdentity
aristaDCS7130B32QD = _AristaDCS7130B32QD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7130, 3261, 32, 3083)
)
_AristaDCS7132LB48Y4C_ObjectIdentity = ObjectIdentity
aristaDCS7132LB48Y4C = _AristaDCS7132LB48Y4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7132, 420, 48, 2600, 4, 2878)
)
_AristaDCS7135LB48Y4C_ObjectIdentity = ObjectIdentity
aristaDCS7135LB48Y4C = _AristaDCS7135LB48Y4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7135, 420, 48, 2600, 4, 2878)
)
_AristaDCS7140T8S_ObjectIdentity = ObjectIdentity
aristaDCS7140T8S = _AristaDCS7140T8S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7140, 427, 8, 3282)
)
_AristaDCS7148S_ObjectIdentity = ObjectIdentity
aristaDCS7148S = _AristaDCS7148S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7148, 3282)
)
_AristaDCS7148SX_ObjectIdentity = ObjectIdentity
aristaDCS7148SX = _AristaDCS7148SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7148, 3741)
)
_AristaDCS7150S24_ObjectIdentity = ObjectIdentity
aristaDCS7150S24 = _AristaDCS7150S24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24)
)
_AristaDCS7150S24CL_ObjectIdentity = ObjectIdentity
aristaDCS7150S24CL = _AristaDCS7150S24CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24, 2745)
)
_AristaDCS7150S24CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7150S24CLSSD = _AristaDCS7150S24CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24, 2745, 761)
)
_AristaDCS7150S52CL_ObjectIdentity = ObjectIdentity
aristaDCS7150S52CL = _AristaDCS7150S52CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 52, 2745)
)
_AristaDCS7150S52CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7150S52CLSSD = _AristaDCS7150S52CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 52, 2745, 761)
)
_AristaDCS7150S64CL_ObjectIdentity = ObjectIdentity
aristaDCS7150S64CL = _AristaDCS7150S64CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 64, 2745)
)
_AristaDCS7150S64CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7150S64CLSSD = _AristaDCS7150S64CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 64, 2745, 761)
)
_AristaDCS7150SC24CLD_ObjectIdentity = ObjectIdentity
aristaDCS7150SC24CLD = _AristaDCS7150SC24CLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3720, 24, 1208)
)
_AristaDCS7150SC64CLD_ObjectIdentity = ObjectIdentity
aristaDCS7150SC64CLD = _AristaDCS7150SC64CLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3720, 64, 1208)
)
_AristaDCS716032CQ_ObjectIdentity = ObjectIdentity
aristaDCS716032CQ = _AristaDCS716032CQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 32, 2726)
)
_AristaDCS716032CQSSD_ObjectIdentity = ObjectIdentity
aristaDCS716032CQSSD = _AristaDCS716032CQSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 32, 2726, 761)
)
_AristaDCS716048YC6_ObjectIdentity = ObjectIdentity
aristaDCS716048YC6 = _AristaDCS716048YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1654, 6)
)
_AristaDCS716048YC6SSD_ObjectIdentity = ObjectIdentity
aristaDCS716048YC6SSD = _AristaDCS716048YC6SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1654, 6, 761)
)
_AristaDCS716048TC6_ObjectIdentity = ObjectIdentity
aristaDCS716048TC6 = _AristaDCS716048TC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1981, 6)
)
_AristaDCS716048TC6SSD_ObjectIdentity = ObjectIdentity
aristaDCS716048TC6SSD = _AristaDCS716048TC6SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1981, 6, 761)
)
_AristaDCS716064YC16_ObjectIdentity = ObjectIdentity
aristaDCS716064YC16 = _AristaDCS716064YC16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 64, 1654, 16)
)
_AristaDCS717032CD_ObjectIdentity = ObjectIdentity
aristaDCS717032CD = _AristaDCS717032CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 32, 2737)
)
_AristaDCS717032CDM_ObjectIdentity = ObjectIdentity
aristaDCS717032CDM = _AristaDCS717032CDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 32, 2737, 972)
)
_AristaDCS717032C_ObjectIdentity = ObjectIdentity
aristaDCS717032C = _AristaDCS717032C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 32, 2878)
)
_AristaDCS717032CM_ObjectIdentity = ObjectIdentity
aristaDCS717032CM = _AristaDCS717032CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 32, 2878, 972)
)
_AristaDCS717064C_ObjectIdentity = ObjectIdentity
aristaDCS717064C = _AristaDCS717064C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 64, 2878)
)
_AristaDCS717064CM_ObjectIdentity = ObjectIdentity
aristaDCS717064CM = _AristaDCS717064CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 64, 2878, 972)
)
_AristaDCS7170B64C_ObjectIdentity = ObjectIdentity
aristaDCS7170B64C = _AristaDCS7170B64C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 3261, 64, 2878)
)
_AristaDCS7170B64CM_ObjectIdentity = ObjectIdentity
aristaDCS7170B64CM = _AristaDCS7170B64CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7170, 3261, 64, 2878, 972)
)
_AristaDCS7250QX64_ObjectIdentity = ObjectIdentity
aristaDCS7250QX64 = _AristaDCS7250QX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64)
)
_AristaDCS7250QX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7250QX64SSD = _AristaDCS7250QX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64, 761)
)
_AristaDCS7250QX64M_ObjectIdentity = ObjectIdentity
aristaDCS7250QX64M = _AristaDCS7250QX64M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64, 972)
)
_AristaDCS7260CX364_ObjectIdentity = ObjectIdentity
aristaDCS7260CX364 = _AristaDCS7260CX364_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 3, 64)
)
_AristaDCS7260CX364LQ_ObjectIdentity = ObjectIdentity
aristaDCS7260CX364LQ = _AristaDCS7260CX364LQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 3, 64, 439)
)
_AristaDCS7260CX364SSD_ObjectIdentity = ObjectIdentity
aristaDCS7260CX364SSD = _AristaDCS7260CX364SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 3, 64, 761)
)
_AristaDCS7260CX364E_ObjectIdentity = ObjectIdentity
aristaDCS7260CX364E = _AristaDCS7260CX364E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 3, 64, 1988)
)
_AristaDCS7260CX64_ObjectIdentity = ObjectIdentity
aristaDCS7260CX64 = _AristaDCS7260CX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 64)
)
_AristaDCS7260CX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7260CX64SSD = _AristaDCS7260CX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 64, 761)
)
_AristaDCS7260QX64_ObjectIdentity = ObjectIdentity
aristaDCS7260QX64 = _AristaDCS7260QX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 3095, 64)
)
_AristaDCS7260QX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7260QX64SSD = _AristaDCS7260QX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 3095, 64, 761)
)
_AristaDCS7280TRA48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280TRA48C6 = _AristaDCS7280TRA48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 312, 48, 2878, 6)
)
_AristaDCS7280TRA48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280TRA48C6M = _AristaDCS7280TRA48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 312, 48, 2878, 6, 972)
)
_AristaDCS7280CRA48_ObjectIdentity = ObjectIdentity
aristaDCS7280CRA48 = _AristaDCS7280CRA48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 877, 48)
)
_AristaDCS7280CRA48M_ObjectIdentity = ObjectIdentity
aristaDCS7280CRA48M = _AristaDCS7280CRA48M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 877, 48, 972)
)
_AristaDCS7280SRA48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280SRA48C6 = _AristaDCS7280SRA48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1347, 48, 2878, 6)
)
_AristaDCS7280SRA48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SRA48C6M = _AristaDCS7280SRA48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1347, 48, 2878, 6, 972)
)
_AristaDCS7280SRM40CX2_ObjectIdentity = ObjectIdentity
aristaDCS7280SRM40CX2 = _AristaDCS7280SRM40CX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1359, 40, 2733, 2)
)
_AristaDCS7280TR340C6_ObjectIdentity = ObjectIdentity
aristaDCS7280TR340C6 = _AristaDCS7280TR340C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1964, 3, 40, 2878, 6)
)
_AristaDCS7280TR48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280TR48C6 = _AristaDCS7280TR48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1964, 48, 2878, 6)
)
_AristaDCS7280TR48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280TR48C6M = _AristaDCS7280TR48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1964, 48, 2878, 6, 972)
)
_AristaDCS7280QRAC36S_ObjectIdentity = ObjectIdentity
aristaDCS7280QRAC36S = _AristaDCS7280QRAC36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2655, 2878, 36, 3282)
)
_AristaDCS7280QRAC36SM_ObjectIdentity = ObjectIdentity
aristaDCS7280QRAC36SM = _AristaDCS7280QRAC36SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2655, 2878, 36, 3282, 972)
)
_AristaDCS7280QRAC72_ObjectIdentity = ObjectIdentity
aristaDCS7280QRAC72 = _AristaDCS7280QRAC72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2655, 2878, 72)
)
_AristaDCS7280QRAC72M_ObjectIdentity = ObjectIdentity
aristaDCS7280QRAC72M = _AristaDCS7280QRAC72M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2655, 2878, 72, 972)
)
_AristaDCS7280CR260_ObjectIdentity = ObjectIdentity
aristaDCS7280CR260 = _AristaDCS7280CR260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 60)
)
_AristaDCS7280CR260SSD_ObjectIdentity = ObjectIdentity
aristaDCS7280CR260SSD = _AristaDCS7280CR260SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 60, 761)
)
_AristaDCS7280CR2K30_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2K30 = _AristaDCS7280CR2K30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 202, 30)
)
_AristaDCS7280CR2K60_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2K60 = _AristaDCS7280CR2K60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 202, 60)
)
_AristaDCS7280CR2K60SSD_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2K60SSD = _AristaDCS7280CR2K60SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 202, 60, 761)
)
_AristaDCS7280CR2M30_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2M30 = _AristaDCS7280CR2M30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 972, 30)
)
_AristaDCS7280CR2A30_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2A30 = _AristaDCS7280CR2A30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 3648, 30)
)
_AristaDCS7280CR2A60_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2A60 = _AristaDCS7280CR2A60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 3648, 60)
)
_AristaDCS7280CR2A60SSD_ObjectIdentity = ObjectIdentity
aristaDCS7280CR2A60SSD = _AristaDCS7280CR2A60SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 2, 3648, 60, 761)
)
_AristaDCS7280CR332D4_ObjectIdentity = ObjectIdentity
aristaDCS7280CR332D4 = _AristaDCS7280CR332D4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 32, 1605, 4)
)
_AristaDCS7280CR332D4M_ObjectIdentity = ObjectIdentity
aristaDCS7280CR332D4M = _AristaDCS7280CR332D4M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 32, 1605, 4, 972)
)
_AristaDCS7280CR332P4_ObjectIdentity = ObjectIdentity
aristaDCS7280CR332P4 = _AristaDCS7280CR332P4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 32, 2129, 4)
)
_AristaDCS7280CR332P4M_ObjectIdentity = ObjectIdentity
aristaDCS7280CR332P4M = _AristaDCS7280CR332P4M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 32, 2129, 4, 972)
)
_AristaDCS7280CR336S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR336S = _AristaDCS7280CR336S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 36, 3282)
)
_AristaDCS7280CR396_ObjectIdentity = ObjectIdentity
aristaDCS7280CR396 = _AristaDCS7280CR396_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 96)
)
_AristaDCS7280CR3K32D4_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K32D4 = _AristaDCS7280CR3K32D4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 32, 1605, 4)
)
_AristaDCS7280CR3K32D4A_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K32D4A = _AristaDCS7280CR3K32D4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 32, 1605, 4, 3648)
)
_AristaDCS7280CR3K32P4_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K32P4 = _AristaDCS7280CR3K32P4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 32, 2129, 4)
)
_AristaDCS7280CR3K32P4A_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K32P4A = _AristaDCS7280CR3K32P4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 32, 2129, 4, 3648)
)
_AristaDCS7280CR3K36S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K36S = _AristaDCS7280CR3K36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 36, 3282)
)
_AristaDCS7280CR3K36A_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K36A = _AristaDCS7280CR3K36A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 36, 3648)
)
_AristaDCS7280CR3K96_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3K96 = _AristaDCS7280CR3K96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 202, 96)
)
_AristaDCS7280CR3MK32D4_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3MK32D4 = _AristaDCS7280CR3MK32D4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 1810, 32, 1605, 4)
)
_AristaDCS7280CR3MK32D4S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3MK32D4S = _AristaDCS7280CR3MK32D4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 1810, 32, 1605, 4, 3282)
)
_AristaDCS7280CR3MK32D4AS_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3MK32D4AS = _AristaDCS7280CR3MK32D4AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 1810, 32, 1605, 4, 3648, 3282)
)
_AristaDCS7280CR3MK32P4_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3MK32P4 = _AristaDCS7280CR3MK32P4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 1810, 32, 2129, 4)
)
_AristaDCS7280CR3MK32P4S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3MK32P4S = _AristaDCS7280CR3MK32P4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 1810, 32, 2129, 4, 3282)
)
_AristaDCS7280CR3E36S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3E36S = _AristaDCS7280CR3E36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 1988, 36, 3282)
)
_AristaDCS7280CR3AM24D12_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AM24D12 = _AristaDCS7280CR3AM24D12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2100, 24, 1605, 12)
)
_AristaDCS7280CR3AM32S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AM32S = _AristaDCS7280CR3AM32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2100, 32, 3282)
)
_AristaDCS7280CR3AM48D6_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AM48D6 = _AristaDCS7280CR3AM48D6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2100, 48, 1605, 6)
)
_AristaDCS7280CR3AM72_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AM72 = _AristaDCS7280CR3AM72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2100, 72)
)
_AristaDCS7280CR3AK24D12_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AK24D12 = _AristaDCS7280CR3AK24D12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2102, 24, 1605, 12)
)
_AristaDCS7280CR3AK24D12S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AK24D12S = _AristaDCS7280CR3AK24D12S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2102, 24, 1605, 12, 3282)
)
_AristaDCS7280CR3AK32S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AK32S = _AristaDCS7280CR3AK32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2102, 32, 3282)
)
_AristaDCS7280CR3AK48D6_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AK48D6 = _AristaDCS7280CR3AK48D6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2102, 48, 1605, 6)
)
_AristaDCS7280CR3AK72_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3AK72 = _AristaDCS7280CR3AK72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 2102, 72)
)
_AristaDCS7280CR3A24D12_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3A24D12 = _AristaDCS7280CR3A24D12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 3648, 24, 1605, 12)
)
_AristaDCS7280CR3A32S_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3A32S = _AristaDCS7280CR3A32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 3648, 32, 3282)
)
_AristaDCS7280CR3A48D6_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3A48D6 = _AristaDCS7280CR3A48D6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 3648, 48, 1605, 6)
)
_AristaDCS7280CR3A72_ObjectIdentity = ObjectIdentity
aristaDCS7280CR3A72 = _AristaDCS7280CR3A72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 3, 3648, 72)
)
_AristaDCS7280CR48_ObjectIdentity = ObjectIdentity
aristaDCS7280CR48 = _AristaDCS7280CR48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 48)
)
_AristaDCS7280CR48SSD_ObjectIdentity = ObjectIdentity
aristaDCS7280CR48SSD = _AristaDCS7280CR48SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 48, 761)
)
_AristaDCS7280DR324_ObjectIdentity = ObjectIdentity
aristaDCS7280DR324 = _AristaDCS7280DR324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 24)
)
_AristaDCS7280DR324M_ObjectIdentity = ObjectIdentity
aristaDCS7280DR324M = _AristaDCS7280DR324M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 24, 972)
)
_AristaDCS7280DR3K24_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3K24 = _AristaDCS7280DR3K24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 202, 24)
)
_AristaDCS7280DR3AM36_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3AM36 = _AristaDCS7280DR3AM36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 2100, 36)
)
_AristaDCS7280DR3AM54_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3AM54 = _AristaDCS7280DR3AM54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 2100, 54)
)
_AristaDCS7280DR3AK36_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3AK36 = _AristaDCS7280DR3AK36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 2102, 36)
)
_AristaDCS7280DR3AK36S_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3AK36S = _AristaDCS7280DR3AK36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 2102, 36, 3282)
)
_AristaDCS7280DR3AK54_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3AK54 = _AristaDCS7280DR3AK54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 2102, 54)
)
_AristaDCS7280DR3A36_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3A36 = _AristaDCS7280DR3A36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 3648, 36)
)
_AristaDCS7280DR3A54_ObjectIdentity = ObjectIdentity
aristaDCS7280DR3A54 = _AristaDCS7280DR3A54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2972, 3, 3648, 54)
)
_AristaDCS7280QRC36_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36 = _AristaDCS7280QRC36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36)
)
_AristaDCS7280QRC36M_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36M = _AristaDCS7280QRC36M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36, 972)
)
_AristaDCS7280QRC36S_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36S = _AristaDCS7280QRC36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36, 3282)
)
_AristaDCS7280QRC36SM_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36SM = _AristaDCS7280QRC36SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36, 3282, 972)
)
_AristaDCS7280QRC72_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC72 = _AristaDCS7280QRC72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 72)
)
_AristaDCS7280QRC72M_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC72M = _AristaDCS7280QRC72M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 72, 972)
)
_AristaDCS7280PR324_ObjectIdentity = ObjectIdentity
aristaDCS7280PR324 = _AristaDCS7280PR324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3232, 3, 24)
)
_AristaDCS7280PR324M_ObjectIdentity = ObjectIdentity
aristaDCS7280PR324M = _AristaDCS7280PR324M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3232, 3, 24, 972)
)
_AristaDCS7280PR348_ObjectIdentity = ObjectIdentity
aristaDCS7280PR348 = _AristaDCS7280PR348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3232, 3, 48)
)
_AristaDCS7280PR3K24_ObjectIdentity = ObjectIdentity
aristaDCS7280PR3K24 = _AristaDCS7280PR3K24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3232, 3, 202, 24)
)
_AristaDCS7280SE64_ObjectIdentity = ObjectIdentity
aristaDCS7280SE64 = _AristaDCS7280SE64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 64)
)
_AristaDCS7280SE68_ObjectIdentity = ObjectIdentity
aristaDCS7280SE68 = _AristaDCS7280SE68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 68)
)
_AristaDCS7280SE72_ObjectIdentity = ObjectIdentity
aristaDCS7280SE72 = _AristaDCS7280SE72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 72)
)
_AristaDCS7280SR248YC6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR248YC6 = _AristaDCS7280SR248YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 48, 1654, 6)
)
_AristaDCS7280SR248YC6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR248YC6M = _AristaDCS7280SR248YC6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 48, 1654, 6, 972)
)
_AristaDCS7280SR2K48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2K48C6 = _AristaDCS7280SR2K48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 202, 48, 2878, 6)
)
_AristaDCS7280SR2K48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2K48C6M = _AristaDCS7280SR2K48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 202, 48, 2878, 6, 972)
)
_AristaDCS7280SR2L48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2L48C6 = _AristaDCS7280SR2L48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 589, 48, 2878, 6)
)
_AristaDCS7280SR2A48YC6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2A48YC6 = _AristaDCS7280SR2A48YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 3648, 48, 1654, 6)
)
_AristaDCS7280SR2A48YC6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2A48YC6M = _AristaDCS7280SR2A48YC6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 3648, 48, 1654, 6, 972)
)
_AristaDCS7280SR340YC6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR340YC6 = _AristaDCS7280SR340YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 40, 1654, 6)
)
_AristaDCS7280SR348YC8_ObjectIdentity = ObjectIdentity
aristaDCS7280SR348YC8 = _AristaDCS7280SR348YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 48, 1654, 8)
)
_AristaDCS7280SR3K48YC8_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3K48YC8 = _AristaDCS7280SR3K48YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 202, 48, 1654, 8)
)
_AristaDCS7280SR3K48YC8A_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3K48YC8A = _AristaDCS7280SR3K48YC8A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 202, 48, 1654, 8, 3648)
)
_AristaDCS7280SR3M48YC8_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3M48YC8 = _AristaDCS7280SR3M48YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 972, 48, 1654, 8)
)
_AristaDCS7280SR3MK48YC8AS_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3MK48YC8AS = _AristaDCS7280SR3MK48YC8AS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 1810, 48, 1654, 8, 3648, 3282)
)
_AristaDCS7280SR3E40YC6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3E40YC6 = _AristaDCS7280SR3E40YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 1988, 40, 1654, 6)
)
_AristaDCS7280SR3E40YC6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3E40YC6M = _AristaDCS7280SR3E40YC6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 1988, 40, 1654, 6, 972)
)
_AristaDCS7280SR3AM48YC8_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3AM48YC8 = _AristaDCS7280SR3AM48YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 2100, 48, 1654, 8)
)
_AristaDCS7280SR3AK48YC8_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3AK48YC8 = _AristaDCS7280SR3AK48YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 2102, 48, 1654, 8)
)
_AristaDCS7280SR3A48YC8_ObjectIdentity = ObjectIdentity
aristaDCS7280SR3A48YC8 = _AristaDCS7280SR3A48YC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 3, 3648, 48, 1654, 8)
)
_AristaDCS7280SR32C2_ObjectIdentity = ObjectIdentity
aristaDCS7280SR32C2 = _AristaDCS7280SR32C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 32, 2878, 2)
)
_AristaDCS7280SR48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR48C6 = _AristaDCS7280SR48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 48, 2878, 6)
)
_AristaDCS7280SR48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR48C6M = _AristaDCS7280SR48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 48, 2878, 6, 972)
)
_AristaDCS7280SRAM48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280SRAM48C6 = _AristaDCS7280SRAM48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3977, 48, 2878, 6)
)
_AristaDCS7304_ObjectIdentity = ObjectIdentity
aristaDCS7304 = _AristaDCS7304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7304)
)
_AristaDCS7308_ObjectIdentity = ObjectIdentity
aristaDCS7308 = _AristaDCS7308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7308)
)
_AristaDCS7316_ObjectIdentity = ObjectIdentity
aristaDCS7316 = _AristaDCS7316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7316)
)
_AristaDCS7504_ObjectIdentity = ObjectIdentity
aristaDCS7504 = _AristaDCS7504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7504)
)
_AristaDCS7504N_ObjectIdentity = ObjectIdentity
aristaDCS7504N = _AristaDCS7504N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7504, 1359)
)
_AristaDCS7508_ObjectIdentity = ObjectIdentity
aristaDCS7508 = _AristaDCS7508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7508)
)
_AristaDCS7508N_ObjectIdentity = ObjectIdentity
aristaDCS7508N = _AristaDCS7508N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7508, 1359)
)
_AristaDCS7512N_ObjectIdentity = ObjectIdentity
aristaDCS7512N = _AristaDCS7512N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7512, 1359)
)
_AristaDCS7516N_ObjectIdentity = ObjectIdentity
aristaDCS7516N = _AristaDCS7516N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7516, 1359)
)
_AristaDCS7804CH_ObjectIdentity = ObjectIdentity
aristaDCS7804CH = _AristaDCS7804CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7804, 2749)
)
_AristaDCS7808CH_ObjectIdentity = ObjectIdentity
aristaDCS7808CH = _AristaDCS7808CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7808, 2749)
)
_AristaDCS7812CH_ObjectIdentity = ObjectIdentity
aristaDCS7812CH = _AristaDCS7812CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7812, 2749)
)
_AristaDCS7816LCH_ObjectIdentity = ObjectIdentity
aristaDCS7816LCH = _AristaDCS7816LCH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7816, 589, 2749)
)
_AristaDCS7816CH_ObjectIdentity = ObjectIdentity
aristaDCS7816CH = _AristaDCS7816CH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7816, 2749)
)
_AristaZTX7250S16S_ObjectIdentity = ObjectIdentity
aristaZTX7250S16S = _AristaZTX7250S16S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3413, 7250, 3282, 16, 3282)
)
_Arista7289_ObjectIdentity = ObjectIdentity
arista7289 = _Arista7289_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 7289)
)
_Arista7358_ObjectIdentity = ObjectIdentity
arista7358 = _Arista7358_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 7358)
)
_Arista7368_ObjectIdentity = ObjectIdentity
arista7368 = _Arista7368_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 7368)
)
_Arista7388_ObjectIdentity = ObjectIdentity
arista7388 = _Arista7388_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 7388)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-PRODUCTS-MIB",
    **{"aristaQuestoneD3020": aristaQuestoneD3020,
       "aristaLY6": aristaLY6,
       "aristaAWE5310": aristaAWE5310,
       "aristaAWE5510": aristaAWE5510,
       "aristaAWE7220RP5TH2S": aristaAWE7220RP5TH2S,
       "aristaAWE7230R4TX4S": aristaAWE7230R4TX4S,
       "aristaAWE7250R16S": aristaAWE7250R16S,
       "aristaSmallstoneD4040": aristaSmallstoneD4040,
       "aristaRedstoneXPD2060": aristaRedstoneXPD2060,
       "aristaCCS710P12": aristaCCS710P12,
       "aristaCCS710P16P": aristaCCS710P16P,
       "aristaCCS720XP24ZY4": aristaCCS720XP24ZY4,
       "aristaCCS720XP24Y6": aristaCCS720XP24Y6,
       "aristaCCS720XP48ZC2": aristaCCS720XP48ZC2,
       "aristaCCS720XP48TXH2CS": aristaCCS720XP48TXH2CS,
       "aristaCCS720XP48Y6": aristaCCS720XP48Y6,
       "aristaCCS720XP96ZC2": aristaCCS720XP96ZC2,
       "aristaCCS720XP96ZC2MS": aristaCCS720XP96ZC2MS,
       "aristaCCS720DF48Y": aristaCCS720DF48Y,
       "aristaCCS720DF48Y2": aristaCCS720DF48Y2,
       "aristaCCS720DF48YMS2": aristaCCS720DF48YMS2,
       "aristaCCS720DF48YDC": aristaCCS720DF48YDC,
       "aristaCCS720DF48YDC2": aristaCCS720DF48YDC2,
       "aristaCCS720DT24S": aristaCCS720DT24S,
       "aristaCCS720DT24S2": aristaCCS720DT24S2,
       "aristaCCS720DT24SMS2": aristaCCS720DT24SMS2,
       "aristaCCS720DT48S": aristaCCS720DT48S,
       "aristaCCS720DT48S2": aristaCCS720DT48S2,
       "aristaCCS720DP24ZS": aristaCCS720DP24ZS,
       "aristaCCS720DP24ZS2": aristaCCS720DP24ZS2,
       "aristaCCS720DP24S": aristaCCS720DP24S,
       "aristaCCS720DP24S2": aristaCCS720DP24S2,
       "aristaCCS720DP24SMS2": aristaCCS720DP24SMS2,
       "aristaCCS720DP48ZS": aristaCCS720DP48ZS,
       "aristaCCS720DP48ZS2": aristaCCS720DP48ZS2,
       "aristaCCS720DP48S": aristaCCS720DP48S,
       "aristaCCS720DP48S2": aristaCCS720DP48S2,
       "aristaCCS720DP48SMS2": aristaCCS720DP48SMS2,
       "aristaCCS722XPM48ZY8": aristaCCS722XPM48ZY8,
       "aristaCCS722XPM48Y4": aristaCCS722XPM48Y4,
       "aristaCCS755CH": aristaCCS755CH,
       "aristaCCS758CH": aristaCCS758CH,
       "aristaCVX": aristaCVX,
       "aristavEOS": aristavEOS,
       "aristaDCS7010T48": aristaDCS7010T48,
       "aristaDCS7010T48DC": aristaDCS7010T48DC,
       "aristaDCS7010TX48": aristaDCS7010TX48,
       "aristaDCS7010TX48C": aristaDCS7010TX48C,
       "aristaDCS7010TX48CDC": aristaDCS7010TX48CDC,
       "aristaDCS7010TX48CDCRV3": aristaDCS7010TX48CDCRV3,
       "aristaDCS7010TX48DC": aristaDCS7010TX48DC,
       "aristaDCS7020TRA48": aristaDCS7020TRA48,
       "aristaDCS7020SRG24C2": aristaDCS7020SRG24C2,
       "aristaDCS7020TR48": aristaDCS7020TR48,
       "aristaDCS7020SR24C2": aristaDCS7020SR24C2,
       "aristaDCS7020SR32C2": aristaDCS7020SR32C2,
       "aristaDCS7048T4S": aristaDCS7048T4S,
       "aristaDCS7048TA": aristaDCS7048TA,
       "aristaDCS7050SPX448D8": aristaDCS7050SPX448D8,
       "aristaDCS7050T36": aristaDCS7050T36,
       "aristaDCS7050T52": aristaDCS7050T52,
       "aristaDCS7050T52SSD": aristaDCS7050T52SSD,
       "aristaDCS7050T64": aristaDCS7050T64,
       "aristaDCS7050T64SSD": aristaDCS7050T64SSD,
       "aristaDCS7050TX2128": aristaDCS7050TX2128,
       "aristaDCS7050TX2128SSD": aristaDCS7050TX2128SSD,
       "aristaDCS7050TX348C8": aristaDCS7050TX348C8,
       "aristaDCS7050TX348C8SSD": aristaDCS7050TX348C8SSD,
       "aristaDCS7050TX48": aristaDCS7050TX48,
       "aristaDCS7050TX48SSD": aristaDCS7050TX48SSD,
       "aristaDCS7050TX64": aristaDCS7050TX64,
       "aristaDCS7050TX64SSD": aristaDCS7050TX64SSD,
       "aristaDCS7050TX72": aristaDCS7050TX72,
       "aristaDCS7050TX72SSD": aristaDCS7050TX72SSD,
       "aristaDCS7050TX72Q": aristaDCS7050TX72Q,
       "aristaDCS7050TX72QSSD": aristaDCS7050TX72QSSD,
       "aristaDCS7050TX96": aristaDCS7050TX96,
       "aristaDCS7050TX96SSD": aristaDCS7050TX96SSD,
       "aristaDCS7050TX128": aristaDCS7050TX128,
       "aristaDCS7050TX128SSD": aristaDCS7050TX128SSD,
       "aristaDCS7050Q16": aristaDCS7050Q16,
       "aristaDCS7050Q16SSD": aristaDCS7050Q16SSD,
       "aristaDCS7050CX332C": aristaDCS7050CX332C,
       "aristaDCS7050CX332S": aristaDCS7050CX332S,
       "aristaDCS7050CX332SSSD": aristaDCS7050CX332SSSD,
       "aristaDCS7050CX3M32S": aristaDCS7050CX3M32S,
       "aristaDCS7050CX424D8": aristaDCS7050CX424D8,
       "aristaDCS7050CX440D": aristaDCS7050CX440D,
       "aristaDCS7050CX4M48D8": aristaDCS7050CX4M48D8,
       "aristaDCS7050DX432S": aristaDCS7050DX432S,
       "aristaDCS7050DX4M32S": aristaDCS7050DX4M32S,
       "aristaDCS7050QX232S": aristaDCS7050QX232S,
       "aristaDCS7050QX232SSSD": aristaDCS7050QX232SSSD,
       "aristaDCS7050QX32": aristaDCS7050QX32,
       "aristaDCS7050QX32SSD": aristaDCS7050QX32SSD,
       "aristaDCS7050QX32CLSSD": aristaDCS7050QX32CLSSD,
       "aristaDCS7050QX32S": aristaDCS7050QX32S,
       "aristaDCS7050QX32SSSD": aristaDCS7050QX32SSSD,
       "aristaDCS7050PX432S": aristaDCS7050PX432S,
       "aristaDCS7050S52": aristaDCS7050S52,
       "aristaDCS7050S52SSD": aristaDCS7050S52SSD,
       "aristaDCS7050S64": aristaDCS7050S64,
       "aristaDCS7050S64SSD": aristaDCS7050S64SSD,
       "aristaDCS7050SDX448D8": aristaDCS7050SDX448D8,
       "aristaDCS7050SX272Q": aristaDCS7050SX272Q,
       "aristaDCS7050SX272QSSD": aristaDCS7050SX272QSSD,
       "aristaDCS7050SX2128": aristaDCS7050SX2128,
       "aristaDCS7050SX2128SSD": aristaDCS7050SX2128SSD,
       "aristaDCS7050SX324YC4CS": aristaDCS7050SX324YC4CS,
       "aristaDCS7050SX348YC8": aristaDCS7050SX348YC8,
       "aristaDCS7050SX348YC8C": aristaDCS7050SX348YC8C,
       "aristaDCS7050SX348YC12": aristaDCS7050SX348YC12,
       "aristaDCS7050SX348YC12SSD": aristaDCS7050SX348YC12SSD,
       "aristaDCS7050SX348C8": aristaDCS7050SX348C8,
       "aristaDCS7050SX348C8C": aristaDCS7050SX348C8C,
       "aristaDCS7050SX396YC8": aristaDCS7050SX396YC8,
       "aristaDCS7050SX64": aristaDCS7050SX64,
       "aristaDCS7050SX64SSD": aristaDCS7050SX64SSD,
       "aristaDCS7050SX72": aristaDCS7050SX72,
       "aristaDCS7050SX72SSD": aristaDCS7050SX72SSD,
       "aristaDCS7050SX72Q": aristaDCS7050SX72Q,
       "aristaDCS7050SX72QSSD": aristaDCS7050SX72QSSD,
       "aristaDCS7050SX96": aristaDCS7050SX96,
       "aristaDCS7050SX96SSD": aristaDCS7050SX96SSD,
       "aristaDCS7050SX128": aristaDCS7050SX128,
       "aristaDCS7050SX128SSD": aristaDCS7050SX128SSD,
       "aristaDCS7060CX232S": aristaDCS7060CX232S,
       "aristaDCS7060CX556D8": aristaDCS7060CX556D8,
       "aristaDCS7060CX32C": aristaDCS7060CX32C,
       "aristaDCS7060CX32S": aristaDCS7060CX32S,
       "aristaDCS7060CX32SSSD": aristaDCS7060CX32SSSD,
       "aristaDCS7060CX32SES": aristaDCS7060CX32SES,
       "aristaDCS7060DX432": aristaDCS7060DX432,
       "aristaDCS7060DX432D": aristaDCS7060DX432D,
       "aristaDCS7060DX432CRV3": aristaDCS7060DX432CRV3,
       "aristaDCS7060DX432S": aristaDCS7060DX432S,
       "aristaDCS7060DX432SBRV3": aristaDCS7060DX432SBRV3,
       "aristaDCS7060DX532": aristaDCS7060DX532,
       "aristaDCS7060DX564": aristaDCS7060DX564,
       "aristaDCS7060DX564E": aristaDCS7060DX564E,
       "aristaDCS7060DX564S": aristaDCS7060DX564S,
       "aristaDCS7060X632PE": aristaDCS7060X632PE,
       "aristaDCS7060X664DE": aristaDCS7060X664DE,
       "aristaDCS7060X664PE": aristaDCS7060X664PE,
       "aristaDCS7060PX432": aristaDCS7060PX432,
       "aristaDCS7060PX432S": aristaDCS7060PX432S,
       "aristaDCS7060PX564E": aristaDCS7060PX564E,
       "aristaDCS7060SX248YC6": aristaDCS7060SX248YC6,
       "aristaDCS7060SX248YC6SSD": aristaDCS7060SX248YC6SSD,
       "aristaDCS7120T4S": aristaDCS7120T4S,
       "aristaDCS7124FX": aristaDCS7124FX,
       "aristaDCS7124FXCL": aristaDCS7124FXCL,
       "aristaDCS7124S": aristaDCS7124S,
       "aristaDCS7124SX": aristaDCS7124SX,
       "aristaDCS7124SXSSD": aristaDCS7124SXSSD,
       "aristaDCS713016G3": aristaDCS713016G3,
       "aristaDCS713016G3S": aristaDCS713016G3S,
       "aristaDCS713048LB": aristaDCS713048LB,
       "aristaDCS713048LA": aristaDCS713048LA,
       "aristaDCS713048LS": aristaDCS713048LS,
       "aristaDCS713048L": aristaDCS713048L,
       "aristaDCS713048LBA": aristaDCS713048LBA,
       "aristaDCS713048LBS": aristaDCS713048LBS,
       "aristaDCS713048LAS": aristaDCS713048LAS,
       "aristaDCS713048E": aristaDCS713048E,
       "aristaDCS713048EHS": aristaDCS713048EHS,
       "aristaDCS713048G3": aristaDCS713048G3,
       "aristaDCS713048G3S": aristaDCS713048G3S,
       "aristaDCS713048EH": aristaDCS713048EH,
       "aristaDCS713048LBAS": aristaDCS713048LBAS,
       "aristaDCS713096": aristaDCS713096,
       "aristaDCS713096LB": aristaDCS713096LB,
       "aristaDCS713096LA": aristaDCS713096LA,
       "aristaDCS713096LS": aristaDCS713096LS,
       "aristaDCS713096L": aristaDCS713096L,
       "aristaDCS713096LBA": aristaDCS713096LBA,
       "aristaDCS713096LBS": aristaDCS713096LBS,
       "aristaDCS713096LAS": aristaDCS713096LAS,
       "aristaDCS713096E": aristaDCS713096E,
       "aristaDCS713096S": aristaDCS713096S,
       "aristaDCS713096LBAS": aristaDCS713096LBAS,
       "aristaDCS7130LBR48S6QD": aristaDCS7130LBR48S6QD,
       "aristaDCS7130LBR48S6QDMD": aristaDCS7130LBR48S6QDMD,
       "aristaDCS7130B32QD": aristaDCS7130B32QD,
       "aristaDCS7132LB48Y4C": aristaDCS7132LB48Y4C,
       "aristaDCS7135LB48Y4C": aristaDCS7135LB48Y4C,
       "aristaDCS7140T8S": aristaDCS7140T8S,
       "aristaDCS7148S": aristaDCS7148S,
       "aristaDCS7148SX": aristaDCS7148SX,
       "aristaDCS7150S24": aristaDCS7150S24,
       "aristaDCS7150S24CL": aristaDCS7150S24CL,
       "aristaDCS7150S24CLSSD": aristaDCS7150S24CLSSD,
       "aristaDCS7150S52CL": aristaDCS7150S52CL,
       "aristaDCS7150S52CLSSD": aristaDCS7150S52CLSSD,
       "aristaDCS7150S64CL": aristaDCS7150S64CL,
       "aristaDCS7150S64CLSSD": aristaDCS7150S64CLSSD,
       "aristaDCS7150SC24CLD": aristaDCS7150SC24CLD,
       "aristaDCS7150SC64CLD": aristaDCS7150SC64CLD,
       "aristaDCS716032CQ": aristaDCS716032CQ,
       "aristaDCS716032CQSSD": aristaDCS716032CQSSD,
       "aristaDCS716048YC6": aristaDCS716048YC6,
       "aristaDCS716048YC6SSD": aristaDCS716048YC6SSD,
       "aristaDCS716048TC6": aristaDCS716048TC6,
       "aristaDCS716048TC6SSD": aristaDCS716048TC6SSD,
       "aristaDCS716064YC16": aristaDCS716064YC16,
       "aristaDCS717032CD": aristaDCS717032CD,
       "aristaDCS717032CDM": aristaDCS717032CDM,
       "aristaDCS717032C": aristaDCS717032C,
       "aristaDCS717032CM": aristaDCS717032CM,
       "aristaDCS717064C": aristaDCS717064C,
       "aristaDCS717064CM": aristaDCS717064CM,
       "aristaDCS7170B64C": aristaDCS7170B64C,
       "aristaDCS7170B64CM": aristaDCS7170B64CM,
       "aristaDCS7250QX64": aristaDCS7250QX64,
       "aristaDCS7250QX64SSD": aristaDCS7250QX64SSD,
       "aristaDCS7250QX64M": aristaDCS7250QX64M,
       "aristaDCS7260CX364": aristaDCS7260CX364,
       "aristaDCS7260CX364LQ": aristaDCS7260CX364LQ,
       "aristaDCS7260CX364SSD": aristaDCS7260CX364SSD,
       "aristaDCS7260CX364E": aristaDCS7260CX364E,
       "aristaDCS7260CX64": aristaDCS7260CX64,
       "aristaDCS7260CX64SSD": aristaDCS7260CX64SSD,
       "aristaDCS7260QX64": aristaDCS7260QX64,
       "aristaDCS7260QX64SSD": aristaDCS7260QX64SSD,
       "aristaDCS7280TRA48C6": aristaDCS7280TRA48C6,
       "aristaDCS7280TRA48C6M": aristaDCS7280TRA48C6M,
       "aristaDCS7280CRA48": aristaDCS7280CRA48,
       "aristaDCS7280CRA48M": aristaDCS7280CRA48M,
       "aristaDCS7280SRA48C6": aristaDCS7280SRA48C6,
       "aristaDCS7280SRA48C6M": aristaDCS7280SRA48C6M,
       "aristaDCS7280SRM40CX2": aristaDCS7280SRM40CX2,
       "aristaDCS7280TR340C6": aristaDCS7280TR340C6,
       "aristaDCS7280TR48C6": aristaDCS7280TR48C6,
       "aristaDCS7280TR48C6M": aristaDCS7280TR48C6M,
       "aristaDCS7280QRAC36S": aristaDCS7280QRAC36S,
       "aristaDCS7280QRAC36SM": aristaDCS7280QRAC36SM,
       "aristaDCS7280QRAC72": aristaDCS7280QRAC72,
       "aristaDCS7280QRAC72M": aristaDCS7280QRAC72M,
       "aristaDCS7280CR260": aristaDCS7280CR260,
       "aristaDCS7280CR260SSD": aristaDCS7280CR260SSD,
       "aristaDCS7280CR2K30": aristaDCS7280CR2K30,
       "aristaDCS7280CR2K60": aristaDCS7280CR2K60,
       "aristaDCS7280CR2K60SSD": aristaDCS7280CR2K60SSD,
       "aristaDCS7280CR2M30": aristaDCS7280CR2M30,
       "aristaDCS7280CR2A30": aristaDCS7280CR2A30,
       "aristaDCS7280CR2A60": aristaDCS7280CR2A60,
       "aristaDCS7280CR2A60SSD": aristaDCS7280CR2A60SSD,
       "aristaDCS7280CR332D4": aristaDCS7280CR332D4,
       "aristaDCS7280CR332D4M": aristaDCS7280CR332D4M,
       "aristaDCS7280CR332P4": aristaDCS7280CR332P4,
       "aristaDCS7280CR332P4M": aristaDCS7280CR332P4M,
       "aristaDCS7280CR336S": aristaDCS7280CR336S,
       "aristaDCS7280CR396": aristaDCS7280CR396,
       "aristaDCS7280CR3K32D4": aristaDCS7280CR3K32D4,
       "aristaDCS7280CR3K32D4A": aristaDCS7280CR3K32D4A,
       "aristaDCS7280CR3K32P4": aristaDCS7280CR3K32P4,
       "aristaDCS7280CR3K32P4A": aristaDCS7280CR3K32P4A,
       "aristaDCS7280CR3K36S": aristaDCS7280CR3K36S,
       "aristaDCS7280CR3K36A": aristaDCS7280CR3K36A,
       "aristaDCS7280CR3K96": aristaDCS7280CR3K96,
       "aristaDCS7280CR3MK32D4": aristaDCS7280CR3MK32D4,
       "aristaDCS7280CR3MK32D4S": aristaDCS7280CR3MK32D4S,
       "aristaDCS7280CR3MK32D4AS": aristaDCS7280CR3MK32D4AS,
       "aristaDCS7280CR3MK32P4": aristaDCS7280CR3MK32P4,
       "aristaDCS7280CR3MK32P4S": aristaDCS7280CR3MK32P4S,
       "aristaDCS7280CR3E36S": aristaDCS7280CR3E36S,
       "aristaDCS7280CR3AM24D12": aristaDCS7280CR3AM24D12,
       "aristaDCS7280CR3AM32S": aristaDCS7280CR3AM32S,
       "aristaDCS7280CR3AM48D6": aristaDCS7280CR3AM48D6,
       "aristaDCS7280CR3AM72": aristaDCS7280CR3AM72,
       "aristaDCS7280CR3AK24D12": aristaDCS7280CR3AK24D12,
       "aristaDCS7280CR3AK24D12S": aristaDCS7280CR3AK24D12S,
       "aristaDCS7280CR3AK32S": aristaDCS7280CR3AK32S,
       "aristaDCS7280CR3AK48D6": aristaDCS7280CR3AK48D6,
       "aristaDCS7280CR3AK72": aristaDCS7280CR3AK72,
       "aristaDCS7280CR3A24D12": aristaDCS7280CR3A24D12,
       "aristaDCS7280CR3A32S": aristaDCS7280CR3A32S,
       "aristaDCS7280CR3A48D6": aristaDCS7280CR3A48D6,
       "aristaDCS7280CR3A72": aristaDCS7280CR3A72,
       "aristaDCS7280CR48": aristaDCS7280CR48,
       "aristaDCS7280CR48SSD": aristaDCS7280CR48SSD,
       "aristaDCS7280DR324": aristaDCS7280DR324,
       "aristaDCS7280DR324M": aristaDCS7280DR324M,
       "aristaDCS7280DR3K24": aristaDCS7280DR3K24,
       "aristaDCS7280DR3AM36": aristaDCS7280DR3AM36,
       "aristaDCS7280DR3AM54": aristaDCS7280DR3AM54,
       "aristaDCS7280DR3AK36": aristaDCS7280DR3AK36,
       "aristaDCS7280DR3AK36S": aristaDCS7280DR3AK36S,
       "aristaDCS7280DR3AK54": aristaDCS7280DR3AK54,
       "aristaDCS7280DR3A36": aristaDCS7280DR3A36,
       "aristaDCS7280DR3A54": aristaDCS7280DR3A54,
       "aristaDCS7280QRC36": aristaDCS7280QRC36,
       "aristaDCS7280QRC36M": aristaDCS7280QRC36M,
       "aristaDCS7280QRC36S": aristaDCS7280QRC36S,
       "aristaDCS7280QRC36SM": aristaDCS7280QRC36SM,
       "aristaDCS7280QRC72": aristaDCS7280QRC72,
       "aristaDCS7280QRC72M": aristaDCS7280QRC72M,
       "aristaDCS7280PR324": aristaDCS7280PR324,
       "aristaDCS7280PR324M": aristaDCS7280PR324M,
       "aristaDCS7280PR348": aristaDCS7280PR348,
       "aristaDCS7280PR3K24": aristaDCS7280PR3K24,
       "aristaDCS7280SE64": aristaDCS7280SE64,
       "aristaDCS7280SE68": aristaDCS7280SE68,
       "aristaDCS7280SE72": aristaDCS7280SE72,
       "aristaDCS7280SR248YC6": aristaDCS7280SR248YC6,
       "aristaDCS7280SR248YC6M": aristaDCS7280SR248YC6M,
       "aristaDCS7280SR2K48C6": aristaDCS7280SR2K48C6,
       "aristaDCS7280SR2K48C6M": aristaDCS7280SR2K48C6M,
       "aristaDCS7280SR2L48C6": aristaDCS7280SR2L48C6,
       "aristaDCS7280SR2A48YC6": aristaDCS7280SR2A48YC6,
       "aristaDCS7280SR2A48YC6M": aristaDCS7280SR2A48YC6M,
       "aristaDCS7280SR340YC6": aristaDCS7280SR340YC6,
       "aristaDCS7280SR348YC8": aristaDCS7280SR348YC8,
       "aristaDCS7280SR3K48YC8": aristaDCS7280SR3K48YC8,
       "aristaDCS7280SR3K48YC8A": aristaDCS7280SR3K48YC8A,
       "aristaDCS7280SR3M48YC8": aristaDCS7280SR3M48YC8,
       "aristaDCS7280SR3MK48YC8AS": aristaDCS7280SR3MK48YC8AS,
       "aristaDCS7280SR3E40YC6": aristaDCS7280SR3E40YC6,
       "aristaDCS7280SR3E40YC6M": aristaDCS7280SR3E40YC6M,
       "aristaDCS7280SR3AM48YC8": aristaDCS7280SR3AM48YC8,
       "aristaDCS7280SR3AK48YC8": aristaDCS7280SR3AK48YC8,
       "aristaDCS7280SR3A48YC8": aristaDCS7280SR3A48YC8,
       "aristaDCS7280SR32C2": aristaDCS7280SR32C2,
       "aristaDCS7280SR48C6": aristaDCS7280SR48C6,
       "aristaDCS7280SR48C6M": aristaDCS7280SR48C6M,
       "aristaDCS7280SRAM48C6": aristaDCS7280SRAM48C6,
       "aristaDCS7304": aristaDCS7304,
       "aristaDCS7308": aristaDCS7308,
       "aristaDCS7316": aristaDCS7316,
       "aristaDCS7504": aristaDCS7504,
       "aristaDCS7504N": aristaDCS7504N,
       "aristaDCS7508": aristaDCS7508,
       "aristaDCS7508N": aristaDCS7508N,
       "aristaDCS7512N": aristaDCS7512N,
       "aristaDCS7516N": aristaDCS7516N,
       "aristaDCS7804CH": aristaDCS7804CH,
       "aristaDCS7808CH": aristaDCS7808CH,
       "aristaDCS7812CH": aristaDCS7812CH,
       "aristaDCS7816LCH": aristaDCS7816LCH,
       "aristaDCS7816CH": aristaDCS7816CH,
       "aristaZTX7250S16S": aristaZTX7250S16S,
       "arista7289": arista7289,
       "arista7358": arista7358,
       "arista7368": arista7368,
       "arista7388": arista7388,
       "aristaProductsMIB": aristaProductsMIB}
)
