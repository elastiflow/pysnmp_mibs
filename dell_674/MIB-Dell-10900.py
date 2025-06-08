# SNMP MIB module (MIB-Dell-10900) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/MIB-Dell-10900.mib
# Produced by pysmi-1.5.11 at Wed May 21 16:21:41 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )





class DellString1(DisplayString):
    """Custom type DellString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_ItAssistant_ObjectIdentity = ObjectIdentity
itAssistant = _ItAssistant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10900)
)
_ItAssistantTrap_ObjectIdentity = ObjectIdentity
itAssistantTrap = _ItAssistantTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1)
)
_ItaAlertMessage_Type = DellString
_ItaAlertMessage_Object = MibScalar
itaAlertMessage = _ItaAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 1),
    _ItaAlertMessage_Type()
)
itaAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertMessage.setStatus("mandatory")
_ItaAlertNode_Type = DellString
_ItaAlertNode_Object = MibScalar
itaAlertNode = _ItaAlertNode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 2),
    _ItaAlertNode_Type()
)
itaAlertNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertNode.setStatus("mandatory")
_ItaAlertSeverity_Type = DellString1
_ItaAlertSeverity_Object = MibScalar
itaAlertSeverity = _ItaAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 3),
    _ItaAlertSeverity_Type()
)
itaAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertSeverity.setStatus("mandatory")
_ItaAlertCounterName_Type = DellString
_ItaAlertCounterName_Object = MibScalar
itaAlertCounterName = _ItaAlertCounterName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 4),
    _ItaAlertCounterName_Type()
)
itaAlertCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertCounterName.setStatus("mandatory")
_ItaAlertThresholdOperator_Type = DellString
_ItaAlertThresholdOperator_Object = MibScalar
itaAlertThresholdOperator = _ItaAlertThresholdOperator_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 5),
    _ItaAlertThresholdOperator_Type()
)
itaAlertThresholdOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertThresholdOperator.setStatus("mandatory")
_ItaAlertThresholdValue_Type = DellString1
_ItaAlertThresholdValue_Object = MibScalar
itaAlertThresholdValue = _ItaAlertThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 6),
    _ItaAlertThresholdValue_Type()
)
itaAlertThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertThresholdValue.setStatus("mandatory")
_ItaAlertThresholdCount_Type = DellString1
_ItaAlertThresholdCount_Object = MibScalar
itaAlertThresholdCount = _ItaAlertThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 7),
    _ItaAlertThresholdCount_Type()
)
itaAlertThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertThresholdCount.setStatus("mandatory")
_ItaAlertTaskName_Type = DellString1
_ItaAlertTaskName_Object = MibScalar
itaAlertTaskName = _ItaAlertTaskName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 8),
    _ItaAlertTaskName_Type()
)
itaAlertTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itaAlertTaskName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

itaAlertSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 1000)
)
itaAlertSystemUp.setObjects(
      *(("MIB-Dell-10900", "itaAlertMessage"),
        ("MIB-Dell-10900", "itaAlertNode"))
)
if mibBuilder.loadTexts:
    itaAlertSystemUp.setStatus(
        ""
    )

itaAlertSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 1001)
)
itaAlertSystemDown.setObjects(
      *(("MIB-Dell-10900", "itaAlertMessage"),
        ("MIB-Dell-10900", "itaAlertNode"))
)
if mibBuilder.loadTexts:
    itaAlertSystemDown.setStatus(
        ""
    )

itaAlertForwardedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 2000)
)
itaAlertForwardedAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertMessage"),
        ("MIB-Dell-10900", "itaAlertNode"),
        ("MIB-Dell-10900", "itaAlertSeverity"))
)
if mibBuilder.loadTexts:
    itaAlertForwardedAlert.setStatus(
        ""
    )

itaAlertSystemMonitoringCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3001)
)
itaAlertSystemMonitoringCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertSystemMonitoringCriticalAlert.setStatus(
        ""
    )

itaAlertSystemMonitoringWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3002)
)
itaAlertSystemMonitoringWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertSystemMonitoringWarningAlert.setStatus(
        ""
    )

itaAlertCPUMonitoringCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3003)
)
itaAlertCPUMonitoringCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertCPUMonitoringCriticalAlert.setStatus(
        ""
    )

itaAlertCPUMonitoringWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3004)
)
itaAlertCPUMonitoringWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertCPUMonitoringWarningAlert.setStatus(
        ""
    )

itaAlertMemoryMonitoringCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3005)
)
itaAlertMemoryMonitoringCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertMemoryMonitoringCriticalAlert.setStatus(
        ""
    )

itaAlertMemoryMonitoringWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3006)
)
itaAlertMemoryMonitoringWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertMemoryMonitoringWarningAlert.setStatus(
        ""
    )

itaAlertNetworkMonitoringCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3007)
)
itaAlertNetworkMonitoringCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertNetworkMonitoringCriticalAlert.setStatus(
        ""
    )

itaAlertNetworkMonitoringWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3008)
)
itaAlertNetworkMonitoringWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertNetworkMonitoringWarningAlert.setStatus(
        ""
    )

itaAlertPhysicalDiskMonitoringCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3009)
)
itaAlertPhysicalDiskMonitoringCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertPhysicalDiskMonitoringCriticalAlert.setStatus(
        ""
    )

itaAlertPhysicalDiskMonitoringWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3010)
)
itaAlertPhysicalDiskMonitoringWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertPhysicalDiskMonitoringWarningAlert.setStatus(
        ""
    )

itaAlertLogicalDiskMonitoringCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3011)
)
itaAlertLogicalDiskMonitoringCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertLogicalDiskMonitoringCriticalAlert.setStatus(
        ""
    )

itaAlertLogicalDiskMonitoringWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3012)
)
itaAlertLogicalDiskMonitoringWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaAlertLogicalDiskMonitoringWarningAlert.setStatus(
        ""
    )

itaPowerManagementCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3015)
)
itaPowerManagementCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaPowerManagementCriticalAlert.setStatus(
        ""
    )

itaPowerManagementWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3016)
)
itaPowerManagementWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"))
)
if mibBuilder.loadTexts:
    itaPowerManagementWarningAlert.setStatus(
        ""
    )

itaPowerManagementGroupWarningAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3017)
)
itaPowerManagementGroupWarningAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"),
        ("MIB-Dell-10900", "itaAlertTaskName"))
)
if mibBuilder.loadTexts:
    itaPowerManagementGroupWarningAlert.setStatus(
        ""
    )

itaPowerManagementGroupCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10900, 1, 0, 3018)
)
itaPowerManagementGroupCriticalAlert.setObjects(
      *(("MIB-Dell-10900", "itaAlertCounterName"),
        ("MIB-Dell-10900", "itaAlertThresholdOperator"),
        ("MIB-Dell-10900", "itaAlertThresholdValue"),
        ("MIB-Dell-10900", "itaAlertThresholdCount"),
        ("MIB-Dell-10900", "itaAlertTaskName"))
)
if mibBuilder.loadTexts:
    itaPowerManagementGroupCriticalAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-Dell-10900",
    **{"DellString": DellString,
       "DellString1": DellString1,
       "dell": dell,
       "itAssistant": itAssistant,
       "itAssistantTrap": itAssistantTrap,
       "itaAlertSystemUp": itaAlertSystemUp,
       "itaAlertSystemDown": itaAlertSystemDown,
       "itaAlertForwardedAlert": itaAlertForwardedAlert,
       "itaAlertSystemMonitoringCriticalAlert": itaAlertSystemMonitoringCriticalAlert,
       "itaAlertSystemMonitoringWarningAlert": itaAlertSystemMonitoringWarningAlert,
       "itaAlertCPUMonitoringCriticalAlert": itaAlertCPUMonitoringCriticalAlert,
       "itaAlertCPUMonitoringWarningAlert": itaAlertCPUMonitoringWarningAlert,
       "itaAlertMemoryMonitoringCriticalAlert": itaAlertMemoryMonitoringCriticalAlert,
       "itaAlertMemoryMonitoringWarningAlert": itaAlertMemoryMonitoringWarningAlert,
       "itaAlertNetworkMonitoringCriticalAlert": itaAlertNetworkMonitoringCriticalAlert,
       "itaAlertNetworkMonitoringWarningAlert": itaAlertNetworkMonitoringWarningAlert,
       "itaAlertPhysicalDiskMonitoringCriticalAlert": itaAlertPhysicalDiskMonitoringCriticalAlert,
       "itaAlertPhysicalDiskMonitoringWarningAlert": itaAlertPhysicalDiskMonitoringWarningAlert,
       "itaAlertLogicalDiskMonitoringCriticalAlert": itaAlertLogicalDiskMonitoringCriticalAlert,
       "itaAlertLogicalDiskMonitoringWarningAlert": itaAlertLogicalDiskMonitoringWarningAlert,
       "itaPowerManagementCriticalAlert": itaPowerManagementCriticalAlert,
       "itaPowerManagementWarningAlert": itaPowerManagementWarningAlert,
       "itaPowerManagementGroupWarningAlert": itaPowerManagementGroupWarningAlert,
       "itaPowerManagementGroupCriticalAlert": itaPowerManagementGroupCriticalAlert,
       "itaAlertMessage": itaAlertMessage,
       "itaAlertNode": itaAlertNode,
       "itaAlertSeverity": itaAlertSeverity,
       "itaAlertCounterName": itaAlertCounterName,
       "itaAlertThresholdOperator": itaAlertThresholdOperator,
       "itaAlertThresholdValue": itaAlertThresholdValue,
       "itaAlertThresholdCount": itaAlertThresholdCount,
       "itaAlertTaskName": itaAlertTaskName}
)
