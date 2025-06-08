# SNMP MIB module (A3COM-HUAWEI-AFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-AFC-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:05:02 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cAFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85)
)
if mibBuilder.loadTexts:
    h3cAFC.setRevisions(
        ("2008-07-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cAFCLeaf_ObjectIdentity = ObjectIdentity
h3cAFCLeaf = _H3cAFCLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1)
)
_H3cDDosAttackTargetIP_Type = IpAddress
_H3cDDosAttackTargetIP_Object = MibScalar
h3cDDosAttackTargetIP = _H3cDDosAttackTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 1),
    _H3cDDosAttackTargetIP_Type()
)
h3cDDosAttackTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackTargetIP.setStatus("current")


class _H3cDDosAttackType_Type(Integer32):
    """Custom type h3cDDosAttackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              11,
              12,
              13,
              14,
              15,
              18,
              19,
              20,
              24,
              27,
              29,
              30,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("land", 1),
          ("smurf", 2),
          ("fraggle", 3),
          ("winnuke", 4),
          ("synflood", 5),
          ("icmpflood", 6),
          ("udpflood", 7),
          ("icmpredirect", 8),
          ("icmpunreachable", 9),
          ("tracert", 11),
          ("tcpflag", 12),
          ("pingofdeath", 13),
          ("teardrop", 14),
          ("ipfragment", 15),
          ("largeicmp", 18),
          ("sourceroute", 19),
          ("routerecord", 20),
          ("fragflood", 24),
          ("scan", 27),
          ("appstreamalarm", 29),
          ("sessionstreamalarm", 30),
          ("tcpabnormal", 32),
          ("ipfragabnormal", 33),
          ("tftpabnormal", 34),
          ("dnsabnormal", 35),
          ("httpabnormal", 36),
          ("telnetabnormal", 37),
          ("ftpabnormal", 38),
          ("smtpabnormal", 39),
          ("pop3abnormal", 40),
          ("snmpabnormal", 41),
          ("ackabnormal", 42),
          ("cc", 43),
          ("otherabnormal", 1024))
    )


_H3cDDosAttackType_Type.__name__ = "Integer32"
_H3cDDosAttackType_Object = MibScalar
h3cDDosAttackType = _H3cDDosAttackType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 2),
    _H3cDDosAttackType_Type()
)
h3cDDosAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackType.setStatus("current")


class _H3cDDosAttackPolicy_Type(OctetString):
    """Custom type h3cDDosAttackPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_H3cDDosAttackPolicy_Type.__name__ = "OctetString"
_H3cDDosAttackPolicy_Object = MibScalar
h3cDDosAttackPolicy = _H3cDDosAttackPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 3),
    _H3cDDosAttackPolicy_Type()
)
h3cDDosAttackPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackPolicy.setStatus("current")
_H3cDDosAttackThreshold_Type = Integer32
_H3cDDosAttackThreshold_Object = MibScalar
h3cDDosAttackThreshold = _H3cDDosAttackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 4),
    _H3cDDosAttackThreshold_Type()
)
h3cDDosAttackThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackThreshold.setStatus("current")
_H3cDDosAttackSpeed_Type = Integer32
_H3cDDosAttackSpeed_Object = MibScalar
h3cDDosAttackSpeed = _H3cDDosAttackSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 5),
    _H3cDDosAttackSpeed_Type()
)
h3cDDosAttackSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDDosAttackSpeed.setStatus("current")
_H3cAFCNotify_ObjectIdentity = ObjectIdentity
h3cAFCNotify = _H3cAFCNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2)
)
_H3cAFCNotifyPrefix_ObjectIdentity = ObjectIdentity
h3cAFCNotifyPrefix = _H3cAFCNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cDDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0, 1)
)
h3cDDosAttackStart.setObjects(
      *(("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackTargetIP"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackType"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackPolicy"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackThreshold"),
        ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackSpeed"))
)
if mibBuilder.loadTexts:
    h3cDDosAttackStart.setStatus(
        "current"
    )

h3cDDosAttackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0, 2)
)
h3cDDosAttackEnd.setObjects(
    ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackTargetIP")
)
if mibBuilder.loadTexts:
    h3cDDosAttackEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-AFC-MIB",
    **{"h3cAFC": h3cAFC,
       "h3cAFCLeaf": h3cAFCLeaf,
       "h3cDDosAttackTargetIP": h3cDDosAttackTargetIP,
       "h3cDDosAttackType": h3cDDosAttackType,
       "h3cDDosAttackPolicy": h3cDDosAttackPolicy,
       "h3cDDosAttackThreshold": h3cDDosAttackThreshold,
       "h3cDDosAttackSpeed": h3cDDosAttackSpeed,
       "h3cAFCNotify": h3cAFCNotify,
       "h3cAFCNotifyPrefix": h3cAFCNotifyPrefix,
       "h3cDDosAttackStart": h3cDDosAttackStart,
       "h3cDDosAttackEnd": h3cDDosAttackEnd}
)
