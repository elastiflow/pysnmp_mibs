# SNMP MIB module (ME1200-UPNP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-UPNP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(ME1200Unsigned8,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200Unsigned8")

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

me1200UpnpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52)
)
if mibBuilder.loadTexts:
    me1200UpnpMib.setRevisions(
        ("2014-04-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200UpnpMibObjects_ObjectIdentity = ObjectIdentity
me1200UpnpMibObjects = _Me1200UpnpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1)
)
_Me1200UpnpConfig_ObjectIdentity = ObjectIdentity
me1200UpnpConfig = _Me1200UpnpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2)
)
_Me1200UpnpConfigGlobals_ObjectIdentity = ObjectIdentity
me1200UpnpConfigGlobals = _Me1200UpnpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1)
)
_Me1200UpnpConfigGlobalsMode_Type = TruthValue
_Me1200UpnpConfigGlobalsMode_Object = MibScalar
me1200UpnpConfigGlobalsMode = _Me1200UpnpConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1, 1),
    _Me1200UpnpConfigGlobalsMode_Type()
)
me1200UpnpConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UpnpConfigGlobalsMode.setStatus("current")


class _Me1200UpnpConfigGlobalsTtl_Type(ME1200Unsigned8):
    """Custom type me1200UpnpConfigGlobalsTtl based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Me1200UpnpConfigGlobalsTtl_Type.__name__ = "ME1200Unsigned8"
_Me1200UpnpConfigGlobalsTtl_Object = MibScalar
me1200UpnpConfigGlobalsTtl = _Me1200UpnpConfigGlobalsTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1, 2),
    _Me1200UpnpConfigGlobalsTtl_Type()
)
me1200UpnpConfigGlobalsTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UpnpConfigGlobalsTtl.setStatus("current")


class _Me1200UpnpConfigGlobalsAdvertisingDuration_Type(Integer32):
    """Custom type me1200UpnpConfigGlobalsAdvertisingDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_Me1200UpnpConfigGlobalsAdvertisingDuration_Type.__name__ = "Integer32"
_Me1200UpnpConfigGlobalsAdvertisingDuration_Object = MibScalar
me1200UpnpConfigGlobalsAdvertisingDuration = _Me1200UpnpConfigGlobalsAdvertisingDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1, 3),
    _Me1200UpnpConfigGlobalsAdvertisingDuration_Type()
)
me1200UpnpConfigGlobalsAdvertisingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UpnpConfigGlobalsAdvertisingDuration.setStatus("current")
_Me1200UpnpMibConformance_ObjectIdentity = ObjectIdentity
me1200UpnpMibConformance = _Me1200UpnpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2)
)
_Me1200UpnpMibCompliances_ObjectIdentity = ObjectIdentity
me1200UpnpMibCompliances = _Me1200UpnpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 1)
)
_Me1200UpnpMibGroups_ObjectIdentity = ObjectIdentity
me1200UpnpMibGroups = _Me1200UpnpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 2)
)

# Managed Objects groups

me1200UpnpConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 2, 1)
)
me1200UpnpConfigGlobalsInfoGroup.setObjects(
      *(("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsMode"),
        ("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsTtl"),
        ("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsAdvertisingDuration"))
)
if mibBuilder.loadTexts:
    me1200UpnpConfigGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200UpnpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 1, 1)
)
me1200UpnpMibCompliance.setObjects(
    ("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsInfoGroup")
)
if mibBuilder.loadTexts:
    me1200UpnpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-UPNP-MIB",
    **{"me1200UpnpMib": me1200UpnpMib,
       "me1200UpnpMibObjects": me1200UpnpMibObjects,
       "me1200UpnpConfig": me1200UpnpConfig,
       "me1200UpnpConfigGlobals": me1200UpnpConfigGlobals,
       "me1200UpnpConfigGlobalsMode": me1200UpnpConfigGlobalsMode,
       "me1200UpnpConfigGlobalsTtl": me1200UpnpConfigGlobalsTtl,
       "me1200UpnpConfigGlobalsAdvertisingDuration": me1200UpnpConfigGlobalsAdvertisingDuration,
       "me1200UpnpMibConformance": me1200UpnpMibConformance,
       "me1200UpnpMibCompliances": me1200UpnpMibCompliances,
       "me1200UpnpMibCompliance": me1200UpnpMibCompliance,
       "me1200UpnpMibGroups": me1200UpnpMibGroups,
       "me1200UpnpConfigGlobalsInfoGroup": me1200UpnpConfigGlobalsInfoGroup}
)
