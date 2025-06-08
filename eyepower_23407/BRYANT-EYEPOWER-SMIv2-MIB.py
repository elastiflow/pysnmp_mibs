# SNMP MIB module (BRYANT-EYEPOWER-SMIv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/eyepower_23407/BRYANT-EYEPOWER-SMIv2-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:59:11 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bryantUnlimited = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23407)
)
if mibBuilder.loadTexts:
    bryantUnlimited.setRevisions(
        ("2018-02-16 22:31",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EyePower_ObjectIdentity = ObjectIdentity
eyePower = _EyePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1)
)
_AddressIP_Type = IpAddress
_AddressIP_Object = MibScalar
addressIP = _AddressIP_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1, 1),
    _AddressIP_Type()
)
addressIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressIP.setStatus("current")


class _AddressMAC_Type(OctetString):
    """Custom type addressMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_AddressMAC_Type.__name__ = "OctetString"
_AddressMAC_Object = MibScalar
addressMAC = _AddressMAC_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1, 2),
    _AddressMAC_Type()
)
addressMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressMAC.setStatus("current")


class _VoltagePOE_Type(Integer32):
    """Custom type voltagePOE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_VoltagePOE_Type.__name__ = "Integer32"
_VoltagePOE_Object = MibScalar
voltagePOE = _VoltagePOE_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1, 3),
    _VoltagePOE_Type()
)
voltagePOE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltagePOE.setStatus("current")
_StatusRelayDisplay_Type = OctetString
_StatusRelayDisplay_Object = MibScalar
statusRelayDisplay = _StatusRelayDisplay_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1, 4),
    _StatusRelayDisplay_Type()
)
statusRelayDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRelayDisplay.setStatus("current")


class _AttackCount_Type(Integer32):
    """Custom type attackCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AttackCount_Type.__name__ = "Integer32"
_AttackCount_Object = MibScalar
attackCount = _AttackCount_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1, 5),
    _AttackCount_Type()
)
attackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attackCount.setStatus("current")
_ControllerIPAddress_Type = IpAddress
_ControllerIPAddress_Object = MibScalar
controllerIPAddress = _ControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 1, 6),
    _ControllerIPAddress_Type()
)
controllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerIPAddress.setStatus("current")
_Unit1_ObjectIdentity = ObjectIdentity
unit1 = _Unit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2)
)
_Unit1Info_ObjectIdentity = ObjectIdentity
unit1Info = _Unit1Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1)
)


class _Unit1Serial_Type(DisplayString):
    """Custom type unit1Serial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Unit1Serial_Type.__name__ = "DisplayString"
_Unit1Serial_Object = MibScalar
unit1Serial = _Unit1Serial_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 1),
    _Unit1Serial_Type()
)
unit1Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1Serial.setStatus("current")
_Unit1LocationName_Type = DisplayString
_Unit1LocationName_Object = MibScalar
unit1LocationName = _Unit1LocationName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 2),
    _Unit1LocationName_Type()
)
unit1LocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1LocationName.setStatus("current")
_Unit1FirmwareVersions_Type = DisplayString
_Unit1FirmwareVersions_Object = MibScalar
unit1FirmwareVersions = _Unit1FirmwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 3),
    _Unit1FirmwareVersions_Type()
)
unit1FirmwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1FirmwareVersions.setStatus("current")


class _Unit1Inlets_Type(Integer32):
    """Custom type unit1Inlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Unit1Inlets_Type.__name__ = "Integer32"
_Unit1Inlets_Object = MibScalar
unit1Inlets = _Unit1Inlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 4),
    _Unit1Inlets_Type()
)
unit1Inlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1Inlets.setStatus("current")


class _Unit1Outlets_Type(Integer32):
    """Custom type unit1Outlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(14, 14),
    )


_Unit1Outlets_Type.__name__ = "Integer32"
_Unit1Outlets_Object = MibScalar
unit1Outlets = _Unit1Outlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 5),
    _Unit1Outlets_Type()
)
unit1Outlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1Outlets.setStatus("current")
_Unit1IntTemp_Type = Integer32
_Unit1IntTemp_Object = MibScalar
unit1IntTemp = _Unit1IntTemp_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 6),
    _Unit1IntTemp_Type()
)
unit1IntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1IntTemp.setStatus("current")
_Unit1IntTempMin_Type = Integer32
_Unit1IntTempMin_Object = MibScalar
unit1IntTempMin = _Unit1IntTempMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 7),
    _Unit1IntTempMin_Type()
)
unit1IntTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1IntTempMin.setStatus("current")
_Unit1IntTempMax_Type = Integer32
_Unit1IntTempMax_Object = MibScalar
unit1IntTempMax = _Unit1IntTempMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 8),
    _Unit1IntTempMax_Type()
)
unit1IntTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1IntTempMax.setStatus("current")


class _Unit1DCSupply_Type(Integer32):
    """Custom type unit1DCSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit1DCSupply_Type.__name__ = "Integer32"
_Unit1DCSupply_Object = MibScalar
unit1DCSupply = _Unit1DCSupply_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 9),
    _Unit1DCSupply_Type()
)
unit1DCSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1DCSupply.setStatus("current")


class _Unit1DCSupplyMin_Type(Integer32):
    """Custom type unit1DCSupplyMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit1DCSupplyMin_Type.__name__ = "Integer32"
_Unit1DCSupplyMin_Object = MibScalar
unit1DCSupplyMin = _Unit1DCSupplyMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 10),
    _Unit1DCSupplyMin_Type()
)
unit1DCSupplyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1DCSupplyMin.setStatus("current")


class _Unit1DCSupplyMax_Type(Integer32):
    """Custom type unit1DCSupplyMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit1DCSupplyMax_Type.__name__ = "Integer32"
_Unit1DCSupplyMax_Object = MibScalar
unit1DCSupplyMax = _Unit1DCSupplyMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 11),
    _Unit1DCSupplyMax_Type()
)
unit1DCSupplyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1DCSupplyMax.setStatus("current")


class _Unit1MiscFlags_Type(Bits):
    """Custom type unit1MiscFlags based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisabled", 0),
          ("cycleTimerRunning", 1),
          ("macroRunning", 2),
          ("fuseFailed", 3))
    )

_Unit1MiscFlags_Type.__name__ = "Bits"
_Unit1MiscFlags_Object = MibScalar
unit1MiscFlags = _Unit1MiscFlags_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 12),
    _Unit1MiscFlags_Type()
)
unit1MiscFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1MiscFlags.setStatus("current")


class _Unit1Buzzer_Type(Bits):
    """Custom type unit1Buzzer based on Bits"""
    namedValues = NamedValues(
        *(("unitLEDsFlashing", 0),
          ("unitIsBeeping", 1),
          ("bInletFailAcknowleged", 2),
          ("bInletFailed", 3),
          ("aInletFailAcknowleged", 4),
          ("aInletFailed", 5),
          ("flashingLEDsEnabled", 6),
          ("beepingEnabled", 7))
    )

_Unit1Buzzer_Type.__name__ = "Bits"
_Unit1Buzzer_Object = MibScalar
unit1Buzzer = _Unit1Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 13),
    _Unit1Buzzer_Type()
)
unit1Buzzer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1Buzzer.setStatus("current")
_Unit1AlarmGPText_Type = DisplayString
_Unit1AlarmGPText_Object = MibScalar
unit1AlarmGPText = _Unit1AlarmGPText_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 1, 14),
    _Unit1AlarmGPText_Type()
)
unit1AlarmGPText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1AlarmGPText.setStatus("current")
_Unit1InletTable_Object = MibTable
unit1InletTable = _Unit1InletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2)
)
if mibBuilder.loadTexts:
    unit1InletTable.setStatus("current")
_Unit1InletTableEntry_Object = MibTableRow
unit1InletTableEntry = _Unit1InletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1)
)
unit1InletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletIndex"),
)
if mibBuilder.loadTexts:
    unit1InletTableEntry.setStatus("current")


class _Unit1InletIndex_Type(Integer32):
    """Custom type unit1InletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit1InletIndex_Type.__name__ = "Integer32"
_Unit1InletIndex_Object = MibTableColumn
unit1InletIndex = _Unit1InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 1),
    _Unit1InletIndex_Type()
)
unit1InletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit1InletIndex.setStatus("current")
_Unit1InletName_Type = DisplayString
_Unit1InletName_Object = MibTableColumn
unit1InletName = _Unit1InletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 2),
    _Unit1InletName_Type()
)
unit1InletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletName.setStatus("current")
_Unit1InletRMSLN_Type = Integer32
_Unit1InletRMSLN_Object = MibTableColumn
unit1InletRMSLN = _Unit1InletRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 3),
    _Unit1InletRMSLN_Type()
)
unit1InletRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletRMSLN.setStatus("current")
_Unit1InletPeakLN_Type = Integer32
_Unit1InletPeakLN_Object = MibTableColumn
unit1InletPeakLN = _Unit1InletPeakLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 4),
    _Unit1InletPeakLN_Type()
)
unit1InletPeakLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletPeakLN.setStatus("current")


class _Unit1InletCrest_Type(Integer32):
    """Custom type unit1InletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit1InletCrest_Type.__name__ = "Integer32"
_Unit1InletCrest_Object = MibTableColumn
unit1InletCrest = _Unit1InletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 5),
    _Unit1InletCrest_Type()
)
unit1InletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletCrest.setStatus("current")
_Unit1InletRMSNE_Type = Integer32
_Unit1InletRMSNE_Object = MibTableColumn
unit1InletRMSNE = _Unit1InletRMSNE_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 6),
    _Unit1InletRMSNE_Type()
)
unit1InletRMSNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletRMSNE.setStatus("current")


class _Unit1InletFrequency_Type(Integer32):
    """Custom type unit1InletFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit1InletFrequency_Type.__name__ = "Integer32"
_Unit1InletFrequency_Object = MibTableColumn
unit1InletFrequency = _Unit1InletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 8),
    _Unit1InletFrequency_Type()
)
unit1InletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletFrequency.setStatus("current")
_Unit1InletLeakage_Type = Integer32
_Unit1InletLeakage_Object = MibTableColumn
unit1InletLeakage = _Unit1InletLeakage_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 9),
    _Unit1InletLeakage_Type()
)
unit1InletLeakage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletLeakage.setStatus("current")


class _Unit1InletVaristors_Type(Integer32):
    """Custom type unit1InletVaristors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Unit1InletVaristors_Type.__name__ = "Integer32"
_Unit1InletVaristors_Object = MibTableColumn
unit1InletVaristors = _Unit1InletVaristors_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 2, 1, 10),
    _Unit1InletVaristors_Type()
)
unit1InletVaristors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1InletVaristors.setStatus("current")
_Unit1BusTable_Object = MibTable
unit1BusTable = _Unit1BusTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3)
)
if mibBuilder.loadTexts:
    unit1BusTable.setStatus("current")
_Unit1BusTableEntry_Object = MibTableRow
unit1BusTableEntry = _Unit1BusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1)
)
unit1BusTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusIndex"),
)
if mibBuilder.loadTexts:
    unit1BusTableEntry.setStatus("current")


class _Unit1BusIndex_Type(Integer32):
    """Custom type unit1BusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit1BusIndex_Type.__name__ = "Integer32"
_Unit1BusIndex_Object = MibTableColumn
unit1BusIndex = _Unit1BusIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 1),
    _Unit1BusIndex_Type()
)
unit1BusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit1BusIndex.setStatus("current")


class _Unit1BusInletStatus_Type(Bits):
    """Custom type unit1BusInletStatus based on Bits"""
    namedValues = NamedValues(
        *(("aInletAvailable", 0),
          ("bInletAvailable", 1),
          ("aInletSelected", 2),
          ("inletPreferenceSet", 3),
          ("aInletPreferred", 4),
          ("nonSyncChangeAllowed", 5),
          ("inletsNotInSync", 6))
    )

_Unit1BusInletStatus_Type.__name__ = "Bits"
_Unit1BusInletStatus_Object = MibTableColumn
unit1BusInletStatus = _Unit1BusInletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 2),
    _Unit1BusInletStatus_Type()
)
unit1BusInletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusInletStatus.setStatus("current")
_Unit1BusRMSLN_Type = Integer32
_Unit1BusRMSLN_Object = MibTableColumn
unit1BusRMSLN = _Unit1BusRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 3),
    _Unit1BusRMSLN_Type()
)
unit1BusRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusRMSLN.setStatus("current")
_Unit1BusCurrent_Type = Integer32
_Unit1BusCurrent_Object = MibTableColumn
unit1BusCurrent = _Unit1BusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 4),
    _Unit1BusCurrent_Type()
)
unit1BusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusCurrent.setStatus("current")


class _Unit1BusCrest_Type(Integer32):
    """Custom type unit1BusCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit1BusCrest_Type.__name__ = "Integer32"
_Unit1BusCrest_Object = MibTableColumn
unit1BusCrest = _Unit1BusCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 5),
    _Unit1BusCrest_Type()
)
unit1BusCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusCrest.setStatus("current")
_Unit1BusApparentPower_Type = Integer32
_Unit1BusApparentPower_Object = MibTableColumn
unit1BusApparentPower = _Unit1BusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 6),
    _Unit1BusApparentPower_Type()
)
unit1BusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusApparentPower.setStatus("current")


class _Unit1BusRealPower_Type(Integer32):
    """Custom type unit1BusRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit1BusRealPower_Type.__name__ = "Integer32"
_Unit1BusRealPower_Object = MibTableColumn
unit1BusRealPower = _Unit1BusRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 7),
    _Unit1BusRealPower_Type()
)
unit1BusRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusRealPower.setStatus("current")
_Unit1BusPowerFactor_Type = Integer32
_Unit1BusPowerFactor_Object = MibTableColumn
unit1BusPowerFactor = _Unit1BusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 8),
    _Unit1BusPowerFactor_Type()
)
unit1BusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusPowerFactor.setStatus("current")
_Unit1BusDCOffset_Type = Integer32
_Unit1BusDCOffset_Object = MibTableColumn
unit1BusDCOffset = _Unit1BusDCOffset_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 3, 1, 9),
    _Unit1BusDCOffset_Type()
)
unit1BusDCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1BusDCOffset.setStatus("current")
_Unit1OutletTable_Object = MibTable
unit1OutletTable = _Unit1OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4)
)
if mibBuilder.loadTexts:
    unit1OutletTable.setStatus("current")
_Unit1OutletTableEntry_Object = MibTableRow
unit1OutletTableEntry = _Unit1OutletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1)
)
unit1OutletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletIndex"),
)
if mibBuilder.loadTexts:
    unit1OutletTableEntry.setStatus("current")


class _Unit1OutletIndex_Type(Integer32):
    """Custom type unit1OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit1OutletIndex_Type.__name__ = "Integer32"
_Unit1OutletIndex_Object = MibTableColumn
unit1OutletIndex = _Unit1OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 1),
    _Unit1OutletIndex_Type()
)
unit1OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit1OutletIndex.setStatus("current")
_Unit1OutletName_Type = DisplayString
_Unit1OutletName_Object = MibTableColumn
unit1OutletName = _Unit1OutletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 2),
    _Unit1OutletName_Type()
)
unit1OutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletName.setStatus("current")


class _Unit1OutletStatus_Type(Bits):
    """Custom type unit1OutletStatus based on Bits"""
    namedValues = NamedValues(
        *(("fuse", 0),
          ("relay", 1),
          ("outlet", 2),
          ("failsafe", 3),
          ("cycle", 4))
    )

_Unit1OutletStatus_Type.__name__ = "Bits"
_Unit1OutletStatus_Object = MibTableColumn
unit1OutletStatus = _Unit1OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 3),
    _Unit1OutletStatus_Type()
)
unit1OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletStatus.setStatus("current")
_Unit1OutletCycleTimer_Type = Integer32
_Unit1OutletCycleTimer_Object = MibTableColumn
unit1OutletCycleTimer = _Unit1OutletCycleTimer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 4),
    _Unit1OutletCycleTimer_Type()
)
unit1OutletCycleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletCycleTimer.setStatus("current")
_Unit1OutletCurrent_Type = Integer32
_Unit1OutletCurrent_Object = MibTableColumn
unit1OutletCurrent = _Unit1OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 5),
    _Unit1OutletCurrent_Type()
)
unit1OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletCurrent.setStatus("current")


class _Unit1OutletCrest_Type(Integer32):
    """Custom type unit1OutletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit1OutletCrest_Type.__name__ = "Integer32"
_Unit1OutletCrest_Object = MibTableColumn
unit1OutletCrest = _Unit1OutletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 6),
    _Unit1OutletCrest_Type()
)
unit1OutletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletCrest.setStatus("current")


class _Unit1OutletRealPower_Type(Integer32):
    """Custom type unit1OutletRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit1OutletRealPower_Type.__name__ = "Integer32"
_Unit1OutletRealPower_Object = MibTableColumn
unit1OutletRealPower = _Unit1OutletRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 7),
    _Unit1OutletRealPower_Type()
)
unit1OutletRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletRealPower.setStatus("current")
_Unit1OutletPowerFactor_Type = Integer32
_Unit1OutletPowerFactor_Object = MibTableColumn
unit1OutletPowerFactor = _Unit1OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 4, 1, 8),
    _Unit1OutletPowerFactor_Type()
)
unit1OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutletPowerFactor.setStatus("current")
_Unit1GPITable_Object = MibTable
unit1GPITable = _Unit1GPITable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 5)
)
if mibBuilder.loadTexts:
    unit1GPITable.setStatus("current")
_Unit1GPITableEntry_Object = MibTableRow
unit1GPITableEntry = _Unit1GPITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 5, 1)
)
unit1GPITableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit1GPIIndex"),
)
if mibBuilder.loadTexts:
    unit1GPITableEntry.setStatus("current")


class _Unit1GPIIndex_Type(Integer32):
    """Custom type unit1GPIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Unit1GPIIndex_Type.__name__ = "Integer32"
_Unit1GPIIndex_Object = MibTableColumn
unit1GPIIndex = _Unit1GPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 5, 1, 1),
    _Unit1GPIIndex_Type()
)
unit1GPIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit1GPIIndex.setStatus("current")


class _Unit1GPIState_Type(Bits):
    """Custom type unit1GPIState based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisableActive", 0),
          ("gpiFitted", 1),
          ("gpiDisabled", 2),
          ("gpiIsOutput", 3),
          ("gpiOutputSetHigh", 4),
          ("gpiReadIsHigh", 5))
    )

_Unit1GPIState_Type.__name__ = "Bits"
_Unit1GPIState_Object = MibTableColumn
unit1GPIState = _Unit1GPIState_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 5, 1, 2),
    _Unit1GPIState_Type()
)
unit1GPIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1GPIState.setStatus("current")
_Unit1SensorTable_Object = MibTable
unit1SensorTable = _Unit1SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6)
)
if mibBuilder.loadTexts:
    unit1SensorTable.setStatus("current")
_Unit1SensorTableEntry_Object = MibTableRow
unit1SensorTableEntry = _Unit1SensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1)
)
unit1SensorTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorIndex"),
)
if mibBuilder.loadTexts:
    unit1SensorTableEntry.setStatus("current")


class _Unit1SensorIndex_Type(Integer32):
    """Custom type unit1SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit1SensorIndex_Type.__name__ = "Integer32"
_Unit1SensorIndex_Object = MibTableColumn
unit1SensorIndex = _Unit1SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 1),
    _Unit1SensorIndex_Type()
)
unit1SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit1SensorIndex.setStatus("current")
_Unit1SensorName_Type = DisplayString
_Unit1SensorName_Object = MibTableColumn
unit1SensorName = _Unit1SensorName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 2),
    _Unit1SensorName_Type()
)
unit1SensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorName.setStatus("current")
_Unit1SensorType_Type = Integer32
_Unit1SensorType_Object = MibTableColumn
unit1SensorType = _Unit1SensorType_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 3),
    _Unit1SensorType_Type()
)
unit1SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorType.setStatus("current")
_Unit1SensorAddress_Type = DisplayString
_Unit1SensorAddress_Object = MibTableColumn
unit1SensorAddress = _Unit1SensorAddress_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 4),
    _Unit1SensorAddress_Type()
)
unit1SensorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorAddress.setStatus("current")


class _Unit1SensorStatus_Type(Integer32):
    """Custom type unit1SensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Unit1SensorStatus_Type.__name__ = "Integer32"
_Unit1SensorStatus_Object = MibTableColumn
unit1SensorStatus = _Unit1SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 5),
    _Unit1SensorStatus_Type()
)
unit1SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorStatus.setStatus("current")
_Unit1SensorLive_Type = Integer32
_Unit1SensorLive_Object = MibTableColumn
unit1SensorLive = _Unit1SensorLive_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 6),
    _Unit1SensorLive_Type()
)
unit1SensorLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorLive.setStatus("current")
_Unit1SensorMin_Type = Integer32
_Unit1SensorMin_Object = MibTableColumn
unit1SensorMin = _Unit1SensorMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 7),
    _Unit1SensorMin_Type()
)
unit1SensorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorMin.setStatus("current")
_Unit1SensorMax_Type = Integer32
_Unit1SensorMax_Object = MibTableColumn
unit1SensorMax = _Unit1SensorMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 2, 6, 1, 8),
    _Unit1SensorMax_Type()
)
unit1SensorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorMax.setStatus("current")
_Unit2_ObjectIdentity = ObjectIdentity
unit2 = _Unit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3)
)
_Unit2Info_ObjectIdentity = ObjectIdentity
unit2Info = _Unit2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1)
)


class _Unit2Serial_Type(DisplayString):
    """Custom type unit2Serial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Unit2Serial_Type.__name__ = "DisplayString"
_Unit2Serial_Object = MibScalar
unit2Serial = _Unit2Serial_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 1),
    _Unit2Serial_Type()
)
unit2Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2Serial.setStatus("current")
_Unit2LocationName_Type = DisplayString
_Unit2LocationName_Object = MibScalar
unit2LocationName = _Unit2LocationName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 2),
    _Unit2LocationName_Type()
)
unit2LocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2LocationName.setStatus("current")
_Unit2FirmwareVersions_Type = DisplayString
_Unit2FirmwareVersions_Object = MibScalar
unit2FirmwareVersions = _Unit2FirmwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 3),
    _Unit2FirmwareVersions_Type()
)
unit2FirmwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2FirmwareVersions.setStatus("current")


class _Unit2Inlets_Type(Integer32):
    """Custom type unit2Inlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Unit2Inlets_Type.__name__ = "Integer32"
_Unit2Inlets_Object = MibScalar
unit2Inlets = _Unit2Inlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 4),
    _Unit2Inlets_Type()
)
unit2Inlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2Inlets.setStatus("current")


class _Unit2Outlets_Type(Integer32):
    """Custom type unit2Outlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(14, 14),
    )


_Unit2Outlets_Type.__name__ = "Integer32"
_Unit2Outlets_Object = MibScalar
unit2Outlets = _Unit2Outlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 5),
    _Unit2Outlets_Type()
)
unit2Outlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2Outlets.setStatus("current")
_Unit2IntTemp_Type = Integer32
_Unit2IntTemp_Object = MibScalar
unit2IntTemp = _Unit2IntTemp_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 6),
    _Unit2IntTemp_Type()
)
unit2IntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2IntTemp.setStatus("current")
_Unit2IntTempMin_Type = Integer32
_Unit2IntTempMin_Object = MibScalar
unit2IntTempMin = _Unit2IntTempMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 7),
    _Unit2IntTempMin_Type()
)
unit2IntTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2IntTempMin.setStatus("current")
_Unit2IntTempMax_Type = Integer32
_Unit2IntTempMax_Object = MibScalar
unit2IntTempMax = _Unit2IntTempMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 8),
    _Unit2IntTempMax_Type()
)
unit2IntTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2IntTempMax.setStatus("current")


class _Unit2DCSupply_Type(Integer32):
    """Custom type unit2DCSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit2DCSupply_Type.__name__ = "Integer32"
_Unit2DCSupply_Object = MibScalar
unit2DCSupply = _Unit2DCSupply_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 9),
    _Unit2DCSupply_Type()
)
unit2DCSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2DCSupply.setStatus("current")


class _Unit2DCSupplyMin_Type(Integer32):
    """Custom type unit2DCSupplyMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit2DCSupplyMin_Type.__name__ = "Integer32"
_Unit2DCSupplyMin_Object = MibScalar
unit2DCSupplyMin = _Unit2DCSupplyMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 10),
    _Unit2DCSupplyMin_Type()
)
unit2DCSupplyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2DCSupplyMin.setStatus("current")


class _Unit2DCSupplyMax_Type(Integer32):
    """Custom type unit2DCSupplyMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit2DCSupplyMax_Type.__name__ = "Integer32"
_Unit2DCSupplyMax_Object = MibScalar
unit2DCSupplyMax = _Unit2DCSupplyMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 11),
    _Unit2DCSupplyMax_Type()
)
unit2DCSupplyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2DCSupplyMax.setStatus("current")


class _Unit2MiscFlags_Type(Bits):
    """Custom type unit2MiscFlags based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisabled", 0),
          ("cycleTimerRunning", 1),
          ("macroRunning", 2),
          ("fuseFailed", 3))
    )

_Unit2MiscFlags_Type.__name__ = "Bits"
_Unit2MiscFlags_Object = MibScalar
unit2MiscFlags = _Unit2MiscFlags_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 12),
    _Unit2MiscFlags_Type()
)
unit2MiscFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2MiscFlags.setStatus("current")


class _Unit2Buzzer_Type(Bits):
    """Custom type unit2Buzzer based on Bits"""
    namedValues = NamedValues(
        *(("unitLEDsFlashing", 0),
          ("unitIsBeeping", 1),
          ("bInletFailAcknowleged", 2),
          ("bInletFailed", 3),
          ("aInletFailAcknowleged", 4),
          ("aInletFailed", 5),
          ("flashingLEDsEnabled", 6),
          ("beepingEnabled", 7))
    )

_Unit2Buzzer_Type.__name__ = "Bits"
_Unit2Buzzer_Object = MibScalar
unit2Buzzer = _Unit2Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 13),
    _Unit2Buzzer_Type()
)
unit2Buzzer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2Buzzer.setStatus("current")
_Unit2AlarmGPText_Type = DisplayString
_Unit2AlarmGPText_Object = MibScalar
unit2AlarmGPText = _Unit2AlarmGPText_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 1, 14),
    _Unit2AlarmGPText_Type()
)
unit2AlarmGPText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2AlarmGPText.setStatus("current")
_Unit2InletTable_Object = MibTable
unit2InletTable = _Unit2InletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2)
)
if mibBuilder.loadTexts:
    unit2InletTable.setStatus("current")
_Unit2InletTableEntry_Object = MibTableRow
unit2InletTableEntry = _Unit2InletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1)
)
unit2InletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletIndex"),
)
if mibBuilder.loadTexts:
    unit2InletTableEntry.setStatus("current")


class _Unit2InletIndex_Type(Integer32):
    """Custom type unit2InletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit2InletIndex_Type.__name__ = "Integer32"
_Unit2InletIndex_Object = MibTableColumn
unit2InletIndex = _Unit2InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 1),
    _Unit2InletIndex_Type()
)
unit2InletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit2InletIndex.setStatus("current")
_Unit2InletName_Type = DisplayString
_Unit2InletName_Object = MibTableColumn
unit2InletName = _Unit2InletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 2),
    _Unit2InletName_Type()
)
unit2InletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletName.setStatus("current")
_Unit2InletRMSLN_Type = Integer32
_Unit2InletRMSLN_Object = MibTableColumn
unit2InletRMSLN = _Unit2InletRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 3),
    _Unit2InletRMSLN_Type()
)
unit2InletRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletRMSLN.setStatus("current")
_Unit2InletPeakLN_Type = Integer32
_Unit2InletPeakLN_Object = MibTableColumn
unit2InletPeakLN = _Unit2InletPeakLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 4),
    _Unit2InletPeakLN_Type()
)
unit2InletPeakLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletPeakLN.setStatus("current")


class _Unit2InletCrest_Type(Integer32):
    """Custom type unit2InletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit2InletCrest_Type.__name__ = "Integer32"
_Unit2InletCrest_Object = MibTableColumn
unit2InletCrest = _Unit2InletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 5),
    _Unit2InletCrest_Type()
)
unit2InletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletCrest.setStatus("current")
_Unit2InletRMSNE_Type = Integer32
_Unit2InletRMSNE_Object = MibTableColumn
unit2InletRMSNE = _Unit2InletRMSNE_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 6),
    _Unit2InletRMSNE_Type()
)
unit2InletRMSNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletRMSNE.setStatus("current")


class _Unit2InletFrequency_Type(Integer32):
    """Custom type unit2InletFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit2InletFrequency_Type.__name__ = "Integer32"
_Unit2InletFrequency_Object = MibTableColumn
unit2InletFrequency = _Unit2InletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 7),
    _Unit2InletFrequency_Type()
)
unit2InletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletFrequency.setStatus("current")
_Unit2InletLeakage_Type = Integer32
_Unit2InletLeakage_Object = MibTableColumn
unit2InletLeakage = _Unit2InletLeakage_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 8),
    _Unit2InletLeakage_Type()
)
unit2InletLeakage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletLeakage.setStatus("current")


class _Unit2InletVaristors_Type(Integer32):
    """Custom type unit2InletVaristors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Unit2InletVaristors_Type.__name__ = "Integer32"
_Unit2InletVaristors_Object = MibTableColumn
unit2InletVaristors = _Unit2InletVaristors_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 2, 1, 9),
    _Unit2InletVaristors_Type()
)
unit2InletVaristors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2InletVaristors.setStatus("current")
_Unit2BusTable_Object = MibTable
unit2BusTable = _Unit2BusTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3)
)
if mibBuilder.loadTexts:
    unit2BusTable.setStatus("current")
_Unit2BusTableEntry_Object = MibTableRow
unit2BusTableEntry = _Unit2BusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1)
)
unit2BusTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusIndex"),
)
if mibBuilder.loadTexts:
    unit2BusTableEntry.setStatus("current")


class _Unit2BusIndex_Type(Integer32):
    """Custom type unit2BusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit2BusIndex_Type.__name__ = "Integer32"
_Unit2BusIndex_Object = MibTableColumn
unit2BusIndex = _Unit2BusIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 1),
    _Unit2BusIndex_Type()
)
unit2BusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit2BusIndex.setStatus("current")


class _Unit2BusInletStatus_Type(Bits):
    """Custom type unit2BusInletStatus based on Bits"""
    namedValues = NamedValues(
        *(("aInletAvailable", 0),
          ("bInletAvailable", 1),
          ("aInletSelected", 2),
          ("inletPreferenceSet", 3),
          ("aInletPreferred", 4),
          ("nonSyncChangeAllowed", 5),
          ("inletsNotInSync", 6))
    )

_Unit2BusInletStatus_Type.__name__ = "Bits"
_Unit2BusInletStatus_Object = MibTableColumn
unit2BusInletStatus = _Unit2BusInletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 2),
    _Unit2BusInletStatus_Type()
)
unit2BusInletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusInletStatus.setStatus("current")
_Unit2BusRMSLN_Type = Integer32
_Unit2BusRMSLN_Object = MibTableColumn
unit2BusRMSLN = _Unit2BusRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 3),
    _Unit2BusRMSLN_Type()
)
unit2BusRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusRMSLN.setStatus("current")
_Unit2BusCurrent_Type = Integer32
_Unit2BusCurrent_Object = MibTableColumn
unit2BusCurrent = _Unit2BusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 4),
    _Unit2BusCurrent_Type()
)
unit2BusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusCurrent.setStatus("current")


class _Unit2BusCrest_Type(Integer32):
    """Custom type unit2BusCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit2BusCrest_Type.__name__ = "Integer32"
_Unit2BusCrest_Object = MibTableColumn
unit2BusCrest = _Unit2BusCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 5),
    _Unit2BusCrest_Type()
)
unit2BusCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusCrest.setStatus("current")
_Unit2BusApparentPower_Type = Integer32
_Unit2BusApparentPower_Object = MibTableColumn
unit2BusApparentPower = _Unit2BusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 6),
    _Unit2BusApparentPower_Type()
)
unit2BusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusApparentPower.setStatus("current")


class _Unit2BusRealPower_Type(Integer32):
    """Custom type unit2BusRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit2BusRealPower_Type.__name__ = "Integer32"
_Unit2BusRealPower_Object = MibTableColumn
unit2BusRealPower = _Unit2BusRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 7),
    _Unit2BusRealPower_Type()
)
unit2BusRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusRealPower.setStatus("current")
_Unit2BusPowerFactor_Type = Integer32
_Unit2BusPowerFactor_Object = MibTableColumn
unit2BusPowerFactor = _Unit2BusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 8),
    _Unit2BusPowerFactor_Type()
)
unit2BusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusPowerFactor.setStatus("current")
_Unit2BusDCOffset_Type = Integer32
_Unit2BusDCOffset_Object = MibTableColumn
unit2BusDCOffset = _Unit2BusDCOffset_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 3, 1, 9),
    _Unit2BusDCOffset_Type()
)
unit2BusDCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2BusDCOffset.setStatus("current")
_Unit2OutletTable_Object = MibTable
unit2OutletTable = _Unit2OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4)
)
if mibBuilder.loadTexts:
    unit2OutletTable.setStatus("current")
_Unit2OutletTableEntry_Object = MibTableRow
unit2OutletTableEntry = _Unit2OutletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1)
)
unit2OutletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletIndex"),
)
if mibBuilder.loadTexts:
    unit2OutletTableEntry.setStatus("current")


class _Unit2OutletIndex_Type(Integer32):
    """Custom type unit2OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit2OutletIndex_Type.__name__ = "Integer32"
_Unit2OutletIndex_Object = MibTableColumn
unit2OutletIndex = _Unit2OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 1),
    _Unit2OutletIndex_Type()
)
unit2OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit2OutletIndex.setStatus("current")
_Unit2OutletName_Type = DisplayString
_Unit2OutletName_Object = MibTableColumn
unit2OutletName = _Unit2OutletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 2),
    _Unit2OutletName_Type()
)
unit2OutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletName.setStatus("current")


class _Unit2OutletStatus_Type(Bits):
    """Custom type unit2OutletStatus based on Bits"""
    namedValues = NamedValues(
        *(("fuse", 0),
          ("relay", 1),
          ("outlet", 2),
          ("failsafe", 3),
          ("cycle", 4))
    )

_Unit2OutletStatus_Type.__name__ = "Bits"
_Unit2OutletStatus_Object = MibTableColumn
unit2OutletStatus = _Unit2OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 3),
    _Unit2OutletStatus_Type()
)
unit2OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletStatus.setStatus("current")
_Unit2OutletCycleTimer_Type = Integer32
_Unit2OutletCycleTimer_Object = MibTableColumn
unit2OutletCycleTimer = _Unit2OutletCycleTimer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 4),
    _Unit2OutletCycleTimer_Type()
)
unit2OutletCycleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletCycleTimer.setStatus("current")
_Unit2OutletCurrent_Type = Integer32
_Unit2OutletCurrent_Object = MibTableColumn
unit2OutletCurrent = _Unit2OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 5),
    _Unit2OutletCurrent_Type()
)
unit2OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletCurrent.setStatus("current")


class _Unit2OutletCrest_Type(Integer32):
    """Custom type unit2OutletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit2OutletCrest_Type.__name__ = "Integer32"
_Unit2OutletCrest_Object = MibTableColumn
unit2OutletCrest = _Unit2OutletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 6),
    _Unit2OutletCrest_Type()
)
unit2OutletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletCrest.setStatus("current")


class _Unit2OutletRealPower_Type(Integer32):
    """Custom type unit2OutletRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit2OutletRealPower_Type.__name__ = "Integer32"
_Unit2OutletRealPower_Object = MibTableColumn
unit2OutletRealPower = _Unit2OutletRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 7),
    _Unit2OutletRealPower_Type()
)
unit2OutletRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletRealPower.setStatus("current")
_Unit2OutletPowerFactor_Type = Integer32
_Unit2OutletPowerFactor_Object = MibTableColumn
unit2OutletPowerFactor = _Unit2OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 4, 1, 8),
    _Unit2OutletPowerFactor_Type()
)
unit2OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutletPowerFactor.setStatus("current")
_Unit2GPITable_Object = MibTable
unit2GPITable = _Unit2GPITable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 5)
)
if mibBuilder.loadTexts:
    unit2GPITable.setStatus("current")
_Unit2GPITableEntry_Object = MibTableRow
unit2GPITableEntry = _Unit2GPITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 5, 1)
)
unit2GPITableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit2GPIIndex"),
)
if mibBuilder.loadTexts:
    unit2GPITableEntry.setStatus("current")


class _Unit2GPIIndex_Type(Integer32):
    """Custom type unit2GPIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Unit2GPIIndex_Type.__name__ = "Integer32"
_Unit2GPIIndex_Object = MibTableColumn
unit2GPIIndex = _Unit2GPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 5, 1, 1),
    _Unit2GPIIndex_Type()
)
unit2GPIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit2GPIIndex.setStatus("current")


class _Unit2GPIState_Type(Bits):
    """Custom type unit2GPIState based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisableActive", 0),
          ("gpiFitted", 1),
          ("gpiDisabled", 2),
          ("gpiIsOutput", 3),
          ("gpiOutputSetHigh", 4),
          ("gpiReadIsHigh", 5))
    )

_Unit2GPIState_Type.__name__ = "Bits"
_Unit2GPIState_Object = MibTableColumn
unit2GPIState = _Unit2GPIState_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 5, 1, 2),
    _Unit2GPIState_Type()
)
unit2GPIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2GPIState.setStatus("current")
_Unit2SensorTable_Object = MibTable
unit2SensorTable = _Unit2SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6)
)
if mibBuilder.loadTexts:
    unit2SensorTable.setStatus("current")
_Unit2SensorTableEntry_Object = MibTableRow
unit2SensorTableEntry = _Unit2SensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1)
)
unit2SensorTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorIndex"),
)
if mibBuilder.loadTexts:
    unit2SensorTableEntry.setStatus("current")


class _Unit2SensorIndex_Type(Integer32):
    """Custom type unit2SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit2SensorIndex_Type.__name__ = "Integer32"
_Unit2SensorIndex_Object = MibTableColumn
unit2SensorIndex = _Unit2SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 1),
    _Unit2SensorIndex_Type()
)
unit2SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit2SensorIndex.setStatus("current")
_Unit2SensorName_Type = DisplayString
_Unit2SensorName_Object = MibTableColumn
unit2SensorName = _Unit2SensorName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 2),
    _Unit2SensorName_Type()
)
unit2SensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorName.setStatus("current")
_Unit2SensorType_Type = Integer32
_Unit2SensorType_Object = MibTableColumn
unit2SensorType = _Unit2SensorType_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 3),
    _Unit2SensorType_Type()
)
unit2SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorType.setStatus("current")
_Unit2SensorAddress_Type = DisplayString
_Unit2SensorAddress_Object = MibTableColumn
unit2SensorAddress = _Unit2SensorAddress_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 4),
    _Unit2SensorAddress_Type()
)
unit2SensorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorAddress.setStatus("current")


class _Unit2SensorStatus_Type(Integer32):
    """Custom type unit2SensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Unit2SensorStatus_Type.__name__ = "Integer32"
_Unit2SensorStatus_Object = MibTableColumn
unit2SensorStatus = _Unit2SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 5),
    _Unit2SensorStatus_Type()
)
unit2SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorStatus.setStatus("current")
_Unit2SensorLive_Type = Integer32
_Unit2SensorLive_Object = MibTableColumn
unit2SensorLive = _Unit2SensorLive_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 6),
    _Unit2SensorLive_Type()
)
unit2SensorLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorLive.setStatus("current")
_Unit2SensorMin_Type = Integer32
_Unit2SensorMin_Object = MibTableColumn
unit2SensorMin = _Unit2SensorMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 7),
    _Unit2SensorMin_Type()
)
unit2SensorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorMin.setStatus("current")
_Unit2SensorMax_Type = Integer32
_Unit2SensorMax_Object = MibTableColumn
unit2SensorMax = _Unit2SensorMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 3, 6, 1, 8),
    _Unit2SensorMax_Type()
)
unit2SensorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorMax.setStatus("current")
_Unit3_ObjectIdentity = ObjectIdentity
unit3 = _Unit3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4)
)
_Unit3Info_ObjectIdentity = ObjectIdentity
unit3Info = _Unit3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1)
)


class _Unit3Serial3_Type(DisplayString):
    """Custom type unit3Serial3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Unit3Serial3_Type.__name__ = "DisplayString"
_Unit3Serial3_Object = MibScalar
unit3Serial3 = _Unit3Serial3_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 1),
    _Unit3Serial3_Type()
)
unit3Serial3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3Serial3.setStatus("current")
_Unit3LocationName_Type = DisplayString
_Unit3LocationName_Object = MibScalar
unit3LocationName = _Unit3LocationName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 2),
    _Unit3LocationName_Type()
)
unit3LocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3LocationName.setStatus("current")
_Unit3FirmwareVersions_Type = DisplayString
_Unit3FirmwareVersions_Object = MibScalar
unit3FirmwareVersions = _Unit3FirmwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 3),
    _Unit3FirmwareVersions_Type()
)
unit3FirmwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3FirmwareVersions.setStatus("current")


class _Unit3Inlets_Type(Integer32):
    """Custom type unit3Inlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Unit3Inlets_Type.__name__ = "Integer32"
_Unit3Inlets_Object = MibScalar
unit3Inlets = _Unit3Inlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 4),
    _Unit3Inlets_Type()
)
unit3Inlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3Inlets.setStatus("current")


class _Unit3Outlets_Type(Integer32):
    """Custom type unit3Outlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Unit3Outlets_Type.__name__ = "Integer32"
_Unit3Outlets_Object = MibScalar
unit3Outlets = _Unit3Outlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 5),
    _Unit3Outlets_Type()
)
unit3Outlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3Outlets.setStatus("current")
_Unit3IntTemp_Type = Integer32
_Unit3IntTemp_Object = MibScalar
unit3IntTemp = _Unit3IntTemp_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 6),
    _Unit3IntTemp_Type()
)
unit3IntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3IntTemp.setStatus("current")
_Unit3IntTempMin_Type = Integer32
_Unit3IntTempMin_Object = MibScalar
unit3IntTempMin = _Unit3IntTempMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 7),
    _Unit3IntTempMin_Type()
)
unit3IntTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3IntTempMin.setStatus("current")
_Unit3IntTempMax_Type = Integer32
_Unit3IntTempMax_Object = MibScalar
unit3IntTempMax = _Unit3IntTempMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 8),
    _Unit3IntTempMax_Type()
)
unit3IntTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3IntTempMax.setStatus("current")


class _Unit3DCSupply_Type(Integer32):
    """Custom type unit3DCSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit3DCSupply_Type.__name__ = "Integer32"
_Unit3DCSupply_Object = MibScalar
unit3DCSupply = _Unit3DCSupply_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 9),
    _Unit3DCSupply_Type()
)
unit3DCSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3DCSupply.setStatus("current")


class _Unit3DCSupplyMin_Type(Integer32):
    """Custom type unit3DCSupplyMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit3DCSupplyMin_Type.__name__ = "Integer32"
_Unit3DCSupplyMin_Object = MibScalar
unit3DCSupplyMin = _Unit3DCSupplyMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 10),
    _Unit3DCSupplyMin_Type()
)
unit3DCSupplyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3DCSupplyMin.setStatus("current")


class _Unit3DCSupplyMax_Type(Integer32):
    """Custom type unit3DCSupplyMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit3DCSupplyMax_Type.__name__ = "Integer32"
_Unit3DCSupplyMax_Object = MibScalar
unit3DCSupplyMax = _Unit3DCSupplyMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 11),
    _Unit3DCSupplyMax_Type()
)
unit3DCSupplyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3DCSupplyMax.setStatus("current")


class _Unit3MiscFlags_Type(Bits):
    """Custom type unit3MiscFlags based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisabled", 0),
          ("cycleTimerRunning", 1),
          ("macroRunning", 2),
          ("fuseFailed", 3))
    )

_Unit3MiscFlags_Type.__name__ = "Bits"
_Unit3MiscFlags_Object = MibScalar
unit3MiscFlags = _Unit3MiscFlags_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 12),
    _Unit3MiscFlags_Type()
)
unit3MiscFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3MiscFlags.setStatus("current")


class _Unit3Buzzer_Type(Bits):
    """Custom type unit3Buzzer based on Bits"""
    namedValues = NamedValues(
        *(("unitLEDsFlashing", 0),
          ("unitIsBeeping", 1),
          ("bInletFailAcknowleged", 2),
          ("bInletFailed", 3),
          ("aInletFailAcknowleged", 4),
          ("aInletFailed", 5),
          ("flashingLEDsEnabled", 6),
          ("beepingEnabled", 7))
    )

_Unit3Buzzer_Type.__name__ = "Bits"
_Unit3Buzzer_Object = MibScalar
unit3Buzzer = _Unit3Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 13),
    _Unit3Buzzer_Type()
)
unit3Buzzer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3Buzzer.setStatus("current")
_Unit3AlarmGPText_Type = DisplayString
_Unit3AlarmGPText_Object = MibScalar
unit3AlarmGPText = _Unit3AlarmGPText_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 1, 14),
    _Unit3AlarmGPText_Type()
)
unit3AlarmGPText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3AlarmGPText.setStatus("current")
_Unit3InletTable_Object = MibTable
unit3InletTable = _Unit3InletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2)
)
if mibBuilder.loadTexts:
    unit3InletTable.setStatus("current")
_Unit3InletTableEntry_Object = MibTableRow
unit3InletTableEntry = _Unit3InletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1)
)
unit3InletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletIndex"),
)
if mibBuilder.loadTexts:
    unit3InletTableEntry.setStatus("current")


class _Unit3InletIndex_Type(Integer32):
    """Custom type unit3InletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit3InletIndex_Type.__name__ = "Integer32"
_Unit3InletIndex_Object = MibTableColumn
unit3InletIndex = _Unit3InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 1),
    _Unit3InletIndex_Type()
)
unit3InletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit3InletIndex.setStatus("current")
_Unit3InletName_Type = DisplayString
_Unit3InletName_Object = MibTableColumn
unit3InletName = _Unit3InletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 2),
    _Unit3InletName_Type()
)
unit3InletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletName.setStatus("current")
_UnitInletRMSLN_Type = Integer32
_UnitInletRMSLN_Object = MibTableColumn
unitInletRMSLN = _UnitInletRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 3),
    _UnitInletRMSLN_Type()
)
unitInletRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInletRMSLN.setStatus("current")
_Unit3InletPeakLN_Type = Integer32
_Unit3InletPeakLN_Object = MibTableColumn
unit3InletPeakLN = _Unit3InletPeakLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 4),
    _Unit3InletPeakLN_Type()
)
unit3InletPeakLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletPeakLN.setStatus("current")


class _Unit3InletCrest_Type(Integer32):
    """Custom type unit3InletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit3InletCrest_Type.__name__ = "Integer32"
_Unit3InletCrest_Object = MibTableColumn
unit3InletCrest = _Unit3InletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 5),
    _Unit3InletCrest_Type()
)
unit3InletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletCrest.setStatus("current")
_Unit3InletRMSNE_Type = Integer32
_Unit3InletRMSNE_Object = MibTableColumn
unit3InletRMSNE = _Unit3InletRMSNE_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 6),
    _Unit3InletRMSNE_Type()
)
unit3InletRMSNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletRMSNE.setStatus("current")


class _Unit3InletFrequency_Type(Integer32):
    """Custom type unit3InletFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit3InletFrequency_Type.__name__ = "Integer32"
_Unit3InletFrequency_Object = MibTableColumn
unit3InletFrequency = _Unit3InletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 7),
    _Unit3InletFrequency_Type()
)
unit3InletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletFrequency.setStatus("current")
_Unit3InletLeakage_Type = Integer32
_Unit3InletLeakage_Object = MibTableColumn
unit3InletLeakage = _Unit3InletLeakage_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 8),
    _Unit3InletLeakage_Type()
)
unit3InletLeakage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletLeakage.setStatus("current")


class _Unit3InletVaristors_Type(Integer32):
    """Custom type unit3InletVaristors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Unit3InletVaristors_Type.__name__ = "Integer32"
_Unit3InletVaristors_Object = MibTableColumn
unit3InletVaristors = _Unit3InletVaristors_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 2, 1, 9),
    _Unit3InletVaristors_Type()
)
unit3InletVaristors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3InletVaristors.setStatus("current")
_Unit3BusTable_Object = MibTable
unit3BusTable = _Unit3BusTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3)
)
if mibBuilder.loadTexts:
    unit3BusTable.setStatus("current")
_Unit3BusTableEntry_Object = MibTableRow
unit3BusTableEntry = _Unit3BusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1)
)
unit3BusTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusIndex"),
)
if mibBuilder.loadTexts:
    unit3BusTableEntry.setStatus("current")


class _Unit3BusIndex_Type(Integer32):
    """Custom type unit3BusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit3BusIndex_Type.__name__ = "Integer32"
_Unit3BusIndex_Object = MibTableColumn
unit3BusIndex = _Unit3BusIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 1),
    _Unit3BusIndex_Type()
)
unit3BusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit3BusIndex.setStatus("current")


class _Unit3BusInletStatus_Type(Bits):
    """Custom type unit3BusInletStatus based on Bits"""
    namedValues = NamedValues(
        *(("aInletAvailable", 0),
          ("bInletAvailable", 1),
          ("aInletSelected", 2),
          ("inletPreferenceSet", 3),
          ("aInletPreferred", 4),
          ("nonSyncChangeAllowed", 5),
          ("inletsNotInSync", 6))
    )

_Unit3BusInletStatus_Type.__name__ = "Bits"
_Unit3BusInletStatus_Object = MibTableColumn
unit3BusInletStatus = _Unit3BusInletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 2),
    _Unit3BusInletStatus_Type()
)
unit3BusInletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusInletStatus.setStatus("current")
_Unit3BusRMSLN_Type = Integer32
_Unit3BusRMSLN_Object = MibTableColumn
unit3BusRMSLN = _Unit3BusRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 3),
    _Unit3BusRMSLN_Type()
)
unit3BusRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusRMSLN.setStatus("current")
_Unit3BusCurrent_Type = Integer32
_Unit3BusCurrent_Object = MibTableColumn
unit3BusCurrent = _Unit3BusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 4),
    _Unit3BusCurrent_Type()
)
unit3BusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusCurrent.setStatus("current")


class _Unit3BusCrest_Type(Integer32):
    """Custom type unit3BusCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit3BusCrest_Type.__name__ = "Integer32"
_Unit3BusCrest_Object = MibTableColumn
unit3BusCrest = _Unit3BusCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 5),
    _Unit3BusCrest_Type()
)
unit3BusCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusCrest.setStatus("current")
_Unit3BusApparentPower_Type = Integer32
_Unit3BusApparentPower_Object = MibTableColumn
unit3BusApparentPower = _Unit3BusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 6),
    _Unit3BusApparentPower_Type()
)
unit3BusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusApparentPower.setStatus("current")


class _Unit3BusRealPower_Type(Integer32):
    """Custom type unit3BusRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit3BusRealPower_Type.__name__ = "Integer32"
_Unit3BusRealPower_Object = MibTableColumn
unit3BusRealPower = _Unit3BusRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 7),
    _Unit3BusRealPower_Type()
)
unit3BusRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusRealPower.setStatus("current")
_Unit3BusPowerFactor_Type = Integer32
_Unit3BusPowerFactor_Object = MibTableColumn
unit3BusPowerFactor = _Unit3BusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 8),
    _Unit3BusPowerFactor_Type()
)
unit3BusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusPowerFactor.setStatus("current")
_Unit3BusDCOffset_Type = Integer32
_Unit3BusDCOffset_Object = MibTableColumn
unit3BusDCOffset = _Unit3BusDCOffset_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 3, 1, 9),
    _Unit3BusDCOffset_Type()
)
unit3BusDCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3BusDCOffset.setStatus("current")
_Unit3OutletTable_Object = MibTable
unit3OutletTable = _Unit3OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4)
)
if mibBuilder.loadTexts:
    unit3OutletTable.setStatus("current")
_Unit3OutletTableEntry_Object = MibTableRow
unit3OutletTableEntry = _Unit3OutletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1)
)
unit3OutletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletIndex"),
)
if mibBuilder.loadTexts:
    unit3OutletTableEntry.setStatus("current")


class _Unit3OutletIndex_Type(Integer32):
    """Custom type unit3OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit3OutletIndex_Type.__name__ = "Integer32"
_Unit3OutletIndex_Object = MibTableColumn
unit3OutletIndex = _Unit3OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 1),
    _Unit3OutletIndex_Type()
)
unit3OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit3OutletIndex.setStatus("current")
_Unit3OutletName_Type = DisplayString
_Unit3OutletName_Object = MibTableColumn
unit3OutletName = _Unit3OutletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 2),
    _Unit3OutletName_Type()
)
unit3OutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletName.setStatus("current")


class _Unit3OutletStatus_Type(Bits):
    """Custom type unit3OutletStatus based on Bits"""
    namedValues = NamedValues(
        *(("fuse", 0),
          ("relay", 1),
          ("outlet", 2),
          ("failsafe", 3),
          ("cycle", 4))
    )

_Unit3OutletStatus_Type.__name__ = "Bits"
_Unit3OutletStatus_Object = MibTableColumn
unit3OutletStatus = _Unit3OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 3),
    _Unit3OutletStatus_Type()
)
unit3OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletStatus.setStatus("current")
_Unit3OutletCycleTimer_Type = Integer32
_Unit3OutletCycleTimer_Object = MibTableColumn
unit3OutletCycleTimer = _Unit3OutletCycleTimer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 4),
    _Unit3OutletCycleTimer_Type()
)
unit3OutletCycleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletCycleTimer.setStatus("current")
_Unit3OutletCurrent_Type = Integer32
_Unit3OutletCurrent_Object = MibTableColumn
unit3OutletCurrent = _Unit3OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 5),
    _Unit3OutletCurrent_Type()
)
unit3OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletCurrent.setStatus("current")


class _Unit3OutletCrest_Type(Integer32):
    """Custom type unit3OutletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit3OutletCrest_Type.__name__ = "Integer32"
_Unit3OutletCrest_Object = MibTableColumn
unit3OutletCrest = _Unit3OutletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 6),
    _Unit3OutletCrest_Type()
)
unit3OutletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletCrest.setStatus("current")


class _Unit3OutletRealPower_Type(Integer32):
    """Custom type unit3OutletRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit3OutletRealPower_Type.__name__ = "Integer32"
_Unit3OutletRealPower_Object = MibTableColumn
unit3OutletRealPower = _Unit3OutletRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 7),
    _Unit3OutletRealPower_Type()
)
unit3OutletRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletRealPower.setStatus("current")
_Unit3OutletPowerFactor_Type = Integer32
_Unit3OutletPowerFactor_Object = MibTableColumn
unit3OutletPowerFactor = _Unit3OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 4, 1, 8),
    _Unit3OutletPowerFactor_Type()
)
unit3OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutletPowerFactor.setStatus("current")
_Unit3GPITable_Object = MibTable
unit3GPITable = _Unit3GPITable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 5)
)
if mibBuilder.loadTexts:
    unit3GPITable.setStatus("current")
_Unit3GPITableEntry_Object = MibTableRow
unit3GPITableEntry = _Unit3GPITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 5, 1)
)
unit3GPITableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit3GPIIndex"),
)
if mibBuilder.loadTexts:
    unit3GPITableEntry.setStatus("current")


class _Unit3GPIIndex_Type(Integer32):
    """Custom type unit3GPIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Unit3GPIIndex_Type.__name__ = "Integer32"
_Unit3GPIIndex_Object = MibTableColumn
unit3GPIIndex = _Unit3GPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 5, 1, 1),
    _Unit3GPIIndex_Type()
)
unit3GPIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit3GPIIndex.setStatus("current")


class _Unit3GPIState_Type(Bits):
    """Custom type unit3GPIState based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisableActive", 0),
          ("gpiFitted", 1),
          ("gpiDisabled", 2),
          ("gpiIsOutput", 3),
          ("gpiOutputSetHigh", 4),
          ("gpiReadIsHigh", 5))
    )

_Unit3GPIState_Type.__name__ = "Bits"
_Unit3GPIState_Object = MibTableColumn
unit3GPIState = _Unit3GPIState_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 5, 1, 2),
    _Unit3GPIState_Type()
)
unit3GPIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3GPIState.setStatus("current")
_Unit3SensorTable_Object = MibTable
unit3SensorTable = _Unit3SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6)
)
if mibBuilder.loadTexts:
    unit3SensorTable.setStatus("current")
_Unit3SensorTableEntry_Object = MibTableRow
unit3SensorTableEntry = _Unit3SensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1)
)
unit3SensorTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorIndex"),
)
if mibBuilder.loadTexts:
    unit3SensorTableEntry.setStatus("current")


class _Unit3SensorIndex_Type(Integer32):
    """Custom type unit3SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit3SensorIndex_Type.__name__ = "Integer32"
_Unit3SensorIndex_Object = MibTableColumn
unit3SensorIndex = _Unit3SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 1),
    _Unit3SensorIndex_Type()
)
unit3SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit3SensorIndex.setStatus("current")
_Unit3SensorName_Type = DisplayString
_Unit3SensorName_Object = MibTableColumn
unit3SensorName = _Unit3SensorName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 2),
    _Unit3SensorName_Type()
)
unit3SensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorName.setStatus("current")
_Unit3SensorType_Type = Integer32
_Unit3SensorType_Object = MibTableColumn
unit3SensorType = _Unit3SensorType_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 3),
    _Unit3SensorType_Type()
)
unit3SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorType.setStatus("current")
_Unit3SensorAddress_Type = DisplayString
_Unit3SensorAddress_Object = MibTableColumn
unit3SensorAddress = _Unit3SensorAddress_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 4),
    _Unit3SensorAddress_Type()
)
unit3SensorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorAddress.setStatus("current")


class _Unit3SensorStatus_Type(Integer32):
    """Custom type unit3SensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Unit3SensorStatus_Type.__name__ = "Integer32"
_Unit3SensorStatus_Object = MibTableColumn
unit3SensorStatus = _Unit3SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 5),
    _Unit3SensorStatus_Type()
)
unit3SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorStatus.setStatus("current")
_Unit3SensorLive_Type = Integer32
_Unit3SensorLive_Object = MibTableColumn
unit3SensorLive = _Unit3SensorLive_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 6),
    _Unit3SensorLive_Type()
)
unit3SensorLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorLive.setStatus("current")
_Unit3SensorMin_Type = Integer32
_Unit3SensorMin_Object = MibTableColumn
unit3SensorMin = _Unit3SensorMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 7),
    _Unit3SensorMin_Type()
)
unit3SensorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorMin.setStatus("current")
_Unit3SensorMax_Type = Integer32
_Unit3SensorMax_Object = MibTableColumn
unit3SensorMax = _Unit3SensorMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 4, 6, 1, 8),
    _Unit3SensorMax_Type()
)
unit3SensorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorMax.setStatus("current")
_Unit4_ObjectIdentity = ObjectIdentity
unit4 = _Unit4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5)
)
_Unit4Info_ObjectIdentity = ObjectIdentity
unit4Info = _Unit4Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1)
)


class _Unit4Serial_Type(DisplayString):
    """Custom type unit4Serial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Unit4Serial_Type.__name__ = "DisplayString"
_Unit4Serial_Object = MibScalar
unit4Serial = _Unit4Serial_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 1),
    _Unit4Serial_Type()
)
unit4Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4Serial.setStatus("current")
_Unit4LocationName_Type = DisplayString
_Unit4LocationName_Object = MibScalar
unit4LocationName = _Unit4LocationName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 2),
    _Unit4LocationName_Type()
)
unit4LocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4LocationName.setStatus("current")
_Unit4FirmwareVersions_Type = DisplayString
_Unit4FirmwareVersions_Object = MibScalar
unit4FirmwareVersions = _Unit4FirmwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 3),
    _Unit4FirmwareVersions_Type()
)
unit4FirmwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4FirmwareVersions.setStatus("current")


class _Unit4Inlets_Type(Integer32):
    """Custom type unit4Inlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Unit4Inlets_Type.__name__ = "Integer32"
_Unit4Inlets_Object = MibScalar
unit4Inlets = _Unit4Inlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 4),
    _Unit4Inlets_Type()
)
unit4Inlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4Inlets.setStatus("current")


class _Unit4Outlets_Type(Integer32):
    """Custom type unit4Outlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Unit4Outlets_Type.__name__ = "Integer32"
_Unit4Outlets_Object = MibScalar
unit4Outlets = _Unit4Outlets_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 5),
    _Unit4Outlets_Type()
)
unit4Outlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4Outlets.setStatus("current")
_Unit4IntTemp_Type = Integer32
_Unit4IntTemp_Object = MibScalar
unit4IntTemp = _Unit4IntTemp_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 6),
    _Unit4IntTemp_Type()
)
unit4IntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4IntTemp.setStatus("current")
_Unit4IntTempMin_Type = Integer32
_Unit4IntTempMin_Object = MibScalar
unit4IntTempMin = _Unit4IntTempMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 7),
    _Unit4IntTempMin_Type()
)
unit4IntTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4IntTempMin.setStatus("current")
_Unit4IntTempMax_Type = Integer32
_Unit4IntTempMax_Object = MibScalar
unit4IntTempMax = _Unit4IntTempMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 8),
    _Unit4IntTempMax_Type()
)
unit4IntTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4IntTempMax.setStatus("current")


class _Unit4DCSupply_Type(Integer32):
    """Custom type unit4DCSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit4DCSupply_Type.__name__ = "Integer32"
_Unit4DCSupply_Object = MibScalar
unit4DCSupply = _Unit4DCSupply_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 9),
    _Unit4DCSupply_Type()
)
unit4DCSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4DCSupply.setStatus("current")


class _Unit4DCSupplyMin_Type(Integer32):
    """Custom type unit4DCSupplyMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit4DCSupplyMin_Type.__name__ = "Integer32"
_Unit4DCSupplyMin_Object = MibScalar
unit4DCSupplyMin = _Unit4DCSupplyMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 10),
    _Unit4DCSupplyMin_Type()
)
unit4DCSupplyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4DCSupplyMin.setStatus("current")


class _Unit4DCSupplyMax_Type(Integer32):
    """Custom type unit4DCSupplyMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Unit4DCSupplyMax_Type.__name__ = "Integer32"
_Unit4DCSupplyMax_Object = MibScalar
unit4DCSupplyMax = _Unit4DCSupplyMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 11),
    _Unit4DCSupplyMax_Type()
)
unit4DCSupplyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4DCSupplyMax.setStatus("current")


class _Unit4MiscFlags_Type(Bits):
    """Custom type unit4MiscFlags based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisabled", 0),
          ("cycleTimerRunning", 1),
          ("macroRunning", 2),
          ("fuseFailed", 3))
    )

_Unit4MiscFlags_Type.__name__ = "Bits"
_Unit4MiscFlags_Object = MibScalar
unit4MiscFlags = _Unit4MiscFlags_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 12),
    _Unit4MiscFlags_Type()
)
unit4MiscFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4MiscFlags.setStatus("current")


class _Unit4Buzzer_Type(Bits):
    """Custom type unit4Buzzer based on Bits"""
    namedValues = NamedValues(
        *(("unitLEDsFlashing", 0),
          ("unitIsBeeping", 1),
          ("bInletFailAcknowleged", 2),
          ("bInletFailed", 3),
          ("aInletFailAcknowleged", 4),
          ("aInletFailed", 5),
          ("flashingLEDsEnabled", 6),
          ("beepingEnabled", 7))
    )

_Unit4Buzzer_Type.__name__ = "Bits"
_Unit4Buzzer_Object = MibScalar
unit4Buzzer = _Unit4Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 13),
    _Unit4Buzzer_Type()
)
unit4Buzzer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4Buzzer.setStatus("current")
_Unit4AlarmGPText_Type = DisplayString
_Unit4AlarmGPText_Object = MibScalar
unit4AlarmGPText = _Unit4AlarmGPText_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 1, 14),
    _Unit4AlarmGPText_Type()
)
unit4AlarmGPText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4AlarmGPText.setStatus("current")
_Unit4InletTable_Object = MibTable
unit4InletTable = _Unit4InletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2)
)
if mibBuilder.loadTexts:
    unit4InletTable.setStatus("current")
_Unit4InletTableEntry_Object = MibTableRow
unit4InletTableEntry = _Unit4InletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1)
)
unit4InletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletIndex"),
)
if mibBuilder.loadTexts:
    unit4InletTableEntry.setStatus("current")


class _Unit4InletIndex_Type(Integer32):
    """Custom type unit4InletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit4InletIndex_Type.__name__ = "Integer32"
_Unit4InletIndex_Object = MibTableColumn
unit4InletIndex = _Unit4InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 1),
    _Unit4InletIndex_Type()
)
unit4InletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit4InletIndex.setStatus("current")
_Unit4InletName_Type = DisplayString
_Unit4InletName_Object = MibTableColumn
unit4InletName = _Unit4InletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 2),
    _Unit4InletName_Type()
)
unit4InletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletName.setStatus("current")
_Unit4InletRMSLN_Type = Integer32
_Unit4InletRMSLN_Object = MibTableColumn
unit4InletRMSLN = _Unit4InletRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 3),
    _Unit4InletRMSLN_Type()
)
unit4InletRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletRMSLN.setStatus("current")
_Unit4InletPeakLN_Type = Integer32
_Unit4InletPeakLN_Object = MibTableColumn
unit4InletPeakLN = _Unit4InletPeakLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 4),
    _Unit4InletPeakLN_Type()
)
unit4InletPeakLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletPeakLN.setStatus("current")


class _Unit4InletCrest_Type(Integer32):
    """Custom type unit4InletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit4InletCrest_Type.__name__ = "Integer32"
_Unit4InletCrest_Object = MibTableColumn
unit4InletCrest = _Unit4InletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 5),
    _Unit4InletCrest_Type()
)
unit4InletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletCrest.setStatus("current")
_Unit4InletRMSNE_Type = Integer32
_Unit4InletRMSNE_Object = MibTableColumn
unit4InletRMSNE = _Unit4InletRMSNE_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 6),
    _Unit4InletRMSNE_Type()
)
unit4InletRMSNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletRMSNE.setStatus("current")


class _Unit4InletFrequency_Type(Integer32):
    """Custom type unit4InletFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit4InletFrequency_Type.__name__ = "Integer32"
_Unit4InletFrequency_Object = MibTableColumn
unit4InletFrequency = _Unit4InletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 7),
    _Unit4InletFrequency_Type()
)
unit4InletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletFrequency.setStatus("current")
_Unit4InletLeakage_Type = Integer32
_Unit4InletLeakage_Object = MibTableColumn
unit4InletLeakage = _Unit4InletLeakage_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 8),
    _Unit4InletLeakage_Type()
)
unit4InletLeakage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletLeakage.setStatus("current")


class _Unit4InletVaristors_Type(Integer32):
    """Custom type unit4InletVaristors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Unit4InletVaristors_Type.__name__ = "Integer32"
_Unit4InletVaristors_Object = MibTableColumn
unit4InletVaristors = _Unit4InletVaristors_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 2, 1, 9),
    _Unit4InletVaristors_Type()
)
unit4InletVaristors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4InletVaristors.setStatus("current")
_Unit4BusTable_Object = MibTable
unit4BusTable = _Unit4BusTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3)
)
if mibBuilder.loadTexts:
    unit4BusTable.setStatus("current")
_Unit4BusTableEntry_Object = MibTableRow
unit4BusTableEntry = _Unit4BusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1)
)
unit4BusTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusIndex"),
)
if mibBuilder.loadTexts:
    unit4BusTableEntry.setStatus("current")


class _Unit4BusIndex_Type(Integer32):
    """Custom type unit4BusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Unit4BusIndex_Type.__name__ = "Integer32"
_Unit4BusIndex_Object = MibTableColumn
unit4BusIndex = _Unit4BusIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 1),
    _Unit4BusIndex_Type()
)
unit4BusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit4BusIndex.setStatus("current")


class _Unit4BusInletStatus_Type(Bits):
    """Custom type unit4BusInletStatus based on Bits"""
    namedValues = NamedValues(
        *(("aInletAvailable", 0),
          ("bInletAvailable", 1),
          ("aInletSelected", 2),
          ("inletPreferenceSet", 3),
          ("aInletPreferred", 4),
          ("nonSyncChangeAllowed", 5),
          ("inletsNotInSync", 6))
    )

_Unit4BusInletStatus_Type.__name__ = "Bits"
_Unit4BusInletStatus_Object = MibTableColumn
unit4BusInletStatus = _Unit4BusInletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 2),
    _Unit4BusInletStatus_Type()
)
unit4BusInletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusInletStatus.setStatus("current")
_Unit4BusRMSLN_Type = Integer32
_Unit4BusRMSLN_Object = MibTableColumn
unit4BusRMSLN = _Unit4BusRMSLN_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 3),
    _Unit4BusRMSLN_Type()
)
unit4BusRMSLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusRMSLN.setStatus("current")
_Unit4BusCurrent_Type = Integer32
_Unit4BusCurrent_Object = MibTableColumn
unit4BusCurrent = _Unit4BusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 4),
    _Unit4BusCurrent_Type()
)
unit4BusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusCurrent.setStatus("current")


class _Unit4BusCrest_Type(Integer32):
    """Custom type unit4BusCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit4BusCrest_Type.__name__ = "Integer32"
_Unit4BusCrest_Object = MibTableColumn
unit4BusCrest = _Unit4BusCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 5),
    _Unit4BusCrest_Type()
)
unit4BusCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusCrest.setStatus("current")
_Unit4BusApparentPower_Type = Integer32
_Unit4BusApparentPower_Object = MibTableColumn
unit4BusApparentPower = _Unit4BusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 6),
    _Unit4BusApparentPower_Type()
)
unit4BusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusApparentPower.setStatus("current")


class _Unit4BusRealPower_Type(Integer32):
    """Custom type unit4BusRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit4BusRealPower_Type.__name__ = "Integer32"
_Unit4BusRealPower_Object = MibTableColumn
unit4BusRealPower = _Unit4BusRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 7),
    _Unit4BusRealPower_Type()
)
unit4BusRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusRealPower.setStatus("current")
_Unit4BusPowerFactor_Type = Integer32
_Unit4BusPowerFactor_Object = MibTableColumn
unit4BusPowerFactor = _Unit4BusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 8),
    _Unit4BusPowerFactor_Type()
)
unit4BusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusPowerFactor.setStatus("current")
_Unit4BusDCOffset_Type = Integer32
_Unit4BusDCOffset_Object = MibTableColumn
unit4BusDCOffset = _Unit4BusDCOffset_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 3, 1, 9),
    _Unit4BusDCOffset_Type()
)
unit4BusDCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4BusDCOffset.setStatus("current")
_Unit4OutletTable_Object = MibTable
unit4OutletTable = _Unit4OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4)
)
if mibBuilder.loadTexts:
    unit4OutletTable.setStatus("current")
_Unit4OutletTableEntry_Object = MibTableRow
unit4OutletTableEntry = _Unit4OutletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1)
)
unit4OutletTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletIndex"),
)
if mibBuilder.loadTexts:
    unit4OutletTableEntry.setStatus("current")


class _Unit4OutletIndex_Type(Integer32):
    """Custom type unit4OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit4OutletIndex_Type.__name__ = "Integer32"
_Unit4OutletIndex_Object = MibTableColumn
unit4OutletIndex = _Unit4OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 1),
    _Unit4OutletIndex_Type()
)
unit4OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit4OutletIndex.setStatus("current")
_Unit4OutletName_Type = DisplayString
_Unit4OutletName_Object = MibTableColumn
unit4OutletName = _Unit4OutletName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 2),
    _Unit4OutletName_Type()
)
unit4OutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletName.setStatus("current")


class _Unit4OutletStatus_Type(Bits):
    """Custom type unit4OutletStatus based on Bits"""
    namedValues = NamedValues(
        *(("fuse", 0),
          ("relay", 1),
          ("outlet", 2),
          ("failsafe", 3),
          ("cycle", 4))
    )

_Unit4OutletStatus_Type.__name__ = "Bits"
_Unit4OutletStatus_Object = MibTableColumn
unit4OutletStatus = _Unit4OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 3),
    _Unit4OutletStatus_Type()
)
unit4OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletStatus.setStatus("current")
_Unit4OutletCycleTimer_Type = Integer32
_Unit4OutletCycleTimer_Object = MibTableColumn
unit4OutletCycleTimer = _Unit4OutletCycleTimer_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 4),
    _Unit4OutletCycleTimer_Type()
)
unit4OutletCycleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletCycleTimer.setStatus("current")
_Unit4OutletCurrent_Type = Integer32
_Unit4OutletCurrent_Object = MibTableColumn
unit4OutletCurrent = _Unit4OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 5),
    _Unit4OutletCurrent_Type()
)
unit4OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletCurrent.setStatus("current")


class _Unit4OutletCrest_Type(Integer32):
    """Custom type unit4OutletCrest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Unit4OutletCrest_Type.__name__ = "Integer32"
_Unit4OutletCrest_Object = MibTableColumn
unit4OutletCrest = _Unit4OutletCrest_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 6),
    _Unit4OutletCrest_Type()
)
unit4OutletCrest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletCrest.setStatus("current")


class _Unit4OutletRealPower_Type(Integer32):
    """Custom type unit4OutletRealPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7000),
    )


_Unit4OutletRealPower_Type.__name__ = "Integer32"
_Unit4OutletRealPower_Object = MibTableColumn
unit4OutletRealPower = _Unit4OutletRealPower_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 7),
    _Unit4OutletRealPower_Type()
)
unit4OutletRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletRealPower.setStatus("current")
_Unit4OutletPowerFactor_Type = Integer32
_Unit4OutletPowerFactor_Object = MibTableColumn
unit4OutletPowerFactor = _Unit4OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 4, 1, 8),
    _Unit4OutletPowerFactor_Type()
)
unit4OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutletPowerFactor.setStatus("current")
_Unit4GPITable_Object = MibTable
unit4GPITable = _Unit4GPITable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 5)
)
if mibBuilder.loadTexts:
    unit4GPITable.setStatus("current")
_Unit4GPITableEntry_Object = MibTableRow
unit4GPITableEntry = _Unit4GPITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 5, 1)
)
unit4GPITableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit4GPIIndex"),
)
if mibBuilder.loadTexts:
    unit4GPITableEntry.setStatus("current")


class _Unit4GPIIndex_Type(Integer32):
    """Custom type unit4GPIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Unit4GPIIndex_Type.__name__ = "Integer32"
_Unit4GPIIndex_Object = MibTableColumn
unit4GPIIndex = _Unit4GPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 5, 1, 1),
    _Unit4GPIIndex_Type()
)
unit4GPIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit4GPIIndex.setStatus("current")


class _Unit4GPIState_Type(Bits):
    """Custom type unit4GPIState based on Bits"""
    namedValues = NamedValues(
        *(("globalGpiDisableActive", 0),
          ("gpiFitted", 1),
          ("gpiDisabled", 2),
          ("gpiIsOutput", 3),
          ("gpiOutputSetHigh", 4),
          ("gpiReadIsHigh", 5))
    )

_Unit4GPIState_Type.__name__ = "Bits"
_Unit4GPIState_Object = MibTableColumn
unit4GPIState = _Unit4GPIState_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 5, 1, 2),
    _Unit4GPIState_Type()
)
unit4GPIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4GPIState.setStatus("current")
_Unit4SensorTable_Object = MibTable
unit4SensorTable = _Unit4SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6)
)
if mibBuilder.loadTexts:
    unit4SensorTable.setStatus("current")
_Unit4SensorTableEntry_Object = MibTableRow
unit4SensorTableEntry = _Unit4SensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1)
)
unit4SensorTableEntry.setIndexNames(
    (0, "BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorIndex"),
)
if mibBuilder.loadTexts:
    unit4SensorTableEntry.setStatus("current")


class _Unit4SensorIndex_Type(Integer32):
    """Custom type unit4SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Unit4SensorIndex_Type.__name__ = "Integer32"
_Unit4SensorIndex_Object = MibTableColumn
unit4SensorIndex = _Unit4SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 1),
    _Unit4SensorIndex_Type()
)
unit4SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unit4SensorIndex.setStatus("current")
_Unit4SensorName_Type = DisplayString
_Unit4SensorName_Object = MibTableColumn
unit4SensorName = _Unit4SensorName_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 2),
    _Unit4SensorName_Type()
)
unit4SensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorName.setStatus("current")
_Unit4SensorType_Type = Integer32
_Unit4SensorType_Object = MibTableColumn
unit4SensorType = _Unit4SensorType_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 3),
    _Unit4SensorType_Type()
)
unit4SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorType.setStatus("current")
_Unit4SensorAddress_Type = DisplayString
_Unit4SensorAddress_Object = MibTableColumn
unit4SensorAddress = _Unit4SensorAddress_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 4),
    _Unit4SensorAddress_Type()
)
unit4SensorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorAddress.setStatus("current")


class _Unit4SensorStatus_Type(Integer32):
    """Custom type unit4SensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Unit4SensorStatus_Type.__name__ = "Integer32"
_Unit4SensorStatus_Object = MibTableColumn
unit4SensorStatus = _Unit4SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 5),
    _Unit4SensorStatus_Type()
)
unit4SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorStatus.setStatus("current")
_Unit4SensorLive_Type = Integer32
_Unit4SensorLive_Object = MibTableColumn
unit4SensorLive = _Unit4SensorLive_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 6),
    _Unit4SensorLive_Type()
)
unit4SensorLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorLive.setStatus("current")
_Unit4SensorMin_Type = Integer32
_Unit4SensorMin_Object = MibTableColumn
unit4SensorMin = _Unit4SensorMin_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 7),
    _Unit4SensorMin_Type()
)
unit4SensorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorMin.setStatus("current")
_Unit4SensorMax_Type = Integer32
_Unit4SensorMax_Object = MibTableColumn
unit4SensorMax = _Unit4SensorMax_Object(
    (1, 3, 6, 1, 4, 1, 23407, 2, 5, 6, 1, 8),
    _Unit4SensorMax_Type()
)
unit4SensorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorMax.setStatus("current")

# Managed Objects groups

eyePowerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23407, 2, 50)
)
eyePowerObjectGroup.setObjects(
      *(("BRYANT-EYEPOWER-SMIv2-MIB", "addressIP"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "addressMAC"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "voltagePOE"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "attackCount"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "statusRelayDisplay"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "controllerIPAddress"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1Serial"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1LocationName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1FirmwareVersions"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1Inlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1Outlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1IntTemp"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1IntTempMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1IntTempMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1DCSupply"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1DCSupplyMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1DCSupplyMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1MiscFlags"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1Buzzer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1AlarmGPText"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletPeakLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletRMSNE"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletFrequency"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletLeakage"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1InletVaristors"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusInletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusApparentPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1BusDCOffset"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletCycleTimer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1OutletPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1GPIState"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorType"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorAddress"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorLive"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit1SensorMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2Serial"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2LocationName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2FirmwareVersions"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2Inlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2Outlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2IntTemp"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2IntTempMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2IntTempMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2DCSupply"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2DCSupplyMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2DCSupplyMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2MiscFlags"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2Buzzer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2AlarmGPText"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletPeakLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletRMSNE"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletFrequency"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletLeakage"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2InletVaristors"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusInletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusApparentPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2BusDCOffset"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletCycleTimer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2OutletPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2GPIState"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorType"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorAddress"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorLive"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit2SensorMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3Serial3"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3LocationName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3FirmwareVersions"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3Inlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3Outlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3IntTemp"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3IntTempMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3IntTempMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3DCSupply"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3DCSupplyMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3DCSupplyMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3MiscFlags"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3Buzzer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3AlarmGPText"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unitInletRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletPeakLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletRMSNE"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletFrequency"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletLeakage"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3InletVaristors"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusInletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusApparentPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3BusDCOffset"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletCycleTimer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3OutletPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3GPIState"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorType"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorAddress"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorLive"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit3SensorMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4Serial"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4LocationName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4FirmwareVersions"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4Inlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4Outlets"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4IntTemp"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4IntTempMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4IntTempMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4DCSupply"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4DCSupplyMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4DCSupplyMax"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4MiscFlags"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4Buzzer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4AlarmGPText"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletPeakLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletRMSNE"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletFrequency"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletLeakage"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4InletVaristors"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusInletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusRMSLN"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusApparentPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4BusDCOffset"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletCycleTimer"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletCurrent"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletCrest"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletRealPower"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4OutletPowerFactor"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4GPIState"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorName"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorType"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorAddress"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorStatus"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorLive"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorMin"),
        ("BRYANT-EYEPOWER-SMIv2-MIB", "unit4SensorMax"))
)
if mibBuilder.loadTexts:
    eyePowerObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRYANT-EYEPOWER-SMIv2-MIB",
    **{"bryantUnlimited": bryantUnlimited,
       "eyePower": eyePower,
       "ethernet": ethernet,
       "addressIP": addressIP,
       "addressMAC": addressMAC,
       "voltagePOE": voltagePOE,
       "statusRelayDisplay": statusRelayDisplay,
       "attackCount": attackCount,
       "controllerIPAddress": controllerIPAddress,
       "unit1": unit1,
       "unit1Info": unit1Info,
       "unit1Serial": unit1Serial,
       "unit1LocationName": unit1LocationName,
       "unit1FirmwareVersions": unit1FirmwareVersions,
       "unit1Inlets": unit1Inlets,
       "unit1Outlets": unit1Outlets,
       "unit1IntTemp": unit1IntTemp,
       "unit1IntTempMin": unit1IntTempMin,
       "unit1IntTempMax": unit1IntTempMax,
       "unit1DCSupply": unit1DCSupply,
       "unit1DCSupplyMin": unit1DCSupplyMin,
       "unit1DCSupplyMax": unit1DCSupplyMax,
       "unit1MiscFlags": unit1MiscFlags,
       "unit1Buzzer": unit1Buzzer,
       "unit1AlarmGPText": unit1AlarmGPText,
       "unit1InletTable": unit1InletTable,
       "unit1InletTableEntry": unit1InletTableEntry,
       "unit1InletIndex": unit1InletIndex,
       "unit1InletName": unit1InletName,
       "unit1InletRMSLN": unit1InletRMSLN,
       "unit1InletPeakLN": unit1InletPeakLN,
       "unit1InletCrest": unit1InletCrest,
       "unit1InletRMSNE": unit1InletRMSNE,
       "unit1InletFrequency": unit1InletFrequency,
       "unit1InletLeakage": unit1InletLeakage,
       "unit1InletVaristors": unit1InletVaristors,
       "unit1BusTable": unit1BusTable,
       "unit1BusTableEntry": unit1BusTableEntry,
       "unit1BusIndex": unit1BusIndex,
       "unit1BusInletStatus": unit1BusInletStatus,
       "unit1BusRMSLN": unit1BusRMSLN,
       "unit1BusCurrent": unit1BusCurrent,
       "unit1BusCrest": unit1BusCrest,
       "unit1BusApparentPower": unit1BusApparentPower,
       "unit1BusRealPower": unit1BusRealPower,
       "unit1BusPowerFactor": unit1BusPowerFactor,
       "unit1BusDCOffset": unit1BusDCOffset,
       "unit1OutletTable": unit1OutletTable,
       "unit1OutletTableEntry": unit1OutletTableEntry,
       "unit1OutletIndex": unit1OutletIndex,
       "unit1OutletName": unit1OutletName,
       "unit1OutletStatus": unit1OutletStatus,
       "unit1OutletCycleTimer": unit1OutletCycleTimer,
       "unit1OutletCurrent": unit1OutletCurrent,
       "unit1OutletCrest": unit1OutletCrest,
       "unit1OutletRealPower": unit1OutletRealPower,
       "unit1OutletPowerFactor": unit1OutletPowerFactor,
       "unit1GPITable": unit1GPITable,
       "unit1GPITableEntry": unit1GPITableEntry,
       "unit1GPIIndex": unit1GPIIndex,
       "unit1GPIState": unit1GPIState,
       "unit1SensorTable": unit1SensorTable,
       "unit1SensorTableEntry": unit1SensorTableEntry,
       "unit1SensorIndex": unit1SensorIndex,
       "unit1SensorName": unit1SensorName,
       "unit1SensorType": unit1SensorType,
       "unit1SensorAddress": unit1SensorAddress,
       "unit1SensorStatus": unit1SensorStatus,
       "unit1SensorLive": unit1SensorLive,
       "unit1SensorMin": unit1SensorMin,
       "unit1SensorMax": unit1SensorMax,
       "unit2": unit2,
       "unit2Info": unit2Info,
       "unit2Serial": unit2Serial,
       "unit2LocationName": unit2LocationName,
       "unit2FirmwareVersions": unit2FirmwareVersions,
       "unit2Inlets": unit2Inlets,
       "unit2Outlets": unit2Outlets,
       "unit2IntTemp": unit2IntTemp,
       "unit2IntTempMin": unit2IntTempMin,
       "unit2IntTempMax": unit2IntTempMax,
       "unit2DCSupply": unit2DCSupply,
       "unit2DCSupplyMin": unit2DCSupplyMin,
       "unit2DCSupplyMax": unit2DCSupplyMax,
       "unit2MiscFlags": unit2MiscFlags,
       "unit2Buzzer": unit2Buzzer,
       "unit2AlarmGPText": unit2AlarmGPText,
       "unit2InletTable": unit2InletTable,
       "unit2InletTableEntry": unit2InletTableEntry,
       "unit2InletIndex": unit2InletIndex,
       "unit2InletName": unit2InletName,
       "unit2InletRMSLN": unit2InletRMSLN,
       "unit2InletPeakLN": unit2InletPeakLN,
       "unit2InletCrest": unit2InletCrest,
       "unit2InletRMSNE": unit2InletRMSNE,
       "unit2InletFrequency": unit2InletFrequency,
       "unit2InletLeakage": unit2InletLeakage,
       "unit2InletVaristors": unit2InletVaristors,
       "unit2BusTable": unit2BusTable,
       "unit2BusTableEntry": unit2BusTableEntry,
       "unit2BusIndex": unit2BusIndex,
       "unit2BusInletStatus": unit2BusInletStatus,
       "unit2BusRMSLN": unit2BusRMSLN,
       "unit2BusCurrent": unit2BusCurrent,
       "unit2BusCrest": unit2BusCrest,
       "unit2BusApparentPower": unit2BusApparentPower,
       "unit2BusRealPower": unit2BusRealPower,
       "unit2BusPowerFactor": unit2BusPowerFactor,
       "unit2BusDCOffset": unit2BusDCOffset,
       "unit2OutletTable": unit2OutletTable,
       "unit2OutletTableEntry": unit2OutletTableEntry,
       "unit2OutletIndex": unit2OutletIndex,
       "unit2OutletName": unit2OutletName,
       "unit2OutletStatus": unit2OutletStatus,
       "unit2OutletCycleTimer": unit2OutletCycleTimer,
       "unit2OutletCurrent": unit2OutletCurrent,
       "unit2OutletCrest": unit2OutletCrest,
       "unit2OutletRealPower": unit2OutletRealPower,
       "unit2OutletPowerFactor": unit2OutletPowerFactor,
       "unit2GPITable": unit2GPITable,
       "unit2GPITableEntry": unit2GPITableEntry,
       "unit2GPIIndex": unit2GPIIndex,
       "unit2GPIState": unit2GPIState,
       "unit2SensorTable": unit2SensorTable,
       "unit2SensorTableEntry": unit2SensorTableEntry,
       "unit2SensorIndex": unit2SensorIndex,
       "unit2SensorName": unit2SensorName,
       "unit2SensorType": unit2SensorType,
       "unit2SensorAddress": unit2SensorAddress,
       "unit2SensorStatus": unit2SensorStatus,
       "unit2SensorLive": unit2SensorLive,
       "unit2SensorMin": unit2SensorMin,
       "unit2SensorMax": unit2SensorMax,
       "unit3": unit3,
       "unit3Info": unit3Info,
       "unit3Serial3": unit3Serial3,
       "unit3LocationName": unit3LocationName,
       "unit3FirmwareVersions": unit3FirmwareVersions,
       "unit3Inlets": unit3Inlets,
       "unit3Outlets": unit3Outlets,
       "unit3IntTemp": unit3IntTemp,
       "unit3IntTempMin": unit3IntTempMin,
       "unit3IntTempMax": unit3IntTempMax,
       "unit3DCSupply": unit3DCSupply,
       "unit3DCSupplyMin": unit3DCSupplyMin,
       "unit3DCSupplyMax": unit3DCSupplyMax,
       "unit3MiscFlags": unit3MiscFlags,
       "unit3Buzzer": unit3Buzzer,
       "unit3AlarmGPText": unit3AlarmGPText,
       "unit3InletTable": unit3InletTable,
       "unit3InletTableEntry": unit3InletTableEntry,
       "unit3InletIndex": unit3InletIndex,
       "unit3InletName": unit3InletName,
       "unitInletRMSLN": unitInletRMSLN,
       "unit3InletPeakLN": unit3InletPeakLN,
       "unit3InletCrest": unit3InletCrest,
       "unit3InletRMSNE": unit3InletRMSNE,
       "unit3InletFrequency": unit3InletFrequency,
       "unit3InletLeakage": unit3InletLeakage,
       "unit3InletVaristors": unit3InletVaristors,
       "unit3BusTable": unit3BusTable,
       "unit3BusTableEntry": unit3BusTableEntry,
       "unit3BusIndex": unit3BusIndex,
       "unit3BusInletStatus": unit3BusInletStatus,
       "unit3BusRMSLN": unit3BusRMSLN,
       "unit3BusCurrent": unit3BusCurrent,
       "unit3BusCrest": unit3BusCrest,
       "unit3BusApparentPower": unit3BusApparentPower,
       "unit3BusRealPower": unit3BusRealPower,
       "unit3BusPowerFactor": unit3BusPowerFactor,
       "unit3BusDCOffset": unit3BusDCOffset,
       "unit3OutletTable": unit3OutletTable,
       "unit3OutletTableEntry": unit3OutletTableEntry,
       "unit3OutletIndex": unit3OutletIndex,
       "unit3OutletName": unit3OutletName,
       "unit3OutletStatus": unit3OutletStatus,
       "unit3OutletCycleTimer": unit3OutletCycleTimer,
       "unit3OutletCurrent": unit3OutletCurrent,
       "unit3OutletCrest": unit3OutletCrest,
       "unit3OutletRealPower": unit3OutletRealPower,
       "unit3OutletPowerFactor": unit3OutletPowerFactor,
       "unit3GPITable": unit3GPITable,
       "unit3GPITableEntry": unit3GPITableEntry,
       "unit3GPIIndex": unit3GPIIndex,
       "unit3GPIState": unit3GPIState,
       "unit3SensorTable": unit3SensorTable,
       "unit3SensorTableEntry": unit3SensorTableEntry,
       "unit3SensorIndex": unit3SensorIndex,
       "unit3SensorName": unit3SensorName,
       "unit3SensorType": unit3SensorType,
       "unit3SensorAddress": unit3SensorAddress,
       "unit3SensorStatus": unit3SensorStatus,
       "unit3SensorLive": unit3SensorLive,
       "unit3SensorMin": unit3SensorMin,
       "unit3SensorMax": unit3SensorMax,
       "unit4": unit4,
       "unit4Info": unit4Info,
       "unit4Serial": unit4Serial,
       "unit4LocationName": unit4LocationName,
       "unit4FirmwareVersions": unit4FirmwareVersions,
       "unit4Inlets": unit4Inlets,
       "unit4Outlets": unit4Outlets,
       "unit4IntTemp": unit4IntTemp,
       "unit4IntTempMin": unit4IntTempMin,
       "unit4IntTempMax": unit4IntTempMax,
       "unit4DCSupply": unit4DCSupply,
       "unit4DCSupplyMin": unit4DCSupplyMin,
       "unit4DCSupplyMax": unit4DCSupplyMax,
       "unit4MiscFlags": unit4MiscFlags,
       "unit4Buzzer": unit4Buzzer,
       "unit4AlarmGPText": unit4AlarmGPText,
       "unit4InletTable": unit4InletTable,
       "unit4InletTableEntry": unit4InletTableEntry,
       "unit4InletIndex": unit4InletIndex,
       "unit4InletName": unit4InletName,
       "unit4InletRMSLN": unit4InletRMSLN,
       "unit4InletPeakLN": unit4InletPeakLN,
       "unit4InletCrest": unit4InletCrest,
       "unit4InletRMSNE": unit4InletRMSNE,
       "unit4InletFrequency": unit4InletFrequency,
       "unit4InletLeakage": unit4InletLeakage,
       "unit4InletVaristors": unit4InletVaristors,
       "unit4BusTable": unit4BusTable,
       "unit4BusTableEntry": unit4BusTableEntry,
       "unit4BusIndex": unit4BusIndex,
       "unit4BusInletStatus": unit4BusInletStatus,
       "unit4BusRMSLN": unit4BusRMSLN,
       "unit4BusCurrent": unit4BusCurrent,
       "unit4BusCrest": unit4BusCrest,
       "unit4BusApparentPower": unit4BusApparentPower,
       "unit4BusRealPower": unit4BusRealPower,
       "unit4BusPowerFactor": unit4BusPowerFactor,
       "unit4BusDCOffset": unit4BusDCOffset,
       "unit4OutletTable": unit4OutletTable,
       "unit4OutletTableEntry": unit4OutletTableEntry,
       "unit4OutletIndex": unit4OutletIndex,
       "unit4OutletName": unit4OutletName,
       "unit4OutletStatus": unit4OutletStatus,
       "unit4OutletCycleTimer": unit4OutletCycleTimer,
       "unit4OutletCurrent": unit4OutletCurrent,
       "unit4OutletCrest": unit4OutletCrest,
       "unit4OutletRealPower": unit4OutletRealPower,
       "unit4OutletPowerFactor": unit4OutletPowerFactor,
       "unit4GPITable": unit4GPITable,
       "unit4GPITableEntry": unit4GPITableEntry,
       "unit4GPIIndex": unit4GPIIndex,
       "unit4GPIState": unit4GPIState,
       "unit4SensorTable": unit4SensorTable,
       "unit4SensorTableEntry": unit4SensorTableEntry,
       "unit4SensorIndex": unit4SensorIndex,
       "unit4SensorName": unit4SensorName,
       "unit4SensorType": unit4SensorType,
       "unit4SensorAddress": unit4SensorAddress,
       "unit4SensorStatus": unit4SensorStatus,
       "unit4SensorLive": unit4SensorLive,
       "unit4SensorMin": unit4SensorMin,
       "unit4SensorMax": unit4SensorMax,
       "eyePowerObjectGroup": eyePowerObjectGroup}
)
