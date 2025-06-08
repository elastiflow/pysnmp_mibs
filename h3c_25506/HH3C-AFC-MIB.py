# SNMP MIB module (HH3C-AFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-AFC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:27:38 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cAFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85)
)
if mibBuilder.loadTexts:
    hh3cAFC.setRevisions(
        ("2008-07-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAFCLeaf_ObjectIdentity = ObjectIdentity
hh3cAFCLeaf = _Hh3cAFCLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1)
)
_Hh3cDDosAttackTargetIP_Type = IpAddress
_Hh3cDDosAttackTargetIP_Object = MibScalar
hh3cDDosAttackTargetIP = _Hh3cDDosAttackTargetIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 1),
    _Hh3cDDosAttackTargetIP_Type()
)
hh3cDDosAttackTargetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackTargetIP.setStatus("current")


class _Hh3cDDosAttackType_Type(Integer32):
    """Custom type hh3cDDosAttackType based on Integer32"""
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


_Hh3cDDosAttackType_Type.__name__ = "Integer32"
_Hh3cDDosAttackType_Object = MibScalar
hh3cDDosAttackType = _Hh3cDDosAttackType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 2),
    _Hh3cDDosAttackType_Type()
)
hh3cDDosAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackType.setStatus("current")


class _Hh3cDDosAttackPolicy_Type(OctetString):
    """Custom type hh3cDDosAttackPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hh3cDDosAttackPolicy_Type.__name__ = "OctetString"
_Hh3cDDosAttackPolicy_Object = MibScalar
hh3cDDosAttackPolicy = _Hh3cDDosAttackPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 3),
    _Hh3cDDosAttackPolicy_Type()
)
hh3cDDosAttackPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackPolicy.setStatus("current")
_Hh3cDDosAttackThreshold_Type = Integer32
_Hh3cDDosAttackThreshold_Object = MibScalar
hh3cDDosAttackThreshold = _Hh3cDDosAttackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 4),
    _Hh3cDDosAttackThreshold_Type()
)
hh3cDDosAttackThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackThreshold.setStatus("current")
_Hh3cDDosAttackSpeed_Type = Integer32
_Hh3cDDosAttackSpeed_Object = MibScalar
hh3cDDosAttackSpeed = _Hh3cDDosAttackSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 5),
    _Hh3cDDosAttackSpeed_Type()
)
hh3cDDosAttackSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDDosAttackSpeed.setStatus("current")
_Hh3cAFCNotify_ObjectIdentity = ObjectIdentity
hh3cAFCNotify = _Hh3cAFCNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2)
)
_Hh3cAFCNotifyPrefix_ObjectIdentity = ObjectIdentity
hh3cAFCNotifyPrefix = _Hh3cAFCNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cDDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0, 1)
)
hh3cDDosAttackStart.setObjects(
      *(("HH3C-AFC-MIB", "hh3cDDosAttackTargetIP"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackType"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackPolicy"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackThreshold"),
        ("HH3C-AFC-MIB", "hh3cDDosAttackSpeed"))
)
if mibBuilder.loadTexts:
    hh3cDDosAttackStart.setStatus(
        "current"
    )

hh3cDDosAttackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0, 2)
)
hh3cDDosAttackEnd.setObjects(
    ("HH3C-AFC-MIB", "hh3cDDosAttackTargetIP")
)
if mibBuilder.loadTexts:
    hh3cDDosAttackEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-AFC-MIB",
    **{"hh3cAFC": hh3cAFC,
       "hh3cAFCLeaf": hh3cAFCLeaf,
       "hh3cDDosAttackTargetIP": hh3cDDosAttackTargetIP,
       "hh3cDDosAttackType": hh3cDDosAttackType,
       "hh3cDDosAttackPolicy": hh3cDDosAttackPolicy,
       "hh3cDDosAttackThreshold": hh3cDDosAttackThreshold,
       "hh3cDDosAttackSpeed": hh3cDDosAttackSpeed,
       "hh3cAFCNotify": hh3cAFCNotify,
       "hh3cAFCNotifyPrefix": hh3cAFCNotifyPrefix,
       "hh3cDDosAttackStart": hh3cDDosAttackStart,
       "hh3cDDosAttackEnd": hh3cDDosAttackEnd}
)
