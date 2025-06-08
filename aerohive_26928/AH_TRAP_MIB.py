# SNMP MIB module (AH_TRAP_MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aerohive_26928/AH_TRAP_MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 12:31:28 2025
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

(AhMACProtocol,
 AhNodeID,
 AhString,
 ahAPTrap) = mibBuilder.importSymbols(
    "AH-SMI-MIB",
    "AhMACProtocol",
    "AhNodeID",
    "AhString",
    "ahAPTrap")

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

ahTrapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AhAuthenticationMethod(TextualConvention, Integer32):
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
        *(("cwp", 0),
          ("open", 1),
          ("wep-open", 2),
          ("wep-shared", 3),
          ("wpa-psk", 4),
          ("wpa2-psk", 5),
          ("wpa-8021x", 6),
          ("wpa2-8021X", 7),
          ("wpa-auto-psk", 8),
          ("wpa-auto-8021x", 9),
          ("dynamic-wep", 10),
          ("8021x", 11))
    )



class AhEncrytionMethod(TextualConvention, Integer32):
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
        *(("AES", 0),
          ("TKIP", 1),
          ("WEP", 2),
          ("Non", 3))
    )



class AhState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ahUp", 1),
          ("ahDown", 2))
    )



class AhProbableCause(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ahClear", 0),
          ("ahUnknown", 1),
          ("ahFlashFailure", 2),
          ("ahFanFailure", 3),
          ("ahPowerSupplyFailure", 4),
          ("ahSoftwareUpgradeFailure", 5),
          ("ahRadioFailure", 6),
          ("ahConfFailure", 7))
    )



# MIB Managed Objects in the order of their OIDs

_AhNotificationVarBind_ObjectIdentity = ObjectIdentity
ahNotificationVarBind = _AhNotificationVarBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2)
)
_AhAPId_Type = AhNodeID
_AhAPId_Object = MibScalar
ahAPId = _AhAPId_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 1),
    _AhAPId_Type()
)
ahAPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahAPId.setStatus("current")
_AhAPName_Type = AhString
_AhAPName_Object = MibScalar
ahAPName = _AhAPName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 2),
    _AhAPName_Type()
)
ahAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahAPName.setStatus("current")


class _AhSeverity_Type(Integer32):
    """Custom type ahSeverity based on Integer32"""
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
        *(("undetermined", 1),
          ("info", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_AhSeverity_Type.__name__ = "Integer32"
_AhSeverity_Object = MibScalar
ahSeverity = _AhSeverity_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 3),
    _AhSeverity_Type()
)
ahSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahSeverity.setStatus("current")


class _AhObjectName_Type(DisplayString):
    """Custom type ahObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AhObjectName_Type.__name__ = "DisplayString"
_AhObjectName_Object = MibScalar
ahObjectName = _AhObjectName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 4),
    _AhObjectName_Type()
)
ahObjectName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahObjectName.setStatus("current")
_AhProbableCause_Type = AhProbableCause
_AhProbableCause_Object = MibScalar
ahProbableCause = _AhProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 5),
    _AhProbableCause_Type()
)
ahProbableCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahProbableCause.setStatus("current")
_AhCurValue_Type = Integer32
_AhCurValue_Object = MibScalar
ahCurValue = _AhCurValue_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 6),
    _AhCurValue_Type()
)
ahCurValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahCurValue.setStatus("current")
_AhThresholdHigh_Type = Integer32
_AhThresholdHigh_Object = MibScalar
ahThresholdHigh = _AhThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 7),
    _AhThresholdHigh_Type()
)
ahThresholdHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahThresholdHigh.setStatus("current")
_AhThresholdLow_Type = Integer32
_AhThresholdLow_Object = MibScalar
ahThresholdLow = _AhThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 8),
    _AhThresholdLow_Type()
)
ahThresholdLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahThresholdLow.setStatus("current")
_AhPreviousState_Type = AhState
_AhPreviousState_Object = MibScalar
ahPreviousState = _AhPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 9),
    _AhPreviousState_Type()
)
ahPreviousState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahPreviousState.setStatus("current")
_AhCurrentState_Type = AhState
_AhCurrentState_Object = MibScalar
ahCurrentState = _AhCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 10),
    _AhCurrentState_Type()
)
ahCurrentState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahCurrentState.setStatus("current")
_AhTrapDesc_Type = DisplayString
_AhTrapDesc_Object = MibScalar
ahTrapDesc = _AhTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 11),
    _AhTrapDesc_Type()
)
ahTrapDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahTrapDesc.setStatus("current")
_AhCode_Type = Integer32
_AhCode_Object = MibScalar
ahCode = _AhCode_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 12),
    _AhCode_Type()
)
ahCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahCode.setStatus("current")
_AhIfIndex_Type = Integer32
_AhIfIndex_Object = MibScalar
ahIfIndex = _AhIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 13),
    _AhIfIndex_Type()
)
ahIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahIfIndex.setStatus("current")


class _AhObjectType_Type(Integer32):
    """Custom type ahObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientLink", 1),
          ("neighborLink", 2))
    )


_AhObjectType_Type.__name__ = "Integer32"
_AhObjectType_Object = MibScalar
ahObjectType = _AhObjectType_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 14),
    _AhObjectType_Type()
)
ahObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahObjectType.setStatus("current")
_AhRemoteId_Type = AhNodeID
_AhRemoteId_Object = MibScalar
ahRemoteId = _AhRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 15),
    _AhRemoteId_Type()
)
ahRemoteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahRemoteId.setStatus("current")


class _AhIDPType_Type(Integer32):
    """Custom type ahIDPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rogue", 1),
          ("valid", 2),
          ("external", 3))
    )


_AhIDPType_Type.__name__ = "Integer32"
_AhIDPType_Object = MibScalar
ahIDPType = _AhIDPType_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 16),
    _AhIDPType_Type()
)
ahIDPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahIDPType.setStatus("current")
_AhIDPChannel_Type = Integer32
_AhIDPChannel_Object = MibScalar
ahIDPChannel = _AhIDPChannel_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 17),
    _AhIDPChannel_Type()
)
ahIDPChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahIDPChannel.setStatus("current")
_AhIDPRSSI_Type = Integer32
_AhIDPRSSI_Object = MibScalar
ahIDPRSSI = _AhIDPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 18),
    _AhIDPRSSI_Type()
)
ahIDPRSSI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahIDPRSSI.setStatus("current")


class _AhIDPCompliance_Type(Integer32):
    """Custom type ahIDPCompliance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("open_policy", 1),
          ("wep_policy", 2),
          ("wpa_policy", 4),
          ("wmm_policy", 8),
          ("oui_policy", 16),
          ("ssid_policy", 32),
          ("short_preamble_policy", 64),
          ("short_beacon_policy", 128),
          ("ad_hoc_policy", 256))
    )


_AhIDPCompliance_Type.__name__ = "Integer32"
_AhIDPCompliance_Object = MibScalar
ahIDPCompliance = _AhIDPCompliance_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 19),
    _AhIDPCompliance_Type()
)
ahIDPCompliance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahIDPCompliance.setStatus("current")


class _AhSSID_Type(DisplayString):
    """Custom type ahSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AhSSID_Type.__name__ = "DisplayString"
_AhSSID_Object = MibScalar
ahSSID = _AhSSID_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 20),
    _AhSSID_Type()
)
ahSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahSSID.setStatus("current")


class _AhStationType_Type(Integer32):
    """Custom type ahStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("station_ap", 1),
          ("station_client", 2))
    )


_AhStationType_Type.__name__ = "Integer32"
_AhStationType_Object = MibScalar
ahStationType = _AhStationType_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 21),
    _AhStationType_Type()
)
ahStationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahStationType.setStatus("current")


class _AhIDPStationData_Type(Integer32):
    """Custom type ahIDPStationData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("open_policy", 1),
          ("wep_policy", 2),
          ("wpa_policy", 4),
          ("wmm_policy", 8),
          ("short_preamble_policy", 64),
          ("short_beacon_policy", 128),
          ("ad_hoc_policy", 256))
    )


_AhIDPStationData_Type.__name__ = "Integer32"
_AhIDPStationData_Object = MibScalar
ahIDPStationData = _AhIDPStationData_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 22),
    _AhIDPStationData_Type()
)
ahIDPStationData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahIDPStationData.setStatus("current")


class _AhRemoved_Type(Integer32):
    """Custom type ahRemoved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("removed_false", 0),
          ("removed_true", 1))
    )


_AhRemoved_Type.__name__ = "Integer32"
_AhRemoved_Object = MibScalar
ahRemoved = _AhRemoved_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 23),
    _AhRemoved_Type()
)
ahRemoved.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahRemoved.setStatus("current")
_AhClientMAC_Type = AhNodeID
_AhClientMAC_Object = MibScalar
ahClientMAC = _AhClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 24),
    _AhClientMAC_Type()
)
ahClientMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahClientMAC.setStatus("current")
_AhCLientIP_Type = DisplayString
_AhCLientIP_Object = MibScalar
ahCLientIP = _AhCLientIP_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 25),
    _AhCLientIP_Type()
)
ahCLientIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahCLientIP.setStatus("current")
_AhClientHostName_Type = DisplayString
_AhClientHostName_Object = MibScalar
ahClientHostName = _AhClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 26),
    _AhClientHostName_Type()
)
ahClientHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahClientHostName.setStatus("current")
_AhClientUserName_Type = DisplayString
_AhClientUserName_Object = MibScalar
ahClientUserName = _AhClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 27),
    _AhClientUserName_Type()
)
ahClientUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahClientUserName.setStatus("current")


class _AhPowerSrc_Type(Integer32):
    """Custom type ahPowerSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adaptor", 0),
          ("poe", 1))
    )


_AhPowerSrc_Type.__name__ = "Integer32"
_AhPowerSrc_Object = MibScalar
ahPowerSrc = _AhPowerSrc_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 28),
    _AhPowerSrc_Type()
)
ahPowerSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahPowerSrc.setStatus("current")
_AhPoEEth0On_Type = TruthValue
_AhPoEEth0On_Object = MibScalar
ahPoEEth0On = _AhPoEEth0On_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 29),
    _AhPoEEth0On_Type()
)
ahPoEEth0On.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahPoEEth0On.setStatus("current")
_AhPoEEth0Pwr_Type = Integer32
_AhPoEEth0Pwr_Object = MibScalar
ahPoEEth0Pwr = _AhPoEEth0Pwr_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 30),
    _AhPoEEth0Pwr_Type()
)
ahPoEEth0Pwr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahPoEEth0Pwr.setStatus("current")
_AhPoEEth1On_Type = TruthValue
_AhPoEEth1On_Object = MibScalar
ahPoEEth1On = _AhPoEEth1On_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 31),
    _AhPoEEth1On_Type()
)
ahPoEEth1On.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahPoEEth1On.setStatus("current")
_AhPoEEth1Pwr_Type = Integer32
_AhPoEEth1Pwr_Object = MibScalar
ahPoEEth1Pwr = _AhPoEEth1Pwr_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 32),
    _AhPoEEth1Pwr_Type()
)
ahPoEEth1Pwr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ahPoEEth1Pwr.setStatus("current")
_AhRadioChannel_Type = Integer32
_AhRadioChannel_Object = MibScalar
ahRadioChannel = _AhRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 33),
    _AhRadioChannel_Type()
)
ahRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioChannel.setStatus("current")
_AhRadioTxPower_Type = Integer32
_AhRadioTxPower_Object = MibScalar
ahRadioTxPower = _AhRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 34),
    _AhRadioTxPower_Type()
)
ahRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxPower.setStatus("current")
_AhClientAuthMethod_Type = AhAuthenticationMethod
_AhClientAuthMethod_Object = MibScalar
ahClientAuthMethod = _AhClientAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 35),
    _AhClientAuthMethod_Type()
)
ahClientAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientAuthMethod.setStatus("current")
_AhClientEncryptionMethod_Type = AhEncrytionMethod
_AhClientEncryptionMethod_Object = MibScalar
ahClientEncryptionMethod = _AhClientEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 36),
    _AhClientEncryptionMethod_Type()
)
ahClientEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientEncryptionMethod.setStatus("current")
_AhClientMACProtocol_Type = AhMACProtocol
_AhClientMACProtocol_Object = MibScalar
ahClientMACProtocol = _AhClientMACProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 37),
    _AhClientMACProtocol_Type()
)
ahClientMACProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientMACProtocol.setStatus("current")
_AhClientVLAN_Type = Integer32
_AhClientVLAN_Object = MibScalar
ahClientVLAN = _AhClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 38),
    _AhClientVLAN_Type()
)
ahClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientVLAN.setStatus("current")
_AhClientUserProfId_Type = Integer32
_AhClientUserProfId_Object = MibScalar
ahClientUserProfId = _AhClientUserProfId_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 39),
    _AhClientUserProfId_Type()
)
ahClientUserProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientUserProfId.setStatus("current")
_AhClientChannel_Type = Integer32
_AhClientChannel_Object = MibScalar
ahClientChannel = _AhClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 40),
    _AhClientChannel_Type()
)
ahClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientChannel.setStatus("current")
_AhClientCWPUsed_Type = TruthValue
_AhClientCWPUsed_Object = MibScalar
ahClientCWPUsed = _AhClientCWPUsed_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 41),
    _AhClientCWPUsed_Type()
)
ahClientCWPUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientCWPUsed.setStatus("current")
_AhBSSID_Type = AhNodeID
_AhBSSID_Object = MibScalar
ahBSSID = _AhBSSID_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 42),
    _AhBSSID_Type()
)
ahBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahBSSID.setStatus("current")


class _AhPoEEth0MaxSpeed_Type(Integer32):
    """Custom type ahPoEEth0MaxSpeed based on Integer32"""
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
        *(("linkdown", 1),
          ("eth10", 2),
          ("eth100", 3),
          ("eth1000", 4))
    )


_AhPoEEth0MaxSpeed_Type.__name__ = "Integer32"
_AhPoEEth0MaxSpeed_Object = MibScalar
ahPoEEth0MaxSpeed = _AhPoEEth0MaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 43),
    _AhPoEEth0MaxSpeed_Type()
)
ahPoEEth0MaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahPoEEth0MaxSpeed.setStatus("current")


class _AhPoEEth1MaxSpeed_Type(Integer32):
    """Custom type ahPoEEth1MaxSpeed based on Integer32"""
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
        *(("linkdown", 1),
          ("eth10", 2),
          ("eth100", 3),
          ("eth1000", 4))
    )


_AhPoEEth1MaxSpeed_Type.__name__ = "Integer32"
_AhPoEEth1MaxSpeed_Object = MibScalar
ahPoEEth1MaxSpeed = _AhPoEEth1MaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 44),
    _AhPoEEth1MaxSpeed_Type()
)
ahPoEEth1MaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahPoEEth1MaxSpeed.setStatus("current")


class _AhPoEWifi0Setting_Type(Integer32):
    """Custom type ahPoEWifi0Setting based on Integer32"""
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
        *(("invalid", 0),
          ("linkdown", 1),
          ("config", 2),
          ("tx2rx3", 3))
    )


_AhPoEWifi0Setting_Type.__name__ = "Integer32"
_AhPoEWifi0Setting_Object = MibScalar
ahPoEWifi0Setting = _AhPoEWifi0Setting_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 45),
    _AhPoEWifi0Setting_Type()
)
ahPoEWifi0Setting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahPoEWifi0Setting.setStatus("current")


class _AhPoEWifi1Setting_Type(Integer32):
    """Custom type ahPoEWifi1Setting based on Integer32"""
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
        *(("invalid", 0),
          ("linkdown", 1),
          ("config", 2),
          ("tx2rx3", 3))
    )


_AhPoEWifi1Setting_Type.__name__ = "Integer32"
_AhPoEWifi1Setting_Object = MibScalar
ahPoEWifi1Setting = _AhPoEWifi1Setting_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 46),
    _AhPoEWifi1Setting_Type()
)
ahPoEWifi1Setting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahPoEWifi1Setting.setStatus("current")


class _AhPoEWifi2Setting_Type(Integer32):
    """Custom type ahPoEWifi2Setting based on Integer32"""
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
        *(("invalid", 0),
          ("linkdown", 1),
          ("config", 2),
          ("tx2rx3", 3))
    )


_AhPoEWifi2Setting_Type.__name__ = "Integer32"
_AhPoEWifi2Setting_Object = MibScalar
ahPoEWifi2Setting = _AhPoEWifi2Setting_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 47),
    _AhPoEWifi2Setting_Type()
)
ahPoEWifi2Setting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahPoEWifi2Setting.setStatus("current")
_AhAssociationTime_Type = Counter32
_AhAssociationTime_Object = MibScalar
ahAssociationTime = _AhAssociationTime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 48),
    _AhAssociationTime_Type()
)
ahAssociationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahAssociationTime.setStatus("current")
_AhIDPInNet_Type = TruthValue
_AhIDPInNet_Object = MibScalar
ahIDPInNet = _AhIDPInNet_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 49),
    _AhIDPInNet_Type()
)
ahIDPInNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIDPInNet.setStatus("current")
_AhDiscoverAge_Type = Counter32
_AhDiscoverAge_Object = MibScalar
ahDiscoverAge = _AhDiscoverAge_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 50),
    _AhDiscoverAge_Type()
)
ahDiscoverAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahDiscoverAge.setStatus("current")
_AhUpdateAge_Type = Counter32
_AhUpdateAge_Object = MibScalar
ahUpdateAge = _AhUpdateAge_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 51),
    _AhUpdateAge_Type()
)
ahUpdateAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahUpdateAge.setStatus("current")
_AhRunningAverageInterference_Type = Integer32
_AhRunningAverageInterference_Object = MibScalar
ahRunningAverageInterference = _AhRunningAverageInterference_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 52),
    _AhRunningAverageInterference_Type()
)
ahRunningAverageInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRunningAverageInterference.setStatus("current")
_AhShortTermInterference_Type = Integer32
_AhShortTermInterference_Object = MibScalar
ahShortTermInterference = _AhShortTermInterference_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 53),
    _AhShortTermInterference_Type()
)
ahShortTermInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahShortTermInterference.setStatus("current")
_AhSnapshotInterference_Type = Integer32
_AhSnapshotInterference_Object = MibScalar
ahSnapshotInterference = _AhSnapshotInterference_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 54),
    _AhSnapshotInterference_Type()
)
ahSnapshotInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSnapshotInterference.setStatus("current")
_AhFailureSet_Type = TruthValue
_AhFailureSet_Object = MibScalar
ahFailureSet = _AhFailureSet_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 55),
    _AhFailureSet_Type()
)
ahFailureSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFailureSet.setStatus("current")
_AhInterferenceThreshold_Type = Integer32
_AhInterferenceThreshold_Object = MibScalar
ahInterferenceThreshold = _AhInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 56),
    _AhInterferenceThreshold_Type()
)
ahInterferenceThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahInterferenceThreshold.setStatus("current")
_AhCRCErrRateThreshold_Type = Integer32
_AhCRCErrRateThreshold_Object = MibScalar
ahCRCErrRateThreshold = _AhCRCErrRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 57),
    _AhCRCErrRateThreshold_Type()
)
ahCRCErrRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahCRCErrRateThreshold.setStatus("current")
_AhCRCErrRate_Type = Integer32
_AhCRCErrRate_Object = MibScalar
ahCRCErrRate = _AhCRCErrRate_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 58),
    _AhCRCErrRate_Type()
)
ahCRCErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahCRCErrRate.setStatus("current")


class _AhBandwidthSentinelStatus_Type(Integer32):
    """Custom type ahBandwidthSentinelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alert", 0),
          ("clear", 1),
          ("bad", 2))
    )


_AhBandwidthSentinelStatus_Type.__name__ = "Integer32"
_AhBandwidthSentinelStatus_Object = MibScalar
ahBandwidthSentinelStatus = _AhBandwidthSentinelStatus_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 59),
    _AhBandwidthSentinelStatus_Type()
)
ahBandwidthSentinelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahBandwidthSentinelStatus.setStatus("current")
_AhGuaranteedBandwidth_Type = Integer32
_AhGuaranteedBandwidth_Object = MibScalar
ahGuaranteedBandwidth = _AhGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 60),
    _AhGuaranteedBandwidth_Type()
)
ahGuaranteedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahGuaranteedBandwidth.setStatus("current")
_AhActualBandwidth_Type = Integer32
_AhActualBandwidth_Object = MibScalar
ahActualBandwidth = _AhActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 61),
    _AhActualBandwidth_Type()
)
ahActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahActualBandwidth.setStatus("current")
_AhBandwidthSentinelAction_Type = Counter32
_AhBandwidthSentinelAction_Object = MibScalar
ahBandwidthSentinelAction = _AhBandwidthSentinelAction_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 62),
    _AhBandwidthSentinelAction_Type()
)
ahBandwidthSentinelAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahBandwidthSentinelAction.setStatus("current")
_AhBeaconInterval_Type = Counter32
_AhBeaconInterval_Object = MibScalar
ahBeaconInterval = _AhBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 63),
    _AhBeaconInterval_Type()
)
ahBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahBeaconInterval.setStatus("current")


class _AhLevel_Type(Integer32):
    """Custom type ahLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("client", 2))
    )


_AhLevel_Type.__name__ = "Integer32"
_AhLevel_Object = MibScalar
ahLevel = _AhLevel_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 64),
    _AhLevel_Type()
)
ahLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLevel.setStatus("current")


class _AhAlarmAlertType_Type(Integer32):
    """Custom type ahAlarmAlertType based on Integer32"""
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
        *(("crcrate", 0),
          ("txdroprate", 1),
          ("txretryrate", 2),
          ("rxdroprate", 3),
          ("airtime", 4))
    )


_AhAlarmAlertType_Type.__name__ = "Integer32"
_AhAlarmAlertType_Object = MibScalar
ahAlarmAlertType = _AhAlarmAlertType_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 65),
    _AhAlarmAlertType_Type()
)
ahAlarmAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahAlarmAlertType.setStatus("current")
_AhThresholdValue_Type = Integer32
_AhThresholdValue_Object = MibScalar
ahThresholdValue = _AhThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 66),
    _AhThresholdValue_Type()
)
ahThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahThresholdValue.setStatus("current")
_AhShortTermValue_Type = Integer32
_AhShortTermValue_Object = MibScalar
ahShortTermValue = _AhShortTermValue_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 67),
    _AhShortTermValue_Type()
)
ahShortTermValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahShortTermValue.setStatus("current")
_AhSnapshotValue_Type = Integer32
_AhSnapshotValue_Object = MibScalar
ahSnapshotValue = _AhSnapshotValue_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 68),
    _AhSnapshotValue_Type()
)
ahSnapshotValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSnapshotValue.setStatus("current")
_AhIfName_Type = AhString
_AhIfName_Object = MibScalar
ahIfName = _AhIfName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 2, 69),
    _AhIfName_Type()
)
ahIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIfName.setStatus("current")

# Managed Objects groups


# Notification objects

ahFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 1)
)
ahFailureTrap.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahSeverity"),
        ("AH_TRAP_MIB", "ahProbableCause"),
        ("AH_TRAP_MIB", "ahFailureSet"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahFailureTrap.setStatus(
        "current"
    )

ahThresholdCrossingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 2)
)
ahThresholdCrossingEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahCurValue"),
        ("AH_TRAP_MIB", "ahThresholdHigh"),
        ("AH_TRAP_MIB", "ahThresholdLow"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahThresholdCrossingEvent.setStatus(
        "current"
    )

ahStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 3)
)
ahStateChangeEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahPreviousState"),
        ("AH_TRAP_MIB", "ahCurrentState"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahStateChangeEvent.setStatus(
        "current"
    )

ahConnectionChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 4)
)
ahConnectionChangeEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahObjectType"),
        ("AH_TRAP_MIB", "ahRemoteId"),
        ("AH_TRAP_MIB", "ahCurrentState"),
        ("AH_TRAP_MIB", "ahSSID"),
        ("AH_TRAP_MIB", "ahCLientIP"),
        ("AH_TRAP_MIB", "ahClientHostName"),
        ("AH_TRAP_MIB", "ahClientUserName"),
        ("AH_TRAP_MIB", "ahClientAuthMethod"),
        ("AH_TRAP_MIB", "ahClientEncryptionMethod"),
        ("AH_TRAP_MIB", "ahClientMACProtocol"),
        ("AH_TRAP_MIB", "ahClientVLAN"),
        ("AH_TRAP_MIB", "ahClientUserProfId"),
        ("AH_TRAP_MIB", "ahClientChannel"),
        ("AH_TRAP_MIB", "ahClientCWPUsed"),
        ("AH_TRAP_MIB", "ahBSSID"),
        ("AH_TRAP_MIB", "ahAssociationTime"),
        ("AH_TRAP_MIB", "ahIfName"),
        ("AH_TRAP_MIB", "ahIDPRSSI"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahConnectionChangeEvent.setStatus(
        "current"
    )

ahIDPStationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 5)
)
ahIDPStationEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahStationType"),
        ("AH_TRAP_MIB", "ahRemoteId"),
        ("AH_TRAP_MIB", "ahIDPType"),
        ("AH_TRAP_MIB", "ahIDPChannel"),
        ("AH_TRAP_MIB", "ahIDPRSSI"),
        ("AH_TRAP_MIB", "ahIDPStationData"),
        ("AH_TRAP_MIB", "ahIDPCompliance"),
        ("AH_TRAP_MIB", "ahSSID"),
        ("AH_TRAP_MIB", "ahRemoved"),
        ("AH_TRAP_MIB", "ahIDPInNet"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahIDPStationEvent.setStatus(
        "current"
    )

ahClientInfoEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 6)
)
ahClientInfoEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahSSID"),
        ("AH_TRAP_MIB", "ahClientMAC"),
        ("AH_TRAP_MIB", "ahCLientIP"),
        ("AH_TRAP_MIB", "ahClientHostName"),
        ("AH_TRAP_MIB", "ahClientUserName"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahClientInfoEvent.setStatus(
        "current"
    )

ahPoEEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 7)
)
ahPoEEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahPowerSrc"),
        ("AH_TRAP_MIB", "ahPoEEth0On"),
        ("AH_TRAP_MIB", "ahPoEEth0Pwr"),
        ("AH_TRAP_MIB", "ahPoEEth0MaxSpeed"),
        ("AH_TRAP_MIB", "ahPoEWifi0Setting"),
        ("AH_TRAP_MIB", "ahPoEEth1On"),
        ("AH_TRAP_MIB", "ahPoEEth1Pwr"),
        ("AH_TRAP_MIB", "ahPoEEth1MaxSpeed"),
        ("AH_TRAP_MIB", "ahPoEWifi1Setting"),
        ("AH_TRAP_MIB", "ahPoEWifi2Setting"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahPoEEvent.setStatus(
        "current"
    )

ahChannelPowerChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 8)
)
ahChannelPowerChangeEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahRadioChannel"),
        ("AH_TRAP_MIB", "ahRadioTxPower"),
        ("AH_TRAP_MIB", "ahBeaconInterval"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahChannelPowerChangeEvent.setStatus(
        "current"
    )

ahIDPMitigateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 9)
)
ahIDPMitigateEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahRemoteId"),
        ("AH_TRAP_MIB", "ahBSSID"),
        ("AH_TRAP_MIB", "ahDiscoverAge"),
        ("AH_TRAP_MIB", "ahUpdateAge"),
        ("AH_TRAP_MIB", "ahRemoved"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahIDPMitigateEvent.setStatus(
        "current"
    )

ahInterferenceMapAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 10)
)
ahInterferenceMapAlertEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahInterferenceThreshold"),
        ("AH_TRAP_MIB", "ahRunningAverageInterference"),
        ("AH_TRAP_MIB", "ahShortTermInterference"),
        ("AH_TRAP_MIB", "ahSnapshotInterference"),
        ("AH_TRAP_MIB", "ahCRCErrRateThreshold"),
        ("AH_TRAP_MIB", "ahCRCErrRate"),
        ("AH_TRAP_MIB", "ahSeverity"),
        ("AH_TRAP_MIB", "ahFailureSet"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahInterferenceMapAlertEvent.setStatus(
        "current"
    )

ahBandwidthSentinelEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 11)
)
ahBandwidthSentinelEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahClientMAC"),
        ("AH_TRAP_MIB", "ahBandwidthSentinelStatus"),
        ("AH_TRAP_MIB", "ahGuaranteedBandwidth"),
        ("AH_TRAP_MIB", "ahActualBandwidth"),
        ("AH_TRAP_MIB", "ahBandwidthSentinelAction"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahBandwidthSentinelEvent.setStatus(
        "current"
    )

ahAlarmMsgMapAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1, 1, 12)
)
ahAlarmMsgMapAlertEvent.setObjects(
      *(("AH_TRAP_MIB", "ahAPId"),
        ("AH_TRAP_MIB", "ahAPName"),
        ("AH_TRAP_MIB", "ahIfIndex"),
        ("AH_TRAP_MIB", "ahObjectName"),
        ("AH_TRAP_MIB", "ahLevel"),
        ("AH_TRAP_MIB", "ahClientMAC"),
        ("AH_TRAP_MIB", "ahSSID"),
        ("AH_TRAP_MIB", "ahAlarmAlertType"),
        ("AH_TRAP_MIB", "ahThresholdValue"),
        ("AH_TRAP_MIB", "ahShortTermValue"),
        ("AH_TRAP_MIB", "ahSnapshotValue"),
        ("AH_TRAP_MIB", "ahFailureSet"),
        ("AH_TRAP_MIB", "ahCode"),
        ("AH_TRAP_MIB", "ahTrapDesc"))
)
if mibBuilder.loadTexts:
    ahAlarmMsgMapAlertEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AH_TRAP_MIB",
    **{"AhAuthenticationMethod": AhAuthenticationMethod,
       "AhEncrytionMethod": AhEncrytionMethod,
       "AhState": AhState,
       "AhProbableCause": AhProbableCause,
       "ahTrapModule": ahTrapModule,
       "ahFailureTrap": ahFailureTrap,
       "ahThresholdCrossingEvent": ahThresholdCrossingEvent,
       "ahStateChangeEvent": ahStateChangeEvent,
       "ahConnectionChangeEvent": ahConnectionChangeEvent,
       "ahIDPStationEvent": ahIDPStationEvent,
       "ahClientInfoEvent": ahClientInfoEvent,
       "ahPoEEvent": ahPoEEvent,
       "ahChannelPowerChangeEvent": ahChannelPowerChangeEvent,
       "ahIDPMitigateEvent": ahIDPMitigateEvent,
       "ahInterferenceMapAlertEvent": ahInterferenceMapAlertEvent,
       "ahBandwidthSentinelEvent": ahBandwidthSentinelEvent,
       "ahAlarmMsgMapAlertEvent": ahAlarmMsgMapAlertEvent,
       "ahNotificationVarBind": ahNotificationVarBind,
       "ahAPId": ahAPId,
       "ahAPName": ahAPName,
       "ahSeverity": ahSeverity,
       "ahObjectName": ahObjectName,
       "ahProbableCause": ahProbableCause,
       "ahCurValue": ahCurValue,
       "ahThresholdHigh": ahThresholdHigh,
       "ahThresholdLow": ahThresholdLow,
       "ahPreviousState": ahPreviousState,
       "ahCurrentState": ahCurrentState,
       "ahTrapDesc": ahTrapDesc,
       "ahCode": ahCode,
       "ahIfIndex": ahIfIndex,
       "ahObjectType": ahObjectType,
       "ahRemoteId": ahRemoteId,
       "ahIDPType": ahIDPType,
       "ahIDPChannel": ahIDPChannel,
       "ahIDPRSSI": ahIDPRSSI,
       "ahIDPCompliance": ahIDPCompliance,
       "ahSSID": ahSSID,
       "ahStationType": ahStationType,
       "ahIDPStationData": ahIDPStationData,
       "ahRemoved": ahRemoved,
       "ahClientMAC": ahClientMAC,
       "ahCLientIP": ahCLientIP,
       "ahClientHostName": ahClientHostName,
       "ahClientUserName": ahClientUserName,
       "ahPowerSrc": ahPowerSrc,
       "ahPoEEth0On": ahPoEEth0On,
       "ahPoEEth0Pwr": ahPoEEth0Pwr,
       "ahPoEEth1On": ahPoEEth1On,
       "ahPoEEth1Pwr": ahPoEEth1Pwr,
       "ahRadioChannel": ahRadioChannel,
       "ahRadioTxPower": ahRadioTxPower,
       "ahClientAuthMethod": ahClientAuthMethod,
       "ahClientEncryptionMethod": ahClientEncryptionMethod,
       "ahClientMACProtocol": ahClientMACProtocol,
       "ahClientVLAN": ahClientVLAN,
       "ahClientUserProfId": ahClientUserProfId,
       "ahClientChannel": ahClientChannel,
       "ahClientCWPUsed": ahClientCWPUsed,
       "ahBSSID": ahBSSID,
       "ahPoEEth0MaxSpeed": ahPoEEth0MaxSpeed,
       "ahPoEEth1MaxSpeed": ahPoEEth1MaxSpeed,
       "ahPoEWifi0Setting": ahPoEWifi0Setting,
       "ahPoEWifi1Setting": ahPoEWifi1Setting,
       "ahPoEWifi2Setting": ahPoEWifi2Setting,
       "ahAssociationTime": ahAssociationTime,
       "ahIDPInNet": ahIDPInNet,
       "ahDiscoverAge": ahDiscoverAge,
       "ahUpdateAge": ahUpdateAge,
       "ahRunningAverageInterference": ahRunningAverageInterference,
       "ahShortTermInterference": ahShortTermInterference,
       "ahSnapshotInterference": ahSnapshotInterference,
       "ahFailureSet": ahFailureSet,
       "ahInterferenceThreshold": ahInterferenceThreshold,
       "ahCRCErrRateThreshold": ahCRCErrRateThreshold,
       "ahCRCErrRate": ahCRCErrRate,
       "ahBandwidthSentinelStatus": ahBandwidthSentinelStatus,
       "ahGuaranteedBandwidth": ahGuaranteedBandwidth,
       "ahActualBandwidth": ahActualBandwidth,
       "ahBandwidthSentinelAction": ahBandwidthSentinelAction,
       "ahBeaconInterval": ahBeaconInterval,
       "ahLevel": ahLevel,
       "ahAlarmAlertType": ahAlarmAlertType,
       "ahThresholdValue": ahThresholdValue,
       "ahShortTermValue": ahShortTermValue,
       "ahSnapshotValue": ahSnapshotValue,
       "ahIfName": ahIfName}
)
