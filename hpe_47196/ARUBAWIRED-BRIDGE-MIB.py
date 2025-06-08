# SNMP MIB module (ARUBAWIRED-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hpe_47196/ARUBAWIRED-BRIDGE-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:59:27 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(dot1dBasePortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePortEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanId,
 VlanIndex,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex",
    "dot1qVlanStaticEntry")

(portCopyEntry,) = mibBuilder.importSymbols(
    "SMON-MIB",
    "portCopyEntry")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ArubaWiredBridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class ConfigStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3))
    )



class VidList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixedLength = 512



class LoopProtectReceiverAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableTx", 1),
          ("noDisable", 2),
          ("disableTxRx", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredBridgeObjects_ObjectIdentity = ObjectIdentity
arubaWiredBridgeObjects = _ArubaWiredBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1)
)
_ArubaWiredBridgeBase_ObjectIdentity = ObjectIdentity
arubaWiredBridgeBase = _ArubaWiredBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 1)
)
_ArubaWiredLoopProtect_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtect = _ArubaWiredLoopProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5)
)
_ArubaWiredLoopProtectNotifications_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectNotifications = _ArubaWiredLoopProtectNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0)
)
_ArubaWiredLoopProtectBase_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectBase = _ArubaWiredLoopProtectBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1)
)


class _ArubaWiredLoopProtectInterval_Type(Integer32):
    """Custom type arubaWiredLoopProtectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ArubaWiredLoopProtectInterval_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectInterval_Object = MibScalar
arubaWiredLoopProtectInterval = _ArubaWiredLoopProtectInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 1),
    _ArubaWiredLoopProtectInterval_Type()
)
arubaWiredLoopProtectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectInterval.setStatus("current")
_ArubaWiredLoopProtectTrapLoopDetectEnable_Type = TruthValue
_ArubaWiredLoopProtectTrapLoopDetectEnable_Object = MibScalar
arubaWiredLoopProtectTrapLoopDetectEnable = _ArubaWiredLoopProtectTrapLoopDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 2),
    _ArubaWiredLoopProtectTrapLoopDetectEnable_Type()
)
arubaWiredLoopProtectTrapLoopDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectTrapLoopDetectEnable.setStatus("current")


class _ArubaWiredLoopProtectEnableTimer_Type(Integer32):
    """Custom type arubaWiredLoopProtectEnableTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArubaWiredLoopProtectEnableTimer_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectEnableTimer_Object = MibScalar
arubaWiredLoopProtectEnableTimer = _ArubaWiredLoopProtectEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 3),
    _ArubaWiredLoopProtectEnableTimer_Type()
)
arubaWiredLoopProtectEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectEnableTimer.setStatus("current")


class _ArubaWiredLoopProtectMode_Type(Integer32):
    """Custom type arubaWiredLoopProtectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_ArubaWiredLoopProtectMode_Type.__name__ = "Integer32"
_ArubaWiredLoopProtectMode_Object = MibScalar
arubaWiredLoopProtectMode = _ArubaWiredLoopProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 4),
    _ArubaWiredLoopProtectMode_Type()
)
arubaWiredLoopProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectMode.setStatus("current")
_ArubaWiredLoopProtectVIDList_Type = VidList
_ArubaWiredLoopProtectVIDList_Object = MibScalar
arubaWiredLoopProtectVIDList = _ArubaWiredLoopProtectVIDList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 5),
    _ArubaWiredLoopProtectVIDList_Type()
)
arubaWiredLoopProtectVIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectVIDList.setStatus("current")
_ArubaWiredLoopProtectPort_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectPort = _ArubaWiredLoopProtectPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2)
)
_ArubaWiredLoopProtectPortTable_Object = MibTable
arubaWiredLoopProtectPortTable = _ArubaWiredLoopProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortTable.setStatus("current")
_ArubaWiredLoopProtectPortEntry_Object = MibTableRow
arubaWiredLoopProtectPortEntry = _ArubaWiredLoopProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1)
)
arubaWiredLoopProtectPortEntry.setIndexNames(
    (0, "ARUBAWIRED-BRIDGE-MIB", "arubaWiredLoopProtectPortInterfaceIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortEntry.setStatus("current")
_ArubaWiredLoopProtectPortInterfaceIndex_Type = InterfaceIndex
_ArubaWiredLoopProtectPortInterfaceIndex_Object = MibTableColumn
arubaWiredLoopProtectPortInterfaceIndex = _ArubaWiredLoopProtectPortInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 1),
    _ArubaWiredLoopProtectPortInterfaceIndex_Type()
)
arubaWiredLoopProtectPortInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortInterfaceIndex.setStatus("current")
_ArubaWiredLoopProtectPortEnable_Type = TruthValue
_ArubaWiredLoopProtectPortEnable_Object = MibTableColumn
arubaWiredLoopProtectPortEnable = _ArubaWiredLoopProtectPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 2),
    _ArubaWiredLoopProtectPortEnable_Type()
)
arubaWiredLoopProtectPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortEnable.setStatus("current")
_ArubaWiredLoopProtectPortLoopDetected_Type = TruthValue
_ArubaWiredLoopProtectPortLoopDetected_Object = MibTableColumn
arubaWiredLoopProtectPortLoopDetected = _ArubaWiredLoopProtectPortLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 3),
    _ArubaWiredLoopProtectPortLoopDetected_Type()
)
arubaWiredLoopProtectPortLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortLoopDetected.setStatus("current")
_ArubaWiredLoopProtectPortLastLoopTime_Type = TimeStamp
_ArubaWiredLoopProtectPortLastLoopTime_Object = MibTableColumn
arubaWiredLoopProtectPortLastLoopTime = _ArubaWiredLoopProtectPortLastLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 4),
    _ArubaWiredLoopProtectPortLastLoopTime_Type()
)
arubaWiredLoopProtectPortLastLoopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortLastLoopTime.setStatus("current")
_ArubaWiredLoopProtectPortLoopCount_Type = Counter32
_ArubaWiredLoopProtectPortLoopCount_Object = MibTableColumn
arubaWiredLoopProtectPortLoopCount = _ArubaWiredLoopProtectPortLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 5),
    _ArubaWiredLoopProtectPortLoopCount_Type()
)
arubaWiredLoopProtectPortLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortLoopCount.setStatus("current")
_ArubaWiredLoopProtectPortReceiverAction_Type = LoopProtectReceiverAction
_ArubaWiredLoopProtectPortReceiverAction_Object = MibTableColumn
arubaWiredLoopProtectPortReceiverAction = _ArubaWiredLoopProtectPortReceiverAction_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 6),
    _ArubaWiredLoopProtectPortReceiverAction_Type()
)
arubaWiredLoopProtectPortReceiverAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortReceiverAction.setStatus("current")


class _ArubaWiredBridgeLoopDetectedVlan_Type(Integer32):
    """Custom type arubaWiredBridgeLoopDetectedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ArubaWiredBridgeLoopDetectedVlan_Type.__name__ = "Integer32"
_ArubaWiredBridgeLoopDetectedVlan_Object = MibScalar
arubaWiredBridgeLoopDetectedVlan = _ArubaWiredBridgeLoopDetectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 7),
    _ArubaWiredBridgeLoopDetectedVlan_Type()
)
arubaWiredBridgeLoopDetectedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredBridgeLoopDetectedVlan.setStatus("current")
_ArubaWiredLoopProtectPortVlanList_Type = VidList
_ArubaWiredLoopProtectPortVlanList_Object = MibTableColumn
arubaWiredLoopProtectPortVlanList = _ArubaWiredLoopProtectPortVlanList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 8),
    _ArubaWiredLoopProtectPortVlanList_Type()
)
arubaWiredLoopProtectPortVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredLoopProtectPortVlanList.setStatus("current")

# Managed Objects groups


# Notification objects

arubaWiredLoopProtectLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 1)
)
arubaWiredLoopProtectLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARUBAWIRED-BRIDGE-MIB", "arubaWiredLoopProtectPortLoopCount"),
        ("ARUBAWIRED-BRIDGE-MIB", "arubaWiredLoopProtectPortReceiverAction"))
)
if mibBuilder.loadTexts:
    arubaWiredLoopProtectLoopDetectedNotification.setStatus(
        "current"
    )

arubaWiredBridgeVlanLoopProtectLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 2)
)
arubaWiredBridgeVlanLoopProtectLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARUBAWIRED-BRIDGE-MIB", "arubaWiredLoopProtectPortLoopCount"),
        ("ARUBAWIRED-BRIDGE-MIB", "arubaWiredLoopProtectPortReceiverAction"),
        ("ARUBAWIRED-BRIDGE-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
)
if mibBuilder.loadTexts:
    arubaWiredBridgeVlanLoopProtectLoopDetectedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-BRIDGE-MIB",
    **{"ArubaWiredBridgeId": ArubaWiredBridgeId,
       "ConfigStatus": ConfigStatus,
       "VidList": VidList,
       "LoopProtectReceiverAction": LoopProtectReceiverAction,
       "arubaWiredBridgeMIB": arubaWiredBridgeMIB,
       "arubaWiredBridgeObjects": arubaWiredBridgeObjects,
       "arubaWiredBridgeBase": arubaWiredBridgeBase,
       "arubaWiredLoopProtect": arubaWiredLoopProtect,
       "arubaWiredLoopProtectNotifications": arubaWiredLoopProtectNotifications,
       "arubaWiredLoopProtectLoopDetectedNotification": arubaWiredLoopProtectLoopDetectedNotification,
       "arubaWiredBridgeVlanLoopProtectLoopDetectedNotification": arubaWiredBridgeVlanLoopProtectLoopDetectedNotification,
       "arubaWiredLoopProtectBase": arubaWiredLoopProtectBase,
       "arubaWiredLoopProtectInterval": arubaWiredLoopProtectInterval,
       "arubaWiredLoopProtectTrapLoopDetectEnable": arubaWiredLoopProtectTrapLoopDetectEnable,
       "arubaWiredLoopProtectEnableTimer": arubaWiredLoopProtectEnableTimer,
       "arubaWiredLoopProtectMode": arubaWiredLoopProtectMode,
       "arubaWiredLoopProtectVIDList": arubaWiredLoopProtectVIDList,
       "arubaWiredLoopProtectPort": arubaWiredLoopProtectPort,
       "arubaWiredLoopProtectPortTable": arubaWiredLoopProtectPortTable,
       "arubaWiredLoopProtectPortEntry": arubaWiredLoopProtectPortEntry,
       "arubaWiredLoopProtectPortInterfaceIndex": arubaWiredLoopProtectPortInterfaceIndex,
       "arubaWiredLoopProtectPortEnable": arubaWiredLoopProtectPortEnable,
       "arubaWiredLoopProtectPortLoopDetected": arubaWiredLoopProtectPortLoopDetected,
       "arubaWiredLoopProtectPortLastLoopTime": arubaWiredLoopProtectPortLastLoopTime,
       "arubaWiredLoopProtectPortLoopCount": arubaWiredLoopProtectPortLoopCount,
       "arubaWiredLoopProtectPortReceiverAction": arubaWiredLoopProtectPortReceiverAction,
       "arubaWiredBridgeLoopDetectedVlan": arubaWiredBridgeLoopDetectedVlan,
       "arubaWiredLoopProtectPortVlanList": arubaWiredLoopProtectPortVlanList}
)
