# SNMP MIB module (WLSX-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aruba_14823/WLSX-WLAN-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:48:55 2025
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaAPStatus,
 ArubaAccessPointMode,
 ArubaActiveState,
 ArubaAntennaSetting,
 ArubaAuthenticationMethods,
 ArubaDual5GMode,
 ArubaEnableValue,
 ArubaEncryptionMethods,
 ArubaEnet1Mode,
 ArubaFlexRadioMode,
 ArubaFrameType,
 ArubaHTExtChannel,
 ArubaHTMode,
 ArubaMeshRole,
 ArubaMonitorMode,
 ArubaPhyType,
 ArubaPortSpeed,
 ArubaRogueApType,
 ArubaSplit5GMode,
 ArubaUnprovisionedStatus,
 ArubaVlanValidRange,
 ArubaVoipProtocolType) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaAPStatus",
    "ArubaAccessPointMode",
    "ArubaActiveState",
    "ArubaAntennaSetting",
    "ArubaAuthenticationMethods",
    "ArubaDual5GMode",
    "ArubaEnableValue",
    "ArubaEncryptionMethods",
    "ArubaEnet1Mode",
    "ArubaFlexRadioMode",
    "ArubaFrameType",
    "ArubaHTExtChannel",
    "ArubaHTMode",
    "ArubaMeshRole",
    "ArubaMonitorMode",
    "ArubaPhyType",
    "ArubaPortSpeed",
    "ArubaRogueApType",
    "ArubaSplit5GMode",
    "ArubaUnprovisionedStatus",
    "ArubaVlanValidRange",
    "ArubaVoipProtocolType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxWlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    wlsxWlanMIB.setRevisions(
        ("2020-08-14 17:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxWlanConfigGroup_ObjectIdentity = ObjectIdentity
wlsxWlanConfigGroup = _WlsxWlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1)
)
_WlsxSSIDConfigGroup_ObjectIdentity = ObjectIdentity
wlsxSSIDConfigGroup = _WlsxSSIDConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1)
)
_WlsxSSIDConfigTable_Object = MibTable
wlsxSSIDConfigTable = _WlsxSSIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxSSIDConfigTable.setStatus("current")
_WlsxSSIDConfigEntry_Object = MibTableRow
wlsxSSIDConfigEntry = _WlsxSSIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1)
)
wlsxSSIDConfigEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
    (0, "WLSX-WLAN-MIB", "wlanESSIDIndex"),
)
if mibBuilder.loadTexts:
    wlsxSSIDConfigEntry.setStatus("current")


class _WlanESSIDIndex_Type(Integer32):
    """Custom type wlanESSIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WlanESSIDIndex_Type.__name__ = "Integer32"
_WlanESSIDIndex_Object = MibTableColumn
wlanESSIDIndex = _WlanESSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 1),
    _WlanESSIDIndex_Type()
)
wlanESSIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanESSIDIndex.setStatus("current")
_WlanSSIDConfigHideSSID_Type = TruthValue
_WlanSSIDConfigHideSSID_Object = MibTableColumn
wlanSSIDConfigHideSSID = _WlanSSIDConfigHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 2),
    _WlanSSIDConfigHideSSID_Type()
)
wlanSSIDConfigHideSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSIDConfigHideSSID.setStatus("current")
_WlanSSIDConfigNumStaAllowed_Type = Unsigned32
_WlanSSIDConfigNumStaAllowed_Object = MibTableColumn
wlanSSIDConfigNumStaAllowed = _WlanSSIDConfigNumStaAllowed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 3),
    _WlanSSIDConfigNumStaAllowed_Type()
)
wlanSSIDConfigNumStaAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSIDConfigNumStaAllowed.setStatus("current")
_WlanSSIDConfigWmmBeDscp_Type = Unsigned32
_WlanSSIDConfigWmmBeDscp_Object = MibTableColumn
wlanSSIDConfigWmmBeDscp = _WlanSSIDConfigWmmBeDscp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 4),
    _WlanSSIDConfigWmmBeDscp_Type()
)
wlanSSIDConfigWmmBeDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSIDConfigWmmBeDscp.setStatus("current")
_WlanSSIDConfigWmmBkDscp_Type = Unsigned32
_WlanSSIDConfigWmmBkDscp_Object = MibTableColumn
wlanSSIDConfigWmmBkDscp = _WlanSSIDConfigWmmBkDscp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 5),
    _WlanSSIDConfigWmmBkDscp_Type()
)
wlanSSIDConfigWmmBkDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSIDConfigWmmBkDscp.setStatus("current")
_WlanSSIDConfigWmmViDscp_Type = Unsigned32
_WlanSSIDConfigWmmViDscp_Object = MibTableColumn
wlanSSIDConfigWmmViDscp = _WlanSSIDConfigWmmViDscp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 6),
    _WlanSSIDConfigWmmViDscp_Type()
)
wlanSSIDConfigWmmViDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSIDConfigWmmViDscp.setStatus("current")
_WlanSSIDConfigWmmVoDscp_Type = Unsigned32
_WlanSSIDConfigWmmVoDscp_Object = MibTableColumn
wlanSSIDConfigWmmVoDscp = _WlanSSIDConfigWmmVoDscp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 1, 1, 1, 7),
    _WlanSSIDConfigWmmVoDscp_Type()
)
wlanSSIDConfigWmmVoDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSIDConfigWmmVoDscp.setStatus("current")
_WlsxAPConfigGroup_ObjectIdentity = ObjectIdentity
wlsxAPConfigGroup = _WlsxAPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 2)
)
_WlsxAPConfigTable_Object = MibTable
wlsxAPConfigTable = _WlsxAPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wlsxAPConfigTable.setStatus("current")
_WlsxAPConfigEntry_Object = MibTableRow
wlsxAPConfigEntry = _WlsxAPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 2, 1, 1)
)
wlsxAPConfigEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
)
if mibBuilder.loadTexts:
    wlsxAPConfigEntry.setStatus("current")
_WlanAPConfigNetmask_Type = IpAddress
_WlanAPConfigNetmask_Object = MibTableColumn
wlanAPConfigNetmask = _WlanAPConfigNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 2, 1, 1, 1),
    _WlanAPConfigNetmask_Type()
)
wlanAPConfigNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPConfigNetmask.setStatus("current")
_WlanAPConfigGateway_Type = IpAddress
_WlanAPConfigGateway_Object = MibTableColumn
wlanAPConfigGateway = _WlanAPConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 1, 2, 1, 1, 2),
    _WlanAPConfigGateway_Type()
)
wlanAPConfigGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPConfigGateway.setStatus("current")
_WlsxWlanStateGroup_ObjectIdentity = ObjectIdentity
wlsxWlanStateGroup = _WlsxWlanStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2)
)
_WlsxWlanAccessPointInfoGroup_ObjectIdentity = ObjectIdentity
wlsxWlanAccessPointInfoGroup = _WlsxWlanAccessPointInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1)
)
_WlsxWlanTotalNumAccessPoints_Type = Unsigned32
_WlsxWlanTotalNumAccessPoints_Object = MibScalar
wlsxWlanTotalNumAccessPoints = _WlsxWlanTotalNumAccessPoints_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 1),
    _WlsxWlanTotalNumAccessPoints_Type()
)
wlsxWlanTotalNumAccessPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxWlanTotalNumAccessPoints.setStatus("current")
_WlsxWlanTotalNumStationsAssociated_Type = Unsigned32
_WlsxWlanTotalNumStationsAssociated_Object = MibScalar
wlsxWlanTotalNumStationsAssociated = _WlsxWlanTotalNumStationsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 2),
    _WlsxWlanTotalNumStationsAssociated_Type()
)
wlsxWlanTotalNumStationsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxWlanTotalNumStationsAssociated.setStatus("current")
_WlsxWlanAPGroupTable_Object = MibTable
wlsxWlanAPGroupTable = _WlsxWlanAPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxWlanAPGroupTable.setStatus("current")
_WlsxWlanAPGroupEntry_Object = MibTableRow
wlsxWlanAPGroupEntry = _WlsxWlanAPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 3, 1)
)
wlsxWlanAPGroupEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPGroup"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPGroupEntry.setStatus("current")
_WlanAPGroup_Type = DisplayString
_WlanAPGroup_Object = MibTableColumn
wlanAPGroup = _WlanAPGroup_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 3, 1, 1),
    _WlanAPGroup_Type()
)
wlanAPGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanAPGroup.setStatus("current")
_WlanAPNumAps_Type = Integer32
_WlanAPNumAps_Object = MibTableColumn
wlanAPNumAps = _WlanAPNumAps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 3, 1, 2),
    _WlanAPNumAps_Type()
)
wlanAPNumAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPNumAps.setStatus("current")
_WlsxWlanAPTable_Object = MibTable
wlsxWlanAPTable = _WlsxWlanAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxWlanAPTable.setStatus("current")
_WlsxWlanAPEntry_Object = MibTableRow
wlsxWlanAPEntry = _WlsxWlanAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1)
)
wlsxWlanAPEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPEntry.setStatus("current")
_WlanAPMacAddress_Type = MacAddress
_WlanAPMacAddress_Object = MibTableColumn
wlanAPMacAddress = _WlanAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 1),
    _WlanAPMacAddress_Type()
)
wlanAPMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanAPMacAddress.setStatus("current")
_WlanAPIpAddress_Type = IpAddress
_WlanAPIpAddress_Object = MibTableColumn
wlanAPIpAddress = _WlanAPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 2),
    _WlanAPIpAddress_Type()
)
wlanAPIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPIpAddress.setStatus("current")
_WlanAPName_Type = DisplayString
_WlanAPName_Object = MibTableColumn
wlanAPName = _WlanAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 3),
    _WlanAPName_Type()
)
wlanAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPName.setStatus("current")
_WlanAPGroupName_Type = DisplayString
_WlanAPGroupName_Object = MibTableColumn
wlanAPGroupName = _WlanAPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 4),
    _WlanAPGroupName_Type()
)
wlanAPGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPGroupName.setStatus("current")
_WlanAPModel_Type = ObjectIdentifier
_WlanAPModel_Object = MibTableColumn
wlanAPModel = _WlanAPModel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 5),
    _WlanAPModel_Type()
)
wlanAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPModel.setStatus("current")


class _WlanAPSerialNumber_Type(DisplayString):
    """Custom type wlanAPSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanAPSerialNumber_Type.__name__ = "DisplayString"
_WlanAPSerialNumber_Object = MibTableColumn
wlanAPSerialNumber = _WlanAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 6),
    _WlanAPSerialNumber_Type()
)
wlanAPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSerialNumber.setStatus("current")
_WlanAPdot11aAntennaGain_Type = Integer32
_WlanAPdot11aAntennaGain_Object = MibTableColumn
wlanAPdot11aAntennaGain = _WlanAPdot11aAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 7),
    _WlanAPdot11aAntennaGain_Type()
)
wlanAPdot11aAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPdot11aAntennaGain.setStatus("current")
_WlanAPdot11gAntennaGain_Type = Integer32
_WlanAPdot11gAntennaGain_Object = MibTableColumn
wlanAPdot11gAntennaGain = _WlanAPdot11gAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 8),
    _WlanAPdot11gAntennaGain_Type()
)
wlanAPdot11gAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPdot11gAntennaGain.setStatus("current")
_WlanAPNumRadios_Type = Integer32
_WlanAPNumRadios_Object = MibTableColumn
wlanAPNumRadios = _WlanAPNumRadios_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 9),
    _WlanAPNumRadios_Type()
)
wlanAPNumRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPNumRadios.setStatus("current")
_WlanAPEnet1Mode_Type = ArubaEnet1Mode
_WlanAPEnet1Mode_Object = MibTableColumn
wlanAPEnet1Mode = _WlanAPEnet1Mode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 10),
    _WlanAPEnet1Mode_Type()
)
wlanAPEnet1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPEnet1Mode.setStatus("current")
_WlanAPIpsecMode_Type = ArubaEnableValue
_WlanAPIpsecMode_Object = MibTableColumn
wlanAPIpsecMode = _WlanAPIpsecMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 11),
    _WlanAPIpsecMode_Type()
)
wlanAPIpsecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPIpsecMode.setStatus("current")
_WlanAPUpTime_Type = TimeTicks
_WlanAPUpTime_Object = MibTableColumn
wlanAPUpTime = _WlanAPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 12),
    _WlanAPUpTime_Type()
)
wlanAPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPUpTime.setStatus("current")
_WlanAPModelName_Type = DisplayString
_WlanAPModelName_Object = MibTableColumn
wlanAPModelName = _WlanAPModelName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 13),
    _WlanAPModelName_Type()
)
wlanAPModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPModelName.setStatus("current")
_WlanAPLocation_Type = DisplayString
_WlanAPLocation_Object = MibTableColumn
wlanAPLocation = _WlanAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 14),
    _WlanAPLocation_Type()
)
wlanAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPLocation.setStatus("current")
_WlanAPBuilding_Type = Integer32
_WlanAPBuilding_Object = MibTableColumn
wlanAPBuilding = _WlanAPBuilding_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 15),
    _WlanAPBuilding_Type()
)
wlanAPBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBuilding.setStatus("current")
_WlanAPFloor_Type = Integer32
_WlanAPFloor_Object = MibTableColumn
wlanAPFloor = _WlanAPFloor_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 16),
    _WlanAPFloor_Type()
)
wlanAPFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFloor.setStatus("current")
_WlanAPLoc_Type = Integer32
_WlanAPLoc_Object = MibTableColumn
wlanAPLoc = _WlanAPLoc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 17),
    _WlanAPLoc_Type()
)
wlanAPLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPLoc.setStatus("current")
_WlanAPExternalAntenna_Type = ArubaAntennaSetting
_WlanAPExternalAntenna_Object = MibTableColumn
wlanAPExternalAntenna = _WlanAPExternalAntenna_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 18),
    _WlanAPExternalAntenna_Type()
)
wlanAPExternalAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPExternalAntenna.setStatus("current")
_WlanAPStatus_Type = ArubaAPStatus
_WlanAPStatus_Object = MibTableColumn
wlanAPStatus = _WlanAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 19),
    _WlanAPStatus_Type()
)
wlanAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatus.setStatus("current")
_WlanAPNumBootstraps_Type = Integer32
_WlanAPNumBootstraps_Object = MibTableColumn
wlanAPNumBootstraps = _WlanAPNumBootstraps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 20),
    _WlanAPNumBootstraps_Type()
)
wlanAPNumBootstraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPNumBootstraps.setStatus("current")
_WlanAPNumReboots_Type = Integer32
_WlanAPNumReboots_Object = MibTableColumn
wlanAPNumReboots = _WlanAPNumReboots_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 21),
    _WlanAPNumReboots_Type()
)
wlanAPNumReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPNumReboots.setStatus("current")
_WlanAPUnprovisioned_Type = ArubaUnprovisionedStatus
_WlanAPUnprovisioned_Object = MibTableColumn
wlanAPUnprovisioned = _WlanAPUnprovisioned_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 22),
    _WlanAPUnprovisioned_Type()
)
wlanAPUnprovisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPUnprovisioned.setStatus("current")
_WlanAPMonitorMode_Type = ArubaMonitorMode
_WlanAPMonitorMode_Object = MibTableColumn
wlanAPMonitorMode = _WlanAPMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 23),
    _WlanAPMonitorMode_Type()
)
wlanAPMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPMonitorMode.setStatus("current")
_WlanAPFQLNBuilding_Type = DisplayString
_WlanAPFQLNBuilding_Object = MibTableColumn
wlanAPFQLNBuilding = _WlanAPFQLNBuilding_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 24),
    _WlanAPFQLNBuilding_Type()
)
wlanAPFQLNBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFQLNBuilding.setStatus("current")
_WlanAPFQLNFloor_Type = DisplayString
_WlanAPFQLNFloor_Object = MibTableColumn
wlanAPFQLNFloor = _WlanAPFQLNFloor_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 25),
    _WlanAPFQLNFloor_Type()
)
wlanAPFQLNFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFQLNFloor.setStatus("current")
_WlanAPFQLN_Type = DisplayString
_WlanAPFQLN_Object = MibTableColumn
wlanAPFQLN = _WlanAPFQLN_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 26),
    _WlanAPFQLN_Type()
)
wlanAPFQLN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPFQLN.setStatus("current")
_WlanAPFQLNCampus_Type = DisplayString
_WlanAPFQLNCampus_Object = MibTableColumn
wlanAPFQLNCampus = _WlanAPFQLNCampus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 27),
    _WlanAPFQLNCampus_Type()
)
wlanAPFQLNCampus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFQLNCampus.setStatus("current")
_WlanAPLongitude_Type = DisplayString
_WlanAPLongitude_Object = MibTableColumn
wlanAPLongitude = _WlanAPLongitude_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 28),
    _WlanAPLongitude_Type()
)
wlanAPLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPLongitude.setStatus("current")
_WlanAPLatitude_Type = DisplayString
_WlanAPLatitude_Object = MibTableColumn
wlanAPLatitude = _WlanAPLatitude_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 29),
    _WlanAPLatitude_Type()
)
wlanAPLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPLatitude.setStatus("current")
_WlanAPAltitude_Type = DisplayString
_WlanAPAltitude_Object = MibTableColumn
wlanAPAltitude = _WlanAPAltitude_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 30),
    _WlanAPAltitude_Type()
)
wlanAPAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPAltitude.setStatus("current")
_WlanAPMeshRole_Type = ArubaMeshRole
_WlanAPMeshRole_Object = MibTableColumn
wlanAPMeshRole = _WlanAPMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 31),
    _WlanAPMeshRole_Type()
)
wlanAPMeshRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPMeshRole.setStatus("current")
_WlanAPSysLocation_Type = DisplayString
_WlanAPSysLocation_Object = MibTableColumn
wlanAPSysLocation = _WlanAPSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 32),
    _WlanAPSysLocation_Type()
)
wlanAPSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSysLocation.setStatus("current")


class _WlanAPHwVersion_Type(DisplayString):
    """Custom type wlanAPHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanAPHwVersion_Type.__name__ = "DisplayString"
_WlanAPHwVersion_Object = MibTableColumn
wlanAPHwVersion = _WlanAPHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 33),
    _WlanAPHwVersion_Type()
)
wlanAPHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPHwVersion.setStatus("current")


class _WlanAPSwVersion_Type(DisplayString):
    """Custom type wlanAPSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanAPSwVersion_Type.__name__ = "DisplayString"
_WlanAPSwVersion_Object = MibTableColumn
wlanAPSwVersion = _WlanAPSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 34),
    _WlanAPSwVersion_Type()
)
wlanAPSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSwVersion.setStatus("current")
_WlanAPNumWarmReboots_Type = Integer32
_WlanAPNumWarmReboots_Object = MibTableColumn
wlanAPNumWarmReboots = _WlanAPNumWarmReboots_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 35),
    _WlanAPNumWarmReboots_Type()
)
wlanAPNumWarmReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPNumWarmReboots.setStatus("current")
_WlanAPOuterIpAddress_Type = IpAddress
_WlanAPOuterIpAddress_Object = MibTableColumn
wlanAPOuterIpAddress = _WlanAPOuterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 36),
    _WlanAPOuterIpAddress_Type()
)
wlanAPOuterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPOuterIpAddress.setStatus("current")
_WlanAPRemoteLanIpAddress_Type = IpAddress
_WlanAPRemoteLanIpAddress_Object = MibTableColumn
wlanAPRemoteLanIpAddress = _WlanAPRemoteLanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 37),
    _WlanAPRemoteLanIpAddress_Type()
)
wlanAPRemoteLanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRemoteLanIpAddress.setStatus("current")


class _WlanAPActiveUplink_Type(Integer32):
    """Custom type wlanAPActiveUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("usb", 2),
          ("pppoe", 3))
    )


_WlanAPActiveUplink_Type.__name__ = "Integer32"
_WlanAPActiveUplink_Object = MibTableColumn
wlanAPActiveUplink = _WlanAPActiveUplink_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 38),
    _WlanAPActiveUplink_Type()
)
wlanAPActiveUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPActiveUplink.setStatus("current")
_WlanAPSwitchIpAddress_Type = IpAddress
_WlanAPSwitchIpAddress_Object = MibTableColumn
wlanAPSwitchIpAddress = _WlanAPSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 39),
    _WlanAPSwitchIpAddress_Type()
)
wlanAPSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSwitchIpAddress.setStatus("current")
_WlanAPStandbyIpAddress_Type = IpAddress
_WlanAPStandbyIpAddress_Object = MibTableColumn
wlanAPStandbyIpAddress = _WlanAPStandbyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 40),
    _WlanAPStandbyIpAddress_Type()
)
wlanAPStandbyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStandbyIpAddress.setStatus("current")


class _WlanAPConnectedAsStandby_Type(Integer32):
    """Custom type wlanAPConnectedAsStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1))
    )


_WlanAPConnectedAsStandby_Type.__name__ = "Integer32"
_WlanAPConnectedAsStandby_Object = MibTableColumn
wlanAPConnectedAsStandby = _WlanAPConnectedAsStandby_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 41),
    _WlanAPConnectedAsStandby_Type()
)
wlanAPConnectedAsStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPConnectedAsStandby.setStatus("current")


class _WlanAPServiceTag_Type(DisplayString):
    """Custom type wlanAPServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlanAPServiceTag_Type.__name__ = "DisplayString"
_WlanAPServiceTag_Object = MibTableColumn
wlanAPServiceTag = _WlanAPServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 42),
    _WlanAPServiceTag_Type()
)
wlanAPServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPServiceTag.setStatus("current")


class _WlanAPConnectedAsDatazone_Type(Integer32):
    """Custom type wlanAPConnectedAsDatazone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WlanAPConnectedAsDatazone_Type.__name__ = "Integer32"
_WlanAPConnectedAsDatazone_Object = MibTableColumn
wlanAPConnectedAsDatazone = _WlanAPConnectedAsDatazone_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 43),
    _WlanAPConnectedAsDatazone_Type()
)
wlanAPConnectedAsDatazone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPConnectedAsDatazone.setStatus("current")


class _WlanAPIpv6Address_Type(DisplayString):
    """Custom type wlanAPIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_WlanAPIpv6Address_Type.__name__ = "DisplayString"
_WlanAPIpv6Address_Object = MibTableColumn
wlanAPIpv6Address = _WlanAPIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 44),
    _WlanAPIpv6Address_Type()
)
wlanAPIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPIpv6Address.setStatus("current")
_WlanAPFlexRadioMode_Type = ArubaFlexRadioMode
_WlanAPFlexRadioMode_Object = MibTableColumn
wlanAPFlexRadioMode = _WlanAPFlexRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 45),
    _WlanAPFlexRadioMode_Type()
)
wlanAPFlexRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFlexRadioMode.setStatus("current")
_WlanAPdot11aAntennaGain10x_Type = Integer32
_WlanAPdot11aAntennaGain10x_Object = MibTableColumn
wlanAPdot11aAntennaGain10x = _WlanAPdot11aAntennaGain10x_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 46),
    _WlanAPdot11aAntennaGain10x_Type()
)
wlanAPdot11aAntennaGain10x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPdot11aAntennaGain10x.setStatus("current")
_WlanAPdot11gAntennaGain10x_Type = Integer32
_WlanAPdot11gAntennaGain10x_Object = MibTableColumn
wlanAPdot11gAntennaGain10x = _WlanAPdot11gAntennaGain10x_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 47),
    _WlanAPdot11gAntennaGain10x_Type()
)
wlanAPdot11gAntennaGain10x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPdot11gAntennaGain10x.setStatus("current")
_WlanAPDual5GMode_Type = ArubaDual5GMode
_WlanAPDual5GMode_Object = MibTableColumn
wlanAPDual5GMode = _WlanAPDual5GMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 48),
    _WlanAPDual5GMode_Type()
)
wlanAPDual5GMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPDual5GMode.setStatus("current")


class _WlanAPActiveIpAddress_Type(DisplayString):
    """Custom type wlanAPActiveIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_WlanAPActiveIpAddress_Type.__name__ = "DisplayString"
_WlanAPActiveIpAddress_Object = MibTableColumn
wlanAPActiveIpAddress = _WlanAPActiveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 49),
    _WlanAPActiveIpAddress_Type()
)
wlanAPActiveIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPActiveIpAddress.setStatus("current")
_WlanAPSplit5GMode_Type = ArubaSplit5GMode
_WlanAPSplit5GMode_Object = MibTableColumn
wlanAPSplit5GMode = _WlanAPSplit5GMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 50),
    _WlanAPSplit5GMode_Type()
)
wlanAPSplit5GMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPSplit5GMode.setStatus("current")


class _WlanAPOuterIpv6Address_Type(DisplayString):
    """Custom type wlanAPOuterIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_WlanAPOuterIpv6Address_Type.__name__ = "DisplayString"
_WlanAPOuterIpv6Address_Object = MibTableColumn
wlanAPOuterIpv6Address = _WlanAPOuterIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 51),
    _WlanAPOuterIpv6Address_Type()
)
wlanAPOuterIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPOuterIpv6Address.setStatus("current")


class _WlanAPRemoteLanIpv6Address_Type(DisplayString):
    """Custom type wlanAPRemoteLanIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_WlanAPRemoteLanIpv6Address_Type.__name__ = "DisplayString"
_WlanAPRemoteLanIpv6Address_Object = MibTableColumn
wlanAPRemoteLanIpv6Address = _WlanAPRemoteLanIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 4, 1, 52),
    _WlanAPRemoteLanIpv6Address_Type()
)
wlanAPRemoteLanIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRemoteLanIpv6Address.setStatus("current")
_WlsxWlanRadioTable_Object = MibTable
wlsxWlanRadioTable = _WlsxWlanRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    wlsxWlanRadioTable.setStatus("current")
_WlsxWlanRadioEntry_Object = MibTableRow
wlsxWlanRadioEntry = _WlsxWlanRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1)
)
wlsxWlanRadioEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
)
if mibBuilder.loadTexts:
    wlsxWlanRadioEntry.setStatus("current")
_WlanAPRadioNumber_Type = Integer32
_WlanAPRadioNumber_Object = MibTableColumn
wlanAPRadioNumber = _WlanAPRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 1),
    _WlanAPRadioNumber_Type()
)
wlanAPRadioNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanAPRadioNumber.setStatus("current")
_WlanAPRadioType_Type = ArubaPhyType
_WlanAPRadioType_Object = MibTableColumn
wlanAPRadioType = _WlanAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 2),
    _WlanAPRadioType_Type()
)
wlanAPRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPRadioType.setStatus("current")
_WlanAPRadioChannel_Type = Integer32
_WlanAPRadioChannel_Object = MibTableColumn
wlanAPRadioChannel = _WlanAPRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 3),
    _WlanAPRadioChannel_Type()
)
wlanAPRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioChannel.setStatus("current")
_WlanAPRadioTransmitPower_Type = Integer32
_WlanAPRadioTransmitPower_Object = MibTableColumn
wlanAPRadioTransmitPower = _WlanAPRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 4),
    _WlanAPRadioTransmitPower_Type()
)
wlanAPRadioTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTransmitPower.setStatus("current")
_WlanAPRadioMode_Type = ArubaAccessPointMode
_WlanAPRadioMode_Object = MibTableColumn
wlanAPRadioMode = _WlanAPRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 5),
    _WlanAPRadioMode_Type()
)
wlanAPRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioMode.setStatus("current")
_WlanAPRadioUtilization_Type = Integer32
_WlanAPRadioUtilization_Object = MibTableColumn
wlanAPRadioUtilization = _WlanAPRadioUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 6),
    _WlanAPRadioUtilization_Type()
)
wlanAPRadioUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioUtilization.setStatus("current")
_WlanAPRadioNumAssociatedClients_Type = Integer32
_WlanAPRadioNumAssociatedClients_Object = MibTableColumn
wlanAPRadioNumAssociatedClients = _WlanAPRadioNumAssociatedClients_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 7),
    _WlanAPRadioNumAssociatedClients_Type()
)
wlanAPRadioNumAssociatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioNumAssociatedClients.setStatus("current")
_WlanAPRadioNumMonitoredClients_Type = Integer32
_WlanAPRadioNumMonitoredClients_Object = MibTableColumn
wlanAPRadioNumMonitoredClients = _WlanAPRadioNumMonitoredClients_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 8),
    _WlanAPRadioNumMonitoredClients_Type()
)
wlanAPRadioNumMonitoredClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioNumMonitoredClients.setStatus("current")
_WlanAPRadioNumActiveBSSIDs_Type = Integer32
_WlanAPRadioNumActiveBSSIDs_Object = MibTableColumn
wlanAPRadioNumActiveBSSIDs = _WlanAPRadioNumActiveBSSIDs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 9),
    _WlanAPRadioNumActiveBSSIDs_Type()
)
wlanAPRadioNumActiveBSSIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioNumActiveBSSIDs.setStatus("current")
_WlanAPRadioNumMonitoredBSSIDs_Type = Integer32
_WlanAPRadioNumMonitoredBSSIDs_Object = MibTableColumn
wlanAPRadioNumMonitoredBSSIDs = _WlanAPRadioNumMonitoredBSSIDs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 10),
    _WlanAPRadioNumMonitoredBSSIDs_Type()
)
wlanAPRadioNumMonitoredBSSIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioNumMonitoredBSSIDs.setStatus("current")
_WlanAPRadioBearing_Type = DisplayString
_WlanAPRadioBearing_Object = MibTableColumn
wlanAPRadioBearing = _WlanAPRadioBearing_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 11),
    _WlanAPRadioBearing_Type()
)
wlanAPRadioBearing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPRadioBearing.setStatus("current")
_WlanAPRadioTiltAngle_Type = DisplayString
_WlanAPRadioTiltAngle_Object = MibTableColumn
wlanAPRadioTiltAngle = _WlanAPRadioTiltAngle_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 12),
    _WlanAPRadioTiltAngle_Type()
)
wlanAPRadioTiltAngle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPRadioTiltAngle.setStatus("current")
_WlanAPRadioHTMode_Type = ArubaHTMode
_WlanAPRadioHTMode_Object = MibTableColumn
wlanAPRadioHTMode = _WlanAPRadioHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 13),
    _WlanAPRadioHTMode_Type()
)
wlanAPRadioHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioHTMode.setStatus("current")
_WlanAPRadioHTExtChannel_Type = ArubaHTExtChannel
_WlanAPRadioHTExtChannel_Object = MibTableColumn
wlanAPRadioHTExtChannel = _WlanAPRadioHTExtChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 14),
    _WlanAPRadioHTExtChannel_Type()
)
wlanAPRadioHTExtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioHTExtChannel.setStatus("current")
_WlanAPRadioHTChannel_Type = DisplayString
_WlanAPRadioHTChannel_Object = MibTableColumn
wlanAPRadioHTChannel = _WlanAPRadioHTChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 15),
    _WlanAPRadioHTChannel_Type()
)
wlanAPRadioHTChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPRadioHTChannel.setStatus("current")
_WlanAPRadioAPName_Type = DisplayString
_WlanAPRadioAPName_Object = MibTableColumn
wlanAPRadioAPName = _WlanAPRadioAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 16),
    _WlanAPRadioAPName_Type()
)
wlanAPRadioAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAPRadioAPName.setStatus("current")
_WlanAPRadioTransmitPower10x_Type = Integer32
_WlanAPRadioTransmitPower10x_Object = MibTableColumn
wlanAPRadioTransmitPower10x = _WlanAPRadioTransmitPower10x_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 17),
    _WlanAPRadioTransmitPower10x_Type()
)
wlanAPRadioTransmitPower10x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTransmitPower10x.setStatus("current")
_WlanAPRadioSecChannel_Type = Integer32
_WlanAPRadioSecChannel_Object = MibTableColumn
wlanAPRadioSecChannel = _WlanAPRadioSecChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 5, 1, 18),
    _WlanAPRadioSecChannel_Type()
)
wlanAPRadioSecChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioSecChannel.setStatus("current")
_WlsxWlanAPBssidTable_Object = MibTable
wlsxWlanAPBssidTable = _WlsxWlanAPBssidTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    wlsxWlanAPBssidTable.setStatus("current")
_WlsxWlanAPBssidEntry_Object = MibTableRow
wlsxWlanAPBssidEntry = _WlsxWlanAPBssidEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1)
)
wlsxWlanAPBssidEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPBssidEntry.setStatus("current")
_WlanAPBSSID_Type = MacAddress
_WlanAPBSSID_Object = MibTableColumn
wlanAPBSSID = _WlanAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 1),
    _WlanAPBSSID_Type()
)
wlanAPBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanAPBSSID.setStatus("current")


class _WlanAPESSID_Type(DisplayString):
    """Custom type wlanAPESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanAPESSID_Type.__name__ = "DisplayString"
_WlanAPESSID_Object = MibTableColumn
wlanAPESSID = _WlanAPESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 2),
    _WlanAPESSID_Type()
)
wlanAPESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPESSID.setStatus("current")
_WlanAPBssidSlot_Type = Unsigned32
_WlanAPBssidSlot_Object = MibTableColumn
wlanAPBssidSlot = _WlanAPBssidSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 3),
    _WlanAPBssidSlot_Type()
)
wlanAPBssidSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidSlot.setStatus("current")
_WlanAPBssidPort_Type = Unsigned32
_WlanAPBssidPort_Object = MibTableColumn
wlanAPBssidPort = _WlanAPBssidPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 4),
    _WlanAPBssidPort_Type()
)
wlanAPBssidPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidPort.setStatus("current")
_WlanAPBssidPhyType_Type = ArubaPhyType
_WlanAPBssidPhyType_Object = MibTableColumn
wlanAPBssidPhyType = _WlanAPBssidPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 5),
    _WlanAPBssidPhyType_Type()
)
wlanAPBssidPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidPhyType.setStatus("current")
_WlanAPBssidRogueType_Type = ArubaRogueApType
_WlanAPBssidRogueType_Object = MibTableColumn
wlanAPBssidRogueType = _WlanAPBssidRogueType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 6),
    _WlanAPBssidRogueType_Type()
)
wlanAPBssidRogueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidRogueType.setStatus("current")


class _WlanAPBssidMode_Type(Integer32):
    """Custom type wlanAPBssidMode based on Integer32"""
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
        *(("ap", 1),
          ("am", 2),
          ("mpp", 3),
          ("mp", 4))
    )


_WlanAPBssidMode_Type.__name__ = "Integer32"
_WlanAPBssidMode_Object = MibTableColumn
wlanAPBssidMode = _WlanAPBssidMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 7),
    _WlanAPBssidMode_Type()
)
wlanAPBssidMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidMode.setStatus("current")


class _WlanAPBssidChannel_Type(Integer32):
    """Custom type wlanAPBssidChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_WlanAPBssidChannel_Type.__name__ = "Integer32"
_WlanAPBssidChannel_Object = MibTableColumn
wlanAPBssidChannel = _WlanAPBssidChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 8),
    _WlanAPBssidChannel_Type()
)
wlanAPBssidChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidChannel.setStatus("deprecated")
_WlanAPBssidUpTime_Type = TimeTicks
_WlanAPBssidUpTime_Object = MibTableColumn
wlanAPBssidUpTime = _WlanAPBssidUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 9),
    _WlanAPBssidUpTime_Type()
)
wlanAPBssidUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidUpTime.setStatus("current")
_WlanAPBssidInactiveTime_Type = TimeTicks
_WlanAPBssidInactiveTime_Object = MibTableColumn
wlanAPBssidInactiveTime = _WlanAPBssidInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 10),
    _WlanAPBssidInactiveTime_Type()
)
wlanAPBssidInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidInactiveTime.setStatus("current")
_WlanAPBssidLoadBalancing_Type = TruthValue
_WlanAPBssidLoadBalancing_Object = MibTableColumn
wlanAPBssidLoadBalancing = _WlanAPBssidLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 11),
    _WlanAPBssidLoadBalancing_Type()
)
wlanAPBssidLoadBalancing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidLoadBalancing.setStatus("current")
_WlanAPBssidNumAssociatedStations_Type = Unsigned32
_WlanAPBssidNumAssociatedStations_Object = MibTableColumn
wlanAPBssidNumAssociatedStations = _WlanAPBssidNumAssociatedStations_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 12),
    _WlanAPBssidNumAssociatedStations_Type()
)
wlanAPBssidNumAssociatedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidNumAssociatedStations.setStatus("current")
_WlanAPBssidAPMacAddress_Type = MacAddress
_WlanAPBssidAPMacAddress_Object = MibTableColumn
wlanAPBssidAPMacAddress = _WlanAPBssidAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 13),
    _WlanAPBssidAPMacAddress_Type()
)
wlanAPBssidAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidAPMacAddress.setStatus("current")
_WlanAPBssidPhyNumber_Type = Integer32
_WlanAPBssidPhyNumber_Object = MibTableColumn
wlanAPBssidPhyNumber = _WlanAPBssidPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 14),
    _WlanAPBssidPhyNumber_Type()
)
wlanAPBssidPhyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidPhyNumber.setStatus("current")
_WlanAPBssidHTMode_Type = ArubaHTMode
_WlanAPBssidHTMode_Object = MibTableColumn
wlanAPBssidHTMode = _WlanAPBssidHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 15),
    _WlanAPBssidHTMode_Type()
)
wlanAPBssidHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidHTMode.setStatus("current")
_WlanAPBssidHTExtChannel_Type = ArubaHTExtChannel
_WlanAPBssidHTExtChannel_Object = MibTableColumn
wlanAPBssidHTExtChannel = _WlanAPBssidHTExtChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 16),
    _WlanAPBssidHTExtChannel_Type()
)
wlanAPBssidHTExtChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidHTExtChannel.setStatus("current")
_WlanAPBssidHTChannel_Type = DisplayString
_WlanAPBssidHTChannel_Object = MibTableColumn
wlanAPBssidHTChannel = _WlanAPBssidHTChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 17),
    _WlanAPBssidHTChannel_Type()
)
wlanAPBssidHTChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidHTChannel.setStatus("current")
_WlanAPBssidSnr_Type = Integer32
_WlanAPBssidSnr_Object = MibTableColumn
wlanAPBssidSnr = _WlanAPBssidSnr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 18),
    _WlanAPBssidSnr_Type()
)
wlanAPBssidSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidSnr.setStatus("current")
_WlanAPBssidChannelV2_Type = Integer32
_WlanAPBssidChannelV2_Object = MibTableColumn
wlanAPBssidChannelV2 = _WlanAPBssidChannelV2_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 19),
    _WlanAPBssidChannelV2_Type()
)
wlanAPBssidChannelV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidChannelV2.setStatus("current")
_WlanAPBssidSecChannel_Type = Integer32
_WlanAPBssidSecChannel_Object = MibTableColumn
wlanAPBssidSecChannel = _WlanAPBssidSecChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 7, 1, 20),
    _WlanAPBssidSecChannel_Type()
)
wlanAPBssidSecChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPBssidSecChannel.setStatus("current")
_WlsxWlanESSIDTable_Object = MibTable
wlsxWlanESSIDTable = _WlsxWlanESSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    wlsxWlanESSIDTable.setStatus("current")
_WlsxWlanESSIDEntry_Object = MibTableRow
wlsxWlanESSIDEntry = _WlsxWlanESSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8, 1)
)
wlsxWlanESSIDEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanESSIDEntry.setStatus("current")


class _WlanESSID_Type(DisplayString):
    """Custom type wlanESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanESSID_Type.__name__ = "DisplayString"
_WlanESSID_Object = MibTableColumn
wlanESSID = _WlanESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8, 1, 1),
    _WlanESSID_Type()
)
wlanESSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanESSID.setStatus("current")
_WlanESSIDNumStations_Type = Unsigned32
_WlanESSIDNumStations_Object = MibTableColumn
wlanESSIDNumStations = _WlanESSIDNumStations_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8, 1, 2),
    _WlanESSIDNumStations_Type()
)
wlanESSIDNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDNumStations.setStatus("current")
_WlanESSIDNumAccessPointsUp_Type = Unsigned32
_WlanESSIDNumAccessPointsUp_Object = MibTableColumn
wlanESSIDNumAccessPointsUp = _WlanESSIDNumAccessPointsUp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8, 1, 3),
    _WlanESSIDNumAccessPointsUp_Type()
)
wlanESSIDNumAccessPointsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDNumAccessPointsUp.setStatus("current")
_WlanESSIDNumAccessPointsDown_Type = Unsigned32
_WlanESSIDNumAccessPointsDown_Object = MibTableColumn
wlanESSIDNumAccessPointsDown = _WlanESSIDNumAccessPointsDown_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8, 1, 4),
    _WlanESSIDNumAccessPointsDown_Type()
)
wlanESSIDNumAccessPointsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDNumAccessPointsDown.setStatus("current")
_WlanESSIDEncryptionType_Type = ArubaEncryptionMethods
_WlanESSIDEncryptionType_Object = MibTableColumn
wlanESSIDEncryptionType = _WlanESSIDEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 8, 1, 5),
    _WlanESSIDEncryptionType_Type()
)
wlanESSIDEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDEncryptionType.setStatus("current")
_WlsxWlanESSIDVlanPoolTable_Object = MibTable
wlsxWlanESSIDVlanPoolTable = _WlsxWlanESSIDVlanPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    wlsxWlanESSIDVlanPoolTable.setStatus("current")
_WlsxWlanESSIDVlanPoolEntry_Object = MibTableRow
wlsxWlanESSIDVlanPoolEntry = _WlsxWlanESSIDVlanPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 9, 1)
)
wlsxWlanESSIDVlanPoolEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
    (0, "WLSX-WLAN-MIB", "wlanESSIDVlanId"),
)
if mibBuilder.loadTexts:
    wlsxWlanESSIDVlanPoolEntry.setStatus("current")
_WlanESSIDVlanId_Type = Unsigned32
_WlanESSIDVlanId_Object = MibTableColumn
wlanESSIDVlanId = _WlanESSIDVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 9, 1, 1),
    _WlanESSIDVlanId_Type()
)
wlanESSIDVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanESSIDVlanId.setStatus("current")
_WlanESSIDVlanPoolStatus_Type = RowStatus
_WlanESSIDVlanPoolStatus_Object = MibTableColumn
wlanESSIDVlanPoolStatus = _WlanESSIDVlanPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 1, 9, 1, 2),
    _WlanESSIDVlanPoolStatus_Type()
)
wlanESSIDVlanPoolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanESSIDVlanPoolStatus.setStatus("current")
_WlsxWlanStationInfoGroup_ObjectIdentity = ObjectIdentity
wlsxWlanStationInfoGroup = _WlsxWlanStationInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2)
)
_WlsxWlanStationTable_Object = MibTable
wlsxWlanStationTable = _WlsxWlanStationTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wlsxWlanStationTable.setStatus("current")
_WlsxWlanStationEntry_Object = MibTableRow
wlsxWlanStationEntry = _WlsxWlanStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1)
)
wlsxWlanStationEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanStationEntry.setStatus("current")
_WlanStaPhyAddress_Type = MacAddress
_WlanStaPhyAddress_Object = MibTableColumn
wlanStaPhyAddress = _WlanStaPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 1),
    _WlanStaPhyAddress_Type()
)
wlanStaPhyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanStaPhyAddress.setStatus("current")
_WlanStaApBssid_Type = MacAddress
_WlanStaApBssid_Object = MibTableColumn
wlanStaApBssid = _WlanStaApBssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 2),
    _WlanStaApBssid_Type()
)
wlanStaApBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaApBssid.setStatus("current")
_WlanStaPhyType_Type = ArubaPhyType
_WlanStaPhyType_Object = MibTableColumn
wlanStaPhyType = _WlanStaPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 3),
    _WlanStaPhyType_Type()
)
wlanStaPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaPhyType.setStatus("current")
_WlanStaIsAuthenticated_Type = TruthValue
_WlanStaIsAuthenticated_Object = MibTableColumn
wlanStaIsAuthenticated = _WlanStaIsAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 4),
    _WlanStaIsAuthenticated_Type()
)
wlanStaIsAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaIsAuthenticated.setStatus("current")
_WlanStaIsAssociated_Type = TruthValue
_WlanStaIsAssociated_Object = MibTableColumn
wlanStaIsAssociated = _WlanStaIsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 5),
    _WlanStaIsAssociated_Type()
)
wlanStaIsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaIsAssociated.setStatus("current")


class _WlanStaChannel_Type(Integer32):
    """Custom type wlanStaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_WlanStaChannel_Type.__name__ = "Integer32"
_WlanStaChannel_Object = MibTableColumn
wlanStaChannel = _WlanStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 6),
    _WlanStaChannel_Type()
)
wlanStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaChannel.setStatus("deprecated")
_WlanStaVlanId_Type = ArubaVlanValidRange
_WlanStaVlanId_Object = MibTableColumn
wlanStaVlanId = _WlanStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 7),
    _WlanStaVlanId_Type()
)
wlanStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaVlanId.setStatus("current")
_WlanStaVOIPState_Type = TruthValue
_WlanStaVOIPState_Object = MibTableColumn
wlanStaVOIPState = _WlanStaVOIPState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 8),
    _WlanStaVOIPState_Type()
)
wlanStaVOIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaVOIPState.setStatus("current")
_WlanStaVOIPProtocol_Type = ArubaVoipProtocolType
_WlanStaVOIPProtocol_Object = MibTableColumn
wlanStaVOIPProtocol = _WlanStaVOIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 9),
    _WlanStaVOIPProtocol_Type()
)
wlanStaVOIPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaVOIPProtocol.setStatus("current")
_WlanStaTransmitRate_Type = Unsigned32
_WlanStaTransmitRate_Object = MibTableColumn
wlanStaTransmitRate = _WlanStaTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 10),
    _WlanStaTransmitRate_Type()
)
wlanStaTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTransmitRate.setStatus("current")
_WlanStaAssociationID_Type = Unsigned32
_WlanStaAssociationID_Object = MibTableColumn
wlanStaAssociationID = _WlanStaAssociationID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 11),
    _WlanStaAssociationID_Type()
)
wlanStaAssociationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssociationID.setStatus("current")


class _WlanStaAccessPointESSID_Type(DisplayString):
    """Custom type wlanStaAccessPointESSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanStaAccessPointESSID_Type.__name__ = "DisplayString"
_WlanStaAccessPointESSID_Object = MibTableColumn
wlanStaAccessPointESSID = _WlanStaAccessPointESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 12),
    _WlanStaAccessPointESSID_Type()
)
wlanStaAccessPointESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAccessPointESSID.setStatus("current")
_WlanStaPhyNumber_Type = Integer32
_WlanStaPhyNumber_Object = MibTableColumn
wlanStaPhyNumber = _WlanStaPhyNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 13),
    _WlanStaPhyNumber_Type()
)
wlanStaPhyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaPhyNumber.setStatus("current")
_WlanStaRSSI_Type = Integer32
_WlanStaRSSI_Object = MibTableColumn
wlanStaRSSI = _WlanStaRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 14),
    _WlanStaRSSI_Type()
)
wlanStaRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRSSI.setStatus("current")
_WlanStaUpTime_Type = TimeTicks
_WlanStaUpTime_Object = MibTableColumn
wlanStaUpTime = _WlanStaUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 15),
    _WlanStaUpTime_Type()
)
wlanStaUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaUpTime.setStatus("current")
_WlanStaHTMode_Type = ArubaHTMode
_WlanStaHTMode_Object = MibTableColumn
wlanStaHTMode = _WlanStaHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 16),
    _WlanStaHTMode_Type()
)
wlanStaHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaHTMode.setStatus("current")
_WlanStaTransmitRateCode_Type = Unsigned32
_WlanStaTransmitRateCode_Object = MibTableColumn
wlanStaTransmitRateCode = _WlanStaTransmitRateCode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 17),
    _WlanStaTransmitRateCode_Type()
)
wlanStaTransmitRateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTransmitRateCode.setStatus("current")
_WlanStaChannelV2_Type = Integer32
_WlanStaChannelV2_Object = MibTableColumn
wlanStaChannelV2 = _WlanStaChannelV2_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 18),
    _WlanStaChannelV2_Type()
)
wlanStaChannelV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaChannelV2.setStatus("current")
_WlanStaSecChannel_Type = Integer32
_WlanStaSecChannel_Object = MibTableColumn
wlanStaSecChannel = _WlanStaSecChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 19),
    _WlanStaSecChannel_Type()
)
wlanStaSecChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaSecChannel.setStatus("current")


class _WlanStaApName_Type(DisplayString):
    """Custom type wlanStaApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanStaApName_Type.__name__ = "DisplayString"
_WlanStaApName_Object = MibTableColumn
wlanStaApName = _WlanStaApName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 1, 1, 20),
    _WlanStaApName_Type()
)
wlanStaApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaApName.setStatus("current")
_WlsxWlanStaAssociationFailureTable_Object = MibTable
wlsxWlanStaAssociationFailureTable = _WlsxWlanStaAssociationFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    wlsxWlanStaAssociationFailureTable.setStatus("current")
_WlsxWlanStaAssociationFailureEntry_Object = MibTableRow
wlsxWlanStaAssociationFailureEntry = _WlsxWlanStaAssociationFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1)
)
wlsxWlanStaAssociationFailureEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanStaAssociationFailureEntry.setStatus("current")


class _WlanStaAssocFailureApName_Type(DisplayString):
    """Custom type wlanStaAssocFailureApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanStaAssocFailureApName_Type.__name__ = "DisplayString"
_WlanStaAssocFailureApName_Object = MibTableColumn
wlanStaAssocFailureApName = _WlanStaAssocFailureApName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1, 1),
    _WlanStaAssocFailureApName_Type()
)
wlanStaAssocFailureApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssocFailureApName.setStatus("current")


class _WlanStaAssocFailureApEssid_Type(DisplayString):
    """Custom type wlanStaAssocFailureApEssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanStaAssocFailureApEssid_Type.__name__ = "DisplayString"
_WlanStaAssocFailureApEssid_Object = MibTableColumn
wlanStaAssocFailureApEssid = _WlanStaAssocFailureApEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1, 2),
    _WlanStaAssocFailureApEssid_Type()
)
wlanStaAssocFailureApEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssocFailureApEssid.setStatus("current")
_WlanStaAssocFailurePhyNum_Type = Integer32
_WlanStaAssocFailurePhyNum_Object = MibTableColumn
wlanStaAssocFailurePhyNum = _WlanStaAssocFailurePhyNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1, 3),
    _WlanStaAssocFailurePhyNum_Type()
)
wlanStaAssocFailurePhyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssocFailurePhyNum.setStatus("current")
_WlanStaAssocFailurePhyType_Type = ArubaPhyType
_WlanStaAssocFailurePhyType_Object = MibTableColumn
wlanStaAssocFailurePhyType = _WlanStaAssocFailurePhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1, 4),
    _WlanStaAssocFailurePhyType_Type()
)
wlanStaAssocFailurePhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssocFailurePhyType.setStatus("current")
_WlanStaAssocFailureElapsedTime_Type = TimeTicks
_WlanStaAssocFailureElapsedTime_Object = MibTableColumn
wlanStaAssocFailureElapsedTime = _WlanStaAssocFailureElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1, 5),
    _WlanStaAssocFailureElapsedTime_Type()
)
wlanStaAssocFailureElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssocFailureElapsedTime.setStatus("current")


class _WlanStaAssocFailureReason_Type(DisplayString):
    """Custom type wlanStaAssocFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_WlanStaAssocFailureReason_Type.__name__ = "DisplayString"
_WlanStaAssocFailureReason_Object = MibTableColumn
wlanStaAssocFailureReason = _WlanStaAssocFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 2, 2, 1, 6),
    _WlanStaAssocFailureReason_Type()
)
wlanStaAssocFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaAssocFailureReason.setStatus("current")
_WlsxWlanAssociationInfoGroup_ObjectIdentity = ObjectIdentity
wlsxWlanAssociationInfoGroup = _WlsxWlanAssociationInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 2, 3)
)
_WlsxWlanStatsGroup_ObjectIdentity = ObjectIdentity
wlsxWlanStatsGroup = _WlsxWlanStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3)
)
_WlsxWlanAccessPointStatsGroup_ObjectIdentity = ObjectIdentity
wlsxWlanAccessPointStatsGroup = _WlsxWlanAccessPointStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1)
)
_WlsxWlanAPStatsTable_Object = MibTable
wlsxWlanAPStatsTable = _WlsxWlanAPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxWlanAPStatsTable.setStatus("current")
_WlsxWlanAPStatsEntry_Object = MibTableRow
wlsxWlanAPStatsEntry = _WlsxWlanAPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1)
)
wlsxWlanAPStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPStatsEntry.setStatus("current")
_WlanAPCurrentChannel_Type = Unsigned32
_WlanAPCurrentChannel_Object = MibTableColumn
wlanAPCurrentChannel = _WlanAPCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 1),
    _WlanAPCurrentChannel_Type()
)
wlanAPCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPCurrentChannel.setStatus("current")
_WlanAPNumClients_Type = Integer32
_WlanAPNumClients_Object = MibTableColumn
wlanAPNumClients = _WlanAPNumClients_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 2),
    _WlanAPNumClients_Type()
)
wlanAPNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPNumClients.setStatus("current")
_WlanAPTxPkts_Type = Counter32
_WlanAPTxPkts_Object = MibTableColumn
wlanAPTxPkts = _WlanAPTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 3),
    _WlanAPTxPkts_Type()
)
wlanAPTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxPkts.setStatus("current")
_WlanAPTxBytes_Type = Counter32
_WlanAPTxBytes_Object = MibTableColumn
wlanAPTxBytes = _WlanAPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 4),
    _WlanAPTxBytes_Type()
)
wlanAPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxBytes.setStatus("current")
_WlanAPRxPkts_Type = Counter32
_WlanAPRxPkts_Object = MibTableColumn
wlanAPRxPkts = _WlanAPRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 5),
    _WlanAPRxPkts_Type()
)
wlanAPRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxPkts.setStatus("current")
_WlanAPRxBytes_Type = Counter32
_WlanAPRxBytes_Object = MibTableColumn
wlanAPRxBytes = _WlanAPRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 6),
    _WlanAPRxBytes_Type()
)
wlanAPRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxBytes.setStatus("current")
_WlanAPTxDeauthentications_Type = Counter32
_WlanAPTxDeauthentications_Object = MibTableColumn
wlanAPTxDeauthentications = _WlanAPTxDeauthentications_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 7),
    _WlanAPTxDeauthentications_Type()
)
wlanAPTxDeauthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxDeauthentications.setStatus("current")
_WlanAPRxDeauthentications_Type = Counter32
_WlanAPRxDeauthentications_Object = MibTableColumn
wlanAPRxDeauthentications = _WlanAPRxDeauthentications_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 8),
    _WlanAPRxDeauthentications_Type()
)
wlanAPRxDeauthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxDeauthentications.setStatus("current")
_WlanAPChannelThroughput_Type = Integer32
_WlanAPChannelThroughput_Object = MibTableColumn
wlanAPChannelThroughput = _WlanAPChannelThroughput_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 9),
    _WlanAPChannelThroughput_Type()
)
wlanAPChannelThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChannelThroughput.setStatus("current")
_WlanAPFrameRetryRate_Type = Integer32
_WlanAPFrameRetryRate_Object = MibTableColumn
wlanAPFrameRetryRate = _WlanAPFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 10),
    _WlanAPFrameRetryRate_Type()
)
wlanAPFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameRetryRate.setStatus("current")
_WlanAPFrameLowSpeedRate_Type = Integer32
_WlanAPFrameLowSpeedRate_Object = MibTableColumn
wlanAPFrameLowSpeedRate = _WlanAPFrameLowSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 11),
    _WlanAPFrameLowSpeedRate_Type()
)
wlanAPFrameLowSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameLowSpeedRate.setStatus("current")
_WlanAPFrameNonUnicastRate_Type = Integer32
_WlanAPFrameNonUnicastRate_Object = MibTableColumn
wlanAPFrameNonUnicastRate = _WlanAPFrameNonUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 12),
    _WlanAPFrameNonUnicastRate_Type()
)
wlanAPFrameNonUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameNonUnicastRate.setStatus("current")
_WlanAPFrameFragmentationRate_Type = Integer32
_WlanAPFrameFragmentationRate_Object = MibTableColumn
wlanAPFrameFragmentationRate = _WlanAPFrameFragmentationRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 13),
    _WlanAPFrameFragmentationRate_Type()
)
wlanAPFrameFragmentationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameFragmentationRate.setStatus("current")
_WlanAPFrameBandwidthRate_Type = Integer32
_WlanAPFrameBandwidthRate_Object = MibTableColumn
wlanAPFrameBandwidthRate = _WlanAPFrameBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 14),
    _WlanAPFrameBandwidthRate_Type()
)
wlanAPFrameBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameBandwidthRate.setStatus("current")
_WlanAPFrameRetryErrorRate_Type = Integer32
_WlanAPFrameRetryErrorRate_Object = MibTableColumn
wlanAPFrameRetryErrorRate = _WlanAPFrameRetryErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 15),
    _WlanAPFrameRetryErrorRate_Type()
)
wlanAPFrameRetryErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameRetryErrorRate.setStatus("current")
_WlanAPChannelErrorRate_Type = Integer32
_WlanAPChannelErrorRate_Object = MibTableColumn
wlanAPChannelErrorRate = _WlanAPChannelErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 16),
    _WlanAPChannelErrorRate_Type()
)
wlanAPChannelErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChannelErrorRate.setStatus("current")
_WlanAPFrameReceiveErrorRate_Type = Integer32
_WlanAPFrameReceiveErrorRate_Object = MibTableColumn
wlanAPFrameReceiveErrorRate = _WlanAPFrameReceiveErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 17),
    _WlanAPFrameReceiveErrorRate_Type()
)
wlanAPFrameReceiveErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPFrameReceiveErrorRate.setStatus("current")
_WlanAPRxDataPkts_Type = Counter32
_WlanAPRxDataPkts_Object = MibTableColumn
wlanAPRxDataPkts = _WlanAPRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 18),
    _WlanAPRxDataPkts_Type()
)
wlanAPRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxDataPkts.setStatus("deprecated")
_WlanAPRxDataBytes_Type = Counter32
_WlanAPRxDataBytes_Object = MibTableColumn
wlanAPRxDataBytes = _WlanAPRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 19),
    _WlanAPRxDataBytes_Type()
)
wlanAPRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxDataBytes.setStatus("deprecated")
_WlanAPTxDataPkts_Type = Counter32
_WlanAPTxDataPkts_Object = MibTableColumn
wlanAPTxDataPkts = _WlanAPTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 20),
    _WlanAPTxDataPkts_Type()
)
wlanAPTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxDataPkts.setStatus("deprecated")
_WlanAPTxDataBytes_Type = Counter32
_WlanAPTxDataBytes_Object = MibTableColumn
wlanAPTxDataBytes = _WlanAPTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 21),
    _WlanAPTxDataBytes_Type()
)
wlanAPTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxDataBytes.setStatus("deprecated")
_WlanAPRxDataPkts64_Type = Counter64
_WlanAPRxDataPkts64_Object = MibTableColumn
wlanAPRxDataPkts64 = _WlanAPRxDataPkts64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 22),
    _WlanAPRxDataPkts64_Type()
)
wlanAPRxDataPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxDataPkts64.setStatus("current")
_WlanAPRxDataBytes64_Type = Counter64
_WlanAPRxDataBytes64_Object = MibTableColumn
wlanAPRxDataBytes64 = _WlanAPRxDataBytes64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 23),
    _WlanAPRxDataBytes64_Type()
)
wlanAPRxDataBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxDataBytes64.setStatus("current")
_WlanAPTxDataPkts64_Type = Counter64
_WlanAPTxDataPkts64_Object = MibTableColumn
wlanAPTxDataPkts64 = _WlanAPTxDataPkts64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 24),
    _WlanAPTxDataPkts64_Type()
)
wlanAPTxDataPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxDataPkts64.setStatus("current")
_WlanAPTxDataBytes64_Type = Counter64
_WlanAPTxDataBytes64_Object = MibTableColumn
wlanAPTxDataBytes64 = _WlanAPTxDataBytes64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 25),
    _WlanAPTxDataBytes64_Type()
)
wlanAPTxDataBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTxDataBytes64.setStatus("current")
_WlanAPWiredRxErrorPkts_Type = Counter32
_WlanAPWiredRxErrorPkts_Object = MibTableColumn
wlanAPWiredRxErrorPkts = _WlanAPWiredRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 26),
    _WlanAPWiredRxErrorPkts_Type()
)
wlanAPWiredRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredRxErrorPkts.setStatus("current")
_WlanAPRxErrorPkts_Type = Counter32
_WlanAPRxErrorPkts_Object = MibTableColumn
wlanAPRxErrorPkts = _WlanAPRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 27),
    _WlanAPRxErrorPkts_Type()
)
wlanAPRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRxErrorPkts.setStatus("current")
_WlanAPHTMode_Type = ArubaHTMode
_WlanAPHTMode_Object = MibTableColumn
wlanAPHTMode = _WlanAPHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 28),
    _WlanAPHTMode_Type()
)
wlanAPHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPHTMode.setStatus("current")
_WlanAPPhyType_Type = ArubaPhyType
_WlanAPPhyType_Object = MibTableColumn
wlanAPPhyType = _WlanAPPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 29),
    _WlanAPPhyType_Type()
)
wlanAPPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPPhyType.setStatus("current")
_WlanAPCurrentSecChannel_Type = Unsigned32
_WlanAPCurrentSecChannel_Object = MibTableColumn
wlanAPCurrentSecChannel = _WlanAPCurrentSecChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 1, 1, 30),
    _WlanAPCurrentSecChannel_Type()
)
wlanAPCurrentSecChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPCurrentSecChannel.setStatus("current")
_WlsxWlanAPRateStatsTable_Object = MibTable
wlsxWlanAPRateStatsTable = _WlsxWlanAPRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxWlanAPRateStatsTable.setStatus("current")
_WlsxWlanAPRateStatsEntry_Object = MibTableRow
wlsxWlanAPRateStatsEntry = _WlsxWlanAPRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1)
)
wlsxWlanAPRateStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPRateStatsEntry.setStatus("current")
_WlanAPStatsTotPktsAt1Mbps_Type = Counter32
_WlanAPStatsTotPktsAt1Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt1Mbps = _WlanAPStatsTotPktsAt1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 1),
    _WlanAPStatsTotPktsAt1Mbps_Type()
)
wlanAPStatsTotPktsAt1Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt1Mbps.setStatus("current")
_WlanAPStatsTotBytesAt1Mbps_Type = Counter32
_WlanAPStatsTotBytesAt1Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt1Mbps = _WlanAPStatsTotBytesAt1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 2),
    _WlanAPStatsTotBytesAt1Mbps_Type()
)
wlanAPStatsTotBytesAt1Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt1Mbps.setStatus("current")
_WlanAPStatsTotPktsAt2Mbps_Type = Counter32
_WlanAPStatsTotPktsAt2Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt2Mbps = _WlanAPStatsTotPktsAt2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 3),
    _WlanAPStatsTotPktsAt2Mbps_Type()
)
wlanAPStatsTotPktsAt2Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt2Mbps.setStatus("current")
_WlanAPStatsTotBytesAt2Mbps_Type = Counter32
_WlanAPStatsTotBytesAt2Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt2Mbps = _WlanAPStatsTotBytesAt2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 4),
    _WlanAPStatsTotBytesAt2Mbps_Type()
)
wlanAPStatsTotBytesAt2Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt2Mbps.setStatus("current")
_WlanAPStatsTotPktsAt5Mbps_Type = Counter32
_WlanAPStatsTotPktsAt5Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt5Mbps = _WlanAPStatsTotPktsAt5Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 5),
    _WlanAPStatsTotPktsAt5Mbps_Type()
)
wlanAPStatsTotPktsAt5Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt5Mbps.setStatus("current")
_WlanAPStatsTotBytesAt5Mbps_Type = Counter32
_WlanAPStatsTotBytesAt5Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt5Mbps = _WlanAPStatsTotBytesAt5Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 6),
    _WlanAPStatsTotBytesAt5Mbps_Type()
)
wlanAPStatsTotBytesAt5Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt5Mbps.setStatus("current")
_WlanAPStatsTotPktsAt11Mbps_Type = Counter32
_WlanAPStatsTotPktsAt11Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt11Mbps = _WlanAPStatsTotPktsAt11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 7),
    _WlanAPStatsTotPktsAt11Mbps_Type()
)
wlanAPStatsTotPktsAt11Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt11Mbps.setStatus("current")
_WlanAPStatsTotBytesAt11Mbps_Type = Counter32
_WlanAPStatsTotBytesAt11Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt11Mbps = _WlanAPStatsTotBytesAt11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 8),
    _WlanAPStatsTotBytesAt11Mbps_Type()
)
wlanAPStatsTotBytesAt11Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt11Mbps.setStatus("current")
_WlanAPStatsTotPktsAt6Mbps_Type = Counter32
_WlanAPStatsTotPktsAt6Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt6Mbps = _WlanAPStatsTotPktsAt6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 9),
    _WlanAPStatsTotPktsAt6Mbps_Type()
)
wlanAPStatsTotPktsAt6Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt6Mbps.setStatus("current")
_WlanAPStatsTotBytesAt6Mbps_Type = Counter32
_WlanAPStatsTotBytesAt6Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt6Mbps = _WlanAPStatsTotBytesAt6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 10),
    _WlanAPStatsTotBytesAt6Mbps_Type()
)
wlanAPStatsTotBytesAt6Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt6Mbps.setStatus("current")
_WlanAPStatsTotPktsAt12Mbps_Type = Counter32
_WlanAPStatsTotPktsAt12Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt12Mbps = _WlanAPStatsTotPktsAt12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 11),
    _WlanAPStatsTotPktsAt12Mbps_Type()
)
wlanAPStatsTotPktsAt12Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt12Mbps.setStatus("current")
_WlanAPStatsTotBytesAt12Mbps_Type = Counter32
_WlanAPStatsTotBytesAt12Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt12Mbps = _WlanAPStatsTotBytesAt12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 12),
    _WlanAPStatsTotBytesAt12Mbps_Type()
)
wlanAPStatsTotBytesAt12Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt12Mbps.setStatus("current")
_WlanAPStatsTotPktsAt18Mbps_Type = Counter32
_WlanAPStatsTotPktsAt18Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt18Mbps = _WlanAPStatsTotPktsAt18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 13),
    _WlanAPStatsTotPktsAt18Mbps_Type()
)
wlanAPStatsTotPktsAt18Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt18Mbps.setStatus("current")
_WlanAPStatsTotBytesAt18Mbps_Type = Counter32
_WlanAPStatsTotBytesAt18Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt18Mbps = _WlanAPStatsTotBytesAt18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 14),
    _WlanAPStatsTotBytesAt18Mbps_Type()
)
wlanAPStatsTotBytesAt18Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt18Mbps.setStatus("current")
_WlanAPStatsTotPktsAt24Mbps_Type = Counter32
_WlanAPStatsTotPktsAt24Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt24Mbps = _WlanAPStatsTotPktsAt24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 15),
    _WlanAPStatsTotPktsAt24Mbps_Type()
)
wlanAPStatsTotPktsAt24Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt24Mbps.setStatus("current")
_WlanAPStatsTotBytesAt24Mbps_Type = Counter32
_WlanAPStatsTotBytesAt24Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt24Mbps = _WlanAPStatsTotBytesAt24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 16),
    _WlanAPStatsTotBytesAt24Mbps_Type()
)
wlanAPStatsTotBytesAt24Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt24Mbps.setStatus("current")
_WlanAPStatsTotPktsAt36Mbps_Type = Counter32
_WlanAPStatsTotPktsAt36Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt36Mbps = _WlanAPStatsTotPktsAt36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 17),
    _WlanAPStatsTotPktsAt36Mbps_Type()
)
wlanAPStatsTotPktsAt36Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt36Mbps.setStatus("current")
_WlanAPStatsTotBytesAt36Mbps_Type = Counter32
_WlanAPStatsTotBytesAt36Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt36Mbps = _WlanAPStatsTotBytesAt36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 18),
    _WlanAPStatsTotBytesAt36Mbps_Type()
)
wlanAPStatsTotBytesAt36Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt36Mbps.setStatus("current")
_WlanAPStatsTotPktsAt48Mbps_Type = Counter32
_WlanAPStatsTotPktsAt48Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt48Mbps = _WlanAPStatsTotPktsAt48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 19),
    _WlanAPStatsTotPktsAt48Mbps_Type()
)
wlanAPStatsTotPktsAt48Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt48Mbps.setStatus("current")
_WlanAPStatsTotBytesAt48Mbps_Type = Counter32
_WlanAPStatsTotBytesAt48Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt48Mbps = _WlanAPStatsTotBytesAt48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 20),
    _WlanAPStatsTotBytesAt48Mbps_Type()
)
wlanAPStatsTotBytesAt48Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt48Mbps.setStatus("current")
_WlanAPStatsTotPktsAt54Mbps_Type = Counter32
_WlanAPStatsTotPktsAt54Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt54Mbps = _WlanAPStatsTotPktsAt54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 21),
    _WlanAPStatsTotPktsAt54Mbps_Type()
)
wlanAPStatsTotPktsAt54Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt54Mbps.setStatus("current")
_WlanAPStatsTotBytesAt54Mbps_Type = Counter32
_WlanAPStatsTotBytesAt54Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt54Mbps = _WlanAPStatsTotBytesAt54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 22),
    _WlanAPStatsTotBytesAt54Mbps_Type()
)
wlanAPStatsTotBytesAt54Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt54Mbps.setStatus("current")
_WlanAPStatsTotPktsAt9Mbps_Type = Counter32
_WlanAPStatsTotPktsAt9Mbps_Object = MibTableColumn
wlanAPStatsTotPktsAt9Mbps = _WlanAPStatsTotPktsAt9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 23),
    _WlanAPStatsTotPktsAt9Mbps_Type()
)
wlanAPStatsTotPktsAt9Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotPktsAt9Mbps.setStatus("current")
_WlanAPStatsTotBytesAt9Mbps_Type = Counter32
_WlanAPStatsTotBytesAt9Mbps_Object = MibTableColumn
wlanAPStatsTotBytesAt9Mbps = _WlanAPStatsTotBytesAt9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 2, 1, 24),
    _WlanAPStatsTotBytesAt9Mbps_Type()
)
wlanAPStatsTotBytesAt9Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotBytesAt9Mbps.setStatus("current")
_WlsxWlanAPDATypeStatsTable_Object = MibTable
wlsxWlanAPDATypeStatsTable = _WlsxWlanAPDATypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxWlanAPDATypeStatsTable.setStatus("current")
_WlsxWlanAPDATypeStatsEntry_Object = MibTableRow
wlsxWlanAPDATypeStatsEntry = _WlsxWlanAPDATypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1)
)
wlsxWlanAPDATypeStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPDATypeStatsEntry.setStatus("current")
_WlanAPStatsTotDABroadcastPkts_Type = Counter32
_WlanAPStatsTotDABroadcastPkts_Object = MibTableColumn
wlanAPStatsTotDABroadcastPkts = _WlanAPStatsTotDABroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1, 1),
    _WlanAPStatsTotDABroadcastPkts_Type()
)
wlanAPStatsTotDABroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDABroadcastPkts.setStatus("current")
_WlanAPStatsTotDABroadcastBytes_Type = Counter32
_WlanAPStatsTotDABroadcastBytes_Object = MibTableColumn
wlanAPStatsTotDABroadcastBytes = _WlanAPStatsTotDABroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1, 2),
    _WlanAPStatsTotDABroadcastBytes_Type()
)
wlanAPStatsTotDABroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDABroadcastBytes.setStatus("current")
_WlanAPStatsTotDAMulticastPkts_Type = Counter32
_WlanAPStatsTotDAMulticastPkts_Object = MibTableColumn
wlanAPStatsTotDAMulticastPkts = _WlanAPStatsTotDAMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1, 3),
    _WlanAPStatsTotDAMulticastPkts_Type()
)
wlanAPStatsTotDAMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDAMulticastPkts.setStatus("current")
_WlanAPStatsTotDAMulticastBytes_Type = Counter32
_WlanAPStatsTotDAMulticastBytes_Object = MibTableColumn
wlanAPStatsTotDAMulticastBytes = _WlanAPStatsTotDAMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1, 4),
    _WlanAPStatsTotDAMulticastBytes_Type()
)
wlanAPStatsTotDAMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDAMulticastBytes.setStatus("current")
_WlanAPStatsTotDAUnicastPkts_Type = Counter32
_WlanAPStatsTotDAUnicastPkts_Object = MibTableColumn
wlanAPStatsTotDAUnicastPkts = _WlanAPStatsTotDAUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1, 5),
    _WlanAPStatsTotDAUnicastPkts_Type()
)
wlanAPStatsTotDAUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDAUnicastPkts.setStatus("current")
_WlanAPStatsTotDAUnicastBytes_Type = Counter32
_WlanAPStatsTotDAUnicastBytes_Object = MibTableColumn
wlanAPStatsTotDAUnicastBytes = _WlanAPStatsTotDAUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 3, 1, 6),
    _WlanAPStatsTotDAUnicastBytes_Type()
)
wlanAPStatsTotDAUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDAUnicastBytes.setStatus("current")
_WlsxWlanAPFrameTypeStatsTable_Object = MibTable
wlsxWlanAPFrameTypeStatsTable = _WlsxWlanAPFrameTypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxWlanAPFrameTypeStatsTable.setStatus("current")
_WlsxWlanAPFrameTypeStatsEntry_Object = MibTableRow
wlsxWlanAPFrameTypeStatsEntry = _WlsxWlanAPFrameTypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1)
)
wlsxWlanAPFrameTypeStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPFrameTypeStatsEntry.setStatus("current")
_WlanAPStatsTotMgmtPkts_Type = Counter32
_WlanAPStatsTotMgmtPkts_Object = MibTableColumn
wlanAPStatsTotMgmtPkts = _WlanAPStatsTotMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1, 1),
    _WlanAPStatsTotMgmtPkts_Type()
)
wlanAPStatsTotMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotMgmtPkts.setStatus("current")
_WlanAPStatsTotMgmtBytes_Type = Counter32
_WlanAPStatsTotMgmtBytes_Object = MibTableColumn
wlanAPStatsTotMgmtBytes = _WlanAPStatsTotMgmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1, 2),
    _WlanAPStatsTotMgmtBytes_Type()
)
wlanAPStatsTotMgmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotMgmtBytes.setStatus("current")
_WlanAPStatsTotCtrlPkts_Type = Counter32
_WlanAPStatsTotCtrlPkts_Object = MibTableColumn
wlanAPStatsTotCtrlPkts = _WlanAPStatsTotCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1, 3),
    _WlanAPStatsTotCtrlPkts_Type()
)
wlanAPStatsTotCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotCtrlPkts.setStatus("current")
_WlanAPStatsTotCtrlBytes_Type = Counter32
_WlanAPStatsTotCtrlBytes_Object = MibTableColumn
wlanAPStatsTotCtrlBytes = _WlanAPStatsTotCtrlBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1, 4),
    _WlanAPStatsTotCtrlBytes_Type()
)
wlanAPStatsTotCtrlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotCtrlBytes.setStatus("current")
_WlanAPStatsTotDataPkts_Type = Counter32
_WlanAPStatsTotDataPkts_Object = MibTableColumn
wlanAPStatsTotDataPkts = _WlanAPStatsTotDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1, 5),
    _WlanAPStatsTotDataPkts_Type()
)
wlanAPStatsTotDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDataPkts.setStatus("current")
_WlanAPStatsTotDataBytes_Type = Counter32
_WlanAPStatsTotDataBytes_Object = MibTableColumn
wlanAPStatsTotDataBytes = _WlanAPStatsTotDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 4, 1, 6),
    _WlanAPStatsTotDataBytes_Type()
)
wlanAPStatsTotDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsTotDataBytes.setStatus("current")
_WlsxWlanAPPktSizeStatsTable_Object = MibTable
wlsxWlanAPPktSizeStatsTable = _WlsxWlanAPPktSizeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5)
)
if mibBuilder.loadTexts:
    wlsxWlanAPPktSizeStatsTable.setStatus("current")
_WlsxWlanAPPktSizeStatsEntry_Object = MibTableRow
wlsxWlanAPPktSizeStatsEntry = _WlsxWlanAPPktSizeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1)
)
wlsxWlanAPPktSizeStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPPktSizeStatsEntry.setStatus("current")
_WlanAPStatsPkts63Bytes_Type = Counter32
_WlanAPStatsPkts63Bytes_Object = MibTableColumn
wlanAPStatsPkts63Bytes = _WlanAPStatsPkts63Bytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1, 1),
    _WlanAPStatsPkts63Bytes_Type()
)
wlanAPStatsPkts63Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsPkts63Bytes.setStatus("current")
_WlanAPStatsPkts64To127_Type = Counter32
_WlanAPStatsPkts64To127_Object = MibTableColumn
wlanAPStatsPkts64To127 = _WlanAPStatsPkts64To127_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1, 2),
    _WlanAPStatsPkts64To127_Type()
)
wlanAPStatsPkts64To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsPkts64To127.setStatus("current")
_WlanAPStatsPkts128To255_Type = Counter32
_WlanAPStatsPkts128To255_Object = MibTableColumn
wlanAPStatsPkts128To255 = _WlanAPStatsPkts128To255_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1, 3),
    _WlanAPStatsPkts128To255_Type()
)
wlanAPStatsPkts128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsPkts128To255.setStatus("current")
_WlanAPStatsPkts256To511_Type = Counter32
_WlanAPStatsPkts256To511_Object = MibTableColumn
wlanAPStatsPkts256To511 = _WlanAPStatsPkts256To511_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1, 4),
    _WlanAPStatsPkts256To511_Type()
)
wlanAPStatsPkts256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsPkts256To511.setStatus("current")
_WlanAPStatsPkts512To1023_Type = Counter32
_WlanAPStatsPkts512To1023_Object = MibTableColumn
wlanAPStatsPkts512To1023 = _WlanAPStatsPkts512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1, 5),
    _WlanAPStatsPkts512To1023_Type()
)
wlanAPStatsPkts512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsPkts512To1023.setStatus("current")
_WlanAPStatsPkts1024To1518_Type = Counter32
_WlanAPStatsPkts1024To1518_Object = MibTableColumn
wlanAPStatsPkts1024To1518 = _WlanAPStatsPkts1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 5, 1, 6),
    _WlanAPStatsPkts1024To1518_Type()
)
wlanAPStatsPkts1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPStatsPkts1024To1518.setStatus("current")
_WlsxWlanAPChStatsTable_Object = MibTable
wlsxWlanAPChStatsTable = _WlsxWlanAPChStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6)
)
if mibBuilder.loadTexts:
    wlsxWlanAPChStatsTable.setStatus("current")
_WlsxWlanAPChStatsEntry_Object = MibTableRow
wlsxWlanAPChStatsEntry = _WlsxWlanAPChStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1)
)
wlsxWlanAPChStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPChStatsEntry.setStatus("current")


class _WlanAPChannelNumber_Type(Integer32):
    """Custom type wlanAPChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_WlanAPChannelNumber_Type.__name__ = "Integer32"
_WlanAPChannelNumber_Object = MibTableColumn
wlanAPChannelNumber = _WlanAPChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 1),
    _WlanAPChannelNumber_Type()
)
wlanAPChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChannelNumber.setStatus("deprecated")
_WlanAPChNumStations_Type = Integer32
_WlanAPChNumStations_Object = MibTableColumn
wlanAPChNumStations = _WlanAPChNumStations_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 2),
    _WlanAPChNumStations_Type()
)
wlanAPChNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChNumStations.setStatus("current")
_WlanAPChTotPkts_Type = Counter32
_WlanAPChTotPkts_Object = MibTableColumn
wlanAPChTotPkts = _WlanAPChTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 3),
    _WlanAPChTotPkts_Type()
)
wlanAPChTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTotPkts.setStatus("current")
_WlanAPChTotBytes_Type = Counter32
_WlanAPChTotBytes_Object = MibTableColumn
wlanAPChTotBytes = _WlanAPChTotBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 4),
    _WlanAPChTotBytes_Type()
)
wlanAPChTotBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTotBytes.setStatus("current")
_WlanAPChTotRetryPkts_Type = Counter32
_WlanAPChTotRetryPkts_Object = MibTableColumn
wlanAPChTotRetryPkts = _WlanAPChTotRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 5),
    _WlanAPChTotRetryPkts_Type()
)
wlanAPChTotRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTotRetryPkts.setStatus("current")
_WlanAPChTotFragmentedPkts_Type = Counter32
_WlanAPChTotFragmentedPkts_Object = MibTableColumn
wlanAPChTotFragmentedPkts = _WlanAPChTotFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 6),
    _WlanAPChTotFragmentedPkts_Type()
)
wlanAPChTotFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTotFragmentedPkts.setStatus("current")
_WlanAPChTotPhyErrPkts_Type = Counter32
_WlanAPChTotPhyErrPkts_Object = MibTableColumn
wlanAPChTotPhyErrPkts = _WlanAPChTotPhyErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 7),
    _WlanAPChTotPhyErrPkts_Type()
)
wlanAPChTotPhyErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTotPhyErrPkts.setStatus("current")
_WlanAPChTotMacErrPkts_Type = Counter32
_WlanAPChTotMacErrPkts_Object = MibTableColumn
wlanAPChTotMacErrPkts = _WlanAPChTotMacErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 8),
    _WlanAPChTotMacErrPkts_Type()
)
wlanAPChTotMacErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTotMacErrPkts.setStatus("current")
_WlanAPChNoise_Type = Integer32
_WlanAPChNoise_Object = MibTableColumn
wlanAPChNoise = _WlanAPChNoise_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 9),
    _WlanAPChNoise_Type()
)
wlanAPChNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChNoise.setStatus("current")
_WlanAPChCoverageIndex_Type = Integer32
_WlanAPChCoverageIndex_Object = MibTableColumn
wlanAPChCoverageIndex = _WlanAPChCoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 10),
    _WlanAPChCoverageIndex_Type()
)
wlanAPChCoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChCoverageIndex.setStatus("current")
_WlanAPChInterferenceIndex_Type = Integer32
_WlanAPChInterferenceIndex_Object = MibTableColumn
wlanAPChInterferenceIndex = _WlanAPChInterferenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 11),
    _WlanAPChInterferenceIndex_Type()
)
wlanAPChInterferenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChInterferenceIndex.setStatus("current")
_WlanAPChFrameRetryRate_Type = Integer32
_WlanAPChFrameRetryRate_Object = MibTableColumn
wlanAPChFrameRetryRate = _WlanAPChFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 12),
    _WlanAPChFrameRetryRate_Type()
)
wlanAPChFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameRetryRate.setStatus("current")
_WlanAPChFrameLowSpeedRate_Type = Integer32
_WlanAPChFrameLowSpeedRate_Object = MibTableColumn
wlanAPChFrameLowSpeedRate = _WlanAPChFrameLowSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 13),
    _WlanAPChFrameLowSpeedRate_Type()
)
wlanAPChFrameLowSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameLowSpeedRate.setStatus("current")
_WlanAPChFrameNonUnicastRate_Type = Integer32
_WlanAPChFrameNonUnicastRate_Object = MibTableColumn
wlanAPChFrameNonUnicastRate = _WlanAPChFrameNonUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 14),
    _WlanAPChFrameNonUnicastRate_Type()
)
wlanAPChFrameNonUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameNonUnicastRate.setStatus("current")
_WlanAPChFrameFragmentationRate_Type = Integer32
_WlanAPChFrameFragmentationRate_Object = MibTableColumn
wlanAPChFrameFragmentationRate = _WlanAPChFrameFragmentationRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 15),
    _WlanAPChFrameFragmentationRate_Type()
)
wlanAPChFrameFragmentationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameFragmentationRate.setStatus("current")
_WlanAPChFrameBandwidthRate_Type = Integer32
_WlanAPChFrameBandwidthRate_Object = MibTableColumn
wlanAPChFrameBandwidthRate = _WlanAPChFrameBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 16),
    _WlanAPChFrameBandwidthRate_Type()
)
wlanAPChFrameBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameBandwidthRate.setStatus("current")
_WlanAPChFrameRetryErrorRate_Type = Integer32
_WlanAPChFrameRetryErrorRate_Object = MibTableColumn
wlanAPChFrameRetryErrorRate = _WlanAPChFrameRetryErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 17),
    _WlanAPChFrameRetryErrorRate_Type()
)
wlanAPChFrameRetryErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameRetryErrorRate.setStatus("deprecated")
_WlanAPChBusyRate_Type = Integer32
_WlanAPChBusyRate_Object = MibTableColumn
wlanAPChBusyRate = _WlanAPChBusyRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 18),
    _WlanAPChBusyRate_Type()
)
wlanAPChBusyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChBusyRate.setStatus("current")
_WlanAPChNumAPs_Type = Integer32
_WlanAPChNumAPs_Object = MibTableColumn
wlanAPChNumAPs = _WlanAPChNumAPs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 19),
    _WlanAPChNumAPs_Type()
)
wlanAPChNumAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChNumAPs.setStatus("current")
_WlanAPChFrameReceiveErrorRate_Type = Integer32
_WlanAPChFrameReceiveErrorRate_Object = MibTableColumn
wlanAPChFrameReceiveErrorRate = _WlanAPChFrameReceiveErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 20),
    _WlanAPChFrameReceiveErrorRate_Type()
)
wlanAPChFrameReceiveErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameReceiveErrorRate.setStatus("current")
_WlanAPChTransmittedFragmentCount_Type = Counter32
_WlanAPChTransmittedFragmentCount_Object = MibTableColumn
wlanAPChTransmittedFragmentCount = _WlanAPChTransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 21),
    _WlanAPChTransmittedFragmentCount_Type()
)
wlanAPChTransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTransmittedFragmentCount.setStatus("current")
_WlanAPChMulticastTransmittedFrameCount_Type = Counter32
_WlanAPChMulticastTransmittedFrameCount_Object = MibTableColumn
wlanAPChMulticastTransmittedFrameCount = _WlanAPChMulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 22),
    _WlanAPChMulticastTransmittedFrameCount_Type()
)
wlanAPChMulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChMulticastTransmittedFrameCount.setStatus("current")
_WlanAPChFailedCount_Type = Counter32
_WlanAPChFailedCount_Object = MibTableColumn
wlanAPChFailedCount = _WlanAPChFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 23),
    _WlanAPChFailedCount_Type()
)
wlanAPChFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFailedCount.setStatus("current")
_WlanAPChRetryCount_Type = Counter32
_WlanAPChRetryCount_Object = MibTableColumn
wlanAPChRetryCount = _WlanAPChRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 24),
    _WlanAPChRetryCount_Type()
)
wlanAPChRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChRetryCount.setStatus("current")
_WlanAPChMultipleRetryCount_Type = Counter32
_WlanAPChMultipleRetryCount_Object = MibTableColumn
wlanAPChMultipleRetryCount = _WlanAPChMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 25),
    _WlanAPChMultipleRetryCount_Type()
)
wlanAPChMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChMultipleRetryCount.setStatus("current")
_WlanAPChFrameDuplicateCount_Type = Counter32
_WlanAPChFrameDuplicateCount_Object = MibTableColumn
wlanAPChFrameDuplicateCount = _WlanAPChFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 26),
    _WlanAPChFrameDuplicateCount_Type()
)
wlanAPChFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFrameDuplicateCount.setStatus("current")
_WlanAPChRTSSuccessCount_Type = Counter32
_WlanAPChRTSSuccessCount_Object = MibTableColumn
wlanAPChRTSSuccessCount = _WlanAPChRTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 27),
    _WlanAPChRTSSuccessCount_Type()
)
wlanAPChRTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChRTSSuccessCount.setStatus("current")
_WlanAPChRTSFailureCount_Type = Counter32
_WlanAPChRTSFailureCount_Object = MibTableColumn
wlanAPChRTSFailureCount = _WlanAPChRTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 28),
    _WlanAPChRTSFailureCount_Type()
)
wlanAPChRTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChRTSFailureCount.setStatus("current")
_WlanAPChACKFailureCount_Type = Counter32
_WlanAPChACKFailureCount_Object = MibTableColumn
wlanAPChACKFailureCount = _WlanAPChACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 29),
    _WlanAPChACKFailureCount_Type()
)
wlanAPChACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChACKFailureCount.setStatus("current")
_WlanAPChReceivedFragmentCount_Type = Counter32
_WlanAPChReceivedFragmentCount_Object = MibTableColumn
wlanAPChReceivedFragmentCount = _WlanAPChReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 30),
    _WlanAPChReceivedFragmentCount_Type()
)
wlanAPChReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChReceivedFragmentCount.setStatus("current")
_WlanAPChMulticastReceivedFrameCount_Type = Counter32
_WlanAPChMulticastReceivedFrameCount_Object = MibTableColumn
wlanAPChMulticastReceivedFrameCount = _WlanAPChMulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 31),
    _WlanAPChMulticastReceivedFrameCount_Type()
)
wlanAPChMulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChMulticastReceivedFrameCount.setStatus("current")
_WlanAPChFCSErrorCount_Type = Counter32
_WlanAPChFCSErrorCount_Object = MibTableColumn
wlanAPChFCSErrorCount = _WlanAPChFCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 32),
    _WlanAPChFCSErrorCount_Type()
)
wlanAPChFCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChFCSErrorCount.setStatus("current")
_WlanAPChTransmittedFrameCount_Type = Counter32
_WlanAPChTransmittedFrameCount_Object = MibTableColumn
wlanAPChTransmittedFrameCount = _WlanAPChTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 33),
    _WlanAPChTransmittedFrameCount_Type()
)
wlanAPChTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTransmittedFrameCount.setStatus("current")
_WlanAPChWEPUndecryptableCount_Type = Counter32
_WlanAPChWEPUndecryptableCount_Object = MibTableColumn
wlanAPChWEPUndecryptableCount = _WlanAPChWEPUndecryptableCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 34),
    _WlanAPChWEPUndecryptableCount_Type()
)
wlanAPChWEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChWEPUndecryptableCount.setStatus("current")


class _WlanAPChRxUtilization_Type(Integer32):
    """Custom type wlanAPChRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlanAPChRxUtilization_Type.__name__ = "Integer32"
_WlanAPChRxUtilization_Object = MibTableColumn
wlanAPChRxUtilization = _WlanAPChRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 35),
    _WlanAPChRxUtilization_Type()
)
wlanAPChRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChRxUtilization.setStatus("current")


class _WlanAPChTxUtilization_Type(Integer32):
    """Custom type wlanAPChTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlanAPChTxUtilization_Type.__name__ = "Integer32"
_WlanAPChTxUtilization_Object = MibTableColumn
wlanAPChTxUtilization = _WlanAPChTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 36),
    _WlanAPChTxUtilization_Type()
)
wlanAPChTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChTxUtilization.setStatus("current")


class _WlanAPChUtilization_Type(Integer32):
    """Custom type wlanAPChUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlanAPChUtilization_Type.__name__ = "Integer32"
_WlanAPChUtilization_Object = MibTableColumn
wlanAPChUtilization = _WlanAPChUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 37),
    _WlanAPChUtilization_Type()
)
wlanAPChUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChUtilization.setStatus("current")
_WlanAPChPhyType_Type = ArubaPhyType
_WlanAPChPhyType_Object = MibTableColumn
wlanAPChPhyType = _WlanAPChPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 38),
    _WlanAPChPhyType_Type()
)
wlanAPChPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChPhyType.setStatus("current")
_WlanAPChannelNumberV2_Type = Integer32
_WlanAPChannelNumberV2_Object = MibTableColumn
wlanAPChannelNumberV2 = _WlanAPChannelNumberV2_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 39),
    _WlanAPChannelNumberV2_Type()
)
wlanAPChannelNumberV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChannelNumberV2.setStatus("current")
_WlanAPChHTMode_Type = ArubaHTMode
_WlanAPChHTMode_Object = MibTableColumn
wlanAPChHTMode = _WlanAPChHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 6, 1, 40),
    _WlanAPChHTMode_Type()
)
wlanAPChHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPChHTMode.setStatus("current")
_WlsxWlanAPWiredStatsTable_Object = MibTable
wlsxWlanAPWiredStatsTable = _WlsxWlanAPWiredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7)
)
if mibBuilder.loadTexts:
    wlsxWlanAPWiredStatsTable.setStatus("deprecated")
_WlsxWlanAPWiredStatsEntry_Object = MibTableRow
wlsxWlanAPWiredStatsEntry = _WlsxWlanAPWiredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1)
)
wlsxWlanAPWiredStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPWiredStatsEntry.setStatus("deprecated")
_WlanAPWiredRxPkts_Type = Counter32
_WlanAPWiredRxPkts_Object = MibTableColumn
wlanAPWiredRxPkts = _WlanAPWiredRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1, 1),
    _WlanAPWiredRxPkts_Type()
)
wlanAPWiredRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredRxPkts.setStatus("deprecated")
_WlanAPWiredRxDroppedPkts_Type = Counter32
_WlanAPWiredRxDroppedPkts_Object = MibTableColumn
wlanAPWiredRxDroppedPkts = _WlanAPWiredRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1, 2),
    _WlanAPWiredRxDroppedPkts_Type()
)
wlanAPWiredRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredRxDroppedPkts.setStatus("deprecated")
_WlanAPWiredRxBytes_Type = Counter32
_WlanAPWiredRxBytes_Object = MibTableColumn
wlanAPWiredRxBytes = _WlanAPWiredRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1, 3),
    _WlanAPWiredRxBytes_Type()
)
wlanAPWiredRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredRxBytes.setStatus("deprecated")
_WlanAPWiredTxBytes_Type = Counter32
_WlanAPWiredTxBytes_Object = MibTableColumn
wlanAPWiredTxBytes = _WlanAPWiredTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1, 4),
    _WlanAPWiredTxBytes_Type()
)
wlanAPWiredTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredTxBytes.setStatus("deprecated")
_WlanAPWiredRxRate_Type = Gauge32
_WlanAPWiredRxRate_Object = MibTableColumn
wlanAPWiredRxRate = _WlanAPWiredRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1, 5),
    _WlanAPWiredRxRate_Type()
)
wlanAPWiredRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredRxRate.setStatus("deprecated")
_WlanAPWiredTxRate_Type = Gauge32
_WlanAPWiredTxRate_Object = MibTableColumn
wlanAPWiredTxRate = _WlanAPWiredTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 7, 1, 6),
    _WlanAPWiredTxRate_Type()
)
wlanAPWiredTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredTxRate.setStatus("deprecated")
_WlsxWlanAPESSIDStatsTable_Object = MibTable
wlsxWlanAPESSIDStatsTable = _WlsxWlanAPESSIDStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 8)
)
if mibBuilder.loadTexts:
    wlsxWlanAPESSIDStatsTable.setStatus("current")
_WlsxWlanAPESSIDStatsEntry_Object = MibTableRow
wlsxWlanAPESSIDStatsEntry = _WlsxWlanAPESSIDStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 8, 1)
)
wlsxWlanAPESSIDStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPESSIDStatsEntry.setStatus("current")
_WlanAPESSIDWirelessRxBytes_Type = Counter32
_WlanAPESSIDWirelessRxBytes_Object = MibTableColumn
wlanAPESSIDWirelessRxBytes = _WlanAPESSIDWirelessRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 8, 1, 1),
    _WlanAPESSIDWirelessRxBytes_Type()
)
wlanAPESSIDWirelessRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPESSIDWirelessRxBytes.setStatus("current")
_WlanAPESSIDWirelessTxBytes_Type = Counter32
_WlanAPESSIDWirelessTxBytes_Object = MibTableColumn
wlanAPESSIDWirelessTxBytes = _WlanAPESSIDWirelessTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 8, 1, 2),
    _WlanAPESSIDWirelessTxBytes_Type()
)
wlanAPESSIDWirelessTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPESSIDWirelessTxBytes.setStatus("current")
_WlanAPESSIDWiredRxBytes_Type = Counter32
_WlanAPESSIDWiredRxBytes_Object = MibTableColumn
wlanAPESSIDWiredRxBytes = _WlanAPESSIDWiredRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 8, 1, 3),
    _WlanAPESSIDWiredRxBytes_Type()
)
wlanAPESSIDWiredRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPESSIDWiredRxBytes.setStatus("current")
_WlanAPESSIDWiredTxBytes_Type = Counter32
_WlanAPESSIDWiredTxBytes_Object = MibTableColumn
wlanAPESSIDWiredTxBytes = _WlanAPESSIDWiredTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 8, 1, 4),
    _WlanAPESSIDWiredTxBytes_Type()
)
wlanAPESSIDWiredTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPESSIDWiredTxBytes.setStatus("current")
_WlsxWlanAPRadioStatsTable_Object = MibTable
wlsxWlanAPRadioStatsTable = _WlsxWlanAPRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9)
)
if mibBuilder.loadTexts:
    wlsxWlanAPRadioStatsTable.setStatus("current")
_WlsxWlanAPRadioStatsEntry_Object = MibTableRow
wlsxWlanAPRadioStatsEntry = _WlsxWlanAPRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1)
)
wlsxWlanAPRadioStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPRadioStatsEntry.setStatus("current")
_WlanAPRadioRxPkts_Type = Counter32
_WlanAPRadioRxPkts_Object = MibTableColumn
wlanAPRadioRxPkts = _WlanAPRadioRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 1),
    _WlanAPRadioRxPkts_Type()
)
wlanAPRadioRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioRxPkts.setStatus("current")
_WlanAPRadioRxBytes_Type = Counter64
_WlanAPRadioRxBytes_Object = MibTableColumn
wlanAPRadioRxBytes = _WlanAPRadioRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 2),
    _WlanAPRadioRxBytes_Type()
)
wlanAPRadioRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioRxBytes.setStatus("current")
_WlanAPRadioTxPkts_Type = Counter32
_WlanAPRadioTxPkts_Object = MibTableColumn
wlanAPRadioTxPkts = _WlanAPRadioTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 3),
    _WlanAPRadioTxPkts_Type()
)
wlanAPRadioTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTxPkts.setStatus("current")
_WlanAPRadioTxBytes_Type = Counter64
_WlanAPRadioTxBytes_Object = MibTableColumn
wlanAPRadioTxBytes = _WlanAPRadioTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 4),
    _WlanAPRadioTxBytes_Type()
)
wlanAPRadioTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTxBytes.setStatus("current")
_WlanAPRadioTxDroppedPkts_Type = Counter32
_WlanAPRadioTxDroppedPkts_Object = MibTableColumn
wlanAPRadioTxDroppedPkts = _WlanAPRadioTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 5),
    _WlanAPRadioTxDroppedPkts_Type()
)
wlanAPRadioTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTxDroppedPkts.setStatus("current")
_WlanAPRadioTxErrorPkts_Type = Counter32
_WlanAPRadioTxErrorPkts_Object = MibTableColumn
wlanAPRadioTxErrorPkts = _WlanAPRadioTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 6),
    _WlanAPRadioTxErrorPkts_Type()
)
wlanAPRadioTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTxErrorPkts.setStatus("current")
_WlanAPRadioRxRate_Type = Gauge32
_WlanAPRadioRxRate_Object = MibTableColumn
wlanAPRadioRxRate = _WlanAPRadioRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 7),
    _WlanAPRadioRxRate_Type()
)
wlanAPRadioRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioRxRate.setStatus("current")
_WlanAPRadioTxRate_Type = Gauge32
_WlanAPRadioTxRate_Object = MibTableColumn
wlanAPRadioTxRate = _WlanAPRadioTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 8),
    _WlanAPRadioTxRate_Type()
)
wlanAPRadioTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTxRate.setStatus("current")
_WlanApRadioAssocReqCount_Type = Counter32
_WlanApRadioAssocReqCount_Object = MibTableColumn
wlanApRadioAssocReqCount = _WlanApRadioAssocReqCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 9),
    _WlanApRadioAssocReqCount_Type()
)
wlanApRadioAssocReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanApRadioAssocReqCount.setStatus("current")
_WlanApRadioAssocReqSuccCount_Type = Counter32
_WlanApRadioAssocReqSuccCount_Object = MibTableColumn
wlanApRadioAssocReqSuccCount = _WlanApRadioAssocReqSuccCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 10),
    _WlanApRadioAssocReqSuccCount_Type()
)
wlanApRadioAssocReqSuccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanApRadioAssocReqSuccCount.setStatus("current")
_WlanApRadioReAssocReqCount_Type = Counter32
_WlanApRadioReAssocReqCount_Object = MibTableColumn
wlanApRadioReAssocReqCount = _WlanApRadioReAssocReqCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 11),
    _WlanApRadioReAssocReqCount_Type()
)
wlanApRadioReAssocReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanApRadioReAssocReqCount.setStatus("current")
_WlanApRadioReAssocReqSuccCount_Type = Counter32
_WlanApRadioReAssocReqSuccCount_Object = MibTableColumn
wlanApRadioReAssocReqSuccCount = _WlanApRadioReAssocReqSuccCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 12),
    _WlanApRadioReAssocReqSuccCount_Type()
)
wlanApRadioReAssocReqSuccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanApRadioReAssocReqSuccCount.setStatus("current")
_WlanAPRadioStationDuration_Type = Integer32
_WlanAPRadioStationDuration_Object = MibTableColumn
wlanAPRadioStationDuration = _WlanAPRadioStationDuration_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 13),
    _WlanAPRadioStationDuration_Type()
)
wlanAPRadioStationDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioStationDuration.setStatus("current")
_WlanAPRadioAssocSuccPercent_Type = Gauge32
_WlanAPRadioAssocSuccPercent_Object = MibTableColumn
wlanAPRadioAssocSuccPercent = _WlanAPRadioAssocSuccPercent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 14),
    _WlanAPRadioAssocSuccPercent_Type()
)
wlanAPRadioAssocSuccPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioAssocSuccPercent.setStatus("current")
_WlanAPRadioTxDataBytes_Type = Counter32
_WlanAPRadioTxDataBytes_Object = MibTableColumn
wlanAPRadioTxDataBytes = _WlanAPRadioTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 9, 1, 15),
    _WlanAPRadioTxDataBytes_Type()
)
wlanAPRadioTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRadioTxDataBytes.setStatus("current")
_WlsxWlanAPWiredPortStatsTable_Object = MibTable
wlsxWlanAPWiredPortStatsTable = _WlsxWlanAPWiredPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10)
)
if mibBuilder.loadTexts:
    wlsxWlanAPWiredPortStatsTable.setStatus("current")
_WlsxWlanAPWiredPortStatsEntry_Object = MibTableRow
wlsxWlanAPWiredPortStatsEntry = _WlsxWlanAPWiredPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1)
)
wlsxWlanAPWiredPortStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPPortIndex"),
)
if mibBuilder.loadTexts:
    wlsxWlanAPWiredPortStatsEntry.setStatus("current")


class _WlanAPPortIndex_Type(Integer32):
    """Custom type wlanAPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WlanAPPortIndex_Type.__name__ = "Integer32"
_WlanAPPortIndex_Object = MibTableColumn
wlanAPPortIndex = _WlanAPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 1),
    _WlanAPPortIndex_Type()
)
wlanAPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanAPPortIndex.setStatus("current")


class _WlanAPPortName_Type(DisplayString):
    """Custom type wlanAPPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WlanAPPortName_Type.__name__ = "DisplayString"
_WlanAPPortName_Object = MibTableColumn
wlanAPPortName = _WlanAPPortName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 2),
    _WlanAPPortName_Type()
)
wlanAPPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPPortName.setStatus("current")
_WlanAPWiredPortRxPkts_Type = Counter32
_WlanAPWiredPortRxPkts_Object = MibTableColumn
wlanAPWiredPortRxPkts = _WlanAPWiredPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 3),
    _WlanAPWiredPortRxPkts_Type()
)
wlanAPWiredPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortRxPkts.setStatus("current")
_WlanAPWiredPortRxDroppedPkts_Type = Counter32
_WlanAPWiredPortRxDroppedPkts_Object = MibTableColumn
wlanAPWiredPortRxDroppedPkts = _WlanAPWiredPortRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 4),
    _WlanAPWiredPortRxDroppedPkts_Type()
)
wlanAPWiredPortRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortRxDroppedPkts.setStatus("current")
_WlanAPWiredPortRxErrors_Type = Counter32
_WlanAPWiredPortRxErrors_Object = MibTableColumn
wlanAPWiredPortRxErrors = _WlanAPWiredPortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 5),
    _WlanAPWiredPortRxErrors_Type()
)
wlanAPWiredPortRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortRxErrors.setStatus("current")
_WlanAPWiredPortRxBytes_Type = Counter64
_WlanAPWiredPortRxBytes_Object = MibTableColumn
wlanAPWiredPortRxBytes = _WlanAPWiredPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 6),
    _WlanAPWiredPortRxBytes_Type()
)
wlanAPWiredPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortRxBytes.setStatus("current")
_WlanAPWiredPortTxPkts_Type = Counter32
_WlanAPWiredPortTxPkts_Object = MibTableColumn
wlanAPWiredPortTxPkts = _WlanAPWiredPortTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 7),
    _WlanAPWiredPortTxPkts_Type()
)
wlanAPWiredPortTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortTxPkts.setStatus("current")
_WlanAPWiredPortTxDroppedPkts_Type = Counter32
_WlanAPWiredPortTxDroppedPkts_Object = MibTableColumn
wlanAPWiredPortTxDroppedPkts = _WlanAPWiredPortTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 8),
    _WlanAPWiredPortTxDroppedPkts_Type()
)
wlanAPWiredPortTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortTxDroppedPkts.setStatus("current")
_WlanAPWiredPortTxErrors_Type = Counter32
_WlanAPWiredPortTxErrors_Object = MibTableColumn
wlanAPWiredPortTxErrors = _WlanAPWiredPortTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 9),
    _WlanAPWiredPortTxErrors_Type()
)
wlanAPWiredPortTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortTxErrors.setStatus("current")
_WlanAPWiredPortTxBytes_Type = Counter64
_WlanAPWiredPortTxBytes_Object = MibTableColumn
wlanAPWiredPortTxBytes = _WlanAPWiredPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 10),
    _WlanAPWiredPortTxBytes_Type()
)
wlanAPWiredPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortTxBytes.setStatus("current")
_WlanAPWiredPortRxRate_Type = Gauge32
_WlanAPWiredPortRxRate_Object = MibTableColumn
wlanAPWiredPortRxRate = _WlanAPWiredPortRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 11),
    _WlanAPWiredPortRxRate_Type()
)
wlanAPWiredPortRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortRxRate.setStatus("current")
_WlanAPWiredPortTxRate_Type = Gauge32
_WlanAPWiredPortTxRate_Object = MibTableColumn
wlanAPWiredPortTxRate = _WlanAPWiredPortTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 12),
    _WlanAPWiredPortTxRate_Type()
)
wlanAPWiredPortTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortTxRate.setStatus("current")
_WlanAPWiredPortSpeed_Type = ArubaPortSpeed
_WlanAPWiredPortSpeed_Object = MibTableColumn
wlanAPWiredPortSpeed = _WlanAPWiredPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 1, 10, 1, 13),
    _WlanAPWiredPortSpeed_Type()
)
wlanAPWiredPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPWiredPortSpeed.setStatus("current")
_WlsxWlanStationStatsGroup_ObjectIdentity = ObjectIdentity
wlsxWlanStationStatsGroup = _WlsxWlanStationStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2)
)
_WlsxWlanStationStatsTable_Object = MibTable
wlsxWlanStationStatsTable = _WlsxWlanStationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wlsxWlanStationStatsTable.setStatus("current")
_WlsxWlanStationStatsEntry_Object = MibTableRow
wlsxWlanStationStatsEntry = _WlsxWlanStationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1)
)
wlsxWlanStationStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanStationStatsEntry.setStatus("current")
_WlanStaChannelNum_Type = Unsigned32
_WlanStaChannelNum_Object = MibTableColumn
wlanStaChannelNum = _WlanStaChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 1),
    _WlanStaChannelNum_Type()
)
wlanStaChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaChannelNum.setStatus("current")
_WlanStaTxPkts_Type = Counter32
_WlanStaTxPkts_Object = MibTableColumn
wlanStaTxPkts = _WlanStaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 2),
    _WlanStaTxPkts_Type()
)
wlanStaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts.setStatus("current")
_WlanStaTxBytes_Type = Counter32
_WlanStaTxBytes_Object = MibTableColumn
wlanStaTxBytes = _WlanStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 3),
    _WlanStaTxBytes_Type()
)
wlanStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytes.setStatus("current")
_WlanStaRxPkts_Type = Counter32
_WlanStaRxPkts_Object = MibTableColumn
wlanStaRxPkts = _WlanStaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 4),
    _WlanStaRxPkts_Type()
)
wlanStaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts.setStatus("current")
_WlanStaRxBytes_Type = Counter32
_WlanStaRxBytes_Object = MibTableColumn
wlanStaRxBytes = _WlanStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 5),
    _WlanStaRxBytes_Type()
)
wlanStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytes.setStatus("current")
_WlanStaTxBCastPkts_Type = Counter32
_WlanStaTxBCastPkts_Object = MibTableColumn
wlanStaTxBCastPkts = _WlanStaTxBCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 6),
    _WlanStaTxBCastPkts_Type()
)
wlanStaTxBCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBCastPkts.setStatus("current")
_WlanStaRxBCastBytes_Type = Counter32
_WlanStaRxBCastBytes_Object = MibTableColumn
wlanStaRxBCastBytes = _WlanStaRxBCastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 7),
    _WlanStaRxBCastBytes_Type()
)
wlanStaRxBCastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBCastBytes.setStatus("deprecated")
_WlanStaTxMCastPkts_Type = Counter32
_WlanStaTxMCastPkts_Object = MibTableColumn
wlanStaTxMCastPkts = _WlanStaTxMCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 8),
    _WlanStaTxMCastPkts_Type()
)
wlanStaTxMCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxMCastPkts.setStatus("current")
_WlanStaRxMCastBytes_Type = Counter32
_WlanStaRxMCastBytes_Object = MibTableColumn
wlanStaRxMCastBytes = _WlanStaRxMCastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 9),
    _WlanStaRxMCastBytes_Type()
)
wlanStaRxMCastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxMCastBytes.setStatus("deprecated")
_WlanStaDataPkts_Type = Counter32
_WlanStaDataPkts_Object = MibTableColumn
wlanStaDataPkts = _WlanStaDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 10),
    _WlanStaDataPkts_Type()
)
wlanStaDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaDataPkts.setStatus("current")
_WlanStaCtrlPkts_Type = Counter32
_WlanStaCtrlPkts_Object = MibTableColumn
wlanStaCtrlPkts = _WlanStaCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 11),
    _WlanStaCtrlPkts_Type()
)
wlanStaCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaCtrlPkts.setStatus("current")
_WlanStaNumAssocRequests_Type = Counter32
_WlanStaNumAssocRequests_Object = MibTableColumn
wlanStaNumAssocRequests = _WlanStaNumAssocRequests_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 12),
    _WlanStaNumAssocRequests_Type()
)
wlanStaNumAssocRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaNumAssocRequests.setStatus("current")
_WlanStaNumAuthRequests_Type = Counter32
_WlanStaNumAuthRequests_Object = MibTableColumn
wlanStaNumAuthRequests = _WlanStaNumAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 13),
    _WlanStaNumAuthRequests_Type()
)
wlanStaNumAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaNumAuthRequests.setStatus("current")
_WlanStaTxDeauthentications_Type = Counter32
_WlanStaTxDeauthentications_Object = MibTableColumn
wlanStaTxDeauthentications = _WlanStaTxDeauthentications_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 14),
    _WlanStaTxDeauthentications_Type()
)
wlanStaTxDeauthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDeauthentications.setStatus("current")
_WlanStaRxDeauthentications_Type = Counter32
_WlanStaRxDeauthentications_Object = MibTableColumn
wlanStaRxDeauthentications = _WlanStaRxDeauthentications_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 15),
    _WlanStaRxDeauthentications_Type()
)
wlanStaRxDeauthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxDeauthentications.setStatus("current")
_WlanStaFrameRetryRate_Type = Integer32
_WlanStaFrameRetryRate_Object = MibTableColumn
wlanStaFrameRetryRate = _WlanStaFrameRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 16),
    _WlanStaFrameRetryRate_Type()
)
wlanStaFrameRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameRetryRate.setStatus("current")
_WlanStaFrameLowSpeedRate_Type = Integer32
_WlanStaFrameLowSpeedRate_Object = MibTableColumn
wlanStaFrameLowSpeedRate = _WlanStaFrameLowSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 17),
    _WlanStaFrameLowSpeedRate_Type()
)
wlanStaFrameLowSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameLowSpeedRate.setStatus("current")
_WlanStaFrameNonUnicastRate_Type = Integer32
_WlanStaFrameNonUnicastRate_Object = MibTableColumn
wlanStaFrameNonUnicastRate = _WlanStaFrameNonUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 18),
    _WlanStaFrameNonUnicastRate_Type()
)
wlanStaFrameNonUnicastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameNonUnicastRate.setStatus("current")
_WlanStaFrameFragmentationRate_Type = Integer32
_WlanStaFrameFragmentationRate_Object = MibTableColumn
wlanStaFrameFragmentationRate = _WlanStaFrameFragmentationRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 19),
    _WlanStaFrameFragmentationRate_Type()
)
wlanStaFrameFragmentationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameFragmentationRate.setStatus("current")
_WlanStaFrameBandwidthRate_Type = Integer32
_WlanStaFrameBandwidthRate_Object = MibTableColumn
wlanStaFrameBandwidthRate = _WlanStaFrameBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 20),
    _WlanStaFrameBandwidthRate_Type()
)
wlanStaFrameBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameBandwidthRate.setStatus("current")
_WlanStaFrameRetryErrorRate_Type = Integer32
_WlanStaFrameRetryErrorRate_Object = MibTableColumn
wlanStaFrameRetryErrorRate = _WlanStaFrameRetryErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 21),
    _WlanStaFrameRetryErrorRate_Type()
)
wlanStaFrameRetryErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameRetryErrorRate.setStatus("deprecated")
_WlanStaFrameReceiveErrorRate_Type = Integer32
_WlanStaFrameReceiveErrorRate_Object = MibTableColumn
wlanStaFrameReceiveErrorRate = _WlanStaFrameReceiveErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 22),
    _WlanStaFrameReceiveErrorRate_Type()
)
wlanStaFrameReceiveErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaFrameReceiveErrorRate.setStatus("current")
_WlanStaTxBCastBytes_Type = Counter32
_WlanStaTxBCastBytes_Object = MibTableColumn
wlanStaTxBCastBytes = _WlanStaTxBCastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 23),
    _WlanStaTxBCastBytes_Type()
)
wlanStaTxBCastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBCastBytes.setStatus("current")
_WlanStaTxMCastBytes_Type = Counter32
_WlanStaTxMCastBytes_Object = MibTableColumn
wlanStaTxMCastBytes = _WlanStaTxMCastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 24),
    _WlanStaTxMCastBytes_Type()
)
wlanStaTxMCastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxMCastBytes.setStatus("current")
_WlanStaTxBytes64_Type = Counter64
_WlanStaTxBytes64_Object = MibTableColumn
wlanStaTxBytes64 = _WlanStaTxBytes64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 25),
    _WlanStaTxBytes64_Type()
)
wlanStaTxBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytes64.setStatus("current")
_WlanStaRxBytes64_Type = Counter64
_WlanStaRxBytes64_Object = MibTableColumn
wlanStaRxBytes64 = _WlanStaRxBytes64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 26),
    _WlanStaRxBytes64_Type()
)
wlanStaRxBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytes64.setStatus("current")
_WlanStaStatsPhyType_Type = ArubaPhyType
_WlanStaStatsPhyType_Object = MibTableColumn
wlanStaStatsPhyType = _WlanStaStatsPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 27),
    _WlanStaStatsPhyType_Type()
)
wlanStaStatsPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaStatsPhyType.setStatus("current")
_WlanStaSecChannelNum_Type = Unsigned32
_WlanStaSecChannelNum_Object = MibTableColumn
wlanStaSecChannelNum = _WlanStaSecChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 28),
    _WlanStaSecChannelNum_Type()
)
wlanStaSecChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaSecChannelNum.setStatus("current")
_WlanStaStatsHTMode_Type = ArubaHTMode
_WlanStaStatsHTMode_Object = MibTableColumn
wlanStaStatsHTMode = _WlanStaStatsHTMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 1, 1, 29),
    _WlanStaStatsHTMode_Type()
)
wlanStaStatsHTMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaStatsHTMode.setStatus("current")
_WlsxWlanStaRateStatsTable_Object = MibTable
wlsxWlanStaRateStatsTable = _WlsxWlanStaRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wlsxWlanStaRateStatsTable.setStatus("current")
_WlsxWlanStaRateStatsEntry_Object = MibTableRow
wlsxWlanStaRateStatsEntry = _WlsxWlanStaRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1)
)
wlsxWlanStaRateStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanStaRateStatsEntry.setStatus("current")
_WlanStaTxPktsAt1Mbps_Type = Counter32
_WlanStaTxPktsAt1Mbps_Object = MibTableColumn
wlanStaTxPktsAt1Mbps = _WlanStaTxPktsAt1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 1),
    _WlanStaTxPktsAt1Mbps_Type()
)
wlanStaTxPktsAt1Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt1Mbps.setStatus("current")
_WlanStaTxBytesAt1Mbps_Type = Counter32
_WlanStaTxBytesAt1Mbps_Object = MibTableColumn
wlanStaTxBytesAt1Mbps = _WlanStaTxBytesAt1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 2),
    _WlanStaTxBytesAt1Mbps_Type()
)
wlanStaTxBytesAt1Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt1Mbps.setStatus("current")
_WlanStaTxPktsAt2Mbps_Type = Counter32
_WlanStaTxPktsAt2Mbps_Object = MibTableColumn
wlanStaTxPktsAt2Mbps = _WlanStaTxPktsAt2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 3),
    _WlanStaTxPktsAt2Mbps_Type()
)
wlanStaTxPktsAt2Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt2Mbps.setStatus("current")
_WlanStaTxBytesAt2Mbps_Type = Counter32
_WlanStaTxBytesAt2Mbps_Object = MibTableColumn
wlanStaTxBytesAt2Mbps = _WlanStaTxBytesAt2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 4),
    _WlanStaTxBytesAt2Mbps_Type()
)
wlanStaTxBytesAt2Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt2Mbps.setStatus("current")
_WlanStaTxPktsAt5Mbps_Type = Counter32
_WlanStaTxPktsAt5Mbps_Object = MibTableColumn
wlanStaTxPktsAt5Mbps = _WlanStaTxPktsAt5Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 5),
    _WlanStaTxPktsAt5Mbps_Type()
)
wlanStaTxPktsAt5Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt5Mbps.setStatus("current")
_WlanStaTxBytesAt5Mbps_Type = Counter32
_WlanStaTxBytesAt5Mbps_Object = MibTableColumn
wlanStaTxBytesAt5Mbps = _WlanStaTxBytesAt5Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 6),
    _WlanStaTxBytesAt5Mbps_Type()
)
wlanStaTxBytesAt5Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt5Mbps.setStatus("current")
_WlanStaTxPktsAt11Mbps_Type = Counter32
_WlanStaTxPktsAt11Mbps_Object = MibTableColumn
wlanStaTxPktsAt11Mbps = _WlanStaTxPktsAt11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 7),
    _WlanStaTxPktsAt11Mbps_Type()
)
wlanStaTxPktsAt11Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt11Mbps.setStatus("current")
_WlanStaTxBytesAt11Mbps_Type = Counter32
_WlanStaTxBytesAt11Mbps_Object = MibTableColumn
wlanStaTxBytesAt11Mbps = _WlanStaTxBytesAt11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 8),
    _WlanStaTxBytesAt11Mbps_Type()
)
wlanStaTxBytesAt11Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt11Mbps.setStatus("current")
_WlanStaTxPktsAt6Mbps_Type = Counter32
_WlanStaTxPktsAt6Mbps_Object = MibTableColumn
wlanStaTxPktsAt6Mbps = _WlanStaTxPktsAt6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 9),
    _WlanStaTxPktsAt6Mbps_Type()
)
wlanStaTxPktsAt6Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt6Mbps.setStatus("current")
_WlanStaTxBytesAt6Mbps_Type = Counter32
_WlanStaTxBytesAt6Mbps_Object = MibTableColumn
wlanStaTxBytesAt6Mbps = _WlanStaTxBytesAt6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 10),
    _WlanStaTxBytesAt6Mbps_Type()
)
wlanStaTxBytesAt6Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt6Mbps.setStatus("current")
_WlanStaTxPktsAt12Mbps_Type = Counter32
_WlanStaTxPktsAt12Mbps_Object = MibTableColumn
wlanStaTxPktsAt12Mbps = _WlanStaTxPktsAt12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 11),
    _WlanStaTxPktsAt12Mbps_Type()
)
wlanStaTxPktsAt12Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt12Mbps.setStatus("current")
_WlanStaTxBytesAt12Mbps_Type = Counter32
_WlanStaTxBytesAt12Mbps_Object = MibTableColumn
wlanStaTxBytesAt12Mbps = _WlanStaTxBytesAt12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 12),
    _WlanStaTxBytesAt12Mbps_Type()
)
wlanStaTxBytesAt12Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt12Mbps.setStatus("current")
_WlanStaTxPktsAt18Mbps_Type = Counter32
_WlanStaTxPktsAt18Mbps_Object = MibTableColumn
wlanStaTxPktsAt18Mbps = _WlanStaTxPktsAt18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 13),
    _WlanStaTxPktsAt18Mbps_Type()
)
wlanStaTxPktsAt18Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt18Mbps.setStatus("current")
_WlanStaTxBytesAt18Mbps_Type = Counter32
_WlanStaTxBytesAt18Mbps_Object = MibTableColumn
wlanStaTxBytesAt18Mbps = _WlanStaTxBytesAt18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 14),
    _WlanStaTxBytesAt18Mbps_Type()
)
wlanStaTxBytesAt18Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt18Mbps.setStatus("current")
_WlanStaTxPktsAt24Mbps_Type = Counter32
_WlanStaTxPktsAt24Mbps_Object = MibTableColumn
wlanStaTxPktsAt24Mbps = _WlanStaTxPktsAt24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 15),
    _WlanStaTxPktsAt24Mbps_Type()
)
wlanStaTxPktsAt24Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt24Mbps.setStatus("current")
_WlanStaTxBytesAt24Mbps_Type = Counter32
_WlanStaTxBytesAt24Mbps_Object = MibTableColumn
wlanStaTxBytesAt24Mbps = _WlanStaTxBytesAt24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 16),
    _WlanStaTxBytesAt24Mbps_Type()
)
wlanStaTxBytesAt24Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt24Mbps.setStatus("current")
_WlanStaTxPktsAt36Mbps_Type = Counter32
_WlanStaTxPktsAt36Mbps_Object = MibTableColumn
wlanStaTxPktsAt36Mbps = _WlanStaTxPktsAt36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 17),
    _WlanStaTxPktsAt36Mbps_Type()
)
wlanStaTxPktsAt36Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt36Mbps.setStatus("current")
_WlanStaTxBytesAt36Mbps_Type = Counter32
_WlanStaTxBytesAt36Mbps_Object = MibTableColumn
wlanStaTxBytesAt36Mbps = _WlanStaTxBytesAt36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 18),
    _WlanStaTxBytesAt36Mbps_Type()
)
wlanStaTxBytesAt36Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt36Mbps.setStatus("current")
_WlanStaTxPktsAt48Mbps_Type = Counter32
_WlanStaTxPktsAt48Mbps_Object = MibTableColumn
wlanStaTxPktsAt48Mbps = _WlanStaTxPktsAt48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 19),
    _WlanStaTxPktsAt48Mbps_Type()
)
wlanStaTxPktsAt48Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt48Mbps.setStatus("current")
_WlanStaTxBytesAt48Mbps_Type = Counter32
_WlanStaTxBytesAt48Mbps_Object = MibTableColumn
wlanStaTxBytesAt48Mbps = _WlanStaTxBytesAt48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 20),
    _WlanStaTxBytesAt48Mbps_Type()
)
wlanStaTxBytesAt48Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt48Mbps.setStatus("current")
_WlanStaTxPktsAt54Mbps_Type = Counter32
_WlanStaTxPktsAt54Mbps_Object = MibTableColumn
wlanStaTxPktsAt54Mbps = _WlanStaTxPktsAt54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 21),
    _WlanStaTxPktsAt54Mbps_Type()
)
wlanStaTxPktsAt54Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt54Mbps.setStatus("current")
_WlanStaTxBytesAt54Mbps_Type = Counter32
_WlanStaTxBytesAt54Mbps_Object = MibTableColumn
wlanStaTxBytesAt54Mbps = _WlanStaTxBytesAt54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 22),
    _WlanStaTxBytesAt54Mbps_Type()
)
wlanStaTxBytesAt54Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt54Mbps.setStatus("current")
_WlanStaRxPktsAt1Mbps_Type = Counter32
_WlanStaRxPktsAt1Mbps_Object = MibTableColumn
wlanStaRxPktsAt1Mbps = _WlanStaRxPktsAt1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 23),
    _WlanStaRxPktsAt1Mbps_Type()
)
wlanStaRxPktsAt1Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt1Mbps.setStatus("current")
_WlanStaRxBytesAt1Mbps_Type = Counter32
_WlanStaRxBytesAt1Mbps_Object = MibTableColumn
wlanStaRxBytesAt1Mbps = _WlanStaRxBytesAt1Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 24),
    _WlanStaRxBytesAt1Mbps_Type()
)
wlanStaRxBytesAt1Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt1Mbps.setStatus("current")
_WlanStaRxPktsAt2Mbps_Type = Counter32
_WlanStaRxPktsAt2Mbps_Object = MibTableColumn
wlanStaRxPktsAt2Mbps = _WlanStaRxPktsAt2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 25),
    _WlanStaRxPktsAt2Mbps_Type()
)
wlanStaRxPktsAt2Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt2Mbps.setStatus("current")
_WlanStaRxBytesAt2Mbps_Type = Counter32
_WlanStaRxBytesAt2Mbps_Object = MibTableColumn
wlanStaRxBytesAt2Mbps = _WlanStaRxBytesAt2Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 26),
    _WlanStaRxBytesAt2Mbps_Type()
)
wlanStaRxBytesAt2Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt2Mbps.setStatus("current")
_WlanStaRxPktsAt5Mbps_Type = Counter32
_WlanStaRxPktsAt5Mbps_Object = MibTableColumn
wlanStaRxPktsAt5Mbps = _WlanStaRxPktsAt5Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 27),
    _WlanStaRxPktsAt5Mbps_Type()
)
wlanStaRxPktsAt5Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt5Mbps.setStatus("current")
_WlanStaRxBytesAt5Mbps_Type = Counter32
_WlanStaRxBytesAt5Mbps_Object = MibTableColumn
wlanStaRxBytesAt5Mbps = _WlanStaRxBytesAt5Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 28),
    _WlanStaRxBytesAt5Mbps_Type()
)
wlanStaRxBytesAt5Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt5Mbps.setStatus("current")
_WlanStaRxPktsAt11Mbps_Type = Counter32
_WlanStaRxPktsAt11Mbps_Object = MibTableColumn
wlanStaRxPktsAt11Mbps = _WlanStaRxPktsAt11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 29),
    _WlanStaRxPktsAt11Mbps_Type()
)
wlanStaRxPktsAt11Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt11Mbps.setStatus("current")
_WlanStaRxBytesAt11Mbps_Type = Counter32
_WlanStaRxBytesAt11Mbps_Object = MibTableColumn
wlanStaRxBytesAt11Mbps = _WlanStaRxBytesAt11Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 30),
    _WlanStaRxBytesAt11Mbps_Type()
)
wlanStaRxBytesAt11Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt11Mbps.setStatus("current")
_WlanStaRxPktsAt6Mbps_Type = Counter32
_WlanStaRxPktsAt6Mbps_Object = MibTableColumn
wlanStaRxPktsAt6Mbps = _WlanStaRxPktsAt6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 31),
    _WlanStaRxPktsAt6Mbps_Type()
)
wlanStaRxPktsAt6Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt6Mbps.setStatus("current")
_WlanStaRxBytesAt6Mbps_Type = Counter32
_WlanStaRxBytesAt6Mbps_Object = MibTableColumn
wlanStaRxBytesAt6Mbps = _WlanStaRxBytesAt6Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 32),
    _WlanStaRxBytesAt6Mbps_Type()
)
wlanStaRxBytesAt6Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt6Mbps.setStatus("current")
_WlanStaRxPktsAt12Mbps_Type = Counter32
_WlanStaRxPktsAt12Mbps_Object = MibTableColumn
wlanStaRxPktsAt12Mbps = _WlanStaRxPktsAt12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 33),
    _WlanStaRxPktsAt12Mbps_Type()
)
wlanStaRxPktsAt12Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt12Mbps.setStatus("current")
_WlanStaRxBytesAt12Mbps_Type = Counter32
_WlanStaRxBytesAt12Mbps_Object = MibTableColumn
wlanStaRxBytesAt12Mbps = _WlanStaRxBytesAt12Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 34),
    _WlanStaRxBytesAt12Mbps_Type()
)
wlanStaRxBytesAt12Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt12Mbps.setStatus("current")
_WlanStaRxPktsAt18Mbps_Type = Counter32
_WlanStaRxPktsAt18Mbps_Object = MibTableColumn
wlanStaRxPktsAt18Mbps = _WlanStaRxPktsAt18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 35),
    _WlanStaRxPktsAt18Mbps_Type()
)
wlanStaRxPktsAt18Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt18Mbps.setStatus("current")
_WlanStaRxBytesAt18Mbps_Type = Counter32
_WlanStaRxBytesAt18Mbps_Object = MibTableColumn
wlanStaRxBytesAt18Mbps = _WlanStaRxBytesAt18Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 36),
    _WlanStaRxBytesAt18Mbps_Type()
)
wlanStaRxBytesAt18Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt18Mbps.setStatus("current")
_WlanStaRxPktsAt24Mbps_Type = Counter32
_WlanStaRxPktsAt24Mbps_Object = MibTableColumn
wlanStaRxPktsAt24Mbps = _WlanStaRxPktsAt24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 37),
    _WlanStaRxPktsAt24Mbps_Type()
)
wlanStaRxPktsAt24Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt24Mbps.setStatus("current")
_WlanStaRxBytesAt24Mbps_Type = Counter32
_WlanStaRxBytesAt24Mbps_Object = MibTableColumn
wlanStaRxBytesAt24Mbps = _WlanStaRxBytesAt24Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 38),
    _WlanStaRxBytesAt24Mbps_Type()
)
wlanStaRxBytesAt24Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt24Mbps.setStatus("current")
_WlanStaRxPktsAt36Mbps_Type = Counter32
_WlanStaRxPktsAt36Mbps_Object = MibTableColumn
wlanStaRxPktsAt36Mbps = _WlanStaRxPktsAt36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 39),
    _WlanStaRxPktsAt36Mbps_Type()
)
wlanStaRxPktsAt36Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt36Mbps.setStatus("current")
_WlanStaRxBytesAt36Mbps_Type = Counter32
_WlanStaRxBytesAt36Mbps_Object = MibTableColumn
wlanStaRxBytesAt36Mbps = _WlanStaRxBytesAt36Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 40),
    _WlanStaRxBytesAt36Mbps_Type()
)
wlanStaRxBytesAt36Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt36Mbps.setStatus("current")
_WlanStaRxPktsAt48Mbps_Type = Counter32
_WlanStaRxPktsAt48Mbps_Object = MibTableColumn
wlanStaRxPktsAt48Mbps = _WlanStaRxPktsAt48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 41),
    _WlanStaRxPktsAt48Mbps_Type()
)
wlanStaRxPktsAt48Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt48Mbps.setStatus("current")
_WlanStaRxBytesAt48Mbps_Type = Counter32
_WlanStaRxBytesAt48Mbps_Object = MibTableColumn
wlanStaRxBytesAt48Mbps = _WlanStaRxBytesAt48Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 42),
    _WlanStaRxBytesAt48Mbps_Type()
)
wlanStaRxBytesAt48Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt48Mbps.setStatus("current")
_WlanStaRxPktsAt54Mbps_Type = Counter32
_WlanStaRxPktsAt54Mbps_Object = MibTableColumn
wlanStaRxPktsAt54Mbps = _WlanStaRxPktsAt54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 43),
    _WlanStaRxPktsAt54Mbps_Type()
)
wlanStaRxPktsAt54Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt54Mbps.setStatus("current")
_WlanStaRxBytesAt54Mbps_Type = Counter32
_WlanStaRxBytesAt54Mbps_Object = MibTableColumn
wlanStaRxBytesAt54Mbps = _WlanStaRxBytesAt54Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 44),
    _WlanStaRxBytesAt54Mbps_Type()
)
wlanStaRxBytesAt54Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt54Mbps.setStatus("current")
_WlanStaTxPktsAt9Mbps_Type = Counter32
_WlanStaTxPktsAt9Mbps_Object = MibTableColumn
wlanStaTxPktsAt9Mbps = _WlanStaTxPktsAt9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 45),
    _WlanStaTxPktsAt9Mbps_Type()
)
wlanStaTxPktsAt9Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPktsAt9Mbps.setStatus("current")
_WlanStaTxBytesAt9Mbps_Type = Counter32
_WlanStaTxBytesAt9Mbps_Object = MibTableColumn
wlanStaTxBytesAt9Mbps = _WlanStaTxBytesAt9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 46),
    _WlanStaTxBytesAt9Mbps_Type()
)
wlanStaTxBytesAt9Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxBytesAt9Mbps.setStatus("current")
_WlanStaRxPktsAt9Mbps_Type = Counter32
_WlanStaRxPktsAt9Mbps_Object = MibTableColumn
wlanStaRxPktsAt9Mbps = _WlanStaRxPktsAt9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 47),
    _WlanStaRxPktsAt9Mbps_Type()
)
wlanStaRxPktsAt9Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPktsAt9Mbps.setStatus("current")
_WlanStaRxBytesAt9Mbps_Type = Counter32
_WlanStaRxBytesAt9Mbps_Object = MibTableColumn
wlanStaRxBytesAt9Mbps = _WlanStaRxBytesAt9Mbps_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 2, 1, 48),
    _WlanStaRxBytesAt9Mbps_Type()
)
wlanStaRxBytesAt9Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxBytesAt9Mbps.setStatus("current")
_WlsxWlanStaDATypeStatsTable_Object = MibTable
wlsxWlanStaDATypeStatsTable = _WlsxWlanStaDATypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3)
)
if mibBuilder.loadTexts:
    wlsxWlanStaDATypeStatsTable.setStatus("current")
_WlsxWlanStaDATypeStatsEntry_Object = MibTableRow
wlsxWlanStaDATypeStatsEntry = _WlsxWlanStaDATypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1)
)
wlsxWlanStaDATypeStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanStaDATypeStatsEntry.setStatus("current")
_WlanStaTxDABroadcastPkts_Type = Counter32
_WlanStaTxDABroadcastPkts_Object = MibTableColumn
wlanStaTxDABroadcastPkts = _WlanStaTxDABroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1, 1),
    _WlanStaTxDABroadcastPkts_Type()
)
wlanStaTxDABroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDABroadcastPkts.setStatus("current")
_WlanStaTxDABroadcastBytes_Type = Counter32
_WlanStaTxDABroadcastBytes_Object = MibTableColumn
wlanStaTxDABroadcastBytes = _WlanStaTxDABroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1, 2),
    _WlanStaTxDABroadcastBytes_Type()
)
wlanStaTxDABroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDABroadcastBytes.setStatus("current")
_WlanStaTxDAMulticastPkts_Type = Counter32
_WlanStaTxDAMulticastPkts_Object = MibTableColumn
wlanStaTxDAMulticastPkts = _WlanStaTxDAMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1, 3),
    _WlanStaTxDAMulticastPkts_Type()
)
wlanStaTxDAMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDAMulticastPkts.setStatus("current")
_WlanStaTxDAMulticastBytes_Type = Counter32
_WlanStaTxDAMulticastBytes_Object = MibTableColumn
wlanStaTxDAMulticastBytes = _WlanStaTxDAMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1, 4),
    _WlanStaTxDAMulticastBytes_Type()
)
wlanStaTxDAMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDAMulticastBytes.setStatus("current")
_WlanStaTxDAUnicastPkts_Type = Counter32
_WlanStaTxDAUnicastPkts_Object = MibTableColumn
wlanStaTxDAUnicastPkts = _WlanStaTxDAUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1, 5),
    _WlanStaTxDAUnicastPkts_Type()
)
wlanStaTxDAUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDAUnicastPkts.setStatus("current")
_WlanStaTxDAUnicastBytes_Type = Counter32
_WlanStaTxDAUnicastBytes_Object = MibTableColumn
wlanStaTxDAUnicastBytes = _WlanStaTxDAUnicastBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 3, 1, 6),
    _WlanStaTxDAUnicastBytes_Type()
)
wlanStaTxDAUnicastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDAUnicastBytes.setStatus("current")
_WlsxWlanStaFrameTypeStatsTable_Object = MibTable
wlsxWlanStaFrameTypeStatsTable = _WlsxWlanStaFrameTypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4)
)
if mibBuilder.loadTexts:
    wlsxWlanStaFrameTypeStatsTable.setStatus("current")
_WlsxWlanStaFrameTypeStatsEntry_Object = MibTableRow
wlsxWlanStaFrameTypeStatsEntry = _WlsxWlanStaFrameTypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1)
)
wlsxWlanStaFrameTypeStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanStaFrameTypeStatsEntry.setStatus("current")
_WlanStaTxMgmtPkts_Type = Counter32
_WlanStaTxMgmtPkts_Object = MibTableColumn
wlanStaTxMgmtPkts = _WlanStaTxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 1),
    _WlanStaTxMgmtPkts_Type()
)
wlanStaTxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxMgmtPkts.setStatus("current")
_WlanStaTxMgmtBytes_Type = Counter32
_WlanStaTxMgmtBytes_Object = MibTableColumn
wlanStaTxMgmtBytes = _WlanStaTxMgmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 2),
    _WlanStaTxMgmtBytes_Type()
)
wlanStaTxMgmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxMgmtBytes.setStatus("current")
_WlanStaTxCtrlPkts_Type = Counter32
_WlanStaTxCtrlPkts_Object = MibTableColumn
wlanStaTxCtrlPkts = _WlanStaTxCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 3),
    _WlanStaTxCtrlPkts_Type()
)
wlanStaTxCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxCtrlPkts.setStatus("current")
_WlanStaTxCtrlBytes_Type = Counter32
_WlanStaTxCtrlBytes_Object = MibTableColumn
wlanStaTxCtrlBytes = _WlanStaTxCtrlBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 4),
    _WlanStaTxCtrlBytes_Type()
)
wlanStaTxCtrlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxCtrlBytes.setStatus("current")
_WlanStaTxDataPkts_Type = Counter32
_WlanStaTxDataPkts_Object = MibTableColumn
wlanStaTxDataPkts = _WlanStaTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 5),
    _WlanStaTxDataPkts_Type()
)
wlanStaTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDataPkts.setStatus("current")
_WlanStaTxDataBytes_Type = Counter32
_WlanStaTxDataBytes_Object = MibTableColumn
wlanStaTxDataBytes = _WlanStaTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 6),
    _WlanStaTxDataBytes_Type()
)
wlanStaTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxDataBytes.setStatus("current")
_WlanStaRxMgmtPkts_Type = Counter32
_WlanStaRxMgmtPkts_Object = MibTableColumn
wlanStaRxMgmtPkts = _WlanStaRxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 7),
    _WlanStaRxMgmtPkts_Type()
)
wlanStaRxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxMgmtPkts.setStatus("current")
_WlanStaRxMgmtBytes_Type = Counter32
_WlanStaRxMgmtBytes_Object = MibTableColumn
wlanStaRxMgmtBytes = _WlanStaRxMgmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 8),
    _WlanStaRxMgmtBytes_Type()
)
wlanStaRxMgmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxMgmtBytes.setStatus("current")
_WlanStaRxCtrlPkts_Type = Counter32
_WlanStaRxCtrlPkts_Object = MibTableColumn
wlanStaRxCtrlPkts = _WlanStaRxCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 9),
    _WlanStaRxCtrlPkts_Type()
)
wlanStaRxCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxCtrlPkts.setStatus("current")
_WlanStaRxCtrlBytes_Type = Counter32
_WlanStaRxCtrlBytes_Object = MibTableColumn
wlanStaRxCtrlBytes = _WlanStaRxCtrlBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 10),
    _WlanStaRxCtrlBytes_Type()
)
wlanStaRxCtrlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxCtrlBytes.setStatus("current")
_WlanStaRxDataPkts_Type = Counter32
_WlanStaRxDataPkts_Object = MibTableColumn
wlanStaRxDataPkts = _WlanStaRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 11),
    _WlanStaRxDataPkts_Type()
)
wlanStaRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxDataPkts.setStatus("current")
_WlanStaRxDataBytes_Type = Counter32
_WlanStaRxDataBytes_Object = MibTableColumn
wlanStaRxDataBytes = _WlanStaRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 4, 1, 12),
    _WlanStaRxDataBytes_Type()
)
wlanStaRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxDataBytes.setStatus("current")
_WlsxWlanStaPktSizeStatsTable_Object = MibTable
wlsxWlanStaPktSizeStatsTable = _WlsxWlanStaPktSizeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5)
)
if mibBuilder.loadTexts:
    wlsxWlanStaPktSizeStatsTable.setStatus("current")
_WlsxWlanStaPktSizeStatsEntry_Object = MibTableRow
wlsxWlanStaPktSizeStatsEntry = _WlsxWlanStaPktSizeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1)
)
wlsxWlanStaPktSizeStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxWlanStaPktSizeStatsEntry.setStatus("current")
_WlanStaTxPkts63Bytes_Type = Counter32
_WlanStaTxPkts63Bytes_Object = MibTableColumn
wlanStaTxPkts63Bytes = _WlanStaTxPkts63Bytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 1),
    _WlanStaTxPkts63Bytes_Type()
)
wlanStaTxPkts63Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts63Bytes.setStatus("current")
_WlanStaTxPkts64To127_Type = Counter32
_WlanStaTxPkts64To127_Object = MibTableColumn
wlanStaTxPkts64To127 = _WlanStaTxPkts64To127_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 2),
    _WlanStaTxPkts64To127_Type()
)
wlanStaTxPkts64To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts64To127.setStatus("current")
_WlanStaTxPkts128To255_Type = Counter32
_WlanStaTxPkts128To255_Object = MibTableColumn
wlanStaTxPkts128To255 = _WlanStaTxPkts128To255_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 3),
    _WlanStaTxPkts128To255_Type()
)
wlanStaTxPkts128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts128To255.setStatus("current")
_WlanStaTxPkts256To511_Type = Counter32
_WlanStaTxPkts256To511_Object = MibTableColumn
wlanStaTxPkts256To511 = _WlanStaTxPkts256To511_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 4),
    _WlanStaTxPkts256To511_Type()
)
wlanStaTxPkts256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts256To511.setStatus("current")
_WlanStaTxPkts512To1023_Type = Counter32
_WlanStaTxPkts512To1023_Object = MibTableColumn
wlanStaTxPkts512To1023 = _WlanStaTxPkts512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 5),
    _WlanStaTxPkts512To1023_Type()
)
wlanStaTxPkts512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts512To1023.setStatus("current")
_WlanStaTxPkts1024To1518_Type = Counter32
_WlanStaTxPkts1024To1518_Object = MibTableColumn
wlanStaTxPkts1024To1518 = _WlanStaTxPkts1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 6),
    _WlanStaTxPkts1024To1518_Type()
)
wlanStaTxPkts1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaTxPkts1024To1518.setStatus("current")
_WlanStaRxPkts63Bytes_Type = Counter32
_WlanStaRxPkts63Bytes_Object = MibTableColumn
wlanStaRxPkts63Bytes = _WlanStaRxPkts63Bytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 7),
    _WlanStaRxPkts63Bytes_Type()
)
wlanStaRxPkts63Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts63Bytes.setStatus("current")
_WlanStaRxPkts64To127_Type = Counter32
_WlanStaRxPkts64To127_Object = MibTableColumn
wlanStaRxPkts64To127 = _WlanStaRxPkts64To127_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 8),
    _WlanStaRxPkts64To127_Type()
)
wlanStaRxPkts64To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts64To127.setStatus("current")
_WlanStaRxPkts128To255_Type = Counter32
_WlanStaRxPkts128To255_Object = MibTableColumn
wlanStaRxPkts128To255 = _WlanStaRxPkts128To255_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 9),
    _WlanStaRxPkts128To255_Type()
)
wlanStaRxPkts128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts128To255.setStatus("current")
_WlanStaRxPkts256To511_Type = Counter32
_WlanStaRxPkts256To511_Object = MibTableColumn
wlanStaRxPkts256To511 = _WlanStaRxPkts256To511_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 10),
    _WlanStaRxPkts256To511_Type()
)
wlanStaRxPkts256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts256To511.setStatus("current")
_WlanStaRxPkts512To1023_Type = Counter32
_WlanStaRxPkts512To1023_Object = MibTableColumn
wlanStaRxPkts512To1023 = _WlanStaRxPkts512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 11),
    _WlanStaRxPkts512To1023_Type()
)
wlanStaRxPkts512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts512To1023.setStatus("current")
_WlanStaRxPkts1024To1518_Type = Counter32
_WlanStaRxPkts1024To1518_Object = MibTableColumn
wlanStaRxPkts1024To1518 = _WlanStaRxPkts1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 2, 5, 1, 12),
    _WlanStaRxPkts1024To1518_Type()
)
wlanStaRxPkts1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStaRxPkts1024To1518.setStatus("current")
_WlsxWlanSwitchStatsGroup_ObjectIdentity = ObjectIdentity
wlsxWlanSwitchStatsGroup = _WlsxWlanSwitchStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3)
)
_WlsxWlanESSIDStatsTable_Object = MibTable
wlsxWlanESSIDStatsTable = _WlsxWlanESSIDStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    wlsxWlanESSIDStatsTable.setStatus("current")
_WlsxWlanESSIDStatsEntry_Object = MibTableRow
wlsxWlanESSIDStatsEntry = _WlsxWlanESSIDStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1)
)
wlsxWlanESSIDStatsEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanESSID"),
)
if mibBuilder.loadTexts:
    wlsxWlanESSIDStatsEntry.setStatus("current")
_WlanESSIDRxPkts_Type = Counter32
_WlanESSIDRxPkts_Object = MibTableColumn
wlanESSIDRxPkts = _WlanESSIDRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 1),
    _WlanESSIDRxPkts_Type()
)
wlanESSIDRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDRxPkts.setStatus("current")
_WlanESSIDRxDroppedPkts_Type = Counter32
_WlanESSIDRxDroppedPkts_Object = MibTableColumn
wlanESSIDRxDroppedPkts = _WlanESSIDRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 2),
    _WlanESSIDRxDroppedPkts_Type()
)
wlanESSIDRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDRxDroppedPkts.setStatus("current")
_WlanESSIDRxRetryPkts_Type = Counter32
_WlanESSIDRxRetryPkts_Object = MibTableColumn
wlanESSIDRxRetryPkts = _WlanESSIDRxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 3),
    _WlanESSIDRxRetryPkts_Type()
)
wlanESSIDRxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDRxRetryPkts.setStatus("current")
_WlanESSIDTxPkts_Type = Counter32
_WlanESSIDTxPkts_Object = MibTableColumn
wlanESSIDTxPkts = _WlanESSIDTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 4),
    _WlanESSIDTxPkts_Type()
)
wlanESSIDTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDTxPkts.setStatus("current")
_WlanESSIDTxDroppedPkts_Type = Counter32
_WlanESSIDTxDroppedPkts_Object = MibTableColumn
wlanESSIDTxDroppedPkts = _WlanESSIDTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 5),
    _WlanESSIDTxDroppedPkts_Type()
)
wlanESSIDTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDTxDroppedPkts.setStatus("current")
_WlanESSIDTxRetryPkts_Type = Counter32
_WlanESSIDTxRetryPkts_Object = MibTableColumn
wlanESSIDTxRetryPkts = _WlanESSIDTxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 6),
    _WlanESSIDTxRetryPkts_Type()
)
wlanESSIDTxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDTxRetryPkts.setStatus("current")
_WlanESSIDTxErrorPkts_Type = Counter32
_WlanESSIDTxErrorPkts_Object = MibTableColumn
wlanESSIDTxErrorPkts = _WlanESSIDTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 7),
    _WlanESSIDTxErrorPkts_Type()
)
wlanESSIDTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDTxErrorPkts.setStatus("current")
_WlanESSIDRxRate_Type = Gauge32
_WlanESSIDRxRate_Object = MibTableColumn
wlanESSIDRxRate = _WlanESSIDRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 8),
    _WlanESSIDRxRate_Type()
)
wlanESSIDRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDRxRate.setStatus("current")
_WlanESSIDTxRate_Type = Gauge32
_WlanESSIDTxRate_Object = MibTableColumn
wlanESSIDTxRate = _WlanESSIDTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 9),
    _WlanESSIDTxRate_Type()
)
wlanESSIDTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDTxRate.setStatus("current")
_WlanESSIDWiredRxPkts_Type = Counter32
_WlanESSIDWiredRxPkts_Object = MibTableColumn
wlanESSIDWiredRxPkts = _WlanESSIDWiredRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 10),
    _WlanESSIDWiredRxPkts_Type()
)
wlanESSIDWiredRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDWiredRxPkts.setStatus("current")
_WlanESSIDWiredRxBytes_Type = Counter32
_WlanESSIDWiredRxBytes_Object = MibTableColumn
wlanESSIDWiredRxBytes = _WlanESSIDWiredRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 11),
    _WlanESSIDWiredRxBytes_Type()
)
wlanESSIDWiredRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDWiredRxBytes.setStatus("current")
_WlanESSIDWiredTxBytes_Type = Counter32
_WlanESSIDWiredTxBytes_Object = MibTableColumn
wlanESSIDWiredTxBytes = _WlanESSIDWiredTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 1, 1, 12),
    _WlanESSIDWiredTxBytes_Type()
)
wlanESSIDWiredTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanESSIDWiredTxBytes.setStatus("current")
_WlsxWlanEthStatsTable_Object = MibTable
wlsxWlanEthStatsTable = _WlsxWlanEthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 2)
)
if mibBuilder.loadTexts:
    wlsxWlanEthStatsTable.setStatus("current")
_WlsxWlanEthStatsEntry_Object = MibTableRow
wlsxWlanEthStatsEntry = _WlsxWlanEthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 2, 1)
)
wlsxWlanEthStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wlsxWlanEthStatsEntry.setStatus("current")
_WlanEthRxRate_Type = Gauge32
_WlanEthRxRate_Object = MibTableColumn
wlanEthRxRate = _WlanEthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 2, 1, 1),
    _WlanEthRxRate_Type()
)
wlanEthRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanEthRxRate.setStatus("current")
_WlanEthTxRate_Type = Gauge32
_WlanEthTxRate_Object = MibTableColumn
wlanEthTxRate = _WlanEthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 3, 3, 2, 1, 2),
    _WlanEthTxRate_Type()
)
wlanEthTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanEthTxRate.setStatus("current")
_WlsxRAPTraps_ObjectIdentity = ObjectIdentity
wlsxRAPTraps = _WlsxRAPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 100)
)

# Managed Objects groups


# Notification objects

wlsxRAPActiveUplink = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 5, 100, 1)
)
wlsxRAPActiveUplink.setObjects(
      *(("WLSX-WLAN-MIB", "wlanAPActiveUplink"),
        ("WLSX-WLAN-MIB", "wlanAPMacAddress"))
)
if mibBuilder.loadTexts:
    wlsxRAPActiveUplink.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-WLAN-MIB",
    **{"wlsxWlanMIB": wlsxWlanMIB,
       "wlsxWlanConfigGroup": wlsxWlanConfigGroup,
       "wlsxSSIDConfigGroup": wlsxSSIDConfigGroup,
       "wlsxSSIDConfigTable": wlsxSSIDConfigTable,
       "wlsxSSIDConfigEntry": wlsxSSIDConfigEntry,
       "wlanESSIDIndex": wlanESSIDIndex,
       "wlanSSIDConfigHideSSID": wlanSSIDConfigHideSSID,
       "wlanSSIDConfigNumStaAllowed": wlanSSIDConfigNumStaAllowed,
       "wlanSSIDConfigWmmBeDscp": wlanSSIDConfigWmmBeDscp,
       "wlanSSIDConfigWmmBkDscp": wlanSSIDConfigWmmBkDscp,
       "wlanSSIDConfigWmmViDscp": wlanSSIDConfigWmmViDscp,
       "wlanSSIDConfigWmmVoDscp": wlanSSIDConfigWmmVoDscp,
       "wlsxAPConfigGroup": wlsxAPConfigGroup,
       "wlsxAPConfigTable": wlsxAPConfigTable,
       "wlsxAPConfigEntry": wlsxAPConfigEntry,
       "wlanAPConfigNetmask": wlanAPConfigNetmask,
       "wlanAPConfigGateway": wlanAPConfigGateway,
       "wlsxWlanStateGroup": wlsxWlanStateGroup,
       "wlsxWlanAccessPointInfoGroup": wlsxWlanAccessPointInfoGroup,
       "wlsxWlanTotalNumAccessPoints": wlsxWlanTotalNumAccessPoints,
       "wlsxWlanTotalNumStationsAssociated": wlsxWlanTotalNumStationsAssociated,
       "wlsxWlanAPGroupTable": wlsxWlanAPGroupTable,
       "wlsxWlanAPGroupEntry": wlsxWlanAPGroupEntry,
       "wlanAPGroup": wlanAPGroup,
       "wlanAPNumAps": wlanAPNumAps,
       "wlsxWlanAPTable": wlsxWlanAPTable,
       "wlsxWlanAPEntry": wlsxWlanAPEntry,
       "wlanAPMacAddress": wlanAPMacAddress,
       "wlanAPIpAddress": wlanAPIpAddress,
       "wlanAPName": wlanAPName,
       "wlanAPGroupName": wlanAPGroupName,
       "wlanAPModel": wlanAPModel,
       "wlanAPSerialNumber": wlanAPSerialNumber,
       "wlanAPdot11aAntennaGain": wlanAPdot11aAntennaGain,
       "wlanAPdot11gAntennaGain": wlanAPdot11gAntennaGain,
       "wlanAPNumRadios": wlanAPNumRadios,
       "wlanAPEnet1Mode": wlanAPEnet1Mode,
       "wlanAPIpsecMode": wlanAPIpsecMode,
       "wlanAPUpTime": wlanAPUpTime,
       "wlanAPModelName": wlanAPModelName,
       "wlanAPLocation": wlanAPLocation,
       "wlanAPBuilding": wlanAPBuilding,
       "wlanAPFloor": wlanAPFloor,
       "wlanAPLoc": wlanAPLoc,
       "wlanAPExternalAntenna": wlanAPExternalAntenna,
       "wlanAPStatus": wlanAPStatus,
       "wlanAPNumBootstraps": wlanAPNumBootstraps,
       "wlanAPNumReboots": wlanAPNumReboots,
       "wlanAPUnprovisioned": wlanAPUnprovisioned,
       "wlanAPMonitorMode": wlanAPMonitorMode,
       "wlanAPFQLNBuilding": wlanAPFQLNBuilding,
       "wlanAPFQLNFloor": wlanAPFQLNFloor,
       "wlanAPFQLN": wlanAPFQLN,
       "wlanAPFQLNCampus": wlanAPFQLNCampus,
       "wlanAPLongitude": wlanAPLongitude,
       "wlanAPLatitude": wlanAPLatitude,
       "wlanAPAltitude": wlanAPAltitude,
       "wlanAPMeshRole": wlanAPMeshRole,
       "wlanAPSysLocation": wlanAPSysLocation,
       "wlanAPHwVersion": wlanAPHwVersion,
       "wlanAPSwVersion": wlanAPSwVersion,
       "wlanAPNumWarmReboots": wlanAPNumWarmReboots,
       "wlanAPOuterIpAddress": wlanAPOuterIpAddress,
       "wlanAPRemoteLanIpAddress": wlanAPRemoteLanIpAddress,
       "wlanAPActiveUplink": wlanAPActiveUplink,
       "wlanAPSwitchIpAddress": wlanAPSwitchIpAddress,
       "wlanAPStandbyIpAddress": wlanAPStandbyIpAddress,
       "wlanAPConnectedAsStandby": wlanAPConnectedAsStandby,
       "wlanAPServiceTag": wlanAPServiceTag,
       "wlanAPConnectedAsDatazone": wlanAPConnectedAsDatazone,
       "wlanAPIpv6Address": wlanAPIpv6Address,
       "wlanAPFlexRadioMode": wlanAPFlexRadioMode,
       "wlanAPdot11aAntennaGain10x": wlanAPdot11aAntennaGain10x,
       "wlanAPdot11gAntennaGain10x": wlanAPdot11gAntennaGain10x,
       "wlanAPDual5GMode": wlanAPDual5GMode,
       "wlanAPActiveIpAddress": wlanAPActiveIpAddress,
       "wlanAPSplit5GMode": wlanAPSplit5GMode,
       "wlanAPOuterIpv6Address": wlanAPOuterIpv6Address,
       "wlanAPRemoteLanIpv6Address": wlanAPRemoteLanIpv6Address,
       "wlsxWlanRadioTable": wlsxWlanRadioTable,
       "wlsxWlanRadioEntry": wlsxWlanRadioEntry,
       "wlanAPRadioNumber": wlanAPRadioNumber,
       "wlanAPRadioType": wlanAPRadioType,
       "wlanAPRadioChannel": wlanAPRadioChannel,
       "wlanAPRadioTransmitPower": wlanAPRadioTransmitPower,
       "wlanAPRadioMode": wlanAPRadioMode,
       "wlanAPRadioUtilization": wlanAPRadioUtilization,
       "wlanAPRadioNumAssociatedClients": wlanAPRadioNumAssociatedClients,
       "wlanAPRadioNumMonitoredClients": wlanAPRadioNumMonitoredClients,
       "wlanAPRadioNumActiveBSSIDs": wlanAPRadioNumActiveBSSIDs,
       "wlanAPRadioNumMonitoredBSSIDs": wlanAPRadioNumMonitoredBSSIDs,
       "wlanAPRadioBearing": wlanAPRadioBearing,
       "wlanAPRadioTiltAngle": wlanAPRadioTiltAngle,
       "wlanAPRadioHTMode": wlanAPRadioHTMode,
       "wlanAPRadioHTExtChannel": wlanAPRadioHTExtChannel,
       "wlanAPRadioHTChannel": wlanAPRadioHTChannel,
       "wlanAPRadioAPName": wlanAPRadioAPName,
       "wlanAPRadioTransmitPower10x": wlanAPRadioTransmitPower10x,
       "wlanAPRadioSecChannel": wlanAPRadioSecChannel,
       "wlsxWlanAPBssidTable": wlsxWlanAPBssidTable,
       "wlsxWlanAPBssidEntry": wlsxWlanAPBssidEntry,
       "wlanAPBSSID": wlanAPBSSID,
       "wlanAPESSID": wlanAPESSID,
       "wlanAPBssidSlot": wlanAPBssidSlot,
       "wlanAPBssidPort": wlanAPBssidPort,
       "wlanAPBssidPhyType": wlanAPBssidPhyType,
       "wlanAPBssidRogueType": wlanAPBssidRogueType,
       "wlanAPBssidMode": wlanAPBssidMode,
       "wlanAPBssidChannel": wlanAPBssidChannel,
       "wlanAPBssidUpTime": wlanAPBssidUpTime,
       "wlanAPBssidInactiveTime": wlanAPBssidInactiveTime,
       "wlanAPBssidLoadBalancing": wlanAPBssidLoadBalancing,
       "wlanAPBssidNumAssociatedStations": wlanAPBssidNumAssociatedStations,
       "wlanAPBssidAPMacAddress": wlanAPBssidAPMacAddress,
       "wlanAPBssidPhyNumber": wlanAPBssidPhyNumber,
       "wlanAPBssidHTMode": wlanAPBssidHTMode,
       "wlanAPBssidHTExtChannel": wlanAPBssidHTExtChannel,
       "wlanAPBssidHTChannel": wlanAPBssidHTChannel,
       "wlanAPBssidSnr": wlanAPBssidSnr,
       "wlanAPBssidChannelV2": wlanAPBssidChannelV2,
       "wlanAPBssidSecChannel": wlanAPBssidSecChannel,
       "wlsxWlanESSIDTable": wlsxWlanESSIDTable,
       "wlsxWlanESSIDEntry": wlsxWlanESSIDEntry,
       "wlanESSID": wlanESSID,
       "wlanESSIDNumStations": wlanESSIDNumStations,
       "wlanESSIDNumAccessPointsUp": wlanESSIDNumAccessPointsUp,
       "wlanESSIDNumAccessPointsDown": wlanESSIDNumAccessPointsDown,
       "wlanESSIDEncryptionType": wlanESSIDEncryptionType,
       "wlsxWlanESSIDVlanPoolTable": wlsxWlanESSIDVlanPoolTable,
       "wlsxWlanESSIDVlanPoolEntry": wlsxWlanESSIDVlanPoolEntry,
       "wlanESSIDVlanId": wlanESSIDVlanId,
       "wlanESSIDVlanPoolStatus": wlanESSIDVlanPoolStatus,
       "wlsxWlanStationInfoGroup": wlsxWlanStationInfoGroup,
       "wlsxWlanStationTable": wlsxWlanStationTable,
       "wlsxWlanStationEntry": wlsxWlanStationEntry,
       "wlanStaPhyAddress": wlanStaPhyAddress,
       "wlanStaApBssid": wlanStaApBssid,
       "wlanStaPhyType": wlanStaPhyType,
       "wlanStaIsAuthenticated": wlanStaIsAuthenticated,
       "wlanStaIsAssociated": wlanStaIsAssociated,
       "wlanStaChannel": wlanStaChannel,
       "wlanStaVlanId": wlanStaVlanId,
       "wlanStaVOIPState": wlanStaVOIPState,
       "wlanStaVOIPProtocol": wlanStaVOIPProtocol,
       "wlanStaTransmitRate": wlanStaTransmitRate,
       "wlanStaAssociationID": wlanStaAssociationID,
       "wlanStaAccessPointESSID": wlanStaAccessPointESSID,
       "wlanStaPhyNumber": wlanStaPhyNumber,
       "wlanStaRSSI": wlanStaRSSI,
       "wlanStaUpTime": wlanStaUpTime,
       "wlanStaHTMode": wlanStaHTMode,
       "wlanStaTransmitRateCode": wlanStaTransmitRateCode,
       "wlanStaChannelV2": wlanStaChannelV2,
       "wlanStaSecChannel": wlanStaSecChannel,
       "wlanStaApName": wlanStaApName,
       "wlsxWlanStaAssociationFailureTable": wlsxWlanStaAssociationFailureTable,
       "wlsxWlanStaAssociationFailureEntry": wlsxWlanStaAssociationFailureEntry,
       "wlanStaAssocFailureApName": wlanStaAssocFailureApName,
       "wlanStaAssocFailureApEssid": wlanStaAssocFailureApEssid,
       "wlanStaAssocFailurePhyNum": wlanStaAssocFailurePhyNum,
       "wlanStaAssocFailurePhyType": wlanStaAssocFailurePhyType,
       "wlanStaAssocFailureElapsedTime": wlanStaAssocFailureElapsedTime,
       "wlanStaAssocFailureReason": wlanStaAssocFailureReason,
       "wlsxWlanAssociationInfoGroup": wlsxWlanAssociationInfoGroup,
       "wlsxWlanStatsGroup": wlsxWlanStatsGroup,
       "wlsxWlanAccessPointStatsGroup": wlsxWlanAccessPointStatsGroup,
       "wlsxWlanAPStatsTable": wlsxWlanAPStatsTable,
       "wlsxWlanAPStatsEntry": wlsxWlanAPStatsEntry,
       "wlanAPCurrentChannel": wlanAPCurrentChannel,
       "wlanAPNumClients": wlanAPNumClients,
       "wlanAPTxPkts": wlanAPTxPkts,
       "wlanAPTxBytes": wlanAPTxBytes,
       "wlanAPRxPkts": wlanAPRxPkts,
       "wlanAPRxBytes": wlanAPRxBytes,
       "wlanAPTxDeauthentications": wlanAPTxDeauthentications,
       "wlanAPRxDeauthentications": wlanAPRxDeauthentications,
       "wlanAPChannelThroughput": wlanAPChannelThroughput,
       "wlanAPFrameRetryRate": wlanAPFrameRetryRate,
       "wlanAPFrameLowSpeedRate": wlanAPFrameLowSpeedRate,
       "wlanAPFrameNonUnicastRate": wlanAPFrameNonUnicastRate,
       "wlanAPFrameFragmentationRate": wlanAPFrameFragmentationRate,
       "wlanAPFrameBandwidthRate": wlanAPFrameBandwidthRate,
       "wlanAPFrameRetryErrorRate": wlanAPFrameRetryErrorRate,
       "wlanAPChannelErrorRate": wlanAPChannelErrorRate,
       "wlanAPFrameReceiveErrorRate": wlanAPFrameReceiveErrorRate,
       "wlanAPRxDataPkts": wlanAPRxDataPkts,
       "wlanAPRxDataBytes": wlanAPRxDataBytes,
       "wlanAPTxDataPkts": wlanAPTxDataPkts,
       "wlanAPTxDataBytes": wlanAPTxDataBytes,
       "wlanAPRxDataPkts64": wlanAPRxDataPkts64,
       "wlanAPRxDataBytes64": wlanAPRxDataBytes64,
       "wlanAPTxDataPkts64": wlanAPTxDataPkts64,
       "wlanAPTxDataBytes64": wlanAPTxDataBytes64,
       "wlanAPWiredRxErrorPkts": wlanAPWiredRxErrorPkts,
       "wlanAPRxErrorPkts": wlanAPRxErrorPkts,
       "wlanAPHTMode": wlanAPHTMode,
       "wlanAPPhyType": wlanAPPhyType,
       "wlanAPCurrentSecChannel": wlanAPCurrentSecChannel,
       "wlsxWlanAPRateStatsTable": wlsxWlanAPRateStatsTable,
       "wlsxWlanAPRateStatsEntry": wlsxWlanAPRateStatsEntry,
       "wlanAPStatsTotPktsAt1Mbps": wlanAPStatsTotPktsAt1Mbps,
       "wlanAPStatsTotBytesAt1Mbps": wlanAPStatsTotBytesAt1Mbps,
       "wlanAPStatsTotPktsAt2Mbps": wlanAPStatsTotPktsAt2Mbps,
       "wlanAPStatsTotBytesAt2Mbps": wlanAPStatsTotBytesAt2Mbps,
       "wlanAPStatsTotPktsAt5Mbps": wlanAPStatsTotPktsAt5Mbps,
       "wlanAPStatsTotBytesAt5Mbps": wlanAPStatsTotBytesAt5Mbps,
       "wlanAPStatsTotPktsAt11Mbps": wlanAPStatsTotPktsAt11Mbps,
       "wlanAPStatsTotBytesAt11Mbps": wlanAPStatsTotBytesAt11Mbps,
       "wlanAPStatsTotPktsAt6Mbps": wlanAPStatsTotPktsAt6Mbps,
       "wlanAPStatsTotBytesAt6Mbps": wlanAPStatsTotBytesAt6Mbps,
       "wlanAPStatsTotPktsAt12Mbps": wlanAPStatsTotPktsAt12Mbps,
       "wlanAPStatsTotBytesAt12Mbps": wlanAPStatsTotBytesAt12Mbps,
       "wlanAPStatsTotPktsAt18Mbps": wlanAPStatsTotPktsAt18Mbps,
       "wlanAPStatsTotBytesAt18Mbps": wlanAPStatsTotBytesAt18Mbps,
       "wlanAPStatsTotPktsAt24Mbps": wlanAPStatsTotPktsAt24Mbps,
       "wlanAPStatsTotBytesAt24Mbps": wlanAPStatsTotBytesAt24Mbps,
       "wlanAPStatsTotPktsAt36Mbps": wlanAPStatsTotPktsAt36Mbps,
       "wlanAPStatsTotBytesAt36Mbps": wlanAPStatsTotBytesAt36Mbps,
       "wlanAPStatsTotPktsAt48Mbps": wlanAPStatsTotPktsAt48Mbps,
       "wlanAPStatsTotBytesAt48Mbps": wlanAPStatsTotBytesAt48Mbps,
       "wlanAPStatsTotPktsAt54Mbps": wlanAPStatsTotPktsAt54Mbps,
       "wlanAPStatsTotBytesAt54Mbps": wlanAPStatsTotBytesAt54Mbps,
       "wlanAPStatsTotPktsAt9Mbps": wlanAPStatsTotPktsAt9Mbps,
       "wlanAPStatsTotBytesAt9Mbps": wlanAPStatsTotBytesAt9Mbps,
       "wlsxWlanAPDATypeStatsTable": wlsxWlanAPDATypeStatsTable,
       "wlsxWlanAPDATypeStatsEntry": wlsxWlanAPDATypeStatsEntry,
       "wlanAPStatsTotDABroadcastPkts": wlanAPStatsTotDABroadcastPkts,
       "wlanAPStatsTotDABroadcastBytes": wlanAPStatsTotDABroadcastBytes,
       "wlanAPStatsTotDAMulticastPkts": wlanAPStatsTotDAMulticastPkts,
       "wlanAPStatsTotDAMulticastBytes": wlanAPStatsTotDAMulticastBytes,
       "wlanAPStatsTotDAUnicastPkts": wlanAPStatsTotDAUnicastPkts,
       "wlanAPStatsTotDAUnicastBytes": wlanAPStatsTotDAUnicastBytes,
       "wlsxWlanAPFrameTypeStatsTable": wlsxWlanAPFrameTypeStatsTable,
       "wlsxWlanAPFrameTypeStatsEntry": wlsxWlanAPFrameTypeStatsEntry,
       "wlanAPStatsTotMgmtPkts": wlanAPStatsTotMgmtPkts,
       "wlanAPStatsTotMgmtBytes": wlanAPStatsTotMgmtBytes,
       "wlanAPStatsTotCtrlPkts": wlanAPStatsTotCtrlPkts,
       "wlanAPStatsTotCtrlBytes": wlanAPStatsTotCtrlBytes,
       "wlanAPStatsTotDataPkts": wlanAPStatsTotDataPkts,
       "wlanAPStatsTotDataBytes": wlanAPStatsTotDataBytes,
       "wlsxWlanAPPktSizeStatsTable": wlsxWlanAPPktSizeStatsTable,
       "wlsxWlanAPPktSizeStatsEntry": wlsxWlanAPPktSizeStatsEntry,
       "wlanAPStatsPkts63Bytes": wlanAPStatsPkts63Bytes,
       "wlanAPStatsPkts64To127": wlanAPStatsPkts64To127,
       "wlanAPStatsPkts128To255": wlanAPStatsPkts128To255,
       "wlanAPStatsPkts256To511": wlanAPStatsPkts256To511,
       "wlanAPStatsPkts512To1023": wlanAPStatsPkts512To1023,
       "wlanAPStatsPkts1024To1518": wlanAPStatsPkts1024To1518,
       "wlsxWlanAPChStatsTable": wlsxWlanAPChStatsTable,
       "wlsxWlanAPChStatsEntry": wlsxWlanAPChStatsEntry,
       "wlanAPChannelNumber": wlanAPChannelNumber,
       "wlanAPChNumStations": wlanAPChNumStations,
       "wlanAPChTotPkts": wlanAPChTotPkts,
       "wlanAPChTotBytes": wlanAPChTotBytes,
       "wlanAPChTotRetryPkts": wlanAPChTotRetryPkts,
       "wlanAPChTotFragmentedPkts": wlanAPChTotFragmentedPkts,
       "wlanAPChTotPhyErrPkts": wlanAPChTotPhyErrPkts,
       "wlanAPChTotMacErrPkts": wlanAPChTotMacErrPkts,
       "wlanAPChNoise": wlanAPChNoise,
       "wlanAPChCoverageIndex": wlanAPChCoverageIndex,
       "wlanAPChInterferenceIndex": wlanAPChInterferenceIndex,
       "wlanAPChFrameRetryRate": wlanAPChFrameRetryRate,
       "wlanAPChFrameLowSpeedRate": wlanAPChFrameLowSpeedRate,
       "wlanAPChFrameNonUnicastRate": wlanAPChFrameNonUnicastRate,
       "wlanAPChFrameFragmentationRate": wlanAPChFrameFragmentationRate,
       "wlanAPChFrameBandwidthRate": wlanAPChFrameBandwidthRate,
       "wlanAPChFrameRetryErrorRate": wlanAPChFrameRetryErrorRate,
       "wlanAPChBusyRate": wlanAPChBusyRate,
       "wlanAPChNumAPs": wlanAPChNumAPs,
       "wlanAPChFrameReceiveErrorRate": wlanAPChFrameReceiveErrorRate,
       "wlanAPChTransmittedFragmentCount": wlanAPChTransmittedFragmentCount,
       "wlanAPChMulticastTransmittedFrameCount": wlanAPChMulticastTransmittedFrameCount,
       "wlanAPChFailedCount": wlanAPChFailedCount,
       "wlanAPChRetryCount": wlanAPChRetryCount,
       "wlanAPChMultipleRetryCount": wlanAPChMultipleRetryCount,
       "wlanAPChFrameDuplicateCount": wlanAPChFrameDuplicateCount,
       "wlanAPChRTSSuccessCount": wlanAPChRTSSuccessCount,
       "wlanAPChRTSFailureCount": wlanAPChRTSFailureCount,
       "wlanAPChACKFailureCount": wlanAPChACKFailureCount,
       "wlanAPChReceivedFragmentCount": wlanAPChReceivedFragmentCount,
       "wlanAPChMulticastReceivedFrameCount": wlanAPChMulticastReceivedFrameCount,
       "wlanAPChFCSErrorCount": wlanAPChFCSErrorCount,
       "wlanAPChTransmittedFrameCount": wlanAPChTransmittedFrameCount,
       "wlanAPChWEPUndecryptableCount": wlanAPChWEPUndecryptableCount,
       "wlanAPChRxUtilization": wlanAPChRxUtilization,
       "wlanAPChTxUtilization": wlanAPChTxUtilization,
       "wlanAPChUtilization": wlanAPChUtilization,
       "wlanAPChPhyType": wlanAPChPhyType,
       "wlanAPChannelNumberV2": wlanAPChannelNumberV2,
       "wlanAPChHTMode": wlanAPChHTMode,
       "wlsxWlanAPWiredStatsTable": wlsxWlanAPWiredStatsTable,
       "wlsxWlanAPWiredStatsEntry": wlsxWlanAPWiredStatsEntry,
       "wlanAPWiredRxPkts": wlanAPWiredRxPkts,
       "wlanAPWiredRxDroppedPkts": wlanAPWiredRxDroppedPkts,
       "wlanAPWiredRxBytes": wlanAPWiredRxBytes,
       "wlanAPWiredTxBytes": wlanAPWiredTxBytes,
       "wlanAPWiredRxRate": wlanAPWiredRxRate,
       "wlanAPWiredTxRate": wlanAPWiredTxRate,
       "wlsxWlanAPESSIDStatsTable": wlsxWlanAPESSIDStatsTable,
       "wlsxWlanAPESSIDStatsEntry": wlsxWlanAPESSIDStatsEntry,
       "wlanAPESSIDWirelessRxBytes": wlanAPESSIDWirelessRxBytes,
       "wlanAPESSIDWirelessTxBytes": wlanAPESSIDWirelessTxBytes,
       "wlanAPESSIDWiredRxBytes": wlanAPESSIDWiredRxBytes,
       "wlanAPESSIDWiredTxBytes": wlanAPESSIDWiredTxBytes,
       "wlsxWlanAPRadioStatsTable": wlsxWlanAPRadioStatsTable,
       "wlsxWlanAPRadioStatsEntry": wlsxWlanAPRadioStatsEntry,
       "wlanAPRadioRxPkts": wlanAPRadioRxPkts,
       "wlanAPRadioRxBytes": wlanAPRadioRxBytes,
       "wlanAPRadioTxPkts": wlanAPRadioTxPkts,
       "wlanAPRadioTxBytes": wlanAPRadioTxBytes,
       "wlanAPRadioTxDroppedPkts": wlanAPRadioTxDroppedPkts,
       "wlanAPRadioTxErrorPkts": wlanAPRadioTxErrorPkts,
       "wlanAPRadioRxRate": wlanAPRadioRxRate,
       "wlanAPRadioTxRate": wlanAPRadioTxRate,
       "wlanApRadioAssocReqCount": wlanApRadioAssocReqCount,
       "wlanApRadioAssocReqSuccCount": wlanApRadioAssocReqSuccCount,
       "wlanApRadioReAssocReqCount": wlanApRadioReAssocReqCount,
       "wlanApRadioReAssocReqSuccCount": wlanApRadioReAssocReqSuccCount,
       "wlanAPRadioStationDuration": wlanAPRadioStationDuration,
       "wlanAPRadioAssocSuccPercent": wlanAPRadioAssocSuccPercent,
       "wlanAPRadioTxDataBytes": wlanAPRadioTxDataBytes,
       "wlsxWlanAPWiredPortStatsTable": wlsxWlanAPWiredPortStatsTable,
       "wlsxWlanAPWiredPortStatsEntry": wlsxWlanAPWiredPortStatsEntry,
       "wlanAPPortIndex": wlanAPPortIndex,
       "wlanAPPortName": wlanAPPortName,
       "wlanAPWiredPortRxPkts": wlanAPWiredPortRxPkts,
       "wlanAPWiredPortRxDroppedPkts": wlanAPWiredPortRxDroppedPkts,
       "wlanAPWiredPortRxErrors": wlanAPWiredPortRxErrors,
       "wlanAPWiredPortRxBytes": wlanAPWiredPortRxBytes,
       "wlanAPWiredPortTxPkts": wlanAPWiredPortTxPkts,
       "wlanAPWiredPortTxDroppedPkts": wlanAPWiredPortTxDroppedPkts,
       "wlanAPWiredPortTxErrors": wlanAPWiredPortTxErrors,
       "wlanAPWiredPortTxBytes": wlanAPWiredPortTxBytes,
       "wlanAPWiredPortRxRate": wlanAPWiredPortRxRate,
       "wlanAPWiredPortTxRate": wlanAPWiredPortTxRate,
       "wlanAPWiredPortSpeed": wlanAPWiredPortSpeed,
       "wlsxWlanStationStatsGroup": wlsxWlanStationStatsGroup,
       "wlsxWlanStationStatsTable": wlsxWlanStationStatsTable,
       "wlsxWlanStationStatsEntry": wlsxWlanStationStatsEntry,
       "wlanStaChannelNum": wlanStaChannelNum,
       "wlanStaTxPkts": wlanStaTxPkts,
       "wlanStaTxBytes": wlanStaTxBytes,
       "wlanStaRxPkts": wlanStaRxPkts,
       "wlanStaRxBytes": wlanStaRxBytes,
       "wlanStaTxBCastPkts": wlanStaTxBCastPkts,
       "wlanStaRxBCastBytes": wlanStaRxBCastBytes,
       "wlanStaTxMCastPkts": wlanStaTxMCastPkts,
       "wlanStaRxMCastBytes": wlanStaRxMCastBytes,
       "wlanStaDataPkts": wlanStaDataPkts,
       "wlanStaCtrlPkts": wlanStaCtrlPkts,
       "wlanStaNumAssocRequests": wlanStaNumAssocRequests,
       "wlanStaNumAuthRequests": wlanStaNumAuthRequests,
       "wlanStaTxDeauthentications": wlanStaTxDeauthentications,
       "wlanStaRxDeauthentications": wlanStaRxDeauthentications,
       "wlanStaFrameRetryRate": wlanStaFrameRetryRate,
       "wlanStaFrameLowSpeedRate": wlanStaFrameLowSpeedRate,
       "wlanStaFrameNonUnicastRate": wlanStaFrameNonUnicastRate,
       "wlanStaFrameFragmentationRate": wlanStaFrameFragmentationRate,
       "wlanStaFrameBandwidthRate": wlanStaFrameBandwidthRate,
       "wlanStaFrameRetryErrorRate": wlanStaFrameRetryErrorRate,
       "wlanStaFrameReceiveErrorRate": wlanStaFrameReceiveErrorRate,
       "wlanStaTxBCastBytes": wlanStaTxBCastBytes,
       "wlanStaTxMCastBytes": wlanStaTxMCastBytes,
       "wlanStaTxBytes64": wlanStaTxBytes64,
       "wlanStaRxBytes64": wlanStaRxBytes64,
       "wlanStaStatsPhyType": wlanStaStatsPhyType,
       "wlanStaSecChannelNum": wlanStaSecChannelNum,
       "wlanStaStatsHTMode": wlanStaStatsHTMode,
       "wlsxWlanStaRateStatsTable": wlsxWlanStaRateStatsTable,
       "wlsxWlanStaRateStatsEntry": wlsxWlanStaRateStatsEntry,
       "wlanStaTxPktsAt1Mbps": wlanStaTxPktsAt1Mbps,
       "wlanStaTxBytesAt1Mbps": wlanStaTxBytesAt1Mbps,
       "wlanStaTxPktsAt2Mbps": wlanStaTxPktsAt2Mbps,
       "wlanStaTxBytesAt2Mbps": wlanStaTxBytesAt2Mbps,
       "wlanStaTxPktsAt5Mbps": wlanStaTxPktsAt5Mbps,
       "wlanStaTxBytesAt5Mbps": wlanStaTxBytesAt5Mbps,
       "wlanStaTxPktsAt11Mbps": wlanStaTxPktsAt11Mbps,
       "wlanStaTxBytesAt11Mbps": wlanStaTxBytesAt11Mbps,
       "wlanStaTxPktsAt6Mbps": wlanStaTxPktsAt6Mbps,
       "wlanStaTxBytesAt6Mbps": wlanStaTxBytesAt6Mbps,
       "wlanStaTxPktsAt12Mbps": wlanStaTxPktsAt12Mbps,
       "wlanStaTxBytesAt12Mbps": wlanStaTxBytesAt12Mbps,
       "wlanStaTxPktsAt18Mbps": wlanStaTxPktsAt18Mbps,
       "wlanStaTxBytesAt18Mbps": wlanStaTxBytesAt18Mbps,
       "wlanStaTxPktsAt24Mbps": wlanStaTxPktsAt24Mbps,
       "wlanStaTxBytesAt24Mbps": wlanStaTxBytesAt24Mbps,
       "wlanStaTxPktsAt36Mbps": wlanStaTxPktsAt36Mbps,
       "wlanStaTxBytesAt36Mbps": wlanStaTxBytesAt36Mbps,
       "wlanStaTxPktsAt48Mbps": wlanStaTxPktsAt48Mbps,
       "wlanStaTxBytesAt48Mbps": wlanStaTxBytesAt48Mbps,
       "wlanStaTxPktsAt54Mbps": wlanStaTxPktsAt54Mbps,
       "wlanStaTxBytesAt54Mbps": wlanStaTxBytesAt54Mbps,
       "wlanStaRxPktsAt1Mbps": wlanStaRxPktsAt1Mbps,
       "wlanStaRxBytesAt1Mbps": wlanStaRxBytesAt1Mbps,
       "wlanStaRxPktsAt2Mbps": wlanStaRxPktsAt2Mbps,
       "wlanStaRxBytesAt2Mbps": wlanStaRxBytesAt2Mbps,
       "wlanStaRxPktsAt5Mbps": wlanStaRxPktsAt5Mbps,
       "wlanStaRxBytesAt5Mbps": wlanStaRxBytesAt5Mbps,
       "wlanStaRxPktsAt11Mbps": wlanStaRxPktsAt11Mbps,
       "wlanStaRxBytesAt11Mbps": wlanStaRxBytesAt11Mbps,
       "wlanStaRxPktsAt6Mbps": wlanStaRxPktsAt6Mbps,
       "wlanStaRxBytesAt6Mbps": wlanStaRxBytesAt6Mbps,
       "wlanStaRxPktsAt12Mbps": wlanStaRxPktsAt12Mbps,
       "wlanStaRxBytesAt12Mbps": wlanStaRxBytesAt12Mbps,
       "wlanStaRxPktsAt18Mbps": wlanStaRxPktsAt18Mbps,
       "wlanStaRxBytesAt18Mbps": wlanStaRxBytesAt18Mbps,
       "wlanStaRxPktsAt24Mbps": wlanStaRxPktsAt24Mbps,
       "wlanStaRxBytesAt24Mbps": wlanStaRxBytesAt24Mbps,
       "wlanStaRxPktsAt36Mbps": wlanStaRxPktsAt36Mbps,
       "wlanStaRxBytesAt36Mbps": wlanStaRxBytesAt36Mbps,
       "wlanStaRxPktsAt48Mbps": wlanStaRxPktsAt48Mbps,
       "wlanStaRxBytesAt48Mbps": wlanStaRxBytesAt48Mbps,
       "wlanStaRxPktsAt54Mbps": wlanStaRxPktsAt54Mbps,
       "wlanStaRxBytesAt54Mbps": wlanStaRxBytesAt54Mbps,
       "wlanStaTxPktsAt9Mbps": wlanStaTxPktsAt9Mbps,
       "wlanStaTxBytesAt9Mbps": wlanStaTxBytesAt9Mbps,
       "wlanStaRxPktsAt9Mbps": wlanStaRxPktsAt9Mbps,
       "wlanStaRxBytesAt9Mbps": wlanStaRxBytesAt9Mbps,
       "wlsxWlanStaDATypeStatsTable": wlsxWlanStaDATypeStatsTable,
       "wlsxWlanStaDATypeStatsEntry": wlsxWlanStaDATypeStatsEntry,
       "wlanStaTxDABroadcastPkts": wlanStaTxDABroadcastPkts,
       "wlanStaTxDABroadcastBytes": wlanStaTxDABroadcastBytes,
       "wlanStaTxDAMulticastPkts": wlanStaTxDAMulticastPkts,
       "wlanStaTxDAMulticastBytes": wlanStaTxDAMulticastBytes,
       "wlanStaTxDAUnicastPkts": wlanStaTxDAUnicastPkts,
       "wlanStaTxDAUnicastBytes": wlanStaTxDAUnicastBytes,
       "wlsxWlanStaFrameTypeStatsTable": wlsxWlanStaFrameTypeStatsTable,
       "wlsxWlanStaFrameTypeStatsEntry": wlsxWlanStaFrameTypeStatsEntry,
       "wlanStaTxMgmtPkts": wlanStaTxMgmtPkts,
       "wlanStaTxMgmtBytes": wlanStaTxMgmtBytes,
       "wlanStaTxCtrlPkts": wlanStaTxCtrlPkts,
       "wlanStaTxCtrlBytes": wlanStaTxCtrlBytes,
       "wlanStaTxDataPkts": wlanStaTxDataPkts,
       "wlanStaTxDataBytes": wlanStaTxDataBytes,
       "wlanStaRxMgmtPkts": wlanStaRxMgmtPkts,
       "wlanStaRxMgmtBytes": wlanStaRxMgmtBytes,
       "wlanStaRxCtrlPkts": wlanStaRxCtrlPkts,
       "wlanStaRxCtrlBytes": wlanStaRxCtrlBytes,
       "wlanStaRxDataPkts": wlanStaRxDataPkts,
       "wlanStaRxDataBytes": wlanStaRxDataBytes,
       "wlsxWlanStaPktSizeStatsTable": wlsxWlanStaPktSizeStatsTable,
       "wlsxWlanStaPktSizeStatsEntry": wlsxWlanStaPktSizeStatsEntry,
       "wlanStaTxPkts63Bytes": wlanStaTxPkts63Bytes,
       "wlanStaTxPkts64To127": wlanStaTxPkts64To127,
       "wlanStaTxPkts128To255": wlanStaTxPkts128To255,
       "wlanStaTxPkts256To511": wlanStaTxPkts256To511,
       "wlanStaTxPkts512To1023": wlanStaTxPkts512To1023,
       "wlanStaTxPkts1024To1518": wlanStaTxPkts1024To1518,
       "wlanStaRxPkts63Bytes": wlanStaRxPkts63Bytes,
       "wlanStaRxPkts64To127": wlanStaRxPkts64To127,
       "wlanStaRxPkts128To255": wlanStaRxPkts128To255,
       "wlanStaRxPkts256To511": wlanStaRxPkts256To511,
       "wlanStaRxPkts512To1023": wlanStaRxPkts512To1023,
       "wlanStaRxPkts1024To1518": wlanStaRxPkts1024To1518,
       "wlsxWlanSwitchStatsGroup": wlsxWlanSwitchStatsGroup,
       "wlsxWlanESSIDStatsTable": wlsxWlanESSIDStatsTable,
       "wlsxWlanESSIDStatsEntry": wlsxWlanESSIDStatsEntry,
       "wlanESSIDRxPkts": wlanESSIDRxPkts,
       "wlanESSIDRxDroppedPkts": wlanESSIDRxDroppedPkts,
       "wlanESSIDRxRetryPkts": wlanESSIDRxRetryPkts,
       "wlanESSIDTxPkts": wlanESSIDTxPkts,
       "wlanESSIDTxDroppedPkts": wlanESSIDTxDroppedPkts,
       "wlanESSIDTxRetryPkts": wlanESSIDTxRetryPkts,
       "wlanESSIDTxErrorPkts": wlanESSIDTxErrorPkts,
       "wlanESSIDRxRate": wlanESSIDRxRate,
       "wlanESSIDTxRate": wlanESSIDTxRate,
       "wlanESSIDWiredRxPkts": wlanESSIDWiredRxPkts,
       "wlanESSIDWiredRxBytes": wlanESSIDWiredRxBytes,
       "wlanESSIDWiredTxBytes": wlanESSIDWiredTxBytes,
       "wlsxWlanEthStatsTable": wlsxWlanEthStatsTable,
       "wlsxWlanEthStatsEntry": wlsxWlanEthStatsEntry,
       "wlanEthRxRate": wlanEthRxRate,
       "wlanEthTxRate": wlanEthTxRate,
       "wlsxRAPTraps": wlsxRAPTraps,
       "wlsxRAPActiveUplink": wlsxRAPActiveUplink}
)
