# SNMP MIB module (WWP-EXT-BRIDGE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-EXT-BRIDGE-TRAP-MIB.mib
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

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpPortAdminStatus,
 wwpPortId,
 wwpPortName,
 wwpPortOperStatus,
 wwpPortType) = mibBuilder.importSymbols(
    "WWP-EXT-BRIDGE-MIB",
    "wwpPortAdminStatus",
    "wwpPortId",
    "wwpPortName",
    "wwpPortOperStatus",
    "wwpPortType")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpExtBridgeTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41)
)
if mibBuilder.loadTexts:
    wwpExtBridgeTrapMIB.setRevisions(
        ("2013-04-22 00:00",
         "2002-10-27 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpExtBridgeTrapMIBObjects_ObjectIdentity = ObjectIdentity
wwpExtBridgeTrapMIBObjects = _WwpExtBridgeTrapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 1)
)


class _WwpStndLinkUpDownTrapsEnable_Type(TruthValue):
    """Custom type wwpStndLinkUpDownTrapsEnable based on TruthValue"""
    defaultValue = 1


_WwpStndLinkUpDownTrapsEnable_Type.__name__ = "TruthValue"
_WwpStndLinkUpDownTrapsEnable_Object = MibScalar
wwpStndLinkUpDownTrapsEnable = _WwpStndLinkUpDownTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 1, 1),
    _WwpStndLinkUpDownTrapsEnable_Type()
)
wwpStndLinkUpDownTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpStndLinkUpDownTrapsEnable.setStatus("current")


class _WwpLinkUpDownTrapsEnable_Type(TruthValue):
    """Custom type wwpLinkUpDownTrapsEnable based on TruthValue"""
    defaultValue = 2


_WwpLinkUpDownTrapsEnable_Type.__name__ = "TruthValue"
_WwpLinkUpDownTrapsEnable_Object = MibScalar
wwpLinkUpDownTrapsEnable = _WwpLinkUpDownTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 1, 2),
    _WwpLinkUpDownTrapsEnable_Type()
)
wwpLinkUpDownTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLinkUpDownTrapsEnable.setStatus("current")
_WwpExtBridgeTrapMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpExtBridgeTrapMIBNotificationPrefix = _WwpExtBridgeTrapMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 2)
)
_WwpExtBridgeTrapMIBNotifications_ObjectIdentity = ObjectIdentity
wwpExtBridgeTrapMIBNotifications = _WwpExtBridgeTrapMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 2, 0)
)
_WwpExtBridgeTrapMIBConformance_ObjectIdentity = ObjectIdentity
wwpExtBridgeTrapMIBConformance = _WwpExtBridgeTrapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 3)
)
_WwpExtBridgeTrapMIBCompliances_ObjectIdentity = ObjectIdentity
wwpExtBridgeTrapMIBCompliances = _WwpExtBridgeTrapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 3, 1)
)
_WwpExtBridgeTrapMIBGroups_ObjectIdentity = ObjectIdentity
wwpExtBridgeTrapMIBGroups = _WwpExtBridgeTrapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 2, 0, 1)
)
wwpLinkUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortId"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortName"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortType"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortAdminStatus"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortOperStatus"))
)
if mibBuilder.loadTexts:
    wwpLinkUp.setStatus(
        "current"
    )

wwpLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 41, 2, 0, 2)
)
wwpLinkDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortId"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortType"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortName"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortAdminStatus"),
        ("WWP-EXT-BRIDGE-MIB", "wwpPortOperStatus"))
)
if mibBuilder.loadTexts:
    wwpLinkDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-EXT-BRIDGE-TRAP-MIB",
    **{"wwpExtBridgeTrapMIB": wwpExtBridgeTrapMIB,
       "wwpExtBridgeTrapMIBObjects": wwpExtBridgeTrapMIBObjects,
       "wwpStndLinkUpDownTrapsEnable": wwpStndLinkUpDownTrapsEnable,
       "wwpLinkUpDownTrapsEnable": wwpLinkUpDownTrapsEnable,
       "wwpExtBridgeTrapMIBNotificationPrefix": wwpExtBridgeTrapMIBNotificationPrefix,
       "wwpExtBridgeTrapMIBNotifications": wwpExtBridgeTrapMIBNotifications,
       "wwpLinkUp": wwpLinkUp,
       "wwpLinkDown": wwpLinkDown,
       "wwpExtBridgeTrapMIBConformance": wwpExtBridgeTrapMIBConformance,
       "wwpExtBridgeTrapMIBCompliances": wwpExtBridgeTrapMIBCompliances,
       "wwpExtBridgeTrapMIBGroups": wwpExtBridgeTrapMIBGroups}
)
