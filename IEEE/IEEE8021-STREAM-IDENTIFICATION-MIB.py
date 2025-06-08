# SNMP MIB module (IEEE8021-STREAM-IDENTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-STREAM-IDENTIFICATION-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:12:58 2025
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

(IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(AutonomousType,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ieee8021StreamIdMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMib.setRevisions(
        ("2021-12-09 00:00",
         "2021-12-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Ieee8021CBStreamIdentificationType(TextualConvention, Integer32):
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("nullStreamIdentification", 1),
          ("srcMacVlanStreamIdentification", 2),
          ("activeDstMacVlanStreamIdentification", 3),
          ("ipStreamStreamIdentification", 4),
          ("maskAndMatchStreamIdentification", 5),
          ("nonIEEESpecified", 256))
    )



class Ieee8021CBTaggedType(TextualConvention, Integer32):
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
        *(("tagged", 1),
          ("priority", 2),
          ("all", 3))
    )



class Ieee8021CBVlanIdentifier(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class Ieee8021CBIpDscpType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )



class Ieee8021CBIdNextProtocolType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("udp", 2),
          ("tcp", 3),
          ("sctp", 4))
    )



class Ieee8021CBLanPathIdType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021StreamIdNotifications_ObjectIdentity = ObjectIdentity
ieee8021StreamIdNotifications = _Ieee8021StreamIdNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 0)
)
_Ieee8021StreamIdObjects_ObjectIdentity = ObjectIdentity
ieee8021StreamIdObjects = _Ieee8021StreamIdObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1)
)
_Ieee8021StreamIdStreamIdentification_ObjectIdentity = ObjectIdentity
ieee8021StreamIdStreamIdentification = _Ieee8021StreamIdStreamIdentification_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1)
)
_Ieee8021StreamIdStreamIdentificationTypes_ObjectIdentity = ObjectIdentity
ieee8021StreamIdStreamIdentificationTypes = _Ieee8021StreamIdStreamIdentificationTypes_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 1)
)
_Ieee8021StreamIdNullStream_ObjectIdentity = ObjectIdentity
ieee8021StreamIdNullStream = _Ieee8021StreamIdNullStream_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdNullStream.setStatus("current")
_Ieee8021StreamIdSrcMacVlan_ObjectIdentity = ObjectIdentity
ieee8021StreamIdSrcMacVlan = _Ieee8021StreamIdSrcMacVlan_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdSrcMacVlan.setStatus("current")
_Ieee8021StreamIdActiveDestMacVlan_ObjectIdentity = ObjectIdentity
ieee8021StreamIdActiveDestMacVlan = _Ieee8021StreamIdActiveDestMacVlan_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdActiveDestMacVlan.setStatus("current")
_Ieee8021StreamIdIpStream_ObjectIdentity = ObjectIdentity
ieee8021StreamIdIpStream = _Ieee8021StreamIdIpStream_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdIpStream.setStatus("current")
_Ieee8021StreamIdMaskAndMatch_ObjectIdentity = ObjectIdentity
ieee8021StreamIdMaskAndMatch = _Ieee8021StreamIdMaskAndMatch_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatch.setStatus("current")
_Ieee8021StreamIdStreamIdentificationTable_Object = MibTable
ieee8021StreamIdStreamIdentificationTable = _Ieee8021StreamIdStreamIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdentificationTable.setStatus("current")
_Ieee8021StreamIdStreamIdentificationEntry_Object = MibTableRow
ieee8021StreamIdStreamIdentificationEntry = _Ieee8021StreamIdStreamIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1)
)
ieee8021StreamIdStreamIdentificationEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdentificationEntry.setStatus("current")
_Ieee8021StreamIdStreamIdentificationIndex_Type = Unsigned32
_Ieee8021StreamIdStreamIdentificationIndex_Object = MibTableColumn
ieee8021StreamIdStreamIdentificationIndex = _Ieee8021StreamIdStreamIdentificationIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 1),
    _Ieee8021StreamIdStreamIdentificationIndex_Type()
)
ieee8021StreamIdStreamIdentificationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdentificationIndex.setStatus("current")


class _Ieee8021StreamIdStreamIdIdentificationType_Type(Ieee8021CBStreamIdentificationType):
    """Custom type ieee8021StreamIdStreamIdIdentificationType based on Ieee8021CBStreamIdentificationType"""
    defaultValue = 1


_Ieee8021StreamIdStreamIdIdentificationType_Type.__name__ = "Ieee8021CBStreamIdentificationType"
_Ieee8021StreamIdStreamIdIdentificationType_Object = MibTableColumn
ieee8021StreamIdStreamIdIdentificationType = _Ieee8021StreamIdStreamIdIdentificationType_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 2),
    _Ieee8021StreamIdStreamIdIdentificationType_Type()
)
ieee8021StreamIdStreamIdIdentificationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdIdentificationType.setStatus("current")


class _Ieee8021StreamIdStreamIdIdentificationTypeOUI_Type(OctetString):
    """Custom type ieee8021StreamIdStreamIdIdentificationTypeOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021StreamIdStreamIdIdentificationTypeOUI_Type.__name__ = "OctetString"
_Ieee8021StreamIdStreamIdIdentificationTypeOUI_Object = MibTableColumn
ieee8021StreamIdStreamIdIdentificationTypeOUI = _Ieee8021StreamIdStreamIdIdentificationTypeOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 3),
    _Ieee8021StreamIdStreamIdIdentificationTypeOUI_Type()
)
ieee8021StreamIdStreamIdIdentificationTypeOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdIdentificationTypeOUI.setStatus("current")


class _Ieee8021StreamIdStreamIdIdentificationCustomType_Type(Integer32):
    """Custom type ieee8021StreamIdStreamIdIdentificationCustomType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Ieee8021StreamIdStreamIdIdentificationCustomType_Type.__name__ = "Integer32"
_Ieee8021StreamIdStreamIdIdentificationCustomType_Object = MibTableColumn
ieee8021StreamIdStreamIdIdentificationCustomType = _Ieee8021StreamIdStreamIdIdentificationCustomType_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 4),
    _Ieee8021StreamIdStreamIdIdentificationCustomType_Type()
)
ieee8021StreamIdStreamIdIdentificationCustomType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdIdentificationCustomType.setStatus("current")


class _Ieee8021StreamIdStreamIdIdentificationCustomTypeOUI_Type(OctetString):
    """Custom type ieee8021StreamIdStreamIdIdentificationCustomTypeOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021StreamIdStreamIdIdentificationCustomTypeOUI_Type.__name__ = "OctetString"
_Ieee8021StreamIdStreamIdIdentificationCustomTypeOUI_Object = MibTableColumn
ieee8021StreamIdStreamIdIdentificationCustomTypeOUI = _Ieee8021StreamIdStreamIdIdentificationCustomTypeOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 5),
    _Ieee8021StreamIdStreamIdIdentificationCustomTypeOUI_Type()
)
ieee8021StreamIdStreamIdIdentificationCustomTypeOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdIdentificationCustomTypeOUI.setStatus("current")
_Ieee8021StreamIdStreamIdIdentificationTypeSelect_Type = AutonomousType
_Ieee8021StreamIdStreamIdIdentificationTypeSelect_Object = MibTableColumn
ieee8021StreamIdStreamIdIdentificationTypeSelect = _Ieee8021StreamIdStreamIdIdentificationTypeSelect_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 6),
    _Ieee8021StreamIdStreamIdIdentificationTypeSelect_Type()
)
ieee8021StreamIdStreamIdIdentificationTypeSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdIdentificationTypeSelect.setStatus("current")
_Ieee8021StreamIdStreamIdHandle_Type = Unsigned32
_Ieee8021StreamIdStreamIdHandle_Object = MibTableColumn
ieee8021StreamIdStreamIdHandle = _Ieee8021StreamIdStreamIdHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 7),
    _Ieee8021StreamIdStreamIdHandle_Type()
)
ieee8021StreamIdStreamIdHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdHandle.setStatus("current")
_Ieee8021StreamIdStreamIdInFacOutputPortList_Type = AutonomousType
_Ieee8021StreamIdStreamIdInFacOutputPortList_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacOutputPortList = _Ieee8021StreamIdStreamIdInFacOutputPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 8),
    _Ieee8021StreamIdStreamIdInFacOutputPortList_Type()
)
ieee8021StreamIdStreamIdInFacOutputPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacOutputPortList.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacOutputPortList_Type = AutonomousType
_Ieee8021StreamIdStreamIdOutFacOutputPortList_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacOutputPortList = _Ieee8021StreamIdStreamIdOutFacOutputPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 9),
    _Ieee8021StreamIdStreamIdOutFacOutputPortList_Type()
)
ieee8021StreamIdStreamIdOutFacOutputPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacOutputPortList.setStatus("current")
_Ieee8021StreamIdStreamIdInFacInputPortList_Type = AutonomousType
_Ieee8021StreamIdStreamIdInFacInputPortList_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacInputPortList = _Ieee8021StreamIdStreamIdInFacInputPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 10),
    _Ieee8021StreamIdStreamIdInFacInputPortList_Type()
)
ieee8021StreamIdStreamIdInFacInputPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacInputPortList.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacInputPortList_Type = AutonomousType
_Ieee8021StreamIdStreamIdOutFacInputPortList_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacInputPortList = _Ieee8021StreamIdStreamIdOutFacInputPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 11),
    _Ieee8021StreamIdStreamIdOutFacInputPortList_Type()
)
ieee8021StreamIdStreamIdOutFacInputPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacInputPortList.setStatus("current")
_Ieee8021StreamIdAutoConfigured_Type = TruthValue
_Ieee8021StreamIdAutoConfigured_Object = MibTableColumn
ieee8021StreamIdAutoConfigured = _Ieee8021StreamIdAutoConfigured_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 12),
    _Ieee8021StreamIdAutoConfigured_Type()
)
ieee8021StreamIdAutoConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdAutoConfigured.setStatus("current")
_Ieee8021StreamIdLanPathId_Type = Ieee8021CBLanPathIdType
_Ieee8021StreamIdLanPathId_Object = MibTableColumn
ieee8021StreamIdLanPathId = _Ieee8021StreamIdLanPathId_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 13),
    _Ieee8021StreamIdLanPathId_Type()
)
ieee8021StreamIdLanPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdLanPathId.setStatus("current")
_Ieee8021StreamIdStatus_Type = RowStatus
_Ieee8021StreamIdStatus_Object = MibTableColumn
ieee8021StreamIdStatus = _Ieee8021StreamIdStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 2, 1, 14),
    _Ieee8021StreamIdStatus_Type()
)
ieee8021StreamIdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStatus.setStatus("current")
_Ieee8021StreamIdNullStreamIdentificationTable_Object = MibTable
ieee8021StreamIdNullStreamIdentificationTable = _Ieee8021StreamIdNullStreamIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdNullStreamIdentificationTable.setStatus("current")
_Ieee8021StreamIdNullStreamIdentificationEntry_Object = MibTableRow
ieee8021StreamIdNullStreamIdentificationEntry = _Ieee8021StreamIdNullStreamIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 3, 1)
)
ieee8021StreamIdNullStreamIdentificationEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdNullStreamIdentificationEntry.setStatus("current")
_Ieee8021StreamIdCpeNullDownDestMac_Type = MacAddress
_Ieee8021StreamIdCpeNullDownDestMac_Object = MibTableColumn
ieee8021StreamIdCpeNullDownDestMac = _Ieee8021StreamIdCpeNullDownDestMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 3, 1, 1),
    _Ieee8021StreamIdCpeNullDownDestMac_Type()
)
ieee8021StreamIdCpeNullDownDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeNullDownDestMac.setStatus("current")
_Ieee8021StreamIdCPENullDownTagged_Type = Ieee8021CBTaggedType
_Ieee8021StreamIdCPENullDownTagged_Object = MibTableColumn
ieee8021StreamIdCPENullDownTagged = _Ieee8021StreamIdCPENullDownTagged_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 3, 1, 2),
    _Ieee8021StreamIdCPENullDownTagged_Type()
)
ieee8021StreamIdCPENullDownTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCPENullDownTagged.setStatus("current")
_Ieee8021StreamIdCpeNullDownVlan_Type = Ieee8021CBVlanIdentifier
_Ieee8021StreamIdCpeNullDownVlan_Object = MibTableColumn
ieee8021StreamIdCpeNullDownVlan = _Ieee8021StreamIdCpeNullDownVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 3, 1, 3),
    _Ieee8021StreamIdCpeNullDownVlan_Type()
)
ieee8021StreamIdCpeNullDownVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeNullDownVlan.setStatus("current")
_Ieee8021StreamIdSrcMacVlanIdentificationTable_Object = MibTable
ieee8021StreamIdSrcMacVlanIdentificationTable = _Ieee8021StreamIdSrcMacVlanIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdSrcMacVlanIdentificationTable.setStatus("current")
_Ieee8021StreamIdSrcMacVlanIdentificationEntry_Object = MibTableRow
ieee8021StreamIdSrcMacVlanIdentificationEntry = _Ieee8021StreamIdSrcMacVlanIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 4, 1)
)
ieee8021StreamIdSrcMacVlanIdentificationEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdSrcMacVlanIdentificationEntry.setStatus("current")
_Ieee8021StreamIdCpeSmacVlanDownSrcMac_Type = MacAddress
_Ieee8021StreamIdCpeSmacVlanDownSrcMac_Object = MibTableColumn
ieee8021StreamIdCpeSmacVlanDownSrcMac = _Ieee8021StreamIdCpeSmacVlanDownSrcMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 4, 1, 1),
    _Ieee8021StreamIdCpeSmacVlanDownSrcMac_Type()
)
ieee8021StreamIdCpeSmacVlanDownSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeSmacVlanDownSrcMac.setStatus("current")
_Ieee8021StreamIdCpeSmacVlanDownTagged_Type = Ieee8021CBTaggedType
_Ieee8021StreamIdCpeSmacVlanDownTagged_Object = MibTableColumn
ieee8021StreamIdCpeSmacVlanDownTagged = _Ieee8021StreamIdCpeSmacVlanDownTagged_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 4, 1, 2),
    _Ieee8021StreamIdCpeSmacVlanDownTagged_Type()
)
ieee8021StreamIdCpeSmacVlanDownTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeSmacVlanDownTagged.setStatus("current")
_Ieee8021StreamIdCpeSmacVlanDownVlan_Type = Ieee8021CBVlanIdentifier
_Ieee8021StreamIdCpeSmacVlanDownVlan_Object = MibTableColumn
ieee8021StreamIdCpeSmacVlanDownVlan = _Ieee8021StreamIdCpeSmacVlanDownVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 4, 1, 3),
    _Ieee8021StreamIdCpeSmacVlanDownVlan_Type()
)
ieee8021StreamIdCpeSmacVlanDownVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeSmacVlanDownVlan.setStatus("current")
_Ieee8021StreamIdActiveDestMacVlanIdentificationTable_Object = MibTable
ieee8021StreamIdActiveDestMacVlanIdentificationTable = _Ieee8021StreamIdActiveDestMacVlanIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdActiveDestMacVlanIdentificationTable.setStatus("current")
_Ieee8021StreamIdActiveDestMacVlanIdentificationEntry_Object = MibTableRow
ieee8021StreamIdActiveDestMacVlanIdentificationEntry = _Ieee8021StreamIdActiveDestMacVlanIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1)
)
ieee8021StreamIdActiveDestMacVlanIdentificationEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdActiveDestMacVlanIdentificationEntry.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanDownDestMac_Type = MacAddress
_Ieee8021StreamIdCpeDmacVlanDownDestMac_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanDownDestMac = _Ieee8021StreamIdCpeDmacVlanDownDestMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 1),
    _Ieee8021StreamIdCpeDmacVlanDownDestMac_Type()
)
ieee8021StreamIdCpeDmacVlanDownDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanDownDestMac.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanDownTagged_Type = Ieee8021CBTaggedType
_Ieee8021StreamIdCpeDmacVlanDownTagged_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanDownTagged = _Ieee8021StreamIdCpeDmacVlanDownTagged_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 2),
    _Ieee8021StreamIdCpeDmacVlanDownTagged_Type()
)
ieee8021StreamIdCpeDmacVlanDownTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanDownTagged.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanDownVlan_Type = Ieee8021CBVlanIdentifier
_Ieee8021StreamIdCpeDmacVlanDownVlan_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanDownVlan = _Ieee8021StreamIdCpeDmacVlanDownVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 3),
    _Ieee8021StreamIdCpeDmacVlanDownVlan_Type()
)
ieee8021StreamIdCpeDmacVlanDownVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanDownVlan.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanDownPriority_Type = IEEE8021PriorityValue
_Ieee8021StreamIdCpeDmacVlanDownPriority_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanDownPriority = _Ieee8021StreamIdCpeDmacVlanDownPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 4),
    _Ieee8021StreamIdCpeDmacVlanDownPriority_Type()
)
ieee8021StreamIdCpeDmacVlanDownPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanDownPriority.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanUpDestMac_Type = MacAddress
_Ieee8021StreamIdCpeDmacVlanUpDestMac_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanUpDestMac = _Ieee8021StreamIdCpeDmacVlanUpDestMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 5),
    _Ieee8021StreamIdCpeDmacVlanUpDestMac_Type()
)
ieee8021StreamIdCpeDmacVlanUpDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanUpDestMac.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanUpTagged_Type = Ieee8021CBTaggedType
_Ieee8021StreamIdCpeDmacVlanUpTagged_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanUpTagged = _Ieee8021StreamIdCpeDmacVlanUpTagged_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 6),
    _Ieee8021StreamIdCpeDmacVlanUpTagged_Type()
)
ieee8021StreamIdCpeDmacVlanUpTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanUpTagged.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanUpVlan_Type = Ieee8021CBVlanIdentifier
_Ieee8021StreamIdCpeDmacVlanUpVlan_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanUpVlan = _Ieee8021StreamIdCpeDmacVlanUpVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 7),
    _Ieee8021StreamIdCpeDmacVlanUpVlan_Type()
)
ieee8021StreamIdCpeDmacVlanUpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanUpVlan.setStatus("current")
_Ieee8021StreamIdCpeDmacVlanUpPriority_Type = IEEE8021PriorityValue
_Ieee8021StreamIdCpeDmacVlanUpPriority_Object = MibTableColumn
ieee8021StreamIdCpeDmacVlanUpPriority = _Ieee8021StreamIdCpeDmacVlanUpPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 5, 1, 8),
    _Ieee8021StreamIdCpeDmacVlanUpPriority_Type()
)
ieee8021StreamIdCpeDmacVlanUpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeDmacVlanUpPriority.setStatus("current")
_Ieee8021StreamIdIpStreamIdentificationTable_Object = MibTable
ieee8021StreamIdIpStreamIdentificationTable = _Ieee8021StreamIdIpStreamIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdIpStreamIdentificationTable.setStatus("current")
_Ieee8021StreamIdIpStreamIdentificationEntry_Object = MibTableRow
ieee8021StreamIdIpStreamIdentificationEntry = _Ieee8021StreamIdIpStreamIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1)
)
ieee8021StreamIdIpStreamIdentificationEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdIpStreamIdentificationEntry.setStatus("current")
_Ieee8021StreamIdCpeIpIdDestMac_Type = MacAddress
_Ieee8021StreamIdCpeIpIdDestMac_Object = MibTableColumn
ieee8021StreamIdCpeIpIdDestMac = _Ieee8021StreamIdCpeIpIdDestMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 1),
    _Ieee8021StreamIdCpeIpIdDestMac_Type()
)
ieee8021StreamIdCpeIpIdDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdDestMac.setStatus("current")
_Ieee8021StreamIdCpeIpIdTagged_Type = Ieee8021CBTaggedType
_Ieee8021StreamIdCpeIpIdTagged_Object = MibTableColumn
ieee8021StreamIdCpeIpIdTagged = _Ieee8021StreamIdCpeIpIdTagged_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 2),
    _Ieee8021StreamIdCpeIpIdTagged_Type()
)
ieee8021StreamIdCpeIpIdTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdTagged.setStatus("current")
_Ieee8021StreamIdCpeIpIdVlan_Type = Ieee8021CBVlanIdentifier
_Ieee8021StreamIdCpeIpIdVlan_Object = MibTableColumn
ieee8021StreamIdCpeIpIdVlan = _Ieee8021StreamIdCpeIpIdVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 3),
    _Ieee8021StreamIdCpeIpIdVlan_Type()
)
ieee8021StreamIdCpeIpIdVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdVlan.setStatus("current")
_Ieee8021StreamIdCpeIpIdIpSourceType_Type = InetAddressType
_Ieee8021StreamIdCpeIpIdIpSourceType_Object = MibTableColumn
ieee8021StreamIdCpeIpIdIpSourceType = _Ieee8021StreamIdCpeIpIdIpSourceType_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 4),
    _Ieee8021StreamIdCpeIpIdIpSourceType_Type()
)
ieee8021StreamIdCpeIpIdIpSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdIpSourceType.setStatus("current")
_Ieee8021StreamIdCpeIpIdIpSource_Type = InetAddress
_Ieee8021StreamIdCpeIpIdIpSource_Object = MibTableColumn
ieee8021StreamIdCpeIpIdIpSource = _Ieee8021StreamIdCpeIpIdIpSource_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 5),
    _Ieee8021StreamIdCpeIpIdIpSource_Type()
)
ieee8021StreamIdCpeIpIdIpSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdIpSource.setStatus("current")
_Ieee8021StreamIdCpeIpIdIpDestinationType_Type = InetAddressType
_Ieee8021StreamIdCpeIpIdIpDestinationType_Object = MibTableColumn
ieee8021StreamIdCpeIpIdIpDestinationType = _Ieee8021StreamIdCpeIpIdIpDestinationType_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 6),
    _Ieee8021StreamIdCpeIpIdIpDestinationType_Type()
)
ieee8021StreamIdCpeIpIdIpDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdIpDestinationType.setStatus("current")
_Ieee8021StreamIdCpeIpIdIpDestination_Type = InetAddress
_Ieee8021StreamIdCpeIpIdIpDestination_Object = MibTableColumn
ieee8021StreamIdCpeIpIdIpDestination = _Ieee8021StreamIdCpeIpIdIpDestination_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 7),
    _Ieee8021StreamIdCpeIpIdIpDestination_Type()
)
ieee8021StreamIdCpeIpIdIpDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdIpDestination.setStatus("current")
_Ieee8021StreamIdCpeIpIdDscp_Type = Ieee8021CBIpDscpType
_Ieee8021StreamIdCpeIpIdDscp_Object = MibTableColumn
ieee8021StreamIdCpeIpIdDscp = _Ieee8021StreamIdCpeIpIdDscp_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 8),
    _Ieee8021StreamIdCpeIpIdDscp_Type()
)
ieee8021StreamIdCpeIpIdDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdDscp.setStatus("current")
_Ieee8021StreamIdCpeIpIdNextProtocol_Type = Ieee8021CBIdNextProtocolType
_Ieee8021StreamIdCpeIpIdNextProtocol_Object = MibTableColumn
ieee8021StreamIdCpeIpIdNextProtocol = _Ieee8021StreamIdCpeIpIdNextProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 9),
    _Ieee8021StreamIdCpeIpIdNextProtocol_Type()
)
ieee8021StreamIdCpeIpIdNextProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdNextProtocol.setStatus("current")
_Ieee8021StreamIdCpeIpIdSourcePort_Type = InetPortNumber
_Ieee8021StreamIdCpeIpIdSourcePort_Object = MibTableColumn
ieee8021StreamIdCpeIpIdSourcePort = _Ieee8021StreamIdCpeIpIdSourcePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 10),
    _Ieee8021StreamIdCpeIpIdSourcePort_Type()
)
ieee8021StreamIdCpeIpIdSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdSourcePort.setStatus("current")
_Ieee8021StreamIdCpeIpIdDestinationPort_Type = InetPortNumber
_Ieee8021StreamIdCpeIpIdDestinationPort_Object = MibTableColumn
ieee8021StreamIdCpeIpIdDestinationPort = _Ieee8021StreamIdCpeIpIdDestinationPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 6, 1, 11),
    _Ieee8021StreamIdCpeIpIdDestinationPort_Type()
)
ieee8021StreamIdCpeIpIdDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeIpIdDestinationPort.setStatus("current")
_Ieee8021StreamIdMaskAndMatchIdentificationTable_Object = MibTable
ieee8021StreamIdMaskAndMatchIdentificationTable = _Ieee8021StreamIdMaskAndMatchIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchIdentificationTable.setStatus("current")
_Ieee8021StreamIdMaskAndMatchIdentificationEntry_Object = MibTableRow
ieee8021StreamIdMaskAndMatchIdentificationEntry = _Ieee8021StreamIdMaskAndMatchIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1)
)
ieee8021StreamIdMaskAndMatchIdentificationEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchIdentificationEntry.setStatus("current")
_Ieee8021StreamIdCpeMmIdDestMacMask_Type = MacAddress
_Ieee8021StreamIdCpeMmIdDestMacMask_Object = MibTableColumn
ieee8021StreamIdCpeMmIdDestMacMask = _Ieee8021StreamIdCpeMmIdDestMacMask_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 1),
    _Ieee8021StreamIdCpeMmIdDestMacMask_Type()
)
ieee8021StreamIdCpeMmIdDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdDestMacMask.setStatus("current")
_Ieee8021StreamIdCpeMmIdDestMacMatch_Type = MacAddress
_Ieee8021StreamIdCpeMmIdDestMacMatch_Object = MibTableColumn
ieee8021StreamIdCpeMmIdDestMacMatch = _Ieee8021StreamIdCpeMmIdDestMacMatch_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 2),
    _Ieee8021StreamIdCpeMmIdDestMacMatch_Type()
)
ieee8021StreamIdCpeMmIdDestMacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdDestMacMatch.setStatus("current")
_Ieee8021StreamIdCpeMmIdSrcMacMask_Type = MacAddress
_Ieee8021StreamIdCpeMmIdSrcMacMask_Object = MibTableColumn
ieee8021StreamIdCpeMmIdSrcMacMask = _Ieee8021StreamIdCpeMmIdSrcMacMask_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 3),
    _Ieee8021StreamIdCpeMmIdSrcMacMask_Type()
)
ieee8021StreamIdCpeMmIdSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdSrcMacMask.setStatus("current")
_Ieee8021StreamIdCpeMmIdSrcMacMatch_Type = MacAddress
_Ieee8021StreamIdCpeMmIdSrcMacMatch_Object = MibTableColumn
ieee8021StreamIdCpeMmIdSrcMacMatch = _Ieee8021StreamIdCpeMmIdSrcMacMatch_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 4),
    _Ieee8021StreamIdCpeMmIdSrcMacMatch_Type()
)
ieee8021StreamIdCpeMmIdSrcMacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdSrcMacMatch.setStatus("current")


class _Ieee8021StreamIdCpeMmIdMsduMaskLength_Type(Integer32):
    """Custom type ieee8021StreamIdCpeMmIdMsduMaskLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1984),
    )


_Ieee8021StreamIdCpeMmIdMsduMaskLength_Type.__name__ = "Integer32"
_Ieee8021StreamIdCpeMmIdMsduMaskLength_Object = MibTableColumn
ieee8021StreamIdCpeMmIdMsduMaskLength = _Ieee8021StreamIdCpeMmIdMsduMaskLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 5),
    _Ieee8021StreamIdCpeMmIdMsduMaskLength_Type()
)
ieee8021StreamIdCpeMmIdMsduMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdMsduMaskLength.setStatus("current")


class _Ieee8021StreamIdCpeMmIdMsduMask_Type(OctetString):
    """Custom type ieee8021StreamIdCpeMmIdMsduMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1984),
    )


_Ieee8021StreamIdCpeMmIdMsduMask_Type.__name__ = "OctetString"
_Ieee8021StreamIdCpeMmIdMsduMask_Object = MibTableColumn
ieee8021StreamIdCpeMmIdMsduMask = _Ieee8021StreamIdCpeMmIdMsduMask_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 6),
    _Ieee8021StreamIdCpeMmIdMsduMask_Type()
)
ieee8021StreamIdCpeMmIdMsduMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdMsduMask.setStatus("current")


class _Ieee8021StreamIdCpeMmIdMsduMatch_Type(OctetString):
    """Custom type ieee8021StreamIdCpeMmIdMsduMatch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1984),
    )


_Ieee8021StreamIdCpeMmIdMsduMatch_Type.__name__ = "OctetString"
_Ieee8021StreamIdCpeMmIdMsduMatch_Object = MibTableColumn
ieee8021StreamIdCpeMmIdMsduMatch = _Ieee8021StreamIdCpeMmIdMsduMatch_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 1, 7, 1, 7),
    _Ieee8021StreamIdCpeMmIdMsduMatch_Type()
)
ieee8021StreamIdCpeMmIdMsduMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdCpeMmIdMsduMatch.setStatus("current")
_Ieee8021StreamIdStreamIdInFacOutputPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021StreamIdStreamIdInFacOutputPortHandleList = _Ieee8021StreamIdStreamIdInFacOutputPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 2)
)
_Ieee8021StreamIdStreamIdInFacOutputPortHandleListTable_Object = MibTable
ieee8021StreamIdStreamIdInFacOutputPortHandleListTable = _Ieee8021StreamIdStreamIdInFacOutputPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacOutputPortHandleListTable.setStatus("current")
_Ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry_Object = MibTableRow
ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry = _Ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 2, 2, 1)
)
ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry.setStatus("current")
_Ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex_Type = Unsigned32
_Ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex = _Ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 2, 2, 1, 1),
    _Ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex_Type()
)
ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex.setStatus("current")
_Ieee8021StreamIdStreamIdInFacOutputPortHandle_Type = VariablePointer
_Ieee8021StreamIdStreamIdInFacOutputPortHandle_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacOutputPortHandle = _Ieee8021StreamIdStreamIdInFacOutputPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 2, 2, 1, 2),
    _Ieee8021StreamIdStreamIdInFacOutputPortHandle_Type()
)
ieee8021StreamIdStreamIdInFacOutputPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacOutputPortHandle.setStatus("current")
_Ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus_Type = RowStatus
_Ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus = _Ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 2, 2, 1, 3),
    _Ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus_Type()
)
ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021StreamIdStreamIdOutFacOutputPortHandleList = _Ieee8021StreamIdStreamIdOutFacOutputPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 3)
)
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleListTable_Object = MibTable
ieee8021StreamIdStreamIdOutFacOutputPortHandleListTable = _Ieee8021StreamIdStreamIdOutFacOutputPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacOutputPortHandleListTable.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry_Object = MibTableRow
ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry = _Ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 3, 3, 1)
)
ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex_Type = Unsigned32
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex = _Ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 3, 3, 1, 1),
    _Ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex_Type()
)
ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacOutputPortHandle_Type = VariablePointer
_Ieee8021StreamIdStreamIdOutFacOutputPortHandle_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacOutputPortHandle = _Ieee8021StreamIdStreamIdOutFacOutputPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 3, 3, 1, 2),
    _Ieee8021StreamIdStreamIdOutFacOutputPortHandle_Type()
)
ieee8021StreamIdStreamIdOutFacOutputPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacOutputPortHandle.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus_Type = RowStatus
_Ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus = _Ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 3, 3, 1, 3),
    _Ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus_Type()
)
ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus.setStatus("current")
_Ieee8021StreamIdStreamIdInFacInputPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021StreamIdStreamIdInFacInputPortHandleList = _Ieee8021StreamIdStreamIdInFacInputPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 4)
)
_Ieee8021StreamIdStreamIdInFacInputPortHandleListTable_Object = MibTable
ieee8021StreamIdStreamIdInFacInputPortHandleListTable = _Ieee8021StreamIdStreamIdInFacInputPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacInputPortHandleListTable.setStatus("current")
_Ieee8021StreamIdStreamIdInFacInputPortHandleListEntry_Object = MibTableRow
ieee8021StreamIdStreamIdInFacInputPortHandleListEntry = _Ieee8021StreamIdStreamIdInFacInputPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 4, 4, 1)
)
ieee8021StreamIdStreamIdInFacInputPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacInputPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacInputPortHandleListEntry.setStatus("current")
_Ieee8021StreamIdStreamIdInFacInputPortHandleListIndex_Type = Unsigned32
_Ieee8021StreamIdStreamIdInFacInputPortHandleListIndex_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacInputPortHandleListIndex = _Ieee8021StreamIdStreamIdInFacInputPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 4, 4, 1, 1),
    _Ieee8021StreamIdStreamIdInFacInputPortHandleListIndex_Type()
)
ieee8021StreamIdStreamIdInFacInputPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacInputPortHandleListIndex.setStatus("current")
_Ieee8021StreamIdStreamIdInFacInputPortHandle_Type = VariablePointer
_Ieee8021StreamIdStreamIdInFacInputPortHandle_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacInputPortHandle = _Ieee8021StreamIdStreamIdInFacInputPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 4, 4, 1, 2),
    _Ieee8021StreamIdStreamIdInFacInputPortHandle_Type()
)
ieee8021StreamIdStreamIdInFacInputPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacInputPortHandle.setStatus("current")
_Ieee8021StreamIdStreamIdInFacInputPortHandleListStatus_Type = RowStatus
_Ieee8021StreamIdStreamIdInFacInputPortHandleListStatus_Object = MibTableColumn
ieee8021StreamIdStreamIdInFacInputPortHandleListStatus = _Ieee8021StreamIdStreamIdInFacInputPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 4, 4, 1, 3),
    _Ieee8021StreamIdStreamIdInFacInputPortHandleListStatus_Type()
)
ieee8021StreamIdStreamIdInFacInputPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdInFacInputPortHandleListStatus.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacInputPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021StreamIdStreamIdOutFacInputPortHandleList = _Ieee8021StreamIdStreamIdOutFacInputPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 5)
)
_Ieee8021StreamIdStreamIdOutFacInputPortHandleListTable_Object = MibTable
ieee8021StreamIdStreamIdOutFacInputPortHandleListTable = _Ieee8021StreamIdStreamIdOutFacInputPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacInputPortHandleListTable.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry_Object = MibTableRow
ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry = _Ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 5, 5, 1)
)
ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationIndex"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex_Type = Unsigned32
_Ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex = _Ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 5, 5, 1, 1),
    _Ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex_Type()
)
ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacInputPortHandle_Type = VariablePointer
_Ieee8021StreamIdStreamIdOutFacInputPortHandle_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacInputPortHandle = _Ieee8021StreamIdStreamIdOutFacInputPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 5, 5, 1, 2),
    _Ieee8021StreamIdStreamIdOutFacInputPortHandle_Type()
)
ieee8021StreamIdStreamIdOutFacInputPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacInputPortHandle.setStatus("current")
_Ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus_Type = RowStatus
_Ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus_Object = MibTableColumn
ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus = _Ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 5, 5, 1, 3),
    _Ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus_Type()
)
ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus.setStatus("current")
_Ieee8021StreamIdPerPortPerStreamCounters_ObjectIdentity = ObjectIdentity
ieee8021StreamIdPerPortPerStreamCounters = _Ieee8021StreamIdPerPortPerStreamCounters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 6)
)
_Ieee8021StreamIdPerPortPerStreamCountersTable_Object = MibTable
ieee8021StreamIdPerPortPerStreamCountersTable = _Ieee8021StreamIdPerPortPerStreamCountersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 6, 6)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortPerStreamCountersTable.setStatus("current")
_Ieee8021StreamIdPerPortPerStreamCountersEntry_Object = MibTableRow
ieee8021StreamIdPerPortPerStreamCountersEntry = _Ieee8021StreamIdPerPortPerStreamCountersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 6, 6, 1)
)
ieee8021StreamIdPerPortPerStreamCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdHandle"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortPerStreamDirection"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortPerStreamCountersEntry.setStatus("current")
_Ieee8021StreamIdPerPortPerStreamDirection_Type = TruthValue
_Ieee8021StreamIdPerPortPerStreamDirection_Object = MibTableColumn
ieee8021StreamIdPerPortPerStreamDirection = _Ieee8021StreamIdPerPortPerStreamDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 6, 6, 1, 1),
    _Ieee8021StreamIdPerPortPerStreamDirection_Type()
)
ieee8021StreamIdPerPortPerStreamDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortPerStreamDirection.setStatus("current")
_Ieee8021StreamIdPerPortPerStreamInputPackets_Type = Counter64
_Ieee8021StreamIdPerPortPerStreamInputPackets_Object = MibTableColumn
ieee8021StreamIdPerPortPerStreamInputPackets = _Ieee8021StreamIdPerPortPerStreamInputPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 6, 6, 1, 2),
    _Ieee8021StreamIdPerPortPerStreamInputPackets_Type()
)
ieee8021StreamIdPerPortPerStreamInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortPerStreamInputPackets.setStatus("current")
_Ieee8021StreamIdPerPortPerStreamOutputPackets_Type = Counter64
_Ieee8021StreamIdPerPortPerStreamOutputPackets_Object = MibTableColumn
ieee8021StreamIdPerPortPerStreamOutputPackets = _Ieee8021StreamIdPerPortPerStreamOutputPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 6, 6, 1, 3),
    _Ieee8021StreamIdPerPortPerStreamOutputPackets_Type()
)
ieee8021StreamIdPerPortPerStreamOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortPerStreamOutputPackets.setStatus("current")
_Ieee8021StreamIdPerPortCounters_ObjectIdentity = ObjectIdentity
ieee8021StreamIdPerPortCounters = _Ieee8021StreamIdPerPortCounters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 7)
)
_Ieee8021StreamIdPerPortCountersTable_Object = MibTable
ieee8021StreamIdPerPortCountersTable = _Ieee8021StreamIdPerPortCountersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 7, 7)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortCountersTable.setStatus("current")
_Ieee8021StreamIdPerPortCountersEntry_Object = MibTableRow
ieee8021StreamIdPerPortCountersEntry = _Ieee8021StreamIdPerPortCountersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 7, 7, 1)
)
ieee8021StreamIdPerPortCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortCountersEntry.setStatus("current")
_Ieee8021StreamIdPerPortInputPackets_Type = Counter64
_Ieee8021StreamIdPerPortInputPackets_Object = MibTableColumn
ieee8021StreamIdPerPortInputPackets = _Ieee8021StreamIdPerPortInputPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 7, 7, 1, 1),
    _Ieee8021StreamIdPerPortInputPackets_Type()
)
ieee8021StreamIdPerPortInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortInputPackets.setStatus("current")
_Ieee8021StreamIdPerPortOutputPackets_Type = Counter64
_Ieee8021StreamIdPerPortOutputPackets_Object = MibTableColumn
ieee8021StreamIdPerPortOutputPackets = _Ieee8021StreamIdPerPortOutputPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 7, 7, 1, 2),
    _Ieee8021StreamIdPerPortOutputPackets_Type()
)
ieee8021StreamIdPerPortOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortOutputPackets.setStatus("current")
_Ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLength_ObjectIdentity = ObjectIdentity
ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLength = _Ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLength_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 8)
)
_Ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthTable_Object = MibTable
ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthTable = _Ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 8, 8)
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthTable.setStatus("current")
_Ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry_Object = MibTableRow
ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry = _Ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 8, 8, 1)
)
ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry.setStatus("current")


class _Ieee8021StreamIdMaskAndMatchMsduMaskMaxLength_Type(Integer32):
    """Custom type ieee8021StreamIdMaskAndMatchMsduMaskMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1984),
    )


_Ieee8021StreamIdMaskAndMatchMsduMaskMaxLength_Type.__name__ = "Integer32"
_Ieee8021StreamIdMaskAndMatchMsduMaskMaxLength_Object = MibTableColumn
ieee8021StreamIdMaskAndMatchMsduMaskMaxLength = _Ieee8021StreamIdMaskAndMatchMsduMaskMaxLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 34, 1, 8, 8, 1, 1),
    _Ieee8021StreamIdMaskAndMatchMsduMaskMaxLength_Type()
)
ieee8021StreamIdMaskAndMatchMsduMaskMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchMsduMaskMaxLength.setStatus("current")
_Ieee8021StreamIdConformance_ObjectIdentity = ObjectIdentity
ieee8021StreamIdConformance = _Ieee8021StreamIdConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 2)
)
_Ieee8021StreamIdCompliances_ObjectIdentity = ObjectIdentity
ieee8021StreamIdCompliances = _Ieee8021StreamIdCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 1)
)
_Ieee8021StreamIdGroups_ObjectIdentity = ObjectIdentity
ieee8021StreamIdGroups = _Ieee8021StreamIdGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2)
)

# Managed Objects groups

ieee8021StreamIdStreamIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 1)
)
ieee8021StreamIdStreamIdentificationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdIdentificationTypeSelect"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdIdentificationType"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdIdentificationTypeOUI"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdIdentificationCustomType"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdIdentificationCustomTypeOUI"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdHandle"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacOutputPortList"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacOutputPortList"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacInputPortList"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacInputPortList"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacOutputPortHandle"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacOutputPortHandle"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacInputPortHandle"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdInFacInputPortHandleListStatus"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacInputPortHandle"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdStreamIdentificationGroup.setStatus("current")

ieee8021StreamIdNullStreamIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 2)
)
ieee8021StreamIdNullStreamIdentificationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeNullDownDestMac"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCPENullDownTagged"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeNullDownVlan"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdNullStreamIdentificationGroup.setStatus("current")

ieee8021StreamIdSrcMacVlanIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 3)
)
ieee8021StreamIdSrcMacVlanIdentificationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeSmacVlanDownSrcMac"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeSmacVlanDownTagged"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeSmacVlanDownVlan"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdSrcMacVlanIdentificationGroup.setStatus("current")

ieee8021StreamIdActiveDestMacVlanIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 4)
)
ieee8021StreamIdActiveDestMacVlanIdentificationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanDownDestMac"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanDownTagged"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanDownVlan"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanDownPriority"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanUpDestMac"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanUpTagged"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanUpVlan"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeDmacVlanUpPriority"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdActiveDestMacVlanIdentificationGroup.setStatus("current")

ieee8021StreamIdIpStreamIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 5)
)
ieee8021StreamIdIpStreamIdentificationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdDestMac"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdTagged"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdVlan"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdIpSourceType"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdIpSource"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdIpDestinationType"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdIpDestination"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdDscp"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdNextProtocol"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdSourcePort"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeIpIdDestinationPort"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdIpStreamIdentificationGroup.setStatus("current")

ieee8021StreamIdAutoConfigurationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 6)
)
ieee8021StreamIdAutoConfigurationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdAutoConfigured"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdLanPathId"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStatus"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdAutoConfigurationGroup.setStatus("current")

ieee8021StreamIdPerPortPerStreamCountersGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 7)
)
ieee8021StreamIdPerPortPerStreamCountersGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortPerStreamInputPackets"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortPerStreamOutputPackets"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortPerStreamCountersGroup.setStatus("current")

ieee8021StreamIdPerPortCountersGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 8)
)
ieee8021StreamIdPerPortCountersGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortInputPackets"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortOutputPackets"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdPerPortCountersGroup.setStatus("current")

ieee8021StreamIdMaskAndMatchIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 9)
)
ieee8021StreamIdMaskAndMatchIdentificationGroup.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdDestMacMask"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdDestMacMatch"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdSrcMacMask"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdSrcMacMatch"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdMsduMaskLength"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdMsduMask"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdCpeMmIdMsduMatch"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchIdentificationGroup.setStatus("current")

ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 2, 10)
)
ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthGroup.setObjects(
    ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdMaskAndMatchMsduMaskMaxLength")
)
if mibBuilder.loadTexts:
    ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021StreamIdCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 34, 2, 1, 1)
)
ieee8021StreamIdCompliance.setObjects(
      *(("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdentificationGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdNullStreamIdentificationGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdSrcMacVlanIdentificationGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdActiveDestMacVlanIdentificationGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdIpStreamIdentificationGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortPerStreamCountersGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdPerPortCountersGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdMaskAndMatchIdentificationGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthGroup"),
        ("IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdAutoConfigurationGroup"))
)
if mibBuilder.loadTexts:
    ieee8021StreamIdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-STREAM-IDENTIFICATION-MIB",
    **{"Ieee8021CBStreamIdentificationType": Ieee8021CBStreamIdentificationType,
       "Ieee8021CBTaggedType": Ieee8021CBTaggedType,
       "Ieee8021CBVlanIdentifier": Ieee8021CBVlanIdentifier,
       "Ieee8021CBIpDscpType": Ieee8021CBIpDscpType,
       "Ieee8021CBIdNextProtocolType": Ieee8021CBIdNextProtocolType,
       "Ieee8021CBLanPathIdType": Ieee8021CBLanPathIdType,
       "ieee8021StreamIdMib": ieee8021StreamIdMib,
       "ieee8021StreamIdNotifications": ieee8021StreamIdNotifications,
       "ieee8021StreamIdObjects": ieee8021StreamIdObjects,
       "ieee8021StreamIdStreamIdentification": ieee8021StreamIdStreamIdentification,
       "ieee8021StreamIdStreamIdentificationTypes": ieee8021StreamIdStreamIdentificationTypes,
       "ieee8021StreamIdNullStream": ieee8021StreamIdNullStream,
       "ieee8021StreamIdSrcMacVlan": ieee8021StreamIdSrcMacVlan,
       "ieee8021StreamIdActiveDestMacVlan": ieee8021StreamIdActiveDestMacVlan,
       "ieee8021StreamIdIpStream": ieee8021StreamIdIpStream,
       "ieee8021StreamIdMaskAndMatch": ieee8021StreamIdMaskAndMatch,
       "ieee8021StreamIdStreamIdentificationTable": ieee8021StreamIdStreamIdentificationTable,
       "ieee8021StreamIdStreamIdentificationEntry": ieee8021StreamIdStreamIdentificationEntry,
       "ieee8021StreamIdStreamIdentificationIndex": ieee8021StreamIdStreamIdentificationIndex,
       "ieee8021StreamIdStreamIdIdentificationType": ieee8021StreamIdStreamIdIdentificationType,
       "ieee8021StreamIdStreamIdIdentificationTypeOUI": ieee8021StreamIdStreamIdIdentificationTypeOUI,
       "ieee8021StreamIdStreamIdIdentificationCustomType": ieee8021StreamIdStreamIdIdentificationCustomType,
       "ieee8021StreamIdStreamIdIdentificationCustomTypeOUI": ieee8021StreamIdStreamIdIdentificationCustomTypeOUI,
       "ieee8021StreamIdStreamIdIdentificationTypeSelect": ieee8021StreamIdStreamIdIdentificationTypeSelect,
       "ieee8021StreamIdStreamIdHandle": ieee8021StreamIdStreamIdHandle,
       "ieee8021StreamIdStreamIdInFacOutputPortList": ieee8021StreamIdStreamIdInFacOutputPortList,
       "ieee8021StreamIdStreamIdOutFacOutputPortList": ieee8021StreamIdStreamIdOutFacOutputPortList,
       "ieee8021StreamIdStreamIdInFacInputPortList": ieee8021StreamIdStreamIdInFacInputPortList,
       "ieee8021StreamIdStreamIdOutFacInputPortList": ieee8021StreamIdStreamIdOutFacInputPortList,
       "ieee8021StreamIdAutoConfigured": ieee8021StreamIdAutoConfigured,
       "ieee8021StreamIdLanPathId": ieee8021StreamIdLanPathId,
       "ieee8021StreamIdStatus": ieee8021StreamIdStatus,
       "ieee8021StreamIdNullStreamIdentificationTable": ieee8021StreamIdNullStreamIdentificationTable,
       "ieee8021StreamIdNullStreamIdentificationEntry": ieee8021StreamIdNullStreamIdentificationEntry,
       "ieee8021StreamIdCpeNullDownDestMac": ieee8021StreamIdCpeNullDownDestMac,
       "ieee8021StreamIdCPENullDownTagged": ieee8021StreamIdCPENullDownTagged,
       "ieee8021StreamIdCpeNullDownVlan": ieee8021StreamIdCpeNullDownVlan,
       "ieee8021StreamIdSrcMacVlanIdentificationTable": ieee8021StreamIdSrcMacVlanIdentificationTable,
       "ieee8021StreamIdSrcMacVlanIdentificationEntry": ieee8021StreamIdSrcMacVlanIdentificationEntry,
       "ieee8021StreamIdCpeSmacVlanDownSrcMac": ieee8021StreamIdCpeSmacVlanDownSrcMac,
       "ieee8021StreamIdCpeSmacVlanDownTagged": ieee8021StreamIdCpeSmacVlanDownTagged,
       "ieee8021StreamIdCpeSmacVlanDownVlan": ieee8021StreamIdCpeSmacVlanDownVlan,
       "ieee8021StreamIdActiveDestMacVlanIdentificationTable": ieee8021StreamIdActiveDestMacVlanIdentificationTable,
       "ieee8021StreamIdActiveDestMacVlanIdentificationEntry": ieee8021StreamIdActiveDestMacVlanIdentificationEntry,
       "ieee8021StreamIdCpeDmacVlanDownDestMac": ieee8021StreamIdCpeDmacVlanDownDestMac,
       "ieee8021StreamIdCpeDmacVlanDownTagged": ieee8021StreamIdCpeDmacVlanDownTagged,
       "ieee8021StreamIdCpeDmacVlanDownVlan": ieee8021StreamIdCpeDmacVlanDownVlan,
       "ieee8021StreamIdCpeDmacVlanDownPriority": ieee8021StreamIdCpeDmacVlanDownPriority,
       "ieee8021StreamIdCpeDmacVlanUpDestMac": ieee8021StreamIdCpeDmacVlanUpDestMac,
       "ieee8021StreamIdCpeDmacVlanUpTagged": ieee8021StreamIdCpeDmacVlanUpTagged,
       "ieee8021StreamIdCpeDmacVlanUpVlan": ieee8021StreamIdCpeDmacVlanUpVlan,
       "ieee8021StreamIdCpeDmacVlanUpPriority": ieee8021StreamIdCpeDmacVlanUpPriority,
       "ieee8021StreamIdIpStreamIdentificationTable": ieee8021StreamIdIpStreamIdentificationTable,
       "ieee8021StreamIdIpStreamIdentificationEntry": ieee8021StreamIdIpStreamIdentificationEntry,
       "ieee8021StreamIdCpeIpIdDestMac": ieee8021StreamIdCpeIpIdDestMac,
       "ieee8021StreamIdCpeIpIdTagged": ieee8021StreamIdCpeIpIdTagged,
       "ieee8021StreamIdCpeIpIdVlan": ieee8021StreamIdCpeIpIdVlan,
       "ieee8021StreamIdCpeIpIdIpSourceType": ieee8021StreamIdCpeIpIdIpSourceType,
       "ieee8021StreamIdCpeIpIdIpSource": ieee8021StreamIdCpeIpIdIpSource,
       "ieee8021StreamIdCpeIpIdIpDestinationType": ieee8021StreamIdCpeIpIdIpDestinationType,
       "ieee8021StreamIdCpeIpIdIpDestination": ieee8021StreamIdCpeIpIdIpDestination,
       "ieee8021StreamIdCpeIpIdDscp": ieee8021StreamIdCpeIpIdDscp,
       "ieee8021StreamIdCpeIpIdNextProtocol": ieee8021StreamIdCpeIpIdNextProtocol,
       "ieee8021StreamIdCpeIpIdSourcePort": ieee8021StreamIdCpeIpIdSourcePort,
       "ieee8021StreamIdCpeIpIdDestinationPort": ieee8021StreamIdCpeIpIdDestinationPort,
       "ieee8021StreamIdMaskAndMatchIdentificationTable": ieee8021StreamIdMaskAndMatchIdentificationTable,
       "ieee8021StreamIdMaskAndMatchIdentificationEntry": ieee8021StreamIdMaskAndMatchIdentificationEntry,
       "ieee8021StreamIdCpeMmIdDestMacMask": ieee8021StreamIdCpeMmIdDestMacMask,
       "ieee8021StreamIdCpeMmIdDestMacMatch": ieee8021StreamIdCpeMmIdDestMacMatch,
       "ieee8021StreamIdCpeMmIdSrcMacMask": ieee8021StreamIdCpeMmIdSrcMacMask,
       "ieee8021StreamIdCpeMmIdSrcMacMatch": ieee8021StreamIdCpeMmIdSrcMacMatch,
       "ieee8021StreamIdCpeMmIdMsduMaskLength": ieee8021StreamIdCpeMmIdMsduMaskLength,
       "ieee8021StreamIdCpeMmIdMsduMask": ieee8021StreamIdCpeMmIdMsduMask,
       "ieee8021StreamIdCpeMmIdMsduMatch": ieee8021StreamIdCpeMmIdMsduMatch,
       "ieee8021StreamIdStreamIdInFacOutputPortHandleList": ieee8021StreamIdStreamIdInFacOutputPortHandleList,
       "ieee8021StreamIdStreamIdInFacOutputPortHandleListTable": ieee8021StreamIdStreamIdInFacOutputPortHandleListTable,
       "ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry": ieee8021StreamIdStreamIdInFacOutputPortHandleListEntry,
       "ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex": ieee8021StreamIdStreamIdInFacOutputPortHandleListIndex,
       "ieee8021StreamIdStreamIdInFacOutputPortHandle": ieee8021StreamIdStreamIdInFacOutputPortHandle,
       "ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus": ieee8021StreamIdStreamIdInFacOutputPortHandleListStatus,
       "ieee8021StreamIdStreamIdOutFacOutputPortHandleList": ieee8021StreamIdStreamIdOutFacOutputPortHandleList,
       "ieee8021StreamIdStreamIdOutFacOutputPortHandleListTable": ieee8021StreamIdStreamIdOutFacOutputPortHandleListTable,
       "ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry": ieee8021StreamIdStreamIdOutFacOutputPortHandleListEntry,
       "ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex": ieee8021StreamIdStreamIdOutFacOutputPortHandleListIndex,
       "ieee8021StreamIdStreamIdOutFacOutputPortHandle": ieee8021StreamIdStreamIdOutFacOutputPortHandle,
       "ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus": ieee8021StreamIdStreamIdOutFacOutputPortHandleListStatus,
       "ieee8021StreamIdStreamIdInFacInputPortHandleList": ieee8021StreamIdStreamIdInFacInputPortHandleList,
       "ieee8021StreamIdStreamIdInFacInputPortHandleListTable": ieee8021StreamIdStreamIdInFacInputPortHandleListTable,
       "ieee8021StreamIdStreamIdInFacInputPortHandleListEntry": ieee8021StreamIdStreamIdInFacInputPortHandleListEntry,
       "ieee8021StreamIdStreamIdInFacInputPortHandleListIndex": ieee8021StreamIdStreamIdInFacInputPortHandleListIndex,
       "ieee8021StreamIdStreamIdInFacInputPortHandle": ieee8021StreamIdStreamIdInFacInputPortHandle,
       "ieee8021StreamIdStreamIdInFacInputPortHandleListStatus": ieee8021StreamIdStreamIdInFacInputPortHandleListStatus,
       "ieee8021StreamIdStreamIdOutFacInputPortHandleList": ieee8021StreamIdStreamIdOutFacInputPortHandleList,
       "ieee8021StreamIdStreamIdOutFacInputPortHandleListTable": ieee8021StreamIdStreamIdOutFacInputPortHandleListTable,
       "ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry": ieee8021StreamIdStreamIdOutFacInputPortHandleListEntry,
       "ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex": ieee8021StreamIdStreamIdOutFacInputPortHandleListIndex,
       "ieee8021StreamIdStreamIdOutFacInputPortHandle": ieee8021StreamIdStreamIdOutFacInputPortHandle,
       "ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus": ieee8021StreamIdStreamIdOutFacInputPortHandleListStatus,
       "ieee8021StreamIdPerPortPerStreamCounters": ieee8021StreamIdPerPortPerStreamCounters,
       "ieee8021StreamIdPerPortPerStreamCountersTable": ieee8021StreamIdPerPortPerStreamCountersTable,
       "ieee8021StreamIdPerPortPerStreamCountersEntry": ieee8021StreamIdPerPortPerStreamCountersEntry,
       "ieee8021StreamIdPerPortPerStreamDirection": ieee8021StreamIdPerPortPerStreamDirection,
       "ieee8021StreamIdPerPortPerStreamInputPackets": ieee8021StreamIdPerPortPerStreamInputPackets,
       "ieee8021StreamIdPerPortPerStreamOutputPackets": ieee8021StreamIdPerPortPerStreamOutputPackets,
       "ieee8021StreamIdPerPortCounters": ieee8021StreamIdPerPortCounters,
       "ieee8021StreamIdPerPortCountersTable": ieee8021StreamIdPerPortCountersTable,
       "ieee8021StreamIdPerPortCountersEntry": ieee8021StreamIdPerPortCountersEntry,
       "ieee8021StreamIdPerPortInputPackets": ieee8021StreamIdPerPortInputPackets,
       "ieee8021StreamIdPerPortOutputPackets": ieee8021StreamIdPerPortOutputPackets,
       "ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLength": ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLength,
       "ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthTable": ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthTable,
       "ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry": ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthEntry,
       "ieee8021StreamIdMaskAndMatchMsduMaskMaxLength": ieee8021StreamIdMaskAndMatchMsduMaskMaxLength,
       "ieee8021StreamIdConformance": ieee8021StreamIdConformance,
       "ieee8021StreamIdCompliances": ieee8021StreamIdCompliances,
       "ieee8021StreamIdCompliance": ieee8021StreamIdCompliance,
       "ieee8021StreamIdGroups": ieee8021StreamIdGroups,
       "ieee8021StreamIdStreamIdentificationGroup": ieee8021StreamIdStreamIdentificationGroup,
       "ieee8021StreamIdNullStreamIdentificationGroup": ieee8021StreamIdNullStreamIdentificationGroup,
       "ieee8021StreamIdSrcMacVlanIdentificationGroup": ieee8021StreamIdSrcMacVlanIdentificationGroup,
       "ieee8021StreamIdActiveDestMacVlanIdentificationGroup": ieee8021StreamIdActiveDestMacVlanIdentificationGroup,
       "ieee8021StreamIdIpStreamIdentificationGroup": ieee8021StreamIdIpStreamIdentificationGroup,
       "ieee8021StreamIdAutoConfigurationGroup": ieee8021StreamIdAutoConfigurationGroup,
       "ieee8021StreamIdPerPortPerStreamCountersGroup": ieee8021StreamIdPerPortPerStreamCountersGroup,
       "ieee8021StreamIdPerPortCountersGroup": ieee8021StreamIdPerPortCountersGroup,
       "ieee8021StreamIdMaskAndMatchIdentificationGroup": ieee8021StreamIdMaskAndMatchIdentificationGroup,
       "ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthGroup": ieee8021StreamIdMaskAndMatchPerPortMsduMaskMaxLengthGroup}
)
