# SNMP MIB module (RBN-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-AUTHENTICATION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:57 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rbnAuthenMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18)
)
if mibBuilder.loadTexts:
    rbnAuthenMib.setRevisions(
        ("2002-05-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnAuthenMibNotifications_ObjectIdentity = ObjectIdentity
rbnAuthenMibNotifications = _RbnAuthenMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 0)
)
_RbnAuthenMibObjects_ObjectIdentity = ObjectIdentity
rbnAuthenMibObjects = _RbnAuthenMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1)
)
_RbnAuthen_ObjectIdentity = ObjectIdentity
rbnAuthen = _RbnAuthen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1)
)
_RbnAuthenTable_Object = MibTable
rbnAuthenTable = _RbnAuthenTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAuthenTable.setStatus("current")
_RbnAuthenEntry_Object = MibTableRow
rbnAuthenEntry = _RbnAuthenEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1)
)
rbnAuthenEntry.setIndexNames(
    (0, "RBN-AUTHENTICATION-MIB", "rbnAuthenIndex"),
)
if mibBuilder.loadTexts:
    rbnAuthenEntry.setStatus("current")


class _RbnAuthenIndex_Type(Unsigned32):
    """Custom type rbnAuthenIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnAuthenIndex_Type.__name__ = "Unsigned32"
_RbnAuthenIndex_Object = MibTableColumn
rbnAuthenIndex = _RbnAuthenIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1, 1),
    _RbnAuthenIndex_Type()
)
rbnAuthenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAuthenIndex.setStatus("current")


class _RbnAuthenUsername_Type(SnmpAdminString):
    """Custom type rbnAuthenUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RbnAuthenUsername_Type.__name__ = "SnmpAdminString"
_RbnAuthenUsername_Object = MibTableColumn
rbnAuthenUsername = _RbnAuthenUsername_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1, 2),
    _RbnAuthenUsername_Type()
)
rbnAuthenUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAuthenUsername.setStatus("current")


class _RbnAuthenContext_Type(SnmpAdminString):
    """Custom type rbnAuthenContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnAuthenContext_Type.__name__ = "SnmpAdminString"
_RbnAuthenContext_Object = MibTableColumn
rbnAuthenContext = _RbnAuthenContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1, 3),
    _RbnAuthenContext_Type()
)
rbnAuthenContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAuthenContext.setStatus("current")
_RbnAuthenIpAddressType_Type = InetAddressType
_RbnAuthenIpAddressType_Object = MibTableColumn
rbnAuthenIpAddressType = _RbnAuthenIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1, 4),
    _RbnAuthenIpAddressType_Type()
)
rbnAuthenIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAuthenIpAddressType.setStatus("current")
_RbnAuthenIpAddress_Type = InetAddress
_RbnAuthenIpAddress_Object = MibTableColumn
rbnAuthenIpAddress = _RbnAuthenIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1, 5),
    _RbnAuthenIpAddress_Type()
)
rbnAuthenIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAuthenIpAddress.setStatus("current")
_RbnAuthenErrorMsgs_Type = SnmpAdminString
_RbnAuthenErrorMsgs_Object = MibTableColumn
rbnAuthenErrorMsgs = _RbnAuthenErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 1, 1, 1, 1, 6),
    _RbnAuthenErrorMsgs_Type()
)
rbnAuthenErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAuthenErrorMsgs.setStatus("current")
_RbnAuthenMibConformance_ObjectIdentity = ObjectIdentity
rbnAuthenMibConformance = _RbnAuthenMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 2)
)
_RbnAuthenMibCompliances_ObjectIdentity = ObjectIdentity
rbnAuthenMibCompliances = _RbnAuthenMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 2, 1)
)
_RbnAuthenMibGroups_ObjectIdentity = ObjectIdentity
rbnAuthenMibGroups = _RbnAuthenMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 2, 2)
)

# Managed Objects groups

rbnAuthenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 2, 2, 1)
)
rbnAuthenGroup.setObjects(
      *(("RBN-AUTHENTICATION-MIB", "rbnAuthenUsername"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenContext"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenIpAddressType"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenIpAddress"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenErrorMsgs"))
)
if mibBuilder.loadTexts:
    rbnAuthenGroup.setStatus("current")


# Notification objects

rbnAuthenCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 0, 1)
)
rbnAuthenCompleted.setObjects(
      *(("RBN-AUTHENTICATION-MIB", "rbnAuthenUsername"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenContext"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenIpAddressType"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenIpAddress"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenErrorMsgs"))
)
if mibBuilder.loadTexts:
    rbnAuthenCompleted.setStatus(
        "current"
    )


# Notifications groups

rbnAuthenNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 2, 2, 2)
)
rbnAuthenNotifyGroup.setObjects(
    ("RBN-AUTHENTICATION-MIB", "rbnAuthenCompleted")
)
if mibBuilder.loadTexts:
    rbnAuthenNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnAuthenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 18, 2, 1, 1)
)
rbnAuthenCompliance.setObjects(
      *(("RBN-AUTHENTICATION-MIB", "rbnAuthenGroup"),
        ("RBN-AUTHENTICATION-MIB", "rbnAuthenNotifyGroup"))
)
if mibBuilder.loadTexts:
    rbnAuthenCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-AUTHENTICATION-MIB",
    **{"rbnAuthenMib": rbnAuthenMib,
       "rbnAuthenMibNotifications": rbnAuthenMibNotifications,
       "rbnAuthenCompleted": rbnAuthenCompleted,
       "rbnAuthenMibObjects": rbnAuthenMibObjects,
       "rbnAuthen": rbnAuthen,
       "rbnAuthenTable": rbnAuthenTable,
       "rbnAuthenEntry": rbnAuthenEntry,
       "rbnAuthenIndex": rbnAuthenIndex,
       "rbnAuthenUsername": rbnAuthenUsername,
       "rbnAuthenContext": rbnAuthenContext,
       "rbnAuthenIpAddressType": rbnAuthenIpAddressType,
       "rbnAuthenIpAddress": rbnAuthenIpAddress,
       "rbnAuthenErrorMsgs": rbnAuthenErrorMsgs,
       "rbnAuthenMibConformance": rbnAuthenMibConformance,
       "rbnAuthenMibCompliances": rbnAuthenMibCompliances,
       "rbnAuthenCompliance": rbnAuthenCompliance,
       "rbnAuthenMibGroups": rbnAuthenMibGroups,
       "rbnAuthenGroup": rbnAuthenGroup,
       "rbnAuthenNotifyGroup": rbnAuthenNotifyGroup}
)
