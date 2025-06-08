# SNMP MIB module (ME1200-HTTPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-HTTPS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

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

me1200HttpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47)
)
if mibBuilder.loadTexts:
    me1200HttpsMIB.setRevisions(
        ("2014-01-29 00:00",
         "2013-10-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200HttpsMIBObjects_ObjectIdentity = ObjectIdentity
me1200HttpsMIBObjects = _Me1200HttpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1)
)
_Me1200HttpsConfig_ObjectIdentity = ObjectIdentity
me1200HttpsConfig = _Me1200HttpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2)
)
_Me1200HttpsGlobals_ObjectIdentity = ObjectIdentity
me1200HttpsGlobals = _Me1200HttpsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2, 1)
)
_Me1200HttpsGlobalsMode_Type = TruthValue
_Me1200HttpsGlobalsMode_Object = MibScalar
me1200HttpsGlobalsMode = _Me1200HttpsGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2, 1, 1),
    _Me1200HttpsGlobalsMode_Type()
)
me1200HttpsGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HttpsGlobalsMode.setStatus("current")
_Me1200HttpsGlobalsRedirectToHttps_Type = TruthValue
_Me1200HttpsGlobalsRedirectToHttps_Object = MibScalar
me1200HttpsGlobalsRedirectToHttps = _Me1200HttpsGlobalsRedirectToHttps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2, 1, 2),
    _Me1200HttpsGlobalsRedirectToHttps_Type()
)
me1200HttpsGlobalsRedirectToHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200HttpsGlobalsRedirectToHttps.setStatus("current")
_Me1200HttpsMIBConformance_ObjectIdentity = ObjectIdentity
me1200HttpsMIBConformance = _Me1200HttpsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2)
)
_Me1200HttpsMIBCompliances_ObjectIdentity = ObjectIdentity
me1200HttpsMIBCompliances = _Me1200HttpsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 1)
)
_Me1200HttpsMIBGroups_ObjectIdentity = ObjectIdentity
me1200HttpsMIBGroups = _Me1200HttpsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 2)
)

# Managed Objects groups

me1200HttpsGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 2, 1)
)
me1200HttpsGlobalsInfoGroup.setObjects(
      *(("ME1200-HTTPS-MIB", "me1200HttpsGlobalsMode"),
        ("ME1200-HTTPS-MIB", "me1200HttpsGlobalsRedirectToHttps"))
)
if mibBuilder.loadTexts:
    me1200HttpsGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200HttpsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 1, 1)
)
me1200HttpsMIBCompliance.setObjects(
    ("ME1200-HTTPS-MIB", "me1200HttpsGlobalsInfoGroup")
)
if mibBuilder.loadTexts:
    me1200HttpsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-HTTPS-MIB",
    **{"me1200HttpsMIB": me1200HttpsMIB,
       "me1200HttpsMIBObjects": me1200HttpsMIBObjects,
       "me1200HttpsConfig": me1200HttpsConfig,
       "me1200HttpsGlobals": me1200HttpsGlobals,
       "me1200HttpsGlobalsMode": me1200HttpsGlobalsMode,
       "me1200HttpsGlobalsRedirectToHttps": me1200HttpsGlobalsRedirectToHttps,
       "me1200HttpsMIBConformance": me1200HttpsMIBConformance,
       "me1200HttpsMIBCompliances": me1200HttpsMIBCompliances,
       "me1200HttpsMIBCompliance": me1200HttpsMIBCompliance,
       "me1200HttpsMIBGroups": me1200HttpsMIBGroups,
       "me1200HttpsGlobalsInfoGroup": me1200HttpsGlobalsInfoGroup}
)
