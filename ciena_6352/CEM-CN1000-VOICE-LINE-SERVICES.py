# SNMP MIB module (CEM-CN1000-VOICE-LINE-SERVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-VOICE-LINE-SERVICES.mib
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

(Cn1000ConfigurationStatus,
 Cn1000LineAppearanceRange,
 Cn1000PortRange,
 Cn1000ShelfRange,
 Cn1000SlotRange,
 cn1000VoiceLineServices) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000ConfigurationStatus",
    "Cn1000LineAppearanceRange",
    "Cn1000PortRange",
    "Cn1000ShelfRange",
    "Cn1000SlotRange",
    "cn1000VoiceLineServices")

(CnGR303LinkSecondaryServiceStateType,) = mibBuilder.importSymbols(
    "CEM-GR303",
    "CnGR303LinkSecondaryServiceStateType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cn1000VoiceLineServicesModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000VoiceLnServAdminState(TextualConvention, Integer32):
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
        *(("undetermined", 0),
          ("down", 1),
          ("up", 2))
    )



class Cn1000SwitchInterfaceGroupType(TextualConvention, Integer32):
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
          ("cnTDM", 1),
          ("cnMGCP", 2),
          ("cnMEGACO", 3),
          ("cnH28", 4))
    )



class Cn1000CodecType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noCodec", 0),
          ("g711M", 1),
          ("g711A", 2),
          ("g726", 3),
          ("g726Sixteen", 4),
          ("g726TwentyFour", 5),
          ("g726ThirtyTwo", 6),
          ("g726Forty", 7),
          ("g729A", 8))
    )



class Cn1000CodecPacketizationPeriodType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30)
        )
    )
    namedValues = NamedValues(
        *(("five", 5),
          ("ten", 10),
          ("fifteen", 15),
          ("twenty", 20),
          ("twentyfive", 25),
          ("thirty", 30))
    )



class Cn1000G726PacketizationRateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              24,
              32,
              40)
        )
    )
    namedValues = NamedValues(
        *(("sixteen", 16),
          ("twentyfour", 24),
          ("thirtytwo", 32),
          ("fourty", 40))
    )



class Cn1000VoiceLnServOperState(TextualConvention, Integer32):
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
        *(("undertermined", 0),
          ("down", 1),
          ("up", 2))
    )



class Cn1000VoiceLnServConnState(TextualConvention, Integer32):
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
        *(("undetermined", 0),
          ("disconnected", 1),
          ("connected", 2))
    )



class Cn1000VoiceLnServSubscriptionConnState(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("disconnected", 1),
          ("setup", 2),
          ("setupPendingTeardown", 3),
          ("pendingRestart", 4),
          ("connectedConfirmingPath", 5),
          ("connected", 6),
          ("connectedPendingModify", 7),
          ("teardown", 8),
          ("teardownPendingSetup", 9),
          ("setupPending", 10),
          ("stalled", 11))
    )



class Cn1000VoiceLnServHookswitchState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("unknown", 1),
          ("onHook", 2),
          ("offHook", 3))
    )



class Cn1000VoiceLGLineOperState(TextualConvention, Integer32):
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
        *(("disconnected", 0),
          ("disabled", 1),
          ("connected", 2),
          ("suspended", 3),
          ("error", 4))
    )



class Cn1000VoiceIpPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000LineGroupReferenceTable_Object = MibTable
cn1000LineGroupReferenceTable = _Cn1000LineGroupReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cn1000LineGroupReferenceTable.setStatus("current")
_Cn1000LineGroupReferenceEntry_Object = MibTableRow
cn1000LineGroupReferenceEntry = _Cn1000LineGroupReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1)
)
cn1000LineGroupReferenceEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIndex"),
)
if mibBuilder.loadTexts:
    cn1000LineGroupReferenceEntry.setStatus("current")


class _Cn1000LineGroupRefIndex_Type(Integer32):
    """Custom type cn1000LineGroupRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000LineGroupRefIndex_Type.__name__ = "Integer32"
_Cn1000LineGroupRefIndex_Object = MibTableColumn
cn1000LineGroupRefIndex = _Cn1000LineGroupRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 1),
    _Cn1000LineGroupRefIndex_Type()
)
cn1000LineGroupRefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineGroupRefIndex.setStatus("current")
_Cn1000LineGroupRefIfGroupIfIndex_Type = InterfaceIndex
_Cn1000LineGroupRefIfGroupIfIndex_Object = MibTableColumn
cn1000LineGroupRefIfGroupIfIndex = _Cn1000LineGroupRefIfGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 2),
    _Cn1000LineGroupRefIfGroupIfIndex_Type()
)
cn1000LineGroupRefIfGroupIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefIfGroupIfIndex.setStatus("deprecated")


class _Cn1000LineGroupRefLineGroupSystemAddress_Type(OctetString):
    """Custom type cn1000LineGroupRefLineGroupSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Cn1000LineGroupRefLineGroupSystemAddress_Type.__name__ = "OctetString"
_Cn1000LineGroupRefLineGroupSystemAddress_Object = MibTableColumn
cn1000LineGroupRefLineGroupSystemAddress = _Cn1000LineGroupRefLineGroupSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 3),
    _Cn1000LineGroupRefLineGroupSystemAddress_Type()
)
cn1000LineGroupRefLineGroupSystemAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefLineGroupSystemAddress.setStatus("current")


class _Cn1000LineGroupRefLineGroupConnectionIndex_Type(Integer32):
    """Custom type cn1000LineGroupRefLineGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Cn1000LineGroupRefLineGroupConnectionIndex_Type.__name__ = "Integer32"
_Cn1000LineGroupRefLineGroupConnectionIndex_Object = MibTableColumn
cn1000LineGroupRefLineGroupConnectionIndex = _Cn1000LineGroupRefLineGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 4),
    _Cn1000LineGroupRefLineGroupConnectionIndex_Type()
)
cn1000LineGroupRefLineGroupConnectionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefLineGroupConnectionIndex.setStatus("current")
_Cn1000LineGroupRefConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000LineGroupRefConfigurationStatus_Object = MibTableColumn
cn1000LineGroupRefConfigurationStatus = _Cn1000LineGroupRefConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 5),
    _Cn1000LineGroupRefConfigurationStatus_Type()
)
cn1000LineGroupRefConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LineGroupRefConfigurationStatus.setStatus("current")


class _Cn1000LineGroupRefMaxRetryDelay_Type(Integer32):
    """Custom type cn1000LineGroupRefMaxRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRefMaxRetryDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRefMaxRetryDelay_Object = MibTableColumn
cn1000LineGroupRefMaxRetryDelay = _Cn1000LineGroupRefMaxRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 6),
    _Cn1000LineGroupRefMaxRetryDelay_Type()
)
cn1000LineGroupRefMaxRetryDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefMaxRetryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cn1000LineGroupRefMaxRetryDelay.setUnits("msec")


class _Cn1000LineGroupRefMaxRoundTripDelay_Type(Integer32):
    """Custom type cn1000LineGroupRefMaxRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRefMaxRoundTripDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRefMaxRoundTripDelay_Object = MibTableColumn
cn1000LineGroupRefMaxRoundTripDelay = _Cn1000LineGroupRefMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 7),
    _Cn1000LineGroupRefMaxRoundTripDelay_Type()
)
cn1000LineGroupRefMaxRoundTripDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cn1000LineGroupRefMaxRoundTripDelay.setUnits("msec")


class _Cn1000LineGroupRefInitialRoundTripDelay_Type(Integer32):
    """Custom type cn1000LineGroupRefInitialRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRefInitialRoundTripDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRefInitialRoundTripDelay_Object = MibTableColumn
cn1000LineGroupRefInitialRoundTripDelay = _Cn1000LineGroupRefInitialRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 8),
    _Cn1000LineGroupRefInitialRoundTripDelay_Type()
)
cn1000LineGroupRefInitialRoundTripDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefInitialRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cn1000LineGroupRefInitialRoundTripDelay.setUnits("msec")


class _Cn1000LineGroupRefPendingTimeout_Type(Integer32):
    """Custom type cn1000LineGroupRefPendingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRefPendingTimeout_Type.__name__ = "Integer32"
_Cn1000LineGroupRefPendingTimeout_Object = MibTableColumn
cn1000LineGroupRefPendingTimeout = _Cn1000LineGroupRefPendingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 9),
    _Cn1000LineGroupRefPendingTimeout_Type()
)
cn1000LineGroupRefPendingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefPendingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cn1000LineGroupRefPendingTimeout.setUnits("msec")
_Cn1000LineGroupRefRowStatus_Type = RowStatus
_Cn1000LineGroupRefRowStatus_Object = MibTableColumn
cn1000LineGroupRefRowStatus = _Cn1000LineGroupRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 10),
    _Cn1000LineGroupRefRowStatus_Type()
)
cn1000LineGroupRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefRowStatus.setStatus("current")
_Cn1000LineGroupRefAdminStatus_Type = Cn1000VoiceLnServAdminState
_Cn1000LineGroupRefAdminStatus_Object = MibTableColumn
cn1000LineGroupRefAdminStatus = _Cn1000LineGroupRefAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 11),
    _Cn1000LineGroupRefAdminStatus_Type()
)
cn1000LineGroupRefAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupRefAdminStatus.setStatus("current")


class _Cn1000LineGroupRefDesc_Type(OctetString):
    """Custom type cn1000LineGroupRefDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cn1000LineGroupRefDesc_Type.__name__ = "OctetString"
_Cn1000LineGroupRefDesc_Object = MibTableColumn
cn1000LineGroupRefDesc = _Cn1000LineGroupRefDesc_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 12),
    _Cn1000LineGroupRefDesc_Type()
)
cn1000LineGroupRefDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefDesc.setStatus("current")


class _Cn1000LineGroupRefIfGroupType_Type(Integer32):
    """Custom type cn1000LineGroupRefIfGroupType based on Integer32"""
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
        *(("cn1000LgrGR303", 1),
          ("cn1000LgrTR08", 2),
          ("cn1000LgrSLC5COT", 3),
          ("cn1000LgrDAX", 4),
          ("cn1000LgrV5", 5))
    )


_Cn1000LineGroupRefIfGroupType_Type.__name__ = "Integer32"
_Cn1000LineGroupRefIfGroupType_Object = MibTableColumn
cn1000LineGroupRefIfGroupType = _Cn1000LineGroupRefIfGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 13),
    _Cn1000LineGroupRefIfGroupType_Type()
)
cn1000LineGroupRefIfGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefIfGroupType.setStatus("current")


class _Cn1000LineGroupRefIfGroupShelf_Type(Integer32):
    """Custom type cn1000LineGroupRefIfGroupShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cn1000LineGroupRefIfGroupShelf_Type.__name__ = "Integer32"
_Cn1000LineGroupRefIfGroupShelf_Object = MibTableColumn
cn1000LineGroupRefIfGroupShelf = _Cn1000LineGroupRefIfGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 14),
    _Cn1000LineGroupRefIfGroupShelf_Type()
)
cn1000LineGroupRefIfGroupShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefIfGroupShelf.setStatus("current")


class _Cn1000LineGroupRefIfGroupSlotGroup_Type(Integer32):
    """Custom type cn1000LineGroupRefIfGroupSlotGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cn1000LineGroupRefIfGroupSlotGroup_Type.__name__ = "Integer32"
_Cn1000LineGroupRefIfGroupSlotGroup_Object = MibTableColumn
cn1000LineGroupRefIfGroupSlotGroup = _Cn1000LineGroupRefIfGroupSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 15),
    _Cn1000LineGroupRefIfGroupSlotGroup_Type()
)
cn1000LineGroupRefIfGroupSlotGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefIfGroupSlotGroup.setStatus("current")


class _Cn1000LineGroupRefIfGroupIndex_Type(Integer32):
    """Custom type cn1000LineGroupRefIfGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cn1000LineGroupRefIfGroupIndex_Type.__name__ = "Integer32"
_Cn1000LineGroupRefIfGroupIndex_Object = MibTableColumn
cn1000LineGroupRefIfGroupIndex = _Cn1000LineGroupRefIfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 1, 1, 16),
    _Cn1000LineGroupRefIfGroupIndex_Type()
)
cn1000LineGroupRefIfGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRefIfGroupIndex.setStatus("current")
_Cn1000LineRefSubscriptionTable_Object = MibTable
cn1000LineRefSubscriptionTable = _Cn1000LineRefSubscriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionTable.setStatus("current")
_Cn1000LineRefSubscriptionEntry_Object = MibTableRow
cn1000LineRefSubscriptionEntry = _Cn1000LineRefSubscriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1)
)
cn1000LineRefSubscriptionEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIndex"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionShelf"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionSlot"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionPort"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionAppearance"),
)
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionEntry.setStatus("current")
_Cn1000LineRefSubscriptionShelf_Type = Cn1000ShelfRange
_Cn1000LineRefSubscriptionShelf_Object = MibTableColumn
cn1000LineRefSubscriptionShelf = _Cn1000LineRefSubscriptionShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 1),
    _Cn1000LineRefSubscriptionShelf_Type()
)
cn1000LineRefSubscriptionShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionShelf.setStatus("current")
_Cn1000LineRefSubscriptionSlot_Type = Cn1000SlotRange
_Cn1000LineRefSubscriptionSlot_Object = MibTableColumn
cn1000LineRefSubscriptionSlot = _Cn1000LineRefSubscriptionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 2),
    _Cn1000LineRefSubscriptionSlot_Type()
)
cn1000LineRefSubscriptionSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionSlot.setStatus("current")
_Cn1000LineRefSubscriptionPort_Type = Cn1000PortRange
_Cn1000LineRefSubscriptionPort_Object = MibTableColumn
cn1000LineRefSubscriptionPort = _Cn1000LineRefSubscriptionPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 3),
    _Cn1000LineRefSubscriptionPort_Type()
)
cn1000LineRefSubscriptionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionPort.setStatus("current")
_Cn1000LineRefSubscriptionAppearance_Type = Cn1000LineAppearanceRange
_Cn1000LineRefSubscriptionAppearance_Object = MibTableColumn
cn1000LineRefSubscriptionAppearance = _Cn1000LineRefSubscriptionAppearance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 4),
    _Cn1000LineRefSubscriptionAppearance_Type()
)
cn1000LineRefSubscriptionAppearance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionAppearance.setStatus("current")


class _Cn1000LineRefSubscriberId_Type(Integer32):
    """Custom type cn1000LineRefSubscriberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000LineRefSubscriberId_Type.__name__ = "Integer32"
_Cn1000LineRefSubscriberId_Object = MibTableColumn
cn1000LineRefSubscriberId = _Cn1000LineRefSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 5),
    _Cn1000LineRefSubscriberId_Type()
)
cn1000LineRefSubscriberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriberId.setStatus("current")


class _Cn1000LineRefSubscriptionIfType_Type(Integer32):
    """Custom type cn1000LineRefSubscriptionIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Cn1000LineRefSubscriptionIfType_Type.__name__ = "Integer32"
_Cn1000LineRefSubscriptionIfType_Object = MibTableColumn
cn1000LineRefSubscriptionIfType = _Cn1000LineRefSubscriptionIfType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 6),
    _Cn1000LineRefSubscriptionIfType_Type()
)
cn1000LineRefSubscriptionIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionIfType.setStatus("current")


class _Cn1000LineRefSubscriptionServiceMode_Type(Integer32):
    """Custom type cn1000LineRefSubscriptionServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("dataMode", 1),
          ("voiceMode", 2))
    )


_Cn1000LineRefSubscriptionServiceMode_Type.__name__ = "Integer32"
_Cn1000LineRefSubscriptionServiceMode_Object = MibTableColumn
cn1000LineRefSubscriptionServiceMode = _Cn1000LineRefSubscriptionServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 7),
    _Cn1000LineRefSubscriptionServiceMode_Type()
)
cn1000LineRefSubscriptionServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionServiceMode.setStatus("current")


class _Cn1000LineRefSubscriptionSignalMode_Type(Integer32):
    """Custom type cn1000LineRefSubscriptionSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("ina95loopstart", 1),
          ("ina99loopstart", 2),
          ("clearChannel", 3))
    )


_Cn1000LineRefSubscriptionSignalMode_Type.__name__ = "Integer32"
_Cn1000LineRefSubscriptionSignalMode_Object = MibTableColumn
cn1000LineRefSubscriptionSignalMode = _Cn1000LineRefSubscriptionSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 8),
    _Cn1000LineRefSubscriptionSignalMode_Type()
)
cn1000LineRefSubscriptionSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionSignalMode.setStatus("current")
_Cn1000LineRefSubscriptionConfigStatus_Type = Cn1000ConfigurationStatus
_Cn1000LineRefSubscriptionConfigStatus_Object = MibTableColumn
cn1000LineRefSubscriptionConfigStatus = _Cn1000LineRefSubscriptionConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 10),
    _Cn1000LineRefSubscriptionConfigStatus_Type()
)
cn1000LineRefSubscriptionConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionConfigStatus.setStatus("current")
_Cn1000LineRefSubscriptionRowStatus_Type = RowStatus
_Cn1000LineRefSubscriptionRowStatus_Object = MibTableColumn
cn1000LineRefSubscriptionRowStatus = _Cn1000LineRefSubscriptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 11),
    _Cn1000LineRefSubscriptionRowStatus_Type()
)
cn1000LineRefSubscriptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionRowStatus.setStatus("current")


class _Cn1000LineRefSubscriptionGroupDesc_Type(OctetString):
    """Custom type cn1000LineRefSubscriptionGroupDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cn1000LineRefSubscriptionGroupDesc_Type.__name__ = "OctetString"
_Cn1000LineRefSubscriptionGroupDesc_Object = MibTableColumn
cn1000LineRefSubscriptionGroupDesc = _Cn1000LineRefSubscriptionGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 3, 1, 12),
    _Cn1000LineRefSubscriptionGroupDesc_Type()
)
cn1000LineRefSubscriptionGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LineRefSubscriptionGroupDesc.setStatus("current")
_Cn1000LineGroupTable_Object = MibTable
cn1000LineGroupTable = _Cn1000LineGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    cn1000LineGroupTable.setStatus("current")
_Cn1000LineGroupEntry_Object = MibTableRow
cn1000LineGroupEntry = _Cn1000LineGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1)
)
cn1000LineGroupEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupIndex"),
)
if mibBuilder.loadTexts:
    cn1000LineGroupEntry.setStatus("current")


class _Cn1000LineGroupIndex_Type(Integer32):
    """Custom type cn1000LineGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000LineGroupIndex_Type.__name__ = "Integer32"
_Cn1000LineGroupIndex_Object = MibTableColumn
cn1000LineGroupIndex = _Cn1000LineGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 1),
    _Cn1000LineGroupIndex_Type()
)
cn1000LineGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineGroupIndex.setStatus("current")
_Cn1000LineGroupType_Type = Cn1000SwitchInterfaceGroupType
_Cn1000LineGroupType_Object = MibTableColumn
cn1000LineGroupType = _Cn1000LineGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 2),
    _Cn1000LineGroupType_Type()
)
cn1000LineGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupType.setStatus("current")


class _Cn1000LineGroupIfGroupSystemAddress_Type(OctetString):
    """Custom type cn1000LineGroupIfGroupSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Cn1000LineGroupIfGroupSystemAddress_Type.__name__ = "OctetString"
_Cn1000LineGroupIfGroupSystemAddress_Object = MibTableColumn
cn1000LineGroupIfGroupSystemAddress = _Cn1000LineGroupIfGroupSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 3),
    _Cn1000LineGroupIfGroupSystemAddress_Type()
)
cn1000LineGroupIfGroupSystemAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupIfGroupSystemAddress.setStatus("current")


class _Cn1000LineGroupConnectionIndex_Type(Integer32):
    """Custom type cn1000LineGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Cn1000LineGroupConnectionIndex_Type.__name__ = "Integer32"
_Cn1000LineGroupConnectionIndex_Object = MibTableColumn
cn1000LineGroupConnectionIndex = _Cn1000LineGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 4),
    _Cn1000LineGroupConnectionIndex_Type()
)
cn1000LineGroupConnectionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupConnectionIndex.setStatus("current")


class _Cn1000LineGroupIfGroupConnectionIndex_Type(Integer32):
    """Custom type cn1000LineGroupIfGroupConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Cn1000LineGroupIfGroupConnectionIndex_Type.__name__ = "Integer32"
_Cn1000LineGroupIfGroupConnectionIndex_Object = MibTableColumn
cn1000LineGroupIfGroupConnectionIndex = _Cn1000LineGroupIfGroupConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 5),
    _Cn1000LineGroupIfGroupConnectionIndex_Type()
)
cn1000LineGroupIfGroupConnectionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupIfGroupConnectionIndex.setStatus("current")
_Cn1000LineGroupConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000LineGroupConfigurationStatus_Object = MibTableColumn
cn1000LineGroupConfigurationStatus = _Cn1000LineGroupConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 6),
    _Cn1000LineGroupConfigurationStatus_Type()
)
cn1000LineGroupConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LineGroupConfigurationStatus.setStatus("current")


class _Cn1000LineGroupRestartInitDelay_Type(Integer32):
    """Custom type cn1000LineGroupRestartInitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRestartInitDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRestartInitDelay_Object = MibTableColumn
cn1000LineGroupRestartInitDelay = _Cn1000LineGroupRestartInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 7),
    _Cn1000LineGroupRestartInitDelay_Type()
)
cn1000LineGroupRestartInitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRestartInitDelay.setStatus("current")


class _Cn1000LineGroupRestartMinDelay_Type(Integer32):
    """Custom type cn1000LineGroupRestartMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRestartMinDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRestartMinDelay_Object = MibTableColumn
cn1000LineGroupRestartMinDelay = _Cn1000LineGroupRestartMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 8),
    _Cn1000LineGroupRestartMinDelay_Type()
)
cn1000LineGroupRestartMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRestartMinDelay.setStatus("current")


class _Cn1000LineGroupRestartMaxDelay_Type(Integer32):
    """Custom type cn1000LineGroupRestartMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRestartMaxDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRestartMaxDelay_Object = MibTableColumn
cn1000LineGroupRestartMaxDelay = _Cn1000LineGroupRestartMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 9),
    _Cn1000LineGroupRestartMaxDelay_Type()
)
cn1000LineGroupRestartMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRestartMaxDelay.setStatus("current")


class _Cn1000LineGroupRetryMaxDelay_Type(Integer32):
    """Custom type cn1000LineGroupRetryMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupRetryMaxDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupRetryMaxDelay_Object = MibTableColumn
cn1000LineGroupRetryMaxDelay = _Cn1000LineGroupRetryMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 10),
    _Cn1000LineGroupRetryMaxDelay_Type()
)
cn1000LineGroupRetryMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRetryMaxDelay.setStatus("current")


class _Cn1000LineGroupMaxRoundTripDelay_Type(Integer32):
    """Custom type cn1000LineGroupMaxRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupMaxRoundTripDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupMaxRoundTripDelay_Object = MibTableColumn
cn1000LineGroupMaxRoundTripDelay = _Cn1000LineGroupMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 11),
    _Cn1000LineGroupMaxRoundTripDelay_Type()
)
cn1000LineGroupMaxRoundTripDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupMaxRoundTripDelay.setStatus("current")


class _Cn1000LineGroupInitialRoundTripDelay_Type(Integer32):
    """Custom type cn1000LineGroupInitialRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupInitialRoundTripDelay_Type.__name__ = "Integer32"
_Cn1000LineGroupInitialRoundTripDelay_Object = MibTableColumn
cn1000LineGroupInitialRoundTripDelay = _Cn1000LineGroupInitialRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 12),
    _Cn1000LineGroupInitialRoundTripDelay_Type()
)
cn1000LineGroupInitialRoundTripDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupInitialRoundTripDelay.setStatus("current")


class _Cn1000LineGroupPendingTimeout_Type(Integer32):
    """Custom type cn1000LineGroupPendingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000LineGroupPendingTimeout_Type.__name__ = "Integer32"
_Cn1000LineGroupPendingTimeout_Object = MibTableColumn
cn1000LineGroupPendingTimeout = _Cn1000LineGroupPendingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 13),
    _Cn1000LineGroupPendingTimeout_Type()
)
cn1000LineGroupPendingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupPendingTimeout.setStatus("current")


class _Cn1000LineGroupInterface_Type(OctetString):
    """Custom type cn1000LineGroupInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cn1000LineGroupInterface_Type.__name__ = "OctetString"
_Cn1000LineGroupInterface_Object = MibTableColumn
cn1000LineGroupInterface = _Cn1000LineGroupInterface_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 14),
    _Cn1000LineGroupInterface_Type()
)
cn1000LineGroupInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupInterface.setStatus("current")


class _Cn1000LineGroupInterfaceBracketed_Type(Integer32):
    """Custom type cn1000LineGroupInterfaceBracketed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unbracketed", 0),
          ("bracketed", 1))
    )


_Cn1000LineGroupInterfaceBracketed_Type.__name__ = "Integer32"
_Cn1000LineGroupInterfaceBracketed_Object = MibTableColumn
cn1000LineGroupInterfaceBracketed = _Cn1000LineGroupInterfaceBracketed_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 15),
    _Cn1000LineGroupInterfaceBracketed_Type()
)
cn1000LineGroupInterfaceBracketed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupInterfaceBracketed.setStatus("deprecated")


class _Cn1000LineGroupSpoofIPAddress_Type(OctetString):
    """Custom type cn1000LineGroupSpoofIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cn1000LineGroupSpoofIPAddress_Type.__name__ = "OctetString"
_Cn1000LineGroupSpoofIPAddress_Object = MibTableColumn
cn1000LineGroupSpoofIPAddress = _Cn1000LineGroupSpoofIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 16),
    _Cn1000LineGroupSpoofIPAddress_Type()
)
cn1000LineGroupSpoofIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupSpoofIPAddress.setStatus("deprecated")


class _Cn1000LineGroupLocalMediaIPAddress_Type(OctetString):
    """Custom type cn1000LineGroupLocalMediaIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cn1000LineGroupLocalMediaIPAddress_Type.__name__ = "OctetString"
_Cn1000LineGroupLocalMediaIPAddress_Object = MibTableColumn
cn1000LineGroupLocalMediaIPAddress = _Cn1000LineGroupLocalMediaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 17),
    _Cn1000LineGroupLocalMediaIPAddress_Type()
)
cn1000LineGroupLocalMediaIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupLocalMediaIPAddress.setStatus("deprecated")
_Cn1000LineGroupCodec_Type = Cn1000CodecType
_Cn1000LineGroupCodec_Object = MibTableColumn
cn1000LineGroupCodec = _Cn1000LineGroupCodec_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 18),
    _Cn1000LineGroupCodec_Type()
)
cn1000LineGroupCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupCodec.setStatus("deprecated")
_Cn1000LineGroupCodecPacketizationPeriod_Type = Cn1000CodecPacketizationPeriodType
_Cn1000LineGroupCodecPacketizationPeriod_Object = MibTableColumn
cn1000LineGroupCodecPacketizationPeriod = _Cn1000LineGroupCodecPacketizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 19),
    _Cn1000LineGroupCodecPacketizationPeriod_Type()
)
cn1000LineGroupCodecPacketizationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupCodecPacketizationPeriod.setStatus("deprecated")
_Cn1000LineGroupG726PacketizationRate_Type = Cn1000G726PacketizationRateType
_Cn1000LineGroupG726PacketizationRate_Object = MibTableColumn
cn1000LineGroupG726PacketizationRate = _Cn1000LineGroupG726PacketizationRate_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 20),
    _Cn1000LineGroupG726PacketizationRate_Type()
)
cn1000LineGroupG726PacketizationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupG726PacketizationRate.setStatus("deprecated")
_Cn1000LineGroupRowStatus_Type = RowStatus
_Cn1000LineGroupRowStatus_Object = MibTableColumn
cn1000LineGroupRowStatus = _Cn1000LineGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 21),
    _Cn1000LineGroupRowStatus_Type()
)
cn1000LineGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineGroupRowStatus.setStatus("current")
_Cn1000LineGroupAdminStatus_Type = Cn1000VoiceLnServAdminState
_Cn1000LineGroupAdminStatus_Object = MibTableColumn
cn1000LineGroupAdminStatus = _Cn1000LineGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 4, 1, 22),
    _Cn1000LineGroupAdminStatus_Type()
)
cn1000LineGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineGroupAdminStatus.setStatus("current")
_Cn1000LineSubscriptionTable_Object = MibTable
cn1000LineSubscriptionTable = _Cn1000LineSubscriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    cn1000LineSubscriptionTable.setStatus("current")
_Cn1000LineSubscriptionEntry_Object = MibTableRow
cn1000LineSubscriptionEntry = _Cn1000LineSubscriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5, 1)
)
cn1000LineSubscriptionEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineSubscriptionLineGroupIndex"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineSubscriptionLineIfIndex"),
)
if mibBuilder.loadTexts:
    cn1000LineSubscriptionEntry.setStatus("current")


class _Cn1000LineSubscriptionLineGroupIndex_Type(Integer32):
    """Custom type cn1000LineSubscriptionLineGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000LineSubscriptionLineGroupIndex_Type.__name__ = "Integer32"
_Cn1000LineSubscriptionLineGroupIndex_Object = MibTableColumn
cn1000LineSubscriptionLineGroupIndex = _Cn1000LineSubscriptionLineGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5, 1, 1),
    _Cn1000LineSubscriptionLineGroupIndex_Type()
)
cn1000LineSubscriptionLineGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineSubscriptionLineGroupIndex.setStatus("current")
_Cn1000LineSubscriptionLineIfIndex_Type = InterfaceIndex
_Cn1000LineSubscriptionLineIfIndex_Object = MibTableColumn
cn1000LineSubscriptionLineIfIndex = _Cn1000LineSubscriptionLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5, 1, 2),
    _Cn1000LineSubscriptionLineIfIndex_Type()
)
cn1000LineSubscriptionLineIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000LineSubscriptionLineIfIndex.setStatus("current")


class _Cn1000LineSubscriptionLossPadValue_Type(Integer32):
    """Custom type cn1000LineSubscriptionLossPadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Cn1000LineSubscriptionLossPadValue_Type.__name__ = "Integer32"
_Cn1000LineSubscriptionLossPadValue_Object = MibTableColumn
cn1000LineSubscriptionLossPadValue = _Cn1000LineSubscriptionLossPadValue_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5, 1, 3),
    _Cn1000LineSubscriptionLossPadValue_Type()
)
cn1000LineSubscriptionLossPadValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000LineSubscriptionLossPadValue.setStatus("current")
if mibBuilder.loadTexts:
    cn1000LineSubscriptionLossPadValue.setUnits("dB")
_Cn1000LineSubscriptionConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000LineSubscriptionConfigurationStatus_Object = MibTableColumn
cn1000LineSubscriptionConfigurationStatus = _Cn1000LineSubscriptionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5, 1, 4),
    _Cn1000LineSubscriptionConfigurationStatus_Type()
)
cn1000LineSubscriptionConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LineSubscriptionConfigurationStatus.setStatus("current")
_Cn1000LineSubscriptionRowStatus_Type = RowStatus
_Cn1000LineSubscriptionRowStatus_Object = MibTableColumn
cn1000LineSubscriptionRowStatus = _Cn1000LineSubscriptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 5, 1, 5),
    _Cn1000LineSubscriptionRowStatus_Type()
)
cn1000LineSubscriptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000LineSubscriptionRowStatus.setStatus("current")
_Cn1000VoiceCrossConnectsTable_Object = MibTable
cn1000VoiceCrossConnectsTable = _Cn1000VoiceCrossConnectsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsTable.setStatus("current")
_Cn1000VoiceCrossConnectsEntry_Object = MibTableRow
cn1000VoiceCrossConnectsEntry = _Cn1000VoiceCrossConnectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6, 1)
)
cn1000VoiceCrossConnectsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000VoiceCrossConnectsF1Cable"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000VoiceCrossConnectsF1Pair"),
)
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsEntry.setStatus("current")


class _Cn1000VoiceCrossConnectsF1Cable_Type(Integer32):
    """Custom type cn1000VoiceCrossConnectsF1Cable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000VoiceCrossConnectsF1Cable_Type.__name__ = "Integer32"
_Cn1000VoiceCrossConnectsF1Cable_Object = MibTableColumn
cn1000VoiceCrossConnectsF1Cable = _Cn1000VoiceCrossConnectsF1Cable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6, 1, 1),
    _Cn1000VoiceCrossConnectsF1Cable_Type()
)
cn1000VoiceCrossConnectsF1Cable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsF1Cable.setStatus("current")


class _Cn1000VoiceCrossConnectsF1Pair_Type(Integer32):
    """Custom type cn1000VoiceCrossConnectsF1Pair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000VoiceCrossConnectsF1Pair_Type.__name__ = "Integer32"
_Cn1000VoiceCrossConnectsF1Pair_Object = MibTableColumn
cn1000VoiceCrossConnectsF1Pair = _Cn1000VoiceCrossConnectsF1Pair_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6, 1, 2),
    _Cn1000VoiceCrossConnectsF1Pair_Type()
)
cn1000VoiceCrossConnectsF1Pair.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsF1Pair.setStatus("current")


class _Cn1000VoiceCrossConnectsF2Cable_Type(Integer32):
    """Custom type cn1000VoiceCrossConnectsF2Cable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000VoiceCrossConnectsF2Cable_Type.__name__ = "Integer32"
_Cn1000VoiceCrossConnectsF2Cable_Object = MibTableColumn
cn1000VoiceCrossConnectsF2Cable = _Cn1000VoiceCrossConnectsF2Cable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6, 1, 3),
    _Cn1000VoiceCrossConnectsF2Cable_Type()
)
cn1000VoiceCrossConnectsF2Cable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsF2Cable.setStatus("current")


class _Cn1000VoiceCrossConnectsF2Pair_Type(Integer32):
    """Custom type cn1000VoiceCrossConnectsF2Pair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Cn1000VoiceCrossConnectsF2Pair_Type.__name__ = "Integer32"
_Cn1000VoiceCrossConnectsF2Pair_Object = MibTableColumn
cn1000VoiceCrossConnectsF2Pair = _Cn1000VoiceCrossConnectsF2Pair_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6, 1, 4),
    _Cn1000VoiceCrossConnectsF2Pair_Type()
)
cn1000VoiceCrossConnectsF2Pair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsF2Pair.setStatus("current")
_Cn1000VoiceCrossConnectsRowStatus_Type = RowStatus
_Cn1000VoiceCrossConnectsRowStatus_Object = MibTableColumn
cn1000VoiceCrossConnectsRowStatus = _Cn1000VoiceCrossConnectsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 6, 1, 5),
    _Cn1000VoiceCrossConnectsRowStatus_Type()
)
cn1000VoiceCrossConnectsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000VoiceCrossConnectsRowStatus.setStatus("current")
_Cn1000VoiceLneServicesConformance_ObjectIdentity = ObjectIdentity
cn1000VoiceLneServicesConformance = _Cn1000VoiceLneServicesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 7)
)
_Cn1000LineGroupRefStatsTable_Object = MibTable
cn1000LineGroupRefStatsTable = _Cn1000LineGroupRefStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8)
)
if mibBuilder.loadTexts:
    cn1000LineGroupRefStatsTable.setStatus("current")
_Cn1000LineGroupRefStatsEntry_Object = MibTableRow
cn1000LineGroupRefStatsEntry = _Cn1000LineGroupRefStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1)
)
cn1000LineGroupRefStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefIndex"),
)
if mibBuilder.loadTexts:
    cn1000LineGroupRefStatsEntry.setStatus("current")


class _Cn1000StatsLGRefIndex_Type(Integer32):
    """Custom type cn1000StatsLGRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000StatsLGRefIndex_Type.__name__ = "Integer32"
_Cn1000StatsLGRefIndex_Object = MibTableColumn
cn1000StatsLGRefIndex = _Cn1000StatsLGRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 1),
    _Cn1000StatsLGRefIndex_Type()
)
cn1000StatsLGRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefIndex.setStatus("current")
_Cn1000StatsLGRefAdminState_Type = Cn1000VoiceLnServAdminState
_Cn1000StatsLGRefAdminState_Object = MibTableColumn
cn1000StatsLGRefAdminState = _Cn1000StatsLGRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 2),
    _Cn1000StatsLGRefAdminState_Type()
)
cn1000StatsLGRefAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefAdminState.setStatus("current")
_Cn1000StatsLGRefOperState_Type = Cn1000VoiceLnServOperState
_Cn1000StatsLGRefOperState_Object = MibTableColumn
cn1000StatsLGRefOperState = _Cn1000StatsLGRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 3),
    _Cn1000StatsLGRefOperState_Type()
)
cn1000StatsLGRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefOperState.setStatus("current")
_Cn1000StatsLGRefConnState_Type = Cn1000VoiceLnServConnState
_Cn1000StatsLGRefConnState_Object = MibTableColumn
cn1000StatsLGRefConnState = _Cn1000StatsLGRefConnState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 4),
    _Cn1000StatsLGRefConnState_Type()
)
cn1000StatsLGRefConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefConnState.setStatus("current")


class _Cn1000LGRefConnReqAttempts_Type(Integer32):
    """Custom type cn1000LGRefConnReqAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000LGRefConnReqAttempts_Type.__name__ = "Integer32"
_Cn1000LGRefConnReqAttempts_Object = MibTableColumn
cn1000LGRefConnReqAttempts = _Cn1000LGRefConnReqAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 5),
    _Cn1000LGRefConnReqAttempts_Type()
)
cn1000LGRefConnReqAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LGRefConnReqAttempts.setStatus("current")


class _Cn1000LGRefConnReqFailures_Type(Integer32):
    """Custom type cn1000LGRefConnReqFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000LGRefConnReqFailures_Type.__name__ = "Integer32"
_Cn1000LGRefConnReqFailures_Object = MibTableColumn
cn1000LGRefConnReqFailures = _Cn1000LGRefConnReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 6),
    _Cn1000LGRefConnReqFailures_Type()
)
cn1000LGRefConnReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LGRefConnReqFailures.setStatus("current")


class _Cn1000LGRefFailedConnections_Type(Integer32):
    """Custom type cn1000LGRefFailedConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000LGRefFailedConnections_Type.__name__ = "Integer32"
_Cn1000LGRefFailedConnections_Object = MibTableColumn
cn1000LGRefFailedConnections = _Cn1000LGRefFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 8, 1, 7),
    _Cn1000LGRefFailedConnections_Type()
)
cn1000LGRefFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000LGRefFailedConnections.setStatus("current")
_Cn1000LineGroupRefSubscriptionsStatsTable_Object = MibTable
cn1000LineGroupRefSubscriptionsStatsTable = _Cn1000LineGroupRefSubscriptionsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9)
)
if mibBuilder.loadTexts:
    cn1000LineGroupRefSubscriptionsStatsTable.setStatus("current")
_Cn1000LineGroupRefSubscriptionsStatsEntry_Object = MibTableRow
cn1000LineGroupRefSubscriptionsStatsEntry = _Cn1000LineGroupRefSubscriptionsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1)
)
cn1000LineGroupRefSubscriptionsStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupRefIndex"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionShelf"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionSlot"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionPort"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionAppearance"),
)
if mibBuilder.loadTexts:
    cn1000LineGroupRefSubscriptionsStatsEntry.setStatus("current")


class _Cn1000StatsLineGroupRefIndex_Type(Integer32):
    """Custom type cn1000StatsLineGroupRefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000StatsLineGroupRefIndex_Type.__name__ = "Integer32"
_Cn1000StatsLineGroupRefIndex_Object = MibTableColumn
cn1000StatsLineGroupRefIndex = _Cn1000StatsLineGroupRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 1),
    _Cn1000StatsLineGroupRefIndex_Type()
)
cn1000StatsLineGroupRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupRefIndex.setStatus("current")
_Cn1000StatsLGRefSubscriptionShelf_Type = Cn1000ShelfRange
_Cn1000StatsLGRefSubscriptionShelf_Object = MibTableColumn
cn1000StatsLGRefSubscriptionShelf = _Cn1000StatsLGRefSubscriptionShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 2),
    _Cn1000StatsLGRefSubscriptionShelf_Type()
)
cn1000StatsLGRefSubscriptionShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubscriptionShelf.setStatus("current")
_Cn1000StatsLGRefSubscriptionSlot_Type = Cn1000SlotRange
_Cn1000StatsLGRefSubscriptionSlot_Object = MibTableColumn
cn1000StatsLGRefSubscriptionSlot = _Cn1000StatsLGRefSubscriptionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 3),
    _Cn1000StatsLGRefSubscriptionSlot_Type()
)
cn1000StatsLGRefSubscriptionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubscriptionSlot.setStatus("current")
_Cn1000StatsLGRefSubscriptionPort_Type = Cn1000PortRange
_Cn1000StatsLGRefSubscriptionPort_Object = MibTableColumn
cn1000StatsLGRefSubscriptionPort = _Cn1000StatsLGRefSubscriptionPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 4),
    _Cn1000StatsLGRefSubscriptionPort_Type()
)
cn1000StatsLGRefSubscriptionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubscriptionPort.setStatus("current")
_Cn1000StatsLGRefSubscriptionAppearance_Type = Cn1000LineAppearanceRange
_Cn1000StatsLGRefSubscriptionAppearance_Object = MibTableColumn
cn1000StatsLGRefSubscriptionAppearance = _Cn1000StatsLGRefSubscriptionAppearance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 5),
    _Cn1000StatsLGRefSubscriptionAppearance_Type()
)
cn1000StatsLGRefSubscriptionAppearance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubscriptionAppearance.setStatus("current")


class _Cn1000StatsLGRefSubscriptionCRV_Type(Integer32):
    """Custom type cn1000StatsLGRefSubscriptionCRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Cn1000StatsLGRefSubscriptionCRV_Type.__name__ = "Integer32"
_Cn1000StatsLGRefSubscriptionCRV_Object = MibTableColumn
cn1000StatsLGRefSubscriptionCRV = _Cn1000StatsLGRefSubscriptionCRV_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 6),
    _Cn1000StatsLGRefSubscriptionCRV_Type()
)
cn1000StatsLGRefSubscriptionCRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubscriptionCRV.setStatus("current")


class _Cn1000StatsLGRefSubscriptionIfType_Type(Integer32):
    """Custom type cn1000StatsLGRefSubscriptionIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Cn1000StatsLGRefSubscriptionIfType_Type.__name__ = "Integer32"
_Cn1000StatsLGRefSubscriptionIfType_Object = MibTableColumn
cn1000StatsLGRefSubscriptionIfType = _Cn1000StatsLGRefSubscriptionIfType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 7),
    _Cn1000StatsLGRefSubscriptionIfType_Type()
)
cn1000StatsLGRefSubscriptionIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubscriptionIfType.setStatus("current")


class _Cn1000StatsLGRefSubPrimaryServiceState_Type(Integer32):
    """Custom type cn1000StatsLGRefSubPrimaryServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("inService", 1),
          ("outOfService", 2),
          ("blocked", 3),
          ("unblocked", 4),
          ("localUnblocked", 5),
          ("remoteUnblocked", 6))
    )


_Cn1000StatsLGRefSubPrimaryServiceState_Type.__name__ = "Integer32"
_Cn1000StatsLGRefSubPrimaryServiceState_Object = MibTableColumn
cn1000StatsLGRefSubPrimaryServiceState = _Cn1000StatsLGRefSubPrimaryServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 8),
    _Cn1000StatsLGRefSubPrimaryServiceState_Type()
)
cn1000StatsLGRefSubPrimaryServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubPrimaryServiceState.setStatus("current")
_Cn1000StatsLGRefSubSecondaryServiceState_Type = CnGR303LinkSecondaryServiceStateType
_Cn1000StatsLGRefSubSecondaryServiceState_Object = MibTableColumn
cn1000StatsLGRefSubSecondaryServiceState = _Cn1000StatsLGRefSubSecondaryServiceState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 9),
    _Cn1000StatsLGRefSubSecondaryServiceState_Type()
)
cn1000StatsLGRefSubSecondaryServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubSecondaryServiceState.setStatus("current")
_Cn1000StatsLGRefSubConnState_Type = Cn1000VoiceLnServSubscriptionConnState
_Cn1000StatsLGRefSubConnState_Object = MibTableColumn
cn1000StatsLGRefSubConnState = _Cn1000StatsLGRefSubConnState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 10),
    _Cn1000StatsLGRefSubConnState_Type()
)
cn1000StatsLGRefSubConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubConnState.setStatus("current")


class _Cn1000StatsLGRefSubNtwkChannel_Type(Integer32):
    """Custom type cn1000StatsLGRefSubNtwkChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Cn1000StatsLGRefSubNtwkChannel_Type.__name__ = "Integer32"
_Cn1000StatsLGRefSubNtwkChannel_Object = MibTableColumn
cn1000StatsLGRefSubNtwkChannel = _Cn1000StatsLGRefSubNtwkChannel_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 11),
    _Cn1000StatsLGRefSubNtwkChannel_Type()
)
cn1000StatsLGRefSubNtwkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubNtwkChannel.setStatus("current")


class _Cn1000StatsLGRefSubLineChannel_Type(Integer32):
    """Custom type cn1000StatsLGRefSubLineChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Cn1000StatsLGRefSubLineChannel_Type.__name__ = "Integer32"
_Cn1000StatsLGRefSubLineChannel_Object = MibTableColumn
cn1000StatsLGRefSubLineChannel = _Cn1000StatsLGRefSubLineChannel_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 12),
    _Cn1000StatsLGRefSubLineChannel_Type()
)
cn1000StatsLGRefSubLineChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubLineChannel.setStatus("current")
_Cn1000StatsLGRefSubHookswitchState_Type = Cn1000VoiceLnServHookswitchState
_Cn1000StatsLGRefSubHookswitchState_Object = MibTableColumn
cn1000StatsLGRefSubHookswitchState = _Cn1000StatsLGRefSubHookswitchState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 9, 1, 13),
    _Cn1000StatsLGRefSubHookswitchState_Type()
)
cn1000StatsLGRefSubHookswitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGRefSubHookswitchState.setStatus("current")
_Cn1000LineGroupStatsTable_Object = MibTable
cn1000LineGroupStatsTable = _Cn1000LineGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 10)
)
if mibBuilder.loadTexts:
    cn1000LineGroupStatsTable.setStatus("current")
_Cn1000LineGroupStatsEntry_Object = MibTableRow
cn1000LineGroupStatsEntry = _Cn1000LineGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 10, 1)
)
cn1000LineGroupStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGIndex"),
)
if mibBuilder.loadTexts:
    cn1000LineGroupStatsEntry.setStatus("current")


class _Cn1000StatsLGIndex_Type(Integer32):
    """Custom type cn1000StatsLGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000StatsLGIndex_Type.__name__ = "Integer32"
_Cn1000StatsLGIndex_Object = MibTableColumn
cn1000StatsLGIndex = _Cn1000StatsLGIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 10, 1, 1),
    _Cn1000StatsLGIndex_Type()
)
cn1000StatsLGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGIndex.setStatus("current")
_Cn1000StatsLGOperState_Type = Cn1000VoiceLnServOperState
_Cn1000StatsLGOperState_Object = MibTableColumn
cn1000StatsLGOperState = _Cn1000StatsLGOperState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 10, 1, 2),
    _Cn1000StatsLGOperState_Type()
)
cn1000StatsLGOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGOperState.setStatus("current")


class _Cn1000StatsLGSuccessfullConnections_Type(Integer32):
    """Custom type cn1000StatsLGSuccessfullConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000StatsLGSuccessfullConnections_Type.__name__ = "Integer32"
_Cn1000StatsLGSuccessfullConnections_Object = MibTableColumn
cn1000StatsLGSuccessfullConnections = _Cn1000StatsLGSuccessfullConnections_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 10, 1, 3),
    _Cn1000StatsLGSuccessfullConnections_Type()
)
cn1000StatsLGSuccessfullConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGSuccessfullConnections.setStatus("current")


class _Cn1000StatsLGUnsuccessfullConnections_Type(Integer32):
    """Custom type cn1000StatsLGUnsuccessfullConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000StatsLGUnsuccessfullConnections_Type.__name__ = "Integer32"
_Cn1000StatsLGUnsuccessfullConnections_Object = MibTableColumn
cn1000StatsLGUnsuccessfullConnections = _Cn1000StatsLGUnsuccessfullConnections_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 10, 1, 4),
    _Cn1000StatsLGUnsuccessfullConnections_Type()
)
cn1000StatsLGUnsuccessfullConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLGUnsuccessfullConnections.setStatus("current")
_Cn1000LineSubscriptionStatsTable_Object = MibTable
cn1000LineSubscriptionStatsTable = _Cn1000LineSubscriptionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11)
)
if mibBuilder.loadTexts:
    cn1000LineSubscriptionStatsTable.setStatus("current")
_Cn1000LineSubscriptionStatsEntry_Object = MibTableRow
cn1000LineSubscriptionStatsEntry = _Cn1000LineSubscriptionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1)
)
cn1000LineSubscriptionStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupIndex"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineShelf"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineSlot"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLinePort"),
)
if mibBuilder.loadTexts:
    cn1000LineSubscriptionStatsEntry.setStatus("current")


class _Cn1000StatsLineGroupIndex_Type(Integer32):
    """Custom type cn1000StatsLineGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000StatsLineGroupIndex_Type.__name__ = "Integer32"
_Cn1000StatsLineGroupIndex_Object = MibTableColumn
cn1000StatsLineGroupIndex = _Cn1000StatsLineGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 1),
    _Cn1000StatsLineGroupIndex_Type()
)
cn1000StatsLineGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupIndex.setStatus("current")


class _Cn1000StatsLineGroupLineShelf_Type(Integer32):
    """Custom type cn1000StatsLineGroupLineShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cn1000StatsLineGroupLineShelf_Type.__name__ = "Integer32"
_Cn1000StatsLineGroupLineShelf_Object = MibTableColumn
cn1000StatsLineGroupLineShelf = _Cn1000StatsLineGroupLineShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 2),
    _Cn1000StatsLineGroupLineShelf_Type()
)
cn1000StatsLineGroupLineShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupLineShelf.setStatus("current")


class _Cn1000StatsLineGroupLineSlot_Type(Integer32):
    """Custom type cn1000StatsLineGroupLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cn1000StatsLineGroupLineSlot_Type.__name__ = "Integer32"
_Cn1000StatsLineGroupLineSlot_Object = MibTableColumn
cn1000StatsLineGroupLineSlot = _Cn1000StatsLineGroupLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 3),
    _Cn1000StatsLineGroupLineSlot_Type()
)
cn1000StatsLineGroupLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupLineSlot.setStatus("current")


class _Cn1000StatsLineGroupLinePort_Type(Integer32):
    """Custom type cn1000StatsLineGroupLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cn1000StatsLineGroupLinePort_Type.__name__ = "Integer32"
_Cn1000StatsLineGroupLinePort_Object = MibTableColumn
cn1000StatsLineGroupLinePort = _Cn1000StatsLineGroupLinePort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 4),
    _Cn1000StatsLineGroupLinePort_Type()
)
cn1000StatsLineGroupLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupLinePort.setStatus("current")


class _Cn1000StatsLineGroupLineAppearance_Type(Integer32):
    """Custom type cn1000StatsLineGroupLineAppearance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cn1000StatsLineGroupLineAppearance_Type.__name__ = "Integer32"
_Cn1000StatsLineGroupLineAppearance_Object = MibTableColumn
cn1000StatsLineGroupLineAppearance = _Cn1000StatsLineGroupLineAppearance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 5),
    _Cn1000StatsLineGroupLineAppearance_Type()
)
cn1000StatsLineGroupLineAppearance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupLineAppearance.setStatus("current")
_Cn1000StatsLineGroupLineOperState_Type = Cn1000VoiceLGLineOperState
_Cn1000StatsLineGroupLineOperState_Object = MibTableColumn
cn1000StatsLineGroupLineOperState = _Cn1000StatsLineGroupLineOperState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 6),
    _Cn1000StatsLineGroupLineOperState_Type()
)
cn1000StatsLineGroupLineOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupLineOperState.setStatus("current")
_Cn1000StatsLineGroupLineHookswitchState_Type = Cn1000VoiceLnServHookswitchState
_Cn1000StatsLineGroupLineHookswitchState_Object = MibTableColumn
cn1000StatsLineGroupLineHookswitchState = _Cn1000StatsLineGroupLineHookswitchState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 11, 1, 7),
    _Cn1000StatsLineGroupLineHookswitchState_Type()
)
cn1000StatsLineGroupLineHookswitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsLineGroupLineHookswitchState.setStatus("current")
_Cn1000MediaGatewayTable_Object = MibTable
cn1000MediaGatewayTable = _Cn1000MediaGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12)
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayTable.setStatus("current")
_Cn1000MediaGatewayEntry_Object = MibTableRow
cn1000MediaGatewayEntry = _Cn1000MediaGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1)
)
cn1000MediaGatewayEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000MGIndex"),
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayEntry.setStatus("current")


class _Cn1000MGIndex_Type(Integer32):
    """Custom type cn1000MGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000MGIndex_Type.__name__ = "Integer32"
_Cn1000MGIndex_Object = MibTableColumn
cn1000MGIndex = _Cn1000MGIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 1),
    _Cn1000MGIndex_Type()
)
cn1000MGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MGIndex.setStatus("current")
_Cn1000MediaGatewayType_Type = Cn1000SwitchInterfaceGroupType
_Cn1000MediaGatewayType_Object = MibTableColumn
cn1000MediaGatewayType = _Cn1000MediaGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 2),
    _Cn1000MediaGatewayType_Type()
)
cn1000MediaGatewayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayType.setStatus("current")


class _Cn1000MediaGatewayMgcIpAddress_Type(OctetString):
    """Custom type cn1000MediaGatewayMgcIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Cn1000MediaGatewayMgcIpAddress_Type.__name__ = "OctetString"
_Cn1000MediaGatewayMgcIpAddress_Object = MibTableColumn
cn1000MediaGatewayMgcIpAddress = _Cn1000MediaGatewayMgcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 3),
    _Cn1000MediaGatewayMgcIpAddress_Type()
)
cn1000MediaGatewayMgcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayMgcIpAddress.setStatus("current")


class _Cn1000MediaGatewaySignallingPort_Type(Integer32):
    """Custom type cn1000MediaGatewaySignallingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Cn1000MediaGatewaySignallingPort_Type.__name__ = "Integer32"
_Cn1000MediaGatewaySignallingPort_Object = MibTableColumn
cn1000MediaGatewaySignallingPort = _Cn1000MediaGatewaySignallingPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 4),
    _Cn1000MediaGatewaySignallingPort_Type()
)
cn1000MediaGatewaySignallingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewaySignallingPort.setStatus("current")


class _Cn1000MediaGatewayMgcPort_Type(Integer32):
    """Custom type cn1000MediaGatewayMgcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Cn1000MediaGatewayMgcPort_Type.__name__ = "Integer32"
_Cn1000MediaGatewayMgcPort_Object = MibTableColumn
cn1000MediaGatewayMgcPort = _Cn1000MediaGatewayMgcPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 5),
    _Cn1000MediaGatewayMgcPort_Type()
)
cn1000MediaGatewayMgcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayMgcPort.setStatus("current")
_Cn1000MediaGatewayConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000MediaGatewayConfigurationStatus_Object = MibTableColumn
cn1000MediaGatewayConfigurationStatus = _Cn1000MediaGatewayConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 6),
    _Cn1000MediaGatewayConfigurationStatus_Type()
)
cn1000MediaGatewayConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaGatewayConfigurationStatus.setStatus("current")


class _Cn1000MediaGatewayRestartInitDelay_Type(Integer32):
    """Custom type cn1000MediaGatewayRestartInitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayRestartInitDelay_Type.__name__ = "Integer32"
_Cn1000MediaGatewayRestartInitDelay_Object = MibTableColumn
cn1000MediaGatewayRestartInitDelay = _Cn1000MediaGatewayRestartInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 7),
    _Cn1000MediaGatewayRestartInitDelay_Type()
)
cn1000MediaGatewayRestartInitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayRestartInitDelay.setStatus("current")


class _Cn1000MediaGatewayRestartMinDelay_Type(Integer32):
    """Custom type cn1000MediaGatewayRestartMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayRestartMinDelay_Type.__name__ = "Integer32"
_Cn1000MediaGatewayRestartMinDelay_Object = MibTableColumn
cn1000MediaGatewayRestartMinDelay = _Cn1000MediaGatewayRestartMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 8),
    _Cn1000MediaGatewayRestartMinDelay_Type()
)
cn1000MediaGatewayRestartMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayRestartMinDelay.setStatus("current")


class _Cn1000MediaGatewayRestartMaxDelay_Type(Integer32):
    """Custom type cn1000MediaGatewayRestartMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayRestartMaxDelay_Type.__name__ = "Integer32"
_Cn1000MediaGatewayRestartMaxDelay_Object = MibTableColumn
cn1000MediaGatewayRestartMaxDelay = _Cn1000MediaGatewayRestartMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 9),
    _Cn1000MediaGatewayRestartMaxDelay_Type()
)
cn1000MediaGatewayRestartMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayRestartMaxDelay.setStatus("current")


class _Cn1000MediaGatewayRetryMaxDelay_Type(Integer32):
    """Custom type cn1000MediaGatewayRetryMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayRetryMaxDelay_Type.__name__ = "Integer32"
_Cn1000MediaGatewayRetryMaxDelay_Object = MibTableColumn
cn1000MediaGatewayRetryMaxDelay = _Cn1000MediaGatewayRetryMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 10),
    _Cn1000MediaGatewayRetryMaxDelay_Type()
)
cn1000MediaGatewayRetryMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayRetryMaxDelay.setStatus("current")


class _Cn1000MediaGatewayMaxRoundTripDelay_Type(Integer32):
    """Custom type cn1000MediaGatewayMaxRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayMaxRoundTripDelay_Type.__name__ = "Integer32"
_Cn1000MediaGatewayMaxRoundTripDelay_Object = MibTableColumn
cn1000MediaGatewayMaxRoundTripDelay = _Cn1000MediaGatewayMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 11),
    _Cn1000MediaGatewayMaxRoundTripDelay_Type()
)
cn1000MediaGatewayMaxRoundTripDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayMaxRoundTripDelay.setStatus("current")


class _Cn1000MediaGatewayInitialRoundTripDelay_Type(Integer32):
    """Custom type cn1000MediaGatewayInitialRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayInitialRoundTripDelay_Type.__name__ = "Integer32"
_Cn1000MediaGatewayInitialRoundTripDelay_Object = MibTableColumn
cn1000MediaGatewayInitialRoundTripDelay = _Cn1000MediaGatewayInitialRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 12),
    _Cn1000MediaGatewayInitialRoundTripDelay_Type()
)
cn1000MediaGatewayInitialRoundTripDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayInitialRoundTripDelay.setStatus("current")


class _Cn1000MediaGatewayPendingTimeout_Type(Integer32):
    """Custom type cn1000MediaGatewayPendingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cn1000MediaGatewayPendingTimeout_Type.__name__ = "Integer32"
_Cn1000MediaGatewayPendingTimeout_Object = MibTableColumn
cn1000MediaGatewayPendingTimeout = _Cn1000MediaGatewayPendingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 13),
    _Cn1000MediaGatewayPendingTimeout_Type()
)
cn1000MediaGatewayPendingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayPendingTimeout.setStatus("current")


class _Cn1000MediaGatewaySignallingInterface_Type(OctetString):
    """Custom type cn1000MediaGatewaySignallingInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cn1000MediaGatewaySignallingInterface_Type.__name__ = "OctetString"
_Cn1000MediaGatewaySignallingInterface_Object = MibTableColumn
cn1000MediaGatewaySignallingInterface = _Cn1000MediaGatewaySignallingInterface_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 14),
    _Cn1000MediaGatewaySignallingInterface_Type()
)
cn1000MediaGatewaySignallingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewaySignallingInterface.setStatus("current")


class _Cn1000MediaGatewayInterfaceBracketed_Type(Integer32):
    """Custom type cn1000MediaGatewayInterfaceBracketed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unbracketed", 0),
          ("bracketed", 1))
    )


_Cn1000MediaGatewayInterfaceBracketed_Type.__name__ = "Integer32"
_Cn1000MediaGatewayInterfaceBracketed_Object = MibTableColumn
cn1000MediaGatewayInterfaceBracketed = _Cn1000MediaGatewayInterfaceBracketed_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 15),
    _Cn1000MediaGatewayInterfaceBracketed_Type()
)
cn1000MediaGatewayInterfaceBracketed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewayInterfaceBracketed.setStatus("current")


class _Cn1000MediaGatewayMgAlias_Type(OctetString):
    """Custom type cn1000MediaGatewayMgAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cn1000MediaGatewayMgAlias_Type.__name__ = "OctetString"
_Cn1000MediaGatewayMgAlias_Object = MibTableColumn
cn1000MediaGatewayMgAlias = _Cn1000MediaGatewayMgAlias_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 16),
    _Cn1000MediaGatewayMgAlias_Type()
)
cn1000MediaGatewayMgAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewayMgAlias.setStatus("current")


class _Cn1000MediaGatewayMediaInterface_Type(OctetString):
    """Custom type cn1000MediaGatewayMediaInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cn1000MediaGatewayMediaInterface_Type.__name__ = "OctetString"
_Cn1000MediaGatewayMediaInterface_Object = MibTableColumn
cn1000MediaGatewayMediaInterface = _Cn1000MediaGatewayMediaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 17),
    _Cn1000MediaGatewayMediaInterface_Type()
)
cn1000MediaGatewayMediaInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewayMediaInterface.setStatus("current")
_Cn1000MediaGatewayCodec_Type = Cn1000CodecType
_Cn1000MediaGatewayCodec_Object = MibTableColumn
cn1000MediaGatewayCodec = _Cn1000MediaGatewayCodec_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 18),
    _Cn1000MediaGatewayCodec_Type()
)
cn1000MediaGatewayCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewayCodec.setStatus("current")


class _Cn1000MediaGatewayCodecPacketizationMin_Type(Integer32):
    """Custom type cn1000MediaGatewayCodecPacketizationMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000MediaGatewayCodecPacketizationMin_Type.__name__ = "Integer32"
_Cn1000MediaGatewayCodecPacketizationMin_Object = MibTableColumn
cn1000MediaGatewayCodecPacketizationMin = _Cn1000MediaGatewayCodecPacketizationMin_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 19),
    _Cn1000MediaGatewayCodecPacketizationMin_Type()
)
cn1000MediaGatewayCodecPacketizationMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayCodecPacketizationMin.setStatus("current")


class _Cn1000MediaGatewayCodecPacketizationMax_Type(Integer32):
    """Custom type cn1000MediaGatewayCodecPacketizationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000MediaGatewayCodecPacketizationMax_Type.__name__ = "Integer32"
_Cn1000MediaGatewayCodecPacketizationMax_Object = MibTableColumn
cn1000MediaGatewayCodecPacketizationMax = _Cn1000MediaGatewayCodecPacketizationMax_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 20),
    _Cn1000MediaGatewayCodecPacketizationMax_Type()
)
cn1000MediaGatewayCodecPacketizationMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayCodecPacketizationMax.setStatus("current")


class _Cn1000MediaGatewayCodecSilenceSupp_Type(Integer32):
    """Custom type cn1000MediaGatewayCodecSilenceSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cn1000MediaGatewayCodecSilenceSupp_Type.__name__ = "Integer32"
_Cn1000MediaGatewayCodecSilenceSupp_Object = MibTableColumn
cn1000MediaGatewayCodecSilenceSupp = _Cn1000MediaGatewayCodecSilenceSupp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 21),
    _Cn1000MediaGatewayCodecSilenceSupp_Type()
)
cn1000MediaGatewayCodecSilenceSupp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayCodecSilenceSupp.setStatus("current")


class _Cn1000MediaGatewayUdpStartRange_Type(Integer32):
    """Custom type cn1000MediaGatewayUdpStartRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49152, 65535),
    )


_Cn1000MediaGatewayUdpStartRange_Type.__name__ = "Integer32"
_Cn1000MediaGatewayUdpStartRange_Object = MibTableColumn
cn1000MediaGatewayUdpStartRange = _Cn1000MediaGatewayUdpStartRange_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 22),
    _Cn1000MediaGatewayUdpStartRange_Type()
)
cn1000MediaGatewayUdpStartRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayUdpStartRange.setStatus("current")
_Cn1000MediaGatewaySigPortType_Type = Cn1000VoiceIpPortType
_Cn1000MediaGatewaySigPortType_Object = MibTableColumn
cn1000MediaGatewaySigPortType = _Cn1000MediaGatewaySigPortType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 23),
    _Cn1000MediaGatewaySigPortType_Type()
)
cn1000MediaGatewaySigPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewaySigPortType.setStatus("current")


class _Cn1000MediaGatewayMgcType_Type(Integer32):
    """Custom type cn1000MediaGatewayMgcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("metaswitch", 0),
          ("convergent", 1))
    )


_Cn1000MediaGatewayMgcType_Type.__name__ = "Integer32"
_Cn1000MediaGatewayMgcType_Object = MibTableColumn
cn1000MediaGatewayMgcType = _Cn1000MediaGatewayMgcType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 24),
    _Cn1000MediaGatewayMgcType_Type()
)
cn1000MediaGatewayMgcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayMgcType.setStatus("current")


class _Cn1000MediaGatewayIpTypeOfService_Type(Integer32):
    """Custom type cn1000MediaGatewayIpTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000MediaGatewayIpTypeOfService_Type.__name__ = "Integer32"
_Cn1000MediaGatewayIpTypeOfService_Object = MibTableColumn
cn1000MediaGatewayIpTypeOfService = _Cn1000MediaGatewayIpTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 25),
    _Cn1000MediaGatewayIpTypeOfService_Type()
)
cn1000MediaGatewayIpTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayIpTypeOfService.setStatus("current")


class _Cn1000MediaGatewayIpTimeToLive_Type(Integer32):
    """Custom type cn1000MediaGatewayIpTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000MediaGatewayIpTimeToLive_Type.__name__ = "Integer32"
_Cn1000MediaGatewayIpTimeToLive_Object = MibTableColumn
cn1000MediaGatewayIpTimeToLive = _Cn1000MediaGatewayIpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 26),
    _Cn1000MediaGatewayIpTimeToLive_Type()
)
cn1000MediaGatewayIpTimeToLive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayIpTimeToLive.setStatus("current")


class _Cn1000MediaGatewayLineIdPrefix_Type(OctetString):
    """Custom type cn1000MediaGatewayLineIdPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Cn1000MediaGatewayLineIdPrefix_Type.__name__ = "OctetString"
_Cn1000MediaGatewayLineIdPrefix_Object = MibTableColumn
cn1000MediaGatewayLineIdPrefix = _Cn1000MediaGatewayLineIdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 27),
    _Cn1000MediaGatewayLineIdPrefix_Type()
)
cn1000MediaGatewayLineIdPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineIdPrefix.setStatus("current")
_Cn1000MediaGatewayRowStatus_Type = RowStatus
_Cn1000MediaGatewayRowStatus_Object = MibTableColumn
cn1000MediaGatewayRowStatus = _Cn1000MediaGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 28),
    _Cn1000MediaGatewayRowStatus_Type()
)
cn1000MediaGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayRowStatus.setStatus("current")
_Cn1000MediaGatewayAdminStatus_Type = Cn1000VoiceLnServAdminState
_Cn1000MediaGatewayAdminStatus_Object = MibTableColumn
cn1000MediaGatewayAdminStatus = _Cn1000MediaGatewayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 12, 1, 29),
    _Cn1000MediaGatewayAdminStatus_Type()
)
cn1000MediaGatewayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewayAdminStatus.setStatus("current")
_Cn1000MediaGatewayLineTable_Object = MibTable
cn1000MediaGatewayLineTable = _Cn1000MediaGatewayLineTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13)
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineTable.setStatus("current")
_Cn1000MediaGatewayLineEntry_Object = MibTableRow
cn1000MediaGatewayLineEntry = _Cn1000MediaGatewayLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13, 1)
)
cn1000MediaGatewayLineEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000MediaGatewayGroupIndex"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000MediaGatewayLineIfIndex"),
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineEntry.setStatus("current")


class _Cn1000MediaGatewayGroupIndex_Type(Integer32):
    """Custom type cn1000MediaGatewayGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000MediaGatewayGroupIndex_Type.__name__ = "Integer32"
_Cn1000MediaGatewayGroupIndex_Object = MibTableColumn
cn1000MediaGatewayGroupIndex = _Cn1000MediaGatewayGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13, 1, 1),
    _Cn1000MediaGatewayGroupIndex_Type()
)
cn1000MediaGatewayGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaGatewayGroupIndex.setStatus("current")
_Cn1000MediaGatewayLineIfIndex_Type = InterfaceIndex
_Cn1000MediaGatewayLineIfIndex_Object = MibTableColumn
cn1000MediaGatewayLineIfIndex = _Cn1000MediaGatewayLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13, 1, 2),
    _Cn1000MediaGatewayLineIfIndex_Type()
)
cn1000MediaGatewayLineIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineIfIndex.setStatus("current")


class _Cn1000MediaGatewayLineLossPadValue_Type(Integer32):
    """Custom type cn1000MediaGatewayLineLossPadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Cn1000MediaGatewayLineLossPadValue_Type.__name__ = "Integer32"
_Cn1000MediaGatewayLineLossPadValue_Object = MibTableColumn
cn1000MediaGatewayLineLossPadValue = _Cn1000MediaGatewayLineLossPadValue_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13, 1, 3),
    _Cn1000MediaGatewayLineLossPadValue_Type()
)
cn1000MediaGatewayLineLossPadValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineLossPadValue.setStatus("current")
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineLossPadValue.setUnits("dB")
_Cn1000MediaGatewayLineConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000MediaGatewayLineConfigurationStatus_Object = MibTableColumn
cn1000MediaGatewayLineConfigurationStatus = _Cn1000MediaGatewayLineConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13, 1, 4),
    _Cn1000MediaGatewayLineConfigurationStatus_Type()
)
cn1000MediaGatewayLineConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineConfigurationStatus.setStatus("current")
_Cn1000MediaGatewayLineRowStatus_Type = RowStatus
_Cn1000MediaGatewayLineRowStatus_Object = MibTableColumn
cn1000MediaGatewayLineRowStatus = _Cn1000MediaGatewayLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 13, 1, 5),
    _Cn1000MediaGatewayLineRowStatus_Type()
)
cn1000MediaGatewayLineRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineRowStatus.setStatus("current")
_Cn1000MediaGatewayStatsTable_Object = MibTable
cn1000MediaGatewayStatsTable = _Cn1000MediaGatewayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14)
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayStatsTable.setStatus("current")
_Cn1000MediaGatewayStatsEntry_Object = MibTableRow
cn1000MediaGatewayStatsEntry = _Cn1000MediaGatewayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14, 1)
)
cn1000MediaGatewayStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsMGIndex"),
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayStatsEntry.setStatus("current")


class _Cn1000StatsMGIndex_Type(Integer32):
    """Custom type cn1000StatsMGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000StatsMGIndex_Type.__name__ = "Integer32"
_Cn1000StatsMGIndex_Object = MibTableColumn
cn1000StatsMGIndex = _Cn1000StatsMGIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14, 1, 1),
    _Cn1000StatsMGIndex_Type()
)
cn1000StatsMGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMGIndex.setStatus("current")
_Cn1000StatsMGOperState_Type = Cn1000VoiceLnServOperState
_Cn1000StatsMGOperState_Object = MibTableColumn
cn1000StatsMGOperState = _Cn1000StatsMGOperState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14, 1, 2),
    _Cn1000StatsMGOperState_Type()
)
cn1000StatsMGOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMGOperState.setStatus("current")


class _Cn1000StatsMGSuccessfullConnections_Type(Integer32):
    """Custom type cn1000StatsMGSuccessfullConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000StatsMGSuccessfullConnections_Type.__name__ = "Integer32"
_Cn1000StatsMGSuccessfullConnections_Object = MibTableColumn
cn1000StatsMGSuccessfullConnections = _Cn1000StatsMGSuccessfullConnections_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14, 1, 3),
    _Cn1000StatsMGSuccessfullConnections_Type()
)
cn1000StatsMGSuccessfullConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMGSuccessfullConnections.setStatus("current")


class _Cn1000StatsMGUnsuccessfullConnections_Type(Integer32):
    """Custom type cn1000StatsMGUnsuccessfullConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000StatsMGUnsuccessfullConnections_Type.__name__ = "Integer32"
_Cn1000StatsMGUnsuccessfullConnections_Object = MibTableColumn
cn1000StatsMGUnsuccessfullConnections = _Cn1000StatsMGUnsuccessfullConnections_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14, 1, 4),
    _Cn1000StatsMGUnsuccessfullConnections_Type()
)
cn1000StatsMGUnsuccessfullConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMGUnsuccessfullConnections.setStatus("current")
_Cn1000StatsMGAdminState_Type = Cn1000VoiceLnServAdminState
_Cn1000StatsMGAdminState_Object = MibTableColumn
cn1000StatsMGAdminState = _Cn1000StatsMGAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 14, 1, 5),
    _Cn1000StatsMGAdminState_Type()
)
cn1000StatsMGAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000StatsMGAdminState.setStatus("current")
_Cn1000MediaGatewayLineStatsTable_Object = MibTable
cn1000MediaGatewayLineStatsTable = _Cn1000MediaGatewayLineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15)
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineStatsTable.setStatus("current")
_Cn1000MediaGatewayLineStatsEntry_Object = MibTableRow
cn1000MediaGatewayLineStatsEntry = _Cn1000MediaGatewayLineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1)
)
cn1000MediaGatewayLineStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsMediaGatewayIndex"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsMediaGatewayLineShelf"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsMediaGatewayLineSlot"),
    (0, "CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsMediaGatewayLinePort"),
)
if mibBuilder.loadTexts:
    cn1000MediaGatewayLineStatsEntry.setStatus("current")


class _Cn1000StatsMediaGatewayIndex_Type(Integer32):
    """Custom type cn1000StatsMediaGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Cn1000StatsMediaGatewayIndex_Type.__name__ = "Integer32"
_Cn1000StatsMediaGatewayIndex_Object = MibTableColumn
cn1000StatsMediaGatewayIndex = _Cn1000StatsMediaGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 1),
    _Cn1000StatsMediaGatewayIndex_Type()
)
cn1000StatsMediaGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayIndex.setStatus("current")


class _Cn1000StatsMediaGatewayLineShelf_Type(Integer32):
    """Custom type cn1000StatsMediaGatewayLineShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cn1000StatsMediaGatewayLineShelf_Type.__name__ = "Integer32"
_Cn1000StatsMediaGatewayLineShelf_Object = MibTableColumn
cn1000StatsMediaGatewayLineShelf = _Cn1000StatsMediaGatewayLineShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 2),
    _Cn1000StatsMediaGatewayLineShelf_Type()
)
cn1000StatsMediaGatewayLineShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayLineShelf.setStatus("current")


class _Cn1000StatsMediaGatewayLineSlot_Type(Integer32):
    """Custom type cn1000StatsMediaGatewayLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cn1000StatsMediaGatewayLineSlot_Type.__name__ = "Integer32"
_Cn1000StatsMediaGatewayLineSlot_Object = MibTableColumn
cn1000StatsMediaGatewayLineSlot = _Cn1000StatsMediaGatewayLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 3),
    _Cn1000StatsMediaGatewayLineSlot_Type()
)
cn1000StatsMediaGatewayLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayLineSlot.setStatus("current")


class _Cn1000StatsMediaGatewayLinePort_Type(Integer32):
    """Custom type cn1000StatsMediaGatewayLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cn1000StatsMediaGatewayLinePort_Type.__name__ = "Integer32"
_Cn1000StatsMediaGatewayLinePort_Object = MibTableColumn
cn1000StatsMediaGatewayLinePort = _Cn1000StatsMediaGatewayLinePort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 4),
    _Cn1000StatsMediaGatewayLinePort_Type()
)
cn1000StatsMediaGatewayLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayLinePort.setStatus("current")


class _Cn1000StatsMediaGatewayLineAppearance_Type(Integer32):
    """Custom type cn1000StatsMediaGatewayLineAppearance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cn1000StatsMediaGatewayLineAppearance_Type.__name__ = "Integer32"
_Cn1000StatsMediaGatewayLineAppearance_Object = MibTableColumn
cn1000StatsMediaGatewayLineAppearance = _Cn1000StatsMediaGatewayLineAppearance_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 5),
    _Cn1000StatsMediaGatewayLineAppearance_Type()
)
cn1000StatsMediaGatewayLineAppearance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayLineAppearance.setStatus("current")
_Cn1000StatsMediaGatewayLineOperState_Type = Cn1000VoiceLGLineOperState
_Cn1000StatsMediaGatewayLineOperState_Object = MibTableColumn
cn1000StatsMediaGatewayLineOperState = _Cn1000StatsMediaGatewayLineOperState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 6),
    _Cn1000StatsMediaGatewayLineOperState_Type()
)
cn1000StatsMediaGatewayLineOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayLineOperState.setStatus("current")
_Cn1000StatsMediaGatewayLineHookswitchState_Type = Cn1000VoiceLnServHookswitchState
_Cn1000StatsMediaGatewayLineHookswitchState_Object = MibTableColumn
cn1000StatsMediaGatewayLineHookswitchState = _Cn1000StatsMediaGatewayLineHookswitchState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 15, 1, 7),
    _Cn1000StatsMediaGatewayLineHookswitchState_Type()
)
cn1000StatsMediaGatewayLineHookswitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000StatsMediaGatewayLineHookswitchState.setStatus("current")

# Managed Objects groups

cn1000VoiceLineServicesObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 4, 1, 7, 1)
)
cn1000VoiceLineServicesObjectsGroup.setObjects(
      *(("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIfGroupIfIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefLineGroupSystemAddress"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefLineGroupConnectionIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefConfigurationStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefMaxRetryDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefMaxRoundTripDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefInitialRoundTripDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefPendingTimeout"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefRowStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefAdminStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriberId"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionServiceMode"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionSignalMode"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionConfigStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionRowStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIfGroupType"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIfGroupShelf"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIfGroupSlotGroup"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefIfGroupIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupType"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupIfGroupSystemAddress"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupConnectionIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupIfGroupConnectionIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupConfigurationStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRestartInitDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRestartMinDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRestartMaxDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRetryMaxDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupMaxRoundTripDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupInitialRoundTripDelay"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupPendingTimeout"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupInterface"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupInterfaceBracketed"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupSpoofIPAddress"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupLocalMediaIPAddress"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupCodec"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupCodecPacketizationPeriod"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupG726PacketizationRate"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRowStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupAdminStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineSubscriptionLossPadValue"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineSubscriptionConfigurationStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineSubscriptionRowStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000VoiceCrossConnectsF2Cable"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000VoiceCrossConnectsF2Pair"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000VoiceCrossConnectsRowStatus"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefAdminState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefOperState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefConnState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LGRefConnReqAttempts"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LGRefConnReqFailures"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LGRefFailedConnections"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupRefIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionShelf"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionSlot"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionPort"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionAppearance"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionCRV"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubPrimaryServiceState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubSecondaryServiceState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubConnState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubNtwkChannel"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubLineChannel"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubHookswitchState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGOperState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGSuccessfullConnections"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGUnsuccessfullConnections"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupIndex"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineShelf"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineSlot"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLinePort"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineAppearance"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineOperState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionGroupDesc"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineGroupRefDesc"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLineGroupLineHookswitchState"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000LineRefSubscriptionIfType"),
        ("CEM-CN1000-VOICE-LINE-SERVICES", "cn1000StatsLGRefSubscriptionIfType"))
)
if mibBuilder.loadTexts:
    cn1000VoiceLineServicesObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-VOICE-LINE-SERVICES",
    **{"Cn1000VoiceLnServAdminState": Cn1000VoiceLnServAdminState,
       "Cn1000SwitchInterfaceGroupType": Cn1000SwitchInterfaceGroupType,
       "Cn1000CodecType": Cn1000CodecType,
       "Cn1000CodecPacketizationPeriodType": Cn1000CodecPacketizationPeriodType,
       "Cn1000G726PacketizationRateType": Cn1000G726PacketizationRateType,
       "Cn1000VoiceLnServOperState": Cn1000VoiceLnServOperState,
       "Cn1000VoiceLnServConnState": Cn1000VoiceLnServConnState,
       "Cn1000VoiceLnServSubscriptionConnState": Cn1000VoiceLnServSubscriptionConnState,
       "Cn1000VoiceLnServHookswitchState": Cn1000VoiceLnServHookswitchState,
       "Cn1000VoiceLGLineOperState": Cn1000VoiceLGLineOperState,
       "Cn1000VoiceIpPortType": Cn1000VoiceIpPortType,
       "cn1000VoiceLineServicesModule": cn1000VoiceLineServicesModule,
       "cn1000LineGroupReferenceTable": cn1000LineGroupReferenceTable,
       "cn1000LineGroupReferenceEntry": cn1000LineGroupReferenceEntry,
       "cn1000LineGroupRefIndex": cn1000LineGroupRefIndex,
       "cn1000LineGroupRefIfGroupIfIndex": cn1000LineGroupRefIfGroupIfIndex,
       "cn1000LineGroupRefLineGroupSystemAddress": cn1000LineGroupRefLineGroupSystemAddress,
       "cn1000LineGroupRefLineGroupConnectionIndex": cn1000LineGroupRefLineGroupConnectionIndex,
       "cn1000LineGroupRefConfigurationStatus": cn1000LineGroupRefConfigurationStatus,
       "cn1000LineGroupRefMaxRetryDelay": cn1000LineGroupRefMaxRetryDelay,
       "cn1000LineGroupRefMaxRoundTripDelay": cn1000LineGroupRefMaxRoundTripDelay,
       "cn1000LineGroupRefInitialRoundTripDelay": cn1000LineGroupRefInitialRoundTripDelay,
       "cn1000LineGroupRefPendingTimeout": cn1000LineGroupRefPendingTimeout,
       "cn1000LineGroupRefRowStatus": cn1000LineGroupRefRowStatus,
       "cn1000LineGroupRefAdminStatus": cn1000LineGroupRefAdminStatus,
       "cn1000LineGroupRefDesc": cn1000LineGroupRefDesc,
       "cn1000LineGroupRefIfGroupType": cn1000LineGroupRefIfGroupType,
       "cn1000LineGroupRefIfGroupShelf": cn1000LineGroupRefIfGroupShelf,
       "cn1000LineGroupRefIfGroupSlotGroup": cn1000LineGroupRefIfGroupSlotGroup,
       "cn1000LineGroupRefIfGroupIndex": cn1000LineGroupRefIfGroupIndex,
       "cn1000LineRefSubscriptionTable": cn1000LineRefSubscriptionTable,
       "cn1000LineRefSubscriptionEntry": cn1000LineRefSubscriptionEntry,
       "cn1000LineRefSubscriptionShelf": cn1000LineRefSubscriptionShelf,
       "cn1000LineRefSubscriptionSlot": cn1000LineRefSubscriptionSlot,
       "cn1000LineRefSubscriptionPort": cn1000LineRefSubscriptionPort,
       "cn1000LineRefSubscriptionAppearance": cn1000LineRefSubscriptionAppearance,
       "cn1000LineRefSubscriberId": cn1000LineRefSubscriberId,
       "cn1000LineRefSubscriptionIfType": cn1000LineRefSubscriptionIfType,
       "cn1000LineRefSubscriptionServiceMode": cn1000LineRefSubscriptionServiceMode,
       "cn1000LineRefSubscriptionSignalMode": cn1000LineRefSubscriptionSignalMode,
       "cn1000LineRefSubscriptionConfigStatus": cn1000LineRefSubscriptionConfigStatus,
       "cn1000LineRefSubscriptionRowStatus": cn1000LineRefSubscriptionRowStatus,
       "cn1000LineRefSubscriptionGroupDesc": cn1000LineRefSubscriptionGroupDesc,
       "cn1000LineGroupTable": cn1000LineGroupTable,
       "cn1000LineGroupEntry": cn1000LineGroupEntry,
       "cn1000LineGroupIndex": cn1000LineGroupIndex,
       "cn1000LineGroupType": cn1000LineGroupType,
       "cn1000LineGroupIfGroupSystemAddress": cn1000LineGroupIfGroupSystemAddress,
       "cn1000LineGroupConnectionIndex": cn1000LineGroupConnectionIndex,
       "cn1000LineGroupIfGroupConnectionIndex": cn1000LineGroupIfGroupConnectionIndex,
       "cn1000LineGroupConfigurationStatus": cn1000LineGroupConfigurationStatus,
       "cn1000LineGroupRestartInitDelay": cn1000LineGroupRestartInitDelay,
       "cn1000LineGroupRestartMinDelay": cn1000LineGroupRestartMinDelay,
       "cn1000LineGroupRestartMaxDelay": cn1000LineGroupRestartMaxDelay,
       "cn1000LineGroupRetryMaxDelay": cn1000LineGroupRetryMaxDelay,
       "cn1000LineGroupMaxRoundTripDelay": cn1000LineGroupMaxRoundTripDelay,
       "cn1000LineGroupInitialRoundTripDelay": cn1000LineGroupInitialRoundTripDelay,
       "cn1000LineGroupPendingTimeout": cn1000LineGroupPendingTimeout,
       "cn1000LineGroupInterface": cn1000LineGroupInterface,
       "cn1000LineGroupInterfaceBracketed": cn1000LineGroupInterfaceBracketed,
       "cn1000LineGroupSpoofIPAddress": cn1000LineGroupSpoofIPAddress,
       "cn1000LineGroupLocalMediaIPAddress": cn1000LineGroupLocalMediaIPAddress,
       "cn1000LineGroupCodec": cn1000LineGroupCodec,
       "cn1000LineGroupCodecPacketizationPeriod": cn1000LineGroupCodecPacketizationPeriod,
       "cn1000LineGroupG726PacketizationRate": cn1000LineGroupG726PacketizationRate,
       "cn1000LineGroupRowStatus": cn1000LineGroupRowStatus,
       "cn1000LineGroupAdminStatus": cn1000LineGroupAdminStatus,
       "cn1000LineSubscriptionTable": cn1000LineSubscriptionTable,
       "cn1000LineSubscriptionEntry": cn1000LineSubscriptionEntry,
       "cn1000LineSubscriptionLineGroupIndex": cn1000LineSubscriptionLineGroupIndex,
       "cn1000LineSubscriptionLineIfIndex": cn1000LineSubscriptionLineIfIndex,
       "cn1000LineSubscriptionLossPadValue": cn1000LineSubscriptionLossPadValue,
       "cn1000LineSubscriptionConfigurationStatus": cn1000LineSubscriptionConfigurationStatus,
       "cn1000LineSubscriptionRowStatus": cn1000LineSubscriptionRowStatus,
       "cn1000VoiceCrossConnectsTable": cn1000VoiceCrossConnectsTable,
       "cn1000VoiceCrossConnectsEntry": cn1000VoiceCrossConnectsEntry,
       "cn1000VoiceCrossConnectsF1Cable": cn1000VoiceCrossConnectsF1Cable,
       "cn1000VoiceCrossConnectsF1Pair": cn1000VoiceCrossConnectsF1Pair,
       "cn1000VoiceCrossConnectsF2Cable": cn1000VoiceCrossConnectsF2Cable,
       "cn1000VoiceCrossConnectsF2Pair": cn1000VoiceCrossConnectsF2Pair,
       "cn1000VoiceCrossConnectsRowStatus": cn1000VoiceCrossConnectsRowStatus,
       "cn1000VoiceLneServicesConformance": cn1000VoiceLneServicesConformance,
       "cn1000VoiceLineServicesObjectsGroup": cn1000VoiceLineServicesObjectsGroup,
       "cn1000LineGroupRefStatsTable": cn1000LineGroupRefStatsTable,
       "cn1000LineGroupRefStatsEntry": cn1000LineGroupRefStatsEntry,
       "cn1000StatsLGRefIndex": cn1000StatsLGRefIndex,
       "cn1000StatsLGRefAdminState": cn1000StatsLGRefAdminState,
       "cn1000StatsLGRefOperState": cn1000StatsLGRefOperState,
       "cn1000StatsLGRefConnState": cn1000StatsLGRefConnState,
       "cn1000LGRefConnReqAttempts": cn1000LGRefConnReqAttempts,
       "cn1000LGRefConnReqFailures": cn1000LGRefConnReqFailures,
       "cn1000LGRefFailedConnections": cn1000LGRefFailedConnections,
       "cn1000LineGroupRefSubscriptionsStatsTable": cn1000LineGroupRefSubscriptionsStatsTable,
       "cn1000LineGroupRefSubscriptionsStatsEntry": cn1000LineGroupRefSubscriptionsStatsEntry,
       "cn1000StatsLineGroupRefIndex": cn1000StatsLineGroupRefIndex,
       "cn1000StatsLGRefSubscriptionShelf": cn1000StatsLGRefSubscriptionShelf,
       "cn1000StatsLGRefSubscriptionSlot": cn1000StatsLGRefSubscriptionSlot,
       "cn1000StatsLGRefSubscriptionPort": cn1000StatsLGRefSubscriptionPort,
       "cn1000StatsLGRefSubscriptionAppearance": cn1000StatsLGRefSubscriptionAppearance,
       "cn1000StatsLGRefSubscriptionCRV": cn1000StatsLGRefSubscriptionCRV,
       "cn1000StatsLGRefSubscriptionIfType": cn1000StatsLGRefSubscriptionIfType,
       "cn1000StatsLGRefSubPrimaryServiceState": cn1000StatsLGRefSubPrimaryServiceState,
       "cn1000StatsLGRefSubSecondaryServiceState": cn1000StatsLGRefSubSecondaryServiceState,
       "cn1000StatsLGRefSubConnState": cn1000StatsLGRefSubConnState,
       "cn1000StatsLGRefSubNtwkChannel": cn1000StatsLGRefSubNtwkChannel,
       "cn1000StatsLGRefSubLineChannel": cn1000StatsLGRefSubLineChannel,
       "cn1000StatsLGRefSubHookswitchState": cn1000StatsLGRefSubHookswitchState,
       "cn1000LineGroupStatsTable": cn1000LineGroupStatsTable,
       "cn1000LineGroupStatsEntry": cn1000LineGroupStatsEntry,
       "cn1000StatsLGIndex": cn1000StatsLGIndex,
       "cn1000StatsLGOperState": cn1000StatsLGOperState,
       "cn1000StatsLGSuccessfullConnections": cn1000StatsLGSuccessfullConnections,
       "cn1000StatsLGUnsuccessfullConnections": cn1000StatsLGUnsuccessfullConnections,
       "cn1000LineSubscriptionStatsTable": cn1000LineSubscriptionStatsTable,
       "cn1000LineSubscriptionStatsEntry": cn1000LineSubscriptionStatsEntry,
       "cn1000StatsLineGroupIndex": cn1000StatsLineGroupIndex,
       "cn1000StatsLineGroupLineShelf": cn1000StatsLineGroupLineShelf,
       "cn1000StatsLineGroupLineSlot": cn1000StatsLineGroupLineSlot,
       "cn1000StatsLineGroupLinePort": cn1000StatsLineGroupLinePort,
       "cn1000StatsLineGroupLineAppearance": cn1000StatsLineGroupLineAppearance,
       "cn1000StatsLineGroupLineOperState": cn1000StatsLineGroupLineOperState,
       "cn1000StatsLineGroupLineHookswitchState": cn1000StatsLineGroupLineHookswitchState,
       "cn1000MediaGatewayTable": cn1000MediaGatewayTable,
       "cn1000MediaGatewayEntry": cn1000MediaGatewayEntry,
       "cn1000MGIndex": cn1000MGIndex,
       "cn1000MediaGatewayType": cn1000MediaGatewayType,
       "cn1000MediaGatewayMgcIpAddress": cn1000MediaGatewayMgcIpAddress,
       "cn1000MediaGatewaySignallingPort": cn1000MediaGatewaySignallingPort,
       "cn1000MediaGatewayMgcPort": cn1000MediaGatewayMgcPort,
       "cn1000MediaGatewayConfigurationStatus": cn1000MediaGatewayConfigurationStatus,
       "cn1000MediaGatewayRestartInitDelay": cn1000MediaGatewayRestartInitDelay,
       "cn1000MediaGatewayRestartMinDelay": cn1000MediaGatewayRestartMinDelay,
       "cn1000MediaGatewayRestartMaxDelay": cn1000MediaGatewayRestartMaxDelay,
       "cn1000MediaGatewayRetryMaxDelay": cn1000MediaGatewayRetryMaxDelay,
       "cn1000MediaGatewayMaxRoundTripDelay": cn1000MediaGatewayMaxRoundTripDelay,
       "cn1000MediaGatewayInitialRoundTripDelay": cn1000MediaGatewayInitialRoundTripDelay,
       "cn1000MediaGatewayPendingTimeout": cn1000MediaGatewayPendingTimeout,
       "cn1000MediaGatewaySignallingInterface": cn1000MediaGatewaySignallingInterface,
       "cn1000MediaGatewayInterfaceBracketed": cn1000MediaGatewayInterfaceBracketed,
       "cn1000MediaGatewayMgAlias": cn1000MediaGatewayMgAlias,
       "cn1000MediaGatewayMediaInterface": cn1000MediaGatewayMediaInterface,
       "cn1000MediaGatewayCodec": cn1000MediaGatewayCodec,
       "cn1000MediaGatewayCodecPacketizationMin": cn1000MediaGatewayCodecPacketizationMin,
       "cn1000MediaGatewayCodecPacketizationMax": cn1000MediaGatewayCodecPacketizationMax,
       "cn1000MediaGatewayCodecSilenceSupp": cn1000MediaGatewayCodecSilenceSupp,
       "cn1000MediaGatewayUdpStartRange": cn1000MediaGatewayUdpStartRange,
       "cn1000MediaGatewaySigPortType": cn1000MediaGatewaySigPortType,
       "cn1000MediaGatewayMgcType": cn1000MediaGatewayMgcType,
       "cn1000MediaGatewayIpTypeOfService": cn1000MediaGatewayIpTypeOfService,
       "cn1000MediaGatewayIpTimeToLive": cn1000MediaGatewayIpTimeToLive,
       "cn1000MediaGatewayLineIdPrefix": cn1000MediaGatewayLineIdPrefix,
       "cn1000MediaGatewayRowStatus": cn1000MediaGatewayRowStatus,
       "cn1000MediaGatewayAdminStatus": cn1000MediaGatewayAdminStatus,
       "cn1000MediaGatewayLineTable": cn1000MediaGatewayLineTable,
       "cn1000MediaGatewayLineEntry": cn1000MediaGatewayLineEntry,
       "cn1000MediaGatewayGroupIndex": cn1000MediaGatewayGroupIndex,
       "cn1000MediaGatewayLineIfIndex": cn1000MediaGatewayLineIfIndex,
       "cn1000MediaGatewayLineLossPadValue": cn1000MediaGatewayLineLossPadValue,
       "cn1000MediaGatewayLineConfigurationStatus": cn1000MediaGatewayLineConfigurationStatus,
       "cn1000MediaGatewayLineRowStatus": cn1000MediaGatewayLineRowStatus,
       "cn1000MediaGatewayStatsTable": cn1000MediaGatewayStatsTable,
       "cn1000MediaGatewayStatsEntry": cn1000MediaGatewayStatsEntry,
       "cn1000StatsMGIndex": cn1000StatsMGIndex,
       "cn1000StatsMGOperState": cn1000StatsMGOperState,
       "cn1000StatsMGSuccessfullConnections": cn1000StatsMGSuccessfullConnections,
       "cn1000StatsMGUnsuccessfullConnections": cn1000StatsMGUnsuccessfullConnections,
       "cn1000StatsMGAdminState": cn1000StatsMGAdminState,
       "cn1000MediaGatewayLineStatsTable": cn1000MediaGatewayLineStatsTable,
       "cn1000MediaGatewayLineStatsEntry": cn1000MediaGatewayLineStatsEntry,
       "cn1000StatsMediaGatewayIndex": cn1000StatsMediaGatewayIndex,
       "cn1000StatsMediaGatewayLineShelf": cn1000StatsMediaGatewayLineShelf,
       "cn1000StatsMediaGatewayLineSlot": cn1000StatsMediaGatewayLineSlot,
       "cn1000StatsMediaGatewayLinePort": cn1000StatsMediaGatewayLinePort,
       "cn1000StatsMediaGatewayLineAppearance": cn1000StatsMediaGatewayLineAppearance,
       "cn1000StatsMediaGatewayLineOperState": cn1000StatsMediaGatewayLineOperState,
       "cn1000StatsMediaGatewayLineHookswitchState": cn1000StatsMediaGatewayLineHookswitchState}
)
