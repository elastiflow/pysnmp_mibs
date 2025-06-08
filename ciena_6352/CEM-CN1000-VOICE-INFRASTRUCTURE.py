# SNMP MIB module (CEM-CN1000-VOICE-INFRASTRUCTURE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-VOICE-INFRASTRUCTURE.mib
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
 Cn1000PortRange,
 Cn1000ShelfRange,
 Cn1000SlotRange,
 cn1000VoiceInfrastructure) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000ConfigurationStatus",
    "Cn1000PortRange",
    "Cn1000ShelfRange",
    "Cn1000SlotRange",
    "cn1000VoiceInfrastructure")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

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

cn1000VoiceInfrastructureModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cn1000VoiceInfrastructureModule.setRevisions(
        ("2002-02-21 10:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000VoiceInfrastructureSignalingEntityType(TextualConvention, Integer32):
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
        *(("cnT1Card", 1),
          ("cnCeCard", 2),
          ("cnE1Card", 3))
    )



class Cn1000VoiceInfrastructureSignalingEndpointType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cnLineSideWanInterface", 1),
          ("cnSwitchSideWanInterface", 2),
          ("cnT1Card", 3),
          ("cnCeCard", 4),
          ("cnVoiceSubtending", 5),
          ("cnE1Card", 6))
    )



class Cn1000VoiceInfrastructureMediaEndpointType(TextualConvention, Integer32):
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
        *(("cnT1Card", 1),
          ("cnLineCard", 2),
          ("cnOnu", 3),
          ("cnEnhancedDTS", 4),
          ("cnWanInterface", 5),
          ("cnVoiceSubtending", 6),
          ("cnChannelBank", 7),
          ("cnE1Card", 8),
          ("cnOlt", 9))
    )



class Cn1000NetworkPathIdentifierRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )



class Cn1000VoiceSubtendingConnectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnVoiceSignaling", 1),
          ("cnVoiceMedia", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000SignalingConfigTable_Object = MibTable
cn1000SignalingConfigTable = _Cn1000SignalingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cn1000SignalingConfigTable.setStatus("current")
_Cn1000SignalingConfigEntry_Object = MibTableRow
cn1000SignalingConfigEntry = _Cn1000SignalingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1)
)
cn1000SignalingConfigEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000Shelf"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SlotGroup"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000Port"),
)
if mibBuilder.loadTexts:
    cn1000SignalingConfigEntry.setStatus("current")
_Cn1000Shelf_Type = Cn1000ShelfRange
_Cn1000Shelf_Object = MibTableColumn
cn1000Shelf = _Cn1000Shelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 1),
    _Cn1000Shelf_Type()
)
cn1000Shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000Shelf.setStatus("current")
_Cn1000SlotGroup_Type = CnSlotGroupNameType
_Cn1000SlotGroup_Object = MibTableColumn
cn1000SlotGroup = _Cn1000SlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 2),
    _Cn1000SlotGroup_Type()
)
cn1000SlotGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SlotGroup.setStatus("current")
_Cn1000Port_Type = Cn1000PortRange
_Cn1000Port_Object = MibTableColumn
cn1000Port = _Cn1000Port_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 3),
    _Cn1000Port_Type()
)
cn1000Port.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000Port.setStatus("current")


class _Cn1000SignalingSystemAddress_Type(OctetString):
    """Custom type cn1000SignalingSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cn1000SignalingSystemAddress_Type.__name__ = "OctetString"
_Cn1000SignalingSystemAddress_Object = MibTableColumn
cn1000SignalingSystemAddress = _Cn1000SignalingSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 4),
    _Cn1000SignalingSystemAddress_Type()
)
cn1000SignalingSystemAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingSystemAddress.setStatus("current")


class _Cn1000SignalingSubnet_Type(OctetString):
    """Custom type cn1000SignalingSubnet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cn1000SignalingSubnet_Type.__name__ = "OctetString"
_Cn1000SignalingSubnet_Object = MibTableColumn
cn1000SignalingSubnet = _Cn1000SignalingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 5),
    _Cn1000SignalingSubnet_Type()
)
cn1000SignalingSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingSubnet.setStatus("current")
_Cn1000SignalingEntityType_Type = Cn1000VoiceInfrastructureSignalingEntityType
_Cn1000SignalingEntityType_Object = MibTableColumn
cn1000SignalingEntityType = _Cn1000SignalingEntityType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 6),
    _Cn1000SignalingEntityType_Type()
)
cn1000SignalingEntityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingEntityType.setStatus("current")
_Cn1000SignalingConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000SignalingConfigurationStatus_Object = MibTableColumn
cn1000SignalingConfigurationStatus = _Cn1000SignalingConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 7),
    _Cn1000SignalingConfigurationStatus_Type()
)
cn1000SignalingConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingConfigurationStatus.setStatus("current")
_Cn1000SignalingConfigEntryRowStatus_Type = RowStatus
_Cn1000SignalingConfigEntryRowStatus_Object = MibTableColumn
cn1000SignalingConfigEntryRowStatus = _Cn1000SignalingConfigEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 2, 1, 9),
    _Cn1000SignalingConfigEntryRowStatus_Type()
)
cn1000SignalingConfigEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingConfigEntryRowStatus.setStatus("current")
_Cn1000SignalingEndpointTable_Object = MibTable
cn1000SignalingEndpointTable = _Cn1000SignalingEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cn1000SignalingEndpointTable.setStatus("current")
_Cn1000SignalingEndpointEntry_Object = MibTableRow
cn1000SignalingEndpointEntry = _Cn1000SignalingEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1)
)
cn1000SignalingEndpointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingEndpointVpi"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingEndpointVci"),
)
if mibBuilder.loadTexts:
    cn1000SignalingEndpointEntry.setStatus("current")


class _Cn1000SignalingEndpointVpi_Type(Integer32):
    """Custom type cn1000SignalingEndpointVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000SignalingEndpointVpi_Type.__name__ = "Integer32"
_Cn1000SignalingEndpointVpi_Object = MibTableColumn
cn1000SignalingEndpointVpi = _Cn1000SignalingEndpointVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1, 1),
    _Cn1000SignalingEndpointVpi_Type()
)
cn1000SignalingEndpointVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SignalingEndpointVpi.setStatus("current")


class _Cn1000SignalingEndpointVci_Type(Integer32):
    """Custom type cn1000SignalingEndpointVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SignalingEndpointVci_Type.__name__ = "Integer32"
_Cn1000SignalingEndpointVci_Object = MibTableColumn
cn1000SignalingEndpointVci = _Cn1000SignalingEndpointVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1, 2),
    _Cn1000SignalingEndpointVci_Type()
)
cn1000SignalingEndpointVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SignalingEndpointVci.setStatus("current")
_Cn1000SignalingEndpointType_Type = Cn1000VoiceInfrastructureSignalingEndpointType
_Cn1000SignalingEndpointType_Object = MibTableColumn
cn1000SignalingEndpointType = _Cn1000SignalingEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1, 3),
    _Cn1000SignalingEndpointType_Type()
)
cn1000SignalingEndpointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingEndpointType.setStatus("current")


class _Cn1000SignalingRemoteSystemAddress_Type(OctetString):
    """Custom type cn1000SignalingRemoteSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cn1000SignalingRemoteSystemAddress_Type.__name__ = "OctetString"
_Cn1000SignalingRemoteSystemAddress_Object = MibTableColumn
cn1000SignalingRemoteSystemAddress = _Cn1000SignalingRemoteSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1, 4),
    _Cn1000SignalingRemoteSystemAddress_Type()
)
cn1000SignalingRemoteSystemAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingRemoteSystemAddress.setStatus("current")
_Cn1000SignalingEndpointConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000SignalingEndpointConfigurationStatus_Object = MibTableColumn
cn1000SignalingEndpointConfigurationStatus = _Cn1000SignalingEndpointConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1, 5),
    _Cn1000SignalingEndpointConfigurationStatus_Type()
)
cn1000SignalingEndpointConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingEndpointConfigurationStatus.setStatus("current")
_Cn1000SignalingEndpointRowStatus_Type = RowStatus
_Cn1000SignalingEndpointRowStatus_Object = MibTableColumn
cn1000SignalingEndpointRowStatus = _Cn1000SignalingEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 6, 1, 7),
    _Cn1000SignalingEndpointRowStatus_Type()
)
cn1000SignalingEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingEndpointRowStatus.setStatus("current")
_Cn1000SignalingConnectionTable_Object = MibTable
cn1000SignalingConnectionTable = _Cn1000SignalingConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cn1000SignalingConnectionTable.setStatus("current")
_Cn1000SignalingConnectionEntry_Object = MibTableRow
cn1000SignalingConnectionEntry = _Cn1000SignalingConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1)
)
cn1000SignalingConnectionEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionLineSideIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionLineSideVpi"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionLineSideVci"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionSwitchSideIfIndex"),
)
if mibBuilder.loadTexts:
    cn1000SignalingConnectionEntry.setStatus("current")
_Cn1000SignalingConnectionLineSideIfIndex_Type = InterfaceIndex
_Cn1000SignalingConnectionLineSideIfIndex_Object = MibTableColumn
cn1000SignalingConnectionLineSideIfIndex = _Cn1000SignalingConnectionLineSideIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 1),
    _Cn1000SignalingConnectionLineSideIfIndex_Type()
)
cn1000SignalingConnectionLineSideIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionLineSideIfIndex.setStatus("current")


class _Cn1000SignalingConnectionLineSideVpi_Type(Integer32):
    """Custom type cn1000SignalingConnectionLineSideVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000SignalingConnectionLineSideVpi_Type.__name__ = "Integer32"
_Cn1000SignalingConnectionLineSideVpi_Object = MibTableColumn
cn1000SignalingConnectionLineSideVpi = _Cn1000SignalingConnectionLineSideVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 6),
    _Cn1000SignalingConnectionLineSideVpi_Type()
)
cn1000SignalingConnectionLineSideVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionLineSideVpi.setStatus("current")


class _Cn1000SignalingConnectionLineSideVci_Type(Integer32):
    """Custom type cn1000SignalingConnectionLineSideVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SignalingConnectionLineSideVci_Type.__name__ = "Integer32"
_Cn1000SignalingConnectionLineSideVci_Object = MibTableColumn
cn1000SignalingConnectionLineSideVci = _Cn1000SignalingConnectionLineSideVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 7),
    _Cn1000SignalingConnectionLineSideVci_Type()
)
cn1000SignalingConnectionLineSideVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionLineSideVci.setStatus("current")
_Cn1000SignalingConnectionSwitchSideIfIndex_Type = InterfaceIndex
_Cn1000SignalingConnectionSwitchSideIfIndex_Object = MibTableColumn
cn1000SignalingConnectionSwitchSideIfIndex = _Cn1000SignalingConnectionSwitchSideIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 8),
    _Cn1000SignalingConnectionSwitchSideIfIndex_Type()
)
cn1000SignalingConnectionSwitchSideIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionSwitchSideIfIndex.setStatus("current")
_Cn1000SignalingConnectionLineSideType_Type = Cn1000VoiceInfrastructureSignalingEndpointType
_Cn1000SignalingConnectionLineSideType_Object = MibTableColumn
cn1000SignalingConnectionLineSideType = _Cn1000SignalingConnectionLineSideType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 13),
    _Cn1000SignalingConnectionLineSideType_Type()
)
cn1000SignalingConnectionLineSideType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionLineSideType.setStatus("current")
_Cn1000SignalingConnectionSwitchSideType_Type = Cn1000VoiceInfrastructureSignalingEndpointType
_Cn1000SignalingConnectionSwitchSideType_Object = MibTableColumn
cn1000SignalingConnectionSwitchSideType = _Cn1000SignalingConnectionSwitchSideType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 14),
    _Cn1000SignalingConnectionSwitchSideType_Type()
)
cn1000SignalingConnectionSwitchSideType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionSwitchSideType.setStatus("current")


class _Cn1000SignalingConnectionInternalSwitchSideVpi_Type(Integer32):
    """Custom type cn1000SignalingConnectionInternalSwitchSideVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000SignalingConnectionInternalSwitchSideVpi_Type.__name__ = "Integer32"
_Cn1000SignalingConnectionInternalSwitchSideVpi_Object = MibTableColumn
cn1000SignalingConnectionInternalSwitchSideVpi = _Cn1000SignalingConnectionInternalSwitchSideVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 17),
    _Cn1000SignalingConnectionInternalSwitchSideVpi_Type()
)
cn1000SignalingConnectionInternalSwitchSideVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionInternalSwitchSideVpi.setStatus("current")


class _Cn1000SignalingConnectionInternalSwitchSideVci_Type(Integer32):
    """Custom type cn1000SignalingConnectionInternalSwitchSideVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SignalingConnectionInternalSwitchSideVci_Type.__name__ = "Integer32"
_Cn1000SignalingConnectionInternalSwitchSideVci_Object = MibTableColumn
cn1000SignalingConnectionInternalSwitchSideVci = _Cn1000SignalingConnectionInternalSwitchSideVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 18),
    _Cn1000SignalingConnectionInternalSwitchSideVci_Type()
)
cn1000SignalingConnectionInternalSwitchSideVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionInternalSwitchSideVci.setStatus("current")
_Cn1000SignalingConnectionConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000SignalingConnectionConfigurationStatus_Object = MibTableColumn
cn1000SignalingConnectionConfigurationStatus = _Cn1000SignalingConnectionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 20),
    _Cn1000SignalingConnectionConfigurationStatus_Type()
)
cn1000SignalingConnectionConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionConfigurationStatus.setStatus("current")
_Cn1000SignalingConnectionRowStatus_Type = RowStatus
_Cn1000SignalingConnectionRowStatus_Object = MibTableColumn
cn1000SignalingConnectionRowStatus = _Cn1000SignalingConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 21),
    _Cn1000SignalingConnectionRowStatus_Type()
)
cn1000SignalingConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionRowStatus.setStatus("current")


class _Cn1000SignalingConnectionDSPvcTag_Type(OctetString):
    """Custom type cn1000SignalingConnectionDSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000SignalingConnectionDSPvcTag_Type.__name__ = "OctetString"
_Cn1000SignalingConnectionDSPvcTag_Object = MibTableColumn
cn1000SignalingConnectionDSPvcTag = _Cn1000SignalingConnectionDSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 22),
    _Cn1000SignalingConnectionDSPvcTag_Type()
)
cn1000SignalingConnectionDSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionDSPvcTag.setStatus("current")


class _Cn1000SignalingConnectionUSPvcTag_Type(OctetString):
    """Custom type cn1000SignalingConnectionUSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000SignalingConnectionUSPvcTag_Type.__name__ = "OctetString"
_Cn1000SignalingConnectionUSPvcTag_Object = MibTableColumn
cn1000SignalingConnectionUSPvcTag = _Cn1000SignalingConnectionUSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 9, 1, 23),
    _Cn1000SignalingConnectionUSPvcTag_Type()
)
cn1000SignalingConnectionUSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SignalingConnectionUSPvcTag.setStatus("current")
_Cn1000MediaEndpointTable_Object = MibTable
cn1000MediaEndpointTable = _Cn1000MediaEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13)
)
if mibBuilder.loadTexts:
    cn1000MediaEndpointTable.setStatus("current")
_Cn1000MediaEndpointEntry_Object = MibTableRow
cn1000MediaEndpointEntry = _Cn1000MediaEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1)
)
cn1000MediaEndpointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointVpi"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointVci"),
)
if mibBuilder.loadTexts:
    cn1000MediaEndpointEntry.setStatus("current")


class _Cn1000MediaEndpointVpi_Type(Integer32):
    """Custom type cn1000MediaEndpointVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cn1000MediaEndpointVpi_Type.__name__ = "Integer32"
_Cn1000MediaEndpointVpi_Object = MibTableColumn
cn1000MediaEndpointVpi = _Cn1000MediaEndpointVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 1),
    _Cn1000MediaEndpointVpi_Type()
)
cn1000MediaEndpointVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaEndpointVpi.setStatus("current")


class _Cn1000MediaEndpointVci_Type(Integer32):
    """Custom type cn1000MediaEndpointVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaEndpointVci_Type.__name__ = "Integer32"
_Cn1000MediaEndpointVci_Object = MibTableColumn
cn1000MediaEndpointVci = _Cn1000MediaEndpointVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 2),
    _Cn1000MediaEndpointVci_Type()
)
cn1000MediaEndpointVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaEndpointVci.setStatus("current")
_Cn1000MediaEndpointRemoteEndpointType_Type = Cn1000VoiceInfrastructureMediaEndpointType
_Cn1000MediaEndpointRemoteEndpointType_Object = MibTableColumn
cn1000MediaEndpointRemoteEndpointType = _Cn1000MediaEndpointRemoteEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 3),
    _Cn1000MediaEndpointRemoteEndpointType_Type()
)
cn1000MediaEndpointRemoteEndpointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointRemoteEndpointType.setStatus("current")


class _Cn1000MediaEndpointRemoteSystemAddress_Type(OctetString):
    """Custom type cn1000MediaEndpointRemoteSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cn1000MediaEndpointRemoteSystemAddress_Type.__name__ = "OctetString"
_Cn1000MediaEndpointRemoteSystemAddress_Object = MibTableColumn
cn1000MediaEndpointRemoteSystemAddress = _Cn1000MediaEndpointRemoteSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 5),
    _Cn1000MediaEndpointRemoteSystemAddress_Type()
)
cn1000MediaEndpointRemoteSystemAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointRemoteSystemAddress.setStatus("current")
_Cn1000MediaEndpointRemoteLineCardShelf_Type = Cn1000ShelfRange
_Cn1000MediaEndpointRemoteLineCardShelf_Object = MibTableColumn
cn1000MediaEndpointRemoteLineCardShelf = _Cn1000MediaEndpointRemoteLineCardShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 6),
    _Cn1000MediaEndpointRemoteLineCardShelf_Type()
)
cn1000MediaEndpointRemoteLineCardShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointRemoteLineCardShelf.setStatus("current")
_Cn1000MediaEndpointRemoteLineCardSlot_Type = Cn1000SlotRange
_Cn1000MediaEndpointRemoteLineCardSlot_Object = MibTableColumn
cn1000MediaEndpointRemoteLineCardSlot = _Cn1000MediaEndpointRemoteLineCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 7),
    _Cn1000MediaEndpointRemoteLineCardSlot_Type()
)
cn1000MediaEndpointRemoteLineCardSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointRemoteLineCardSlot.setStatus("current")


class _Cn1000MediaEndpointRemoteLineCardOffset_Type(Integer32):
    """Custom type cn1000MediaEndpointRemoteLineCardOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Cn1000MediaEndpointRemoteLineCardOffset_Type.__name__ = "Integer32"
_Cn1000MediaEndpointRemoteLineCardOffset_Object = MibTableColumn
cn1000MediaEndpointRemoteLineCardOffset = _Cn1000MediaEndpointRemoteLineCardOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 8),
    _Cn1000MediaEndpointRemoteLineCardOffset_Type()
)
cn1000MediaEndpointRemoteLineCardOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointRemoteLineCardOffset.setStatus("current")
_Cn1000MediaEndpointNetworkPathId_Type = Cn1000NetworkPathIdentifierRange
_Cn1000MediaEndpointNetworkPathId_Object = MibTableColumn
cn1000MediaEndpointNetworkPathId = _Cn1000MediaEndpointNetworkPathId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 9),
    _Cn1000MediaEndpointNetworkPathId_Type()
)
cn1000MediaEndpointNetworkPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointNetworkPathId.setStatus("current")
_Cn1000MediaEndpointConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000MediaEndpointConfigurationStatus_Object = MibTableColumn
cn1000MediaEndpointConfigurationStatus = _Cn1000MediaEndpointConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 11),
    _Cn1000MediaEndpointConfigurationStatus_Type()
)
cn1000MediaEndpointConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaEndpointConfigurationStatus.setStatus("current")
_Cn1000MediaEndpointRowStatus_Type = RowStatus
_Cn1000MediaEndpointRowStatus_Object = MibTableColumn
cn1000MediaEndpointRowStatus = _Cn1000MediaEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 13, 1, 12),
    _Cn1000MediaEndpointRowStatus_Type()
)
cn1000MediaEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaEndpointRowStatus.setStatus("current")
_Cn1000MediaConnectionTable_Object = MibTable
cn1000MediaConnectionTable = _Cn1000MediaConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14)
)
if mibBuilder.loadTexts:
    cn1000MediaConnectionTable.setStatus("current")
_Cn1000MediaConnectionEntry_Object = MibTableRow
cn1000MediaConnectionEntry = _Cn1000MediaConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1)
)
cn1000MediaConnectionEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionLineSideIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionSwitchSideIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionOffset"),
)
if mibBuilder.loadTexts:
    cn1000MediaConnectionEntry.setStatus("current")
_Cn1000MediaConnectionLineSideIfIndex_Type = InterfaceIndex
_Cn1000MediaConnectionLineSideIfIndex_Object = MibTableColumn
cn1000MediaConnectionLineSideIfIndex = _Cn1000MediaConnectionLineSideIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 1),
    _Cn1000MediaConnectionLineSideIfIndex_Type()
)
cn1000MediaConnectionLineSideIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionLineSideIfIndex.setStatus("current")
_Cn1000MediaConnectionSwitchSideIfIndex_Type = InterfaceIndex
_Cn1000MediaConnectionSwitchSideIfIndex_Object = MibTableColumn
cn1000MediaConnectionSwitchSideIfIndex = _Cn1000MediaConnectionSwitchSideIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 2),
    _Cn1000MediaConnectionSwitchSideIfIndex_Type()
)
cn1000MediaConnectionSwitchSideIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionSwitchSideIfIndex.setStatus("current")


class _Cn1000MediaConnectionOffset_Type(Integer32):
    """Custom type cn1000MediaConnectionOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cn1000MediaConnectionOffset_Type.__name__ = "Integer32"
_Cn1000MediaConnectionOffset_Object = MibTableColumn
cn1000MediaConnectionOffset = _Cn1000MediaConnectionOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 3),
    _Cn1000MediaConnectionOffset_Type()
)
cn1000MediaConnectionOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionOffset.setStatus("current")


class _Cn1000MediaConnectionInternalLineSideVpi_Type(Integer32):
    """Custom type cn1000MediaConnectionInternalLineSideVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000MediaConnectionInternalLineSideVpi_Type.__name__ = "Integer32"
_Cn1000MediaConnectionInternalLineSideVpi_Object = MibTableColumn
cn1000MediaConnectionInternalLineSideVpi = _Cn1000MediaConnectionInternalLineSideVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 4),
    _Cn1000MediaConnectionInternalLineSideVpi_Type()
)
cn1000MediaConnectionInternalLineSideVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionInternalLineSideVpi.setStatus("current")


class _Cn1000MediaConnectionInternalLineSideVci_Type(Integer32):
    """Custom type cn1000MediaConnectionInternalLineSideVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaConnectionInternalLineSideVci_Type.__name__ = "Integer32"
_Cn1000MediaConnectionInternalLineSideVci_Object = MibTableColumn
cn1000MediaConnectionInternalLineSideVci = _Cn1000MediaConnectionInternalLineSideVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 5),
    _Cn1000MediaConnectionInternalLineSideVci_Type()
)
cn1000MediaConnectionInternalLineSideVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionInternalLineSideVci.setStatus("current")


class _Cn1000MediaConnectionInternalLineSideOffset_Type(Integer32):
    """Custom type cn1000MediaConnectionInternalLineSideOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cn1000MediaConnectionInternalLineSideOffset_Type.__name__ = "Integer32"
_Cn1000MediaConnectionInternalLineSideOffset_Object = MibTableColumn
cn1000MediaConnectionInternalLineSideOffset = _Cn1000MediaConnectionInternalLineSideOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 6),
    _Cn1000MediaConnectionInternalLineSideOffset_Type()
)
cn1000MediaConnectionInternalLineSideOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionInternalLineSideOffset.setStatus("current")


class _Cn1000MediaConnectionInternalSwitchSideVpi_Type(Integer32):
    """Custom type cn1000MediaConnectionInternalSwitchSideVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000MediaConnectionInternalSwitchSideVpi_Type.__name__ = "Integer32"
_Cn1000MediaConnectionInternalSwitchSideVpi_Object = MibTableColumn
cn1000MediaConnectionInternalSwitchSideVpi = _Cn1000MediaConnectionInternalSwitchSideVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 7),
    _Cn1000MediaConnectionInternalSwitchSideVpi_Type()
)
cn1000MediaConnectionInternalSwitchSideVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionInternalSwitchSideVpi.setStatus("current")


class _Cn1000MediaConnectionInternalSwitchSideVci_Type(Integer32):
    """Custom type cn1000MediaConnectionInternalSwitchSideVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaConnectionInternalSwitchSideVci_Type.__name__ = "Integer32"
_Cn1000MediaConnectionInternalSwitchSideVci_Object = MibTableColumn
cn1000MediaConnectionInternalSwitchSideVci = _Cn1000MediaConnectionInternalSwitchSideVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 8),
    _Cn1000MediaConnectionInternalSwitchSideVci_Type()
)
cn1000MediaConnectionInternalSwitchSideVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionInternalSwitchSideVci.setStatus("current")


class _Cn1000MediaConnectionInternalSwitchSideOffset_Type(Integer32):
    """Custom type cn1000MediaConnectionInternalSwitchSideOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cn1000MediaConnectionInternalSwitchSideOffset_Type.__name__ = "Integer32"
_Cn1000MediaConnectionInternalSwitchSideOffset_Object = MibTableColumn
cn1000MediaConnectionInternalSwitchSideOffset = _Cn1000MediaConnectionInternalSwitchSideOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 9),
    _Cn1000MediaConnectionInternalSwitchSideOffset_Type()
)
cn1000MediaConnectionInternalSwitchSideOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionInternalSwitchSideOffset.setStatus("current")
_Cn1000MediaConnectionLineSideType_Type = Cn1000VoiceInfrastructureMediaEndpointType
_Cn1000MediaConnectionLineSideType_Object = MibTableColumn
cn1000MediaConnectionLineSideType = _Cn1000MediaConnectionLineSideType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 10),
    _Cn1000MediaConnectionLineSideType_Type()
)
cn1000MediaConnectionLineSideType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaConnectionLineSideType.setStatus("current")
_Cn1000MediaConnectionSwitchSideType_Type = Cn1000VoiceInfrastructureMediaEndpointType
_Cn1000MediaConnectionSwitchSideType_Object = MibTableColumn
cn1000MediaConnectionSwitchSideType = _Cn1000MediaConnectionSwitchSideType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 11),
    _Cn1000MediaConnectionSwitchSideType_Type()
)
cn1000MediaConnectionSwitchSideType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaConnectionSwitchSideType.setStatus("current")
_Cn1000MediaConnectionConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000MediaConnectionConfigurationStatus_Object = MibTableColumn
cn1000MediaConnectionConfigurationStatus = _Cn1000MediaConnectionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 13),
    _Cn1000MediaConnectionConfigurationStatus_Type()
)
cn1000MediaConnectionConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionConfigurationStatus.setStatus("current")
_Cn1000MediaConnectionRowStatus_Type = RowStatus
_Cn1000MediaConnectionRowStatus_Object = MibTableColumn
cn1000MediaConnectionRowStatus = _Cn1000MediaConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 17),
    _Cn1000MediaConnectionRowStatus_Type()
)
cn1000MediaConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaConnectionRowStatus.setStatus("current")


class _Cn1000MediaConnectionDSPvcTag_Type(OctetString):
    """Custom type cn1000MediaConnectionDSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000MediaConnectionDSPvcTag_Type.__name__ = "OctetString"
_Cn1000MediaConnectionDSPvcTag_Object = MibTableColumn
cn1000MediaConnectionDSPvcTag = _Cn1000MediaConnectionDSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 18),
    _Cn1000MediaConnectionDSPvcTag_Type()
)
cn1000MediaConnectionDSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionDSPvcTag.setStatus("current")


class _Cn1000MediaConnectionUSPvcTag_Type(OctetString):
    """Custom type cn1000MediaConnectionUSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000MediaConnectionUSPvcTag_Type.__name__ = "OctetString"
_Cn1000MediaConnectionUSPvcTag_Object = MibTableColumn
cn1000MediaConnectionUSPvcTag = _Cn1000MediaConnectionUSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 14, 1, 19),
    _Cn1000MediaConnectionUSPvcTag_Type()
)
cn1000MediaConnectionUSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaConnectionUSPvcTag.setStatus("current")
_Cn1000MediaWanConnectionTable_Object = MibTable
cn1000MediaWanConnectionTable = _Cn1000MediaWanConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15)
)
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionTable.setStatus("current")
_Cn1000MediaWanConnectionEntry_Object = MibTableRow
cn1000MediaWanConnectionEntry = _Cn1000MediaWanConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1)
)
cn1000MediaWanConnectionEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanVpi"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanVci"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionOffset"),
)
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionEntry.setStatus("current")
_Cn1000MediaConnectionWanIfIndex_Type = InterfaceIndex
_Cn1000MediaConnectionWanIfIndex_Object = MibTableColumn
cn1000MediaConnectionWanIfIndex = _Cn1000MediaConnectionWanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 1),
    _Cn1000MediaConnectionWanIfIndex_Type()
)
cn1000MediaConnectionWanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanIfIndex.setStatus("current")


class _Cn1000MediaConnectionWanVpi_Type(Integer32):
    """Custom type cn1000MediaConnectionWanVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000MediaConnectionWanVpi_Type.__name__ = "Integer32"
_Cn1000MediaConnectionWanVpi_Object = MibTableColumn
cn1000MediaConnectionWanVpi = _Cn1000MediaConnectionWanVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 2),
    _Cn1000MediaConnectionWanVpi_Type()
)
cn1000MediaConnectionWanVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanVpi.setStatus("current")


class _Cn1000MediaConnectionWanVci_Type(Integer32):
    """Custom type cn1000MediaConnectionWanVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaConnectionWanVci_Type.__name__ = "Integer32"
_Cn1000MediaConnectionWanVci_Object = MibTableColumn
cn1000MediaConnectionWanVci = _Cn1000MediaConnectionWanVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 3),
    _Cn1000MediaConnectionWanVci_Type()
)
cn1000MediaConnectionWanVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanVci.setStatus("current")
_Cn1000MediaWanConnectionIfIndex_Type = InterfaceIndex
_Cn1000MediaWanConnectionIfIndex_Object = MibTableColumn
cn1000MediaWanConnectionIfIndex = _Cn1000MediaWanConnectionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 4),
    _Cn1000MediaWanConnectionIfIndex_Type()
)
cn1000MediaWanConnectionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIfIndex.setStatus("current")


class _Cn1000MediaWanConnectionOffset_Type(Integer32):
    """Custom type cn1000MediaWanConnectionOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cn1000MediaWanConnectionOffset_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionOffset_Object = MibTableColumn
cn1000MediaWanConnectionOffset = _Cn1000MediaWanConnectionOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 5),
    _Cn1000MediaWanConnectionOffset_Type()
)
cn1000MediaWanConnectionOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionOffset.setStatus("current")


class _Cn1000MediaWanConnectionInternalVpi_Type(Integer32):
    """Custom type cn1000MediaWanConnectionInternalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000MediaWanConnectionInternalVpi_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionInternalVpi_Object = MibTableColumn
cn1000MediaWanConnectionInternalVpi = _Cn1000MediaWanConnectionInternalVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 6),
    _Cn1000MediaWanConnectionInternalVpi_Type()
)
cn1000MediaWanConnectionInternalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionInternalVpi.setStatus("current")


class _Cn1000MediaWanConnectionInternalVci_Type(Integer32):
    """Custom type cn1000MediaWanConnectionInternalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaWanConnectionInternalVci_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionInternalVci_Object = MibTableColumn
cn1000MediaWanConnectionInternalVci = _Cn1000MediaWanConnectionInternalVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 7),
    _Cn1000MediaWanConnectionInternalVci_Type()
)
cn1000MediaWanConnectionInternalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionInternalVci.setStatus("current")


class _Cn1000MediaWanConnectionInternalOffset_Type(Integer32):
    """Custom type cn1000MediaWanConnectionInternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cn1000MediaWanConnectionInternalOffset_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionInternalOffset_Object = MibTableColumn
cn1000MediaWanConnectionInternalOffset = _Cn1000MediaWanConnectionInternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 8),
    _Cn1000MediaWanConnectionInternalOffset_Type()
)
cn1000MediaWanConnectionInternalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionInternalOffset.setStatus("current")
_Cn1000MediaWanConnectionEndpointType_Type = Cn1000VoiceInfrastructureMediaEndpointType
_Cn1000MediaWanConnectionEndpointType_Object = MibTableColumn
cn1000MediaWanConnectionEndpointType = _Cn1000MediaWanConnectionEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 9),
    _Cn1000MediaWanConnectionEndpointType_Type()
)
cn1000MediaWanConnectionEndpointType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionEndpointType.setStatus("current")


class _Cn1000MediaWanConnectionCdvt_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCdvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Cn1000MediaWanConnectionCdvt_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCdvt_Object = MibTableColumn
cn1000MediaWanConnectionCdvt = _Cn1000MediaWanConnectionCdvt_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 10),
    _Cn1000MediaWanConnectionCdvt_Type()
)
cn1000MediaWanConnectionCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCdvt.setStatus("current")
_Cn1000MediaWanConnectionConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000MediaWanConnectionConfigurationStatus_Object = MibTableColumn
cn1000MediaWanConnectionConfigurationStatus = _Cn1000MediaWanConnectionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 11),
    _Cn1000MediaWanConnectionConfigurationStatus_Type()
)
cn1000MediaWanConnectionConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionConfigurationStatus.setStatus("current")
_Cn1000MediaWanConnectionRowStatus_Type = RowStatus
_Cn1000MediaWanConnectionRowStatus_Object = MibTableColumn
cn1000MediaWanConnectionRowStatus = _Cn1000MediaWanConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 12),
    _Cn1000MediaWanConnectionRowStatus_Type()
)
cn1000MediaWanConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionRowStatus.setStatus("current")


class _Cn1000MediaWanConnectionDSPvcTag_Type(OctetString):
    """Custom type cn1000MediaWanConnectionDSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000MediaWanConnectionDSPvcTag_Type.__name__ = "OctetString"
_Cn1000MediaWanConnectionDSPvcTag_Object = MibTableColumn
cn1000MediaWanConnectionDSPvcTag = _Cn1000MediaWanConnectionDSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 13),
    _Cn1000MediaWanConnectionDSPvcTag_Type()
)
cn1000MediaWanConnectionDSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionDSPvcTag.setStatus("current")


class _Cn1000MediaWanConnectionUSPvcTag_Type(OctetString):
    """Custom type cn1000MediaWanConnectionUSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000MediaWanConnectionUSPvcTag_Type.__name__ = "OctetString"
_Cn1000MediaWanConnectionUSPvcTag_Object = MibTableColumn
cn1000MediaWanConnectionUSPvcTag = _Cn1000MediaWanConnectionUSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 15, 1, 14),
    _Cn1000MediaWanConnectionUSPvcTag_Type()
)
cn1000MediaWanConnectionUSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionUSPvcTag.setStatus("current")
_Cn1000SubtendingConnectionTable_Object = MibTable
cn1000SubtendingConnectionTable = _Cn1000SubtendingConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16)
)
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionTable.setStatus("current")
_Cn1000SubtendingConnectionEntry_Object = MibTableRow
cn1000SubtendingConnectionEntry = _Cn1000SubtendingConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1)
)
cn1000SubtendingConnectionEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionIfIndex1"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionVpi1"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionVci1"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionIfIndex2"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionVpi2"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionVci2"),
)
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionEntry.setStatus("current")
_Cn1000SubtendingConnectionIfIndex1_Type = InterfaceIndex
_Cn1000SubtendingConnectionIfIndex1_Object = MibTableColumn
cn1000SubtendingConnectionIfIndex1 = _Cn1000SubtendingConnectionIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 1),
    _Cn1000SubtendingConnectionIfIndex1_Type()
)
cn1000SubtendingConnectionIfIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionIfIndex1.setStatus("current")


class _Cn1000SubtendingConnectionVpi1_Type(Integer32):
    """Custom type cn1000SubtendingConnectionVpi1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000SubtendingConnectionVpi1_Type.__name__ = "Integer32"
_Cn1000SubtendingConnectionVpi1_Object = MibTableColumn
cn1000SubtendingConnectionVpi1 = _Cn1000SubtendingConnectionVpi1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 2),
    _Cn1000SubtendingConnectionVpi1_Type()
)
cn1000SubtendingConnectionVpi1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionVpi1.setStatus("current")


class _Cn1000SubtendingConnectionVci1_Type(Integer32):
    """Custom type cn1000SubtendingConnectionVci1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SubtendingConnectionVci1_Type.__name__ = "Integer32"
_Cn1000SubtendingConnectionVci1_Object = MibTableColumn
cn1000SubtendingConnectionVci1 = _Cn1000SubtendingConnectionVci1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 3),
    _Cn1000SubtendingConnectionVci1_Type()
)
cn1000SubtendingConnectionVci1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionVci1.setStatus("current")
_Cn1000SubtendingConnectionIfIndex2_Type = InterfaceIndex
_Cn1000SubtendingConnectionIfIndex2_Object = MibTableColumn
cn1000SubtendingConnectionIfIndex2 = _Cn1000SubtendingConnectionIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 4),
    _Cn1000SubtendingConnectionIfIndex2_Type()
)
cn1000SubtendingConnectionIfIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionIfIndex2.setStatus("current")


class _Cn1000SubtendingConnectionVpi2_Type(Integer32):
    """Custom type cn1000SubtendingConnectionVpi2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000SubtendingConnectionVpi2_Type.__name__ = "Integer32"
_Cn1000SubtendingConnectionVpi2_Object = MibTableColumn
cn1000SubtendingConnectionVpi2 = _Cn1000SubtendingConnectionVpi2_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 5),
    _Cn1000SubtendingConnectionVpi2_Type()
)
cn1000SubtendingConnectionVpi2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionVpi2.setStatus("current")


class _Cn1000SubtendingConnectionVci2_Type(Integer32):
    """Custom type cn1000SubtendingConnectionVci2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000SubtendingConnectionVci2_Type.__name__ = "Integer32"
_Cn1000SubtendingConnectionVci2_Object = MibTableColumn
cn1000SubtendingConnectionVci2 = _Cn1000SubtendingConnectionVci2_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 6),
    _Cn1000SubtendingConnectionVci2_Type()
)
cn1000SubtendingConnectionVci2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionVci2.setStatus("current")
_Cn1000SubtendingConnectionType_Type = Cn1000VoiceSubtendingConnectionType
_Cn1000SubtendingConnectionType_Object = MibTableColumn
cn1000SubtendingConnectionType = _Cn1000SubtendingConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 7),
    _Cn1000SubtendingConnectionType_Type()
)
cn1000SubtendingConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionType.setStatus("current")
_Cn1000SubtendingConnectionConfigurationStatus_Type = Cn1000ConfigurationStatus
_Cn1000SubtendingConnectionConfigurationStatus_Object = MibTableColumn
cn1000SubtendingConnectionConfigurationStatus = _Cn1000SubtendingConnectionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 8),
    _Cn1000SubtendingConnectionConfigurationStatus_Type()
)
cn1000SubtendingConnectionConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionConfigurationStatus.setStatus("current")
_Cn1000SubtendingConnectionRowStatus_Type = RowStatus
_Cn1000SubtendingConnectionRowStatus_Object = MibTableColumn
cn1000SubtendingConnectionRowStatus = _Cn1000SubtendingConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 9),
    _Cn1000SubtendingConnectionRowStatus_Type()
)
cn1000SubtendingConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionRowStatus.setStatus("current")


class _Cn1000SubtendingConnectionDSPvcTag_Type(OctetString):
    """Custom type cn1000SubtendingConnectionDSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000SubtendingConnectionDSPvcTag_Type.__name__ = "OctetString"
_Cn1000SubtendingConnectionDSPvcTag_Object = MibTableColumn
cn1000SubtendingConnectionDSPvcTag = _Cn1000SubtendingConnectionDSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 22),
    _Cn1000SubtendingConnectionDSPvcTag_Type()
)
cn1000SubtendingConnectionDSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionDSPvcTag.setStatus("current")


class _Cn1000SubtendingConnectionUSPvcTag_Type(OctetString):
    """Custom type cn1000SubtendingConnectionUSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cn1000SubtendingConnectionUSPvcTag_Type.__name__ = "OctetString"
_Cn1000SubtendingConnectionUSPvcTag_Object = MibTableColumn
cn1000SubtendingConnectionUSPvcTag = _Cn1000SubtendingConnectionUSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 16, 1, 23),
    _Cn1000SubtendingConnectionUSPvcTag_Type()
)
cn1000SubtendingConnectionUSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000SubtendingConnectionUSPvcTag.setStatus("current")
_Cn1000MediaCurrentStatsTable_Object = MibTable
cn1000MediaCurrentStatsTable = _Cn1000MediaCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17)
)
if mibBuilder.loadTexts:
    cn1000MediaCurrentStatsTable.setStatus("current")
_Cn1000MediaCurrentStatsEntry_Object = MibTableRow
cn1000MediaCurrentStatsEntry = _Cn1000MediaCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1)
)
cn1000MediaCurrentStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsDs1Shelf"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsDs1SlotGroup"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsRemoteSysAddr"),
)
if mibBuilder.loadTexts:
    cn1000MediaCurrentStatsEntry.setStatus("current")
_Cn1000MediaCurrStatsDs1Shelf_Type = Cn1000ShelfRange
_Cn1000MediaCurrStatsDs1Shelf_Object = MibTableColumn
cn1000MediaCurrStatsDs1Shelf = _Cn1000MediaCurrStatsDs1Shelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 1),
    _Cn1000MediaCurrStatsDs1Shelf_Type()
)
cn1000MediaCurrStatsDs1Shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsDs1Shelf.setStatus("current")
_Cn1000MediaCurrStatsDs1SlotGroup_Type = CnSlotGroupNameType
_Cn1000MediaCurrStatsDs1SlotGroup_Object = MibTableColumn
cn1000MediaCurrStatsDs1SlotGroup = _Cn1000MediaCurrStatsDs1SlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 2),
    _Cn1000MediaCurrStatsDs1SlotGroup_Type()
)
cn1000MediaCurrStatsDs1SlotGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsDs1SlotGroup.setStatus("current")
_Cn1000MediaCurrStatsRemoteSysAddr_Type = IpAddress
_Cn1000MediaCurrStatsRemoteSysAddr_Object = MibTableColumn
cn1000MediaCurrStatsRemoteSysAddr = _Cn1000MediaCurrStatsRemoteSysAddr_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 3),
    _Cn1000MediaCurrStatsRemoteSysAddr_Type()
)
cn1000MediaCurrStatsRemoteSysAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsRemoteSysAddr.setStatus("current")


class _Cn1000MediaCurrStatsPegCount_Type(Integer32):
    """Custom type cn1000MediaCurrStatsPegCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaCurrStatsPegCount_Type.__name__ = "Integer32"
_Cn1000MediaCurrStatsPegCount_Object = MibTableColumn
cn1000MediaCurrStatsPegCount = _Cn1000MediaCurrStatsPegCount_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 4),
    _Cn1000MediaCurrStatsPegCount_Type()
)
cn1000MediaCurrStatsPegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsPegCount.setStatus("current")


class _Cn1000MediaCurrStatsBlockage_Type(Integer32):
    """Custom type cn1000MediaCurrStatsBlockage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaCurrStatsBlockage_Type.__name__ = "Integer32"
_Cn1000MediaCurrStatsBlockage_Object = MibTableColumn
cn1000MediaCurrStatsBlockage = _Cn1000MediaCurrStatsBlockage_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 5),
    _Cn1000MediaCurrStatsBlockage_Type()
)
cn1000MediaCurrStatsBlockage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsBlockage.setStatus("current")


class _Cn1000MediaCurrStatsHoldTime_Type(Integer32):
    """Custom type cn1000MediaCurrStatsHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaCurrStatsHoldTime_Type.__name__ = "Integer32"
_Cn1000MediaCurrStatsHoldTime_Object = MibTableColumn
cn1000MediaCurrStatsHoldTime = _Cn1000MediaCurrStatsHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 6),
    _Cn1000MediaCurrStatsHoldTime_Type()
)
cn1000MediaCurrStatsHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsHoldTime.setStatus("current")


class _Cn1000MediaCurrStatsAvailableTimeslots_Type(Integer32):
    """Custom type cn1000MediaCurrStatsAvailableTimeslots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaCurrStatsAvailableTimeslots_Type.__name__ = "Integer32"
_Cn1000MediaCurrStatsAvailableTimeslots_Object = MibTableColumn
cn1000MediaCurrStatsAvailableTimeslots = _Cn1000MediaCurrStatsAvailableTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 7),
    _Cn1000MediaCurrStatsAvailableTimeslots_Type()
)
cn1000MediaCurrStatsAvailableTimeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsAvailableTimeslots.setStatus("current")


class _Cn1000MediaCurrStatsTimeslotsInUse_Type(Integer32):
    """Custom type cn1000MediaCurrStatsTimeslotsInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaCurrStatsTimeslotsInUse_Type.__name__ = "Integer32"
_Cn1000MediaCurrStatsTimeslotsInUse_Object = MibTableColumn
cn1000MediaCurrStatsTimeslotsInUse = _Cn1000MediaCurrStatsTimeslotsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 8),
    _Cn1000MediaCurrStatsTimeslotsInUse_Type()
)
cn1000MediaCurrStatsTimeslotsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsTimeslotsInUse.setStatus("current")


class _Cn1000MediaCurrStatsTimeslotsHighWater_Type(Integer32):
    """Custom type cn1000MediaCurrStatsTimeslotsHighWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaCurrStatsTimeslotsHighWater_Type.__name__ = "Integer32"
_Cn1000MediaCurrStatsTimeslotsHighWater_Object = MibTableColumn
cn1000MediaCurrStatsTimeslotsHighWater = _Cn1000MediaCurrStatsTimeslotsHighWater_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 17, 1, 9),
    _Cn1000MediaCurrStatsTimeslotsHighWater_Type()
)
cn1000MediaCurrStatsTimeslotsHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaCurrStatsTimeslotsHighWater.setStatus("current")
_Cn1000MediaIntervalStatsTable_Object = MibTable
cn1000MediaIntervalStatsTable = _Cn1000MediaIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18)
)
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsTable.setStatus("current")
_Cn1000MediaIntervalStatsEntry_Object = MibTableRow
cn1000MediaIntervalStatsEntry = _Cn1000MediaIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1)
)
cn1000MediaIntervalStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsDs1Shelf"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsDs1SlotGroup"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsRemoteSysAddr"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsInterval"),
)
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsEntry.setStatus("current")
_Cn1000MediaIntervalStatsDs1Shelf_Type = Cn1000ShelfRange
_Cn1000MediaIntervalStatsDs1Shelf_Object = MibTableColumn
cn1000MediaIntervalStatsDs1Shelf = _Cn1000MediaIntervalStatsDs1Shelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 1),
    _Cn1000MediaIntervalStatsDs1Shelf_Type()
)
cn1000MediaIntervalStatsDs1Shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsDs1Shelf.setStatus("current")
_Cn1000MediaIntervalStatsDs1SlotGroup_Type = CnSlotGroupNameType
_Cn1000MediaIntervalStatsDs1SlotGroup_Object = MibTableColumn
cn1000MediaIntervalStatsDs1SlotGroup = _Cn1000MediaIntervalStatsDs1SlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 2),
    _Cn1000MediaIntervalStatsDs1SlotGroup_Type()
)
cn1000MediaIntervalStatsDs1SlotGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsDs1SlotGroup.setStatus("current")
_Cn1000MediaIntervalStatsRemoteSysAddr_Type = IpAddress
_Cn1000MediaIntervalStatsRemoteSysAddr_Object = MibTableColumn
cn1000MediaIntervalStatsRemoteSysAddr = _Cn1000MediaIntervalStatsRemoteSysAddr_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 3),
    _Cn1000MediaIntervalStatsRemoteSysAddr_Type()
)
cn1000MediaIntervalStatsRemoteSysAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsRemoteSysAddr.setStatus("current")


class _Cn1000MediaIntervalStatsInterval_Type(Integer32):
    """Custom type cn1000MediaIntervalStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cn1000MediaIntervalStatsInterval_Type.__name__ = "Integer32"
_Cn1000MediaIntervalStatsInterval_Object = MibTableColumn
cn1000MediaIntervalStatsInterval = _Cn1000MediaIntervalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 4),
    _Cn1000MediaIntervalStatsInterval_Type()
)
cn1000MediaIntervalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsInterval.setStatus("current")


class _Cn1000MediaIntervalStatsPegCount_Type(Integer32):
    """Custom type cn1000MediaIntervalStatsPegCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaIntervalStatsPegCount_Type.__name__ = "Integer32"
_Cn1000MediaIntervalStatsPegCount_Object = MibTableColumn
cn1000MediaIntervalStatsPegCount = _Cn1000MediaIntervalStatsPegCount_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 5),
    _Cn1000MediaIntervalStatsPegCount_Type()
)
cn1000MediaIntervalStatsPegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsPegCount.setStatus("current")


class _Cn1000MediaIntervalStatsBlockage_Type(Integer32):
    """Custom type cn1000MediaIntervalStatsBlockage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaIntervalStatsBlockage_Type.__name__ = "Integer32"
_Cn1000MediaIntervalStatsBlockage_Object = MibTableColumn
cn1000MediaIntervalStatsBlockage = _Cn1000MediaIntervalStatsBlockage_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 6),
    _Cn1000MediaIntervalStatsBlockage_Type()
)
cn1000MediaIntervalStatsBlockage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsBlockage.setStatus("current")


class _Cn1000MediaIntervalStatsHoldTime_Type(Integer32):
    """Custom type cn1000MediaIntervalStatsHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaIntervalStatsHoldTime_Type.__name__ = "Integer32"
_Cn1000MediaIntervalStatsHoldTime_Object = MibTableColumn
cn1000MediaIntervalStatsHoldTime = _Cn1000MediaIntervalStatsHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 7),
    _Cn1000MediaIntervalStatsHoldTime_Type()
)
cn1000MediaIntervalStatsHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsHoldTime.setStatus("current")


class _Cn1000MediaIntervalStatsAvailableTimeslots_Type(Integer32):
    """Custom type cn1000MediaIntervalStatsAvailableTimeslots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaIntervalStatsAvailableTimeslots_Type.__name__ = "Integer32"
_Cn1000MediaIntervalStatsAvailableTimeslots_Object = MibTableColumn
cn1000MediaIntervalStatsAvailableTimeslots = _Cn1000MediaIntervalStatsAvailableTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 8),
    _Cn1000MediaIntervalStatsAvailableTimeslots_Type()
)
cn1000MediaIntervalStatsAvailableTimeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsAvailableTimeslots.setStatus("current")


class _Cn1000MediaIntervalStatsTimeslotsHighWater_Type(Integer32):
    """Custom type cn1000MediaIntervalStatsTimeslotsHighWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaIntervalStatsTimeslotsHighWater_Type.__name__ = "Integer32"
_Cn1000MediaIntervalStatsTimeslotsHighWater_Object = MibTableColumn
cn1000MediaIntervalStatsTimeslotsHighWater = _Cn1000MediaIntervalStatsTimeslotsHighWater_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 18, 1, 9),
    _Cn1000MediaIntervalStatsTimeslotsHighWater_Type()
)
cn1000MediaIntervalStatsTimeslotsHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaIntervalStatsTimeslotsHighWater.setStatus("current")
_Cn1000MediaWanConnectionIntervalStatsTable_Object = MibTable
cn1000MediaWanConnectionIntervalStatsTable = _Cn1000MediaWanConnectionIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19)
)
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsTable.setStatus("current")
_Cn1000MediaWanConnectionIntervalStatsEntry_Object = MibTableRow
cn1000MediaWanConnectionIntervalStatsEntry = _Cn1000MediaWanConnectionIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1)
)
cn1000MediaWanConnectionIntervalStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanIntervalStatsIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanIntervalStatsVpi"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanIntervalStatsVci"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsOffset"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsInterval"),
)
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsEntry.setStatus("current")
_Cn1000MediaConnectionWanIntervalStatsIfIndex_Type = InterfaceIndex
_Cn1000MediaConnectionWanIntervalStatsIfIndex_Object = MibTableColumn
cn1000MediaConnectionWanIntervalStatsIfIndex = _Cn1000MediaConnectionWanIntervalStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 1),
    _Cn1000MediaConnectionWanIntervalStatsIfIndex_Type()
)
cn1000MediaConnectionWanIntervalStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanIntervalStatsIfIndex.setStatus("current")


class _Cn1000MediaConnectionWanIntervalStatsVpi_Type(Integer32):
    """Custom type cn1000MediaConnectionWanIntervalStatsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000MediaConnectionWanIntervalStatsVpi_Type.__name__ = "Integer32"
_Cn1000MediaConnectionWanIntervalStatsVpi_Object = MibTableColumn
cn1000MediaConnectionWanIntervalStatsVpi = _Cn1000MediaConnectionWanIntervalStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 2),
    _Cn1000MediaConnectionWanIntervalStatsVpi_Type()
)
cn1000MediaConnectionWanIntervalStatsVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanIntervalStatsVpi.setStatus("current")


class _Cn1000MediaConnectionWanIntervalStatsVci_Type(Integer32):
    """Custom type cn1000MediaConnectionWanIntervalStatsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaConnectionWanIntervalStatsVci_Type.__name__ = "Integer32"
_Cn1000MediaConnectionWanIntervalStatsVci_Object = MibTableColumn
cn1000MediaConnectionWanIntervalStatsVci = _Cn1000MediaConnectionWanIntervalStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 3),
    _Cn1000MediaConnectionWanIntervalStatsVci_Type()
)
cn1000MediaConnectionWanIntervalStatsVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanIntervalStatsVci.setStatus("current")
_Cn1000MediaWanConnectionIntervalStatsIfIndex_Type = InterfaceIndex
_Cn1000MediaWanConnectionIntervalStatsIfIndex_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsIfIndex = _Cn1000MediaWanConnectionIntervalStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 4),
    _Cn1000MediaWanConnectionIntervalStatsIfIndex_Type()
)
cn1000MediaWanConnectionIntervalStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsIfIndex.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsOffset_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaWanConnectionIntervalStatsOffset_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsOffset_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsOffset = _Cn1000MediaWanConnectionIntervalStatsOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 5),
    _Cn1000MediaWanConnectionIntervalStatsOffset_Type()
)
cn1000MediaWanConnectionIntervalStatsOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsOffset.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsInterval_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cn1000MediaWanConnectionIntervalStatsInterval_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsInterval_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsInterval = _Cn1000MediaWanConnectionIntervalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 6),
    _Cn1000MediaWanConnectionIntervalStatsInterval_Type()
)
cn1000MediaWanConnectionIntervalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsInterval.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsUnderFlows_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsUnderFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsUnderFlows_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsUnderFlows_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsUnderFlows = _Cn1000MediaWanConnectionIntervalStatsUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 7),
    _Cn1000MediaWanConnectionIntervalStatsUnderFlows_Type()
)
cn1000MediaWanConnectionIntervalStatsUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsUnderFlows.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsOverFlows_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsOverFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsOverFlows_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsOverFlows_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsOverFlows = _Cn1000MediaWanConnectionIntervalStatsOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 8),
    _Cn1000MediaWanConnectionIntervalStatsOverFlows_Type()
)
cn1000MediaWanConnectionIntervalStatsOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsOverFlows.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsCellDrop_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsCellDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsCellDrop_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsCellDrop_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsCellDrop = _Cn1000MediaWanConnectionIntervalStatsCellDrop_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 9),
    _Cn1000MediaWanConnectionIntervalStatsCellDrop_Type()
)
cn1000MediaWanConnectionIntervalStatsCellDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsCellDrop.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsMisInsertedCell_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsMisInsertedCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsMisInsertedCell_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsMisInsertedCell_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsMisInsertedCell = _Cn1000MediaWanConnectionIntervalStatsMisInsertedCell_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 10),
    _Cn1000MediaWanConnectionIntervalStatsMisInsertedCell_Type()
)
cn1000MediaWanConnectionIntervalStatsMisInsertedCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsMisInsertedCell.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsSequenceErrors_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsSequenceErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsSequenceErrors_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsSequenceErrors_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsSequenceErrors = _Cn1000MediaWanConnectionIntervalStatsSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 11),
    _Cn1000MediaWanConnectionIntervalStatsSequenceErrors_Type()
)
cn1000MediaWanConnectionIntervalStatsSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsSequenceErrors.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsPointerReframes_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsPointerReframes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsPointerReframes_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsPointerReframes_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsPointerReframes = _Cn1000MediaWanConnectionIntervalStatsPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 12),
    _Cn1000MediaWanConnectionIntervalStatsPointerReframes_Type()
)
cn1000MediaWanConnectionIntervalStatsPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsPointerReframes.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsHeaderErrors_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsHeaderErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsHeaderErrors_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsHeaderErrors_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsHeaderErrors = _Cn1000MediaWanConnectionIntervalStatsHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 13),
    _Cn1000MediaWanConnectionIntervalStatsHeaderErrors_Type()
)
cn1000MediaWanConnectionIntervalStatsHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsHeaderErrors.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsPointerParityErrors_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsPointerParityErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsPointerParityErrors_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsPointerParityErrors_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsPointerParityErrors = _Cn1000MediaWanConnectionIntervalStatsPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 14),
    _Cn1000MediaWanConnectionIntervalStatsPointerParityErrors_Type()
)
cn1000MediaWanConnectionIntervalStatsPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsPointerParityErrors.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsRxCells_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsRxCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsRxCells_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsRxCells_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsRxCells = _Cn1000MediaWanConnectionIntervalStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 15),
    _Cn1000MediaWanConnectionIntervalStatsRxCells_Type()
)
cn1000MediaWanConnectionIntervalStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsRxCells.setStatus("current")


class _Cn1000MediaWanConnectionIntervalStatsTxCells_Type(Integer32):
    """Custom type cn1000MediaWanConnectionIntervalStatsTxCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionIntervalStatsTxCells_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionIntervalStatsTxCells_Object = MibTableColumn
cn1000MediaWanConnectionIntervalStatsTxCells = _Cn1000MediaWanConnectionIntervalStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 19, 1, 16),
    _Cn1000MediaWanConnectionIntervalStatsTxCells_Type()
)
cn1000MediaWanConnectionIntervalStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionIntervalStatsTxCells.setStatus("current")
_Cn1000MediaWanConnectionCurrentStatsTable_Object = MibTable
cn1000MediaWanConnectionCurrentStatsTable = _Cn1000MediaWanConnectionCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20)
)
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsTable.setStatus("current")
_Cn1000MediaWanConnectionCurrentStatsEntry_Object = MibTableRow
cn1000MediaWanConnectionCurrentStatsEntry = _Cn1000MediaWanConnectionCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1)
)
cn1000MediaWanConnectionCurrentStatsEntry.setIndexNames(
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanCurrentStatsIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanCurrentStatsVpi"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionWanCurrentStatsVci"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsIfIndex"),
    (0, "CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsOffset"),
)
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsEntry.setStatus("current")
_Cn1000MediaConnectionWanCurrentStatsIfIndex_Type = InterfaceIndex
_Cn1000MediaConnectionWanCurrentStatsIfIndex_Object = MibTableColumn
cn1000MediaConnectionWanCurrentStatsIfIndex = _Cn1000MediaConnectionWanCurrentStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 1),
    _Cn1000MediaConnectionWanCurrentStatsIfIndex_Type()
)
cn1000MediaConnectionWanCurrentStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanCurrentStatsIfIndex.setStatus("current")


class _Cn1000MediaConnectionWanCurrentStatsVpi_Type(Integer32):
    """Custom type cn1000MediaConnectionWanCurrentStatsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cn1000MediaConnectionWanCurrentStatsVpi_Type.__name__ = "Integer32"
_Cn1000MediaConnectionWanCurrentStatsVpi_Object = MibTableColumn
cn1000MediaConnectionWanCurrentStatsVpi = _Cn1000MediaConnectionWanCurrentStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 2),
    _Cn1000MediaConnectionWanCurrentStatsVpi_Type()
)
cn1000MediaConnectionWanCurrentStatsVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanCurrentStatsVpi.setStatus("current")


class _Cn1000MediaConnectionWanCurrentStatsVci_Type(Integer32):
    """Custom type cn1000MediaConnectionWanCurrentStatsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaConnectionWanCurrentStatsVci_Type.__name__ = "Integer32"
_Cn1000MediaConnectionWanCurrentStatsVci_Object = MibTableColumn
cn1000MediaConnectionWanCurrentStatsVci = _Cn1000MediaConnectionWanCurrentStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 3),
    _Cn1000MediaConnectionWanCurrentStatsVci_Type()
)
cn1000MediaConnectionWanCurrentStatsVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaConnectionWanCurrentStatsVci.setStatus("current")
_Cn1000MediaWanConnectionCurrentStatsIfIndex_Type = InterfaceIndex
_Cn1000MediaWanConnectionCurrentStatsIfIndex_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsIfIndex = _Cn1000MediaWanConnectionCurrentStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 4),
    _Cn1000MediaWanConnectionCurrentStatsIfIndex_Type()
)
cn1000MediaWanConnectionCurrentStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsIfIndex.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsOffset_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cn1000MediaWanConnectionCurrentStatsOffset_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsOffset_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsOffset = _Cn1000MediaWanConnectionCurrentStatsOffset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 5),
    _Cn1000MediaWanConnectionCurrentStatsOffset_Type()
)
cn1000MediaWanConnectionCurrentStatsOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsOffset.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsUnderFlows_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsUnderFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsUnderFlows_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsUnderFlows_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsUnderFlows = _Cn1000MediaWanConnectionCurrentStatsUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 6),
    _Cn1000MediaWanConnectionCurrentStatsUnderFlows_Type()
)
cn1000MediaWanConnectionCurrentStatsUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsUnderFlows.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsOverFlows_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsOverFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsOverFlows_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsOverFlows_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsOverFlows = _Cn1000MediaWanConnectionCurrentStatsOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 7),
    _Cn1000MediaWanConnectionCurrentStatsOverFlows_Type()
)
cn1000MediaWanConnectionCurrentStatsOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsOverFlows.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsCellDrop_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsCellDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsCellDrop_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsCellDrop_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsCellDrop = _Cn1000MediaWanConnectionCurrentStatsCellDrop_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 8),
    _Cn1000MediaWanConnectionCurrentStatsCellDrop_Type()
)
cn1000MediaWanConnectionCurrentStatsCellDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsCellDrop.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsMisInsertedCell_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsMisInsertedCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsMisInsertedCell_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsMisInsertedCell_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsMisInsertedCell = _Cn1000MediaWanConnectionCurrentStatsMisInsertedCell_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 9),
    _Cn1000MediaWanConnectionCurrentStatsMisInsertedCell_Type()
)
cn1000MediaWanConnectionCurrentStatsMisInsertedCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsMisInsertedCell.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsSequenceErrors_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsSequenceErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsSequenceErrors_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsSequenceErrors_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsSequenceErrors = _Cn1000MediaWanConnectionCurrentStatsSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 10),
    _Cn1000MediaWanConnectionCurrentStatsSequenceErrors_Type()
)
cn1000MediaWanConnectionCurrentStatsSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsSequenceErrors.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsPointerReframes_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsPointerReframes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsPointerReframes_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsPointerReframes_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsPointerReframes = _Cn1000MediaWanConnectionCurrentStatsPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 11),
    _Cn1000MediaWanConnectionCurrentStatsPointerReframes_Type()
)
cn1000MediaWanConnectionCurrentStatsPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsPointerReframes.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsHeaderErrors_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsHeaderErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsHeaderErrors_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsHeaderErrors_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsHeaderErrors = _Cn1000MediaWanConnectionCurrentStatsHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 12),
    _Cn1000MediaWanConnectionCurrentStatsHeaderErrors_Type()
)
cn1000MediaWanConnectionCurrentStatsHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsHeaderErrors.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsPointerParityErrors_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsPointerParityErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsPointerParityErrors_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsPointerParityErrors_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsPointerParityErrors = _Cn1000MediaWanConnectionCurrentStatsPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 13),
    _Cn1000MediaWanConnectionCurrentStatsPointerParityErrors_Type()
)
cn1000MediaWanConnectionCurrentStatsPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsPointerParityErrors.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsRxCells_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsRxCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsRxCells_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsRxCells_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsRxCells = _Cn1000MediaWanConnectionCurrentStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 14),
    _Cn1000MediaWanConnectionCurrentStatsRxCells_Type()
)
cn1000MediaWanConnectionCurrentStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsRxCells.setStatus("current")


class _Cn1000MediaWanConnectionCurrentStatsTxCells_Type(Integer32):
    """Custom type cn1000MediaWanConnectionCurrentStatsTxCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cn1000MediaWanConnectionCurrentStatsTxCells_Type.__name__ = "Integer32"
_Cn1000MediaWanConnectionCurrentStatsTxCells_Object = MibTableColumn
cn1000MediaWanConnectionCurrentStatsTxCells = _Cn1000MediaWanConnectionCurrentStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 20, 1, 15),
    _Cn1000MediaWanConnectionCurrentStatsTxCells_Type()
)
cn1000MediaWanConnectionCurrentStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000MediaWanConnectionCurrentStatsTxCells.setStatus("current")
_Cn1000VoiceInfrastructureConformance_ObjectIdentity = ObjectIdentity
cn1000VoiceInfrastructureConformance = _Cn1000VoiceInfrastructureConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 21)
)

# Managed Objects groups

cn1000VoiceInfrastructureObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 3, 1, 21, 1)
)
cn1000VoiceInfrastructureObjectGroup.setObjects(
      *(("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingSystemAddress"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingSubnet"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingEntityType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConfigEntryRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingEndpointType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingRemoteSystemAddress"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingEndpointConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingEndpointRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionLineSideType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionSwitchSideType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionInternalSwitchSideVpi"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionInternalSwitchSideVci"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SignalingConnectionRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointRemoteEndpointType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointRemoteSystemAddress"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointRemoteLineCardShelf"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointRemoteLineCardSlot"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointRemoteLineCardOffset"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointNetworkPathId"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaEndpointRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionInternalLineSideVpi"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionInternalLineSideVci"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionInternalLineSideOffset"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionInternalSwitchSideVpi"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionInternalSwitchSideVci"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionInternalSwitchSideOffset"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionLineSideType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionSwitchSideType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaConnectionRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionInternalVpi"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionInternalVci"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionInternalOffset"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionEndpointType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionType"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionConfigurationStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000SubtendingConnectionRowStatus"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsPegCount"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsBlockage"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsHoldTime"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsAvailableTimeslots"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsTimeslotsInUse"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaCurrStatsTimeslotsHighWater"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsPegCount"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsBlockage"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsHoldTime"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsAvailableTimeslots"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaIntervalStatsTimeslotsHighWater"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsUnderFlows"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsOverFlows"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsCellDrop"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsMisInsertedCell"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsSequenceErrors"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsPointerReframes"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsHeaderErrors"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsPointerParityErrors"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsRxCells"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionIntervalStatsTxCells"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsUnderFlows"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsOverFlows"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsCellDrop"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsMisInsertedCell"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsSequenceErrors"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsPointerReframes"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsHeaderErrors"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsPointerParityErrors"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsRxCells"),
        ("CEM-CN1000-VOICE-INFRASTRUCTURE", "cn1000MediaWanConnectionCurrentStatsTxCells"))
)
if mibBuilder.loadTexts:
    cn1000VoiceInfrastructureObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-VOICE-INFRASTRUCTURE",
    **{"Cn1000VoiceInfrastructureSignalingEntityType": Cn1000VoiceInfrastructureSignalingEntityType,
       "Cn1000VoiceInfrastructureSignalingEndpointType": Cn1000VoiceInfrastructureSignalingEndpointType,
       "Cn1000VoiceInfrastructureMediaEndpointType": Cn1000VoiceInfrastructureMediaEndpointType,
       "Cn1000NetworkPathIdentifierRange": Cn1000NetworkPathIdentifierRange,
       "Cn1000VoiceSubtendingConnectionType": Cn1000VoiceSubtendingConnectionType,
       "cn1000VoiceInfrastructureModule": cn1000VoiceInfrastructureModule,
       "cn1000SignalingConfigTable": cn1000SignalingConfigTable,
       "cn1000SignalingConfigEntry": cn1000SignalingConfigEntry,
       "cn1000Shelf": cn1000Shelf,
       "cn1000SlotGroup": cn1000SlotGroup,
       "cn1000Port": cn1000Port,
       "cn1000SignalingSystemAddress": cn1000SignalingSystemAddress,
       "cn1000SignalingSubnet": cn1000SignalingSubnet,
       "cn1000SignalingEntityType": cn1000SignalingEntityType,
       "cn1000SignalingConfigurationStatus": cn1000SignalingConfigurationStatus,
       "cn1000SignalingConfigEntryRowStatus": cn1000SignalingConfigEntryRowStatus,
       "cn1000SignalingEndpointTable": cn1000SignalingEndpointTable,
       "cn1000SignalingEndpointEntry": cn1000SignalingEndpointEntry,
       "cn1000SignalingEndpointVpi": cn1000SignalingEndpointVpi,
       "cn1000SignalingEndpointVci": cn1000SignalingEndpointVci,
       "cn1000SignalingEndpointType": cn1000SignalingEndpointType,
       "cn1000SignalingRemoteSystemAddress": cn1000SignalingRemoteSystemAddress,
       "cn1000SignalingEndpointConfigurationStatus": cn1000SignalingEndpointConfigurationStatus,
       "cn1000SignalingEndpointRowStatus": cn1000SignalingEndpointRowStatus,
       "cn1000SignalingConnectionTable": cn1000SignalingConnectionTable,
       "cn1000SignalingConnectionEntry": cn1000SignalingConnectionEntry,
       "cn1000SignalingConnectionLineSideIfIndex": cn1000SignalingConnectionLineSideIfIndex,
       "cn1000SignalingConnectionLineSideVpi": cn1000SignalingConnectionLineSideVpi,
       "cn1000SignalingConnectionLineSideVci": cn1000SignalingConnectionLineSideVci,
       "cn1000SignalingConnectionSwitchSideIfIndex": cn1000SignalingConnectionSwitchSideIfIndex,
       "cn1000SignalingConnectionLineSideType": cn1000SignalingConnectionLineSideType,
       "cn1000SignalingConnectionSwitchSideType": cn1000SignalingConnectionSwitchSideType,
       "cn1000SignalingConnectionInternalSwitchSideVpi": cn1000SignalingConnectionInternalSwitchSideVpi,
       "cn1000SignalingConnectionInternalSwitchSideVci": cn1000SignalingConnectionInternalSwitchSideVci,
       "cn1000SignalingConnectionConfigurationStatus": cn1000SignalingConnectionConfigurationStatus,
       "cn1000SignalingConnectionRowStatus": cn1000SignalingConnectionRowStatus,
       "cn1000SignalingConnectionDSPvcTag": cn1000SignalingConnectionDSPvcTag,
       "cn1000SignalingConnectionUSPvcTag": cn1000SignalingConnectionUSPvcTag,
       "cn1000MediaEndpointTable": cn1000MediaEndpointTable,
       "cn1000MediaEndpointEntry": cn1000MediaEndpointEntry,
       "cn1000MediaEndpointVpi": cn1000MediaEndpointVpi,
       "cn1000MediaEndpointVci": cn1000MediaEndpointVci,
       "cn1000MediaEndpointRemoteEndpointType": cn1000MediaEndpointRemoteEndpointType,
       "cn1000MediaEndpointRemoteSystemAddress": cn1000MediaEndpointRemoteSystemAddress,
       "cn1000MediaEndpointRemoteLineCardShelf": cn1000MediaEndpointRemoteLineCardShelf,
       "cn1000MediaEndpointRemoteLineCardSlot": cn1000MediaEndpointRemoteLineCardSlot,
       "cn1000MediaEndpointRemoteLineCardOffset": cn1000MediaEndpointRemoteLineCardOffset,
       "cn1000MediaEndpointNetworkPathId": cn1000MediaEndpointNetworkPathId,
       "cn1000MediaEndpointConfigurationStatus": cn1000MediaEndpointConfigurationStatus,
       "cn1000MediaEndpointRowStatus": cn1000MediaEndpointRowStatus,
       "cn1000MediaConnectionTable": cn1000MediaConnectionTable,
       "cn1000MediaConnectionEntry": cn1000MediaConnectionEntry,
       "cn1000MediaConnectionLineSideIfIndex": cn1000MediaConnectionLineSideIfIndex,
       "cn1000MediaConnectionSwitchSideIfIndex": cn1000MediaConnectionSwitchSideIfIndex,
       "cn1000MediaConnectionOffset": cn1000MediaConnectionOffset,
       "cn1000MediaConnectionInternalLineSideVpi": cn1000MediaConnectionInternalLineSideVpi,
       "cn1000MediaConnectionInternalLineSideVci": cn1000MediaConnectionInternalLineSideVci,
       "cn1000MediaConnectionInternalLineSideOffset": cn1000MediaConnectionInternalLineSideOffset,
       "cn1000MediaConnectionInternalSwitchSideVpi": cn1000MediaConnectionInternalSwitchSideVpi,
       "cn1000MediaConnectionInternalSwitchSideVci": cn1000MediaConnectionInternalSwitchSideVci,
       "cn1000MediaConnectionInternalSwitchSideOffset": cn1000MediaConnectionInternalSwitchSideOffset,
       "cn1000MediaConnectionLineSideType": cn1000MediaConnectionLineSideType,
       "cn1000MediaConnectionSwitchSideType": cn1000MediaConnectionSwitchSideType,
       "cn1000MediaConnectionConfigurationStatus": cn1000MediaConnectionConfigurationStatus,
       "cn1000MediaConnectionRowStatus": cn1000MediaConnectionRowStatus,
       "cn1000MediaConnectionDSPvcTag": cn1000MediaConnectionDSPvcTag,
       "cn1000MediaConnectionUSPvcTag": cn1000MediaConnectionUSPvcTag,
       "cn1000MediaWanConnectionTable": cn1000MediaWanConnectionTable,
       "cn1000MediaWanConnectionEntry": cn1000MediaWanConnectionEntry,
       "cn1000MediaConnectionWanIfIndex": cn1000MediaConnectionWanIfIndex,
       "cn1000MediaConnectionWanVpi": cn1000MediaConnectionWanVpi,
       "cn1000MediaConnectionWanVci": cn1000MediaConnectionWanVci,
       "cn1000MediaWanConnectionIfIndex": cn1000MediaWanConnectionIfIndex,
       "cn1000MediaWanConnectionOffset": cn1000MediaWanConnectionOffset,
       "cn1000MediaWanConnectionInternalVpi": cn1000MediaWanConnectionInternalVpi,
       "cn1000MediaWanConnectionInternalVci": cn1000MediaWanConnectionInternalVci,
       "cn1000MediaWanConnectionInternalOffset": cn1000MediaWanConnectionInternalOffset,
       "cn1000MediaWanConnectionEndpointType": cn1000MediaWanConnectionEndpointType,
       "cn1000MediaWanConnectionCdvt": cn1000MediaWanConnectionCdvt,
       "cn1000MediaWanConnectionConfigurationStatus": cn1000MediaWanConnectionConfigurationStatus,
       "cn1000MediaWanConnectionRowStatus": cn1000MediaWanConnectionRowStatus,
       "cn1000MediaWanConnectionDSPvcTag": cn1000MediaWanConnectionDSPvcTag,
       "cn1000MediaWanConnectionUSPvcTag": cn1000MediaWanConnectionUSPvcTag,
       "cn1000SubtendingConnectionTable": cn1000SubtendingConnectionTable,
       "cn1000SubtendingConnectionEntry": cn1000SubtendingConnectionEntry,
       "cn1000SubtendingConnectionIfIndex1": cn1000SubtendingConnectionIfIndex1,
       "cn1000SubtendingConnectionVpi1": cn1000SubtendingConnectionVpi1,
       "cn1000SubtendingConnectionVci1": cn1000SubtendingConnectionVci1,
       "cn1000SubtendingConnectionIfIndex2": cn1000SubtendingConnectionIfIndex2,
       "cn1000SubtendingConnectionVpi2": cn1000SubtendingConnectionVpi2,
       "cn1000SubtendingConnectionVci2": cn1000SubtendingConnectionVci2,
       "cn1000SubtendingConnectionType": cn1000SubtendingConnectionType,
       "cn1000SubtendingConnectionConfigurationStatus": cn1000SubtendingConnectionConfigurationStatus,
       "cn1000SubtendingConnectionRowStatus": cn1000SubtendingConnectionRowStatus,
       "cn1000SubtendingConnectionDSPvcTag": cn1000SubtendingConnectionDSPvcTag,
       "cn1000SubtendingConnectionUSPvcTag": cn1000SubtendingConnectionUSPvcTag,
       "cn1000MediaCurrentStatsTable": cn1000MediaCurrentStatsTable,
       "cn1000MediaCurrentStatsEntry": cn1000MediaCurrentStatsEntry,
       "cn1000MediaCurrStatsDs1Shelf": cn1000MediaCurrStatsDs1Shelf,
       "cn1000MediaCurrStatsDs1SlotGroup": cn1000MediaCurrStatsDs1SlotGroup,
       "cn1000MediaCurrStatsRemoteSysAddr": cn1000MediaCurrStatsRemoteSysAddr,
       "cn1000MediaCurrStatsPegCount": cn1000MediaCurrStatsPegCount,
       "cn1000MediaCurrStatsBlockage": cn1000MediaCurrStatsBlockage,
       "cn1000MediaCurrStatsHoldTime": cn1000MediaCurrStatsHoldTime,
       "cn1000MediaCurrStatsAvailableTimeslots": cn1000MediaCurrStatsAvailableTimeslots,
       "cn1000MediaCurrStatsTimeslotsInUse": cn1000MediaCurrStatsTimeslotsInUse,
       "cn1000MediaCurrStatsTimeslotsHighWater": cn1000MediaCurrStatsTimeslotsHighWater,
       "cn1000MediaIntervalStatsTable": cn1000MediaIntervalStatsTable,
       "cn1000MediaIntervalStatsEntry": cn1000MediaIntervalStatsEntry,
       "cn1000MediaIntervalStatsDs1Shelf": cn1000MediaIntervalStatsDs1Shelf,
       "cn1000MediaIntervalStatsDs1SlotGroup": cn1000MediaIntervalStatsDs1SlotGroup,
       "cn1000MediaIntervalStatsRemoteSysAddr": cn1000MediaIntervalStatsRemoteSysAddr,
       "cn1000MediaIntervalStatsInterval": cn1000MediaIntervalStatsInterval,
       "cn1000MediaIntervalStatsPegCount": cn1000MediaIntervalStatsPegCount,
       "cn1000MediaIntervalStatsBlockage": cn1000MediaIntervalStatsBlockage,
       "cn1000MediaIntervalStatsHoldTime": cn1000MediaIntervalStatsHoldTime,
       "cn1000MediaIntervalStatsAvailableTimeslots": cn1000MediaIntervalStatsAvailableTimeslots,
       "cn1000MediaIntervalStatsTimeslotsHighWater": cn1000MediaIntervalStatsTimeslotsHighWater,
       "cn1000MediaWanConnectionIntervalStatsTable": cn1000MediaWanConnectionIntervalStatsTable,
       "cn1000MediaWanConnectionIntervalStatsEntry": cn1000MediaWanConnectionIntervalStatsEntry,
       "cn1000MediaConnectionWanIntervalStatsIfIndex": cn1000MediaConnectionWanIntervalStatsIfIndex,
       "cn1000MediaConnectionWanIntervalStatsVpi": cn1000MediaConnectionWanIntervalStatsVpi,
       "cn1000MediaConnectionWanIntervalStatsVci": cn1000MediaConnectionWanIntervalStatsVci,
       "cn1000MediaWanConnectionIntervalStatsIfIndex": cn1000MediaWanConnectionIntervalStatsIfIndex,
       "cn1000MediaWanConnectionIntervalStatsOffset": cn1000MediaWanConnectionIntervalStatsOffset,
       "cn1000MediaWanConnectionIntervalStatsInterval": cn1000MediaWanConnectionIntervalStatsInterval,
       "cn1000MediaWanConnectionIntervalStatsUnderFlows": cn1000MediaWanConnectionIntervalStatsUnderFlows,
       "cn1000MediaWanConnectionIntervalStatsOverFlows": cn1000MediaWanConnectionIntervalStatsOverFlows,
       "cn1000MediaWanConnectionIntervalStatsCellDrop": cn1000MediaWanConnectionIntervalStatsCellDrop,
       "cn1000MediaWanConnectionIntervalStatsMisInsertedCell": cn1000MediaWanConnectionIntervalStatsMisInsertedCell,
       "cn1000MediaWanConnectionIntervalStatsSequenceErrors": cn1000MediaWanConnectionIntervalStatsSequenceErrors,
       "cn1000MediaWanConnectionIntervalStatsPointerReframes": cn1000MediaWanConnectionIntervalStatsPointerReframes,
       "cn1000MediaWanConnectionIntervalStatsHeaderErrors": cn1000MediaWanConnectionIntervalStatsHeaderErrors,
       "cn1000MediaWanConnectionIntervalStatsPointerParityErrors": cn1000MediaWanConnectionIntervalStatsPointerParityErrors,
       "cn1000MediaWanConnectionIntervalStatsRxCells": cn1000MediaWanConnectionIntervalStatsRxCells,
       "cn1000MediaWanConnectionIntervalStatsTxCells": cn1000MediaWanConnectionIntervalStatsTxCells,
       "cn1000MediaWanConnectionCurrentStatsTable": cn1000MediaWanConnectionCurrentStatsTable,
       "cn1000MediaWanConnectionCurrentStatsEntry": cn1000MediaWanConnectionCurrentStatsEntry,
       "cn1000MediaConnectionWanCurrentStatsIfIndex": cn1000MediaConnectionWanCurrentStatsIfIndex,
       "cn1000MediaConnectionWanCurrentStatsVpi": cn1000MediaConnectionWanCurrentStatsVpi,
       "cn1000MediaConnectionWanCurrentStatsVci": cn1000MediaConnectionWanCurrentStatsVci,
       "cn1000MediaWanConnectionCurrentStatsIfIndex": cn1000MediaWanConnectionCurrentStatsIfIndex,
       "cn1000MediaWanConnectionCurrentStatsOffset": cn1000MediaWanConnectionCurrentStatsOffset,
       "cn1000MediaWanConnectionCurrentStatsUnderFlows": cn1000MediaWanConnectionCurrentStatsUnderFlows,
       "cn1000MediaWanConnectionCurrentStatsOverFlows": cn1000MediaWanConnectionCurrentStatsOverFlows,
       "cn1000MediaWanConnectionCurrentStatsCellDrop": cn1000MediaWanConnectionCurrentStatsCellDrop,
       "cn1000MediaWanConnectionCurrentStatsMisInsertedCell": cn1000MediaWanConnectionCurrentStatsMisInsertedCell,
       "cn1000MediaWanConnectionCurrentStatsSequenceErrors": cn1000MediaWanConnectionCurrentStatsSequenceErrors,
       "cn1000MediaWanConnectionCurrentStatsPointerReframes": cn1000MediaWanConnectionCurrentStatsPointerReframes,
       "cn1000MediaWanConnectionCurrentStatsHeaderErrors": cn1000MediaWanConnectionCurrentStatsHeaderErrors,
       "cn1000MediaWanConnectionCurrentStatsPointerParityErrors": cn1000MediaWanConnectionCurrentStatsPointerParityErrors,
       "cn1000MediaWanConnectionCurrentStatsRxCells": cn1000MediaWanConnectionCurrentStatsRxCells,
       "cn1000MediaWanConnectionCurrentStatsTxCells": cn1000MediaWanConnectionCurrentStatsTxCells,
       "cn1000VoiceInfrastructureConformance": cn1000VoiceInfrastructureConformance,
       "cn1000VoiceInfrastructureObjectGroup": cn1000VoiceInfrastructureObjectGroup}
)
