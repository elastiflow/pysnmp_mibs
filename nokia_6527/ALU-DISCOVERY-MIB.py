# SNMP MIB module (ALU-DISCOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-DISCOVERY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxChassisIndex,
 tmnxChassisNotifyHwIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex",
    "tmnxChassisNotifyHwIndex")

(alcatelCommonMIBModules,
 alcatelConformance,
 alcatelNotifyPrefix,
 alcatelObjects) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "alcatelCommonMIBModules",
    "alcatelConformance",
    "alcatelNotifyPrefix",
    "alcatelObjects")


# MODULE-IDENTITY

aluDiscoveryMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    aluDiscoveryMIBModule.setRevisions(
        ("1909-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluDiscoveryStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAutoDiscovery", 0),
          ("inProgress", 1),
          ("halted", 2),
          ("terminated", 4),
          ("successful", 5))
    )



class AluDiscoveryStage(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("selfDiscovery", 1),
          ("aquiringNetwork", 2),
          ("aquiringConfig", 3),
          ("testAndCommitConfig", 4))
    )



class AluDiscoveryCircuitId(DisplayString):
    status = "current"


class AluDiscoveryFailureFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("configConflict", 0),
          ("eqNotReady", 1),
          ("noPortsReady", 2),
          ("noNetworkFound", 3),
          ("ipRequestFailed", 4),
          ("portSelectFailed", 5),
          ("configLoadingProblem", 6),
          ("configTestingFailed", 7),
          ("configCommitProblem", 8))
    )


# MIB Managed Objects in the order of their OIDs

_AluDiscoveryMIBConformance_ObjectIdentity = ObjectIdentity
aluDiscoveryMIBConformance = _AluDiscoveryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4)
)
_AluDiscoveryConformance_ObjectIdentity = ObjectIdentity
aluDiscoveryConformance = _AluDiscoveryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1)
)
_AluDiscoveryCompliances_ObjectIdentity = ObjectIdentity
aluDiscoveryCompliances = _AluDiscoveryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 1)
)
_AluDiscoveryComp7705_ObjectIdentity = ObjectIdentity
aluDiscoveryComp7705 = _AluDiscoveryComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 1, 1)
)
_AluDiscoveryGroups_ObjectIdentity = ObjectIdentity
aluDiscoveryGroups = _AluDiscoveryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 2)
)
_AluDiscoveryObjs_ObjectIdentity = ObjectIdentity
aluDiscoveryObjs = _AluDiscoveryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4)
)
_AluDiscoveryTable_Object = MibTable
aluDiscoveryTable = _AluDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    aluDiscoveryTable.setStatus("current")
_AluDiscoveryEntry_Object = MibTableRow
aluDiscoveryEntry = _AluDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1)
)
aluDiscoveryEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    aluDiscoveryEntry.setStatus("current")
_AluDiscoveryStatus_Type = AluDiscoveryStatus
_AluDiscoveryStatus_Object = MibTableColumn
aluDiscoveryStatus = _AluDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 1),
    _AluDiscoveryStatus_Type()
)
aluDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryStatus.setStatus("current")
_AluDiscoveryStage_Type = AluDiscoveryStage
_AluDiscoveryStage_Object = MibTableColumn
aluDiscoveryStage = _AluDiscoveryStage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 2),
    _AluDiscoveryStage_Type()
)
aluDiscoveryStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryStage.setStatus("current")
_AluDiscoveryStartTime_Type = TimeStamp
_AluDiscoveryStartTime_Object = MibTableColumn
aluDiscoveryStartTime = _AluDiscoveryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 3),
    _AluDiscoveryStartTime_Type()
)
aluDiscoveryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryStartTime.setStatus("current")
_AluDiscoveryEndTime_Type = TimeStamp
_AluDiscoveryEndTime_Object = MibTableColumn
aluDiscoveryEndTime = _AluDiscoveryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 4),
    _AluDiscoveryEndTime_Type()
)
aluDiscoveryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryEndTime.setStatus("current")
_AluDiscoverySystemIpAddr_Type = IpAddress
_AluDiscoverySystemIpAddr_Object = MibTableColumn
aluDiscoverySystemIpAddr = _AluDiscoverySystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 5),
    _AluDiscoverySystemIpAddr_Type()
)
aluDiscoverySystemIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoverySystemIpAddr.setStatus("current")
_AluDiscoverySystemSubnet_Type = IpAddress
_AluDiscoverySystemSubnet_Object = MibTableColumn
aluDiscoverySystemSubnet = _AluDiscoverySystemSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 6),
    _AluDiscoverySystemSubnet_Type()
)
aluDiscoverySystemSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoverySystemSubnet.setStatus("current")
_AluDiscoveryLocalCircId_Type = AluDiscoveryCircuitId
_AluDiscoveryLocalCircId_Object = MibTableColumn
aluDiscoveryLocalCircId = _AluDiscoveryLocalCircId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 7),
    _AluDiscoveryLocalCircId_Type()
)
aluDiscoveryLocalCircId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryLocalCircId.setStatus("current")
_AluDiscoveryLocalIpAddr_Type = IpAddress
_AluDiscoveryLocalIpAddr_Object = MibTableColumn
aluDiscoveryLocalIpAddr = _AluDiscoveryLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 8),
    _AluDiscoveryLocalIpAddr_Type()
)
aluDiscoveryLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryLocalIpAddr.setStatus("current")
_AluDiscoveryLocalSubnet_Type = IpAddress
_AluDiscoveryLocalSubnet_Object = MibTableColumn
aluDiscoveryLocalSubnet = _AluDiscoveryLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 9),
    _AluDiscoveryLocalSubnet_Type()
)
aluDiscoveryLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryLocalSubnet.setStatus("current")
_AluDiscoveryGatewayCircId_Type = AluDiscoveryCircuitId
_AluDiscoveryGatewayCircId_Object = MibTableColumn
aluDiscoveryGatewayCircId = _AluDiscoveryGatewayCircId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 10),
    _AluDiscoveryGatewayCircId_Type()
)
aluDiscoveryGatewayCircId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryGatewayCircId.setStatus("current")
_AluDiscoveryGatewayRemId_Type = DisplayString
_AluDiscoveryGatewayRemId_Object = MibTableColumn
aluDiscoveryGatewayRemId = _AluDiscoveryGatewayRemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 11),
    _AluDiscoveryGatewayRemId_Type()
)
aluDiscoveryGatewayRemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryGatewayRemId.setStatus("current")
_AluDiscoveryGatewayIpAddr_Type = IpAddress
_AluDiscoveryGatewayIpAddr_Object = MibTableColumn
aluDiscoveryGatewayIpAddr = _AluDiscoveryGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 12),
    _AluDiscoveryGatewayIpAddr_Type()
)
aluDiscoveryGatewayIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryGatewayIpAddr.setStatus("current")
_AluDiscoveryServerIpAddr_Type = IpAddress
_AluDiscoveryServerIpAddr_Object = MibTableColumn
aluDiscoveryServerIpAddr = _AluDiscoveryServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 13),
    _AluDiscoveryServerIpAddr_Type()
)
aluDiscoveryServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryServerIpAddr.setStatus("current")
_AluDiscoveryFailureFlags_Type = AluDiscoveryFailureFlags
_AluDiscoveryFailureFlags_Object = MibTableColumn
aluDiscoveryFailureFlags = _AluDiscoveryFailureFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 14),
    _AluDiscoveryFailureFlags_Type()
)
aluDiscoveryFailureFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDiscoveryFailureFlags.setStatus("current")
_AluDiscoveryBofInfo_ObjectIdentity = ObjectIdentity
aluDiscoveryBofInfo = _AluDiscoveryBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2)
)


class _AluSbiAutoDiscover_Type(TruthValue):
    """Custom type aluSbiAutoDiscover based on TruthValue"""
    defaultValue = 2


_AluSbiAutoDiscover_Type.__name__ = "TruthValue"
_AluSbiAutoDiscover_Object = MibScalar
aluSbiAutoDiscover = _AluSbiAutoDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2, 1),
    _AluSbiAutoDiscover_Type()
)
aluSbiAutoDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSbiAutoDiscover.setStatus("current")


class _AluSbiAutoDiscoverId_Type(DisplayString):
    """Custom type aluSbiAutoDiscoverId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AluSbiAutoDiscoverId_Type.__name__ = "DisplayString"
_AluSbiAutoDiscoverId_Object = MibScalar
aluSbiAutoDiscoverId = _AluSbiAutoDiscoverId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2, 2),
    _AluSbiAutoDiscoverId_Type()
)
aluSbiAutoDiscoverId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSbiAutoDiscoverId.setStatus("current")


class _AluSbiAutoDiscoverVlan_Type(Unsigned32):
    """Custom type aluSbiAutoDiscoverVlan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AluSbiAutoDiscoverVlan_Type.__name__ = "Unsigned32"
_AluSbiAutoDiscoverVlan_Object = MibScalar
aluSbiAutoDiscoverVlan = _AluSbiAutoDiscoverVlan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2, 3),
    _AluSbiAutoDiscoverVlan_Type()
)
aluSbiAutoDiscoverVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSbiAutoDiscoverVlan.setStatus("current")
_AluDiscoveryNotificationsPrefix_ObjectIdentity = ObjectIdentity
aluDiscoveryNotificationsPrefix = _AluDiscoveryNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4)
)
_AluDiscoveryNotifications_ObjectIdentity = ObjectIdentity
aluDiscoveryNotifications = _AluDiscoveryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0)
)

# Managed Objects groups

aluDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 2, 1)
)
aluDiscoveryGroup.setObjects(
      *(("ALU-DISCOVERY-MIB", "aluDiscoveryStatus"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryStage"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryStartTime"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryEndTime"),
        ("ALU-DISCOVERY-MIB", "aluDiscoverySystemIpAddr"),
        ("ALU-DISCOVERY-MIB", "aluDiscoverySystemSubnet"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalCircId"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalIpAddr"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalSubnet"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayCircId"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayRemId"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayIpAddr"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryServerIpAddr"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryFailureFlags"),
        ("ALU-DISCOVERY-MIB", "aluSbiAutoDiscover"),
        ("ALU-DISCOVERY-MIB", "aluSbiAutoDiscoverId"),
        ("ALU-DISCOVERY-MIB", "aluSbiAutoDiscoverVlan"))
)
if mibBuilder.loadTexts:
    aluDiscoveryGroup.setStatus("current")


# Notification objects

aluDiscoveryStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0, 1)
)
if mibBuilder.loadTexts:
    aluDiscoveryStarted.setStatus(
        "current"
    )

aluDiscoveryTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0, 2)
)
aluDiscoveryTerminated.setObjects(
    ("ALU-DISCOVERY-MIB", "aluDiscoveryFailureFlags")
)
if mibBuilder.loadTexts:
    aluDiscoveryTerminated.setStatus(
        "current"
    )

aluDiscoverySuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0, 3)
)
aluDiscoverySuccessful.setObjects(
      *(("ALU-DISCOVERY-MIB", "aluDiscoverySystemIpAddr"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalCircId"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalIpAddr"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayCircId"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayIpAddr"))
)
if mibBuilder.loadTexts:
    aluDiscoverySuccessful.setStatus(
        "current"
    )


# Notifications groups

aluDiscoveryNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 2, 2)
)
aluDiscoveryNotificationGroup.setObjects(
      *(("ALU-DISCOVERY-MIB", "aluDiscoveryStarted"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryTerminated"),
        ("ALU-DISCOVERY-MIB", "aluDiscoverySuccessful"))
)
if mibBuilder.loadTexts:
    aluDiscoveryNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluDiscoveryComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 1, 1, 1)
)
aluDiscoveryComp7705V1v0.setObjects(
      *(("ALU-DISCOVERY-MIB", "aluDiscoveryGroup"),
        ("ALU-DISCOVERY-MIB", "aluDiscoveryNotificationGroup"))
)
if mibBuilder.loadTexts:
    aluDiscoveryComp7705V1v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-DISCOVERY-MIB",
    **{"AluDiscoveryStatus": AluDiscoveryStatus,
       "AluDiscoveryStage": AluDiscoveryStage,
       "AluDiscoveryCircuitId": AluDiscoveryCircuitId,
       "AluDiscoveryFailureFlags": AluDiscoveryFailureFlags,
       "aluDiscoveryMIBModule": aluDiscoveryMIBModule,
       "aluDiscoveryMIBConformance": aluDiscoveryMIBConformance,
       "aluDiscoveryConformance": aluDiscoveryConformance,
       "aluDiscoveryCompliances": aluDiscoveryCompliances,
       "aluDiscoveryComp7705": aluDiscoveryComp7705,
       "aluDiscoveryComp7705V1v0": aluDiscoveryComp7705V1v0,
       "aluDiscoveryGroups": aluDiscoveryGroups,
       "aluDiscoveryGroup": aluDiscoveryGroup,
       "aluDiscoveryNotificationGroup": aluDiscoveryNotificationGroup,
       "aluDiscoveryObjs": aluDiscoveryObjs,
       "aluDiscoveryTable": aluDiscoveryTable,
       "aluDiscoveryEntry": aluDiscoveryEntry,
       "aluDiscoveryStatus": aluDiscoveryStatus,
       "aluDiscoveryStage": aluDiscoveryStage,
       "aluDiscoveryStartTime": aluDiscoveryStartTime,
       "aluDiscoveryEndTime": aluDiscoveryEndTime,
       "aluDiscoverySystemIpAddr": aluDiscoverySystemIpAddr,
       "aluDiscoverySystemSubnet": aluDiscoverySystemSubnet,
       "aluDiscoveryLocalCircId": aluDiscoveryLocalCircId,
       "aluDiscoveryLocalIpAddr": aluDiscoveryLocalIpAddr,
       "aluDiscoveryLocalSubnet": aluDiscoveryLocalSubnet,
       "aluDiscoveryGatewayCircId": aluDiscoveryGatewayCircId,
       "aluDiscoveryGatewayRemId": aluDiscoveryGatewayRemId,
       "aluDiscoveryGatewayIpAddr": aluDiscoveryGatewayIpAddr,
       "aluDiscoveryServerIpAddr": aluDiscoveryServerIpAddr,
       "aluDiscoveryFailureFlags": aluDiscoveryFailureFlags,
       "aluDiscoveryBofInfo": aluDiscoveryBofInfo,
       "aluSbiAutoDiscover": aluSbiAutoDiscover,
       "aluSbiAutoDiscoverId": aluSbiAutoDiscoverId,
       "aluSbiAutoDiscoverVlan": aluSbiAutoDiscoverVlan,
       "aluDiscoveryNotificationsPrefix": aluDiscoveryNotificationsPrefix,
       "aluDiscoveryNotifications": aluDiscoveryNotifications,
       "aluDiscoveryStarted": aluDiscoveryStarted,
       "aluDiscoveryTerminated": aluDiscoveryTerminated,
       "aluDiscoverySuccessful": aluDiscoverySuccessful}
)
