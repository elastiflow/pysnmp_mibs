# SNMP MIB module (SMARTHOME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/autoalert_47534/SMARTHOME-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:40:01 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

shMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1)
)
if mibBuilder.loadTexts:
    shMIB.setRevisions(
        ("2016-05-05 22:12",
         "2016-04-05 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ShMIBObjects_ObjectIdentity = ObjectIdentity
shMIBObjects = _ShMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1)
)
_ShInfo_ObjectIdentity = ObjectIdentity
shInfo = _ShInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 1)
)
_ShVersion_Type = Integer32
_ShVersion_Object = MibScalar
shVersion = _ShVersion_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 1, 1),
    _ShVersion_Type()
)
shVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shVersion.setStatus("current")
_ShVendorName_Type = DisplayString
_ShVendorName_Object = MibScalar
shVendorName = _ShVendorName_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 1, 2),
    _ShVendorName_Type()
)
shVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shVendorName.setStatus("current")
_ShModelType_Type = DisplayString
_ShModelType_Object = MibScalar
shModelType = _ShModelType_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 1, 3),
    _ShModelType_Type()
)
shModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shModelType.setStatus("current")
_ShIpAddress_Type = InetAddressIPv6
_ShIpAddress_Object = MibScalar
shIpAddress = _ShIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 1, 4),
    _ShIpAddress_Type()
)
shIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shIpAddress.setStatus("current")
_ShTable_ObjectIdentity = ObjectIdentity
shTable = _ShTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2)
)
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1, 1)
)
outletEntry.setIndexNames(
    (0, "SMARTHOME-MIB", "shName"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _ShName_Type(DisplayString):
    """Custom type shName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ShName_Type.__name__ = "DisplayString"
_ShName_Object = MibTableColumn
shName = _ShName_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1, 1, 1),
    _ShName_Type()
)
shName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shName.setStatus("current")
_ShLocation_Type = DisplayString
_ShLocation_Object = MibTableColumn
shLocation = _ShLocation_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1, 1, 2),
    _ShLocation_Type()
)
shLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shLocation.setStatus("current")


class _ShStatus_Type(Integer32):
    """Custom type shStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("unreachable", 3))
    )


_ShStatus_Type.__name__ = "Integer32"
_ShStatus_Object = MibTableColumn
shStatus = _ShStatus_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1, 1, 3),
    _ShStatus_Type()
)
shStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shStatus.setStatus("current")


class _ShOperationState_Type(Integer32):
    """Custom type shOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchOn", 1),
          ("switchOff", 2))
    )


_ShOperationState_Type.__name__ = "Integer32"
_ShOperationState_Object = MibTableColumn
shOperationState = _ShOperationState_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1, 1, 4),
    _ShOperationState_Type()
)
shOperationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shOperationState.setStatus("current")
_ShOutletConsumption_Type = Integer32
_ShOutletConsumption_Object = MibTableColumn
shOutletConsumption = _ShOutletConsumption_Object(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 2, 1, 1, 5),
    _ShOutletConsumption_Type()
)
shOutletConsumption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shOutletConsumption.setStatus("current")
_ShNotifications_ObjectIdentity = ObjectIdentity
shNotifications = _ShNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 3)
)
_ShNotificationsPrefix_ObjectIdentity = ObjectIdentity
shNotificationsPrefix = _ShNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 3, 0)
)
_ShMIBConformance_ObjectIdentity = ObjectIdentity
shMIBConformance = _ShMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2)
)
_ShMIBCompliances_ObjectIdentity = ObjectIdentity
shMIBCompliances = _ShMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2, 1)
)
_ShMIBGroups_ObjectIdentity = ObjectIdentity
shMIBGroups = _ShMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2, 2)
)

# Managed Objects groups

shInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2, 2, 1)
)
shInfoGroup.setObjects(
      *(("SMARTHOME-MIB", "shVersion"),
        ("SMARTHOME-MIB", "shVendorName"),
        ("SMARTHOME-MIB", "shModelType"),
        ("SMARTHOME-MIB", "shIpAddress"))
)
if mibBuilder.loadTexts:
    shInfoGroup.setStatus("current")

shTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2, 2, 2)
)
shTableGroup.setObjects(
      *(("SMARTHOME-MIB", "shLocation"),
        ("SMARTHOME-MIB", "shStatus"),
        ("SMARTHOME-MIB", "shOperationState"),
        ("SMARTHOME-MIB", "shOutletConsumption"))
)
if mibBuilder.loadTexts:
    shTableGroup.setStatus("current")


# Notification objects

shOutletUnreachableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47534, 1, 1, 3, 0, 1)
)
shOutletUnreachableNotification.setObjects(
    ("SMARTHOME-MIB", "shLocation")
)
if mibBuilder.loadTexts:
    shOutletUnreachableNotification.setStatus(
        "current"
    )


# Notifications groups

shNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2, 2, 3)
)
shNotificationGroup.setObjects(
    ("SMARTHOME-MIB", "shOutletUnreachableNotification")
)
if mibBuilder.loadTexts:
    shNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

shBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47534, 1, 2, 1, 1)
)
shBasicCompliance.setObjects(
      *(("SMARTHOME-MIB", "shInfoGroup"),
        ("SMARTHOME-MIB", "shTableGroup"),
        ("SMARTHOME-MIB", "shNotificationGroup"))
)
if mibBuilder.loadTexts:
    shBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMARTHOME-MIB",
    **{"shMIB": shMIB,
       "shMIBObjects": shMIBObjects,
       "shInfo": shInfo,
       "shVersion": shVersion,
       "shVendorName": shVendorName,
       "shModelType": shModelType,
       "shIpAddress": shIpAddress,
       "shTable": shTable,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "shName": shName,
       "shLocation": shLocation,
       "shStatus": shStatus,
       "shOperationState": shOperationState,
       "shOutletConsumption": shOutletConsumption,
       "shNotifications": shNotifications,
       "shNotificationsPrefix": shNotificationsPrefix,
       "shOutletUnreachableNotification": shOutletUnreachableNotification,
       "shMIBConformance": shMIBConformance,
       "shMIBCompliances": shMIBCompliances,
       "shBasicCompliance": shBasicCompliance,
       "shMIBGroups": shMIBGroups,
       "shInfoGroup": shInfoGroup,
       "shTableGroup": shTableGroup,
       "shNotificationGroup": shNotificationGroup}
)
