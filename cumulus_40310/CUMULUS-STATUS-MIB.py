# SNMP MIB module (CUMULUS-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cumulus_40310/CUMULUS-STATUS-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:08:37 2025
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

(cumulusMib,) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "cumulusMib")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cumulusSystemStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentSwitchSensorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("normal", 3),
          ("warning", 4),
          ("alert", 5),
          ("critical", 6),
          ("NotPresent", 7),
          ("NotOperational", 8))
    )



class AgentSwitchErrorFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("error", 1))
    )



class AgentSwitchPrecision(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 9),
    )



# MIB Managed Objects in the order of their OIDs

_AgentInfoGroup_ObjectIdentity = ObjectIdentity
agentInfoGroup = _AgentInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1)
)
_AgentSwitchCpuProcessGroup_ObjectIdentity = ObjectIdentity
agentSwitchCpuProcessGroup = _AgentSwitchCpuProcessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1)
)
_AgentSwitchCpuProcessMemFree_Type = Integer32
_AgentSwitchCpuProcessMemFree_Object = MibScalar
agentSwitchCpuProcessMemFree = _AgentSwitchCpuProcessMemFree_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 1),
    _AgentSwitchCpuProcessMemFree_Type()
)
agentSwitchCpuProcessMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemFree.setStatus("current")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemFree.setUnits("KBytes")


class _AgentSwitchCpuProcessMemAvailable_Type(Integer32):
    """Custom type agentSwitchCpuProcessMemAvailable based on Integer32"""
    defaultValue = 2


_AgentSwitchCpuProcessMemAvailable_Type.__name__ = "Integer32"
_AgentSwitchCpuProcessMemAvailable_Object = MibScalar
agentSwitchCpuProcessMemAvailable = _AgentSwitchCpuProcessMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 2),
    _AgentSwitchCpuProcessMemAvailable_Type()
)
agentSwitchCpuProcessMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemAvailable.setStatus("current")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemAvailable.setUnits("KBytes")
_AgentSwitchCpuProcessMemTotal_Type = Integer32
_AgentSwitchCpuProcessMemTotal_Object = MibScalar
agentSwitchCpuProcessMemTotal = _AgentSwitchCpuProcessMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 3),
    _AgentSwitchCpuProcessMemTotal_Type()
)
agentSwitchCpuProcessMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemTotal.setStatus("current")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemTotal.setUnits("KBytes")
_AgentSwitchCpuProcessMemPrecision_Type = AgentSwitchPrecision
_AgentSwitchCpuProcessMemPrecision_Object = MibScalar
agentSwitchCpuProcessMemPrecision = _AgentSwitchCpuProcessMemPrecision_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 4),
    _AgentSwitchCpuProcessMemPrecision_Type()
)
agentSwitchCpuProcessMemPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessMemPrecision.setStatus("current")


class _AgentSwitchCpuProcessRisingThreshold_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessRisingThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentSwitchCpuProcessRisingThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessRisingThreshold_Object = MibScalar
agentSwitchCpuProcessRisingThreshold = _AgentSwitchCpuProcessRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 5),
    _AgentSwitchCpuProcessRisingThreshold_Type()
)
agentSwitchCpuProcessRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessRisingThreshold.setStatus("current")


class _AgentSwitchCpuProcessRisingThresholdInterval_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessRisingThresholdInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_AgentSwitchCpuProcessRisingThresholdInterval_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessRisingThresholdInterval_Object = MibScalar
agentSwitchCpuProcessRisingThresholdInterval = _AgentSwitchCpuProcessRisingThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 6),
    _AgentSwitchCpuProcessRisingThresholdInterval_Type()
)
agentSwitchCpuProcessRisingThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessRisingThresholdInterval.setStatus("current")


class _AgentSwitchCpuProcessFallingThreshold_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessFallingThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentSwitchCpuProcessFallingThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessFallingThreshold_Object = MibScalar
agentSwitchCpuProcessFallingThreshold = _AgentSwitchCpuProcessFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 7),
    _AgentSwitchCpuProcessFallingThreshold_Type()
)
agentSwitchCpuProcessFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessFallingThreshold.setStatus("current")


class _AgentSwitchCpuProcessFallingThresholdInterval_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessFallingThresholdInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_AgentSwitchCpuProcessFallingThresholdInterval_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessFallingThresholdInterval_Object = MibScalar
agentSwitchCpuProcessFallingThresholdInterval = _AgentSwitchCpuProcessFallingThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 8),
    _AgentSwitchCpuProcessFallingThresholdInterval_Type()
)
agentSwitchCpuProcessFallingThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessFallingThresholdInterval.setStatus("current")


class _AgentSwitchCpuProcessFreeMemoryThreshold_Type(Unsigned32):
    """Custom type agentSwitchCpuProcessFreeMemoryThreshold based on Unsigned32"""
    defaultValue = 0


_AgentSwitchCpuProcessFreeMemoryThreshold_Type.__name__ = "Unsigned32"
_AgentSwitchCpuProcessFreeMemoryThreshold_Object = MibScalar
agentSwitchCpuProcessFreeMemoryThreshold = _AgentSwitchCpuProcessFreeMemoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 9),
    _AgentSwitchCpuProcessFreeMemoryThreshold_Type()
)
agentSwitchCpuProcessFreeMemoryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessFreeMemoryThreshold.setStatus("current")
_AgentSwitchCpuProcessTotalUtilization_Type = DisplayString
_AgentSwitchCpuProcessTotalUtilization_Object = MibScalar
agentSwitchCpuProcessTotalUtilization = _AgentSwitchCpuProcessTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 10),
    _AgentSwitchCpuProcessTotalUtilization_Type()
)
agentSwitchCpuProcessTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcessTotalUtilization.setStatus("current")
_AgentSwitchCpuProcess5SecUtilization_Type = Integer32
_AgentSwitchCpuProcess5SecUtilization_Object = MibScalar
agentSwitchCpuProcess5SecUtilization = _AgentSwitchCpuProcess5SecUtilization_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 11),
    _AgentSwitchCpuProcess5SecUtilization_Type()
)
agentSwitchCpuProcess5SecUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcess5SecUtilization.setStatus("current")
_AgentSwitchCpuProcess1minUtilization_Type = Integer32
_AgentSwitchCpuProcess1minUtilization_Object = MibScalar
agentSwitchCpuProcess1minUtilization = _AgentSwitchCpuProcess1minUtilization_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 12),
    _AgentSwitchCpuProcess1minUtilization_Type()
)
agentSwitchCpuProcess1minUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcess1minUtilization.setStatus("current")
_AgentSwitchCpuProcess5minUtilization_Type = Integer32
_AgentSwitchCpuProcess5minUtilization_Object = MibScalar
agentSwitchCpuProcess5minUtilization = _AgentSwitchCpuProcess5minUtilization_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 13),
    _AgentSwitchCpuProcess5minUtilization_Type()
)
agentSwitchCpuProcess5minUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcess5minUtilization.setStatus("current")
_AgentSwitchCpuProcess15minUtilization_Type = Integer32
_AgentSwitchCpuProcess15minUtilization_Object = MibScalar
agentSwitchCpuProcess15minUtilization = _AgentSwitchCpuProcess15minUtilization_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 14),
    _AgentSwitchCpuProcess15minUtilization_Type()
)
agentSwitchCpuProcess15minUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuProcess15minUtilization.setStatus("current")
_AgentSwitchCpuUtzPrecision_Type = AgentSwitchPrecision
_AgentSwitchCpuUtzPrecision_Object = MibScalar
agentSwitchCpuUtzPrecision = _AgentSwitchCpuUtzPrecision_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 15),
    _AgentSwitchCpuUtzPrecision_Type()
)
agentSwitchCpuUtzPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuUtzPrecision.setStatus("current")
_AgentSwitchCpuCores_Type = Integer32
_AgentSwitchCpuCores_Object = MibScalar
agentSwitchCpuCores = _AgentSwitchCpuCores_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 16),
    _AgentSwitchCpuCores_Type()
)
agentSwitchCpuCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuCores.setStatus("current")
_AgentSwitchCPUUtzErrorFlag_Type = AgentSwitchErrorFlag
_AgentSwitchCPUUtzErrorFlag_Object = MibScalar
agentSwitchCPUUtzErrorFlag = _AgentSwitchCPUUtzErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 100),
    _AgentSwitchCPUUtzErrorFlag_Type()
)
agentSwitchCPUUtzErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCPUUtzErrorFlag.setStatus("current")
_AgentSwitchCPUUtzErrorMsg_Type = DisplayString
_AgentSwitchCPUUtzErrorMsg_Object = MibScalar
agentSwitchCPUUtzErrorMsg = _AgentSwitchCPUUtzErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 101),
    _AgentSwitchCPUUtzErrorMsg_Type()
)
agentSwitchCPUUtzErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCPUUtzErrorMsg.setStatus("current")
_AgentSwitchMemErrorFlag_Type = AgentSwitchErrorFlag
_AgentSwitchMemErrorFlag_Object = MibScalar
agentSwitchMemErrorFlag = _AgentSwitchMemErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 102),
    _AgentSwitchMemErrorFlag_Type()
)
agentSwitchMemErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMemErrorFlag.setStatus("current")
_AgentSwitchMemErrorMsg_Type = DisplayString
_AgentSwitchMemErrorMsg_Object = MibScalar
agentSwitchMemErrorMsg = _AgentSwitchMemErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 1, 1, 103),
    _AgentSwitchMemErrorMsg_Type()
)
agentSwitchMemErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMemErrorMsg.setStatus("current")
_AgentSwitchNotifications_ObjectIdentity = ObjectIdentity
agentSwitchNotifications = _AgentSwitchNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 5, 2)
)
_AgentSwitchCpuutilizationStatus_Type = AgentSwitchSensorStatus
_AgentSwitchCpuutilizationStatus_Object = MibScalar
agentSwitchCpuutilizationStatus = _AgentSwitchCpuutilizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 2, 1),
    _AgentSwitchCpuutilizationStatus_Type()
)
agentSwitchCpuutilizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCpuutilizationStatus.setStatus("current")
_AgentSwitchMemStatus_Type = AgentSwitchSensorStatus
_AgentSwitchMemStatus_Object = MibScalar
agentSwitchMemStatus = _AgentSwitchMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 40310, 5, 2, 2),
    _AgentSwitchMemStatus_Type()
)
agentSwitchMemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMemStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-STATUS-MIB",
    **{"AgentSwitchSensorStatus": AgentSwitchSensorStatus,
       "AgentSwitchErrorFlag": AgentSwitchErrorFlag,
       "AgentSwitchPrecision": AgentSwitchPrecision,
       "cumulusSystemStatus": cumulusSystemStatus,
       "agentInfoGroup": agentInfoGroup,
       "agentSwitchCpuProcessGroup": agentSwitchCpuProcessGroup,
       "agentSwitchCpuProcessMemFree": agentSwitchCpuProcessMemFree,
       "agentSwitchCpuProcessMemAvailable": agentSwitchCpuProcessMemAvailable,
       "agentSwitchCpuProcessMemTotal": agentSwitchCpuProcessMemTotal,
       "agentSwitchCpuProcessMemPrecision": agentSwitchCpuProcessMemPrecision,
       "agentSwitchCpuProcessRisingThreshold": agentSwitchCpuProcessRisingThreshold,
       "agentSwitchCpuProcessRisingThresholdInterval": agentSwitchCpuProcessRisingThresholdInterval,
       "agentSwitchCpuProcessFallingThreshold": agentSwitchCpuProcessFallingThreshold,
       "agentSwitchCpuProcessFallingThresholdInterval": agentSwitchCpuProcessFallingThresholdInterval,
       "agentSwitchCpuProcessFreeMemoryThreshold": agentSwitchCpuProcessFreeMemoryThreshold,
       "agentSwitchCpuProcessTotalUtilization": agentSwitchCpuProcessTotalUtilization,
       "agentSwitchCpuProcess5SecUtilization": agentSwitchCpuProcess5SecUtilization,
       "agentSwitchCpuProcess1minUtilization": agentSwitchCpuProcess1minUtilization,
       "agentSwitchCpuProcess5minUtilization": agentSwitchCpuProcess5minUtilization,
       "agentSwitchCpuProcess15minUtilization": agentSwitchCpuProcess15minUtilization,
       "agentSwitchCpuUtzPrecision": agentSwitchCpuUtzPrecision,
       "agentSwitchCpuCores": agentSwitchCpuCores,
       "agentSwitchCPUUtzErrorFlag": agentSwitchCPUUtzErrorFlag,
       "agentSwitchCPUUtzErrorMsg": agentSwitchCPUUtzErrorMsg,
       "agentSwitchMemErrorFlag": agentSwitchMemErrorFlag,
       "agentSwitchMemErrorMsg": agentSwitchMemErrorMsg,
       "agentSwitchNotifications": agentSwitchNotifications,
       "agentSwitchCpuutilizationStatus": agentSwitchCpuutilizationStatus,
       "agentSwitchMemStatus": agentSwitchMemStatus}
)
