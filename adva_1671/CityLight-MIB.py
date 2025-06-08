# SNMP MIB module (CityLight-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_1671/CityLight-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:25:51 2025
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
 ObjectName,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso,
 private) = mibBuilder.importSymbols(
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
    "ObjectName",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "private")

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

_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Adva_ObjectIdentity = ObjectIdentity
adva = _Adva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671)
)
_CityLight_ObjectIdentity = ObjectIdentity
cityLight = _CityLight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2)
)
_CityLightSystem_ObjectIdentity = ObjectIdentity
cityLightSystem = _CityLightSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1)
)


class _CLIGHTSystemSerialNumber_Type(DisplayString):
    """Custom type cLIGHTSystemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CLIGHTSystemSerialNumber_Type.__name__ = "DisplayString"
_CLIGHTSystemSerialNumber_Object = MibScalar
cLIGHTSystemSerialNumber = _CLIGHTSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 1),
    _CLIGHTSystemSerialNumber_Type()
)
cLIGHTSystemSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIGHTSystemSerialNumber.setStatus("mandatory")
_CLIGHTSystemReset_Type = Integer32
_CLIGHTSystemReset_Object = MibScalar
cLIGHTSystemReset = _CLIGHTSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 2),
    _CLIGHTSystemReset_Type()
)
cLIGHTSystemReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cLIGHTSystemReset.setStatus("mandatory")


class _CLIGHTSystemHWVersion_Type(DisplayString):
    """Custom type cLIGHTSystemHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CLIGHTSystemHWVersion_Type.__name__ = "DisplayString"
_CLIGHTSystemHWVersion_Object = MibScalar
cLIGHTSystemHWVersion = _CLIGHTSystemHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 3),
    _CLIGHTSystemHWVersion_Type()
)
cLIGHTSystemHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIGHTSystemHWVersion.setStatus("mandatory")


class _CLIGHTSystemFWVersion_Type(DisplayString):
    """Custom type cLIGHTSystemFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CLIGHTSystemFWVersion_Type.__name__ = "DisplayString"
_CLIGHTSystemFWVersion_Object = MibScalar
cLIGHTSystemFWVersion = _CLIGHTSystemFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 4),
    _CLIGHTSystemFWVersion_Type()
)
cLIGHTSystemFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIGHTSystemFWVersion.setStatus("mandatory")


class _CLIGHTSystemConfiguration_Type(Integer32):
    """Custom type cLIGHTSystemConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sixteenSlotChassis", 1),
          ("onePlusOneChassis", 2),
          ("onePlusTwoChassis", 3))
    )


_CLIGHTSystemConfiguration_Type.__name__ = "Integer32"
_CLIGHTSystemConfiguration_Object = MibScalar
cLIGHTSystemConfiguration = _CLIGHTSystemConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 5),
    _CLIGHTSystemConfiguration_Type()
)
cLIGHTSystemConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIGHTSystemConfiguration.setStatus("mandatory")


class _CLIGHTSystemPSUState_Type(Integer32):
    """Custom type cLIGHTSystemPSUState based on Integer32"""
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
        *(("good", 1),
          ("primaryFailed", 2),
          ("secondaryFailed", 3),
          ("notFitted", 4))
    )


_CLIGHTSystemPSUState_Type.__name__ = "Integer32"
_CLIGHTSystemPSUState_Object = MibScalar
cLIGHTSystemPSUState = _CLIGHTSystemPSUState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 6),
    _CLIGHTSystemPSUState_Type()
)
cLIGHTSystemPSUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIGHTSystemPSUState.setStatus("mandatory")


class _CLIGHTSystemTemperature_Type(Integer32):
    """Custom type cLIGHTSystemTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("overTemperature", 2),
          ("underTemperature", 3))
    )


_CLIGHTSystemTemperature_Type.__name__ = "Integer32"
_CLIGHTSystemTemperature_Object = MibScalar
cLIGHTSystemTemperature = _CLIGHTSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 7),
    _CLIGHTSystemTemperature_Type()
)
cLIGHTSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIGHTSystemTemperature.setStatus("mandatory")


class _CLIGHTSystemFanState_Type(Integer32):
    """Custom type cLIGHTSystemFanState based on Integer32"""
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
        *(("good", 1),
          ("primaryFailed", 2),
          ("psu1FanFailed", 3),
          ("psu2FanFailed", 4),
          ("secondaryFailed", 5))
    )


_CLIGHTSystemFanState_Type.__name__ = "Integer32"
_CLIGHTSystemFanState_Object = MibScalar
cLIGHTSystemFanState = _CLIGHTSystemFanState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 8),
    _CLIGHTSystemFanState_Type()
)
cLIGHTSystemFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLIGHTSystemFanState.setStatus("mandatory")


class _CLIGHTSystemLocation_Type(DisplayString):
    """Custom type cLIGHTSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_CLIGHTSystemLocation_Type.__name__ = "DisplayString"
_CLIGHTSystemLocation_Object = MibScalar
cLIGHTSystemLocation = _CLIGHTSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 9),
    _CLIGHTSystemLocation_Type()
)
cLIGHTSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIGHTSystemLocation.setStatus("mandatory")


class _CLIGHTSystemLanSpeed_Type(Integer32):
    """Custom type cLIGHTSystemLanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ten", 1),
          ("hundred", 2))
    )


_CLIGHTSystemLanSpeed_Type.__name__ = "Integer32"
_CLIGHTSystemLanSpeed_Object = MibScalar
cLIGHTSystemLanSpeed = _CLIGHTSystemLanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 10),
    _CLIGHTSystemLanSpeed_Type()
)
cLIGHTSystemLanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLIGHTSystemLanSpeed.setStatus("mandatory")
_CLIGHTGlobalTrapTable_Object = MibTable
cLIGHTGlobalTrapTable = _CLIGHTGlobalTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 11)
)
if mibBuilder.loadTexts:
    cLIGHTGlobalTrapTable.setStatus("mandatory")
_GlobalRecipientEntry_Object = MibTableRow
globalRecipientEntry = _GlobalRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 11, 1)
)
globalRecipientEntry.setIndexNames(
    (0, "CityLight-MIB", "recipientIndex"),
)
if mibBuilder.loadTexts:
    globalRecipientEntry.setStatus("mandatory")
_RecipientIndex_Type = Integer32
_RecipientIndex_Object = MibTableColumn
recipientIndex = _RecipientIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 11, 1, 1),
    _RecipientIndex_Type()
)
recipientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recipientIndex.setStatus("mandatory")
_GlobalRecipientAddr_Type = IpAddress
_GlobalRecipientAddr_Object = MibTableColumn
globalRecipientAddr = _GlobalRecipientAddr_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 11, 1, 2),
    _GlobalRecipientAddr_Type()
)
globalRecipientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalRecipientAddr.setStatus("mandatory")


class _GlobalRecipientDescr_Type(DisplayString):
    """Custom type globalRecipientDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 29),
    )


_GlobalRecipientDescr_Type.__name__ = "DisplayString"
_GlobalRecipientDescr_Object = MibTableColumn
globalRecipientDescr = _GlobalRecipientDescr_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 11, 1, 3),
    _GlobalRecipientDescr_Type()
)
globalRecipientDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalRecipientDescr.setStatus("mandatory")
_CLIGHTSlotTrapTable_Object = MibTable
cLIGHTSlotTrapTable = _CLIGHTSlotTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 12)
)
if mibBuilder.loadTexts:
    cLIGHTSlotTrapTable.setStatus("mandatory")
_SlotRecipientEntry_Object = MibTableRow
slotRecipientEntry = _SlotRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 12, 1)
)
slotRecipientEntry.setIndexNames(
    (0, "CityLight-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotRecipientEntry.setStatus("mandatory")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 12, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("mandatory")
_SlotRecipientAddr_Type = IpAddress
_SlotRecipientAddr_Object = MibTableColumn
slotRecipientAddr = _SlotRecipientAddr_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 12, 1, 2),
    _SlotRecipientAddr_Type()
)
slotRecipientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotRecipientAddr.setStatus("mandatory")


class _SlotRecipientDescr_Type(DisplayString):
    """Custom type slotRecipientDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 29),
    )


_SlotRecipientDescr_Type.__name__ = "DisplayString"
_SlotRecipientDescr_Object = MibTableColumn
slotRecipientDescr = _SlotRecipientDescr_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 1, 12, 1, 3),
    _SlotRecipientDescr_Type()
)
slotRecipientDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotRecipientDescr.setStatus("mandatory")
_LocalInterfaceDescr_ObjectIdentity = ObjectIdentity
localInterfaceDescr = _LocalInterfaceDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2)
)
_CLIGHTLocalInterfaceTable_Object = MibTable
cLIGHTLocalInterfaceTable = _CLIGHTLocalInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cLIGHTLocalInterfaceTable.setStatus("mandatory")
_IfaceDescription_Object = MibTableRow
ifaceDescription = _IfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1)
)
ifaceDescription.setIndexNames(
    (0, "CityLight-MIB", "localSlotIndex"),
)
if mibBuilder.loadTexts:
    ifaceDescription.setStatus("mandatory")
_LocalSlotIndex_Type = Integer32
_LocalSlotIndex_Object = MibTableColumn
localSlotIndex = _LocalSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 1),
    _LocalSlotIndex_Type()
)
localSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localSlotIndex.setStatus("mandatory")


class _InterfaceType_Type(Integer32):
    """Custom type interfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("ethernet10Mbps", 1),
          ("ethernet100Mbps", 2),
          ("ethernet10-100Mbps", 3),
          ("atm622Mbps", 4),
          ("atm155Mbps", 5),
          ("tokenRing4-16Mbps", 6),
          ("ethernetGigabit", 7),
          ("fastEthernetSwitch10-100Mbps", 8),
          ("fiberChannel1062", 9),
          ("escon200", 10),
          ("fiberChannel266", 11),
          ("fiberChannel531", 12),
          ("fddi", 13),
          ("e1t1OnePort", 14),
          ("e1t1TwoPort", 15),
          ("ethernet100FX", 16),
          ("ethernetSwitch100FX", 17),
          ("ethernet10-100WDM", 18),
          ("ethernetSwitch10-100WDM", 19),
          ("ethernetGigabitWDM", 20),
          ("fiberChannelWDM", 21),
          ("highSpeedMultiProtocol", 22),
          ("highSpeedMultiProtocolWDM", 23),
          ("lowSpeedMultiProtocol", 24),
          ("lowSpeedMultiProtocolWDM", 25),
          ("e1t1Mux", 26),
          ("e1t1MuxWDM", 27),
          ("atm622WDM", 28),
          ("protectedGigabit", 29),
          ("protectedGigabitDoubleWidth", 30),
          ("cwdmFilter", 31),
          ("cwdmFilterTripleWidth1", 32),
          ("protectedATM622", 33),
          ("protectedATM622DoubleWidth", 34),
          ("protected2-5Gbps", 35),
          ("protected2-5GbpsDoubleWidth", 36),
          ("cwdmFilterTripleWidth2", 37),
          ("protectedFibreChannel", 38),
          ("protectedFibreChannelDoubleWidth", 39))
    )


_InterfaceType_Type.__name__ = "Integer32"
_InterfaceType_Object = MibTableColumn
interfaceType = _InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 2),
    _InterfaceType_Type()
)
interfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceType.setStatus("mandatory")


class _IfaceFiberPortState_Type(Integer32):
    """Custom type ifaceFiberPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("checkRx", 2),
          ("remoteFault", 3))
    )


_IfaceFiberPortState_Type.__name__ = "Integer32"
_IfaceFiberPortState_Object = MibTableColumn
ifaceFiberPortState = _IfaceFiberPortState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 3),
    _IfaceFiberPortState_Type()
)
ifaceFiberPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceFiberPortState.setStatus("mandatory")


class _IfaceUserPortState_Type(Integer32):
    """Custom type ifaceUserPortState based on Integer32"""
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
        *(("active", 1),
          ("linkUp", 2),
          ("linkDown", 3),
          ("remoteFault", 4),
          ("linkDownAndRemoteFault", 5))
    )


_IfaceUserPortState_Type.__name__ = "Integer32"
_IfaceUserPortState_Object = MibTableColumn
ifaceUserPortState = _IfaceUserPortState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 4),
    _IfaceUserPortState_Type()
)
ifaceUserPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPortState.setStatus("mandatory")


class _IfaceLANdata_Type(Integer32):
    """Custom type ifaceLANdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_IfaceLANdata_Type.__name__ = "Integer32"
_IfaceLANdata_Object = MibTableColumn
ifaceLANdata = _IfaceLANdata_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 5),
    _IfaceLANdata_Type()
)
ifaceLANdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceLANdata.setStatus("mandatory")


class _IfaceVersion_Type(DisplayString):
    """Custom type ifaceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_IfaceVersion_Type.__name__ = "DisplayString"
_IfaceVersion_Object = MibTableColumn
ifaceVersion = _IfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 6),
    _IfaceVersion_Type()
)
ifaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceVersion.setStatus("mandatory")


class _IfacePSUStatus_Type(Integer32):
    """Custom type ifacePSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("underVoltage", 2),
          ("overVoltage", 3))
    )


_IfacePSUStatus_Type.__name__ = "Integer32"
_IfacePSUStatus_Object = MibTableColumn
ifacePSUStatus = _IfacePSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 7),
    _IfacePSUStatus_Type()
)
ifacePSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifacePSUStatus.setStatus("mandatory")
_IfaceTemperature_Type = Integer32
_IfaceTemperature_Object = MibTableColumn
ifaceTemperature = _IfaceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 8),
    _IfaceTemperature_Type()
)
ifaceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceTemperature.setStatus("mandatory")


class _IfaceSerialNumber_Type(DisplayString):
    """Custom type ifaceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfaceSerialNumber_Type.__name__ = "DisplayString"
_IfaceSerialNumber_Object = MibTableColumn
ifaceSerialNumber = _IfaceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 9),
    _IfaceSerialNumber_Type()
)
ifaceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSerialNumber.setStatus("mandatory")


class _IfaceLanSpeed_Type(Integer32):
    """Custom type ifaceLanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_IfaceLanSpeed_Type.__name__ = "Integer32"
_IfaceLanSpeed_Object = MibTableColumn
ifaceLanSpeed = _IfaceLanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 10),
    _IfaceLanSpeed_Type()
)
ifaceLanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceLanSpeed.setStatus("mandatory")


class _IfaceUserPort2State_Type(Integer32):
    """Custom type ifaceUserPort2State based on Integer32"""
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
        *(("active", 1),
          ("linkUp", 2),
          ("linkDown", 3),
          ("remoteFault", 4),
          ("linkDownAndRemoteFault", 5))
    )


_IfaceUserPort2State_Type.__name__ = "Integer32"
_IfaceUserPort2State_Object = MibTableColumn
ifaceUserPort2State = _IfaceUserPort2State_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 11),
    _IfaceUserPort2State_Type()
)
ifaceUserPort2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPort2State.setStatus("mandatory")


class _IfaceFiberPortBState_Type(Integer32):
    """Custom type ifaceFiberPortBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("checkRx", 2),
          ("remoteFault", 3))
    )


_IfaceFiberPortBState_Type.__name__ = "Integer32"
_IfaceFiberPortBState_Object = MibTableColumn
ifaceFiberPortBState = _IfaceFiberPortBState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 12),
    _IfaceFiberPortBState_Type()
)
ifaceFiberPortBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceFiberPortBState.setStatus("mandatory")


class _IfaceSystemConnectorType_Type(Integer32):
    """Custom type ifaceSystemConnectorType based on Integer32"""
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
        *(("sc", 1),
          ("st", 2),
          ("fc", 3),
          ("rj45", 4))
    )


_IfaceSystemConnectorType_Type.__name__ = "Integer32"
_IfaceSystemConnectorType_Object = MibTableColumn
ifaceSystemConnectorType = _IfaceSystemConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 13),
    _IfaceSystemConnectorType_Type()
)
ifaceSystemConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSystemConnectorType.setStatus("mandatory")


class _IfaceSystemFibreType_Type(Integer32):
    """Custom type ifaceSystemFibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2))
    )


_IfaceSystemFibreType_Type.__name__ = "Integer32"
_IfaceSystemFibreType_Object = MibTableColumn
ifaceSystemFibreType = _IfaceSystemFibreType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 14),
    _IfaceSystemFibreType_Type()
)
ifaceSystemFibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSystemFibreType.setStatus("mandatory")


class _IfaceSystemLaserType_Type(Integer32):
    """Custom type ifaceSystemLaserType based on Integer32"""
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
        *(("standard", 1),
          ("medium", 2),
          ("high", 3),
          ("veryHigh", 4))
    )


_IfaceSystemLaserType_Type.__name__ = "Integer32"
_IfaceSystemLaserType_Object = MibTableColumn
ifaceSystemLaserType = _IfaceSystemLaserType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 15),
    _IfaceSystemLaserType_Type()
)
ifaceSystemLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSystemLaserType.setStatus("mandatory")


class _IfaceSystemLaserRange_Type(Integer32):
    """Custom type ifaceSystemLaserRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_IfaceSystemLaserRange_Type.__name__ = "Integer32"
_IfaceSystemLaserRange_Object = MibTableColumn
ifaceSystemLaserRange = _IfaceSystemLaserRange_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 16),
    _IfaceSystemLaserRange_Type()
)
ifaceSystemLaserRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSystemLaserRange.setStatus("mandatory")


class _IfaceSystemWavelength_Type(DisplayString):
    """Custom type ifaceSystemWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IfaceSystemWavelength_Type.__name__ = "DisplayString"
_IfaceSystemWavelength_Object = MibTableColumn
ifaceSystemWavelength = _IfaceSystemWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 17),
    _IfaceSystemWavelength_Type()
)
ifaceSystemWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSystemWavelength.setStatus("mandatory")


class _IfaceUserPortConnectorType_Type(Integer32):
    """Custom type ifaceUserPortConnectorType based on Integer32"""
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
        *(("sc", 1),
          ("st", 2),
          ("fc", 3),
          ("rj45", 4))
    )


_IfaceUserPortConnectorType_Type.__name__ = "Integer32"
_IfaceUserPortConnectorType_Object = MibTableColumn
ifaceUserPortConnectorType = _IfaceUserPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 18),
    _IfaceUserPortConnectorType_Type()
)
ifaceUserPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPortConnectorType.setStatus("mandatory")


class _IfaceUserPortFibreType_Type(Integer32):
    """Custom type ifaceUserPortFibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2))
    )


_IfaceUserPortFibreType_Type.__name__ = "Integer32"
_IfaceUserPortFibreType_Object = MibTableColumn
ifaceUserPortFibreType = _IfaceUserPortFibreType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 19),
    _IfaceUserPortFibreType_Type()
)
ifaceUserPortFibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPortFibreType.setStatus("mandatory")


class _IfaceUserPortLaserType_Type(Integer32):
    """Custom type ifaceUserPortLaserType based on Integer32"""
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
        *(("standard", 1),
          ("medium", 2),
          ("high", 3),
          ("veryHigh", 4))
    )


_IfaceUserPortLaserType_Type.__name__ = "Integer32"
_IfaceUserPortLaserType_Object = MibTableColumn
ifaceUserPortLaserType = _IfaceUserPortLaserType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 20),
    _IfaceUserPortLaserType_Type()
)
ifaceUserPortLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPortLaserType.setStatus("mandatory")


class _IfaceUserPortLaserRange_Type(Integer32):
    """Custom type ifaceUserPortLaserRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_IfaceUserPortLaserRange_Type.__name__ = "Integer32"
_IfaceUserPortLaserRange_Object = MibTableColumn
ifaceUserPortLaserRange = _IfaceUserPortLaserRange_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 21),
    _IfaceUserPortLaserRange_Type()
)
ifaceUserPortLaserRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPortLaserRange.setStatus("mandatory")


class _IfaceUserPortWavelength_Type(DisplayString):
    """Custom type ifaceUserPortWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IfaceUserPortWavelength_Type.__name__ = "DisplayString"
_IfaceUserPortWavelength_Object = MibTableColumn
ifaceUserPortWavelength = _IfaceUserPortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 22),
    _IfaceUserPortWavelength_Type()
)
ifaceUserPortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPortWavelength.setStatus("mandatory")


class _IfaceUserPort2ConnectorType_Type(Integer32):
    """Custom type ifaceUserPort2ConnectorType based on Integer32"""
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
        *(("sc", 1),
          ("st", 2),
          ("fc", 3),
          ("rj45", 4))
    )


_IfaceUserPort2ConnectorType_Type.__name__ = "Integer32"
_IfaceUserPort2ConnectorType_Object = MibTableColumn
ifaceUserPort2ConnectorType = _IfaceUserPort2ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 23),
    _IfaceUserPort2ConnectorType_Type()
)
ifaceUserPort2ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPort2ConnectorType.setStatus("mandatory")


class _IfaceUserPort2FibreType_Type(Integer32):
    """Custom type ifaceUserPort2FibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2))
    )


_IfaceUserPort2FibreType_Type.__name__ = "Integer32"
_IfaceUserPort2FibreType_Object = MibTableColumn
ifaceUserPort2FibreType = _IfaceUserPort2FibreType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 24),
    _IfaceUserPort2FibreType_Type()
)
ifaceUserPort2FibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPort2FibreType.setStatus("mandatory")


class _IfaceUserPort2LaserType_Type(Integer32):
    """Custom type ifaceUserPort2LaserType based on Integer32"""
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
        *(("standard", 1),
          ("medium", 2),
          ("high", 3),
          ("veryHigh", 4))
    )


_IfaceUserPort2LaserType_Type.__name__ = "Integer32"
_IfaceUserPort2LaserType_Object = MibTableColumn
ifaceUserPort2LaserType = _IfaceUserPort2LaserType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 25),
    _IfaceUserPort2LaserType_Type()
)
ifaceUserPort2LaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPort2LaserType.setStatus("mandatory")


class _IfaceUserPort2LaserRange_Type(Integer32):
    """Custom type ifaceUserPort2LaserRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_IfaceUserPort2LaserRange_Type.__name__ = "Integer32"
_IfaceUserPort2LaserRange_Object = MibTableColumn
ifaceUserPort2LaserRange = _IfaceUserPort2LaserRange_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 26),
    _IfaceUserPort2LaserRange_Type()
)
ifaceUserPort2LaserRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPort2LaserRange.setStatus("mandatory")


class _IfaceUserPort2Wavelength_Type(DisplayString):
    """Custom type ifaceUserPort2Wavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IfaceUserPort2Wavelength_Type.__name__ = "DisplayString"
_IfaceUserPort2Wavelength_Object = MibTableColumn
ifaceUserPort2Wavelength = _IfaceUserPort2Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 2, 1, 1, 27),
    _IfaceUserPort2Wavelength_Type()
)
ifaceUserPort2Wavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceUserPort2Wavelength.setStatus("mandatory")
_RemoteInterfaceDescr_ObjectIdentity = ObjectIdentity
remoteInterfaceDescr = _RemoteInterfaceDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3)
)
_CLIGHTRemoteInterfaceTable_Object = MibTable
cLIGHTRemoteInterfaceTable = _CLIGHTRemoteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cLIGHTRemoteInterfaceTable.setStatus("mandatory")
_RemoteIfaceDescription_Object = MibTableRow
remoteIfaceDescription = _RemoteIfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1)
)
remoteIfaceDescription.setIndexNames(
    (0, "CityLight-MIB", "remoteSlotIndex"),
)
if mibBuilder.loadTexts:
    remoteIfaceDescription.setStatus("mandatory")
_RemoteSlotIndex_Type = Integer32
_RemoteSlotIndex_Object = MibTableColumn
remoteSlotIndex = _RemoteSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 1),
    _RemoteSlotIndex_Type()
)
remoteSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSlotIndex.setStatus("mandatory")


class _RemoteIfaceType_Type(Integer32):
    """Custom type remoteIfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("ethernet10Mbps", 1),
          ("ethernet100Mbps", 2),
          ("ethernet10-100Mbps", 3),
          ("atm622Mbps", 4),
          ("atm155Mbps", 5),
          ("tokenRing4-16Mbps", 6),
          ("ethernetGigabit", 7),
          ("fastEthernetSwitch10-100Mbps", 8),
          ("fiberChannel1062", 9),
          ("escon200", 10),
          ("fiberChannel266", 11),
          ("fiberChannel531", 12),
          ("fddi", 13),
          ("e1t1OnePort", 14),
          ("e1t1TwoPort", 15),
          ("ethernet100FX", 16),
          ("ethernetSwitch100FX", 17),
          ("ethernet10-100WDM", 18),
          ("ethernetSwitch10-100WDM", 19),
          ("ethernetGigabitWDM", 20),
          ("fiberChannelWDM", 21),
          ("highSpeedMultiProtocol", 22),
          ("highSpeedMultiProtocolWDM", 23),
          ("lowSpeedMultiProtocol", 24),
          ("lowSpeedMultiProtocolWDM", 25),
          ("e1t1Mux", 26),
          ("e1t1MuxWDM", 27),
          ("atm622WDM", 28),
          ("protectedGigabit", 29),
          ("protectedGigabitDoubleWidth", 30),
          ("cwdmFilter", 31),
          ("cwdmFilterTripleWidth2", 32),
          ("protectedATM622", 33),
          ("protectedATM622DoubleWidth", 34),
          ("protected2-5Gbps", 35),
          ("protected2-5GbpsDoubleWidth", 36),
          ("cwdmFilterTripleWidth3", 37),
          ("protectedFibreChannel", 38),
          ("protectedFibreChannelDoubleWidth", 39))
    )


_RemoteIfaceType_Type.__name__ = "Integer32"
_RemoteIfaceType_Object = MibTableColumn
remoteIfaceType = _RemoteIfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 2),
    _RemoteIfaceType_Type()
)
remoteIfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceType.setStatus("mandatory")


class _RemoteIfaceFiberPortState_Type(Integer32):
    """Custom type remoteIfaceFiberPortState based on Integer32"""
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
        *(("inserted", 1),
          ("notInserted", 2),
          ("checkRx", 3),
          ("remoteFault", 4))
    )


_RemoteIfaceFiberPortState_Type.__name__ = "Integer32"
_RemoteIfaceFiberPortState_Object = MibTableColumn
remoteIfaceFiberPortState = _RemoteIfaceFiberPortState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 3),
    _RemoteIfaceFiberPortState_Type()
)
remoteIfaceFiberPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceFiberPortState.setStatus("mandatory")


class _RemoteIfaceUserPortState_Type(Integer32):
    """Custom type remoteIfaceUserPortState based on Integer32"""
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
        *(("active", 1),
          ("linkUp", 2),
          ("linkDown", 3),
          ("remoteFault", 4),
          ("linkDownAndRemoteFault", 5))
    )


_RemoteIfaceUserPortState_Type.__name__ = "Integer32"
_RemoteIfaceUserPortState_Object = MibTableColumn
remoteIfaceUserPortState = _RemoteIfaceUserPortState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 4),
    _RemoteIfaceUserPortState_Type()
)
remoteIfaceUserPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPortState.setStatus("mandatory")


class _RemoteIfaceLANdata_Type(Integer32):
    """Custom type remoteIfaceLANdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_RemoteIfaceLANdata_Type.__name__ = "Integer32"
_RemoteIfaceLANdata_Object = MibTableColumn
remoteIfaceLANdata = _RemoteIfaceLANdata_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 5),
    _RemoteIfaceLANdata_Type()
)
remoteIfaceLANdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceLANdata.setStatus("mandatory")


class _RemoteIfaceVersion_Type(DisplayString):
    """Custom type remoteIfaceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RemoteIfaceVersion_Type.__name__ = "DisplayString"
_RemoteIfaceVersion_Object = MibTableColumn
remoteIfaceVersion = _RemoteIfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 6),
    _RemoteIfaceVersion_Type()
)
remoteIfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceVersion.setStatus("mandatory")


class _RemoteIfaceLocation_Type(DisplayString):
    """Custom type remoteIfaceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_RemoteIfaceLocation_Type.__name__ = "DisplayString"
_RemoteIfaceLocation_Object = MibTableColumn
remoteIfaceLocation = _RemoteIfaceLocation_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 7),
    _RemoteIfaceLocation_Type()
)
remoteIfaceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteIfaceLocation.setStatus("mandatory")


class _RemoteIfacePSUStatus_Type(Integer32):
    """Custom type remoteIfacePSUStatus based on Integer32"""
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
        *(("good", 1),
          ("primaryFailed", 2),
          ("secondaryFailed", 3),
          ("unknown", 4))
    )


_RemoteIfacePSUStatus_Type.__name__ = "Integer32"
_RemoteIfacePSUStatus_Object = MibTableColumn
remoteIfacePSUStatus = _RemoteIfacePSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 8),
    _RemoteIfacePSUStatus_Type()
)
remoteIfacePSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfacePSUStatus.setStatus("mandatory")
_RemoteIfaceTemperature_Type = Integer32
_RemoteIfaceTemperature_Object = MibTableColumn
remoteIfaceTemperature = _RemoteIfaceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 9),
    _RemoteIfaceTemperature_Type()
)
remoteIfaceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceTemperature.setStatus("mandatory")


class _RemoteIfaceFanStatus_Type(Integer32):
    """Custom type remoteIfaceFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("failed", 2))
    )


_RemoteIfaceFanStatus_Type.__name__ = "Integer32"
_RemoteIfaceFanStatus_Object = MibTableColumn
remoteIfaceFanStatus = _RemoteIfaceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 10),
    _RemoteIfaceFanStatus_Type()
)
remoteIfaceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceFanStatus.setStatus("mandatory")


class _RemoteIfaceTempStatus_Type(Integer32):
    """Custom type remoteIfaceTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("overTemperature", 2),
          ("underTemperature", 3))
    )


_RemoteIfaceTempStatus_Type.__name__ = "Integer32"
_RemoteIfaceTempStatus_Object = MibTableColumn
remoteIfaceTempStatus = _RemoteIfaceTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 11),
    _RemoteIfaceTempStatus_Type()
)
remoteIfaceTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceTempStatus.setStatus("mandatory")


class _RemoteIfaceSerialNumber_Type(DisplayString):
    """Custom type remoteIfaceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RemoteIfaceSerialNumber_Type.__name__ = "DisplayString"
_RemoteIfaceSerialNumber_Object = MibTableColumn
remoteIfaceSerialNumber = _RemoteIfaceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 12),
    _RemoteIfaceSerialNumber_Type()
)
remoteIfaceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceSerialNumber.setStatus("mandatory")


class _RemoteIfaceUserPort2State_Type(Integer32):
    """Custom type remoteIfaceUserPort2State based on Integer32"""
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
        *(("active", 1),
          ("linkUp", 2),
          ("linkDown", 3),
          ("remoteFault", 4),
          ("linkDownAndRemoteFault", 5))
    )


_RemoteIfaceUserPort2State_Type.__name__ = "Integer32"
_RemoteIfaceUserPort2State_Object = MibTableColumn
remoteIfaceUserPort2State = _RemoteIfaceUserPort2State_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 13),
    _RemoteIfaceUserPort2State_Type()
)
remoteIfaceUserPort2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPort2State.setStatus("mandatory")


class _RemoteIfaceFiberPortBState_Type(Integer32):
    """Custom type remoteIfaceFiberPortBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("checkRx", 3),
          ("remoteFault", 4))
    )


_RemoteIfaceFiberPortBState_Type.__name__ = "Integer32"
_RemoteIfaceFiberPortBState_Object = MibTableColumn
remoteIfaceFiberPortBState = _RemoteIfaceFiberPortBState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 14),
    _RemoteIfaceFiberPortBState_Type()
)
remoteIfaceFiberPortBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceFiberPortBState.setStatus("mandatory")


class _RemoteIfaceSystemConnectorType_Type(Integer32):
    """Custom type remoteIfaceSystemConnectorType based on Integer32"""
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
        *(("sc", 1),
          ("st", 2),
          ("fc", 3),
          ("rj45", 4))
    )


_RemoteIfaceSystemConnectorType_Type.__name__ = "Integer32"
_RemoteIfaceSystemConnectorType_Object = MibTableColumn
remoteIfaceSystemConnectorType = _RemoteIfaceSystemConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 15),
    _RemoteIfaceSystemConnectorType_Type()
)
remoteIfaceSystemConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceSystemConnectorType.setStatus("mandatory")


class _RemoteIfaceSystemFibreType_Type(Integer32):
    """Custom type remoteIfaceSystemFibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2))
    )


_RemoteIfaceSystemFibreType_Type.__name__ = "Integer32"
_RemoteIfaceSystemFibreType_Object = MibTableColumn
remoteIfaceSystemFibreType = _RemoteIfaceSystemFibreType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 16),
    _RemoteIfaceSystemFibreType_Type()
)
remoteIfaceSystemFibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceSystemFibreType.setStatus("mandatory")


class _RemoteIfaceSystemLaserType_Type(Integer32):
    """Custom type remoteIfaceSystemLaserType based on Integer32"""
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
        *(("standard", 1),
          ("medium", 2),
          ("high", 3),
          ("veryHigh", 4))
    )


_RemoteIfaceSystemLaserType_Type.__name__ = "Integer32"
_RemoteIfaceSystemLaserType_Object = MibTableColumn
remoteIfaceSystemLaserType = _RemoteIfaceSystemLaserType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 17),
    _RemoteIfaceSystemLaserType_Type()
)
remoteIfaceSystemLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceSystemLaserType.setStatus("mandatory")


class _RemoteIfaceSystemLaserRange_Type(Integer32):
    """Custom type remoteIfaceSystemLaserRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_RemoteIfaceSystemLaserRange_Type.__name__ = "Integer32"
_RemoteIfaceSystemLaserRange_Object = MibTableColumn
remoteIfaceSystemLaserRange = _RemoteIfaceSystemLaserRange_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 18),
    _RemoteIfaceSystemLaserRange_Type()
)
remoteIfaceSystemLaserRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceSystemLaserRange.setStatus("mandatory")


class _RemoteIfaceSystemWavelength_Type(DisplayString):
    """Custom type remoteIfaceSystemWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RemoteIfaceSystemWavelength_Type.__name__ = "DisplayString"
_RemoteIfaceSystemWavelength_Object = MibTableColumn
remoteIfaceSystemWavelength = _RemoteIfaceSystemWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 19),
    _RemoteIfaceSystemWavelength_Type()
)
remoteIfaceSystemWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceSystemWavelength.setStatus("mandatory")


class _RemoteIfaceUserPortConnectorType_Type(Integer32):
    """Custom type remoteIfaceUserPortConnectorType based on Integer32"""
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
        *(("sc", 1),
          ("st", 2),
          ("fc", 3),
          ("rj45", 4))
    )


_RemoteIfaceUserPortConnectorType_Type.__name__ = "Integer32"
_RemoteIfaceUserPortConnectorType_Object = MibTableColumn
remoteIfaceUserPortConnectorType = _RemoteIfaceUserPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 20),
    _RemoteIfaceUserPortConnectorType_Type()
)
remoteIfaceUserPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPortConnectorType.setStatus("mandatory")


class _RemoteIfaceUserPortFibreType_Type(Integer32):
    """Custom type remoteIfaceUserPortFibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2))
    )


_RemoteIfaceUserPortFibreType_Type.__name__ = "Integer32"
_RemoteIfaceUserPortFibreType_Object = MibTableColumn
remoteIfaceUserPortFibreType = _RemoteIfaceUserPortFibreType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 21),
    _RemoteIfaceUserPortFibreType_Type()
)
remoteIfaceUserPortFibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPortFibreType.setStatus("mandatory")


class _RemoteIfaceUserPortLaserType_Type(Integer32):
    """Custom type remoteIfaceUserPortLaserType based on Integer32"""
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
        *(("standard", 1),
          ("medium", 2),
          ("high", 3),
          ("veryHigh", 4))
    )


_RemoteIfaceUserPortLaserType_Type.__name__ = "Integer32"
_RemoteIfaceUserPortLaserType_Object = MibTableColumn
remoteIfaceUserPortLaserType = _RemoteIfaceUserPortLaserType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 22),
    _RemoteIfaceUserPortLaserType_Type()
)
remoteIfaceUserPortLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPortLaserType.setStatus("mandatory")


class _RemoteIfaceUserPortLaserRange_Type(Integer32):
    """Custom type remoteIfaceUserPortLaserRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_RemoteIfaceUserPortLaserRange_Type.__name__ = "Integer32"
_RemoteIfaceUserPortLaserRange_Object = MibTableColumn
remoteIfaceUserPortLaserRange = _RemoteIfaceUserPortLaserRange_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 23),
    _RemoteIfaceUserPortLaserRange_Type()
)
remoteIfaceUserPortLaserRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPortLaserRange.setStatus("mandatory")


class _RemoteIfaceUserPortWavelength_Type(DisplayString):
    """Custom type remoteIfaceUserPortWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RemoteIfaceUserPortWavelength_Type.__name__ = "DisplayString"
_RemoteIfaceUserPortWavelength_Object = MibTableColumn
remoteIfaceUserPortWavelength = _RemoteIfaceUserPortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 24),
    _RemoteIfaceUserPortWavelength_Type()
)
remoteIfaceUserPortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPortWavelength.setStatus("mandatory")


class _RemoteIfaceUserPort2ConnectorType_Type(Integer32):
    """Custom type remoteIfaceUserPort2ConnectorType based on Integer32"""
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
        *(("sc", 1),
          ("st", 2),
          ("fc", 3),
          ("rj45", 4))
    )


_RemoteIfaceUserPort2ConnectorType_Type.__name__ = "Integer32"
_RemoteIfaceUserPort2ConnectorType_Object = MibTableColumn
remoteIfaceUserPort2ConnectorType = _RemoteIfaceUserPort2ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 25),
    _RemoteIfaceUserPort2ConnectorType_Type()
)
remoteIfaceUserPort2ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPort2ConnectorType.setStatus("mandatory")


class _RemoteIfaceUserPort2FibreType_Type(Integer32):
    """Custom type remoteIfaceUserPort2FibreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("multiMode", 2))
    )


_RemoteIfaceUserPort2FibreType_Type.__name__ = "Integer32"
_RemoteIfaceUserPort2FibreType_Object = MibTableColumn
remoteIfaceUserPort2FibreType = _RemoteIfaceUserPort2FibreType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 26),
    _RemoteIfaceUserPort2FibreType_Type()
)
remoteIfaceUserPort2FibreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPort2FibreType.setStatus("mandatory")


class _RemoteIfaceUserPort2LaserType_Type(Integer32):
    """Custom type remoteIfaceUserPort2LaserType based on Integer32"""
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
        *(("standard", 1),
          ("medium", 2),
          ("high", 3),
          ("veryHigh", 4))
    )


_RemoteIfaceUserPort2LaserType_Type.__name__ = "Integer32"
_RemoteIfaceUserPort2LaserType_Object = MibTableColumn
remoteIfaceUserPort2LaserType = _RemoteIfaceUserPort2LaserType_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 27),
    _RemoteIfaceUserPort2LaserType_Type()
)
remoteIfaceUserPort2LaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPort2LaserType.setStatus("mandatory")


class _RemoteIfaceUserPort2LaserRange_Type(Integer32):
    """Custom type remoteIfaceUserPort2LaserRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_RemoteIfaceUserPort2LaserRange_Type.__name__ = "Integer32"
_RemoteIfaceUserPort2LaserRange_Object = MibTableColumn
remoteIfaceUserPort2LaserRange = _RemoteIfaceUserPort2LaserRange_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 28),
    _RemoteIfaceUserPort2LaserRange_Type()
)
remoteIfaceUserPort2LaserRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPort2LaserRange.setStatus("mandatory")


class _RemoteIfaceUserPort2Wavelength_Type(DisplayString):
    """Custom type remoteIfaceUserPort2Wavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RemoteIfaceUserPort2Wavelength_Type.__name__ = "DisplayString"
_RemoteIfaceUserPort2Wavelength_Object = MibTableColumn
remoteIfaceUserPort2Wavelength = _RemoteIfaceUserPort2Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 3, 1, 1, 29),
    _RemoteIfaceUserPort2Wavelength_Type()
)
remoteIfaceUserPort2Wavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIfaceUserPort2Wavelength.setStatus("mandatory")
_TrapEnable_ObjectIdentity = ObjectIdentity
trapEnable = _TrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4)
)


class _TeSystemPSUState_Type(Integer32):
    """Custom type teSystemPSUState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeSystemPSUState_Type.__name__ = "Integer32"
_TeSystemPSUState_Object = MibScalar
teSystemPSUState = _TeSystemPSUState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 1),
    _TeSystemPSUState_Type()
)
teSystemPSUState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teSystemPSUState.setStatus("mandatory")


class _TeSystemTempState_Type(Integer32):
    """Custom type teSystemTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeSystemTempState_Type.__name__ = "Integer32"
_TeSystemTempState_Object = MibScalar
teSystemTempState = _TeSystemTempState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 2),
    _TeSystemTempState_Type()
)
teSystemTempState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teSystemTempState.setStatus("mandatory")


class _TeSystemFanFailState_Type(Integer32):
    """Custom type teSystemFanFailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeSystemFanFailState_Type.__name__ = "Integer32"
_TeSystemFanFailState_Object = MibScalar
teSystemFanFailState = _TeSystemFanFailState_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 3),
    _TeSystemFanFailState_Type()
)
teSystemFanFailState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teSystemFanFailState.setStatus("mandatory")


class _TeSystemAuthentication_Type(Integer32):
    """Custom type teSystemAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeSystemAuthentication_Type.__name__ = "Integer32"
_TeSystemAuthentication_Object = MibScalar
teSystemAuthentication = _TeSystemAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 4),
    _TeSystemAuthentication_Type()
)
teSystemAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teSystemAuthentication.setStatus("mandatory")
_TeSlotTrapTable_Object = MibTable
teSlotTrapTable = _TeSlotTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5)
)
if mibBuilder.loadTexts:
    teSlotTrapTable.setStatus("mandatory")
_ClSlotTrapEntry_Object = MibTableRow
clSlotTrapEntry = _ClSlotTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1)
)
clSlotTrapEntry.setIndexNames(
    (0, "CityLight-MIB", "teSlotIndex"),
)
if mibBuilder.loadTexts:
    clSlotTrapEntry.setStatus("mandatory")
_TeSlotIndex_Type = Integer32
_TeSlotIndex_Object = MibTableColumn
teSlotIndex = _TeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 1),
    _TeSlotIndex_Type()
)
teSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teSlotIndex.setStatus("mandatory")


class _TeLocalFibreRxWrap_Type(Integer32):
    """Custom type teLocalFibreRxWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeLocalFibreRxWrap_Type.__name__ = "Integer32"
_TeLocalFibreRxWrap_Object = MibTableColumn
teLocalFibreRxWrap = _TeLocalFibreRxWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 2),
    _TeLocalFibreRxWrap_Type()
)
teLocalFibreRxWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teLocalFibreRxWrap.setStatus("mandatory")


class _TeRemoteFaultWrap_Type(Integer32):
    """Custom type teRemoteFaultWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeRemoteFaultWrap_Type.__name__ = "Integer32"
_TeRemoteFaultWrap_Object = MibTableColumn
teRemoteFaultWrap = _TeRemoteFaultWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 3),
    _TeRemoteFaultWrap_Type()
)
teRemoteFaultWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teRemoteFaultWrap.setStatus("mandatory")


class _TeLocalUserPortWrap_Type(Integer32):
    """Custom type teLocalUserPortWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeLocalUserPortWrap_Type.__name__ = "Integer32"
_TeLocalUserPortWrap_Object = MibTableColumn
teLocalUserPortWrap = _TeLocalUserPortWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 4),
    _TeLocalUserPortWrap_Type()
)
teLocalUserPortWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teLocalUserPortWrap.setStatus("mandatory")


class _TeRemoteUserPortWrap_Type(Integer32):
    """Custom type teRemoteUserPortWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeRemoteUserPortWrap_Type.__name__ = "Integer32"
_TeRemoteUserPortWrap_Object = MibTableColumn
teRemoteUserPortWrap = _TeRemoteUserPortWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 5),
    _TeRemoteUserPortWrap_Type()
)
teRemoteUserPortWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teRemoteUserPortWrap.setStatus("mandatory")


class _TeRemotePSUWrap_Type(Integer32):
    """Custom type teRemotePSUWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeRemotePSUWrap_Type.__name__ = "Integer32"
_TeRemotePSUWrap_Object = MibTableColumn
teRemotePSUWrap = _TeRemotePSUWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 6),
    _TeRemotePSUWrap_Type()
)
teRemotePSUWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teRemotePSUWrap.setStatus("mandatory")


class _TeRemoteTempWrap_Type(Integer32):
    """Custom type teRemoteTempWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeRemoteTempWrap_Type.__name__ = "Integer32"
_TeRemoteTempWrap_Object = MibTableColumn
teRemoteTempWrap = _TeRemoteTempWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 7),
    _TeRemoteTempWrap_Type()
)
teRemoteTempWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teRemoteTempWrap.setStatus("mandatory")


class _TeRemoteFanFailWrap_Type(Integer32):
    """Custom type teRemoteFanFailWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TeRemoteFanFailWrap_Type.__name__ = "Integer32"
_TeRemoteFanFailWrap_Object = MibTableColumn
teRemoteFanFailWrap = _TeRemoteFanFailWrap_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 4, 5, 1, 8),
    _TeRemoteFanFailWrap_Type()
)
teRemoteFanFailWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teRemoteFanFailWrap.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5)
)
_SecurityUserTable_Object = MibTable
securityUserTable = _SecurityUserTable_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1)
)
if mibBuilder.loadTexts:
    securityUserTable.setStatus("mandatory")
_SecurityUserEntry_Object = MibTableRow
securityUserEntry = _SecurityUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1, 1)
)
securityUserEntry.setIndexNames(
    (0, "CityLight-MIB", "securityAccountIndex"),
)
if mibBuilder.loadTexts:
    securityUserEntry.setStatus("mandatory")
_SecurityAccountIndex_Type = Integer32
_SecurityAccountIndex_Object = MibTableColumn
securityAccountIndex = _SecurityAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1, 1, 1),
    _SecurityAccountIndex_Type()
)
securityAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAccountIndex.setStatus("mandatory")


class _SecurityUserName_Type(DisplayString):
    """Custom type securityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 10),
    )


_SecurityUserName_Type.__name__ = "DisplayString"
_SecurityUserName_Object = MibTableColumn
securityUserName = _SecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1, 1, 2),
    _SecurityUserName_Type()
)
securityUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserName.setStatus("mandatory")


class _SecurityUserAccessLevel_Type(Integer32):
    """Custom type securityUserAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 1),
          ("manager", 2))
    )


_SecurityUserAccessLevel_Type.__name__ = "Integer32"
_SecurityUserAccessLevel_Object = MibTableColumn
securityUserAccessLevel = _SecurityUserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1, 1, 3),
    _SecurityUserAccessLevel_Type()
)
securityUserAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserAccessLevel.setStatus("mandatory")


class _SecurityUserPassword_Type(DisplayString):
    """Custom type securityUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_SecurityUserPassword_Type.__name__ = "DisplayString"
_SecurityUserPassword_Object = MibTableColumn
securityUserPassword = _SecurityUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1, 1, 4),
    _SecurityUserPassword_Type()
)
securityUserPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    securityUserPassword.setStatus("mandatory")
_SecurityAccountStatus_Type = Integer32
_SecurityAccountStatus_Object = MibTableColumn
securityAccountStatus = _SecurityAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 5, 1, 1, 5),
    _SecurityAccountStatus_Type()
)
securityAccountStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    securityAccountStatus.setStatus("mandatory")
_TrapLog_ObjectIdentity = ObjectIdentity
trapLog = _TrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6)
)
_CLightTrapLog_Object = MibTable
cLightTrapLog = _CLightTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cLightTrapLog.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1)
)
logEntry.setIndexNames(
    (0, "CityLight-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")
_Destination_Type = IpAddress
_Destination_Object = MibTableColumn
destination = _Destination_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1, 2),
    _Destination_Type()
)
destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destination.setStatus("mandatory")


class _TimeStamp_Type(DisplayString):
    """Custom type timeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TimeStamp_Type.__name__ = "DisplayString"
_TimeStamp_Object = MibTableColumn
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1, 3),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeStamp.setStatus("mandatory")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1, 4),
    _Description_Type()
)
description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")


class _Parameter1_Type(DisplayString):
    """Custom type parameter1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Parameter1_Type.__name__ = "DisplayString"
_Parameter1_Object = MibTableColumn
parameter1 = _Parameter1_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1, 5),
    _Parameter1_Type()
)
parameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameter1.setStatus("mandatory")


class _Parameter2_Type(DisplayString):
    """Custom type parameter2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Parameter2_Type.__name__ = "DisplayString"
_Parameter2_Object = MibTableColumn
parameter2 = _Parameter2_Object(
    (1, 3, 6, 1, 4, 1, 1671, 2, 6, 1, 1, 6),
    _Parameter2_Type()
)
parameter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parameter2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

localFibreRxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 40)
)
localFibreRxTrap.setObjects(
      *(("CityLight-MIB", "localSlotIndex"),
        ("CityLight-MIB", "ifaceFiberPortState"))
)
if mibBuilder.loadTexts:
    localFibreRxTrap.setStatus(
        ""
    )

localUserPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 42)
)
localUserPortTrap.setObjects(
      *(("CityLight-MIB", "localSlotIndex"),
        ("CityLight-MIB", "ifaceUserPortState"))
)
if mibBuilder.loadTexts:
    localUserPortTrap.setStatus(
        ""
    )

localEOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 43)
)
localEOLTrap.setObjects(
    ("CityLight-MIB", "localSlotIndex")
)
if mibBuilder.loadTexts:
    localEOLTrap.setStatus(
        ""
    )

localCardRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 44)
)
localCardRemovedTrap.setObjects(
    ("CityLight-MIB", "localSlotIndex")
)
if mibBuilder.loadTexts:
    localCardRemovedTrap.setStatus(
        ""
    )

localUserPort2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 45)
)
localUserPort2Trap.setObjects(
      *(("CityLight-MIB", "localSlotIndex"),
        ("CityLight-MIB", "ifaceUserPort2State"))
)
if mibBuilder.loadTexts:
    localUserPort2Trap.setStatus(
        ""
    )

localFibreATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 46)
)
localFibreATrap.setObjects(
      *(("CityLight-MIB", "localSlotIndex"),
        ("CityLight-MIB", "ifaceFiberPortState"))
)
if mibBuilder.loadTexts:
    localFibreATrap.setStatus(
        ""
    )

localFibreBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 47)
)
localFibreBTrap.setObjects(
      *(("CityLight-MIB", "localSlotIndex"),
        ("CityLight-MIB", "ifaceFiberPortBState"))
)
if mibBuilder.loadTexts:
    localFibreBTrap.setStatus(
        ""
    )

remoteUserRxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 50)
)
remoteUserRxTrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "remoteIfaceUserPortState"))
)
if mibBuilder.loadTexts:
    remoteUserRxTrap.setStatus(
        ""
    )

remotePsuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 51)
)
remotePsuTrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "remoteIfacePSUStatus"))
)
if mibBuilder.loadTexts:
    remotePsuTrap.setStatus(
        ""
    )

remoteTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 52)
)
remoteTempTrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "remoteIfaceTempStatus"))
)
if mibBuilder.loadTexts:
    remoteTempTrap.setStatus(
        ""
    )

remoteFanFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 53)
)
remoteFanFailTrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "remoteIfaceFanStatus"))
)
if mibBuilder.loadTexts:
    remoteFanFailTrap.setStatus(
        ""
    )

remoteEOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 54)
)
remoteEOLTrap.setObjects(
    ("CityLight-MIB", "remoteSlotIndex")
)
if mibBuilder.loadTexts:
    remoteEOLTrap.setStatus(
        ""
    )

remoteFibreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 55)
)
remoteFibreTrap.setObjects(
      *(("CityLight-MIB", "localSlotIndex"),
        ("CityLight-MIB", "remoteIfaceFiberPortState"))
)
if mibBuilder.loadTexts:
    remoteFibreTrap.setStatus(
        ""
    )

remoteUser2RxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 56)
)
remoteUser2RxTrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "remoteIfaceUserPort2State"))
)
if mibBuilder.loadTexts:
    remoteUser2RxTrap.setStatus(
        ""
    )

remoteFibreATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 57)
)
remoteFibreATrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "ifaceFiberPortState"))
)
if mibBuilder.loadTexts:
    remoteFibreATrap.setStatus(
        ""
    )

remoteFibreBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 58)
)
remoteFibreBTrap.setObjects(
      *(("CityLight-MIB", "remoteSlotIndex"),
        ("CityLight-MIB", "ifaceFiberPortBState"))
)
if mibBuilder.loadTexts:
    remoteFibreBTrap.setStatus(
        ""
    )

systemPsuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 60)
)
systemPsuTrap.setObjects(
    ("CityLight-MIB", "cLIGHTSystemPSUState")
)
if mibBuilder.loadTexts:
    systemPsuTrap.setStatus(
        ""
    )

systemTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 61)
)
systemTempTrap.setObjects(
    ("CityLight-MIB", "cLIGHTSystemTemperature")
)
if mibBuilder.loadTexts:
    systemTempTrap.setStatus(
        ""
    )

systemFanFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1671, 0, 62)
)
systemFanFailTrap.setObjects(
    ("CityLight-MIB", "cLIGHTSystemFanState")
)
if mibBuilder.loadTexts:
    systemFanFailTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CityLight-MIB",
    **{"enterprises": enterprises,
       "adva": adva,
       "localFibreRxTrap": localFibreRxTrap,
       "localUserPortTrap": localUserPortTrap,
       "localEOLTrap": localEOLTrap,
       "localCardRemovedTrap": localCardRemovedTrap,
       "localUserPort2Trap": localUserPort2Trap,
       "localFibreATrap": localFibreATrap,
       "localFibreBTrap": localFibreBTrap,
       "remoteUserRxTrap": remoteUserRxTrap,
       "remotePsuTrap": remotePsuTrap,
       "remoteTempTrap": remoteTempTrap,
       "remoteFanFailTrap": remoteFanFailTrap,
       "remoteEOLTrap": remoteEOLTrap,
       "remoteFibreTrap": remoteFibreTrap,
       "remoteUser2RxTrap": remoteUser2RxTrap,
       "remoteFibreATrap": remoteFibreATrap,
       "remoteFibreBTrap": remoteFibreBTrap,
       "systemPsuTrap": systemPsuTrap,
       "systemTempTrap": systemTempTrap,
       "systemFanFailTrap": systemFanFailTrap,
       "cityLight": cityLight,
       "cityLightSystem": cityLightSystem,
       "cLIGHTSystemSerialNumber": cLIGHTSystemSerialNumber,
       "cLIGHTSystemReset": cLIGHTSystemReset,
       "cLIGHTSystemHWVersion": cLIGHTSystemHWVersion,
       "cLIGHTSystemFWVersion": cLIGHTSystemFWVersion,
       "cLIGHTSystemConfiguration": cLIGHTSystemConfiguration,
       "cLIGHTSystemPSUState": cLIGHTSystemPSUState,
       "cLIGHTSystemTemperature": cLIGHTSystemTemperature,
       "cLIGHTSystemFanState": cLIGHTSystemFanState,
       "cLIGHTSystemLocation": cLIGHTSystemLocation,
       "cLIGHTSystemLanSpeed": cLIGHTSystemLanSpeed,
       "cLIGHTGlobalTrapTable": cLIGHTGlobalTrapTable,
       "globalRecipientEntry": globalRecipientEntry,
       "recipientIndex": recipientIndex,
       "globalRecipientAddr": globalRecipientAddr,
       "globalRecipientDescr": globalRecipientDescr,
       "cLIGHTSlotTrapTable": cLIGHTSlotTrapTable,
       "slotRecipientEntry": slotRecipientEntry,
       "slotIndex": slotIndex,
       "slotRecipientAddr": slotRecipientAddr,
       "slotRecipientDescr": slotRecipientDescr,
       "localInterfaceDescr": localInterfaceDescr,
       "cLIGHTLocalInterfaceTable": cLIGHTLocalInterfaceTable,
       "ifaceDescription": ifaceDescription,
       "localSlotIndex": localSlotIndex,
       "interfaceType": interfaceType,
       "ifaceFiberPortState": ifaceFiberPortState,
       "ifaceUserPortState": ifaceUserPortState,
       "ifaceLANdata": ifaceLANdata,
       "ifaceVersion": ifaceVersion,
       "ifacePSUStatus": ifacePSUStatus,
       "ifaceTemperature": ifaceTemperature,
       "ifaceSerialNumber": ifaceSerialNumber,
       "ifaceLanSpeed": ifaceLanSpeed,
       "ifaceUserPort2State": ifaceUserPort2State,
       "ifaceFiberPortBState": ifaceFiberPortBState,
       "ifaceSystemConnectorType": ifaceSystemConnectorType,
       "ifaceSystemFibreType": ifaceSystemFibreType,
       "ifaceSystemLaserType": ifaceSystemLaserType,
       "ifaceSystemLaserRange": ifaceSystemLaserRange,
       "ifaceSystemWavelength": ifaceSystemWavelength,
       "ifaceUserPortConnectorType": ifaceUserPortConnectorType,
       "ifaceUserPortFibreType": ifaceUserPortFibreType,
       "ifaceUserPortLaserType": ifaceUserPortLaserType,
       "ifaceUserPortLaserRange": ifaceUserPortLaserRange,
       "ifaceUserPortWavelength": ifaceUserPortWavelength,
       "ifaceUserPort2ConnectorType": ifaceUserPort2ConnectorType,
       "ifaceUserPort2FibreType": ifaceUserPort2FibreType,
       "ifaceUserPort2LaserType": ifaceUserPort2LaserType,
       "ifaceUserPort2LaserRange": ifaceUserPort2LaserRange,
       "ifaceUserPort2Wavelength": ifaceUserPort2Wavelength,
       "remoteInterfaceDescr": remoteInterfaceDescr,
       "cLIGHTRemoteInterfaceTable": cLIGHTRemoteInterfaceTable,
       "remoteIfaceDescription": remoteIfaceDescription,
       "remoteSlotIndex": remoteSlotIndex,
       "remoteIfaceType": remoteIfaceType,
       "remoteIfaceFiberPortState": remoteIfaceFiberPortState,
       "remoteIfaceUserPortState": remoteIfaceUserPortState,
       "remoteIfaceLANdata": remoteIfaceLANdata,
       "remoteIfaceVersion": remoteIfaceVersion,
       "remoteIfaceLocation": remoteIfaceLocation,
       "remoteIfacePSUStatus": remoteIfacePSUStatus,
       "remoteIfaceTemperature": remoteIfaceTemperature,
       "remoteIfaceFanStatus": remoteIfaceFanStatus,
       "remoteIfaceTempStatus": remoteIfaceTempStatus,
       "remoteIfaceSerialNumber": remoteIfaceSerialNumber,
       "remoteIfaceUserPort2State": remoteIfaceUserPort2State,
       "remoteIfaceFiberPortBState": remoteIfaceFiberPortBState,
       "remoteIfaceSystemConnectorType": remoteIfaceSystemConnectorType,
       "remoteIfaceSystemFibreType": remoteIfaceSystemFibreType,
       "remoteIfaceSystemLaserType": remoteIfaceSystemLaserType,
       "remoteIfaceSystemLaserRange": remoteIfaceSystemLaserRange,
       "remoteIfaceSystemWavelength": remoteIfaceSystemWavelength,
       "remoteIfaceUserPortConnectorType": remoteIfaceUserPortConnectorType,
       "remoteIfaceUserPortFibreType": remoteIfaceUserPortFibreType,
       "remoteIfaceUserPortLaserType": remoteIfaceUserPortLaserType,
       "remoteIfaceUserPortLaserRange": remoteIfaceUserPortLaserRange,
       "remoteIfaceUserPortWavelength": remoteIfaceUserPortWavelength,
       "remoteIfaceUserPort2ConnectorType": remoteIfaceUserPort2ConnectorType,
       "remoteIfaceUserPort2FibreType": remoteIfaceUserPort2FibreType,
       "remoteIfaceUserPort2LaserType": remoteIfaceUserPort2LaserType,
       "remoteIfaceUserPort2LaserRange": remoteIfaceUserPort2LaserRange,
       "remoteIfaceUserPort2Wavelength": remoteIfaceUserPort2Wavelength,
       "trapEnable": trapEnable,
       "teSystemPSUState": teSystemPSUState,
       "teSystemTempState": teSystemTempState,
       "teSystemFanFailState": teSystemFanFailState,
       "teSystemAuthentication": teSystemAuthentication,
       "teSlotTrapTable": teSlotTrapTable,
       "clSlotTrapEntry": clSlotTrapEntry,
       "teSlotIndex": teSlotIndex,
       "teLocalFibreRxWrap": teLocalFibreRxWrap,
       "teRemoteFaultWrap": teRemoteFaultWrap,
       "teLocalUserPortWrap": teLocalUserPortWrap,
       "teRemoteUserPortWrap": teRemoteUserPortWrap,
       "teRemotePSUWrap": teRemotePSUWrap,
       "teRemoteTempWrap": teRemoteTempWrap,
       "teRemoteFanFailWrap": teRemoteFanFailWrap,
       "security": security,
       "securityUserTable": securityUserTable,
       "securityUserEntry": securityUserEntry,
       "securityAccountIndex": securityAccountIndex,
       "securityUserName": securityUserName,
       "securityUserAccessLevel": securityUserAccessLevel,
       "securityUserPassword": securityUserPassword,
       "securityAccountStatus": securityAccountStatus,
       "trapLog": trapLog,
       "cLightTrapLog": cLightTrapLog,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "destination": destination,
       "timeStamp": timeStamp,
       "description": description,
       "parameter1": parameter1,
       "parameter2": parameter2}
)
