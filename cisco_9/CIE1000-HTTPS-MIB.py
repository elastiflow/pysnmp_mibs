# SNMP MIB module (CIE1000-HTTPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-HTTPS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000HttpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47)
)
if mibBuilder.loadTexts:
    cie1000HttpsMib.setRevisions(
        ("2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000HttpsMibObjects_ObjectIdentity = ObjectIdentity
cie1000HttpsMibObjects = _Cie1000HttpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1)
)
_Cie1000HttpsConfig_ObjectIdentity = ObjectIdentity
cie1000HttpsConfig = _Cie1000HttpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2)
)
_Cie1000HttpsConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000HttpsConfigGlobals = _Cie1000HttpsConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2, 1)
)
_Cie1000HttpsConfigGlobalsMode_Type = TruthValue
_Cie1000HttpsConfigGlobalsMode_Object = MibScalar
cie1000HttpsConfigGlobalsMode = _Cie1000HttpsConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2, 1, 1),
    _Cie1000HttpsConfigGlobalsMode_Type()
)
cie1000HttpsConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000HttpsConfigGlobalsMode.setStatus("current")
_Cie1000HttpsConfigGlobalsRedirectToHttps_Type = TruthValue
_Cie1000HttpsConfigGlobalsRedirectToHttps_Object = MibScalar
cie1000HttpsConfigGlobalsRedirectToHttps = _Cie1000HttpsConfigGlobalsRedirectToHttps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2, 1, 2),
    _Cie1000HttpsConfigGlobalsRedirectToHttps_Type()
)
cie1000HttpsConfigGlobalsRedirectToHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000HttpsConfigGlobalsRedirectToHttps.setStatus("current")
_Cie1000HttpsMibConformance_ObjectIdentity = ObjectIdentity
cie1000HttpsMibConformance = _Cie1000HttpsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2)
)
_Cie1000HttpsMibCompliances_ObjectIdentity = ObjectIdentity
cie1000HttpsMibCompliances = _Cie1000HttpsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 1)
)
_Cie1000HttpsMibGroups_ObjectIdentity = ObjectIdentity
cie1000HttpsMibGroups = _Cie1000HttpsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 2)
)

# Managed Objects groups

cie1000HttpsConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 2, 1)
)
cie1000HttpsConfigGlobalsInfoGroup.setObjects(
      *(("CIE1000-HTTPS-MIB", "cie1000HttpsConfigGlobalsMode"),
        ("CIE1000-HTTPS-MIB", "cie1000HttpsConfigGlobalsRedirectToHttps"))
)
if mibBuilder.loadTexts:
    cie1000HttpsConfigGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000HttpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 1, 1)
)
cie1000HttpsMibCompliance.setObjects(
    ("CIE1000-HTTPS-MIB", "cie1000HttpsConfigGlobalsInfoGroup")
)
if mibBuilder.loadTexts:
    cie1000HttpsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-HTTPS-MIB",
    **{"cie1000HttpsMib": cie1000HttpsMib,
       "cie1000HttpsMibObjects": cie1000HttpsMibObjects,
       "cie1000HttpsConfig": cie1000HttpsConfig,
       "cie1000HttpsConfigGlobals": cie1000HttpsConfigGlobals,
       "cie1000HttpsConfigGlobalsMode": cie1000HttpsConfigGlobalsMode,
       "cie1000HttpsConfigGlobalsRedirectToHttps": cie1000HttpsConfigGlobalsRedirectToHttps,
       "cie1000HttpsMibConformance": cie1000HttpsMibConformance,
       "cie1000HttpsMibCompliances": cie1000HttpsMibCompliances,
       "cie1000HttpsMibCompliance": cie1000HttpsMibCompliance,
       "cie1000HttpsMibGroups": cie1000HttpsMibGroups,
       "cie1000HttpsConfigGlobalsInfoGroup": cie1000HttpsConfigGlobalsInfoGroup}
)
