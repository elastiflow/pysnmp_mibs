# SNMP MIB module (CEM-CN1000-HARDWARE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-HARDWARE.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnCN1000HardwareModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 8)
)
if mibBuilder.loadTexts:
    cnCN1000HardwareModule.setRevisions(
        ("2001-10-23 15:42",
         "2002-11-06 10:22",
         "2003-02-24 03:30",
         "2003-02-26 06:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000ShelfType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cn1000MainShelfType", 1),
          ("cn1000ExpansionShelfType", 2),
          ("cn1000AlarmTestShelfType", 3),
          ("cn1000TalkBatteryShelfType", 4),
          ("cn1000FanAssemblyShelfType", 5),
          ("cn1000AirFilterShelfType", 6),
          ("cn1000SpecialShelfType", 7),
          ("cn1000RemoteONUShelfType", 8),
          ("cn1000PONShelfType", 9))
    )



class Cn1000HWProvisionedCardType(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11,
              12,
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
              9999)
        )
    )
    namedValues = NamedValues(
        *(("cn1000HWCECard", 0),
          ("cn1000HWT1Card", 1),
          ("cn1000HWOC3WanCardEnhancedShorthaul", 2),
          ("cn1000HWOC3WanCardEnhancedLonghaul", 3),
          ("cn1000HWOC3WanCardShorthaul", 4),
          ("cn1000HWOC3WanCardLonghaul", 5),
          ("cn1000HWAdslLineCard", 6),
          ("cn1000HWAlarmInterfaceCard", 7),
          ("cn1000HWOpticalLineCard", 9),
          ("cn1000HWFeatureCard", 10),
          ("cn1000HWOpticalInterfaceCard", 11),
          ("cn1000HWCatenaChannelUnitCard", 12),
          ("cn1000HWOC12WanCard", 14),
          ("cn1000HWDS3WanCard", 15),
          ("cn1000HWMetallicTestCard", 16),
          ("cn1000HWFan", 17),
          ("cn1000HWTalkBatteryFilter", 18),
          ("cn1000HWONUPowerUnit", 19),
          ("cn1000HWAlarmTestFeederCard", 20),
          ("cn1000HWCoinChannelUnitCard", 21),
          ("cn1000HWIsdnChannelUnitCard", 22),
          ("cn1000HWDdsChannelUnitCard", 23),
          ("cn1000HWDidChannelUnitCard", 24),
          ("cn1000HWEspotsFeedChannelUnitCard", 25),
          ("cn1000HWEspotsSinkChannelUnitCard", 26),
          ("cn1000HwFourWire0ChannelUnitCard", 27),
          ("cn1000HwIsdnNullChannelUnitCard", 28),
          ("cn1000HwDigitalBypassChannelUnitCard", 29),
          ("cn1000HwEbsChannelUnitCard", 30),
          ("cn1000HwDcAlarmChannelUnitCard", 31),
          ("cn1000HwSpotsChannelUnitCard", 32),
          ("cn1000HwPlarChannelUnitCard", 33),
          ("cn1000HwPotsChannelUnit", 34),
          ("cn1000HwOpticalLineTermination", 35),
          ("cn1000HwOpticalNetworkTermination", 36),
          ("cn1000HWE1Card", 37),
          ("cn1000HWNoCardProvisioned", 9999))
    )



class Cn1000HWInstalledCardType(TextualConvention, Integer32):
    status = "current"
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
              40,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("cn1000HWCECard", 0),
          ("cn1000HWT1Card", 1),
          ("cn1000HWOC3WanCardEnhancedShorthaul", 2),
          ("cn1000HWOC3WanCardEnhancedLonghaul", 3),
          ("cn1000HWOC3WanCardShorthaul", 4),
          ("cn1000HWOC3WanCardLonghaul", 5),
          ("cn1000HWAdslLineCard", 6),
          ("cn1000HWAlarmInterfaceCard", 7),
          ("cn1000HWHydraLineCard", 8),
          ("cn1000HWOpticalLineCard", 9),
          ("cn1000HWFeatureCard", 10),
          ("cn1000HWOpticalInterfaceCard", 11),
          ("cn1000HWCatenaChannelUnitCard", 12),
          ("cn1000HWLegacyChannelUnitCard", 13),
          ("cn1000HWOC12WanCard", 14),
          ("cn1000HWDS3WanCard", 15),
          ("cn1000HWMetallicTestCard", 16),
          ("cn1000HWFan", 17),
          ("cn1000HWTalkBatteryFilter", 18),
          ("cn1000HWONUPowerUnit", 19),
          ("cn1000HWAlarmTestFeederCard", 20),
          ("cn1000HWCoinChannelUnitCard", 21),
          ("cn1000HWsdnChannelUnitCard", 22),
          ("cn1000HWDdsChannelUnitCard", 23),
          ("cn1000HWDidChannelUnitCard", 24),
          ("cn1000HWEspotsFeedChannelUnitCard", 25),
          ("cn1000HWEspotsSinkChannelUnitCard", 26),
          ("cn1000HWFourWire0ChannelUnitCard", 27),
          ("cn1000HWIsdnNullChannelUnitCard", 28),
          ("cn1000HWDigitalBypassChannelUnitCard", 29),
          ("cn1000HWEbsChannelUnitCard", 30),
          ("cn1000HWDcAlarmChannelUnitCard", 31),
          ("cn1000HWSpotsChannelUnitCard", 32),
          ("cn1000HWPlarChannelUnitCard", 33),
          ("cn1000HWPotsChannelUnit", 34),
          ("cn1000HWOpticalLineTermination", 35),
          ("cn1000HWOpticalNetworkTermination", 36),
          ("cn1000HWE1Card", 37),
          ("cn1000HWDSLOnlyLineCard", 40),
          ("cn1000HWNoCardPresent", 9999))
    )



class Cn1000HWLedType(TextualConvention, Integer32):
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
        *(("mTCLED", 1),
          ("statusLED", 2),
          ("activityLED", 3),
          ("linkLED", 4),
          ("maxLEDType", 5))
    )



class Cn1000HWLedColourType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ledOff", 0),
          ("ledFlashing", 1),
          ("ledOn", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000ShelfTable_Object = MibTable
cn1000ShelfTable = _Cn1000ShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1)
)
if mibBuilder.loadTexts:
    cn1000ShelfTable.setStatus("current")
_Cn1000ShelfEntry_Object = MibTableRow
cn1000ShelfEntry = _Cn1000ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1)
)
cn1000ShelfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cn1000ShelfEntry.setStatus("current")


class _Cn1000HWShelfName_Type(OctetString):
    """Custom type cn1000HWShelfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cn1000HWShelfName_Type.__name__ = "OctetString"
_Cn1000HWShelfName_Object = MibTableColumn
cn1000HWShelfName = _Cn1000HWShelfName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 1),
    _Cn1000HWShelfName_Type()
)
cn1000HWShelfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000HWShelfName.setStatus("current")
_Cn100ShelfTableRowStatus_Type = RowStatus
_Cn100ShelfTableRowStatus_Object = MibTableColumn
cn100ShelfTableRowStatus = _Cn100ShelfTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 2),
    _Cn100ShelfTableRowStatus_Type()
)
cn100ShelfTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn100ShelfTableRowStatus.setStatus("current")
_Cn1000ShelfNumber_Type = PhysicalIndex
_Cn1000ShelfNumber_Object = MibTableColumn
cn1000ShelfNumber = _Cn1000ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 3),
    _Cn1000ShelfNumber_Type()
)
cn1000ShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000ShelfNumber.setStatus("current")
_Cn1000ShelfType_Type = Cn1000ShelfType
_Cn1000ShelfType_Object = MibTableColumn
cn1000ShelfType = _Cn1000ShelfType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 4),
    _Cn1000ShelfType_Type()
)
cn1000ShelfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000ShelfType.setStatus("current")
_Cn1000AssociatedPortShelf_Type = Integer32
_Cn1000AssociatedPortShelf_Object = MibTableColumn
cn1000AssociatedPortShelf = _Cn1000AssociatedPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 5),
    _Cn1000AssociatedPortShelf_Type()
)
cn1000AssociatedPortShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000AssociatedPortShelf.setStatus("current")
_Cn1000AssociatedPortSlotOrSlotGroup_Type = CnSlotGroupNameType
_Cn1000AssociatedPortSlotOrSlotGroup_Object = MibTableColumn
cn1000AssociatedPortSlotOrSlotGroup = _Cn1000AssociatedPortSlotOrSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 6),
    _Cn1000AssociatedPortSlotOrSlotGroup_Type()
)
cn1000AssociatedPortSlotOrSlotGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000AssociatedPortSlotOrSlotGroup.setStatus("current")
_Cn1000AssociatedPortPort_Type = Integer32
_Cn1000AssociatedPortPort_Object = MibTableColumn
cn1000AssociatedPortPort = _Cn1000AssociatedPortPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 7),
    _Cn1000AssociatedPortPort_Type()
)
cn1000AssociatedPortPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000AssociatedPortPort.setStatus("current")


class _Cn1000ShelfF2Cable_Type(Integer32):
    """Custom type cn1000ShelfF2Cable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000ShelfF2Cable_Type.__name__ = "Integer32"
_Cn1000ShelfF2Cable_Object = MibTableColumn
cn1000ShelfF2Cable = _Cn1000ShelfF2Cable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 8),
    _Cn1000ShelfF2Cable_Type()
)
cn1000ShelfF2Cable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000ShelfF2Cable.setStatus("current")


class _Cn1000ShelfF2PairRangeStart_Type(Integer32):
    """Custom type cn1000ShelfF2PairRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000ShelfF2PairRangeStart_Type.__name__ = "Integer32"
_Cn1000ShelfF2PairRangeStart_Object = MibTableColumn
cn1000ShelfF2PairRangeStart = _Cn1000ShelfF2PairRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 9),
    _Cn1000ShelfF2PairRangeStart_Type()
)
cn1000ShelfF2PairRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000ShelfF2PairRangeStart.setStatus("current")


class _Cn1000ShelfF2PairRangeEnd_Type(Integer32):
    """Custom type cn1000ShelfF2PairRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000ShelfF2PairRangeEnd_Type.__name__ = "Integer32"
_Cn1000ShelfF2PairRangeEnd_Object = MibTableColumn
cn1000ShelfF2PairRangeEnd = _Cn1000ShelfF2PairRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 10),
    _Cn1000ShelfF2PairRangeEnd_Type()
)
cn1000ShelfF2PairRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000ShelfF2PairRangeEnd.setStatus("current")


class _Cn1000ShelfShelfId_Type(OctetString):
    """Custom type cn1000ShelfShelfId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_Cn1000ShelfShelfId_Type.__name__ = "OctetString"
_Cn1000ShelfShelfId_Object = MibTableColumn
cn1000ShelfShelfId = _Cn1000ShelfShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 1, 1, 11),
    _Cn1000ShelfShelfId_Type()
)
cn1000ShelfShelfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000ShelfShelfId.setStatus("current")
_Cn1000SlotTable_Object = MibTable
cn1000SlotTable = _Cn1000SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2)
)
if mibBuilder.loadTexts:
    cn1000SlotTable.setStatus("current")
_Cn1000SlotEntry_Object = MibTableRow
cn1000SlotEntry = _Cn1000SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1)
)
cn1000SlotEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cn1000SlotEntry.setStatus("current")


class _Cn1000HWCardType_Type(Cn1000HWProvisionedCardType):
    """Custom type cn1000HWCardType based on Cn1000HWProvisionedCardType"""
    defaultValue = 9999


_Cn1000HWCardType_Type.__name__ = "Cn1000HWProvisionedCardType"
_Cn1000HWCardType_Object = MibTableColumn
cn1000HWCardType = _Cn1000HWCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 1),
    _Cn1000HWCardType_Type()
)
cn1000HWCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000HWCardType.setStatus("current")


class _Cn1000HWCardStatus_Type(Integer32):
    """Custom type cn1000HWCardStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cn1000HWNotPresent", 1),
          ("cn1000HWUp", 2),
          ("cn1000HWDown", 3),
          ("cn1000HWValidationFailed", 4),
          ("cn1000HWUnknownCardInstalled", 5),
          ("cn1000HWUnprovisionedCardInserted", 6),
          ("cn1000HWConfigurationMismatch", 7),
          ("cn1000HWNotProvisioned", 8),
          ("cn1000HWTesting", 9))
    )


_Cn1000HWCardStatus_Type.__name__ = "Integer32"
_Cn1000HWCardStatus_Object = MibTableColumn
cn1000HWCardStatus = _Cn1000HWCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 2),
    _Cn1000HWCardStatus_Type()
)
cn1000HWCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000HWCardStatus.setStatus("current")
_Cn1000HWLastStatusChange_Type = TimeTicks
_Cn1000HWLastStatusChange_Object = MibTableColumn
cn1000HWLastStatusChange = _Cn1000HWLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 3),
    _Cn1000HWLastStatusChange_Type()
)
cn1000HWLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000HWLastStatusChange.setStatus("current")
_Cn1000HWShelfNumber_Type = Integer32
_Cn1000HWShelfNumber_Object = MibTableColumn
cn1000HWShelfNumber = _Cn1000HWShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 4),
    _Cn1000HWShelfNumber_Type()
)
cn1000HWShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000HWShelfNumber.setStatus("current")
_Cn1000HWSlotNumber_Type = Integer32
_Cn1000HWSlotNumber_Object = MibTableColumn
cn1000HWSlotNumber = _Cn1000HWSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 5),
    _Cn1000HWSlotNumber_Type()
)
cn1000HWSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000HWSlotNumber.setStatus("current")


class _Cn1000HWSerialNumber_Type(OctetString):
    """Custom type cn1000HWSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cn1000HWSerialNumber_Type.__name__ = "OctetString"
_Cn1000HWSerialNumber_Object = MibTableColumn
cn1000HWSerialNumber = _Cn1000HWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 6),
    _Cn1000HWSerialNumber_Type()
)
cn1000HWSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000HWSerialNumber.setStatus("current")


class _Cn1000HWHardwareVersion_Type(OctetString):
    """Custom type cn1000HWHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cn1000HWHardwareVersion_Type.__name__ = "OctetString"
_Cn1000HWHardwareVersion_Object = MibTableColumn
cn1000HWHardwareVersion = _Cn1000HWHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 7),
    _Cn1000HWHardwareVersion_Type()
)
cn1000HWHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000HWHardwareVersion.setStatus("current")


class _Cn1000HWSoftwareVersion_Type(OctetString):
    """Custom type cn1000HWSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cn1000HWSoftwareVersion_Type.__name__ = "OctetString"
_Cn1000HWSoftwareVersion_Object = MibTableColumn
cn1000HWSoftwareVersion = _Cn1000HWSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 8),
    _Cn1000HWSoftwareVersion_Type()
)
cn1000HWSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000HWSoftwareVersion.setStatus("current")


class _Cn1000HWProductCode_Type(OctetString):
    """Custom type cn1000HWProductCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cn1000HWProductCode_Type.__name__ = "OctetString"
_Cn1000HWProductCode_Object = MibTableColumn
cn1000HWProductCode = _Cn1000HWProductCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 9),
    _Cn1000HWProductCode_Type()
)
cn1000HWProductCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000HWProductCode.setStatus("current")


class _Cn1000HWCleiCode_Type(OctetString):
    """Custom type cn1000HWCleiCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cn1000HWCleiCode_Type.__name__ = "OctetString"
_Cn1000HWCleiCode_Object = MibTableColumn
cn1000HWCleiCode = _Cn1000HWCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 10),
    _Cn1000HWCleiCode_Type()
)
cn1000HWCleiCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000HWCleiCode.setStatus("current")
_Cn1000HWInstalledCardType_Type = Cn1000HWInstalledCardType
_Cn1000HWInstalledCardType_Object = MibTableColumn
cn1000HWInstalledCardType = _Cn1000HWInstalledCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 11),
    _Cn1000HWInstalledCardType_Type()
)
cn1000HWInstalledCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000HWInstalledCardType.setStatus("current")
_Cn1000SlotDiagnoticsEnabled_Type = TruthValue
_Cn1000SlotDiagnoticsEnabled_Object = MibTableColumn
cn1000SlotDiagnoticsEnabled = _Cn1000SlotDiagnoticsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 2, 1, 12),
    _Cn1000SlotDiagnoticsEnabled_Type()
)
cn1000SlotDiagnoticsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000SlotDiagnoticsEnabled.setStatus("current")
_Cn1000CardLedTable_Object = MibTable
cn1000CardLedTable = _Cn1000CardLedTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3)
)
if mibBuilder.loadTexts:
    cn1000CardLedTable.setStatus("current")
_Cn1000CardLedEntry_Object = MibTableRow
cn1000CardLedEntry = _Cn1000CardLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1)
)
cn1000CardLedEntry.setIndexNames(
    (0, "CEM-CN1000-HARDWARE", "cn1000CardLedShelfNumber"),
    (0, "CEM-CN1000-HARDWARE", "cn1000CardLedSlotNumber"),
)
if mibBuilder.loadTexts:
    cn1000CardLedEntry.setStatus("current")


class _Cn1000CardLedShelfNumber_Type(Integer32):
    """Custom type cn1000CardLedShelfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cn1000CardLedShelfNumber_Type.__name__ = "Integer32"
_Cn1000CardLedShelfNumber_Object = MibTableColumn
cn1000CardLedShelfNumber = _Cn1000CardLedShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1, 1),
    _Cn1000CardLedShelfNumber_Type()
)
cn1000CardLedShelfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000CardLedShelfNumber.setStatus("current")


class _Cn1000CardLedSlotNumber_Type(Integer32):
    """Custom type cn1000CardLedSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cn1000CardLedSlotNumber_Type.__name__ = "Integer32"
_Cn1000CardLedSlotNumber_Object = MibTableColumn
cn1000CardLedSlotNumber = _Cn1000CardLedSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1, 2),
    _Cn1000CardLedSlotNumber_Type()
)
cn1000CardLedSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000CardLedSlotNumber.setStatus("current")
_Cn1000CardLedCardType_Type = Cn1000HWInstalledCardType
_Cn1000CardLedCardType_Object = MibTableColumn
cn1000CardLedCardType = _Cn1000CardLedCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1, 3),
    _Cn1000CardLedCardType_Type()
)
cn1000CardLedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000CardLedCardType.setStatus("current")
_Cn1000CardLedType_Type = Cn1000HWLedType
_Cn1000CardLedType_Object = MibTableColumn
cn1000CardLedType = _Cn1000CardLedType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1, 4),
    _Cn1000CardLedType_Type()
)
cn1000CardLedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000CardLedType.setStatus("deprecated")
_Cn1000CardLedState_Type = Cn1000HWLedColourType
_Cn1000CardLedState_Object = MibTableColumn
cn1000CardLedState = _Cn1000CardLedState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1, 5),
    _Cn1000CardLedState_Type()
)
cn1000CardLedState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000CardLedState.setStatus("current")
_Cn1000CardLedFlash_Type = TruthValue
_Cn1000CardLedFlash_Object = MibTableColumn
cn1000CardLedFlash = _Cn1000CardLedFlash_Object(
    (1, 3, 6, 1, 4, 1, 6352, 8, 3, 1, 6),
    _Cn1000CardLedFlash_Type()
)
cn1000CardLedFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000CardLedFlash.setStatus("deprecated")
_Cn100010HWGroups_ObjectIdentity = ObjectIdentity
cn100010HWGroups = _Cn100010HWGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 8, 4)
)

# Managed Objects groups

cn100010HWObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 8, 4, 1)
)
cn100010HWObjectGroup.setObjects(
      *(("CEM-CN1000-HARDWARE", "cn1000HWShelfName"),
        ("CEM-CN1000-HARDWARE", "cn100ShelfTableRowStatus"),
        ("CEM-CN1000-HARDWARE", "cn1000ShelfNumber"),
        ("CEM-CN1000-HARDWARE", "cn1000HWCardType"),
        ("CEM-CN1000-HARDWARE", "cn1000HWCardStatus"),
        ("CEM-CN1000-HARDWARE", "cn1000HWLastStatusChange"),
        ("CEM-CN1000-HARDWARE", "cn1000HWShelfNumber"),
        ("CEM-CN1000-HARDWARE", "cn1000HWSlotNumber"),
        ("CEM-CN1000-HARDWARE", "cn1000HWSerialNumber"),
        ("CEM-CN1000-HARDWARE", "cn1000HWHardwareVersion"),
        ("CEM-CN1000-HARDWARE", "cn1000HWProductCode"),
        ("CEM-CN1000-HARDWARE", "cn1000HWCleiCode"),
        ("CEM-CN1000-HARDWARE", "cn1000HWSoftwareVersion"),
        ("CEM-CN1000-HARDWARE", "cn1000HWInstalledCardType"),
        ("CEM-CN1000-HARDWARE", "cn1000CardLedCardType"),
        ("CEM-CN1000-HARDWARE", "cn1000CardLedState"),
        ("CEM-CN1000-HARDWARE", "cn1000ShelfF2Cable"),
        ("CEM-CN1000-HARDWARE", "cn1000ShelfF2PairRangeStart"),
        ("CEM-CN1000-HARDWARE", "cn1000ShelfF2PairRangeEnd"),
        ("CEM-CN1000-HARDWARE", "cn1000ShelfShelfId"),
        ("CEM-CN1000-HARDWARE", "cn1000ShelfType"),
        ("CEM-CN1000-HARDWARE", "cn1000AssociatedPortShelf"),
        ("CEM-CN1000-HARDWARE", "cn1000AssociatedPortPort"),
        ("CEM-CN1000-HARDWARE", "cn1000SlotDiagnoticsEnabled"),
        ("CEM-CN1000-HARDWARE", "cn1000AssociatedPortSlotOrSlotGroup"))
)
if mibBuilder.loadTexts:
    cn100010HWObjectGroup.setStatus("current")

cn100010HWDepcratedObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 8, 4, 2)
)
cn100010HWDepcratedObjects.setObjects(
      *(("CEM-CN1000-HARDWARE", "cn1000CardLedFlash"),
        ("CEM-CN1000-HARDWARE", "cn1000CardLedType"))
)
if mibBuilder.loadTexts:
    cn100010HWDepcratedObjects.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-HARDWARE",
    **{"Cn1000ShelfType": Cn1000ShelfType,
       "Cn1000HWProvisionedCardType": Cn1000HWProvisionedCardType,
       "Cn1000HWInstalledCardType": Cn1000HWInstalledCardType,
       "Cn1000HWLedType": Cn1000HWLedType,
       "Cn1000HWLedColourType": Cn1000HWLedColourType,
       "cnCN1000HardwareModule": cnCN1000HardwareModule,
       "cn1000ShelfTable": cn1000ShelfTable,
       "cn1000ShelfEntry": cn1000ShelfEntry,
       "cn1000HWShelfName": cn1000HWShelfName,
       "cn100ShelfTableRowStatus": cn100ShelfTableRowStatus,
       "cn1000ShelfNumber": cn1000ShelfNumber,
       "cn1000ShelfType": cn1000ShelfType,
       "cn1000AssociatedPortShelf": cn1000AssociatedPortShelf,
       "cn1000AssociatedPortSlotOrSlotGroup": cn1000AssociatedPortSlotOrSlotGroup,
       "cn1000AssociatedPortPort": cn1000AssociatedPortPort,
       "cn1000ShelfF2Cable": cn1000ShelfF2Cable,
       "cn1000ShelfF2PairRangeStart": cn1000ShelfF2PairRangeStart,
       "cn1000ShelfF2PairRangeEnd": cn1000ShelfF2PairRangeEnd,
       "cn1000ShelfShelfId": cn1000ShelfShelfId,
       "cn1000SlotTable": cn1000SlotTable,
       "cn1000SlotEntry": cn1000SlotEntry,
       "cn1000HWCardType": cn1000HWCardType,
       "cn1000HWCardStatus": cn1000HWCardStatus,
       "cn1000HWLastStatusChange": cn1000HWLastStatusChange,
       "cn1000HWShelfNumber": cn1000HWShelfNumber,
       "cn1000HWSlotNumber": cn1000HWSlotNumber,
       "cn1000HWSerialNumber": cn1000HWSerialNumber,
       "cn1000HWHardwareVersion": cn1000HWHardwareVersion,
       "cn1000HWSoftwareVersion": cn1000HWSoftwareVersion,
       "cn1000HWProductCode": cn1000HWProductCode,
       "cn1000HWCleiCode": cn1000HWCleiCode,
       "cn1000HWInstalledCardType": cn1000HWInstalledCardType,
       "cn1000SlotDiagnoticsEnabled": cn1000SlotDiagnoticsEnabled,
       "cn1000CardLedTable": cn1000CardLedTable,
       "cn1000CardLedEntry": cn1000CardLedEntry,
       "cn1000CardLedShelfNumber": cn1000CardLedShelfNumber,
       "cn1000CardLedSlotNumber": cn1000CardLedSlotNumber,
       "cn1000CardLedCardType": cn1000CardLedCardType,
       "cn1000CardLedType": cn1000CardLedType,
       "cn1000CardLedState": cn1000CardLedState,
       "cn1000CardLedFlash": cn1000CardLedFlash,
       "cn100010HWGroups": cn100010HWGroups,
       "cn100010HWObjectGroup": cn100010HWObjectGroup,
       "cn100010HWDepcratedObjects": cn100010HWDepcratedObjects}
)
