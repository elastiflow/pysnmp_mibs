# SNMP MIB module (CIE1000-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-LLDP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000DisplayString,
 CIE1000Integer64,
 CIE1000InterfaceIndex,
 CIE1000RowEditorState,
 CIE1000Unsigned16,
 CIE1000Unsigned64,
 CIE1000Unsigned8) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000Integer64",
    "CIE1000InterfaceIndex",
    "CIE1000RowEditorState",
    "CIE1000Unsigned16",
    "CIE1000Unsigned64",
    "CIE1000Unsigned8")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000LldpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34)
)
if mibBuilder.loadTexts:
    cie1000LldpMib.setRevisions(
        ("2016-04-07 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000lldpAdminState(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("txAndRx", 1),
          ("txOnly", 2),
          ("rxOnly", 3))
    )



class CIE1000lldpmedAltitudeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meters", 1),
          ("floors", 2))
    )



class CIE1000lldpmedCivicAddressType(TextualConvention, Integer32):
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("state", 1),
          ("county", 2),
          ("city", 3),
          ("district", 4),
          ("block", 5),
          ("street", 6),
          ("leadingStreetDirection", 16),
          ("trailingStreetSuffix", 17),
          ("streetSuffix", 18),
          ("houseNo", 19),
          ("houseNoSuffix", 20),
          ("landmark", 21),
          ("additionalInfo", 22),
          ("name", 23),
          ("zipCode", 24),
          ("building", 25),
          ("apartment", 26),
          ("floor", 27),
          ("roomNumber", 28),
          ("placeType", 29),
          ("postalCommunityName", 30),
          ("poBox", 31),
          ("additionalCode", 32))
    )



class CIE1000lldpmedDatumType(TextualConvention, Integer32):
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
        *(("wgs84", 1),
          ("nad83navd88", 2),
          ("nad83mllw", 3))
    )



class CIE1000lldpmedDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 0),
          ("endpoint", 1))
    )



class CIE1000lldpmedRemoteDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("endpointClassI", 1),
          ("endpointClassII", 2),
          ("endpointClassIII", 3),
          ("networkConnectivity", 4),
          ("reserved", 5))
    )



class CIE1000lldpmedRemoteNetworkPolicyApplicationType(TextualConvention, Integer32):
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
        *(("voice", 1),
          ("voiceSignaling", 2),
          ("guestVoice", 3),
          ("guestVoiceSignaling", 4),
          ("softphoneVoice", 5),
          ("videoConferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000LldpMibObjects_ObjectIdentity = ObjectIdentity
cie1000LldpMibObjects = _Cie1000LldpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1)
)
_Cie1000LldpConfig_ObjectIdentity = ObjectIdentity
cie1000LldpConfig = _Cie1000LldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2)
)
_Cie1000LldpConfigGlobal_ObjectIdentity = ObjectIdentity
cie1000LldpConfigGlobal = _Cie1000LldpConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 1)
)
_Cie1000LldpConfigGlobalReInitDelay_Type = CIE1000Unsigned16
_Cie1000LldpConfigGlobalReInitDelay_Object = MibScalar
cie1000LldpConfigGlobalReInitDelay = _Cie1000LldpConfigGlobalReInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 1, 1),
    _Cie1000LldpConfigGlobalReInitDelay_Type()
)
cie1000LldpConfigGlobalReInitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigGlobalReInitDelay.setStatus("current")
_Cie1000LldpConfigGlobalMsgTxHold_Type = CIE1000Unsigned16
_Cie1000LldpConfigGlobalMsgTxHold_Object = MibScalar
cie1000LldpConfigGlobalMsgTxHold = _Cie1000LldpConfigGlobalMsgTxHold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 1, 2),
    _Cie1000LldpConfigGlobalMsgTxHold_Type()
)
cie1000LldpConfigGlobalMsgTxHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigGlobalMsgTxHold.setStatus("current")
_Cie1000LldpConfigGlobalMsgTxInterval_Type = CIE1000Unsigned16
_Cie1000LldpConfigGlobalMsgTxInterval_Object = MibScalar
cie1000LldpConfigGlobalMsgTxInterval = _Cie1000LldpConfigGlobalMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 1, 3),
    _Cie1000LldpConfigGlobalMsgTxInterval_Type()
)
cie1000LldpConfigGlobalMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigGlobalMsgTxInterval.setStatus("current")
_Cie1000LldpConfigGlobalTxDelay_Type = CIE1000Unsigned16
_Cie1000LldpConfigGlobalTxDelay_Object = MibScalar
cie1000LldpConfigGlobalTxDelay = _Cie1000LldpConfigGlobalTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 1, 4),
    _Cie1000LldpConfigGlobalTxDelay_Type()
)
cie1000LldpConfigGlobalTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigGlobalTxDelay.setStatus("current")
_Cie1000LldpConfigTable_Object = MibTable
cie1000LldpConfigTable = _Cie1000LldpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000LldpConfigTable.setStatus("current")
_Cie1000LldpConfigEntry_Object = MibTableRow
cie1000LldpConfigEntry = _Cie1000LldpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2, 1)
)
cie1000LldpConfigEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpConfigIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpConfigEntry.setStatus("current")
_Cie1000LldpConfigIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpConfigIfIndex_Object = MibTableColumn
cie1000LldpConfigIfIndex = _Cie1000LldpConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2, 1, 1),
    _Cie1000LldpConfigIfIndex_Type()
)
cie1000LldpConfigIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpConfigIfIndex.setStatus("current")
_Cie1000LldpConfigAdminState_Type = CIE1000lldpAdminState
_Cie1000LldpConfigAdminState_Object = MibTableColumn
cie1000LldpConfigAdminState = _Cie1000LldpConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2, 1, 3),
    _Cie1000LldpConfigAdminState_Type()
)
cie1000LldpConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigAdminState.setStatus("current")
_Cie1000LldpConfigCdpAware_Type = TruthValue
_Cie1000LldpConfigCdpAware_Object = MibTableColumn
cie1000LldpConfigCdpAware = _Cie1000LldpConfigCdpAware_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2, 1, 4),
    _Cie1000LldpConfigCdpAware_Type()
)
cie1000LldpConfigCdpAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigCdpAware.setStatus("current")
_Cie1000LldpConfigOptionalTlvs_Type = CIE1000Unsigned8
_Cie1000LldpConfigOptionalTlvs_Object = MibTableColumn
cie1000LldpConfigOptionalTlvs = _Cie1000LldpConfigOptionalTlvs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2, 1, 5),
    _Cie1000LldpConfigOptionalTlvs_Type()
)
cie1000LldpConfigOptionalTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigOptionalTlvs.setStatus("current")
_Cie1000LldpConfigSnmpNotificationEna_Type = TruthValue
_Cie1000LldpConfigSnmpNotificationEna_Object = MibTableColumn
cie1000LldpConfigSnmpNotificationEna = _Cie1000LldpConfigSnmpNotificationEna_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 2, 1, 6),
    _Cie1000LldpConfigSnmpNotificationEna_Type()
)
cie1000LldpConfigSnmpNotificationEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigSnmpNotificationEna.setStatus("current")
_Cie1000LldpConfigMed_ObjectIdentity = ObjectIdentity
cie1000LldpConfigMed = _Cie1000LldpConfigMed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3)
)
_Cie1000LldpConfigMedTable_Object = MibTable
cie1000LldpConfigMedTable = _Cie1000LldpConfigMedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedTable.setStatus("current")
_Cie1000LldpConfigMedEntry_Object = MibTableRow
cie1000LldpConfigMedEntry = _Cie1000LldpConfigMedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 1, 1)
)
cie1000LldpConfigMedEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpConfigMedIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedEntry.setStatus("current")
_Cie1000LldpConfigMedIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpConfigMedIfIndex_Object = MibTableColumn
cie1000LldpConfigMedIfIndex = _Cie1000LldpConfigMedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 1, 1, 1),
    _Cie1000LldpConfigMedIfIndex_Type()
)
cie1000LldpConfigMedIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedIfIndex.setStatus("current")
_Cie1000LldpConfigMedOptionalTlvs_Type = CIE1000Unsigned8
_Cie1000LldpConfigMedOptionalTlvs_Object = MibTableColumn
cie1000LldpConfigMedOptionalTlvs = _Cie1000LldpConfigMedOptionalTlvs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 1, 1, 3),
    _Cie1000LldpConfigMedOptionalTlvs_Type()
)
cie1000LldpConfigMedOptionalTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedOptionalTlvs.setStatus("current")
_Cie1000LldpConfigMedDeviceType_Type = CIE1000lldpmedDeviceType
_Cie1000LldpConfigMedDeviceType_Object = MibTableColumn
cie1000LldpConfigMedDeviceType = _Cie1000LldpConfigMedDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 1, 1, 4),
    _Cie1000LldpConfigMedDeviceType_Type()
)
cie1000LldpConfigMedDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedDeviceType.setStatus("current")
_Cie1000LldpConfigMedPolicyTable_Object = MibTable
cie1000LldpConfigMedPolicyTable = _Cie1000LldpConfigMedPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyTable.setStatus("current")
_Cie1000LldpConfigMedPolicyEntry_Object = MibTableRow
cie1000LldpConfigMedPolicyEntry = _Cie1000LldpConfigMedPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1)
)
cie1000LldpConfigMedPolicyEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyEntry.setStatus("current")


class _Cie1000LldpConfigMedPolicyLldpmedPolicy_Type(Integer32):
    """Custom type cie1000LldpConfigMedPolicyLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cie1000LldpConfigMedPolicyLldpmedPolicy_Type.__name__ = "Integer32"
_Cie1000LldpConfigMedPolicyLldpmedPolicy_Object = MibTableColumn
cie1000LldpConfigMedPolicyLldpmedPolicy = _Cie1000LldpConfigMedPolicyLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 1),
    _Cie1000LldpConfigMedPolicyLldpmedPolicy_Type()
)
cie1000LldpConfigMedPolicyLldpmedPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyLldpmedPolicy.setStatus("current")
_Cie1000LldpConfigMedPolicyApplicationType_Type = CIE1000lldpmedRemoteNetworkPolicyApplicationType
_Cie1000LldpConfigMedPolicyApplicationType_Object = MibTableColumn
cie1000LldpConfigMedPolicyApplicationType = _Cie1000LldpConfigMedPolicyApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 3),
    _Cie1000LldpConfigMedPolicyApplicationType_Type()
)
cie1000LldpConfigMedPolicyApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyApplicationType.setStatus("current")
_Cie1000LldpConfigMedPolicyTagged_Type = TruthValue
_Cie1000LldpConfigMedPolicyTagged_Object = MibTableColumn
cie1000LldpConfigMedPolicyTagged = _Cie1000LldpConfigMedPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 4),
    _Cie1000LldpConfigMedPolicyTagged_Type()
)
cie1000LldpConfigMedPolicyTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyTagged.setStatus("current")


class _Cie1000LldpConfigMedPolicyVlanId_Type(CIE1000Unsigned16):
    """Custom type cie1000LldpConfigMedPolicyVlanId based on CIE1000Unsigned16"""
    subtypeSpec = CIE1000Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cie1000LldpConfigMedPolicyVlanId_Type.__name__ = "CIE1000Unsigned16"
_Cie1000LldpConfigMedPolicyVlanId_Object = MibTableColumn
cie1000LldpConfigMedPolicyVlanId = _Cie1000LldpConfigMedPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 5),
    _Cie1000LldpConfigMedPolicyVlanId_Type()
)
cie1000LldpConfigMedPolicyVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyVlanId.setStatus("current")


class _Cie1000LldpConfigMedPolicyL2Priority_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpConfigMedPolicyL2Priority based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000LldpConfigMedPolicyL2Priority_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpConfigMedPolicyL2Priority_Object = MibTableColumn
cie1000LldpConfigMedPolicyL2Priority = _Cie1000LldpConfigMedPolicyL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 6),
    _Cie1000LldpConfigMedPolicyL2Priority_Type()
)
cie1000LldpConfigMedPolicyL2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyL2Priority.setStatus("current")


class _Cie1000LldpConfigMedPolicyDscp_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpConfigMedPolicyDscp based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cie1000LldpConfigMedPolicyDscp_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpConfigMedPolicyDscp_Object = MibTableColumn
cie1000LldpConfigMedPolicyDscp = _Cie1000LldpConfigMedPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 7),
    _Cie1000LldpConfigMedPolicyDscp_Type()
)
cie1000LldpConfigMedPolicyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyDscp.setStatus("current")
_Cie1000LldpConfigMedPolicyAction_Type = CIE1000RowEditorState
_Cie1000LldpConfigMedPolicyAction_Object = MibTableColumn
cie1000LldpConfigMedPolicyAction = _Cie1000LldpConfigMedPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 2, 1, 100),
    _Cie1000LldpConfigMedPolicyAction_Type()
)
cie1000LldpConfigMedPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyAction.setStatus("current")
_Cie1000LldpConfigMedPolicyListTable_Object = MibTable
cie1000LldpConfigMedPolicyListTable = _Cie1000LldpConfigMedPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyListTable.setStatus("current")
_Cie1000LldpConfigMedPolicyListEntry_Object = MibTableRow
cie1000LldpConfigMedPolicyListEntry = _Cie1000LldpConfigMedPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 3, 1)
)
cie1000LldpConfigMedPolicyListEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyListIfIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyListLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyListEntry.setStatus("current")
_Cie1000LldpConfigMedPolicyListIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpConfigMedPolicyListIfIndex_Object = MibTableColumn
cie1000LldpConfigMedPolicyListIfIndex = _Cie1000LldpConfigMedPolicyListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 3, 1, 1),
    _Cie1000LldpConfigMedPolicyListIfIndex_Type()
)
cie1000LldpConfigMedPolicyListIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyListIfIndex.setStatus("current")


class _Cie1000LldpConfigMedPolicyListLldpmedPolicy_Type(Integer32):
    """Custom type cie1000LldpConfigMedPolicyListLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cie1000LldpConfigMedPolicyListLldpmedPolicy_Type.__name__ = "Integer32"
_Cie1000LldpConfigMedPolicyListLldpmedPolicy_Object = MibTableColumn
cie1000LldpConfigMedPolicyListLldpmedPolicy = _Cie1000LldpConfigMedPolicyListLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 3, 1, 3),
    _Cie1000LldpConfigMedPolicyListLldpmedPolicy_Type()
)
cie1000LldpConfigMedPolicyListLldpmedPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyListLldpmedPolicy.setStatus("current")
_Cie1000LldpConfigMedPolicyListLldpmedPoliciesList_Type = TruthValue
_Cie1000LldpConfigMedPolicyListLldpmedPoliciesList_Object = MibTableColumn
cie1000LldpConfigMedPolicyListLldpmedPoliciesList = _Cie1000LldpConfigMedPolicyListLldpmedPoliciesList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 3, 1, 4),
    _Cie1000LldpConfigMedPolicyListLldpmedPoliciesList_Type()
)
cie1000LldpConfigMedPolicyListLldpmedPoliciesList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyListLldpmedPoliciesList.setStatus("current")
_Cie1000LldpConfigMedGlobal_ObjectIdentity = ObjectIdentity
cie1000LldpConfigMedGlobal = _Cie1000LldpConfigMedGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4)
)


class _Cie1000LldpConfigMedGlobalFastRepeatCount_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpConfigMedGlobalFastRepeatCount based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Cie1000LldpConfigMedGlobalFastRepeatCount_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpConfigMedGlobalFastRepeatCount_Object = MibScalar
cie1000LldpConfigMedGlobalFastRepeatCount = _Cie1000LldpConfigMedGlobalFastRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 1),
    _Cie1000LldpConfigMedGlobalFastRepeatCount_Type()
)
cie1000LldpConfigMedGlobalFastRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalFastRepeatCount.setStatus("current")
_Cie1000LldpConfigMedGlobalLatitude_Type = CIE1000Integer64
_Cie1000LldpConfigMedGlobalLatitude_Object = MibScalar
cie1000LldpConfigMedGlobalLatitude = _Cie1000LldpConfigMedGlobalLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 2),
    _Cie1000LldpConfigMedGlobalLatitude_Type()
)
cie1000LldpConfigMedGlobalLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalLatitude.setStatus("current")
_Cie1000LldpConfigMedGlobalLongitude_Type = CIE1000Integer64
_Cie1000LldpConfigMedGlobalLongitude_Object = MibScalar
cie1000LldpConfigMedGlobalLongitude = _Cie1000LldpConfigMedGlobalLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 3),
    _Cie1000LldpConfigMedGlobalLongitude_Type()
)
cie1000LldpConfigMedGlobalLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalLongitude.setStatus("current")
_Cie1000LldpConfigMedGlobalAltitudeType_Type = CIE1000lldpmedAltitudeType
_Cie1000LldpConfigMedGlobalAltitudeType_Object = MibScalar
cie1000LldpConfigMedGlobalAltitudeType = _Cie1000LldpConfigMedGlobalAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 4),
    _Cie1000LldpConfigMedGlobalAltitudeType_Type()
)
cie1000LldpConfigMedGlobalAltitudeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalAltitudeType.setStatus("current")
_Cie1000LldpConfigMedGlobalAltitude_Type = Integer32
_Cie1000LldpConfigMedGlobalAltitude_Object = MibScalar
cie1000LldpConfigMedGlobalAltitude = _Cie1000LldpConfigMedGlobalAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 5),
    _Cie1000LldpConfigMedGlobalAltitude_Type()
)
cie1000LldpConfigMedGlobalAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalAltitude.setStatus("current")


class _Cie1000LldpConfigMedGlobalElinAddr_Type(CIE1000DisplayString):
    """Custom type cie1000LldpConfigMedGlobalElinAddr based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Cie1000LldpConfigMedGlobalElinAddr_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpConfigMedGlobalElinAddr_Object = MibScalar
cie1000LldpConfigMedGlobalElinAddr = _Cie1000LldpConfigMedGlobalElinAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 6),
    _Cie1000LldpConfigMedGlobalElinAddr_Type()
)
cie1000LldpConfigMedGlobalElinAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalElinAddr.setStatus("current")
_Cie1000LldpConfigMedGlobalDatum_Type = CIE1000lldpmedDatumType
_Cie1000LldpConfigMedGlobalDatum_Object = MibScalar
cie1000LldpConfigMedGlobalDatum = _Cie1000LldpConfigMedGlobalDatum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 7),
    _Cie1000LldpConfigMedGlobalDatum_Type()
)
cie1000LldpConfigMedGlobalDatum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalDatum.setStatus("current")


class _Cie1000LldpConfigMedGlobalCountryCode_Type(CIE1000DisplayString):
    """Custom type cie1000LldpConfigMedGlobalCountryCode based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cie1000LldpConfigMedGlobalCountryCode_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpConfigMedGlobalCountryCode_Object = MibScalar
cie1000LldpConfigMedGlobalCountryCode = _Cie1000LldpConfigMedGlobalCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 4, 8),
    _Cie1000LldpConfigMedGlobalCountryCode_Type()
)
cie1000LldpConfigMedGlobalCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalCountryCode.setStatus("current")
_Cie1000LldpConfigMedLocationInfTable_Object = MibTable
cie1000LldpConfigMedLocationInfTable = _Cie1000LldpConfigMedLocationInfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedLocationInfTable.setStatus("current")
_Cie1000LldpConfigMedLocationInfEntry_Object = MibTableRow
cie1000LldpConfigMedLocationInfEntry = _Cie1000LldpConfigMedLocationInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 5, 1)
)
cie1000LldpConfigMedLocationInfEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpConfigMedLocationInfLldpmedIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedLocationInfEntry.setStatus("current")
_Cie1000LldpConfigMedLocationInfLldpmedIndex_Type = CIE1000lldpmedCivicAddressType
_Cie1000LldpConfigMedLocationInfLldpmedIndex_Object = MibTableColumn
cie1000LldpConfigMedLocationInfLldpmedIndex = _Cie1000LldpConfigMedLocationInfLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 5, 1, 2),
    _Cie1000LldpConfigMedLocationInfLldpmedIndex_Type()
)
cie1000LldpConfigMedLocationInfLldpmedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedLocationInfLldpmedIndex.setStatus("current")


class _Cie1000LldpConfigMedLocationInfCivicAddress_Type(CIE1000DisplayString):
    """Custom type cie1000LldpConfigMedLocationInfCivicAddress based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpConfigMedLocationInfCivicAddress_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpConfigMedLocationInfCivicAddress_Object = MibTableColumn
cie1000LldpConfigMedLocationInfCivicAddress = _Cie1000LldpConfigMedLocationInfCivicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 5, 1, 3),
    _Cie1000LldpConfigMedLocationInfCivicAddress_Type()
)
cie1000LldpConfigMedLocationInfCivicAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedLocationInfCivicAddress.setStatus("current")
_Cie1000LldpConfigMedPolicyRowEditor_ObjectIdentity = ObjectIdentity
cie1000LldpConfigMedPolicyRowEditor = _Cie1000LldpConfigMedPolicyRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6)
)


class _Cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy_Type(Integer32):
    """Custom type cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy_Type.__name__ = "Integer32"
_Cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy = _Cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 1),
    _Cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy_Type()
)
cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy.setStatus("current")
_Cie1000LldpConfigMedPolicyRowEditorApplicationType_Type = CIE1000lldpmedRemoteNetworkPolicyApplicationType
_Cie1000LldpConfigMedPolicyRowEditorApplicationType_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorApplicationType = _Cie1000LldpConfigMedPolicyRowEditorApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 3),
    _Cie1000LldpConfigMedPolicyRowEditorApplicationType_Type()
)
cie1000LldpConfigMedPolicyRowEditorApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorApplicationType.setStatus("current")
_Cie1000LldpConfigMedPolicyRowEditorTagged_Type = TruthValue
_Cie1000LldpConfigMedPolicyRowEditorTagged_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorTagged = _Cie1000LldpConfigMedPolicyRowEditorTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 4),
    _Cie1000LldpConfigMedPolicyRowEditorTagged_Type()
)
cie1000LldpConfigMedPolicyRowEditorTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorTagged.setStatus("current")


class _Cie1000LldpConfigMedPolicyRowEditorVlanId_Type(CIE1000Unsigned16):
    """Custom type cie1000LldpConfigMedPolicyRowEditorVlanId based on CIE1000Unsigned16"""
    subtypeSpec = CIE1000Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cie1000LldpConfigMedPolicyRowEditorVlanId_Type.__name__ = "CIE1000Unsigned16"
_Cie1000LldpConfigMedPolicyRowEditorVlanId_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorVlanId = _Cie1000LldpConfigMedPolicyRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 5),
    _Cie1000LldpConfigMedPolicyRowEditorVlanId_Type()
)
cie1000LldpConfigMedPolicyRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorVlanId.setStatus("current")


class _Cie1000LldpConfigMedPolicyRowEditorL2Priority_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpConfigMedPolicyRowEditorL2Priority based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000LldpConfigMedPolicyRowEditorL2Priority_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpConfigMedPolicyRowEditorL2Priority_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorL2Priority = _Cie1000LldpConfigMedPolicyRowEditorL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 6),
    _Cie1000LldpConfigMedPolicyRowEditorL2Priority_Type()
)
cie1000LldpConfigMedPolicyRowEditorL2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorL2Priority.setStatus("current")


class _Cie1000LldpConfigMedPolicyRowEditorDscp_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpConfigMedPolicyRowEditorDscp based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cie1000LldpConfigMedPolicyRowEditorDscp_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpConfigMedPolicyRowEditorDscp_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorDscp = _Cie1000LldpConfigMedPolicyRowEditorDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 7),
    _Cie1000LldpConfigMedPolicyRowEditorDscp_Type()
)
cie1000LldpConfigMedPolicyRowEditorDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorDscp.setStatus("current")
_Cie1000LldpConfigMedPolicyRowEditorAction_Type = CIE1000RowEditorState
_Cie1000LldpConfigMedPolicyRowEditorAction_Object = MibScalar
cie1000LldpConfigMedPolicyRowEditorAction = _Cie1000LldpConfigMedPolicyRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 2, 3, 6, 100),
    _Cie1000LldpConfigMedPolicyRowEditorAction_Type()
)
cie1000LldpConfigMedPolicyRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorAction.setStatus("current")
_Cie1000LldpStatus_ObjectIdentity = ObjectIdentity
cie1000LldpStatus = _Cie1000LldpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3)
)
_Cie1000LldpStatusStatistics_ObjectIdentity = ObjectIdentity
cie1000LldpStatusStatistics = _Cie1000LldpStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1)
)
_Cie1000LldpStatusStatisticsGlobalCounters_ObjectIdentity = ObjectIdentity
cie1000LldpStatusStatisticsGlobalCounters = _Cie1000LldpStatusStatisticsGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 1)
)
_Cie1000LldpStatusStatisticsGlobalCountersTableInserts_Type = Unsigned32
_Cie1000LldpStatusStatisticsGlobalCountersTableInserts_Object = MibScalar
cie1000LldpStatusStatisticsGlobalCountersTableInserts = _Cie1000LldpStatusStatisticsGlobalCountersTableInserts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 1, 1),
    _Cie1000LldpStatusStatisticsGlobalCountersTableInserts_Type()
)
cie1000LldpStatusStatisticsGlobalCountersTableInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsGlobalCountersTableInserts.setStatus("current")
_Cie1000LldpStatusStatisticsGlobalCountersTableDeletes_Type = Unsigned32
_Cie1000LldpStatusStatisticsGlobalCountersTableDeletes_Object = MibScalar
cie1000LldpStatusStatisticsGlobalCountersTableDeletes = _Cie1000LldpStatusStatisticsGlobalCountersTableDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 1, 2),
    _Cie1000LldpStatusStatisticsGlobalCountersTableDeletes_Type()
)
cie1000LldpStatusStatisticsGlobalCountersTableDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsGlobalCountersTableDeletes.setStatus("current")
_Cie1000LldpStatusStatisticsGlobalCountersTableDrops_Type = Unsigned32
_Cie1000LldpStatusStatisticsGlobalCountersTableDrops_Object = MibScalar
cie1000LldpStatusStatisticsGlobalCountersTableDrops = _Cie1000LldpStatusStatisticsGlobalCountersTableDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 1, 3),
    _Cie1000LldpStatusStatisticsGlobalCountersTableDrops_Type()
)
cie1000LldpStatusStatisticsGlobalCountersTableDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsGlobalCountersTableDrops.setStatus("current")
_Cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts_Type = Unsigned32
_Cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts_Object = MibScalar
cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts = _Cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 1, 4),
    _Cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts_Type()
)
cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts.setStatus("current")
_Cie1000LldpStatusStatisticsGlobalCountersLastChangeTime_Type = CIE1000Unsigned64
_Cie1000LldpStatusStatisticsGlobalCountersLastChangeTime_Object = MibScalar
cie1000LldpStatusStatisticsGlobalCountersLastChangeTime = _Cie1000LldpStatusStatisticsGlobalCountersLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 1, 5),
    _Cie1000LldpStatusStatisticsGlobalCountersLastChangeTime_Type()
)
cie1000LldpStatusStatisticsGlobalCountersLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsGlobalCountersLastChangeTime.setStatus("current")
_Cie1000LldpStatusStatisticsTable_Object = MibTable
cie1000LldpStatusStatisticsTable = _Cie1000LldpStatusStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsTable.setStatus("current")
_Cie1000LldpStatusStatisticsEntry_Object = MibTableRow
cie1000LldpStatusStatisticsEntry = _Cie1000LldpStatusStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1)
)
cie1000LldpStatusStatisticsEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsEntry.setStatus("current")
_Cie1000LldpStatusStatisticsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpStatusStatisticsIfIndex_Object = MibTableColumn
cie1000LldpStatusStatisticsIfIndex = _Cie1000LldpStatusStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 1),
    _Cie1000LldpStatusStatisticsIfIndex_Type()
)
cie1000LldpStatusStatisticsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsIfIndex.setStatus("current")
_Cie1000LldpStatusStatisticsTxTotal_Type = Unsigned32
_Cie1000LldpStatusStatisticsTxTotal_Object = MibTableColumn
cie1000LldpStatusStatisticsTxTotal = _Cie1000LldpStatusStatisticsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 2),
    _Cie1000LldpStatusStatisticsTxTotal_Type()
)
cie1000LldpStatusStatisticsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsTxTotal.setStatus("current")
_Cie1000LldpStatusStatisticsRxTotal_Type = Unsigned32
_Cie1000LldpStatusStatisticsRxTotal_Object = MibTableColumn
cie1000LldpStatusStatisticsRxTotal = _Cie1000LldpStatusStatisticsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 3),
    _Cie1000LldpStatusStatisticsRxTotal_Type()
)
cie1000LldpStatusStatisticsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsRxTotal.setStatus("current")
_Cie1000LldpStatusStatisticsRxError_Type = Unsigned32
_Cie1000LldpStatusStatisticsRxError_Object = MibTableColumn
cie1000LldpStatusStatisticsRxError = _Cie1000LldpStatusStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 4),
    _Cie1000LldpStatusStatisticsRxError_Type()
)
cie1000LldpStatusStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsRxError.setStatus("current")
_Cie1000LldpStatusStatisticsRxDiscarded_Type = Unsigned32
_Cie1000LldpStatusStatisticsRxDiscarded_Object = MibTableColumn
cie1000LldpStatusStatisticsRxDiscarded = _Cie1000LldpStatusStatisticsRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 5),
    _Cie1000LldpStatusStatisticsRxDiscarded_Type()
)
cie1000LldpStatusStatisticsRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsRxDiscarded.setStatus("current")
_Cie1000LldpStatusStatisticsTLVsDiscarded_Type = Unsigned32
_Cie1000LldpStatusStatisticsTLVsDiscarded_Object = MibTableColumn
cie1000LldpStatusStatisticsTLVsDiscarded = _Cie1000LldpStatusStatisticsTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 6),
    _Cie1000LldpStatusStatisticsTLVsDiscarded_Type()
)
cie1000LldpStatusStatisticsTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsTLVsDiscarded.setStatus("current")
_Cie1000LldpStatusStatisticsTLVsUnrecognized_Type = Unsigned32
_Cie1000LldpStatusStatisticsTLVsUnrecognized_Object = MibTableColumn
cie1000LldpStatusStatisticsTLVsUnrecognized = _Cie1000LldpStatusStatisticsTLVsUnrecognized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 7),
    _Cie1000LldpStatusStatisticsTLVsUnrecognized_Type()
)
cie1000LldpStatusStatisticsTLVsUnrecognized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsTLVsUnrecognized.setStatus("current")
_Cie1000LldpStatusStatisticsTLVsOrgDiscarded_Type = Unsigned32
_Cie1000LldpStatusStatisticsTLVsOrgDiscarded_Object = MibTableColumn
cie1000LldpStatusStatisticsTLVsOrgDiscarded = _Cie1000LldpStatusStatisticsTLVsOrgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 8),
    _Cie1000LldpStatusStatisticsTLVsOrgDiscarded_Type()
)
cie1000LldpStatusStatisticsTLVsOrgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsTLVsOrgDiscarded.setStatus("current")
_Cie1000LldpStatusStatisticsAgeOuts_Type = Unsigned32
_Cie1000LldpStatusStatisticsAgeOuts_Object = MibTableColumn
cie1000LldpStatusStatisticsAgeOuts = _Cie1000LldpStatusStatisticsAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 1, 2, 1, 9),
    _Cie1000LldpStatusStatisticsAgeOuts_Type()
)
cie1000LldpStatusStatisticsAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsAgeOuts.setStatus("current")
_Cie1000LldpStatusNeighborsInfTable_Object = MibTable
cie1000LldpStatusNeighborsInfTable = _Cie1000LldpStatusNeighborsInfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfTable.setStatus("current")
_Cie1000LldpStatusNeighborsInfEntry_Object = MibTableRow
cie1000LldpStatusNeighborsInfEntry = _Cie1000LldpStatusNeighborsInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1)
)
cie1000LldpStatusNeighborsInfEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfIfIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfLldpmedIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfEntry.setStatus("current")
_Cie1000LldpStatusNeighborsInfIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpStatusNeighborsInfIfIndex_Object = MibTableColumn
cie1000LldpStatusNeighborsInfIfIndex = _Cie1000LldpStatusNeighborsInfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 1),
    _Cie1000LldpStatusNeighborsInfIfIndex_Type()
)
cie1000LldpStatusNeighborsInfIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfIfIndex.setStatus("current")


class _Cie1000LldpStatusNeighborsInfLldpmedIndex_Type(Integer32):
    """Custom type cie1000LldpStatusNeighborsInfLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Cie1000LldpStatusNeighborsInfLldpmedIndex_Type.__name__ = "Integer32"
_Cie1000LldpStatusNeighborsInfLldpmedIndex_Object = MibTableColumn
cie1000LldpStatusNeighborsInfLldpmedIndex = _Cie1000LldpStatusNeighborsInfLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 2),
    _Cie1000LldpStatusNeighborsInfLldpmedIndex_Type()
)
cie1000LldpStatusNeighborsInfLldpmedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfLldpmedIndex.setStatus("current")


class _Cie1000LldpStatusNeighborsInfChassisId_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusNeighborsInfChassisId based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Cie1000LldpStatusNeighborsInfChassisId_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusNeighborsInfChassisId_Object = MibTableColumn
cie1000LldpStatusNeighborsInfChassisId = _Cie1000LldpStatusNeighborsInfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 4),
    _Cie1000LldpStatusNeighborsInfChassisId_Type()
)
cie1000LldpStatusNeighborsInfChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfChassisId.setStatus("current")


class _Cie1000LldpStatusNeighborsInfPortId_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusNeighborsInfPortId based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Cie1000LldpStatusNeighborsInfPortId_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusNeighborsInfPortId_Object = MibTableColumn
cie1000LldpStatusNeighborsInfPortId = _Cie1000LldpStatusNeighborsInfPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 5),
    _Cie1000LldpStatusNeighborsInfPortId_Type()
)
cie1000LldpStatusNeighborsInfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfPortId.setStatus("current")


class _Cie1000LldpStatusNeighborsInfPortDescription_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusNeighborsInfPortDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Cie1000LldpStatusNeighborsInfPortDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusNeighborsInfPortDescription_Object = MibTableColumn
cie1000LldpStatusNeighborsInfPortDescription = _Cie1000LldpStatusNeighborsInfPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 6),
    _Cie1000LldpStatusNeighborsInfPortDescription_Type()
)
cie1000LldpStatusNeighborsInfPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfPortDescription.setStatus("current")


class _Cie1000LldpStatusNeighborsInfSystemName_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusNeighborsInfSystemName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Cie1000LldpStatusNeighborsInfSystemName_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusNeighborsInfSystemName_Object = MibTableColumn
cie1000LldpStatusNeighborsInfSystemName = _Cie1000LldpStatusNeighborsInfSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 7),
    _Cie1000LldpStatusNeighborsInfSystemName_Type()
)
cie1000LldpStatusNeighborsInfSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfSystemName.setStatus("current")


class _Cie1000LldpStatusNeighborsInfSystemDescription_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusNeighborsInfSystemDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Cie1000LldpStatusNeighborsInfSystemDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusNeighborsInfSystemDescription_Object = MibTableColumn
cie1000LldpStatusNeighborsInfSystemDescription = _Cie1000LldpStatusNeighborsInfSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 8),
    _Cie1000LldpStatusNeighborsInfSystemDescription_Type()
)
cie1000LldpStatusNeighborsInfSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfSystemDescription.setStatus("current")
_Cie1000LldpStatusNeighborsInfSystemCapabilities_Type = CIE1000Unsigned16
_Cie1000LldpStatusNeighborsInfSystemCapabilities_Object = MibTableColumn
cie1000LldpStatusNeighborsInfSystemCapabilities = _Cie1000LldpStatusNeighborsInfSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 9),
    _Cie1000LldpStatusNeighborsInfSystemCapabilities_Type()
)
cie1000LldpStatusNeighborsInfSystemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfSystemCapabilities.setStatus("current")
_Cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable_Type = CIE1000Unsigned16
_Cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable_Object = MibTableColumn
cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable = _Cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 2, 1, 10),
    _Cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable_Type()
)
cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfTable_Object = MibTable
cie1000LldpStatusNeighborsMgmtInfTable = _Cie1000LldpStatusNeighborsMgmtInfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfTable.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfEntry_Object = MibTableRow
cie1000LldpStatusNeighborsMgmtInfEntry = _Cie1000LldpStatusNeighborsMgmtInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1)
)
cie1000LldpStatusNeighborsMgmtInfEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfIfIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfLldpmedIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfLldpManagement"),
)
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfEntry.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpStatusNeighborsMgmtInfIfIndex_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfIfIndex = _Cie1000LldpStatusNeighborsMgmtInfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 1),
    _Cie1000LldpStatusNeighborsMgmtInfIfIndex_Type()
)
cie1000LldpStatusNeighborsMgmtInfIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfIfIndex.setStatus("current")


class _Cie1000LldpStatusNeighborsMgmtInfLldpmedIndex_Type(Integer32):
    """Custom type cie1000LldpStatusNeighborsMgmtInfLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Cie1000LldpStatusNeighborsMgmtInfLldpmedIndex_Type.__name__ = "Integer32"
_Cie1000LldpStatusNeighborsMgmtInfLldpmedIndex_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfLldpmedIndex = _Cie1000LldpStatusNeighborsMgmtInfLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 2),
    _Cie1000LldpStatusNeighborsMgmtInfLldpmedIndex_Type()
)
cie1000LldpStatusNeighborsMgmtInfLldpmedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfLldpmedIndex.setStatus("current")


class _Cie1000LldpStatusNeighborsMgmtInfLldpManagement_Type(Integer32):
    """Custom type cie1000LldpStatusNeighborsMgmtInfLldpManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cie1000LldpStatusNeighborsMgmtInfLldpManagement_Type.__name__ = "Integer32"
_Cie1000LldpStatusNeighborsMgmtInfLldpManagement_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfLldpManagement = _Cie1000LldpStatusNeighborsMgmtInfLldpManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 4),
    _Cie1000LldpStatusNeighborsMgmtInfLldpManagement_Type()
)
cie1000LldpStatusNeighborsMgmtInfLldpManagement.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfLldpManagement.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype_Type = CIE1000Unsigned8
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype = _Cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 5),
    _Cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype_Type()
)
cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype.setStatus("current")


class _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress = _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 6),
    _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress_Type()
)
cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype_Type = Integer32
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype = _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 7),
    _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype_Type()
)
cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface_Type = Integer32
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface = _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 8),
    _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface_Type()
)
cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface.setStatus("current")
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid_Type = ObjectIdentifier
_Cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid_Object = MibTableColumn
cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid = _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 3, 1, 9),
    _Cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid_Type()
)
cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid.setStatus("current")
_Cie1000LldpStatusMed_ObjectIdentity = ObjectIdentity
cie1000LldpStatusMed = _Cie1000LldpStatusMed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4)
)
_Cie1000LldpStatusMedRemoteDeviceInfoTable_Object = MibTable
cie1000LldpStatusMedRemoteDeviceInfoTable = _Cie1000LldpStatusMedRemoteDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoTable.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoEntry_Object = MibTableRow
cie1000LldpStatusMedRemoteDeviceInfoEntry = _Cie1000LldpStatusMedRemoteDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1)
)
cie1000LldpStatusMedRemoteDeviceInfoEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoIfIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoEntry.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpStatusMedRemoteDeviceInfoIfIndex_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoIfIndex = _Cie1000LldpStatusMedRemoteDeviceInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 1),
    _Cie1000LldpStatusMedRemoteDeviceInfoIfIndex_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoIfIndex.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex_Type(Integer32):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex_Type.__name__ = "Integer32"
_Cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex = _Cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 2),
    _Cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoCapabilities_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoCapabilities_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoCapabilities = _Cie1000LldpStatusMedRemoteDeviceInfoCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 4),
    _Cie1000LldpStatusMedRemoteDeviceInfoCapabilities_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoCapabilities.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled = _Cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 5),
    _Cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoLatitude_Type = CIE1000Integer64
_Cie1000LldpStatusMedRemoteDeviceInfoLatitude_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoLatitude = _Cie1000LldpStatusMedRemoteDeviceInfoLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 6),
    _Cie1000LldpStatusMedRemoteDeviceInfoLatitude_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoLatitude.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoLongitude_Type = CIE1000Integer64
_Cie1000LldpStatusMedRemoteDeviceInfoLongitude_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoLongitude = _Cie1000LldpStatusMedRemoteDeviceInfoLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 7),
    _Cie1000LldpStatusMedRemoteDeviceInfoLongitude_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoLongitude.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoAltitudeType_Type = CIE1000lldpmedAltitudeType
_Cie1000LldpStatusMedRemoteDeviceInfoAltitudeType_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoAltitudeType = _Cie1000LldpStatusMedRemoteDeviceInfoAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 8),
    _Cie1000LldpStatusMedRemoteDeviceInfoAltitudeType_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoAltitudeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoAltitudeType.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoAltitude_Type = Integer32
_Cie1000LldpStatusMedRemoteDeviceInfoAltitude_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoAltitude = _Cie1000LldpStatusMedRemoteDeviceInfoAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 9),
    _Cie1000LldpStatusMedRemoteDeviceInfoAltitude_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoAltitude.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoDatum_Type = CIE1000lldpmedDatumType
_Cie1000LldpStatusMedRemoteDeviceInfoDatum_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoDatum = _Cie1000LldpStatusMedRemoteDeviceInfoDatum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 10),
    _Cie1000LldpStatusMedRemoteDeviceInfoDatum_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoDatum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoDatum.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoElinaddr_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoElinaddr based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoElinaddr_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoElinaddr_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoElinaddr = _Cie1000LldpStatusMedRemoteDeviceInfoElinaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 11),
    _Cie1000LldpStatusMedRemoteDeviceInfoElinaddr_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoElinaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoElinaddr.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoDeviceType_Type = CIE1000lldpmedRemoteDeviceType
_Cie1000LldpStatusMedRemoteDeviceInfoDeviceType_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoDeviceType = _Cie1000LldpStatusMedRemoteDeviceInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 12),
    _Cie1000LldpStatusMedRemoteDeviceInfoDeviceType_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoDeviceType.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoHwRev_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoHwRev based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoHwRev_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoHwRev_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoHwRev = _Cie1000LldpStatusMedRemoteDeviceInfoHwRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 13),
    _Cie1000LldpStatusMedRemoteDeviceInfoHwRev_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoHwRev.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoFwRev_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoFwRev based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoFwRev_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoFwRev_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoFwRev = _Cie1000LldpStatusMedRemoteDeviceInfoFwRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 14),
    _Cie1000LldpStatusMedRemoteDeviceInfoFwRev_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoFwRev.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoSwRev_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoSwRev based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoSwRev_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoSwRev_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoSwRev = _Cie1000LldpStatusMedRemoteDeviceInfoSwRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 15),
    _Cie1000LldpStatusMedRemoteDeviceInfoSwRev_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoSwRev.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoSerialNo_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoSerialNo based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoSerialNo_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoSerialNo_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoSerialNo = _Cie1000LldpStatusMedRemoteDeviceInfoSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 16),
    _Cie1000LldpStatusMedRemoteDeviceInfoSerialNo_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoSerialNo.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoManufacturerName_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoManufacturerName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoManufacturerName_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoManufacturerName_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoManufacturerName = _Cie1000LldpStatusMedRemoteDeviceInfoManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 17),
    _Cie1000LldpStatusMedRemoteDeviceInfoManufacturerName_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoManufacturerName.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoModelName_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoModelName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoModelName_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoModelName_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoModelName = _Cie1000LldpStatusMedRemoteDeviceInfoModelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 18),
    _Cie1000LldpStatusMedRemoteDeviceInfoModelName_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoModelName.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceInfoAssetId_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceInfoAssetId based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceInfoAssetId_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceInfoAssetId_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoAssetId = _Cie1000LldpStatusMedRemoteDeviceInfoAssetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 19),
    _Cie1000LldpStatusMedRemoteDeviceInfoAssetId_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoAssetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoAssetId.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys = _Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 20),
    _Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys = _Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 21),
    _Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys = _Cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 22),
    _Cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho = _Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 23),
    _Cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Type = CIE1000Unsigned16
_Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho = _Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 1, 1, 24),
    _Cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Type()
)
cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceLocInfoTable_Object = MibTable
cie1000LldpStatusMedRemoteDeviceLocInfoTable = _Cie1000LldpStatusMedRemoteDeviceLocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoTable.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceLocInfoEntry_Object = MibTableRow
cie1000LldpStatusMedRemoteDeviceLocInfoEntry = _Cie1000LldpStatusMedRemoteDeviceLocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1)
)
cie1000LldpStatusMedRemoteDeviceLocInfoEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoEntry.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex = _Cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 1),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Type(Integer32):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Type.__name__ = "Integer32"
_Cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex = _Cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 2),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoState_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoState based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoState_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoState_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoState = _Cie1000LldpStatusMedRemoteDeviceLocInfoState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 5),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoState_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoState.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoCounty_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoCounty based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoCounty_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoCounty_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoCounty = _Cie1000LldpStatusMedRemoteDeviceLocInfoCounty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 6),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoCounty_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoCounty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoCounty.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoCity_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoCity based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoCity_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoCity_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoCity = _Cie1000LldpStatusMedRemoteDeviceLocInfoCity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 7),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoCity_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoCity.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoDistrict_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoDistrict based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoDistrict_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoDistrict_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoDistrict = _Cie1000LldpStatusMedRemoteDeviceLocInfoDistrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 8),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoDistrict_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoDistrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoDistrict.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoBlock_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoBlock based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoBlock_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoBlock_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoBlock = _Cie1000LldpStatusMedRemoteDeviceLocInfoBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 9),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoBlock_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoBlock.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoStreet_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoStreet based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoStreet_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoStreet_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoStreet = _Cie1000LldpStatusMedRemoteDeviceLocInfoStreet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 10),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoStreet_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoStreet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoStreet.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection = _Cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 11),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix = _Cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 12),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix = _Cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 13),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo = _Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 14),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix = _Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 15),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoLandmark_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoLandmark based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoLandmark_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoLandmark_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoLandmark = _Cie1000LldpStatusMedRemoteDeviceLocInfoLandmark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 16),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoLandmark_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoLandmark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoLandmark.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo = _Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 17),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoName_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoName_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoName_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoName = _Cie1000LldpStatusMedRemoteDeviceLocInfoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 18),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoName_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoName.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoZipCode_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoZipCode based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoZipCode_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoZipCode_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoZipCode = _Cie1000LldpStatusMedRemoteDeviceLocInfoZipCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 19),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoZipCode_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoZipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoZipCode.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoBuilding_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoBuilding based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoBuilding_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoBuilding_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoBuilding = _Cie1000LldpStatusMedRemoteDeviceLocInfoBuilding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 20),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoBuilding_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoBuilding.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoApartment_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoApartment based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoApartment_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoApartment_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoApartment = _Cie1000LldpStatusMedRemoteDeviceLocInfoApartment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 21),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoApartment_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoApartment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoApartment.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoFloor_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoFloor based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoFloor_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoFloor_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoFloor = _Cie1000LldpStatusMedRemoteDeviceLocInfoFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 22),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoFloor_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoFloor.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber = _Cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 23),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType = _Cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 24),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName = _Cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 25),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoPoBox_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoPoBox based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoPoBox_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoPoBox_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoPoBox = _Cie1000LldpStatusMedRemoteDeviceLocInfoPoBox_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 26),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoPoBox_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoPoBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoPoBox.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode = _Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 27),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode_Type(CIE1000DisplayString):
    """Custom type cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode_Type.__name__ = "CIE1000DisplayString"
_Cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode = _Cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 2, 1, 28),
    _Cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode_Type()
)
cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTable_Object = MibTable
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTable = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTable.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry_Object = MibTableRow
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1)
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex"),
    (0, "CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 1),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type(Integer32):
    """Custom type cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type.__name__ = "Integer32"
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 2),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Type(Integer32):
    """Custom type cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Type.__name__ = "Integer32"
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 3),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Type = CIE1000lldpmedRemoteNetworkPolicyApplicationType
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 5),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Type = TruthValue
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 6),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy.setStatus("current")
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Type = TruthValue
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 7),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Type(CIE1000Unsigned16):
    """Custom type cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId based on CIE1000Unsigned16"""
    subtypeSpec = CIE1000Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Type.__name__ = "CIE1000Unsigned16"
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 8),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 9),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority.setStatus("current")


class _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Type(CIE1000Unsigned8):
    """Custom type cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Type.__name__ = "CIE1000Unsigned8"
_Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Object = MibTableColumn
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp = _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 3, 4, 3, 1, 10),
    _Cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Type()
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp.setStatus("current")
_Cie1000LldpControl_ObjectIdentity = ObjectIdentity
cie1000LldpControl = _Cie1000LldpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4)
)
_Cie1000LldpControlStatisticsClear_ObjectIdentity = ObjectIdentity
cie1000LldpControlStatisticsClear = _Cie1000LldpControlStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1)
)
_Cie1000LldpControlStatisticsClearTable_Object = MibTable
cie1000LldpControlStatisticsClearTable = _Cie1000LldpControlStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearTable.setStatus("current")
_Cie1000LldpControlStatisticsClearEntry_Object = MibTableRow
cie1000LldpControlStatisticsClearEntry = _Cie1000LldpControlStatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1, 1, 1)
)
cie1000LldpControlStatisticsClearEntry.setIndexNames(
    (0, "CIE1000-LLDP-MIB", "cie1000LldpControlStatisticsClearIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearEntry.setStatus("current")
_Cie1000LldpControlStatisticsClearIfIndex_Type = CIE1000InterfaceIndex
_Cie1000LldpControlStatisticsClearIfIndex_Object = MibTableColumn
cie1000LldpControlStatisticsClearIfIndex = _Cie1000LldpControlStatisticsClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1, 1, 1, 1),
    _Cie1000LldpControlStatisticsClearIfIndex_Type()
)
cie1000LldpControlStatisticsClearIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearIfIndex.setStatus("current")
_Cie1000LldpControlStatisticsClearStatisticsClear_Type = TruthValue
_Cie1000LldpControlStatisticsClearStatisticsClear_Object = MibTableColumn
cie1000LldpControlStatisticsClearStatisticsClear = _Cie1000LldpControlStatisticsClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1, 1, 1, 2),
    _Cie1000LldpControlStatisticsClearStatisticsClear_Type()
)
cie1000LldpControlStatisticsClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearStatisticsClear.setStatus("current")
_Cie1000LldpControlStatisticsClearGlobal_ObjectIdentity = ObjectIdentity
cie1000LldpControlStatisticsClearGlobal = _Cie1000LldpControlStatisticsClearGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1, 2)
)
_Cie1000LldpControlStatisticsClearGlobalClear_Type = TruthValue
_Cie1000LldpControlStatisticsClearGlobalClear_Object = MibScalar
cie1000LldpControlStatisticsClearGlobalClear = _Cie1000LldpControlStatisticsClearGlobalClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 1, 4, 1, 2, 1),
    _Cie1000LldpControlStatisticsClearGlobalClear_Type()
)
cie1000LldpControlStatisticsClearGlobalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearGlobalClear.setStatus("current")
_Cie1000LldpMibConformance_ObjectIdentity = ObjectIdentity
cie1000LldpMibConformance = _Cie1000LldpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2)
)
_Cie1000LldpMibCompliances_ObjectIdentity = ObjectIdentity
cie1000LldpMibCompliances = _Cie1000LldpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 1)
)
_Cie1000LldpMibGroups_ObjectIdentity = ObjectIdentity
cie1000LldpMibGroups = _Cie1000LldpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2)
)

# Managed Objects groups

cie1000LldpConfigGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 1)
)
cie1000LldpConfigGlobalInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigGlobalReInitDelay"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigGlobalMsgTxHold"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigGlobalMsgTxInterval"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigGlobalTxDelay"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigGlobalInfoGroup.setStatus("current")

cie1000LldpConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 2)
)
cie1000LldpConfigInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigAdminState"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigCdpAware"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigOptionalTlvs"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigSnmpNotificationEna"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigInfoGroup.setStatus("current")

cie1000LldpConfigMedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 3)
)
cie1000LldpConfigMedInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigMedIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedOptionalTlvs"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedDeviceType"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedInfoGroup.setStatus("current")

cie1000LldpConfigMedPolicyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 4)
)
cie1000LldpConfigMedPolicyInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyLldpmedPolicy"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyApplicationType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyTagged"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyVlanId"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyL2Priority"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyDscp"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyAction"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyInfoGroup.setStatus("current")

cie1000LldpConfigMedPolicyListInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 5)
)
cie1000LldpConfigMedPolicyListInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyListIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyListLldpmedPolicy"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyListLldpmedPoliciesList"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyListInfoGroup.setStatus("current")

cie1000LldpConfigMedGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 6)
)
cie1000LldpConfigMedGlobalInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalFastRepeatCount"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalLatitude"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalLongitude"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalAltitudeType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalAltitude"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalElinAddr"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalDatum"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalCountryCode"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedGlobalInfoGroup.setStatus("current")

cie1000LldpConfigMedLocationInfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 7)
)
cie1000LldpConfigMedLocationInfInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigMedLocationInfLldpmedIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedLocationInfCivicAddress"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedLocationInfInfoGroup.setStatus("current")

cie1000LldpConfigMedPolicyRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 8)
)
cie1000LldpConfigMedPolicyRowEditorInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorApplicationType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorTagged"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorVlanId"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorL2Priority"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorDscp"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000LldpConfigMedPolicyRowEditorInfoGroup.setStatus("current")

cie1000LldpStatusStatisticsGlobalCountersInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 9)
)
cie1000LldpStatusStatisticsGlobalCountersInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsGlobalCountersTableInserts"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsGlobalCountersTableDeletes"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsGlobalCountersTableDrops"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsGlobalCountersLastChangeTime"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsGlobalCountersInfoGroup.setStatus("current")

cie1000LldpStatusStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 10)
)
cie1000LldpStatusStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsTxTotal"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsRxTotal"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsRxError"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsRxDiscarded"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsTLVsDiscarded"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsTLVsUnrecognized"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsTLVsOrgDiscarded"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsAgeOuts"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusStatisticsTableInfoGroup.setStatus("current")

cie1000LldpStatusNeighborsInfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 11)
)
cie1000LldpStatusNeighborsInfInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfLldpmedIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfChassisId"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfPortId"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfPortDescription"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfSystemName"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfSystemDescription"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfSystemCapabilities"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsInfInfoGroup.setStatus("current")

cie1000LldpStatusNeighborsMgmtInfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 12)
)
cie1000LldpStatusNeighborsMgmtInfInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfLldpmedIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfLldpManagement"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusNeighborsMgmtInfInfoGroup.setStatus("current")

cie1000LldpStatusMedRemoteDeviceInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 13)
)
cie1000LldpStatusMedRemoteDeviceInfoInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoCapabilities"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoLatitude"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoLongitude"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoAltitudeType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoAltitude"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoDatum"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoElinaddr"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoDeviceType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoHwRev"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoFwRev"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoSwRev"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoSerialNo"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoManufacturerName"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoModelName"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoAssetId"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceInfoInfoGroup.setStatus("current")

cie1000LldpStatusMedRemoteDeviceLocInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 14)
)
cie1000LldpStatusMedRemoteDeviceLocInfoInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoState"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoCounty"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoCity"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoDistrict"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoBlock"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoStreet"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoLandmark"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoName"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoZipCode"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoBuilding"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoApartment"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoFloor"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoPoBox"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceLocInfoInfoGroup.setStatus("current")

cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 15)
)
cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp"))
)
if mibBuilder.loadTexts:
    cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup.setStatus("current")

cie1000LldpControlStatisticsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 16)
)
cie1000LldpControlStatisticsClearTableInfoGroup.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpControlStatisticsClearIfIndex"),
        ("CIE1000-LLDP-MIB", "cie1000LldpControlStatisticsClearStatisticsClear"))
)
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearTableInfoGroup.setStatus("current")

cie1000LldpControlStatisticsClearGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 2, 17)
)
cie1000LldpControlStatisticsClearGlobalInfoGroup.setObjects(
    ("CIE1000-LLDP-MIB", "cie1000LldpControlStatisticsClearGlobalClear")
)
if mibBuilder.loadTexts:
    cie1000LldpControlStatisticsClearGlobalInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000LldpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 34, 2, 1, 1)
)
cie1000LldpMibCompliance.setObjects(
      *(("CIE1000-LLDP-MIB", "cie1000LldpConfigGlobalInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyListInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedGlobalInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedLocationInfInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpConfigMedPolicyRowEditorInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsGlobalCountersInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusStatisticsTableInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsInfInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusNeighborsMgmtInfInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceInfoInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceLocInfoInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpControlStatisticsClearTableInfoGroup"),
        ("CIE1000-LLDP-MIB", "cie1000LldpControlStatisticsClearGlobalInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000LldpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-LLDP-MIB",
    **{"CIE1000lldpAdminState": CIE1000lldpAdminState,
       "CIE1000lldpmedAltitudeType": CIE1000lldpmedAltitudeType,
       "CIE1000lldpmedCivicAddressType": CIE1000lldpmedCivicAddressType,
       "CIE1000lldpmedDatumType": CIE1000lldpmedDatumType,
       "CIE1000lldpmedDeviceType": CIE1000lldpmedDeviceType,
       "CIE1000lldpmedRemoteDeviceType": CIE1000lldpmedRemoteDeviceType,
       "CIE1000lldpmedRemoteNetworkPolicyApplicationType": CIE1000lldpmedRemoteNetworkPolicyApplicationType,
       "cie1000LldpMib": cie1000LldpMib,
       "cie1000LldpMibObjects": cie1000LldpMibObjects,
       "cie1000LldpConfig": cie1000LldpConfig,
       "cie1000LldpConfigGlobal": cie1000LldpConfigGlobal,
       "cie1000LldpConfigGlobalReInitDelay": cie1000LldpConfigGlobalReInitDelay,
       "cie1000LldpConfigGlobalMsgTxHold": cie1000LldpConfigGlobalMsgTxHold,
       "cie1000LldpConfigGlobalMsgTxInterval": cie1000LldpConfigGlobalMsgTxInterval,
       "cie1000LldpConfigGlobalTxDelay": cie1000LldpConfigGlobalTxDelay,
       "cie1000LldpConfigTable": cie1000LldpConfigTable,
       "cie1000LldpConfigEntry": cie1000LldpConfigEntry,
       "cie1000LldpConfigIfIndex": cie1000LldpConfigIfIndex,
       "cie1000LldpConfigAdminState": cie1000LldpConfigAdminState,
       "cie1000LldpConfigCdpAware": cie1000LldpConfigCdpAware,
       "cie1000LldpConfigOptionalTlvs": cie1000LldpConfigOptionalTlvs,
       "cie1000LldpConfigSnmpNotificationEna": cie1000LldpConfigSnmpNotificationEna,
       "cie1000LldpConfigMed": cie1000LldpConfigMed,
       "cie1000LldpConfigMedTable": cie1000LldpConfigMedTable,
       "cie1000LldpConfigMedEntry": cie1000LldpConfigMedEntry,
       "cie1000LldpConfigMedIfIndex": cie1000LldpConfigMedIfIndex,
       "cie1000LldpConfigMedOptionalTlvs": cie1000LldpConfigMedOptionalTlvs,
       "cie1000LldpConfigMedDeviceType": cie1000LldpConfigMedDeviceType,
       "cie1000LldpConfigMedPolicyTable": cie1000LldpConfigMedPolicyTable,
       "cie1000LldpConfigMedPolicyEntry": cie1000LldpConfigMedPolicyEntry,
       "cie1000LldpConfigMedPolicyLldpmedPolicy": cie1000LldpConfigMedPolicyLldpmedPolicy,
       "cie1000LldpConfigMedPolicyApplicationType": cie1000LldpConfigMedPolicyApplicationType,
       "cie1000LldpConfigMedPolicyTagged": cie1000LldpConfigMedPolicyTagged,
       "cie1000LldpConfigMedPolicyVlanId": cie1000LldpConfigMedPolicyVlanId,
       "cie1000LldpConfigMedPolicyL2Priority": cie1000LldpConfigMedPolicyL2Priority,
       "cie1000LldpConfigMedPolicyDscp": cie1000LldpConfigMedPolicyDscp,
       "cie1000LldpConfigMedPolicyAction": cie1000LldpConfigMedPolicyAction,
       "cie1000LldpConfigMedPolicyListTable": cie1000LldpConfigMedPolicyListTable,
       "cie1000LldpConfigMedPolicyListEntry": cie1000LldpConfigMedPolicyListEntry,
       "cie1000LldpConfigMedPolicyListIfIndex": cie1000LldpConfigMedPolicyListIfIndex,
       "cie1000LldpConfigMedPolicyListLldpmedPolicy": cie1000LldpConfigMedPolicyListLldpmedPolicy,
       "cie1000LldpConfigMedPolicyListLldpmedPoliciesList": cie1000LldpConfigMedPolicyListLldpmedPoliciesList,
       "cie1000LldpConfigMedGlobal": cie1000LldpConfigMedGlobal,
       "cie1000LldpConfigMedGlobalFastRepeatCount": cie1000LldpConfigMedGlobalFastRepeatCount,
       "cie1000LldpConfigMedGlobalLatitude": cie1000LldpConfigMedGlobalLatitude,
       "cie1000LldpConfigMedGlobalLongitude": cie1000LldpConfigMedGlobalLongitude,
       "cie1000LldpConfigMedGlobalAltitudeType": cie1000LldpConfigMedGlobalAltitudeType,
       "cie1000LldpConfigMedGlobalAltitude": cie1000LldpConfigMedGlobalAltitude,
       "cie1000LldpConfigMedGlobalElinAddr": cie1000LldpConfigMedGlobalElinAddr,
       "cie1000LldpConfigMedGlobalDatum": cie1000LldpConfigMedGlobalDatum,
       "cie1000LldpConfigMedGlobalCountryCode": cie1000LldpConfigMedGlobalCountryCode,
       "cie1000LldpConfigMedLocationInfTable": cie1000LldpConfigMedLocationInfTable,
       "cie1000LldpConfigMedLocationInfEntry": cie1000LldpConfigMedLocationInfEntry,
       "cie1000LldpConfigMedLocationInfLldpmedIndex": cie1000LldpConfigMedLocationInfLldpmedIndex,
       "cie1000LldpConfigMedLocationInfCivicAddress": cie1000LldpConfigMedLocationInfCivicAddress,
       "cie1000LldpConfigMedPolicyRowEditor": cie1000LldpConfigMedPolicyRowEditor,
       "cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy": cie1000LldpConfigMedPolicyRowEditorLldpmedPolicy,
       "cie1000LldpConfigMedPolicyRowEditorApplicationType": cie1000LldpConfigMedPolicyRowEditorApplicationType,
       "cie1000LldpConfigMedPolicyRowEditorTagged": cie1000LldpConfigMedPolicyRowEditorTagged,
       "cie1000LldpConfigMedPolicyRowEditorVlanId": cie1000LldpConfigMedPolicyRowEditorVlanId,
       "cie1000LldpConfigMedPolicyRowEditorL2Priority": cie1000LldpConfigMedPolicyRowEditorL2Priority,
       "cie1000LldpConfigMedPolicyRowEditorDscp": cie1000LldpConfigMedPolicyRowEditorDscp,
       "cie1000LldpConfigMedPolicyRowEditorAction": cie1000LldpConfigMedPolicyRowEditorAction,
       "cie1000LldpStatus": cie1000LldpStatus,
       "cie1000LldpStatusStatistics": cie1000LldpStatusStatistics,
       "cie1000LldpStatusStatisticsGlobalCounters": cie1000LldpStatusStatisticsGlobalCounters,
       "cie1000LldpStatusStatisticsGlobalCountersTableInserts": cie1000LldpStatusStatisticsGlobalCountersTableInserts,
       "cie1000LldpStatusStatisticsGlobalCountersTableDeletes": cie1000LldpStatusStatisticsGlobalCountersTableDeletes,
       "cie1000LldpStatusStatisticsGlobalCountersTableDrops": cie1000LldpStatusStatisticsGlobalCountersTableDrops,
       "cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts": cie1000LldpStatusStatisticsGlobalCountersTableAgeOuts,
       "cie1000LldpStatusStatisticsGlobalCountersLastChangeTime": cie1000LldpStatusStatisticsGlobalCountersLastChangeTime,
       "cie1000LldpStatusStatisticsTable": cie1000LldpStatusStatisticsTable,
       "cie1000LldpStatusStatisticsEntry": cie1000LldpStatusStatisticsEntry,
       "cie1000LldpStatusStatisticsIfIndex": cie1000LldpStatusStatisticsIfIndex,
       "cie1000LldpStatusStatisticsTxTotal": cie1000LldpStatusStatisticsTxTotal,
       "cie1000LldpStatusStatisticsRxTotal": cie1000LldpStatusStatisticsRxTotal,
       "cie1000LldpStatusStatisticsRxError": cie1000LldpStatusStatisticsRxError,
       "cie1000LldpStatusStatisticsRxDiscarded": cie1000LldpStatusStatisticsRxDiscarded,
       "cie1000LldpStatusStatisticsTLVsDiscarded": cie1000LldpStatusStatisticsTLVsDiscarded,
       "cie1000LldpStatusStatisticsTLVsUnrecognized": cie1000LldpStatusStatisticsTLVsUnrecognized,
       "cie1000LldpStatusStatisticsTLVsOrgDiscarded": cie1000LldpStatusStatisticsTLVsOrgDiscarded,
       "cie1000LldpStatusStatisticsAgeOuts": cie1000LldpStatusStatisticsAgeOuts,
       "cie1000LldpStatusNeighborsInfTable": cie1000LldpStatusNeighborsInfTable,
       "cie1000LldpStatusNeighborsInfEntry": cie1000LldpStatusNeighborsInfEntry,
       "cie1000LldpStatusNeighborsInfIfIndex": cie1000LldpStatusNeighborsInfIfIndex,
       "cie1000LldpStatusNeighborsInfLldpmedIndex": cie1000LldpStatusNeighborsInfLldpmedIndex,
       "cie1000LldpStatusNeighborsInfChassisId": cie1000LldpStatusNeighborsInfChassisId,
       "cie1000LldpStatusNeighborsInfPortId": cie1000LldpStatusNeighborsInfPortId,
       "cie1000LldpStatusNeighborsInfPortDescription": cie1000LldpStatusNeighborsInfPortDescription,
       "cie1000LldpStatusNeighborsInfSystemName": cie1000LldpStatusNeighborsInfSystemName,
       "cie1000LldpStatusNeighborsInfSystemDescription": cie1000LldpStatusNeighborsInfSystemDescription,
       "cie1000LldpStatusNeighborsInfSystemCapabilities": cie1000LldpStatusNeighborsInfSystemCapabilities,
       "cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable": cie1000LldpStatusNeighborsInfSystemCapabilitiesEnable,
       "cie1000LldpStatusNeighborsMgmtInfTable": cie1000LldpStatusNeighborsMgmtInfTable,
       "cie1000LldpStatusNeighborsMgmtInfEntry": cie1000LldpStatusNeighborsMgmtInfEntry,
       "cie1000LldpStatusNeighborsMgmtInfIfIndex": cie1000LldpStatusNeighborsMgmtInfIfIndex,
       "cie1000LldpStatusNeighborsMgmtInfLldpmedIndex": cie1000LldpStatusNeighborsMgmtInfLldpmedIndex,
       "cie1000LldpStatusNeighborsMgmtInfLldpManagement": cie1000LldpStatusNeighborsMgmtInfLldpManagement,
       "cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype": cie1000LldpStatusNeighborsMgmtInfSystemMgmAddressSubtype,
       "cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress": cie1000LldpStatusNeighborsMgmtInfSystemMgmtAddress,
       "cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype": cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterfaceSubtype,
       "cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface": cie1000LldpStatusNeighborsMgmtInfSystemMgmtInterface,
       "cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid": cie1000LldpStatusNeighborsMgmtInfSystemMgmtOid,
       "cie1000LldpStatusMed": cie1000LldpStatusMed,
       "cie1000LldpStatusMedRemoteDeviceInfoTable": cie1000LldpStatusMedRemoteDeviceInfoTable,
       "cie1000LldpStatusMedRemoteDeviceInfoEntry": cie1000LldpStatusMedRemoteDeviceInfoEntry,
       "cie1000LldpStatusMedRemoteDeviceInfoIfIndex": cie1000LldpStatusMedRemoteDeviceInfoIfIndex,
       "cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex": cie1000LldpStatusMedRemoteDeviceInfoLldpmedIndex,
       "cie1000LldpStatusMedRemoteDeviceInfoCapabilities": cie1000LldpStatusMedRemoteDeviceInfoCapabilities,
       "cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled": cie1000LldpStatusMedRemoteDeviceInfoCapabilitiesEnabled,
       "cie1000LldpStatusMedRemoteDeviceInfoLatitude": cie1000LldpStatusMedRemoteDeviceInfoLatitude,
       "cie1000LldpStatusMedRemoteDeviceInfoLongitude": cie1000LldpStatusMedRemoteDeviceInfoLongitude,
       "cie1000LldpStatusMedRemoteDeviceInfoAltitudeType": cie1000LldpStatusMedRemoteDeviceInfoAltitudeType,
       "cie1000LldpStatusMedRemoteDeviceInfoAltitude": cie1000LldpStatusMedRemoteDeviceInfoAltitude,
       "cie1000LldpStatusMedRemoteDeviceInfoDatum": cie1000LldpStatusMedRemoteDeviceInfoDatum,
       "cie1000LldpStatusMedRemoteDeviceInfoElinaddr": cie1000LldpStatusMedRemoteDeviceInfoElinaddr,
       "cie1000LldpStatusMedRemoteDeviceInfoDeviceType": cie1000LldpStatusMedRemoteDeviceInfoDeviceType,
       "cie1000LldpStatusMedRemoteDeviceInfoHwRev": cie1000LldpStatusMedRemoteDeviceInfoHwRev,
       "cie1000LldpStatusMedRemoteDeviceInfoFwRev": cie1000LldpStatusMedRemoteDeviceInfoFwRev,
       "cie1000LldpStatusMedRemoteDeviceInfoSwRev": cie1000LldpStatusMedRemoteDeviceInfoSwRev,
       "cie1000LldpStatusMedRemoteDeviceInfoSerialNo": cie1000LldpStatusMedRemoteDeviceInfoSerialNo,
       "cie1000LldpStatusMedRemoteDeviceInfoManufacturerName": cie1000LldpStatusMedRemoteDeviceInfoManufacturerName,
       "cie1000LldpStatusMedRemoteDeviceInfoModelName": cie1000LldpStatusMedRemoteDeviceInfoModelName,
       "cie1000LldpStatusMedRemoteDeviceInfoAssetId": cie1000LldpStatusMedRemoteDeviceInfoAssetId,
       "cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys": cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSys,
       "cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys": cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSys,
       "cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys": cie1000LldpStatusMedRemoteDeviceInfoEeeFbTwSys,
       "cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho": cie1000LldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho,
       "cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho": cie1000LldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho,
       "cie1000LldpStatusMedRemoteDeviceLocInfoTable": cie1000LldpStatusMedRemoteDeviceLocInfoTable,
       "cie1000LldpStatusMedRemoteDeviceLocInfoEntry": cie1000LldpStatusMedRemoteDeviceLocInfoEntry,
       "cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex": cie1000LldpStatusMedRemoteDeviceLocInfoIfIndex,
       "cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex": cie1000LldpStatusMedRemoteDeviceLocInfoLldpmedIndex,
       "cie1000LldpStatusMedRemoteDeviceLocInfoState": cie1000LldpStatusMedRemoteDeviceLocInfoState,
       "cie1000LldpStatusMedRemoteDeviceLocInfoCounty": cie1000LldpStatusMedRemoteDeviceLocInfoCounty,
       "cie1000LldpStatusMedRemoteDeviceLocInfoCity": cie1000LldpStatusMedRemoteDeviceLocInfoCity,
       "cie1000LldpStatusMedRemoteDeviceLocInfoDistrict": cie1000LldpStatusMedRemoteDeviceLocInfoDistrict,
       "cie1000LldpStatusMedRemoteDeviceLocInfoBlock": cie1000LldpStatusMedRemoteDeviceLocInfoBlock,
       "cie1000LldpStatusMedRemoteDeviceLocInfoStreet": cie1000LldpStatusMedRemoteDeviceLocInfoStreet,
       "cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection": cie1000LldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection,
       "cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix": cie1000LldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix,
       "cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix": cie1000LldpStatusMedRemoteDeviceLocInfoStreetSuffix,
       "cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo": cie1000LldpStatusMedRemoteDeviceLocInfoHouseNo,
       "cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix": cie1000LldpStatusMedRemoteDeviceLocInfoHouseNoSuffix,
       "cie1000LldpStatusMedRemoteDeviceLocInfoLandmark": cie1000LldpStatusMedRemoteDeviceLocInfoLandmark,
       "cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo": cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalInfo,
       "cie1000LldpStatusMedRemoteDeviceLocInfoName": cie1000LldpStatusMedRemoteDeviceLocInfoName,
       "cie1000LldpStatusMedRemoteDeviceLocInfoZipCode": cie1000LldpStatusMedRemoteDeviceLocInfoZipCode,
       "cie1000LldpStatusMedRemoteDeviceLocInfoBuilding": cie1000LldpStatusMedRemoteDeviceLocInfoBuilding,
       "cie1000LldpStatusMedRemoteDeviceLocInfoApartment": cie1000LldpStatusMedRemoteDeviceLocInfoApartment,
       "cie1000LldpStatusMedRemoteDeviceLocInfoFloor": cie1000LldpStatusMedRemoteDeviceLocInfoFloor,
       "cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber": cie1000LldpStatusMedRemoteDeviceLocInfoRoomNumber,
       "cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType": cie1000LldpStatusMedRemoteDeviceLocInfoPlaceType,
       "cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName": cie1000LldpStatusMedRemoteDeviceLocInfoPostalCommunityName,
       "cie1000LldpStatusMedRemoteDeviceLocInfoPoBox": cie1000LldpStatusMedRemoteDeviceLocInfoPoBox,
       "cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode": cie1000LldpStatusMedRemoteDeviceLocInfoAdditionalCode,
       "cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode": cie1000LldpStatusMedRemoteDeviceLocInfoCountryCode,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTable": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTable,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoEntry,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoTagged,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoDscp,
       "cie1000LldpControl": cie1000LldpControl,
       "cie1000LldpControlStatisticsClear": cie1000LldpControlStatisticsClear,
       "cie1000LldpControlStatisticsClearTable": cie1000LldpControlStatisticsClearTable,
       "cie1000LldpControlStatisticsClearEntry": cie1000LldpControlStatisticsClearEntry,
       "cie1000LldpControlStatisticsClearIfIndex": cie1000LldpControlStatisticsClearIfIndex,
       "cie1000LldpControlStatisticsClearStatisticsClear": cie1000LldpControlStatisticsClearStatisticsClear,
       "cie1000LldpControlStatisticsClearGlobal": cie1000LldpControlStatisticsClearGlobal,
       "cie1000LldpControlStatisticsClearGlobalClear": cie1000LldpControlStatisticsClearGlobalClear,
       "cie1000LldpMibConformance": cie1000LldpMibConformance,
       "cie1000LldpMibCompliances": cie1000LldpMibCompliances,
       "cie1000LldpMibCompliance": cie1000LldpMibCompliance,
       "cie1000LldpMibGroups": cie1000LldpMibGroups,
       "cie1000LldpConfigGlobalInfoGroup": cie1000LldpConfigGlobalInfoGroup,
       "cie1000LldpConfigInfoGroup": cie1000LldpConfigInfoGroup,
       "cie1000LldpConfigMedInfoGroup": cie1000LldpConfigMedInfoGroup,
       "cie1000LldpConfigMedPolicyInfoGroup": cie1000LldpConfigMedPolicyInfoGroup,
       "cie1000LldpConfigMedPolicyListInfoGroup": cie1000LldpConfigMedPolicyListInfoGroup,
       "cie1000LldpConfigMedGlobalInfoGroup": cie1000LldpConfigMedGlobalInfoGroup,
       "cie1000LldpConfigMedLocationInfInfoGroup": cie1000LldpConfigMedLocationInfInfoGroup,
       "cie1000LldpConfigMedPolicyRowEditorInfoGroup": cie1000LldpConfigMedPolicyRowEditorInfoGroup,
       "cie1000LldpStatusStatisticsGlobalCountersInfoGroup": cie1000LldpStatusStatisticsGlobalCountersInfoGroup,
       "cie1000LldpStatusStatisticsTableInfoGroup": cie1000LldpStatusStatisticsTableInfoGroup,
       "cie1000LldpStatusNeighborsInfInfoGroup": cie1000LldpStatusNeighborsInfInfoGroup,
       "cie1000LldpStatusNeighborsMgmtInfInfoGroup": cie1000LldpStatusNeighborsMgmtInfInfoGroup,
       "cie1000LldpStatusMedRemoteDeviceInfoInfoGroup": cie1000LldpStatusMedRemoteDeviceInfoInfoGroup,
       "cie1000LldpStatusMedRemoteDeviceLocInfoInfoGroup": cie1000LldpStatusMedRemoteDeviceLocInfoInfoGroup,
       "cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup": cie1000LldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup,
       "cie1000LldpControlStatisticsClearTableInfoGroup": cie1000LldpControlStatisticsClearTableInfoGroup,
       "cie1000LldpControlStatisticsClearGlobalInfoGroup": cie1000LldpControlStatisticsClearGlobalInfoGroup}
)
