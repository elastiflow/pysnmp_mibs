# SNMP MIB module (WWP-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-DHCP-CLIENT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:51:13 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpDhcpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18)
)
if mibBuilder.loadTexts:
    wwpDhcpClientMIB.setRevisions(
        ("2001-04-03 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpDhcpClientMIBObjects = _WwpDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 1)
)
_WwpDhcpClient_ObjectIdentity = ObjectIdentity
wwpDhcpClient = _WwpDhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1)
)


class _WwpDhcpActivate_Type(TruthValue):
    """Custom type wwpDhcpActivate based on TruthValue"""
    defaultValue = 2


_WwpDhcpActivate_Type.__name__ = "TruthValue"
_WwpDhcpActivate_Object = MibScalar
wwpDhcpActivate = _WwpDhcpActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 1),
    _WwpDhcpActivate_Type()
)
wwpDhcpActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpActivate.setStatus("current")


class _WwpDhcpIfName_Type(DisplayString):
    """Custom type wwpDhcpIfName based on DisplayString"""
    defaultValue = OctetString("mgmt")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpDhcpIfName_Type.__name__ = "DisplayString"
_WwpDhcpIfName_Object = MibScalar
wwpDhcpIfName = _WwpDhcpIfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 2),
    _WwpDhcpIfName_Type()
)
wwpDhcpIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpIfName.setStatus("current")


class _WwpDhcpDiscoveryMsgInterval_Type(Integer32):
    """Custom type wwpDhcpDiscoveryMsgInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpDiscoveryMsgInterval_Type.__name__ = "Integer32"
_WwpDhcpDiscoveryMsgInterval_Object = MibScalar
wwpDhcpDiscoveryMsgInterval = _WwpDhcpDiscoveryMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 3),
    _WwpDhcpDiscoveryMsgInterval_Type()
)
wwpDhcpDiscoveryMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpDiscoveryMsgInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpDiscoveryMsgInterval.setUnits("miliseconds")


class _WwpDhcpLeaseTime_Type(Integer32):
    """Custom type wwpDhcpLeaseTime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpDhcpLeaseTime_Type.__name__ = "Integer32"
_WwpDhcpLeaseTime_Object = MibScalar
wwpDhcpLeaseTime = _WwpDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 4),
    _WwpDhcpLeaseTime_Type()
)
wwpDhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDhcpLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpDhcpLeaseTime.setUnits("Hours")
_WwpDhcpClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpDhcpClientMIBNotificationPrefix = _WwpDhcpClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 2)
)
_WwpDhcpClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpDhcpClientMIBNotifications = _WwpDhcpClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 2, 0)
)
_WwpDhcpClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpDhcpClientMIBConformance = _WwpDhcpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 3)
)
_WwpDhcpClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpDhcpClientMIBCompliances = _WwpDhcpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 3, 1)
)
_WwpDhcpClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpDhcpClientMIBGroups = _WwpDhcpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 18, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-DHCP-CLIENT-MIB",
    **{"wwpDhcpClientMIB": wwpDhcpClientMIB,
       "wwpDhcpClientMIBObjects": wwpDhcpClientMIBObjects,
       "wwpDhcpClient": wwpDhcpClient,
       "wwpDhcpActivate": wwpDhcpActivate,
       "wwpDhcpIfName": wwpDhcpIfName,
       "wwpDhcpDiscoveryMsgInterval": wwpDhcpDiscoveryMsgInterval,
       "wwpDhcpLeaseTime": wwpDhcpLeaseTime,
       "wwpDhcpClientMIBNotificationPrefix": wwpDhcpClientMIBNotificationPrefix,
       "wwpDhcpClientMIBNotifications": wwpDhcpClientMIBNotifications,
       "wwpDhcpClientMIBConformance": wwpDhcpClientMIBConformance,
       "wwpDhcpClientMIBCompliances": wwpDhcpClientMIBCompliances,
       "wwpDhcpClientMIBGroups": wwpDhcpClientMIBGroups}
)
