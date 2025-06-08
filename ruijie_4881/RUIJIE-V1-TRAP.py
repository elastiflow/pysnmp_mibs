# SNMP MIB module (RUIJIE-V1-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-V1-TRAP.mib
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

(ruijieMacNotiHisMacChangedMsg,) = mibBuilder.importSymbols(
    "RUIJIE-ADDRESS-MIB",
    "ruijieMacNotiHisMacChangedMsg")

(ruijieEntityStateChgDesc,
 ruijieTemperatureWarningDesc) = mibBuilder.importSymbols(
    "RUIJIE-ENTITY-MIB",
    "ruijieEntityStateChgDesc",
    "ruijieTemperatureWarningDesc")

(ruijieIgmpInterfaceHostVersion,
 ruijieIgmpInterfaceIfIndex,
 ruijieIgmpInterfaceVersion) = mibBuilder.importSymbols(
    "RUIJIE-IGMP-MIB",
    "ruijieIgmpInterfaceHostVersion",
    "ruijieIgmpInterfaceIfIndex",
    "ruijieIgmpInterfaceVersion")

(lineDetectPosition,
 lineDetectStatus) = mibBuilder.importSymbols(
    "RUIJIE-INTERFACE-MIB",
    "lineDetectPosition",
    "lineDetectStatus")

(switch,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "switch")

(ruijieSMPArpAttackCriticalStatus,
 ruijieSMPArpAttackFrameContent,
 ruijieSMPArpAttackInterfaceIndex,
 ruijieSMPArpAttackInterfacePort,
 ruijieSMPArpAttackInterfaceSlot,
 ruijieSMPArpAttackInterfaceVlanID,
 ruijieSMPArpAttackMac,
 ruijieSMPArpAttackStatus,
 ruijieSMPArpAttackSubnetIP,
 ruijieSMPArpAttackSubnetIPNum,
 ruijieSMPFrameContent,
 ruijieSMPFrameContentLength,
 ruijieSMPSwitchIP,
 ruijieSMPSwitchInterfaceID,
 ruijieSMPSwitchInterfaceVLANID) = mibBuilder.importSymbols(
    "RUIJIE-SMP-MIB",
    "ruijieSMPArpAttackCriticalStatus",
    "ruijieSMPArpAttackFrameContent",
    "ruijieSMPArpAttackInterfaceIndex",
    "ruijieSMPArpAttackInterfacePort",
    "ruijieSMPArpAttackInterfaceSlot",
    "ruijieSMPArpAttackInterfaceVlanID",
    "ruijieSMPArpAttackMac",
    "ruijieSMPArpAttackStatus",
    "ruijieSMPArpAttackSubnetIP",
    "ruijieSMPArpAttackSubnetIPNum",
    "ruijieSMPFrameContent",
    "ruijieSMPFrameContentLength",
    "ruijieSMPSwitchIP",
    "ruijieSMPSwitchInterfaceID",
    "ruijieSMPSwitchInterfaceVLANID")

(ruijieSystemHardChangeDesc,
 ruijieSystemHwFan,
 ruijieSystemHwPower) = mibBuilder.importSymbols(
    "RUIJIE-SYSTEM-MIB",
    "ruijieSystemHardChangeDesc",
    "ruijieSystemHwFan",
    "ruijieSystemHwPower")

(stormViolationAlarmType,) = mibBuilder.importSymbols(
    "RUIJIE-TRAFFIC-CTRL-MIB",
    "stormViolationAlarmType")

(ruijieUrpfIfDropRate,) = mibBuilder.importSymbols(
    "RUIJIE-URPF-MIB",
    "ruijieUrpfIfDropRate")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

sysHardChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 1)
)
sysHardChangeDetected.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemHardChangeDesc")
)
if mibBuilder.loadTexts:
    sysHardChangeDetected.setStatus(
        ""
    )

portSecurityViolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 2)
)
portSecurityViolate.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portSecurityViolate.setStatus(
        ""
    )

stormViolationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 3)
)
stormViolationAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUIJIE-TRAFFIC-CTRL-MIB", "stormViolationAlarmType"))
)
if mibBuilder.loadTexts:
    stormViolationAlarm.setStatus(
        ""
    )

macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 4)
)
macNotification.setObjects(
    ("RUIJIE-ADDRESS-MIB", "ruijieMacNotiHisMacChangedMsg")
)
if mibBuilder.loadTexts:
    macNotification.setStatus(
        ""
    )

powerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 5)
)
powerStateChange.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemHwPower")
)
if mibBuilder.loadTexts:
    powerStateChange.setStatus(
        ""
    )

fanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 6)
)
fanStateChange.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemHwFan")
)
if mibBuilder.loadTexts:
    fanStateChange.setStatus(
        ""
    )

pimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 7)
)
pimNeighborLoss.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    pimNeighborLoss.setStatus(
        ""
    )

igmpVersionConflicted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 8)
)
igmpVersionConflicted.setObjects(
      *(("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceIfIndex"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceVersion"),
        ("RUIJIE-IGMP-MIB", "ruijieIgmpInterfaceHostVersion"))
)
if mibBuilder.loadTexts:
    igmpVersionConflicted.setStatus(
        ""
    )

dvmrpRouteInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 9)
)
if mibBuilder.loadTexts:
    dvmrpRouteInformation.setStatus(
        ""
    )

entityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 10)
)
entityNotification.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    entityNotification.setStatus(
        ""
    )

temperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 12)
)
temperatureWarning.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    temperatureWarning.setStatus(
        ""
    )

lineDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 13)
)
lineDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUIJIE-INTERFACE-MIB", "lineDetectStatus"),
        ("RUIJIE-INTERFACE-MIB", "lineDetectPosition"))
)
if mibBuilder.loadTexts:
    lineDetect.setStatus(
        ""
    )

smpFrameRelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 14)
)
smpFrameRelay.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPSwitchIP"),
        ("RUIJIE-SMP-MIB", "ruijieSMPSwitchInterfaceID"),
        ("RUIJIE-SMP-MIB", "ruijieSMPSwitchInterfaceVLANID"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameContentLength"),
        ("RUIJIE-SMP-MIB", "ruijieSMPFrameContent"))
)
if mibBuilder.loadTexts:
    smpFrameRelay.setStatus(
        ""
    )

smpArpAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 15)
)
smpArpAttack.setObjects(
      *(("RUIJIE-SMP-MIB", "ruijieSMPArpAttackSubnetIP"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackSubnetIPNum"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfaceSlot"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfacePort"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfaceVlanID"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackFrameContent"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackStatus"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackCriticalStatus"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackMac"),
        ("RUIJIE-SMP-MIB", "ruijieSMPArpAttackInterfaceIndex"))
)
if mibBuilder.loadTexts:
    smpArpAttack.setStatus(
        ""
    )

urpfIfDropRateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 0, 17)
)
urpfIfDropRateNotify.setObjects(
    ("RUIJIE-URPF-MIB", "ruijieUrpfIfDropRate")
)
if mibBuilder.loadTexts:
    urpfIfDropRateNotify.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-V1-TRAP",
    **{"sysHardChangeDetected": sysHardChangeDetected,
       "portSecurityViolate": portSecurityViolate,
       "stormViolationAlarm": stormViolationAlarm,
       "macNotification": macNotification,
       "powerStateChange": powerStateChange,
       "fanStateChange": fanStateChange,
       "pimNeighborLoss": pimNeighborLoss,
       "igmpVersionConflicted": igmpVersionConflicted,
       "dvmrpRouteInformation": dvmrpRouteInformation,
       "entityNotification": entityNotification,
       "temperatureWarning": temperatureWarning,
       "lineDetect": lineDetect,
       "smpFrameRelay": smpFrameRelay,
       "smpArpAttack": smpArpAttack,
       "urpfIfDropRateNotify": urpfIfDropRateNotify}
)
