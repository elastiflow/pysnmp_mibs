# SNMP MIB module (FSP1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FSP1000-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(PhysicalIndex,
 entPhysicalClass,
 entPhysicalContainedIn,
 entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName,
 entPhysicalParentRelPos,
 entPhysicalVendorType) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalClass",
    "entPhysicalContainedIn",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName",
    "entPhysicalParentRelPos",
    "entPhysicalVendorType")

(InterfaceIndex,
 ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry",
    "ifIndex")

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
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

fsp1000MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceAlarmTypes(TextualConvention, Integer32):
    status = "current"
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
        *(("lossOfSignal", 1),
          ("lossOfFrame", 2),
          ("lossOfClock", 3),
          ("errorRateFail", 4))
    )



class EquipmentAlarmTypes(TextualConvention, Integer32):
    status = "current"
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
        *(("fanFail", 1),
          ("powerFail", 2),
          ("tempTooHigh", 3),
          ("tempTooLow", 4))
    )



class TrapAlarmSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("warning", 5),
          ("cleared", 6))
    )



class PortModeCommand(TextualConvention, Integer32):
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
        *(("fibreAPrimary", 1),
          ("fibreBPrimary", 2),
          ("auto", 3))
    )



class PortMode(TextualConvention, Integer32):
    status = "current"
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
        *(("isPrimary", 1),
          ("isSecondary", 2),
          ("isNotConfigured", 3),
          ("isNotAvailable", 4))
    )



class OnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class AvailState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )



class ContainerState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("containerEmpty", 1),
          ("containsAcceptedUnit", 2))
    )



class ContainsPhysicalIndex(PhysicalIndex):
    status = "current"


class DataRate(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mb10", 2),
          ("mb34", 3),
          ("mb43", 4),
          ("mb100", 5),
          ("mb125", 6),
          ("mb143", 7),
          ("mb155", 8),
          ("mb177", 9),
          ("mb200", 10),
          ("mb266", 11),
          ("mb270", 12),
          ("mb360", 13),
          ("mb640", 14),
          ("mb622", 15),
          ("mb1062", 16),
          ("mb1250", 17),
          ("mb1485", 18),
          ("mb2488", 19))
    )



class ClockRate(TextualConvention, Integer32):
    status = "current"
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
        *(("powerDown", 1),
          ("xclk6", 2),
          ("xclk4", 3),
          ("xclk2", 4))
    )



class LineProtectionIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class ChannelList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class ServiceList(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noService", 1),
          ("ethernet", 2),
          ("gigabit", 3),
          ("fibreChannel", 4),
          ("escon", 5),
          ("oc3stm1", 6),
          ("oc12stm4", 7),
          ("e3", 8),
          ("t3", 9),
          ("video", 10),
          ("oc48stm16", 11),
          ("atm", 12),
          ("reserved", 255))
    )



class NodeType(TextualConvention, Integer32):
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
        *(("fsp1000", 1),
          ("sgm", 2),
          ("mct", 3))
    )



class PortConnectorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mu", 1),
          ("sc", 2),
          ("st", 3),
          ("fc", 4),
          ("rj", 5))
    )



class LoopbackState(TextualConvention, Integer32):
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
        *(("near", 1),
          ("far", 2),
          ("off", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Adva_ObjectIdentity = ObjectIdentity
adva = _Adva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_Fsp1000_ObjectIdentity = ObjectIdentity
fsp1000 = _Fsp1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6)
)
_Fsp1000Products_ObjectIdentity = ObjectIdentity
fsp1000Products = _Fsp1000Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 1)
)
_Fsp1000V1_ObjectIdentity = ObjectIdentity
fsp1000V1 = _Fsp1000V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fsp1000V1.setStatus("current")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1)
)
_AlarmFilters_ObjectIdentity = ObjectIdentity
alarmFilters = _AlarmFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1)
)
_InterfaceAlarmFilterTable_Object = MibTable
interfaceAlarmFilterTable = _InterfaceAlarmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceAlarmFilterTable.setStatus("current")
_InterfaceAlarmFilterEntry_Object = MibTableRow
interfaceAlarmFilterEntry = _InterfaceAlarmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 1, 1)
)
interfaceAlarmFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP1000-MIB", "interfaceAlarmFilterType"),
)
if mibBuilder.loadTexts:
    interfaceAlarmFilterEntry.setStatus("current")
_InterfaceAlarmFilterType_Type = InterfaceAlarmTypes
_InterfaceAlarmFilterType_Object = MibTableColumn
interfaceAlarmFilterType = _InterfaceAlarmFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 1, 1, 1),
    _InterfaceAlarmFilterType_Type()
)
interfaceAlarmFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceAlarmFilterType.setStatus("current")
_InterfaceAlarmFilterState_Type = OnOff
_InterfaceAlarmFilterState_Object = MibTableColumn
interfaceAlarmFilterState = _InterfaceAlarmFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 1, 1, 2),
    _InterfaceAlarmFilterState_Type()
)
interfaceAlarmFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceAlarmFilterState.setStatus("current")
_EquipmentAlarmFilterTable_Object = MibTable
equipmentAlarmFilterTable = _EquipmentAlarmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    equipmentAlarmFilterTable.setStatus("current")
_EquipmentAlarmFilterEntry_Object = MibTableRow
equipmentAlarmFilterEntry = _EquipmentAlarmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 2, 1)
)
equipmentAlarmFilterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP1000-MIB", "equipmentAlarmFilterType"),
)
if mibBuilder.loadTexts:
    equipmentAlarmFilterEntry.setStatus("current")
_EquipmentAlarmFilterType_Type = EquipmentAlarmTypes
_EquipmentAlarmFilterType_Object = MibTableColumn
equipmentAlarmFilterType = _EquipmentAlarmFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 2, 1, 1),
    _EquipmentAlarmFilterType_Type()
)
equipmentAlarmFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentAlarmFilterType.setStatus("current")
_EquipmentAlarmFilterState_Type = OnOff
_EquipmentAlarmFilterState_Object = MibTableColumn
equipmentAlarmFilterState = _EquipmentAlarmFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 1, 2, 1, 2),
    _EquipmentAlarmFilterState_Type()
)
equipmentAlarmFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentAlarmFilterState.setStatus("current")
_CurrentAlarms_ObjectIdentity = ObjectIdentity
currentAlarms = _CurrentAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2)
)
_InterfaceCurrentAlarmTable_Object = MibTable
interfaceCurrentAlarmTable = _InterfaceCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceCurrentAlarmTable.setStatus("current")
_InterfaceCurrentAlarmEntry_Object = MibTableRow
interfaceCurrentAlarmEntry = _InterfaceCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 1, 1)
)
interfaceCurrentAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FSP1000-MIB", "interfaceCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    interfaceCurrentAlarmEntry.setStatus("current")
_InterfaceCurrentAlarmType_Type = InterfaceAlarmTypes
_InterfaceCurrentAlarmType_Object = MibTableColumn
interfaceCurrentAlarmType = _InterfaceCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 1, 1, 1),
    _InterfaceCurrentAlarmType_Type()
)
interfaceCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceCurrentAlarmType.setStatus("current")
_InterfaceCurrentAlarmSeverity_Type = TrapAlarmSeverity
_InterfaceCurrentAlarmSeverity_Object = MibTableColumn
interfaceCurrentAlarmSeverity = _InterfaceCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 1, 1, 2),
    _InterfaceCurrentAlarmSeverity_Type()
)
interfaceCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCurrentAlarmSeverity.setStatus("current")
_EquipmentCurrentAlarmTable_Object = MibTable
equipmentCurrentAlarmTable = _EquipmentCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    equipmentCurrentAlarmTable.setStatus("current")
_EquipmentCurrentAlarmEntry_Object = MibTableRow
equipmentCurrentAlarmEntry = _EquipmentCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 2, 1)
)
equipmentCurrentAlarmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "FSP1000-MIB", "equipmentCurrentAlarmType"),
)
if mibBuilder.loadTexts:
    equipmentCurrentAlarmEntry.setStatus("current")
_EquipmentCurrentAlarmType_Type = EquipmentAlarmTypes
_EquipmentCurrentAlarmType_Object = MibTableColumn
equipmentCurrentAlarmType = _EquipmentCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 2, 1, 1),
    _EquipmentCurrentAlarmType_Type()
)
equipmentCurrentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    equipmentCurrentAlarmType.setStatus("current")
_EquipmentCurrentAlarmSeverity_Type = TrapAlarmSeverity
_EquipmentCurrentAlarmSeverity_Object = MibTableColumn
equipmentCurrentAlarmSeverity = _EquipmentCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 1, 2, 2, 1, 2),
    _EquipmentCurrentAlarmSeverity_Type()
)
equipmentCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentCurrentAlarmSeverity.setStatus("current")
_AdminMIB_ObjectIdentity = ObjectIdentity
adminMIB = _AdminMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2)
)


class _NeType_Type(Integer32):
    """Custom type neType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("fsp1000", 1)
    )


_NeType_Type.__name__ = "Integer32"
_NeType_Object = MibScalar
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 1),
    _NeType_Type()
)
neType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neType.setStatus("current")


class _NeMibVariant_Type(Integer32):
    """Custom type neMibVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_NeMibVariant_Type.__name__ = "Integer32"
_NeMibVariant_Object = MibScalar
neMibVariant = _NeMibVariant_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 2),
    _NeMibVariant_Type()
)
neMibVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMibVariant.setStatus("current")
_NeTrapsinkTable_Object = MibTable
neTrapsinkTable = _NeTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    neTrapsinkTable.setStatus("current")
_NeTrapsinkEntry_Object = MibTableRow
neTrapsinkEntry = _NeTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1)
)
neTrapsinkEntry.setIndexNames(
    (0, "FSP1000-MIB", "neTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    neTrapsinkEntry.setStatus("current")


class _NeTrapsinkNumber_Type(Integer32):
    """Custom type neTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NeTrapsinkNumber_Type.__name__ = "Integer32"
_NeTrapsinkNumber_Object = MibTableColumn
neTrapsinkNumber = _NeTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1, 1),
    _NeTrapsinkNumber_Type()
)
neTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkNumber.setStatus("current")
_NeTrapsinkAddress_Type = DisplayString
_NeTrapsinkAddress_Object = MibTableColumn
neTrapsinkAddress = _NeTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1, 2),
    _NeTrapsinkAddress_Type()
)
neTrapsinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkAddress.setStatus("current")
_NeTrapsinkDescription_Type = DisplayString
_NeTrapsinkDescription_Object = MibTableColumn
neTrapsinkDescription = _NeTrapsinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1, 3),
    _NeTrapsinkDescription_Type()
)
neTrapsinkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkDescription.setStatus("current")
_NeTrapsinkCommunity_Type = DisplayString
_NeTrapsinkCommunity_Object = MibTableColumn
neTrapsinkCommunity = _NeTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1, 4),
    _NeTrapsinkCommunity_Type()
)
neTrapsinkCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkCommunity.setStatus("current")


class _NeTrapsinkPriority_Type(Integer32):
    """Custom type neTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NeTrapsinkPriority_Type.__name__ = "Integer32"
_NeTrapsinkPriority_Object = MibTableColumn
neTrapsinkPriority = _NeTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1, 5),
    _NeTrapsinkPriority_Type()
)
neTrapsinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkPriority.setStatus("current")


class _NeTrapsinkPort_Type(Integer32):
    """Custom type neTrapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NeTrapsinkPort_Type.__name__ = "Integer32"
_NeTrapsinkPort_Object = MibTableColumn
neTrapsinkPort = _NeTrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 3, 1, 6),
    _NeTrapsinkPort_Type()
)
neTrapsinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neTrapsinkPort.setStatus("current")
_NeNumberOfEvents_Type = Counter32
_NeNumberOfEvents_Object = MibScalar
neNumberOfEvents = _NeNumberOfEvents_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 5),
    _NeNumberOfEvents_Type()
)
neNumberOfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNumberOfEvents.setStatus("current")
_NeManufacturer_Type = DisplayString
_NeManufacturer_Object = MibScalar
neManufacturer = _NeManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 7),
    _NeManufacturer_Type()
)
neManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neManufacturer.setStatus("current")


class _DetectedTopologyType_Type(Integer32):
    """Custom type detectedTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectedToFsp1000", 1),
          ("connectedToFsp3000", 2))
    )


_DetectedTopologyType_Type.__name__ = "Integer32"
_DetectedTopologyType_Object = MibScalar
detectedTopologyType = _DetectedTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 9),
    _DetectedTopologyType_Type()
)
detectedTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detectedTopologyType.setStatus("current")
_TopologyTable_Object = MibTable
topologyTable = _TopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 10)
)
if mibBuilder.loadTexts:
    topologyTable.setStatus("current")
_TopologyEntry_Object = MibTableRow
topologyEntry = _TopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 10, 1)
)
topologyEntry.setIndexNames(
    (0, "FSP1000-MIB", "topologyIndex"),
)
if mibBuilder.loadTexts:
    topologyEntry.setStatus("current")


class _TopologyIndex_Type(Integer32):
    """Custom type topologyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TopologyIndex_Type.__name__ = "Integer32"
_TopologyIndex_Object = MibTableColumn
topologyIndex = _TopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 10, 1, 1),
    _TopologyIndex_Type()
)
topologyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyIndex.setStatus("current")
_NodeIpAddress_Type = IpAddress
_NodeIpAddress_Object = MibTableColumn
nodeIpAddress = _NodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 10, 1, 2),
    _NodeIpAddress_Type()
)
nodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIpAddress.setStatus("current")
_NodeType_Type = NodeType
_NodeType_Object = MibTableColumn
nodeType = _NodeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 2, 10, 1, 3),
    _NodeType_Type()
)
nodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeType.setStatus("current")
_TrapMIB_ObjectIdentity = ObjectIdentity
trapMIB = _TrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3)
)
_TrapVariables_ObjectIdentity = ObjectIdentity
trapVariables = _TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 1)
)
_ContainerState_Type = ContainerState
_ContainerState_Object = MibScalar
containerState = _ContainerState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 1, 1),
    _ContainerState_Type()
)
containerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    containerState.setStatus("current")
_ContainsPhysicalIndex_Type = ContainsPhysicalIndex
_ContainsPhysicalIndex_Object = MibScalar
containsPhysicalIndex = _ContainsPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 1, 2),
    _ContainsPhysicalIndex_Type()
)
containsPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    containsPhysicalIndex.setStatus("current")
_ConfigurationMIB_ObjectIdentity = ObjectIdentity
configurationMIB = _ConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4)
)
_InterfaceConfiguration_ObjectIdentity = ObjectIdentity
interfaceConfiguration = _InterfaceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1)
)
_InterfaceTrailTerminationTable_Object = MibTable
interfaceTrailTerminationTable = _InterfaceTrailTerminationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceTrailTerminationTable.setStatus("current")
_InterfaceTrailTerminationEntry_Object = MibTableRow
interfaceTrailTerminationEntry = _InterfaceTrailTerminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1)
)
interfaceTrailTerminationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceTrailTerminationEntry.setStatus("current")


class _InterfaceTrailTerminationIdentifier_Type(DisplayString):
    """Custom type interfaceTrailTerminationIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_InterfaceTrailTerminationIdentifier_Type.__name__ = "DisplayString"
_InterfaceTrailTerminationIdentifier_Object = MibTableColumn
interfaceTrailTerminationIdentifier = _InterfaceTrailTerminationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 1),
    _InterfaceTrailTerminationIdentifier_Type()
)
interfaceTrailTerminationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationIdentifier.setStatus("current")
_InterfaceTrailTerminationLoopbackState_Type = LoopbackState
_InterfaceTrailTerminationLoopbackState_Object = MibTableColumn
interfaceTrailTerminationLoopbackState = _InterfaceTrailTerminationLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 2),
    _InterfaceTrailTerminationLoopbackState_Type()
)
interfaceTrailTerminationLoopbackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLoopbackState.setStatus("current")


class _InterfaceTrailTerminationLaserTxState_Type(Integer32):
    """Custom type interfaceTrailTerminationLaserTxState based on Integer32"""
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
          ("alwaysOn", 3))
    )


_InterfaceTrailTerminationLaserTxState_Type.__name__ = "Integer32"
_InterfaceTrailTerminationLaserTxState_Object = MibTableColumn
interfaceTrailTerminationLaserTxState = _InterfaceTrailTerminationLaserTxState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 3),
    _InterfaceTrailTerminationLaserTxState_Type()
)
interfaceTrailTerminationLaserTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLaserTxState.setStatus("current")


class _InterfaceTrailTerminationLaserTxCurrent_Type(Integer32):
    """Custom type interfaceTrailTerminationLaserTxCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_InterfaceTrailTerminationLaserTxCurrent_Type.__name__ = "Integer32"
_InterfaceTrailTerminationLaserTxCurrent_Object = MibTableColumn
interfaceTrailTerminationLaserTxCurrent = _InterfaceTrailTerminationLaserTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 4),
    _InterfaceTrailTerminationLaserTxCurrent_Type()
)
interfaceTrailTerminationLaserTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationLaserTxCurrent.setStatus("current")
_InterfaceTrailTerminationDataRate_Type = DataRate
_InterfaceTrailTerminationDataRate_Object = MibTableColumn
interfaceTrailTerminationDataRate = _InterfaceTrailTerminationDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 5),
    _InterfaceTrailTerminationDataRate_Type()
)
interfaceTrailTerminationDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationDataRate.setStatus("current")
_InterfaceTrailTerminationRxClockRate_Type = ClockRate
_InterfaceTrailTerminationRxClockRate_Object = MibTableColumn
interfaceTrailTerminationRxClockRate = _InterfaceTrailTerminationRxClockRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 6),
    _InterfaceTrailTerminationRxClockRate_Type()
)
interfaceTrailTerminationRxClockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationRxClockRate.setStatus("current")


class _InterfaceTrailTerminationWavelength_Type(DisplayString):
    """Custom type interfaceTrailTerminationWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_InterfaceTrailTerminationWavelength_Type.__name__ = "DisplayString"
_InterfaceTrailTerminationWavelength_Object = MibTableColumn
interfaceTrailTerminationWavelength = _InterfaceTrailTerminationWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 7),
    _InterfaceTrailTerminationWavelength_Type()
)
interfaceTrailTerminationWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationWavelength.setStatus("current")
_InterfaceTrailTerminationAutoShutdown_Type = OnOff
_InterfaceTrailTerminationAutoShutdown_Object = MibTableColumn
interfaceTrailTerminationAutoShutdown = _InterfaceTrailTerminationAutoShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 8),
    _InterfaceTrailTerminationAutoShutdown_Type()
)
interfaceTrailTerminationAutoShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationAutoShutdown.setStatus("current")


class _InterfaceTrailTerminationTxLambdaId_Type(DisplayString):
    """Custom type interfaceTrailTerminationTxLambdaId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_InterfaceTrailTerminationTxLambdaId_Type.__name__ = "DisplayString"
_InterfaceTrailTerminationTxLambdaId_Object = MibTableColumn
interfaceTrailTerminationTxLambdaId = _InterfaceTrailTerminationTxLambdaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 9),
    _InterfaceTrailTerminationTxLambdaId_Type()
)
interfaceTrailTerminationTxLambdaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationTxLambdaId.setStatus("current")


class _InterfaceTrailTerminationRxLambdaId_Type(DisplayString):
    """Custom type interfaceTrailTerminationRxLambdaId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_InterfaceTrailTerminationRxLambdaId_Type.__name__ = "DisplayString"
_InterfaceTrailTerminationRxLambdaId_Object = MibTableColumn
interfaceTrailTerminationRxLambdaId = _InterfaceTrailTerminationRxLambdaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 1, 1, 1, 10),
    _InterfaceTrailTerminationRxLambdaId_Type()
)
interfaceTrailTerminationRxLambdaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTrailTerminationRxLambdaId.setStatus("current")
_EquipmentConfiguration_ObjectIdentity = ObjectIdentity
equipmentConfiguration = _EquipmentConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2)
)
_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 1, 1)
)
chassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("current")


class _ChassisEnvironmentTemp_Type(Integer32):
    """Custom type chassisEnvironmentTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_ChassisEnvironmentTemp_Type.__name__ = "Integer32"
_ChassisEnvironmentTemp_Object = MibTableColumn
chassisEnvironmentTemp = _ChassisEnvironmentTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 1, 1, 1),
    _ChassisEnvironmentTemp_Type()
)
chassisEnvironmentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisEnvironmentTemp.setStatus("current")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 2, 1)
)
moduleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleCardType_Type(Integer32):
    """Custom type moduleCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleCardType_Type.__name__ = "Integer32"
_ModuleCardType_Object = MibTableColumn
moduleCardType = _ModuleCardType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 2, 1, 1),
    _ModuleCardType_Type()
)
moduleCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCardType.setStatus("current")
_ModuleSidebandState_Type = OnOff
_ModuleSidebandState_Object = MibTableColumn
moduleSidebandState = _ModuleSidebandState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 2, 1, 2),
    _ModuleSidebandState_Type()
)
moduleSidebandState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSidebandState.setStatus("current")
_ModulePortConnectorType_Type = PortConnectorType
_ModulePortConnectorType_Object = MibTableColumn
modulePortConnectorType = _ModulePortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 2, 2, 1, 3),
    _ModulePortConnectorType_Type()
)
modulePortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePortConnectorType.setStatus("current")
_LineProtection_ObjectIdentity = ObjectIdentity
lineProtection = _LineProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3)
)
_LineProtectionTable_Object = MibTable
lineProtectionTable = _LineProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lineProtectionTable.setStatus("current")
_LineProtectionEntry_Object = MibTableRow
lineProtectionEntry = _LineProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1)
)
lineProtectionEntry.setIndexNames(
    (0, "FSP1000-MIB", "LineProtectionIndex"),
)
if mibBuilder.loadTexts:
    lineProtectionEntry.setStatus("current")
_LineSwitchLineAInterfaceIndex_Type = PhysicalIndex
_LineSwitchLineAInterfaceIndex_Object = MibTableColumn
lineSwitchLineAInterfaceIndex = _LineSwitchLineAInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1, 1),
    _LineSwitchLineAInterfaceIndex_Type()
)
lineSwitchLineAInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSwitchLineAInterfaceIndex.setStatus("current")
_LineSwitchLineBInterfaceIndex_Type = PhysicalIndex
_LineSwitchLineBInterfaceIndex_Object = MibTableColumn
lineSwitchLineBInterfaceIndex = _LineSwitchLineBInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1, 2),
    _LineSwitchLineBInterfaceIndex_Type()
)
lineSwitchLineBInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSwitchLineBInterfaceIndex.setStatus("current")
_LineSwitchLineAState_Type = PortMode
_LineSwitchLineAState_Object = MibTableColumn
lineSwitchLineAState = _LineSwitchLineAState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1, 3),
    _LineSwitchLineAState_Type()
)
lineSwitchLineAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSwitchLineAState.setStatus("current")
_LineSwitchLineBState_Type = PortMode
_LineSwitchLineBState_Object = MibTableColumn
lineSwitchLineBState = _LineSwitchLineBState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1, 4),
    _LineSwitchLineBState_Type()
)
lineSwitchLineBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSwitchLineBState.setStatus("current")
_LineSwitchLineMode_Type = PortModeCommand
_LineSwitchLineMode_Object = MibTableColumn
lineSwitchLineMode = _LineSwitchLineMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1, 5),
    _LineSwitchLineMode_Type()
)
lineSwitchLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSwitchLineMode.setStatus("current")
_LineSwitchLineModeLastRequest_Type = PortModeCommand
_LineSwitchLineModeLastRequest_Object = MibTableColumn
lineSwitchLineModeLastRequest = _LineSwitchLineModeLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 3, 1, 1, 6),
    _LineSwitchLineModeLastRequest_Type()
)
lineSwitchLineModeLastRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSwitchLineModeLastRequest.setStatus("current")
_ChannelAllocation_ObjectIdentity = ObjectIdentity
channelAllocation = _ChannelAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4)
)


class _ChannelBandwidthAvail_Type(Integer32):
    """Custom type channelBandwidthAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ChannelBandwidthAvail_Type.__name__ = "Integer32"
_ChannelBandwidthAvail_Object = MibScalar
channelBandwidthAvail = _ChannelBandwidthAvail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 1),
    _ChannelBandwidthAvail_Type()
)
channelBandwidthAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidthAvail.setStatus("current")
_ChannelMapTable_Object = MibTable
channelMapTable = _ChannelMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    channelMapTable.setStatus("current")
_ChannelMapEntry_Object = MibTableRow
channelMapEntry = _ChannelMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 2, 1)
)
channelMapEntry.setIndexNames(
    (0, "FSP1000-MIB", "systemChannel"),
)
if mibBuilder.loadTexts:
    channelMapEntry.setStatus("current")


class _SystemChannel_Type(Integer32):
    """Custom type systemChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SystemChannel_Type.__name__ = "Integer32"
_SystemChannel_Object = MibTableColumn
systemChannel = _SystemChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 2, 1, 1),
    _SystemChannel_Type()
)
systemChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChannel.setStatus("current")
_BundleLocalUserPort_Type = InterfaceIndex
_BundleLocalUserPort_Object = MibTableColumn
bundleLocalUserPort = _BundleLocalUserPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 2, 1, 1),
    _BundleLocalUserPort_Type()
)
bundleLocalUserPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleLocalUserPort.setStatus("current")


class _ChannelState_Type(Integer32):
    """Custom type channelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("allocated", 2),
          ("reserved", 3))
    )


_ChannelState_Type.__name__ = "Integer32"
_ChannelState_Object = MibTableColumn
channelState = _ChannelState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 2, 1, 2),
    _ChannelState_Type()
)
channelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelState.setStatus("current")
_UserPort_Type = InterfaceIndex
_UserPort_Object = MibTableColumn
userPort = _UserPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 4, 2, 1, 3),
    _UserPort_Type()
)
userPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPort.setStatus("current")
_BundleAllocation_ObjectIdentity = ObjectIdentity
bundleAllocation = _BundleAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5)
)
_BundleAllocationTable_Object = MibTable
bundleAllocationTable = _BundleAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    bundleAllocationTable.setStatus("current")
_BundleAllocationEntry_Object = MibTableRow
bundleAllocationEntry = _BundleAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1, 1)
)
bundleAllocationEntry.setIndexNames(
    (0, "FSP1000-MIB", "bundleLocalUserPort"),
)
if mibBuilder.loadTexts:
    bundleAllocationEntry.setStatus("current")
_BundleService_Type = ServiceList
_BundleService_Object = MibTableColumn
bundleService = _BundleService_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1, 1, 2),
    _BundleService_Type()
)
bundleService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleService.setStatus("current")
_BundleDataRate_Type = DataRate
_BundleDataRate_Object = MibTableColumn
bundleDataRate = _BundleDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1, 1, 3),
    _BundleDataRate_Type()
)
bundleDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleDataRate.setStatus("current")


class _BundleRemoteUserPort_Type(Integer32):
    """Custom type bundleRemoteUserPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BundleRemoteUserPort_Type.__name__ = "Integer32"
_BundleRemoteUserPort_Object = MibTableColumn
bundleRemoteUserPort = _BundleRemoteUserPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1, 1, 4),
    _BundleRemoteUserPort_Type()
)
bundleRemoteUserPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleRemoteUserPort.setStatus("current")


class _BundleDescription_Type(DisplayString):
    """Custom type bundleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BundleDescription_Type.__name__ = "DisplayString"
_BundleDescription_Object = MibTableColumn
bundleDescription = _BundleDescription_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1, 1, 5),
    _BundleDescription_Type()
)
bundleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleDescription.setStatus("current")


class _BundleStatus_Type(Integer32):
    """Custom type bundleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("allocated", 2),
          ("reserved", 3))
    )


_BundleStatus_Type.__name__ = "Integer32"
_BundleStatus_Object = MibTableColumn
bundleStatus = _BundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 1, 1, 6),
    _BundleStatus_Type()
)
bundleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleStatus.setStatus("current")
_BundleAllocationRequest_Type = InterfaceIndex
_BundleAllocationRequest_Object = MibScalar
bundleAllocationRequest = _BundleAllocationRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 4, 5, 3),
    _BundleAllocationRequest_Type()
)
bundleAllocationRequest.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bundleAllocationRequest.setStatus("current")
_PerformanceMIB_ObjectIdentity = ObjectIdentity
performanceMIB = _PerformanceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5)
)
_PerformanceAdmin_ObjectIdentity = ObjectIdentity
performanceAdmin = _PerformanceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 1)
)
_InterfaceBertAdminTable_Object = MibTable
interfaceBertAdminTable = _InterfaceBertAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceBertAdminTable.setStatus("current")
_InterfaceBertAdminEntry_Object = MibTableRow
interfaceBertAdminEntry = _InterfaceBertAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 1, 1, 1)
)
interfaceBertAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceBertAdminEntry.setStatus("current")
_InterfaceErrorRateLimit_Type = Integer32
_InterfaceErrorRateLimit_Object = MibTableColumn
interfaceErrorRateLimit = _InterfaceErrorRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 1, 1, 1, 1),
    _InterfaceErrorRateLimit_Type()
)
interfaceErrorRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceErrorRateLimit.setStatus("current")
_PerformanceMonitoring_ObjectIdentity = ObjectIdentity
performanceMonitoring = _PerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2)
)
_InterfaceBertTable_Object = MibTable
interfaceBertTable = _InterfaceBertTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceBertTable.setStatus("current")
_InterfaceBertEntry_Object = MibTableRow
interfaceBertEntry = _InterfaceBertEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1)
)
interfaceBertEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceBertEntry.setStatus("current")
_InterfaceCorrectableErrors_Type = Integer32
_InterfaceCorrectableErrors_Object = MibTableColumn
interfaceCorrectableErrors = _InterfaceCorrectableErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 1),
    _InterfaceCorrectableErrors_Type()
)
interfaceCorrectableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCorrectableErrors.setStatus("current")
_InterfaceCorrectableErrorRate_Type = Integer32
_InterfaceCorrectableErrorRate_Object = MibTableColumn
interfaceCorrectableErrorRate = _InterfaceCorrectableErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 2),
    _InterfaceCorrectableErrorRate_Type()
)
interfaceCorrectableErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCorrectableErrorRate.setStatus("current")
_InterfaceUncorrectableErrors_Type = Integer32
_InterfaceUncorrectableErrors_Object = MibTableColumn
interfaceUncorrectableErrors = _InterfaceUncorrectableErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 3),
    _InterfaceUncorrectableErrors_Type()
)
interfaceUncorrectableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceUncorrectableErrors.setStatus("current")
_InterfaceUncorrectableErrorRate_Type = Integer32
_InterfaceUncorrectableErrorRate_Object = MibTableColumn
interfaceUncorrectableErrorRate = _InterfaceUncorrectableErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 4),
    _InterfaceUncorrectableErrorRate_Type()
)
interfaceUncorrectableErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceUncorrectableErrorRate.setStatus("current")
_InterfaceGoodFrames_Type = Integer32
_InterfaceGoodFrames_Object = MibTableColumn
interfaceGoodFrames = _InterfaceGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 5),
    _InterfaceGoodFrames_Type()
)
interfaceGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceGoodFrames.setStatus("current")
_InterfaceGoodFrameRate_Type = Integer32
_InterfaceGoodFrameRate_Object = MibTableColumn
interfaceGoodFrameRate = _InterfaceGoodFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 6),
    _InterfaceGoodFrameRate_Type()
)
interfaceGoodFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceGoodFrameRate.setStatus("current")
_InterfaceBadFrames_Type = Integer32
_InterfaceBadFrames_Object = MibTableColumn
interfaceBadFrames = _InterfaceBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 7),
    _InterfaceBadFrames_Type()
)
interfaceBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBadFrames.setStatus("current")
_InterfaceBadFrameRate_Type = Integer32
_InterfaceBadFrameRate_Object = MibTableColumn
interfaceBadFrameRate = _InterfaceBadFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 5, 2, 1, 1, 8),
    _InterfaceBadFrameRate_Type()
)
interfaceBadFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBadFrameRate.setStatus("current")

# Managed Objects groups


# Notification objects

containerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 4)
)
containerStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "containsPhysicalIndex"),
        ("FSP1000-MIB", "containerState"))
)
if mibBuilder.loadTexts:
    containerStateChange.setStatus(
        "current"
    )

neAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 6)
)
if mibBuilder.loadTexts:
    neAttributeValueChange.setStatus(
        "current"
    )

interfaceAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 7)
)
interfaceAttributeValueChange.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    interfaceAttributeValueChange.setStatus(
        "current"
    )

equipmentAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 8)
)
equipmentAttributeValueChange.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    equipmentAttributeValueChange.setStatus(
        "current"
    )

modeAttributeValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 9)
)
modeAttributeValueChange.setObjects(
    ("FSP1000-MIB", "LineProtectionIndex")
)
if mibBuilder.loadTexts:
    modeAttributeValueChange.setStatus(
        "current"
    )

interfaceAlarmLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 12)
)
interfaceAlarmLossOfSignal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfSignal.setStatus(
        "current"
    )

topologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 13)
)
if mibBuilder.loadTexts:
    topologyChanged.setStatus(
        "current"
    )

equipmentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 14)
)
equipmentStateChange.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    equipmentStateChange.setStatus(
        "current"
    )

bundleAllocationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 15)
)
bundleAllocationChanged.setObjects(
      *(("FSP1000-MIB", "bundleLocalUserPort"),
        ("FSP1000-MIB", "bundleService"),
        ("FSP1000-MIB", "bundleDataRate"),
        ("FSP1000-MIB", "bundleRemoteUserPort"),
        ("FSP1000-MIB", "bundleStatus"))
)
if mibBuilder.loadTexts:
    bundleAllocationChanged.setStatus(
        "current"
    )

equipmentAlarmFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 16)
)
equipmentAlarmFilterChanged.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentAlarmFilterType"),
        ("FSP1000-MIB", "equipmentAlarmFilterState"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFilterChanged.setStatus(
        "current"
    )

interfaceAlarmFilterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 17)
)
interfaceAlarmFilterChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceAlarmFilterType"),
        ("FSP1000-MIB", "interfaceAlarmFilterState"))
)
if mibBuilder.loadTexts:
    interfaceAlarmFilterChanged.setStatus(
        "current"
    )

lineProtectionRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 18)
)
if mibBuilder.loadTexts:
    lineProtectionRequest.setStatus(
        "current"
    )

interfaceAlarmNoLossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 501)
)
interfaceAlarmNoLossOfSignal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfSignal.setStatus(
        "current"
    )

equipmentAlarmFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 504)
)
equipmentAlarmFanFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmFanFail.setStatus(
        "current"
    )

equipmentAlarmNoFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 505)
)
equipmentAlarmNoFanFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoFanFail.setStatus(
        "current"
    )

equipmentAlarmTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 508)
)
equipmentAlarmTempTooHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempTooHigh.setStatus(
        "current"
    )

equipmentAlarmTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 510)
)
equipmentAlarmTempTooLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempTooLow.setStatus(
        "current"
    )

equipmentAlarmTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 511)
)
equipmentAlarmTempNormal.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmTempNormal.setStatus(
        "current"
    )

equipmentAlarmPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 520)
)
equipmentAlarmPowerFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmPowerFail.setStatus(
        "current"
    )

equipmentAlarmNoPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 521)
)
equipmentAlarmNoPowerFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmNoPowerFail.setStatus(
        "current"
    )

equipmentAlarmOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 522)
)
equipmentAlarmOverVoltage.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmOverVoltage.setStatus(
        "current"
    )

equipmentAlarmUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 523)
)
equipmentAlarmUnderVoltage.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmUnderVoltage.setStatus(
        "current"
    )

equipmentAlarmVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 524)
)
equipmentAlarmVoltageNormal.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("FSP1000-MIB", "equipmentCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    equipmentAlarmVoltageNormal.setStatus(
        "current"
    )

interfaceAlarmLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 553)
)
interfaceAlarmLossOfFrame.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfFrame.setStatus(
        "current"
    )

interfaceAlarmNoLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 554)
)
interfaceAlarmNoLossOfFrame.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfFrame.setStatus(
        "current"
    )

interfaceAlarmLossOfClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 555)
)
interfaceAlarmLossOfClock.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmLossOfClock.setStatus(
        "current"
    )

interfaceAlarmNoLossOfClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 556)
)
interfaceAlarmNoLossOfClock.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoLossOfClock.setStatus(
        "current"
    )

interfaceAlarmErrorRateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 557)
)
interfaceAlarmErrorRateFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmErrorRateFail.setStatus(
        "current"
    )

interfaceAlarmNoErrorRateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 558)
)
interfaceAlarmNoErrorRateFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoErrorRateFail.setStatus(
        "current"
    )

interfaceAlarmConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 559)
)
interfaceAlarmConfigurationError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmConfigurationError.setStatus(
        "current"
    )

interfaceAlarmConfigurationGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 560)
)
interfaceAlarmConfigurationGood.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmConfigurationGood.setStatus(
        "current"
    )

interfaceAlarmInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 561)
)
interfaceAlarmInternalError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmInternalError.setStatus(
        "current"
    )

interfaceAlarmNoInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 6, 2, 3, 562)
)
interfaceAlarmNoInternalError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FSP1000-MIB", "interfaceCurrentAlarmSeverity"))
)
if mibBuilder.loadTexts:
    interfaceAlarmNoInternalError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSP1000-MIB",
    **{"InterfaceAlarmTypes": InterfaceAlarmTypes,
       "EquipmentAlarmTypes": EquipmentAlarmTypes,
       "TrapAlarmSeverity": TrapAlarmSeverity,
       "PortModeCommand": PortModeCommand,
       "PortMode": PortMode,
       "OnOff": OnOff,
       "AvailState": AvailState,
       "ContainerState": ContainerState,
       "ContainsPhysicalIndex": ContainsPhysicalIndex,
       "DataRate": DataRate,
       "ClockRate": ClockRate,
       "LineProtectionIndex": LineProtectionIndex,
       "ChannelList": ChannelList,
       "ServiceList": ServiceList,
       "NodeType": NodeType,
       "PortConnectorType": PortConnectorType,
       "LoopbackState": LoopbackState,
       "adva": adva,
       "products": products,
       "fsp1000": fsp1000,
       "fsp1000Products": fsp1000Products,
       "fsp1000V1": fsp1000V1,
       "fsp1000MIB": fsp1000MIB,
       "alarmMIB": alarmMIB,
       "alarmFilters": alarmFilters,
       "interfaceAlarmFilterTable": interfaceAlarmFilterTable,
       "interfaceAlarmFilterEntry": interfaceAlarmFilterEntry,
       "interfaceAlarmFilterType": interfaceAlarmFilterType,
       "interfaceAlarmFilterState": interfaceAlarmFilterState,
       "equipmentAlarmFilterTable": equipmentAlarmFilterTable,
       "equipmentAlarmFilterEntry": equipmentAlarmFilterEntry,
       "equipmentAlarmFilterType": equipmentAlarmFilterType,
       "equipmentAlarmFilterState": equipmentAlarmFilterState,
       "currentAlarms": currentAlarms,
       "interfaceCurrentAlarmTable": interfaceCurrentAlarmTable,
       "interfaceCurrentAlarmEntry": interfaceCurrentAlarmEntry,
       "interfaceCurrentAlarmType": interfaceCurrentAlarmType,
       "interfaceCurrentAlarmSeverity": interfaceCurrentAlarmSeverity,
       "equipmentCurrentAlarmTable": equipmentCurrentAlarmTable,
       "equipmentCurrentAlarmEntry": equipmentCurrentAlarmEntry,
       "equipmentCurrentAlarmType": equipmentCurrentAlarmType,
       "equipmentCurrentAlarmSeverity": equipmentCurrentAlarmSeverity,
       "adminMIB": adminMIB,
       "neType": neType,
       "neMibVariant": neMibVariant,
       "neTrapsinkTable": neTrapsinkTable,
       "neTrapsinkEntry": neTrapsinkEntry,
       "neTrapsinkNumber": neTrapsinkNumber,
       "neTrapsinkAddress": neTrapsinkAddress,
       "neTrapsinkDescription": neTrapsinkDescription,
       "neTrapsinkCommunity": neTrapsinkCommunity,
       "neTrapsinkPriority": neTrapsinkPriority,
       "neTrapsinkPort": neTrapsinkPort,
       "neNumberOfEvents": neNumberOfEvents,
       "neManufacturer": neManufacturer,
       "detectedTopologyType": detectedTopologyType,
       "topologyTable": topologyTable,
       "topologyEntry": topologyEntry,
       "topologyIndex": topologyIndex,
       "nodeIpAddress": nodeIpAddress,
       "nodeType": nodeType,
       "trapMIB": trapMIB,
       "trapVariables": trapVariables,
       "containerState": containerState,
       "containsPhysicalIndex": containsPhysicalIndex,
       "containerStateChange": containerStateChange,
       "neAttributeValueChange": neAttributeValueChange,
       "interfaceAttributeValueChange": interfaceAttributeValueChange,
       "equipmentAttributeValueChange": equipmentAttributeValueChange,
       "modeAttributeValueChange": modeAttributeValueChange,
       "interfaceAlarmLossOfSignal": interfaceAlarmLossOfSignal,
       "topologyChanged": topologyChanged,
       "equipmentStateChange": equipmentStateChange,
       "bundleAllocationChanged": bundleAllocationChanged,
       "equipmentAlarmFilterChanged": equipmentAlarmFilterChanged,
       "interfaceAlarmFilterChanged": interfaceAlarmFilterChanged,
       "lineProtectionRequest": lineProtectionRequest,
       "interfaceAlarmNoLossOfSignal": interfaceAlarmNoLossOfSignal,
       "equipmentAlarmFanFail": equipmentAlarmFanFail,
       "equipmentAlarmNoFanFail": equipmentAlarmNoFanFail,
       "equipmentAlarmTempTooHigh": equipmentAlarmTempTooHigh,
       "equipmentAlarmTempTooLow": equipmentAlarmTempTooLow,
       "equipmentAlarmTempNormal": equipmentAlarmTempNormal,
       "equipmentAlarmPowerFail": equipmentAlarmPowerFail,
       "equipmentAlarmNoPowerFail": equipmentAlarmNoPowerFail,
       "equipmentAlarmOverVoltage": equipmentAlarmOverVoltage,
       "equipmentAlarmUnderVoltage": equipmentAlarmUnderVoltage,
       "equipmentAlarmVoltageNormal": equipmentAlarmVoltageNormal,
       "interfaceAlarmLossOfFrame": interfaceAlarmLossOfFrame,
       "interfaceAlarmNoLossOfFrame": interfaceAlarmNoLossOfFrame,
       "interfaceAlarmLossOfClock": interfaceAlarmLossOfClock,
       "interfaceAlarmNoLossOfClock": interfaceAlarmNoLossOfClock,
       "interfaceAlarmErrorRateFail": interfaceAlarmErrorRateFail,
       "interfaceAlarmNoErrorRateFail": interfaceAlarmNoErrorRateFail,
       "interfaceAlarmConfigurationError": interfaceAlarmConfigurationError,
       "interfaceAlarmConfigurationGood": interfaceAlarmConfigurationGood,
       "interfaceAlarmInternalError": interfaceAlarmInternalError,
       "interfaceAlarmNoInternalError": interfaceAlarmNoInternalError,
       "configurationMIB": configurationMIB,
       "interfaceConfiguration": interfaceConfiguration,
       "interfaceTrailTerminationTable": interfaceTrailTerminationTable,
       "interfaceTrailTerminationEntry": interfaceTrailTerminationEntry,
       "interfaceTrailTerminationIdentifier": interfaceTrailTerminationIdentifier,
       "interfaceTrailTerminationLoopbackState": interfaceTrailTerminationLoopbackState,
       "interfaceTrailTerminationLaserTxState": interfaceTrailTerminationLaserTxState,
       "interfaceTrailTerminationLaserTxCurrent": interfaceTrailTerminationLaserTxCurrent,
       "interfaceTrailTerminationDataRate": interfaceTrailTerminationDataRate,
       "interfaceTrailTerminationRxClockRate": interfaceTrailTerminationRxClockRate,
       "interfaceTrailTerminationWavelength": interfaceTrailTerminationWavelength,
       "interfaceTrailTerminationAutoShutdown": interfaceTrailTerminationAutoShutdown,
       "interfaceTrailTerminationTxLambdaId": interfaceTrailTerminationTxLambdaId,
       "interfaceTrailTerminationRxLambdaId": interfaceTrailTerminationRxLambdaId,
       "equipmentConfiguration": equipmentConfiguration,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisEnvironmentTemp": chassisEnvironmentTemp,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleCardType": moduleCardType,
       "moduleSidebandState": moduleSidebandState,
       "modulePortConnectorType": modulePortConnectorType,
       "lineProtection": lineProtection,
       "lineProtectionTable": lineProtectionTable,
       "lineProtectionEntry": lineProtectionEntry,
       "lineSwitchLineAInterfaceIndex": lineSwitchLineAInterfaceIndex,
       "lineSwitchLineBInterfaceIndex": lineSwitchLineBInterfaceIndex,
       "lineSwitchLineAState": lineSwitchLineAState,
       "lineSwitchLineBState": lineSwitchLineBState,
       "lineSwitchLineMode": lineSwitchLineMode,
       "lineSwitchLineModeLastRequest": lineSwitchLineModeLastRequest,
       "channelAllocation": channelAllocation,
       "channelBandwidthAvail": channelBandwidthAvail,
       "channelMapTable": channelMapTable,
       "channelMapEntry": channelMapEntry,
       "systemChannel": systemChannel,
       "bundleLocalUserPort": bundleLocalUserPort,
       "channelState": channelState,
       "userPort": userPort,
       "bundleAllocation": bundleAllocation,
       "bundleAllocationTable": bundleAllocationTable,
       "bundleAllocationEntry": bundleAllocationEntry,
       "bundleService": bundleService,
       "bundleDataRate": bundleDataRate,
       "bundleRemoteUserPort": bundleRemoteUserPort,
       "bundleDescription": bundleDescription,
       "bundleStatus": bundleStatus,
       "bundleAllocationRequest": bundleAllocationRequest,
       "performanceMIB": performanceMIB,
       "performanceAdmin": performanceAdmin,
       "interfaceBertAdminTable": interfaceBertAdminTable,
       "interfaceBertAdminEntry": interfaceBertAdminEntry,
       "interfaceErrorRateLimit": interfaceErrorRateLimit,
       "performanceMonitoring": performanceMonitoring,
       "interfaceBertTable": interfaceBertTable,
       "interfaceBertEntry": interfaceBertEntry,
       "interfaceCorrectableErrors": interfaceCorrectableErrors,
       "interfaceCorrectableErrorRate": interfaceCorrectableErrorRate,
       "interfaceUncorrectableErrors": interfaceUncorrectableErrors,
       "interfaceUncorrectableErrorRate": interfaceUncorrectableErrorRate,
       "interfaceGoodFrames": interfaceGoodFrames,
       "interfaceGoodFrameRate": interfaceGoodFrameRate,
       "interfaceBadFrames": interfaceBadFrames,
       "interfaceBadFrameRate": interfaceBadFrameRate}
)
