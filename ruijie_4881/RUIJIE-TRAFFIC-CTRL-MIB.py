# SNMP MIB module (RUIJIE-TRAFFIC-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TRAFFIC-CTRL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijieTrafficCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14)
)
if mibBuilder.loadTexts:
    ruijieTrafficCtrlMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



# MIB Managed Objects in the order of their OIDs

_RuijieTrafficCtrlMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTrafficCtrlMIBObjects = _RuijieTrafficCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1)
)
_RuijiePtTrafficCtrlTable_Object = MibTable
ruijiePtTrafficCtrlTable = _RuijiePtTrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiePtTrafficCtrlTable.setStatus("current")
_RuijiePtTrafficCtrlEntry_Object = MibTableRow
ruijiePtTrafficCtrlEntry = _RuijiePtTrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1)
)
ruijiePtTrafficCtrlEntry.setIndexNames(
    (0, "RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtTrafficCtrlIfIndex"),
)
if mibBuilder.loadTexts:
    ruijiePtTrafficCtrlEntry.setStatus("current")
_RuijiePtTrafficCtrlIfIndex_Type = IfIndex
_RuijiePtTrafficCtrlIfIndex_Object = MibTableColumn
ruijiePtTrafficCtrlIfIndex = _RuijiePtTrafficCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 1),
    _RuijiePtTrafficCtrlIfIndex_Type()
)
ruijiePtTrafficCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePtTrafficCtrlIfIndex.setStatus("current")


class _RuijiePtProtectedPortStatus_Type(EnabledStatus):
    """Custom type ruijiePtProtectedPortStatus based on EnabledStatus"""
    defaultValue = 2


_RuijiePtProtectedPortStatus_Type.__name__ = "EnabledStatus"
_RuijiePtProtectedPortStatus_Object = MibTableColumn
ruijiePtProtectedPortStatus = _RuijiePtProtectedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 2),
    _RuijiePtProtectedPortStatus_Type()
)
ruijiePtProtectedPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtProtectedPortStatus.setStatus("current")
_RuijiePtBroadcastStormControlStatus_Type = EnabledStatus
_RuijiePtBroadcastStormControlStatus_Object = MibTableColumn
ruijiePtBroadcastStormControlStatus = _RuijiePtBroadcastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 3),
    _RuijiePtBroadcastStormControlStatus_Type()
)
ruijiePtBroadcastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtBroadcastStormControlStatus.setStatus("current")
_RuijiePtMulticastStormControlStatus_Type = EnabledStatus
_RuijiePtMulticastStormControlStatus_Object = MibTableColumn
ruijiePtMulticastStormControlStatus = _RuijiePtMulticastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 4),
    _RuijiePtMulticastStormControlStatus_Type()
)
ruijiePtMulticastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtMulticastStormControlStatus.setStatus("current")
_RuijiePtUnicastStormControlStatus_Type = EnabledStatus
_RuijiePtUnicastStormControlStatus_Object = MibTableColumn
ruijiePtUnicastStormControlStatus = _RuijiePtUnicastStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 5),
    _RuijiePtUnicastStormControlStatus_Type()
)
ruijiePtUnicastStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtUnicastStormControlStatus.setStatus("current")


class _RuijiePtBroadcastStormControlLevel_Type(Percent):
    """Custom type ruijiePtBroadcastStormControlLevel based on Percent"""
    defaultValue = 10


_RuijiePtBroadcastStormControlLevel_Type.__name__ = "Percent"
_RuijiePtBroadcastStormControlLevel_Object = MibTableColumn
ruijiePtBroadcastStormControlLevel = _RuijiePtBroadcastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 6),
    _RuijiePtBroadcastStormControlLevel_Type()
)
ruijiePtBroadcastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtBroadcastStormControlLevel.setStatus("current")


class _RuijiePtMulticastStormControlLevel_Type(Percent):
    """Custom type ruijiePtMulticastStormControlLevel based on Percent"""
    defaultValue = 10


_RuijiePtMulticastStormControlLevel_Type.__name__ = "Percent"
_RuijiePtMulticastStormControlLevel_Object = MibTableColumn
ruijiePtMulticastStormControlLevel = _RuijiePtMulticastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 7),
    _RuijiePtMulticastStormControlLevel_Type()
)
ruijiePtMulticastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtMulticastStormControlLevel.setStatus("current")


class _RuijiePtUnicastStormControlLevel_Type(Percent):
    """Custom type ruijiePtUnicastStormControlLevel based on Percent"""
    defaultValue = 10


_RuijiePtUnicastStormControlLevel_Type.__name__ = "Percent"
_RuijiePtUnicastStormControlLevel_Object = MibTableColumn
ruijiePtUnicastStormControlLevel = _RuijiePtUnicastStormControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 1, 1, 1, 8),
    _RuijiePtUnicastStormControlLevel_Type()
)
ruijiePtUnicastStormControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePtUnicastStormControlLevel.setStatus("current")
_RuijiePtTrafficCtrlTraps_ObjectIdentity = ObjectIdentity
ruijiePtTrafficCtrlTraps = _RuijiePtTrafficCtrlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 2)
)


class _StormViolationAlarmType_Type(Integer32):
    """Custom type stormViolationAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("broadcast", 2),
          ("mutlicast", 3),
          ("unicast", 4))
    )


_StormViolationAlarmType_Type.__name__ = "Integer32"
_StormViolationAlarmType_Object = MibScalar
stormViolationAlarmType = _StormViolationAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 2, 1),
    _StormViolationAlarmType_Type()
)
stormViolationAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stormViolationAlarmType.setStatus("current")
_RuijiePtTrafficCtrlMIBConformance_ObjectIdentity = ObjectIdentity
ruijiePtTrafficCtrlMIBConformance = _RuijiePtTrafficCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3)
)
_RuijiePtTrafficCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
ruijiePtTrafficCtrlMIBCompliances = _RuijiePtTrafficCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 1)
)
_RuijiePtTrafficCtrlMIBGroups_ObjectIdentity = ObjectIdentity
ruijiePtTrafficCtrlMIBGroups = _RuijiePtTrafficCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 2)
)

# Managed Objects groups

ruijiePtTrafficCtrlMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 2, 1)
)
ruijiePtTrafficCtrlMIBGroup.setObjects(
      *(("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtTrafficCtrlIfIndex"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtProtectedPortStatus"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtBroadcastStormControlStatus"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtMulticastStormControlStatus"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtUnicastStormControlStatus"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtBroadcastStormControlLevel"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtMulticastStormControlLevel"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtUnicastStormControlLevel"))
)
if mibBuilder.loadTexts:
    ruijiePtTrafficCtrlMIBGroup.setStatus("current")


# Notification objects

stormViolationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 2, 2)
)
stormViolationAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
)
if mibBuilder.loadTexts:
    stormViolationAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijiePtTrafficCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 14, 3, 1, 1)
)
ruijiePtTrafficCtrlMIBCompliance.setObjects(
    ("RUIJIE-TRAFFIC-CTRL-MIB", "ruijiePtTrafficCtrlMIBGroup")
)
if mibBuilder.loadTexts:
    ruijiePtTrafficCtrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TRAFFIC-CTRL-MIB",
    **{"Percent": Percent,
       "ruijieTrafficCtrlMIB": ruijieTrafficCtrlMIB,
       "ruijieTrafficCtrlMIBObjects": ruijieTrafficCtrlMIBObjects,
       "ruijiePtTrafficCtrlTable": ruijiePtTrafficCtrlTable,
       "ruijiePtTrafficCtrlEntry": ruijiePtTrafficCtrlEntry,
       "ruijiePtTrafficCtrlIfIndex": ruijiePtTrafficCtrlIfIndex,
       "ruijiePtProtectedPortStatus": ruijiePtProtectedPortStatus,
       "ruijiePtBroadcastStormControlStatus": ruijiePtBroadcastStormControlStatus,
       "ruijiePtMulticastStormControlStatus": ruijiePtMulticastStormControlStatus,
       "ruijiePtUnicastStormControlStatus": ruijiePtUnicastStormControlStatus,
       "ruijiePtBroadcastStormControlLevel": ruijiePtBroadcastStormControlLevel,
       "ruijiePtMulticastStormControlLevel": ruijiePtMulticastStormControlLevel,
       "ruijiePtUnicastStormControlLevel": ruijiePtUnicastStormControlLevel,
       "ruijiePtTrafficCtrlTraps": ruijiePtTrafficCtrlTraps,
       "stormViolationAlarmType": stormViolationAlarmType,
       "stormViolationAlarm": stormViolationAlarm,
       "ruijiePtTrafficCtrlMIBConformance": ruijiePtTrafficCtrlMIBConformance,
       "ruijiePtTrafficCtrlMIBCompliances": ruijiePtTrafficCtrlMIBCompliances,
       "ruijiePtTrafficCtrlMIBCompliance": ruijiePtTrafficCtrlMIBCompliance,
       "ruijiePtTrafficCtrlMIBGroups": ruijiePtTrafficCtrlMIBGroups,
       "ruijiePtTrafficCtrlMIBGroup": ruijiePtTrafficCtrlMIBGroup}
)
