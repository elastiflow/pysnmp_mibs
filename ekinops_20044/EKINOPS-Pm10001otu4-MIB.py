# SNMP MIB module (EKINOPS-Pm10001otu4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm10001otu4-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:47 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

modulePm10001otu4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82)
)
if mibBuilder.loadTexts:
    modulePm10001otu4.setRevisions(
        ("2016-11-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm10001otu4MultiRate(TextualConvention, Integer32):
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
        *(("rate100Mhz", 0),
          ("rate250Mhz", 1),
          ("rate500Mhz", 2),
          ("rate1Ghz", 3))
    )



class Pm10001otu4OtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Pm10001otu4OtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Pm10001otu4AdjustValue(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Pm10001otu4ClientProtocol(TextualConvention, Integer32):
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
        *(("protocolclientvalue0", 0),
          ("protocolclientvalue1", 1),
          ("protocolclientvalue2", 2),
          ("protocolclientvalue3", 3),
          ("protocolclientvalue4", 4),
          ("protocolclientvalue5", 5),
          ("protocolclientvalue6", 6),
          ("protocolclientvalue7", 7),
          ("protocolclientvalue8", 8))
    )



class Pm10001otu4ProtocolMode(TextualConvention, Integer32):
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
        *(("protocolmodevalue0", 0),
          ("protocolmodevalue1", 1),
          ("protocolmodevalue2", 2),
          ("protocolmodevalue3", 3))
    )



class Pm10001otu4OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm10001otu4OrxChannel(TextualConvention, Integer32):
    status = "current"


class Rm10010ClientIgnoreTimer(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ignoretimerclientvalue0", 0),
          ("ignoretimerclientvalue1", 1),
          ("ignoretimerclientvalue2", 2),
          ("ignoretimerclientvalue3", 3),
          ("ignoretimerclientvalue4", 4),
          ("ignoretimerclientvalue5", 5),
          ("ignoretimerclientvalue6", 6),
          ("ignoretimerclientvalue7", 7),
          ("ignoretimerclientvalue8", 8),
          ("ignoretimerclientvalue9", 9),
          ("ignoretimerclientvalue10", 10))
    )



class Pm10001otu4CompensationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compensationautomode", 0),
          ("compensationmanmode", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Pm10001otu4alarms_ObjectIdentity = ObjectIdentity
pm10001otu4alarms = _Pm10001otu4alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2)
)
_Pm10001otu4AlmOther_ObjectIdentity = ObjectIdentity
pm10001otu4AlmOther = _Pm10001otu4AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1)
)
_Pm10001otu4AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm10001otu4AlmOtherNurg = _Pm10001otu4AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1)
)
_Pm10001otu4AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm10001otu4AlmsynthAlm2 = _Pm10001otu4AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1, 2)
)
_Pm10001otu4AlmConfTableSave_Type = EkiOnOff
_Pm10001otu4AlmConfTableSave_Object = MibScalar
pm10001otu4AlmConfTableSave = _Pm10001otu4AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1, 2, 1),
    _Pm10001otu4AlmConfTableSave_Type()
)
pm10001otu4AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmConfTableSave.setStatus("current")
_Pm10001otu4AlmInvUpload_Type = EkiOnOff
_Pm10001otu4AlmInvUpload_Object = MibScalar
pm10001otu4AlmInvUpload = _Pm10001otu4AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1, 2, 2),
    _Pm10001otu4AlmInvUpload_Type()
)
pm10001otu4AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmInvUpload.setStatus("current")
_Pm10001otu4AlmConfTableLoad_Type = EkiOnOff
_Pm10001otu4AlmConfTableLoad_Object = MibScalar
pm10001otu4AlmConfTableLoad = _Pm10001otu4AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1, 2, 3),
    _Pm10001otu4AlmConfTableLoad_Type()
)
pm10001otu4AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmConfTableLoad.setStatus("current")
_Pm10001otu4AlmCorrelatOff_Type = EkiOnOff
_Pm10001otu4AlmCorrelatOff_Object = MibScalar
pm10001otu4AlmCorrelatOff = _Pm10001otu4AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1, 2, 4),
    _Pm10001otu4AlmCorrelatOff_Type()
)
pm10001otu4AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCorrelatOff.setStatus("current")
_Pm10001otu4AlmMaintenanceOn_Type = EkiOnOff
_Pm10001otu4AlmMaintenanceOn_Object = MibScalar
pm10001otu4AlmMaintenanceOn = _Pm10001otu4AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 1, 2, 5),
    _Pm10001otu4AlmMaintenanceOn_Type()
)
pm10001otu4AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMaintenanceOn.setStatus("current")
_Pm10001otu4AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm10001otu4AlmOtherUrg = _Pm10001otu4AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 2)
)
_Pm10001otu4AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm10001otu4AlmOtherCrit = _Pm10001otu4AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3)
)
_Pm10001otu4AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm10001otu4AlmsynthAlm0 = _Pm10001otu4AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 0)
)
_Pm10001otu4AlmFailFan_Type = EkiOnOff
_Pm10001otu4AlmFailFan_Object = MibScalar
pm10001otu4AlmFailFan = _Pm10001otu4AlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 0, 2),
    _Pm10001otu4AlmFailFan_Type()
)
pm10001otu4AlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmFailFan.setStatus("current")
_Pm10001otu4AlmModGlobFail_Type = EkiOnOff
_Pm10001otu4AlmModGlobFail_Object = MibScalar
pm10001otu4AlmModGlobFail = _Pm10001otu4AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 0, 9),
    _Pm10001otu4AlmModGlobFail_Type()
)
pm10001otu4AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmModGlobFail.setStatus("current")
_Pm10001otu4AlmDefFuseA_Type = EkiOnOff
_Pm10001otu4AlmDefFuseA_Object = MibScalar
pm10001otu4AlmDefFuseA = _Pm10001otu4AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 0, 15),
    _Pm10001otu4AlmDefFuseA_Type()
)
pm10001otu4AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmDefFuseA.setStatus("current")
_Pm10001otu4AlmDefFuseB_Type = EkiOnOff
_Pm10001otu4AlmDefFuseB_Object = MibScalar
pm10001otu4AlmDefFuseB = _Pm10001otu4AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 0, 16),
    _Pm10001otu4AlmDefFuseB_Type()
)
pm10001otu4AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmDefFuseB.setStatus("current")
_Pm10001otu4AlmclientModuleState_ObjectIdentity = ObjectIdentity
pm10001otu4AlmclientModuleState = _Pm10001otu4AlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40)
)
_Pm10001otu4AlmCfpInitialize_Type = EkiOnOff
_Pm10001otu4AlmCfpInitialize_Object = MibScalar
pm10001otu4AlmCfpInitialize = _Pm10001otu4AlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 1),
    _Pm10001otu4AlmCfpInitialize_Type()
)
pm10001otu4AlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpInitialize.setStatus("current")
_Pm10001otu4AlmCfpLowPower_Type = EkiOnOff
_Pm10001otu4AlmCfpLowPower_Object = MibScalar
pm10001otu4AlmCfpLowPower = _Pm10001otu4AlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 2),
    _Pm10001otu4AlmCfpLowPower_Type()
)
pm10001otu4AlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpLowPower.setStatus("current")
_Pm10001otu4AlmCfpHighPowerUp_Type = EkiOnOff
_Pm10001otu4AlmCfpHighPowerUp_Object = MibScalar
pm10001otu4AlmCfpHighPowerUp = _Pm10001otu4AlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 3),
    _Pm10001otu4AlmCfpHighPowerUp_Type()
)
pm10001otu4AlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpHighPowerUp.setStatus("current")
_Pm10001otu4AlmCfpTxOff_Type = EkiOnOff
_Pm10001otu4AlmCfpTxOff_Object = MibScalar
pm10001otu4AlmCfpTxOff = _Pm10001otu4AlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 4),
    _Pm10001otu4AlmCfpTxOff_Type()
)
pm10001otu4AlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxOff.setStatus("current")
_Pm10001otu4AlmCfpTxTurnOn_Type = EkiOnOff
_Pm10001otu4AlmCfpTxTurnOn_Object = MibScalar
pm10001otu4AlmCfpTxTurnOn = _Pm10001otu4AlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 5),
    _Pm10001otu4AlmCfpTxTurnOn_Type()
)
pm10001otu4AlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxTurnOn.setStatus("current")
_Pm10001otu4AlmCfpReady_Type = EkiOnOff
_Pm10001otu4AlmCfpReady_Object = MibScalar
pm10001otu4AlmCfpReady = _Pm10001otu4AlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 6),
    _Pm10001otu4AlmCfpReady_Type()
)
pm10001otu4AlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpReady.setStatus("current")
_Pm10001otu4AlmCfpFault_Type = EkiOnOff
_Pm10001otu4AlmCfpFault_Object = MibScalar
pm10001otu4AlmCfpFault = _Pm10001otu4AlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 7),
    _Pm10001otu4AlmCfpFault_Type()
)
pm10001otu4AlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpFault.setStatus("current")
_Pm10001otu4AlmCfpTxTurnOff_Type = EkiOnOff
_Pm10001otu4AlmCfpTxTurnOff_Object = MibScalar
pm10001otu4AlmCfpTxTurnOff = _Pm10001otu4AlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 8),
    _Pm10001otu4AlmCfpTxTurnOff_Type()
)
pm10001otu4AlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxTurnOff.setStatus("current")
_Pm10001otu4AlmCfpHighPowerDown_Type = EkiOnOff
_Pm10001otu4AlmCfpHighPowerDown_Object = MibScalar
pm10001otu4AlmCfpHighPowerDown = _Pm10001otu4AlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 40, 9),
    _Pm10001otu4AlmCfpHighPowerDown_Type()
)
pm10001otu4AlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpHighPowerDown.setStatus("current")
_Pm10001otu4AlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10001otu4AlmclientModuleGeneralStatus = _Pm10001otu4AlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41)
)
_Pm10001otu4AlmCfpOutOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmCfpOutOfAlignment_Object = MibScalar
pm10001otu4AlmCfpOutOfAlignment = _Pm10001otu4AlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 4),
    _Pm10001otu4AlmCfpOutOfAlignment_Type()
)
pm10001otu4AlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpOutOfAlignment.setStatus("current")
_Pm10001otu4AlmCfpRxNetworkLol_Type = EkiOnOff
_Pm10001otu4AlmCfpRxNetworkLol_Object = MibScalar
pm10001otu4AlmCfpRxNetworkLol = _Pm10001otu4AlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 5),
    _Pm10001otu4AlmCfpRxNetworkLol_Type()
)
pm10001otu4AlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpRxNetworkLol.setStatus("current")
_Pm10001otu4AlmCfpRxLos_Type = EkiOnOff
_Pm10001otu4AlmCfpRxLos_Object = MibScalar
pm10001otu4AlmCfpRxLos = _Pm10001otu4AlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 6),
    _Pm10001otu4AlmCfpRxLos_Type()
)
pm10001otu4AlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpRxLos.setStatus("current")
_Pm10001otu4AlmCfpTxHostLol_Type = EkiOnOff
_Pm10001otu4AlmCfpTxHostLol_Object = MibScalar
pm10001otu4AlmCfpTxHostLol = _Pm10001otu4AlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 7),
    _Pm10001otu4AlmCfpTxHostLol_Type()
)
pm10001otu4AlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxHostLol.setStatus("current")
_Pm10001otu4AlmCfpTxLosf_Type = EkiOnOff
_Pm10001otu4AlmCfpTxLosf_Object = MibScalar
pm10001otu4AlmCfpTxLosf = _Pm10001otu4AlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 8),
    _Pm10001otu4AlmCfpTxLosf_Type()
)
pm10001otu4AlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxLosf.setStatus("current")
_Pm10001otu4AlmCfpTxCmuLol_Type = EkiOnOff
_Pm10001otu4AlmCfpTxCmuLol_Object = MibScalar
pm10001otu4AlmCfpTxCmuLol = _Pm10001otu4AlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 9),
    _Pm10001otu4AlmCfpTxCmuLol_Type()
)
pm10001otu4AlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxCmuLol.setStatus("current")
_Pm10001otu4AlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm10001otu4AlmCfpTxJitterPllLol_Object = MibScalar
pm10001otu4AlmCfpTxJitterPllLol = _Pm10001otu4AlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 10),
    _Pm10001otu4AlmCfpTxJitterPllLol_Type()
)
pm10001otu4AlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpTxJitterPllLol.setStatus("current")
_Pm10001otu4AlmCfpLossOfRefclk_Type = EkiOnOff
_Pm10001otu4AlmCfpLossOfRefclk_Object = MibScalar
pm10001otu4AlmCfpLossOfRefclk = _Pm10001otu4AlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 11),
    _Pm10001otu4AlmCfpLossOfRefclk_Type()
)
pm10001otu4AlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpLossOfRefclk.setStatus("current")
_Pm10001otu4AlmCfpHwInterlock_Type = EkiOnOff
_Pm10001otu4AlmCfpHwInterlock_Object = MibScalar
pm10001otu4AlmCfpHwInterlock = _Pm10001otu4AlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 41, 14),
    _Pm10001otu4AlmCfpHwInterlock_Type()
)
pm10001otu4AlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpHwInterlock.setStatus("current")
_Pm10001otu4AlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10001otu4AlmclientGlobalAlarmSummary = _Pm10001otu4AlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42)
)
_Pm10001otu4AlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm10001otu4AlmCfpSoftGlobAlarmTest_Object = MibScalar
pm10001otu4AlmCfpSoftGlobAlarmTest = _Pm10001otu4AlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 1),
    _Pm10001otu4AlmCfpSoftGlobAlarmTest_Type()
)
pm10001otu4AlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm10001otu4AlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10001otu4AlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm10001otu4AlmCfpNetworkLaneAlarmWarning2 = _Pm10001otu4AlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 7),
    _Pm10001otu4AlmCfpNetworkLaneAlarmWarning2_Type()
)
pm10001otu4AlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm10001otu4AlmCfpModuleState_Type = EkiOnOff
_Pm10001otu4AlmCfpModuleState_Object = MibScalar
pm10001otu4AlmCfpModuleState = _Pm10001otu4AlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 8),
    _Pm10001otu4AlmCfpModuleState_Type()
)
pm10001otu4AlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpModuleState.setStatus("current")
_Pm10001otu4AlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm10001otu4AlmCfpModuleGeneralStatus_Object = MibScalar
pm10001otu4AlmCfpModuleGeneralStatus = _Pm10001otu4AlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 9),
    _Pm10001otu4AlmCfpModuleGeneralStatus_Type()
)
pm10001otu4AlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpModuleGeneralStatus.setStatus("current")
_Pm10001otu4AlmCfpModuleFault_Type = EkiOnOff
_Pm10001otu4AlmCfpModuleFault_Object = MibScalar
pm10001otu4AlmCfpModuleFault = _Pm10001otu4AlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 10),
    _Pm10001otu4AlmCfpModuleFault_Type()
)
pm10001otu4AlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpModuleFault.setStatus("current")
_Pm10001otu4AlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm10001otu4AlmCfpModuleAlarmWarning1_Object = MibScalar
pm10001otu4AlmCfpModuleAlarmWarning1 = _Pm10001otu4AlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 11),
    _Pm10001otu4AlmCfpModuleAlarmWarning1_Type()
)
pm10001otu4AlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpModuleAlarmWarning1.setStatus("current")
_Pm10001otu4AlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm10001otu4AlmCfpModuleAlarmWarning2_Object = MibScalar
pm10001otu4AlmCfpModuleAlarmWarning2 = _Pm10001otu4AlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 12),
    _Pm10001otu4AlmCfpModuleAlarmWarning2_Type()
)
pm10001otu4AlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpModuleAlarmWarning2.setStatus("current")
_Pm10001otu4AlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10001otu4AlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm10001otu4AlmCfpNetworkLaneAlarmWarning1 = _Pm10001otu4AlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 13),
    _Pm10001otu4AlmCfpNetworkLaneAlarmWarning1_Type()
)
pm10001otu4AlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm10001otu4AlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10001otu4AlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm10001otu4AlmCfpNetworkLaneFaultStatus = _Pm10001otu4AlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 14),
    _Pm10001otu4AlmCfpNetworkLaneFaultStatus_Type()
)
pm10001otu4AlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm10001otu4AlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm10001otu4AlmCfpHostLaneFaultStatus_Object = MibScalar
pm10001otu4AlmCfpHostLaneFaultStatus = _Pm10001otu4AlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 15),
    _Pm10001otu4AlmCfpHostLaneFaultStatus_Type()
)
pm10001otu4AlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpHostLaneFaultStatus.setStatus("current")
_Pm10001otu4AlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm10001otu4AlmCfpGlobAlarmAssertion_Object = MibScalar
pm10001otu4AlmCfpGlobAlarmAssertion = _Pm10001otu4AlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 42, 16),
    _Pm10001otu4AlmCfpGlobAlarmAssertion_Type()
)
pm10001otu4AlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmCfpGlobAlarmAssertion.setStatus("current")
_Pm10001otu4AlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaModuleState = _Pm10001otu4AlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46)
)
_Pm10001otu4AlmMsaInitialize_Type = EkiOnOff
_Pm10001otu4AlmMsaInitialize_Object = MibScalar
pm10001otu4AlmMsaInitialize = _Pm10001otu4AlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 1),
    _Pm10001otu4AlmMsaInitialize_Type()
)
pm10001otu4AlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaInitialize.setStatus("current")
_Pm10001otu4AlmMsaLowPower_Type = EkiOnOff
_Pm10001otu4AlmMsaLowPower_Object = MibScalar
pm10001otu4AlmMsaLowPower = _Pm10001otu4AlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 2),
    _Pm10001otu4AlmMsaLowPower_Type()
)
pm10001otu4AlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaLowPower.setStatus("current")
_Pm10001otu4AlmMsaHighPowerUp_Type = EkiOnOff
_Pm10001otu4AlmMsaHighPowerUp_Object = MibScalar
pm10001otu4AlmMsaHighPowerUp = _Pm10001otu4AlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 3),
    _Pm10001otu4AlmMsaHighPowerUp_Type()
)
pm10001otu4AlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaHighPowerUp.setStatus("current")
_Pm10001otu4AlmMsaTxOff_Type = EkiOnOff
_Pm10001otu4AlmMsaTxOff_Object = MibScalar
pm10001otu4AlmMsaTxOff = _Pm10001otu4AlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 4),
    _Pm10001otu4AlmMsaTxOff_Type()
)
pm10001otu4AlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxOff.setStatus("current")
_Pm10001otu4AlmMsaTxTurnOn_Type = EkiOnOff
_Pm10001otu4AlmMsaTxTurnOn_Object = MibScalar
pm10001otu4AlmMsaTxTurnOn = _Pm10001otu4AlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 5),
    _Pm10001otu4AlmMsaTxTurnOn_Type()
)
pm10001otu4AlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxTurnOn.setStatus("current")
_Pm10001otu4AlmMsaReady_Type = EkiOnOff
_Pm10001otu4AlmMsaReady_Object = MibScalar
pm10001otu4AlmMsaReady = _Pm10001otu4AlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 6),
    _Pm10001otu4AlmMsaReady_Type()
)
pm10001otu4AlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaReady.setStatus("current")
_Pm10001otu4AlmMsaFault_Type = EkiOnOff
_Pm10001otu4AlmMsaFault_Object = MibScalar
pm10001otu4AlmMsaFault = _Pm10001otu4AlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 7),
    _Pm10001otu4AlmMsaFault_Type()
)
pm10001otu4AlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaFault.setStatus("current")
_Pm10001otu4AlmMsaTxTurnOff_Type = EkiOnOff
_Pm10001otu4AlmMsaTxTurnOff_Object = MibScalar
pm10001otu4AlmMsaTxTurnOff = _Pm10001otu4AlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 8),
    _Pm10001otu4AlmMsaTxTurnOff_Type()
)
pm10001otu4AlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxTurnOff.setStatus("current")
_Pm10001otu4AlmMsaHighPowerDown_Type = EkiOnOff
_Pm10001otu4AlmMsaHighPowerDown_Object = MibScalar
pm10001otu4AlmMsaHighPowerDown = _Pm10001otu4AlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 46, 9),
    _Pm10001otu4AlmMsaHighPowerDown_Type()
)
pm10001otu4AlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaHighPowerDown.setStatus("current")
_Pm10001otu4AlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaModuleGeneralStatus = _Pm10001otu4AlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47)
)
_Pm10001otu4AlmMsaOutOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmMsaOutOfAlignment_Object = MibScalar
pm10001otu4AlmMsaOutOfAlignment = _Pm10001otu4AlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 4),
    _Pm10001otu4AlmMsaOutOfAlignment_Type()
)
pm10001otu4AlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaOutOfAlignment.setStatus("current")
_Pm10001otu4AlmMsaRxNetworkLol_Type = EkiOnOff
_Pm10001otu4AlmMsaRxNetworkLol_Object = MibScalar
pm10001otu4AlmMsaRxNetworkLol = _Pm10001otu4AlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 5),
    _Pm10001otu4AlmMsaRxNetworkLol_Type()
)
pm10001otu4AlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaRxNetworkLol.setStatus("current")
_Pm10001otu4AlmMsaRxLos_Type = EkiOnOff
_Pm10001otu4AlmMsaRxLos_Object = MibScalar
pm10001otu4AlmMsaRxLos = _Pm10001otu4AlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 6),
    _Pm10001otu4AlmMsaRxLos_Type()
)
pm10001otu4AlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaRxLos.setStatus("current")
_Pm10001otu4AlmMsaTxHostLol_Type = EkiOnOff
_Pm10001otu4AlmMsaTxHostLol_Object = MibScalar
pm10001otu4AlmMsaTxHostLol = _Pm10001otu4AlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 7),
    _Pm10001otu4AlmMsaTxHostLol_Type()
)
pm10001otu4AlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxHostLol.setStatus("current")
_Pm10001otu4AlmMsaTxLosf_Type = EkiOnOff
_Pm10001otu4AlmMsaTxLosf_Object = MibScalar
pm10001otu4AlmMsaTxLosf = _Pm10001otu4AlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 8),
    _Pm10001otu4AlmMsaTxLosf_Type()
)
pm10001otu4AlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxLosf.setStatus("current")
_Pm10001otu4AlmMsaTxCmuLol_Type = EkiOnOff
_Pm10001otu4AlmMsaTxCmuLol_Object = MibScalar
pm10001otu4AlmMsaTxCmuLol = _Pm10001otu4AlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 9),
    _Pm10001otu4AlmMsaTxCmuLol_Type()
)
pm10001otu4AlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxCmuLol.setStatus("current")
_Pm10001otu4AlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm10001otu4AlmMsaTxJitterPllLol_Object = MibScalar
pm10001otu4AlmMsaTxJitterPllLol = _Pm10001otu4AlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 10),
    _Pm10001otu4AlmMsaTxJitterPllLol_Type()
)
pm10001otu4AlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaTxJitterPllLol.setStatus("current")
_Pm10001otu4AlmMsaLossOfRefclk_Type = EkiOnOff
_Pm10001otu4AlmMsaLossOfRefclk_Object = MibScalar
pm10001otu4AlmMsaLossOfRefclk = _Pm10001otu4AlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 11),
    _Pm10001otu4AlmMsaLossOfRefclk_Type()
)
pm10001otu4AlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaLossOfRefclk.setStatus("current")
_Pm10001otu4AlmMsaHwInterlock_Type = EkiOnOff
_Pm10001otu4AlmMsaHwInterlock_Object = MibScalar
pm10001otu4AlmMsaHwInterlock = _Pm10001otu4AlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 47, 14),
    _Pm10001otu4AlmMsaHwInterlock_Type()
)
pm10001otu4AlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaHwInterlock.setStatus("current")
_Pm10001otu4AlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaGlobalAlarmSummary = _Pm10001otu4AlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48)
)
_Pm10001otu4AlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm10001otu4AlmMsaSoftGlobAlarmTest_Object = MibScalar
pm10001otu4AlmMsaSoftGlobAlarmTest = _Pm10001otu4AlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 1),
    _Pm10001otu4AlmMsaSoftGlobAlarmTest_Type()
)
pm10001otu4AlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm10001otu4AlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm10001otu4AlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm10001otu4AlmMsaNetworkHostAlarmStatus = _Pm10001otu4AlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 6),
    _Pm10001otu4AlmMsaNetworkHostAlarmStatus_Type()
)
pm10001otu4AlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm10001otu4AlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10001otu4AlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm10001otu4AlmMsaNetworkLaneAlarmWarning2 = _Pm10001otu4AlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 7),
    _Pm10001otu4AlmMsaNetworkLaneAlarmWarning2_Type()
)
pm10001otu4AlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm10001otu4AlmMsaModuleState_Type = EkiOnOff
_Pm10001otu4AlmMsaModuleState_Object = MibScalar
pm10001otu4AlmMsaModuleState = _Pm10001otu4AlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 8),
    _Pm10001otu4AlmMsaModuleState_Type()
)
pm10001otu4AlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaModuleState.setStatus("current")
_Pm10001otu4AlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm10001otu4AlmMsaModuleGeneralStatus_Object = MibScalar
pm10001otu4AlmMsaModuleGeneralStatus = _Pm10001otu4AlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 9),
    _Pm10001otu4AlmMsaModuleGeneralStatus_Type()
)
pm10001otu4AlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaModuleGeneralStatus.setStatus("current")
_Pm10001otu4AlmModuleFault_Type = EkiOnOff
_Pm10001otu4AlmModuleFault_Object = MibScalar
pm10001otu4AlmModuleFault = _Pm10001otu4AlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 10),
    _Pm10001otu4AlmModuleFault_Type()
)
pm10001otu4AlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmModuleFault.setStatus("current")
_Pm10001otu4AlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm10001otu4AlmMsaModuleAlarmWarning1_Object = MibScalar
pm10001otu4AlmMsaModuleAlarmWarning1 = _Pm10001otu4AlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 11),
    _Pm10001otu4AlmMsaModuleAlarmWarning1_Type()
)
pm10001otu4AlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaModuleAlarmWarning1.setStatus("current")
_Pm10001otu4AlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm10001otu4AlmMsaModuleAlarmWarning2_Object = MibScalar
pm10001otu4AlmMsaModuleAlarmWarning2 = _Pm10001otu4AlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 12),
    _Pm10001otu4AlmMsaModuleAlarmWarning2_Type()
)
pm10001otu4AlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaModuleAlarmWarning2.setStatus("current")
_Pm10001otu4AlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10001otu4AlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm10001otu4AlmMsaNetworkLaneAlarmWarning1 = _Pm10001otu4AlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 13),
    _Pm10001otu4AlmMsaNetworkLaneAlarmWarning1_Type()
)
pm10001otu4AlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm10001otu4AlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10001otu4AlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm10001otu4AlmMsaNetworkLaneFaultStatus = _Pm10001otu4AlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 14),
    _Pm10001otu4AlmMsaNetworkLaneFaultStatus_Type()
)
pm10001otu4AlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm10001otu4AlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm10001otu4AlmMsaHostLaneFaultStatus_Object = MibScalar
pm10001otu4AlmMsaHostLaneFaultStatus = _Pm10001otu4AlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 15),
    _Pm10001otu4AlmMsaHostLaneFaultStatus_Type()
)
pm10001otu4AlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaHostLaneFaultStatus.setStatus("current")
_Pm10001otu4AlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm10001otu4AlmMsaGlobAlarmAssertion_Object = MibScalar
pm10001otu4AlmMsaGlobAlarmAssertion = _Pm10001otu4AlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 48, 16),
    _Pm10001otu4AlmMsaGlobAlarmAssertion_Type()
)
pm10001otu4AlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmMsaGlobAlarmAssertion.setStatus("current")
_Pm10001otu4AlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaNetworkTxAlignment = _Pm10001otu4AlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 49)
)
_Pm10001otu4AlmNetTxTimingFault_Type = EkiOnOff
_Pm10001otu4AlmNetTxTimingFault_Object = MibScalar
pm10001otu4AlmNetTxTimingFault = _Pm10001otu4AlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 49, 12),
    _Pm10001otu4AlmNetTxTimingFault_Type()
)
pm10001otu4AlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetTxTimingFault.setStatus("current")
_Pm10001otu4AlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm10001otu4AlmNetTxReferenceClockFault_Object = MibScalar
pm10001otu4AlmNetTxReferenceClockFault = _Pm10001otu4AlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 49, 13),
    _Pm10001otu4AlmNetTxReferenceClockFault_Type()
)
pm10001otu4AlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetTxReferenceClockFault.setStatus("current")
_Pm10001otu4AlmNetTxCmuLockFault_Type = EkiOnOff
_Pm10001otu4AlmNetTxCmuLockFault_Object = MibScalar
pm10001otu4AlmNetTxCmuLockFault = _Pm10001otu4AlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 49, 14),
    _Pm10001otu4AlmNetTxCmuLockFault_Type()
)
pm10001otu4AlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetTxCmuLockFault.setStatus("current")
_Pm10001otu4AlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmNetTxOutOfAlignment_Object = MibScalar
pm10001otu4AlmNetTxOutOfAlignment = _Pm10001otu4AlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 49, 15),
    _Pm10001otu4AlmNetTxOutOfAlignment_Type()
)
pm10001otu4AlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetTxOutOfAlignment.setStatus("current")
_Pm10001otu4AlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmNetTxLossOfAlignment_Object = MibScalar
pm10001otu4AlmNetTxLossOfAlignment = _Pm10001otu4AlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 49, 16),
    _Pm10001otu4AlmNetTxLossOfAlignment_Type()
)
pm10001otu4AlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetTxLossOfAlignment.setStatus("current")
_Pm10001otu4AlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaNetworkRxAlignment = _Pm10001otu4AlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 50)
)
_Pm10001otu4AlmNetRxTimingFault_Type = EkiOnOff
_Pm10001otu4AlmNetRxTimingFault_Object = MibScalar
pm10001otu4AlmNetRxTimingFault = _Pm10001otu4AlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 50, 12),
    _Pm10001otu4AlmNetRxTimingFault_Type()
)
pm10001otu4AlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetRxTimingFault.setStatus("current")
_Pm10001otu4AlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmNetRxOutOfAlignment_Object = MibScalar
pm10001otu4AlmNetRxOutOfAlignment = _Pm10001otu4AlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 50, 13),
    _Pm10001otu4AlmNetRxOutOfAlignment_Type()
)
pm10001otu4AlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetRxOutOfAlignment.setStatus("current")
_Pm10001otu4AlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmNetRxLossOfAlignment_Object = MibScalar
pm10001otu4AlmNetRxLossOfAlignment = _Pm10001otu4AlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 50, 14),
    _Pm10001otu4AlmNetRxLossOfAlignment_Type()
)
pm10001otu4AlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetRxLossOfAlignment.setStatus("current")
_Pm10001otu4AlmNetRxModemLockFault_Type = EkiOnOff
_Pm10001otu4AlmNetRxModemLockFault_Object = MibScalar
pm10001otu4AlmNetRxModemLockFault = _Pm10001otu4AlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 50, 15),
    _Pm10001otu4AlmNetRxModemLockFault_Type()
)
pm10001otu4AlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetRxModemLockFault.setStatus("current")
_Pm10001otu4AlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm10001otu4AlmNetRxModemSyncDetectFault_Object = MibScalar
pm10001otu4AlmNetRxModemSyncDetectFault = _Pm10001otu4AlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 50, 16),
    _Pm10001otu4AlmNetRxModemSyncDetectFault_Type()
)
pm10001otu4AlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetRxModemSyncDetectFault.setStatus("current")
_Pm10001otu4AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaNetworkHostNetworkAlarmSummary = _Pm10001otu4AlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51)
)
_Pm10001otu4AlmNetworkTxAlignment_Type = EkiOnOff
_Pm10001otu4AlmNetworkTxAlignment_Object = MibScalar
pm10001otu4AlmNetworkTxAlignment = _Pm10001otu4AlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51, 11),
    _Pm10001otu4AlmNetworkTxAlignment_Type()
)
pm10001otu4AlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetworkTxAlignment.setStatus("current")
_Pm10001otu4AlmNetworkRxAlignment_Type = EkiOnOff
_Pm10001otu4AlmNetworkRxAlignment_Object = MibScalar
pm10001otu4AlmNetworkRxAlignment = _Pm10001otu4AlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51, 12),
    _Pm10001otu4AlmNetworkRxAlignment_Type()
)
pm10001otu4AlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetworkRxAlignment.setStatus("current")
_Pm10001otu4AlmNetworkRxOtn_Type = EkiOnOff
_Pm10001otu4AlmNetworkRxOtn_Object = MibScalar
pm10001otu4AlmNetworkRxOtn = _Pm10001otu4AlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51, 13),
    _Pm10001otu4AlmNetworkRxOtn_Type()
)
pm10001otu4AlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmNetworkRxOtn.setStatus("current")
_Pm10001otu4AlmHostRxAlignment_Type = EkiOnOff
_Pm10001otu4AlmHostRxAlignment_Object = MibScalar
pm10001otu4AlmHostRxAlignment = _Pm10001otu4AlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51, 14),
    _Pm10001otu4AlmHostRxAlignment_Type()
)
pm10001otu4AlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostRxAlignment.setStatus("current")
_Pm10001otu4AlmHostTxAlignment_Type = EkiOnOff
_Pm10001otu4AlmHostTxAlignment_Object = MibScalar
pm10001otu4AlmHostTxAlignment = _Pm10001otu4AlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51, 15),
    _Pm10001otu4AlmHostTxAlignment_Type()
)
pm10001otu4AlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostTxAlignment.setStatus("current")
_Pm10001otu4AlmHostTxOtnStatus_Type = EkiOnOff
_Pm10001otu4AlmHostTxOtnStatus_Object = MibScalar
pm10001otu4AlmHostTxOtnStatus = _Pm10001otu4AlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 51, 16),
    _Pm10001otu4AlmHostTxOtnStatus_Type()
)
pm10001otu4AlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostTxOtnStatus.setStatus("current")
_Pm10001otu4AlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaHostTxAlignment = _Pm10001otu4AlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 52)
)
_Pm10001otu4AlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm10001otu4AlmHostTxDeskewLockFault_Object = MibScalar
pm10001otu4AlmHostTxDeskewLockFault = _Pm10001otu4AlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 52, 13),
    _Pm10001otu4AlmHostTxDeskewLockFault_Type()
)
pm10001otu4AlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostTxDeskewLockFault.setStatus("current")
_Pm10001otu4AlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmHostTxOutOfAlignment_Object = MibScalar
pm10001otu4AlmHostTxOutOfAlignment = _Pm10001otu4AlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 52, 14),
    _Pm10001otu4AlmHostTxOutOfAlignment_Type()
)
pm10001otu4AlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostTxOutOfAlignment.setStatus("current")
_Pm10001otu4AlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmHostTxLossOfAlignment_Object = MibScalar
pm10001otu4AlmHostTxLossOfAlignment = _Pm10001otu4AlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 52, 15),
    _Pm10001otu4AlmHostTxLossOfAlignment_Type()
)
pm10001otu4AlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostTxLossOfAlignment.setStatus("current")
_Pm10001otu4AlmHostTxCdrLockFault_Type = EkiOnOff
_Pm10001otu4AlmHostTxCdrLockFault_Object = MibScalar
pm10001otu4AlmHostTxCdrLockFault = _Pm10001otu4AlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 52, 16),
    _Pm10001otu4AlmHostTxCdrLockFault_Type()
)
pm10001otu4AlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostTxCdrLockFault.setStatus("current")
_Pm10001otu4AlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm10001otu4AlmmsaHostRxAlignment = _Pm10001otu4AlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 53)
)
_Pm10001otu4AlmHostRxCmuLockFault_Type = EkiOnOff
_Pm10001otu4AlmHostRxCmuLockFault_Object = MibScalar
pm10001otu4AlmHostRxCmuLockFault = _Pm10001otu4AlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 53, 14),
    _Pm10001otu4AlmHostRxCmuLockFault_Type()
)
pm10001otu4AlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostRxCmuLockFault.setStatus("current")
_Pm10001otu4AlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmHostRxOutOfAlignment_Object = MibScalar
pm10001otu4AlmHostRxOutOfAlignment = _Pm10001otu4AlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 53, 15),
    _Pm10001otu4AlmHostRxOutOfAlignment_Type()
)
pm10001otu4AlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostRxOutOfAlignment.setStatus("current")
_Pm10001otu4AlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm10001otu4AlmHostRxLossOfAlignment_Object = MibScalar
pm10001otu4AlmHostRxLossOfAlignment = _Pm10001otu4AlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 1, 3, 53, 16),
    _Pm10001otu4AlmHostRxLossOfAlignment_Type()
)
pm10001otu4AlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHostRxLossOfAlignment.setStatus("current")
_Pm10001otu4AlmClient_ObjectIdentity = ObjectIdentity
pm10001otu4AlmClient = _Pm10001otu4AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2)
)
_Pm10001otu4AlmClientNurg_ObjectIdentity = ObjectIdentity
pm10001otu4AlmClientNurg = _Pm10001otu4AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1)
)
_Pm10001otu4AlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pm10001otu4AlmclientNetworkLaneAlarmWarningTable = _Pm10001otu4AlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pm10001otu4AlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pm10001otu4AlmclientNetworkLaneAlarmWarningEntry = _Pm10001otu4AlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1)
)
pm10001otu4AlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pm10001otu4AlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pm10001otu4AlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pm10001otu4AlmclientNetworkLaneAlarmWarningIndex = _Pm10001otu4AlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 1),
    _Pm10001otu4AlmclientNetworkLaneAlarmWarningIndex_Type()
)
pm10001otu4AlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pm10001otu4AlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientRxPowerLowAlarmPortn = _Pm10001otu4AlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 2),
    _Pm10001otu4AlmClientRxPowerLowAlarmPortn_Type()
)
pm10001otu4AlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientRxPowerLowWarningPortn = _Pm10001otu4AlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 3),
    _Pm10001otu4AlmClientRxPowerLowWarningPortn_Type()
)
pm10001otu4AlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientRxPowerLowWarningPortn.setStatus("current")
_Pm10001otu4AlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientRxPowerHighWarningPortn = _Pm10001otu4AlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 4),
    _Pm10001otu4AlmClientRxPowerHighWarningPortn_Type()
)
pm10001otu4AlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientRxPowerHighWarningPortn.setStatus("current")
_Pm10001otu4AlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientRxPowerHighAlarmPortn = _Pm10001otu4AlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 5),
    _Pm10001otu4AlmClientRxPowerHighAlarmPortn_Type()
)
pm10001otu4AlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLaserTempLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLaserTempLowAlarmPortn = _Pm10001otu4AlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 6),
    _Pm10001otu4AlmLaserTempLowAlarmPortn_Type()
)
pm10001otu4AlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLaserTempLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientLaserTempLowWarningPortn = _Pm10001otu4AlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 7),
    _Pm10001otu4AlmClientLaserTempLowWarningPortn_Type()
)
pm10001otu4AlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaserTempLowWarningPortn.setStatus("current")
_Pm10001otu4AlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientLaserTempHighWarningPortn = _Pm10001otu4AlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 8),
    _Pm10001otu4AlmClientLaserTempHighWarningPortn_Type()
)
pm10001otu4AlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaserTempHighWarningPortn.setStatus("current")
_Pm10001otu4AlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientLaserTempHighAlarmPortn = _Pm10001otu4AlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 9),
    _Pm10001otu4AlmClientLaserTempHighAlarmPortn_Type()
)
pm10001otu4AlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientTxPowerLowAlarmPortn = _Pm10001otu4AlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 10),
    _Pm10001otu4AlmClientTxPowerLowAlarmPortn_Type()
)
pm10001otu4AlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientTxPowerLowWarningPortn = _Pm10001otu4AlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 11),
    _Pm10001otu4AlmClientTxPowerLowWarningPortn_Type()
)
pm10001otu4AlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientTxPowerLowWarningPortn.setStatus("current")
_Pm10001otu4AlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientTxPowerHighWarningPortn = _Pm10001otu4AlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 12),
    _Pm10001otu4AlmClientTxPowerHighWarningPortn_Type()
)
pm10001otu4AlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientTxPowerHighWarningPortn.setStatus("current")
_Pm10001otu4AlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientTxPowerHighAlarmPortn = _Pm10001otu4AlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 13),
    _Pm10001otu4AlmClientTxPowerHighAlarmPortn_Type()
)
pm10001otu4AlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientBiasLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientBiasLowAlarmPortn = _Pm10001otu4AlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 14),
    _Pm10001otu4AlmClientBiasLowAlarmPortn_Type()
)
pm10001otu4AlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientBiasLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientBiasLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientBiasLowWarningPortn = _Pm10001otu4AlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 15),
    _Pm10001otu4AlmClientBiasLowWarningPortn_Type()
)
pm10001otu4AlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientBiasLowWarningPortn.setStatus("current")
_Pm10001otu4AlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmClientBiasHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmClientBiasHighWarningPortn = _Pm10001otu4AlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 16),
    _Pm10001otu4AlmClientBiasHighWarningPortn_Type()
)
pm10001otu4AlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientBiasHighWarningPortn.setStatus("current")
_Pm10001otu4AlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmClientBiasHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmClientBiasHighAlarmPortn = _Pm10001otu4AlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 56, 1, 17),
    _Pm10001otu4AlmClientBiasHighAlarmPortn_Type()
)
pm10001otu4AlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientBiasHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmclientSfpWarnDdmTable_Object = MibTable
pm10001otu4AlmclientSfpWarnDdmTable = _Pm10001otu4AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientSfpWarnDdmTable.setStatus("current")
_Pm10001otu4AlmclientSfpWarnDdmEntry_Object = MibTableRow
pm10001otu4AlmclientSfpWarnDdmEntry = _Pm10001otu4AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1)
)
pm10001otu4AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm10001otu4AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm10001otu4AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm10001otu4AlmclientSfpWarnDdmIndex = _Pm10001otu4AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 1),
    _Pm10001otu4AlmclientSfpWarnDdmIndex_Type()
)
pm10001otu4AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmclientSfpWarnDdmIndex.setStatus("current")
_Pm10001otu4AlmTxPwLowWngPortn_Type = EkiOnOff
_Pm10001otu4AlmTxPwLowWngPortn_Object = MibTableColumn
pm10001otu4AlmTxPwLowWngPortn = _Pm10001otu4AlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 2),
    _Pm10001otu4AlmTxPwLowWngPortn_Type()
)
pm10001otu4AlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxPwLowWngPortn.setStatus("current")
_Pm10001otu4AlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm10001otu4AlmTxPwrHighWngPortn_Object = MibTableColumn
pm10001otu4AlmTxPwrHighWngPortn = _Pm10001otu4AlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 3),
    _Pm10001otu4AlmTxPwrHighWngPortn_Type()
)
pm10001otu4AlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxPwrHighWngPortn.setStatus("current")
_Pm10001otu4AlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm10001otu4AlmTxBiasLowWngPortn_Object = MibTableColumn
pm10001otu4AlmTxBiasLowWngPortn = _Pm10001otu4AlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 4),
    _Pm10001otu4AlmTxBiasLowWngPortn_Type()
)
pm10001otu4AlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxBiasLowWngPortn.setStatus("current")
_Pm10001otu4AlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm10001otu4AlmTxBiasHighWngPortn_Object = MibTableColumn
pm10001otu4AlmTxBiasHighWngPortn = _Pm10001otu4AlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 5),
    _Pm10001otu4AlmTxBiasHighWngPortn_Type()
)
pm10001otu4AlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxBiasHighWngPortn.setStatus("current")
_Pm10001otu4AlmVccLowWngPortn_Type = EkiOnOff
_Pm10001otu4AlmVccLowWngPortn_Object = MibTableColumn
pm10001otu4AlmVccLowWngPortn = _Pm10001otu4AlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 6),
    _Pm10001otu4AlmVccLowWngPortn_Type()
)
pm10001otu4AlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmVccLowWngPortn.setStatus("current")
_Pm10001otu4AlmVccHighWngPortn_Type = EkiOnOff
_Pm10001otu4AlmVccHighWngPortn_Object = MibTableColumn
pm10001otu4AlmVccHighWngPortn = _Pm10001otu4AlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 7),
    _Pm10001otu4AlmVccHighWngPortn_Type()
)
pm10001otu4AlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmVccHighWngPortn.setStatus("current")
_Pm10001otu4AlmTempLowWngPortn_Type = EkiOnOff
_Pm10001otu4AlmTempLowWngPortn_Object = MibTableColumn
pm10001otu4AlmTempLowWngPortn = _Pm10001otu4AlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 8),
    _Pm10001otu4AlmTempLowWngPortn_Type()
)
pm10001otu4AlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTempLowWngPortn.setStatus("current")
_Pm10001otu4AlmTempHighWngPortn_Type = EkiOnOff
_Pm10001otu4AlmTempHighWngPortn_Object = MibTableColumn
pm10001otu4AlmTempHighWngPortn = _Pm10001otu4AlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 9),
    _Pm10001otu4AlmTempHighWngPortn_Type()
)
pm10001otu4AlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTempHighWngPortn.setStatus("current")
_Pm10001otu4AlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm10001otu4AlmRxPwrLowWngPortn_Object = MibTableColumn
pm10001otu4AlmRxPwrLowWngPortn = _Pm10001otu4AlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 16),
    _Pm10001otu4AlmRxPwrLowWngPortn_Type()
)
pm10001otu4AlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxPwrLowWngPortn.setStatus("current")
_Pm10001otu4AlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm10001otu4AlmRxPwrHighWngPortn_Object = MibTableColumn
pm10001otu4AlmRxPwrHighWngPortn = _Pm10001otu4AlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 1, 232, 1, 17),
    _Pm10001otu4AlmRxPwrHighWngPortn_Type()
)
pm10001otu4AlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxPwrHighWngPortn.setStatus("current")
_Pm10001otu4AlmClientUrg_ObjectIdentity = ObjectIdentity
pm10001otu4AlmClientUrg = _Pm10001otu4AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2)
)
_Pm10001otu4AlmclientNetworkLaneFaultTable_Object = MibTable
pm10001otu4AlmclientNetworkLaneFaultTable = _Pm10001otu4AlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientNetworkLaneFaultTable.setStatus("current")
_Pm10001otu4AlmclientNetworkLaneFaultEntry_Object = MibTableRow
pm10001otu4AlmclientNetworkLaneFaultEntry = _Pm10001otu4AlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1)
)
pm10001otu4AlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pm10001otu4AlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10001otu4AlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pm10001otu4AlmclientNetworkLaneFaultIndex = _Pm10001otu4AlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 1),
    _Pm10001otu4AlmclientNetworkLaneFaultIndex_Type()
)
pm10001otu4AlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmclientNetworkLaneFaultIndex.setStatus("current")
_Pm10001otu4AlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneRxFifoErrorPortn = _Pm10001otu4AlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 4),
    _Pm10001otu4AlmClientLaneRxFifoErrorPortn_Type()
)
pm10001otu4AlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pm10001otu4AlmClientLaneRxLolPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneRxLolPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneRxLolPortn = _Pm10001otu4AlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 5),
    _Pm10001otu4AlmClientLaneRxLolPortn_Type()
)
pm10001otu4AlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneRxLolPortn.setStatus("current")
_Pm10001otu4AlmClientLaneRxLosPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneRxLosPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneRxLosPortn = _Pm10001otu4AlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 6),
    _Pm10001otu4AlmClientLaneRxLosPortn_Type()
)
pm10001otu4AlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneRxLosPortn.setStatus("current")
_Pm10001otu4AlmClientLaneTxLolPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneTxLolPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneTxLolPortn = _Pm10001otu4AlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 8),
    _Pm10001otu4AlmClientLaneTxLolPortn_Type()
)
pm10001otu4AlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneTxLolPortn.setStatus("current")
_Pm10001otu4AlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneTxLosfPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneTxLosfPortn = _Pm10001otu4AlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 9),
    _Pm10001otu4AlmClientLaneTxLosfPortn_Type()
)
pm10001otu4AlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneTxLosfPortn.setStatus("current")
_Pm10001otu4AlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneApdPowerSupplyPortn = _Pm10001otu4AlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 15),
    _Pm10001otu4AlmClientLaneApdPowerSupplyPortn_Type()
)
pm10001otu4AlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pm10001otu4AlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneWavelengthUnlockedPortn = _Pm10001otu4AlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 16),
    _Pm10001otu4AlmClientLaneWavelengthUnlockedPortn_Type()
)
pm10001otu4AlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10001otu4AlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneTecFaultPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneTecFaultPortn = _Pm10001otu4AlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 72, 1, 17),
    _Pm10001otu4AlmClientLaneTecFaultPortn_Type()
)
pm10001otu4AlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneTecFaultPortn.setStatus("current")
_Pm10001otu4AlmclientHostLaneFaultTable_Object = MibTable
pm10001otu4AlmclientHostLaneFaultTable = _Pm10001otu4AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientHostLaneFaultTable.setStatus("current")
_Pm10001otu4AlmclientHostLaneFaultEntry_Object = MibTableRow
pm10001otu4AlmclientHostLaneFaultEntry = _Pm10001otu4AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1)
)
pm10001otu4AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientHostLaneFaultEntry.setStatus("current")


class _Pm10001otu4AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10001otu4AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmclientHostLaneFaultIndex_Object = MibTableColumn
pm10001otu4AlmclientHostLaneFaultIndex = _Pm10001otu4AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 1),
    _Pm10001otu4AlmclientHostLaneFaultIndex_Type()
)
pm10001otu4AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmclientHostLaneFaultIndex.setStatus("current")
_Pm10001otu4AlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLossOfSyncPortn_Object = MibTableColumn
pm10001otu4AlmClientLossOfSyncPortn = _Pm10001otu4AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 2),
    _Pm10001otu4AlmClientLossOfSyncPortn_Type()
)
pm10001otu4AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLossOfSyncPortn.setStatus("current")
_Pm10001otu4AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm10001otu4AlmClientInputLossOfSigPortn_Object = MibTableColumn
pm10001otu4AlmClientInputLossOfSigPortn = _Pm10001otu4AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 3),
    _Pm10001otu4AlmClientInputLossOfSigPortn_Type()
)
pm10001otu4AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientInputLossOfSigPortn.setStatus("current")
_Pm10001otu4AlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm10001otu4AlmClientLanesMarkerUnlockPortn = _Pm10001otu4AlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 4),
    _Pm10001otu4AlmClientLanesMarkerUnlockPortn_Type()
)
pm10001otu4AlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm10001otu4AlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm10001otu4AlmClientLanes6466UnlockPortn = _Pm10001otu4AlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 5),
    _Pm10001otu4AlmClientLanes6466UnlockPortn_Type()
)
pm10001otu4AlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLanes6466UnlockPortn.setStatus("current")
_Pm10001otu4AlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm10001otu4AlmClientLanesNotAlignedPortn = _Pm10001otu4AlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 6),
    _Pm10001otu4AlmClientLanesNotAlignedPortn_Type()
)
pm10001otu4AlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLanesNotAlignedPortn.setStatus("current")
_Pm10001otu4AlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm10001otu4AlmClientCsfDetectedPortn_Object = MibTableColumn
pm10001otu4AlmClientCsfDetectedPortn = _Pm10001otu4AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 7),
    _Pm10001otu4AlmClientCsfDetectedPortn_Type()
)
pm10001otu4AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientCsfDetectedPortn.setStatus("current")
_Pm10001otu4AlmClientTxHostLolPortn_Type = EkiOnOff
_Pm10001otu4AlmClientTxHostLolPortn_Object = MibTableColumn
pm10001otu4AlmClientTxHostLolPortn = _Pm10001otu4AlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 10),
    _Pm10001otu4AlmClientTxHostLolPortn_Type()
)
pm10001otu4AlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientTxHostLolPortn.setStatus("current")
_Pm10001otu4AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm10001otu4AlmClientLaneTxFifoErrorPortn = _Pm10001otu4AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 11),
    _Pm10001otu4AlmClientLaneTxFifoErrorPortn_Type()
)
pm10001otu4AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm10001otu4AlmLfDetectedPortn_Type = EkiOnOff
_Pm10001otu4AlmLfDetectedPortn_Object = MibTableColumn
pm10001otu4AlmLfDetectedPortn = _Pm10001otu4AlmLfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 12),
    _Pm10001otu4AlmLfDetectedPortn_Type()
)
pm10001otu4AlmLfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLfDetectedPortn.setStatus("current")
_Pm10001otu4AlmRfDetectedPortn_Type = EkiOnOff
_Pm10001otu4AlmRfDetectedPortn_Object = MibTableColumn
pm10001otu4AlmRfDetectedPortn = _Pm10001otu4AlmRfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 88, 1, 13),
    _Pm10001otu4AlmRfDetectedPortn_Type()
)
pm10001otu4AlmRfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRfDetectedPortn.setStatus("current")
_Pm10001otu4AlmclientSfpAlmDdmTable_Object = MibTable
pm10001otu4AlmclientSfpAlmDdmTable = _Pm10001otu4AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientSfpAlmDdmTable.setStatus("current")
_Pm10001otu4AlmclientSfpAlmDdmEntry_Object = MibTableRow
pm10001otu4AlmclientSfpAlmDdmEntry = _Pm10001otu4AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1)
)
pm10001otu4AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm10001otu4AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm10001otu4AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm10001otu4AlmclientSfpAlmDdmIndex = _Pm10001otu4AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 1),
    _Pm10001otu4AlmclientSfpAlmDdmIndex_Type()
)
pm10001otu4AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmclientSfpAlmDdmIndex.setStatus("current")
_Pm10001otu4AlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmTxPwrLowAlaPortn_Object = MibTableColumn
pm10001otu4AlmTxPwrLowAlaPortn = _Pm10001otu4AlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 2),
    _Pm10001otu4AlmTxPwrLowAlaPortn_Type()
)
pm10001otu4AlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxPwrLowAlaPortn.setStatus("current")
_Pm10001otu4AlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmTxPwrHighAlaPortn_Object = MibTableColumn
pm10001otu4AlmTxPwrHighAlaPortn = _Pm10001otu4AlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 3),
    _Pm10001otu4AlmTxPwrHighAlaPortn_Type()
)
pm10001otu4AlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxPwrHighAlaPortn.setStatus("current")
_Pm10001otu4AlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmTxBiasLowAlaPortn_Object = MibTableColumn
pm10001otu4AlmTxBiasLowAlaPortn = _Pm10001otu4AlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 4),
    _Pm10001otu4AlmTxBiasLowAlaPortn_Type()
)
pm10001otu4AlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxBiasLowAlaPortn.setStatus("current")
_Pm10001otu4AlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmTxBiasHighAlaPortn_Object = MibTableColumn
pm10001otu4AlmTxBiasHighAlaPortn = _Pm10001otu4AlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 5),
    _Pm10001otu4AlmTxBiasHighAlaPortn_Type()
)
pm10001otu4AlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxBiasHighAlaPortn.setStatus("current")
_Pm10001otu4AlmVccLowAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmVccLowAlaPortn_Object = MibTableColumn
pm10001otu4AlmVccLowAlaPortn = _Pm10001otu4AlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 6),
    _Pm10001otu4AlmVccLowAlaPortn_Type()
)
pm10001otu4AlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmVccLowAlaPortn.setStatus("current")
_Pm10001otu4AlmVccHighAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmVccHighAlaPortn_Object = MibTableColumn
pm10001otu4AlmVccHighAlaPortn = _Pm10001otu4AlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 7),
    _Pm10001otu4AlmVccHighAlaPortn_Type()
)
pm10001otu4AlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmVccHighAlaPortn.setStatus("current")
_Pm10001otu4AlmTempLowAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmTempLowAlaPortn_Object = MibTableColumn
pm10001otu4AlmTempLowAlaPortn = _Pm10001otu4AlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 8),
    _Pm10001otu4AlmTempLowAlaPortn_Type()
)
pm10001otu4AlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTempLowAlaPortn.setStatus("current")
_Pm10001otu4AlmTempHighAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmTempHighAlaPortn_Object = MibTableColumn
pm10001otu4AlmTempHighAlaPortn = _Pm10001otu4AlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 9),
    _Pm10001otu4AlmTempHighAlaPortn_Type()
)
pm10001otu4AlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTempHighAlaPortn.setStatus("current")
_Pm10001otu4AlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmRxPwrLowAlaPortn_Object = MibTableColumn
pm10001otu4AlmRxPwrLowAlaPortn = _Pm10001otu4AlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 16),
    _Pm10001otu4AlmRxPwrLowAlaPortn_Type()
)
pm10001otu4AlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxPwrLowAlaPortn.setStatus("current")
_Pm10001otu4AlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm10001otu4AlmRxPwrHighAlaPortn_Object = MibTableColumn
pm10001otu4AlmRxPwrHighAlaPortn = _Pm10001otu4AlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 2, 216, 1, 17),
    _Pm10001otu4AlmRxPwrHighAlaPortn_Type()
)
pm10001otu4AlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxPwrHighAlaPortn.setStatus("current")
_Pm10001otu4AlmClientCrit_ObjectIdentity = ObjectIdentity
pm10001otu4AlmClientCrit = _Pm10001otu4AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3)
)
_Pm10001otu4AlmsynthAlmPortTable_Object = MibTable
pm10001otu4AlmsynthAlmPortTable = _Pm10001otu4AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmsynthAlmPortTable.setStatus("current")
_Pm10001otu4AlmsynthAlmPortEntry_Object = MibTableRow
pm10001otu4AlmsynthAlmPortEntry = _Pm10001otu4AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1)
)
pm10001otu4AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmsynthAlmPortEntry.setStatus("current")


class _Pm10001otu4AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm10001otu4AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmsynthAlmPortIndex_Object = MibTableColumn
pm10001otu4AlmsynthAlmPortIndex = _Pm10001otu4AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 1),
    _Pm10001otu4AlmsynthAlmPortIndex_Type()
)
pm10001otu4AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmsynthAlmPortIndex.setStatus("current")
_Pm10001otu4AlmSfpAbsentPortn_Type = EkiOnOff
_Pm10001otu4AlmSfpAbsentPortn_Object = MibTableColumn
pm10001otu4AlmSfpAbsentPortn = _Pm10001otu4AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 2),
    _Pm10001otu4AlmSfpAbsentPortn_Type()
)
pm10001otu4AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmSfpAbsentPortn.setStatus("current")
_Pm10001otu4AlmDdmAbsentPortn_Type = EkiOnOff
_Pm10001otu4AlmDdmAbsentPortn_Object = MibTableColumn
pm10001otu4AlmDdmAbsentPortn = _Pm10001otu4AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 3),
    _Pm10001otu4AlmDdmAbsentPortn_Type()
)
pm10001otu4AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmDdmAbsentPortn.setStatus("current")
_Pm10001otu4AlmHwFailAccPortn_Type = EkiOnOff
_Pm10001otu4AlmHwFailAccPortn_Object = MibTableColumn
pm10001otu4AlmHwFailAccPortn = _Pm10001otu4AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 5),
    _Pm10001otu4AlmHwFailAccPortn_Type()
)
pm10001otu4AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmHwFailAccPortn.setStatus("current")
_Pm10001otu4AlmDwLsdPortn_Type = EkiOnOff
_Pm10001otu4AlmDwLsdPortn_Object = MibTableColumn
pm10001otu4AlmDwLsdPortn = _Pm10001otu4AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 6),
    _Pm10001otu4AlmDwLsdPortn_Type()
)
pm10001otu4AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmDwLsdPortn.setStatus("current")
_Pm10001otu4AlmClientLocalOosPortn_Type = EkiOnOff
_Pm10001otu4AlmClientLocalOosPortn_Object = MibTableColumn
pm10001otu4AlmClientLocalOosPortn = _Pm10001otu4AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 7),
    _Pm10001otu4AlmClientLocalOosPortn_Type()
)
pm10001otu4AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientLocalOosPortn.setStatus("current")
_Pm10001otu4AlmClientRemoteOosPortn_Type = EkiOnOff
_Pm10001otu4AlmClientRemoteOosPortn_Object = MibTableColumn
pm10001otu4AlmClientRemoteOosPortn = _Pm10001otu4AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 8),
    _Pm10001otu4AlmClientRemoteOosPortn_Type()
)
pm10001otu4AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmClientRemoteOosPortn.setStatus("current")
_Pm10001otu4AlmDwCaisPortn_Type = EkiOnOff
_Pm10001otu4AlmDwCaisPortn_Object = MibTableColumn
pm10001otu4AlmDwCaisPortn = _Pm10001otu4AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 9),
    _Pm10001otu4AlmDwCaisPortn_Type()
)
pm10001otu4AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmDwCaisPortn.setStatus("current")
_Pm10001otu4AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmSfpDdmWarningPortn_Object = MibTableColumn
pm10001otu4AlmSfpDdmWarningPortn = _Pm10001otu4AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 10),
    _Pm10001otu4AlmSfpDdmWarningPortn_Type()
)
pm10001otu4AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmSfpDdmWarningPortn.setStatus("current")
_Pm10001otu4AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm10001otu4AlmSfpDdmAlmPortn_Object = MibTableColumn
pm10001otu4AlmSfpDdmAlmPortn = _Pm10001otu4AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 11),
    _Pm10001otu4AlmSfpDdmAlmPortn_Type()
)
pm10001otu4AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmSfpDdmAlmPortn.setStatus("current")
_Pm10001otu4AlmIdleInsertedPortn_Type = EkiOnOff
_Pm10001otu4AlmIdleInsertedPortn_Object = MibTableColumn
pm10001otu4AlmIdleInsertedPortn = _Pm10001otu4AlmIdleInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 12),
    _Pm10001otu4AlmIdleInsertedPortn_Type()
)
pm10001otu4AlmIdleInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmIdleInsertedPortn.setStatus("current")
_Pm10001otu4AlmFailAccPortn_Type = EkiOnOff
_Pm10001otu4AlmFailAccPortn_Object = MibTableColumn
pm10001otu4AlmFailAccPortn = _Pm10001otu4AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 13),
    _Pm10001otu4AlmFailAccPortn_Type()
)
pm10001otu4AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmFailAccPortn.setStatus("current")
_Pm10001otu4AlmUpCsfPortn_Type = EkiOnOff
_Pm10001otu4AlmUpCsfPortn_Object = MibTableColumn
pm10001otu4AlmUpCsfPortn = _Pm10001otu4AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 2, 3, 8, 1, 17),
    _Pm10001otu4AlmUpCsfPortn_Type()
)
pm10001otu4AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmUpCsfPortn.setStatus("current")
_Pm10001otu4AlmLine_ObjectIdentity = ObjectIdentity
pm10001otu4AlmLine = _Pm10001otu4AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3)
)
_Pm10001otu4AlmLineNurg_ObjectIdentity = ObjectIdentity
pm10001otu4AlmLineNurg = _Pm10001otu4AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1)
)
_Pm10001otu4AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm10001otu4AlmlineNetworkLaneAlarmWarning1Table = _Pm10001otu4AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry = _Pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1)
)
pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm10001otu4AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm10001otu4AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm10001otu4AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm10001otu4AlmlineNetworkLaneAlarmWarning1Index = _Pm10001otu4AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 1),
    _Pm10001otu4AlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm10001otu4AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm10001otu4AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineRxPowerLowAlarmPortn = _Pm10001otu4AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 2),
    _Pm10001otu4AlmLineRxPowerLowAlarmPortn_Type()
)
pm10001otu4AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineRxPowerLowWarningPortn = _Pm10001otu4AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 3),
    _Pm10001otu4AlmLineRxPowerLowWarningPortn_Type()
)
pm10001otu4AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm10001otu4AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineRxPowerHighWarningPortn = _Pm10001otu4AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 4),
    _Pm10001otu4AlmLineRxPowerHighWarningPortn_Type()
)
pm10001otu4AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm10001otu4AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineRxPowerHighAlarmPortn = _Pm10001otu4AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 5),
    _Pm10001otu4AlmLineRxPowerHighAlarmPortn_Type()
)
pm10001otu4AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineLaserTempLowAlarmPortn = _Pm10001otu4AlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 6),
    _Pm10001otu4AlmLineLaserTempLowAlarmPortn_Type()
)
pm10001otu4AlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineLaserTempLowWarningPortn = _Pm10001otu4AlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 7),
    _Pm10001otu4AlmLineLaserTempLowWarningPortn_Type()
)
pm10001otu4AlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm10001otu4AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineLaserTempHighWarningPortn = _Pm10001otu4AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 8),
    _Pm10001otu4AlmLineLaserTempHighWarningPortn_Type()
)
pm10001otu4AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm10001otu4AlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineLaserTempHighAlarmPortn = _Pm10001otu4AlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 9),
    _Pm10001otu4AlmLineLaserTempHighAlarmPortn_Type()
)
pm10001otu4AlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineTxPowerLowAlarmPortn = _Pm10001otu4AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 10),
    _Pm10001otu4AlmLineTxPowerLowAlarmPortn_Type()
)
pm10001otu4AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineTxPowerLowWarningPortn = _Pm10001otu4AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 11),
    _Pm10001otu4AlmLineTxPowerLowWarningPortn_Type()
)
pm10001otu4AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm10001otu4AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineTxPowerHighWarningPortn = _Pm10001otu4AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 12),
    _Pm10001otu4AlmLineTxPowerHighWarningPortn_Type()
)
pm10001otu4AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm10001otu4AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineTxPowerHighAlarmPortn = _Pm10001otu4AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 13),
    _Pm10001otu4AlmLineTxPowerHighAlarmPortn_Type()
)
pm10001otu4AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineBiasLowAlarmPortn = _Pm10001otu4AlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 14),
    _Pm10001otu4AlmLineBiasLowAlarmPortn_Type()
)
pm10001otu4AlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineBiasLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineBiasLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineBiasLowWarningPortn = _Pm10001otu4AlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 15),
    _Pm10001otu4AlmLineBiasLowWarningPortn_Type()
)
pm10001otu4AlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineBiasLowWarningPortn.setStatus("current")
_Pm10001otu4AlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineBiasHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineBiasHighWarningPortn = _Pm10001otu4AlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 16),
    _Pm10001otu4AlmLineBiasHighWarningPortn_Type()
)
pm10001otu4AlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineBiasHighWarningPortn.setStatus("current")
_Pm10001otu4AlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmLineBiasHighAlarmPortn = _Pm10001otu4AlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 104, 1, 17),
    _Pm10001otu4AlmLineBiasHighAlarmPortn_Type()
)
pm10001otu4AlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineBiasHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm10001otu4AlmlineNetworkLaneAlarmWarning2Table = _Pm10001otu4AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry = _Pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1)
)
pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm10001otu4AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm10001otu4AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm10001otu4AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm10001otu4AlmlineNetworkLaneAlarmWarning2Index = _Pm10001otu4AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 1),
    _Pm10001otu4AlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm10001otu4AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm10001otu4AlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmTxModulatorBiasLowAlarmPortn = _Pm10001otu4AlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 2),
    _Pm10001otu4AlmTxModulatorBiasLowAlarmPortn_Type()
)
pm10001otu4AlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmTxModulatorBiasLowWarningPortn = _Pm10001otu4AlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 3),
    _Pm10001otu4AlmTxModulatorBiasLowWarningPortn_Type()
)
pm10001otu4AlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm10001otu4AlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmTxModulatorBiasHighWarningPortn = _Pm10001otu4AlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 4),
    _Pm10001otu4AlmTxModulatorBiasHighWarningPortn_Type()
)
pm10001otu4AlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm10001otu4AlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmTxModulatorBiasHighAlarmPortn = _Pm10001otu4AlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 5),
    _Pm10001otu4AlmTxModulatorBiasHighAlarmPortn_Type()
)
pm10001otu4AlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserTempLowAlarmPortn = _Pm10001otu4AlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 6),
    _Pm10001otu4AlmRxLaserTempLowAlarmPortn_Type()
)
pm10001otu4AlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserTempLowWarningPortn = _Pm10001otu4AlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 7),
    _Pm10001otu4AlmRxLaserTempLowWarningPortn_Type()
)
pm10001otu4AlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm10001otu4AlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserTempHighWarningPortn = _Pm10001otu4AlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 8),
    _Pm10001otu4AlmRxLaserTempHighWarningPortn_Type()
)
pm10001otu4AlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm10001otu4AlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserTempHighAlarmPortn = _Pm10001otu4AlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 9),
    _Pm10001otu4AlmRxLaserTempHighAlarmPortn_Type()
)
pm10001otu4AlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserOutputLowAlarmPortn = _Pm10001otu4AlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 10),
    _Pm10001otu4AlmRxLaserOutputLowAlarmPortn_Type()
)
pm10001otu4AlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserOutputLowWarningPortn = _Pm10001otu4AlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 11),
    _Pm10001otu4AlmRxLaserOutputLowWarningPortn_Type()
)
pm10001otu4AlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm10001otu4AlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserOutputHighWarningPortn = _Pm10001otu4AlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 12),
    _Pm10001otu4AlmRxLaserOutputHighWarningPortn_Type()
)
pm10001otu4AlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm10001otu4AlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserOutputHighAlarmPortn = _Pm10001otu4AlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 13),
    _Pm10001otu4AlmRxLaserOutputHighAlarmPortn_Type()
)
pm10001otu4AlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserBiasLowAlarmPortn = _Pm10001otu4AlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 14),
    _Pm10001otu4AlmRxLaserBiasLowAlarmPortn_Type()
)
pm10001otu4AlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm10001otu4AlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserBiasLowWarningPortn = _Pm10001otu4AlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 15),
    _Pm10001otu4AlmRxLaserBiasLowWarningPortn_Type()
)
pm10001otu4AlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm10001otu4AlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserBiasHighWarningPortn = _Pm10001otu4AlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 16),
    _Pm10001otu4AlmRxLaserBiasHighWarningPortn_Type()
)
pm10001otu4AlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm10001otu4AlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm10001otu4AlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm10001otu4AlmRxLaserBiasHighAlarmPortn = _Pm10001otu4AlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 1, 120, 1, 17),
    _Pm10001otu4AlmRxLaserBiasHighAlarmPortn_Type()
)
pm10001otu4AlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm10001otu4AlmLineUrg_ObjectIdentity = ObjectIdentity
pm10001otu4AlmLineUrg = _Pm10001otu4AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2)
)
_Pm10001otu4AlmlineNetworkLaneFaultTable_Object = MibTable
pm10001otu4AlmlineNetworkLaneFaultTable = _Pm10001otu4AlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneFaultTable.setStatus("current")
_Pm10001otu4AlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm10001otu4AlmlineNetworkLaneFaultEntry = _Pm10001otu4AlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1)
)
pm10001otu4AlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm10001otu4AlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10001otu4AlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm10001otu4AlmlineNetworkLaneFaultIndex = _Pm10001otu4AlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 1),
    _Pm10001otu4AlmlineNetworkLaneFaultIndex_Type()
)
pm10001otu4AlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm10001otu4AlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneRxTecFaultPortn = _Pm10001otu4AlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 3),
    _Pm10001otu4AlmLineLaneRxTecFaultPortn_Type()
)
pm10001otu4AlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm10001otu4AlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneRxFifoErrorPortn = _Pm10001otu4AlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 4),
    _Pm10001otu4AlmLineLaneRxFifoErrorPortn_Type()
)
pm10001otu4AlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm10001otu4AlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneRxLolPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneRxLolPortn = _Pm10001otu4AlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 5),
    _Pm10001otu4AlmLineLaneRxLolPortn_Type()
)
pm10001otu4AlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneRxLolPortn.setStatus("current")
_Pm10001otu4AlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneRxLosPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneRxLosPortn = _Pm10001otu4AlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 6),
    _Pm10001otu4AlmLineLaneRxLosPortn_Type()
)
pm10001otu4AlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneRxLosPortn.setStatus("current")
_Pm10001otu4AlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneTxLolPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneTxLolPortn = _Pm10001otu4AlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 8),
    _Pm10001otu4AlmLineLaneTxLolPortn_Type()
)
pm10001otu4AlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneTxLolPortn.setStatus("current")
_Pm10001otu4AlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneTxLosfPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneTxLosfPortn = _Pm10001otu4AlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 9),
    _Pm10001otu4AlmLineLaneTxLosfPortn_Type()
)
pm10001otu4AlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneTxLosfPortn.setStatus("current")
_Pm10001otu4AlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneApdPowerSupplyPortn = _Pm10001otu4AlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 15),
    _Pm10001otu4AlmLineLaneApdPowerSupplyPortn_Type()
)
pm10001otu4AlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm10001otu4AlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneWavelengthUnlockedPortn = _Pm10001otu4AlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 16),
    _Pm10001otu4AlmLineLaneWavelengthUnlockedPortn_Type()
)
pm10001otu4AlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10001otu4AlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneTecFaultPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneTecFaultPortn = _Pm10001otu4AlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 136, 1, 17),
    _Pm10001otu4AlmLineLaneTecFaultPortn_Type()
)
pm10001otu4AlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneTecFaultPortn.setStatus("current")
_Pm10001otu4AlmlineHostLaneFaultTable_Object = MibTable
pm10001otu4AlmlineHostLaneFaultTable = _Pm10001otu4AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineHostLaneFaultTable.setStatus("current")
_Pm10001otu4AlmlineHostLaneFaultEntry_Object = MibTableRow
pm10001otu4AlmlineHostLaneFaultEntry = _Pm10001otu4AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1)
)
pm10001otu4AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineHostLaneFaultEntry.setStatus("current")


class _Pm10001otu4AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10001otu4AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmlineHostLaneFaultIndex_Object = MibTableColumn
pm10001otu4AlmlineHostLaneFaultIndex = _Pm10001otu4AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 1),
    _Pm10001otu4AlmlineHostLaneFaultIndex_Type()
)
pm10001otu4AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmlineHostLaneFaultIndex.setStatus("current")
_Pm10001otu4AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm10001otu4AlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm10001otu4AlmLineInputLossOfSignalPortn = _Pm10001otu4AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 2),
    _Pm10001otu4AlmLineInputLossOfSignalPortn_Type()
)
pm10001otu4AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineInputLossOfSignalPortn.setStatus("current")
_Pm10001otu4AlmLineLossOfFramePortn_Type = EkiOnOff
_Pm10001otu4AlmLineLossOfFramePortn_Object = MibTableColumn
pm10001otu4AlmLineLossOfFramePortn = _Pm10001otu4AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 3),
    _Pm10001otu4AlmLineLossOfFramePortn_Type()
)
pm10001otu4AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLossOfFramePortn.setStatus("current")
_Pm10001otu4AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm10001otu4AlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm10001otu4AlmLineSmBdiInsertedPortn = _Pm10001otu4AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 4),
    _Pm10001otu4AlmLineSmBdiInsertedPortn_Type()
)
pm10001otu4AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineSmBdiInsertedPortn.setStatus("current")
_Pm10001otu4AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm10001otu4AlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm10001otu4AlmLineSmBdiDetectedPortn = _Pm10001otu4AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 5),
    _Pm10001otu4AlmLineSmBdiDetectedPortn_Type()
)
pm10001otu4AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineSmBdiDetectedPortn.setStatus("current")
_Pm10001otu4AlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm10001otu4AlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm10001otu4AlmLineSmIaeInsertedPortn = _Pm10001otu4AlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 6),
    _Pm10001otu4AlmLineSmIaeInsertedPortn_Type()
)
pm10001otu4AlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineSmIaeInsertedPortn.setStatus("current")
_Pm10001otu4AlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm10001otu4AlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm10001otu4AlmLineSmIaeDetectedPortn = _Pm10001otu4AlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 7),
    _Pm10001otu4AlmLineSmIaeDetectedPortn_Type()
)
pm10001otu4AlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineSmIaeDetectedPortn.setStatus("current")
_Pm10001otu4AlmLineTxHostLolPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxHostLolPortn_Object = MibTableColumn
pm10001otu4AlmLineTxHostLolPortn = _Pm10001otu4AlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 10),
    _Pm10001otu4AlmLineTxHostLolPortn_Type()
)
pm10001otu4AlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxHostLolPortn.setStatus("current")
_Pm10001otu4AlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm10001otu4AlmLineLaneTxFifoErrorPortn = _Pm10001otu4AlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 11),
    _Pm10001otu4AlmLineLaneTxFifoErrorPortn_Type()
)
pm10001otu4AlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm10001otu4AlmLinePowerDegradePortn_Type = EkiOnOff
_Pm10001otu4AlmLinePowerDegradePortn_Object = MibTableColumn
pm10001otu4AlmLinePowerDegradePortn = _Pm10001otu4AlmLinePowerDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 16),
    _Pm10001otu4AlmLinePowerDegradePortn_Type()
)
pm10001otu4AlmLinePowerDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLinePowerDegradePortn.setStatus("current")
_Pm10001otu4AlmLineTrxOverTempPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTrxOverTempPortn_Object = MibTableColumn
pm10001otu4AlmLineTrxOverTempPortn = _Pm10001otu4AlmLineTrxOverTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 152, 1, 17),
    _Pm10001otu4AlmLineTrxOverTempPortn_Type()
)
pm10001otu4AlmLineTrxOverTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTrxOverTempPortn.setStatus("current")
_Pm10001otu4AlmlineNetworkLaneRxOtnTable_Object = MibTable
pm10001otu4AlmlineNetworkLaneRxOtnTable = _Pm10001otu4AlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm10001otu4AlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm10001otu4AlmlineNetworkLaneRxOtnEntry = _Pm10001otu4AlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1)
)
pm10001otu4AlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm10001otu4AlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm10001otu4AlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm10001otu4AlmlineNetworkLaneRxOtnIndex = _Pm10001otu4AlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 1),
    _Pm10001otu4AlmlineNetworkLaneRxOtnIndex_Type()
)
pm10001otu4AlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm10001otu4AlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnOduAisPortn = _Pm10001otu4AlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 10),
    _Pm10001otu4AlmLineRxOtnOduAisPortn_Type()
)
pm10001otu4AlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnOduAisPortn.setStatus("current")
_Pm10001otu4AlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnOtuAisPortn = _Pm10001otu4AlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 11),
    _Pm10001otu4AlmLineRxOtnOtuAisPortn_Type()
)
pm10001otu4AlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm10001otu4AlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxSmBdiPortn_Object = MibTableColumn
pm10001otu4AlmLineRxSmBdiPortn = _Pm10001otu4AlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 12),
    _Pm10001otu4AlmLineRxSmBdiPortn_Type()
)
pm10001otu4AlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxSmBdiPortn.setStatus("current")
_Pm10001otu4AlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnIaePortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnIaePortn = _Pm10001otu4AlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 13),
    _Pm10001otu4AlmLineRxOtnIaePortn_Type()
)
pm10001otu4AlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnIaePortn.setStatus("current")
_Pm10001otu4AlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnOomPortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnOomPortn = _Pm10001otu4AlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 14),
    _Pm10001otu4AlmLineRxOtnOomPortn_Type()
)
pm10001otu4AlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnOomPortn.setStatus("current")
_Pm10001otu4AlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnLomPortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnLomPortn = _Pm10001otu4AlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 15),
    _Pm10001otu4AlmLineRxOtnLomPortn_Type()
)
pm10001otu4AlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnLomPortn.setStatus("current")
_Pm10001otu4AlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnOofPortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnOofPortn = _Pm10001otu4AlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 16),
    _Pm10001otu4AlmLineRxOtnOofPortn_Type()
)
pm10001otu4AlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnOofPortn.setStatus("current")
_Pm10001otu4AlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm10001otu4AlmLineRxOtnLofPortn_Object = MibTableColumn
pm10001otu4AlmLineRxOtnLofPortn = _Pm10001otu4AlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 168, 1, 17),
    _Pm10001otu4AlmLineRxOtnLofPortn_Type()
)
pm10001otu4AlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineRxOtnLofPortn.setStatus("current")
_Pm10001otu4AlmlineHostLaneTxOtnTable_Object = MibTable
pm10001otu4AlmlineHostLaneTxOtnTable = _Pm10001otu4AlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineHostLaneTxOtnTable.setStatus("current")
_Pm10001otu4AlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm10001otu4AlmlineHostLaneTxOtnEntry = _Pm10001otu4AlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1)
)
pm10001otu4AlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm10001otu4AlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm10001otu4AlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm10001otu4AlmlineHostLaneTxOtnIndex = _Pm10001otu4AlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 1),
    _Pm10001otu4AlmlineHostLaneTxOtnIndex_Type()
)
pm10001otu4AlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm10001otu4AlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnOduAisPortn = _Pm10001otu4AlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 10),
    _Pm10001otu4AlmLineTxOtnOduAisPortn_Type()
)
pm10001otu4AlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnOduAisPortn.setStatus("current")
_Pm10001otu4AlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnOtuAisPortn = _Pm10001otu4AlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 11),
    _Pm10001otu4AlmLineTxOtnOtuAisPortn_Type()
)
pm10001otu4AlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm10001otu4AlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxSmBdiPortn_Object = MibTableColumn
pm10001otu4AlmLineTxSmBdiPortn = _Pm10001otu4AlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 12),
    _Pm10001otu4AlmLineTxSmBdiPortn_Type()
)
pm10001otu4AlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxSmBdiPortn.setStatus("current")
_Pm10001otu4AlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnIaePortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnIaePortn = _Pm10001otu4AlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 13),
    _Pm10001otu4AlmLineTxOtnIaePortn_Type()
)
pm10001otu4AlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnIaePortn.setStatus("current")
_Pm10001otu4AlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnOomPortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnOomPortn = _Pm10001otu4AlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 14),
    _Pm10001otu4AlmLineTxOtnOomPortn_Type()
)
pm10001otu4AlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnOomPortn.setStatus("current")
_Pm10001otu4AlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnLomPortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnLomPortn = _Pm10001otu4AlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 15),
    _Pm10001otu4AlmLineTxOtnLomPortn_Type()
)
pm10001otu4AlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnLomPortn.setStatus("current")
_Pm10001otu4AlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnOofPortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnOofPortn = _Pm10001otu4AlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 16),
    _Pm10001otu4AlmLineTxOtnOofPortn_Type()
)
pm10001otu4AlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnOofPortn.setStatus("current")
_Pm10001otu4AlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm10001otu4AlmLineTxOtnLofPortn_Object = MibTableColumn
pm10001otu4AlmLineTxOtnLofPortn = _Pm10001otu4AlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 2, 184, 1, 17),
    _Pm10001otu4AlmLineTxOtnLofPortn_Type()
)
pm10001otu4AlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineTxOtnLofPortn.setStatus("current")
_Pm10001otu4AlmLineCrit_ObjectIdentity = ObjectIdentity
pm10001otu4AlmLineCrit = _Pm10001otu4AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3)
)
_Pm10001otu4AlmsynthAlmLineTable_Object = MibTable
pm10001otu4AlmsynthAlmLineTable = _Pm10001otu4AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pm10001otu4AlmsynthAlmLineTable.setStatus("current")
_Pm10001otu4AlmsynthAlmLineEntry_Object = MibTableRow
pm10001otu4AlmsynthAlmLineEntry = _Pm10001otu4AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1)
)
pm10001otu4AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4AlmsynthAlmLineEntry.setStatus("current")


class _Pm10001otu4AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm10001otu4AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm10001otu4AlmsynthAlmLineIndex_Object = MibTableColumn
pm10001otu4AlmsynthAlmLineIndex = _Pm10001otu4AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 1),
    _Pm10001otu4AlmsynthAlmLineIndex_Type()
)
pm10001otu4AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmsynthAlmLineIndex.setStatus("current")
_Pm10001otu4AlmXfpAbsentPortn_Type = EkiOnOff
_Pm10001otu4AlmXfpAbsentPortn_Object = MibTableColumn
pm10001otu4AlmXfpAbsentPortn = _Pm10001otu4AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 2),
    _Pm10001otu4AlmXfpAbsentPortn_Type()
)
pm10001otu4AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmXfpAbsentPortn.setStatus("current")
_Pm10001otu4AlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm10001otu4AlmXfpInitNotComplPortn_Object = MibTableColumn
pm10001otu4AlmXfpInitNotComplPortn = _Pm10001otu4AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 3),
    _Pm10001otu4AlmXfpInitNotComplPortn_Type()
)
pm10001otu4AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmXfpInitNotComplPortn.setStatus("current")
_Pm10001otu4AlmLineHwFailPortn_Type = EkiOnOff
_Pm10001otu4AlmLineHwFailPortn_Object = MibTableColumn
pm10001otu4AlmLineHwFailPortn = _Pm10001otu4AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 5),
    _Pm10001otu4AlmLineHwFailPortn_Type()
)
pm10001otu4AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineHwFailPortn.setStatus("current")
_Pm10001otu4AlmXfpTxOffPortn_Type = EkiOnOff
_Pm10001otu4AlmXfpTxOffPortn_Object = MibTableColumn
pm10001otu4AlmXfpTxOffPortn = _Pm10001otu4AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 6),
    _Pm10001otu4AlmXfpTxOffPortn_Type()
)
pm10001otu4AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmXfpTxOffPortn.setStatus("current")
_Pm10001otu4AlmLineLocalOosPortn_Type = EkiOnOff
_Pm10001otu4AlmLineLocalOosPortn_Object = MibTableColumn
pm10001otu4AlmLineLocalOosPortn = _Pm10001otu4AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 7),
    _Pm10001otu4AlmLineLocalOosPortn_Type()
)
pm10001otu4AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineLocalOosPortn.setStatus("current")
_Pm10001otu4AlmUpRdiInsPortn_Type = EkiOnOff
_Pm10001otu4AlmUpRdiInsPortn_Object = MibTableColumn
pm10001otu4AlmUpRdiInsPortn = _Pm10001otu4AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 9),
    _Pm10001otu4AlmUpRdiInsPortn_Type()
)
pm10001otu4AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmUpRdiInsPortn.setStatus("current")
_Pm10001otu4AlmLineDdmWarningPortn_Type = EkiOnOff
_Pm10001otu4AlmLineDdmWarningPortn_Object = MibTableColumn
pm10001otu4AlmLineDdmWarningPortn = _Pm10001otu4AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 10),
    _Pm10001otu4AlmLineDdmWarningPortn_Type()
)
pm10001otu4AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineDdmWarningPortn.setStatus("current")
_Pm10001otu4AlmLineDdmAlmPortn_Type = EkiOnOff
_Pm10001otu4AlmLineDdmAlmPortn_Object = MibTableColumn
pm10001otu4AlmLineDdmAlmPortn = _Pm10001otu4AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 11),
    _Pm10001otu4AlmLineDdmAlmPortn_Type()
)
pm10001otu4AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineDdmAlmPortn.setStatus("current")
_Pm10001otu4AlmLineFailPortn_Type = EkiOnOff
_Pm10001otu4AlmLineFailPortn_Object = MibTableColumn
pm10001otu4AlmLineFailPortn = _Pm10001otu4AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 13),
    _Pm10001otu4AlmLineFailPortn_Type()
)
pm10001otu4AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineFailPortn.setStatus("current")
_Pm10001otu4AlmLineActivePortn_Type = EkiOnOff
_Pm10001otu4AlmLineActivePortn_Object = MibTableColumn
pm10001otu4AlmLineActivePortn = _Pm10001otu4AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 2, 3, 3, 24, 1, 17),
    _Pm10001otu4AlmLineActivePortn_Type()
)
pm10001otu4AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4AlmLineActivePortn.setStatus("current")
_Pm10001otu4measures_ObjectIdentity = ObjectIdentity
pm10001otu4measures = _Pm10001otu4measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3)
)
_Pm10001otu4MesrOther_ObjectIdentity = ObjectIdentity
pm10001otu4MesrOther = _Pm10001otu4MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1)
)
_Pm10001otu4Mesrsynth0_Type = EkiMeasureType
_Pm10001otu4Mesrsynth0_Object = MibScalar
pm10001otu4Mesrsynth0 = _Pm10001otu4Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 0),
    _Pm10001otu4Mesrsynth0_Type()
)
pm10001otu4Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4Mesrsynth0.setStatus("deprecated")
_Pm10001otu4Mesrsynth1_Type = EkiMeasureType
_Pm10001otu4Mesrsynth1_Object = MibScalar
pm10001otu4Mesrsynth1 = _Pm10001otu4Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 1),
    _Pm10001otu4Mesrsynth1_Type()
)
pm10001otu4Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4Mesrsynth1.setStatus("deprecated")


class _Pm10001otu4MesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm10001otu4MesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrpmIntervalNumber_Object = MibScalar
pm10001otu4MesrpmIntervalNumber = _Pm10001otu4MesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 7),
    _Pm10001otu4MesrpmIntervalNumber_Type()
)
pm10001otu4MesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrpmIntervalNumber.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm10001otu4MesrlineNetTxLaserOutputPwrAverage = _Pm10001otu4MesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 180),
    _Pm10001otu4MesrlineNetTxLaserOutputPwrAverage_Type()
)
pm10001otu4MesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxLaserTempAverage_Object = MibScalar
pm10001otu4MesrlineNetTxLaserTempAverage = _Pm10001otu4MesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 181),
    _Pm10001otu4MesrlineNetTxLaserTempAverage_Type()
)
pm10001otu4MesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm10001otu4MesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm10001otu4MesrlineNetTxBiasCurrentAverage = _Pm10001otu4MesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 182),
    _Pm10001otu4MesrlineNetTxBiasCurrentAverage_Type()
)
pm10001otu4MesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm10001otu4MesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetRxInputPwrAverage_Object = MibScalar
pm10001otu4MesrlineNetRxInputPwrAverage = _Pm10001otu4MesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 183),
    _Pm10001otu4MesrlineNetRxInputPwrAverage_Type()
)
pm10001otu4MesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm10001otu4MesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineResidualChromaticDispAverage_Object = MibScalar
pm10001otu4MesrlineResidualChromaticDispAverage = _Pm10001otu4MesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 184),
    _Pm10001otu4MesrlineResidualChromaticDispAverage_Type()
)
pm10001otu4MesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm10001otu4MesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineDiffGroupDelayAverage_Object = MibScalar
pm10001otu4MesrlineDiffGroupDelayAverage = _Pm10001otu4MesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 185),
    _Pm10001otu4MesrlineDiffGroupDelayAverage_Type()
)
pm10001otu4MesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm10001otu4MesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineQFactorAverage_Object = MibScalar
pm10001otu4MesrlineQFactorAverage = _Pm10001otu4MesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 186),
    _Pm10001otu4MesrlineQFactorAverage_Type()
)
pm10001otu4MesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorAverage.setStatus("current")


class _Pm10001otu4MesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm10001otu4MesrlineCarrierFreqOffsetAverage = _Pm10001otu4MesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 187),
    _Pm10001otu4MesrlineCarrierFreqOffsetAverage_Type()
)
pm10001otu4MesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm10001otu4MesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineOsnrAverage_Object = MibScalar
pm10001otu4MesrlineOsnrAverage = _Pm10001otu4MesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 188),
    _Pm10001otu4MesrlineOsnrAverage_Type()
)
pm10001otu4MesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrAverage.setStatus("current")


class _Pm10001otu4MesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetTxTempMin_Object = MibScalar
pm10001otu4MesrclientNetTxTempMin = _Pm10001otu4MesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 192),
    _Pm10001otu4MesrclientNetTxTempMin_Type()
)
pm10001otu4MesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxTempMin.setStatus("current")


class _Pm10001otu4MesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetTxBiasMin_Object = MibScalar
pm10001otu4MesrclientNetTxBiasMin = _Pm10001otu4MesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 193),
    _Pm10001otu4MesrclientNetTxBiasMin_Type()
)
pm10001otu4MesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxBiasMin.setStatus("current")


class _Pm10001otu4MesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetTxPwrMin_Object = MibScalar
pm10001otu4MesrclientNetTxPwrMin = _Pm10001otu4MesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 194),
    _Pm10001otu4MesrclientNetTxPwrMin_Type()
)
pm10001otu4MesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxPwrMin.setStatus("current")


class _Pm10001otu4MesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetRxPwrMin_Object = MibScalar
pm10001otu4MesrclientNetRxPwrMin = _Pm10001otu4MesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 195),
    _Pm10001otu4MesrclientNetRxPwrMin_Type()
)
pm10001otu4MesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetRxPwrMin.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm10001otu4MesrlineNetTxLaserOutputPwrMin = _Pm10001otu4MesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 196),
    _Pm10001otu4MesrlineNetTxLaserOutputPwrMin_Type()
)
pm10001otu4MesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxLaserTempMin_Object = MibScalar
pm10001otu4MesrlineNetTxLaserTempMin = _Pm10001otu4MesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 197),
    _Pm10001otu4MesrlineNetTxLaserTempMin_Type()
)
pm10001otu4MesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempMin.setStatus("current")


class _Pm10001otu4MesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxBiasCurrentMin_Object = MibScalar
pm10001otu4MesrlineNetTxBiasCurrentMin = _Pm10001otu4MesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 198),
    _Pm10001otu4MesrlineNetTxBiasCurrentMin_Type()
)
pm10001otu4MesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm10001otu4MesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetRxInputPwrMin_Object = MibScalar
pm10001otu4MesrlineNetRxInputPwrMin = _Pm10001otu4MesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 199),
    _Pm10001otu4MesrlineNetRxInputPwrMin_Type()
)
pm10001otu4MesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrMin.setStatus("current")


class _Pm10001otu4MesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineResidualChromaticDispMin_Object = MibScalar
pm10001otu4MesrlineResidualChromaticDispMin = _Pm10001otu4MesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 200),
    _Pm10001otu4MesrlineResidualChromaticDispMin_Type()
)
pm10001otu4MesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispMin.setStatus("current")


class _Pm10001otu4MesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineDiffGroupDelayMin_Object = MibScalar
pm10001otu4MesrlineDiffGroupDelayMin = _Pm10001otu4MesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 201),
    _Pm10001otu4MesrlineDiffGroupDelayMin_Type()
)
pm10001otu4MesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayMin.setStatus("current")


class _Pm10001otu4MesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineQFactorMin_Object = MibScalar
pm10001otu4MesrlineQFactorMin = _Pm10001otu4MesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 202),
    _Pm10001otu4MesrlineQFactorMin_Type()
)
pm10001otu4MesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorMin.setStatus("current")


class _Pm10001otu4MesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineCarrierFreqOffsetMin_Object = MibScalar
pm10001otu4MesrlineCarrierFreqOffsetMin = _Pm10001otu4MesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 203),
    _Pm10001otu4MesrlineCarrierFreqOffsetMin_Type()
)
pm10001otu4MesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm10001otu4MesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineOsnrMin_Object = MibScalar
pm10001otu4MesrlineOsnrMin = _Pm10001otu4MesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 204),
    _Pm10001otu4MesrlineOsnrMin_Type()
)
pm10001otu4MesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrMin.setStatus("current")


class _Pm10001otu4MesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetTxTempMax_Object = MibScalar
pm10001otu4MesrclientNetTxTempMax = _Pm10001otu4MesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 208),
    _Pm10001otu4MesrclientNetTxTempMax_Type()
)
pm10001otu4MesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxTempMax.setStatus("current")


class _Pm10001otu4MesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetTxBiasMax_Object = MibScalar
pm10001otu4MesrclientNetTxBiasMax = _Pm10001otu4MesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 209),
    _Pm10001otu4MesrclientNetTxBiasMax_Type()
)
pm10001otu4MesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxBiasMax.setStatus("current")


class _Pm10001otu4MesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetTxPwrMax_Object = MibScalar
pm10001otu4MesrclientNetTxPwrMax = _Pm10001otu4MesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 210),
    _Pm10001otu4MesrclientNetTxPwrMax_Type()
)
pm10001otu4MesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxPwrMax.setStatus("current")


class _Pm10001otu4MesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientNetRxPwrMax_Object = MibScalar
pm10001otu4MesrclientNetRxPwrMax = _Pm10001otu4MesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 211),
    _Pm10001otu4MesrclientNetRxPwrMax_Type()
)
pm10001otu4MesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetRxPwrMax.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm10001otu4MesrlineNetTxLaserOutputPwrMax = _Pm10001otu4MesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 212),
    _Pm10001otu4MesrlineNetTxLaserOutputPwrMax_Type()
)
pm10001otu4MesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxLaserTempMax_Object = MibScalar
pm10001otu4MesrlineNetTxLaserTempMax = _Pm10001otu4MesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 213),
    _Pm10001otu4MesrlineNetTxLaserTempMax_Type()
)
pm10001otu4MesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempMax.setStatus("current")


class _Pm10001otu4MesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetTxBiasCurrentMax_Object = MibScalar
pm10001otu4MesrlineNetTxBiasCurrentMax = _Pm10001otu4MesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 214),
    _Pm10001otu4MesrlineNetTxBiasCurrentMax_Type()
)
pm10001otu4MesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm10001otu4MesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineNetRxInputPwrMax_Object = MibScalar
pm10001otu4MesrlineNetRxInputPwrMax = _Pm10001otu4MesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 215),
    _Pm10001otu4MesrlineNetRxInputPwrMax_Type()
)
pm10001otu4MesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrMax.setStatus("current")


class _Pm10001otu4MesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineResidualChromaticDispMax_Object = MibScalar
pm10001otu4MesrlineResidualChromaticDispMax = _Pm10001otu4MesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 216),
    _Pm10001otu4MesrlineResidualChromaticDispMax_Type()
)
pm10001otu4MesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispMax.setStatus("current")


class _Pm10001otu4MesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineDiffGroupDelayMax_Object = MibScalar
pm10001otu4MesrlineDiffGroupDelayMax = _Pm10001otu4MesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 217),
    _Pm10001otu4MesrlineDiffGroupDelayMax_Type()
)
pm10001otu4MesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayMax.setStatus("current")


class _Pm10001otu4MesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineQFactorMax_Object = MibScalar
pm10001otu4MesrlineQFactorMax = _Pm10001otu4MesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 218),
    _Pm10001otu4MesrlineQFactorMax_Type()
)
pm10001otu4MesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorMax.setStatus("current")


class _Pm10001otu4MesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineCarrierFreqOffsetMax_Object = MibScalar
pm10001otu4MesrlineCarrierFreqOffsetMax = _Pm10001otu4MesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 219),
    _Pm10001otu4MesrlineCarrierFreqOffsetMax_Type()
)
pm10001otu4MesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm10001otu4MesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineOsnrMax_Object = MibScalar
pm10001otu4MesrlineOsnrMax = _Pm10001otu4MesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 1, 220),
    _Pm10001otu4MesrlineOsnrMax_Type()
)
pm10001otu4MesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrMax.setStatus("current")
_Pm10001otu4MesrClient_ObjectIdentity = ObjectIdentity
pm10001otu4MesrClient = _Pm10001otu4MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2)
)


class _Pm10001otu4MesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientCfpTemp_Object = MibScalar
pm10001otu4MesrclientCfpTemp = _Pm10001otu4MesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 8),
    _Pm10001otu4MesrclientCfpTemp_Type()
)
pm10001otu4MesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientCfpTemp.setStatus("current")


class _Pm10001otu4MesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientCfp3v3Voltage_Object = MibScalar
pm10001otu4MesrclientCfp3v3Voltage = _Pm10001otu4MesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 9),
    _Pm10001otu4MesrclientCfp3v3Voltage_Type()
)
pm10001otu4MesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientCfp3v3Voltage.setStatus("current")


class _Pm10001otu4MesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10001otu4MesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrclientSoaBiasCurrent_Object = MibScalar
pm10001otu4MesrclientSoaBiasCurrent = _Pm10001otu4MesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 10),
    _Pm10001otu4MesrclientSoaBiasCurrent_Type()
)
pm10001otu4MesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientSoaBiasCurrent.setStatus("current")
_Pm10001otu4MesrclientNetTxTempTable_Object = MibTable
pm10001otu4MesrclientNetTxTempTable = _Pm10001otu4MesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxTempTable.setStatus("current")
_Pm10001otu4MesrclientNetTxTempEntry_Object = MibTableRow
pm10001otu4MesrclientNetTxTempEntry = _Pm10001otu4MesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 16, 1)
)
pm10001otu4MesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxTempEntry.setStatus("current")


class _Pm10001otu4MesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetTxTempIndex_Object = MibTableColumn
pm10001otu4MesrclientNetTxTempIndex = _Pm10001otu4MesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 16, 1, 1),
    _Pm10001otu4MesrclientNetTxTempIndex_Type()
)
pm10001otu4MesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxTempIndex.setStatus("current")


class _Pm10001otu4MesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetTxTempPortn_Object = MibTableColumn
pm10001otu4MesrclientNetTxTempPortn = _Pm10001otu4MesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 16, 1, 2),
    _Pm10001otu4MesrclientNetTxTempPortn_Type()
)
pm10001otu4MesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxTempPortn.setStatus("current")
_Pm10001otu4MesrclientNetTxBiasTable_Object = MibTable
pm10001otu4MesrclientNetTxBiasTable = _Pm10001otu4MesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxBiasTable.setStatus("current")
_Pm10001otu4MesrclientNetTxBiasEntry_Object = MibTableRow
pm10001otu4MesrclientNetTxBiasEntry = _Pm10001otu4MesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 32, 1)
)
pm10001otu4MesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxBiasEntry.setStatus("current")


class _Pm10001otu4MesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetTxBiasIndex_Object = MibTableColumn
pm10001otu4MesrclientNetTxBiasIndex = _Pm10001otu4MesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 32, 1, 1),
    _Pm10001otu4MesrclientNetTxBiasIndex_Type()
)
pm10001otu4MesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxBiasIndex.setStatus("current")


class _Pm10001otu4MesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetTxBiasPortn_Object = MibTableColumn
pm10001otu4MesrclientNetTxBiasPortn = _Pm10001otu4MesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 32, 1, 2),
    _Pm10001otu4MesrclientNetTxBiasPortn_Type()
)
pm10001otu4MesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxBiasPortn.setStatus("current")
_Pm10001otu4MesrclientNetTxPwrTable_Object = MibTable
pm10001otu4MesrclientNetTxPwrTable = _Pm10001otu4MesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxPwrTable.setStatus("current")
_Pm10001otu4MesrclientNetTxPwrEntry_Object = MibTableRow
pm10001otu4MesrclientNetTxPwrEntry = _Pm10001otu4MesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 48, 1)
)
pm10001otu4MesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxPwrEntry.setStatus("current")


class _Pm10001otu4MesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetTxPwrIndex_Object = MibTableColumn
pm10001otu4MesrclientNetTxPwrIndex = _Pm10001otu4MesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 48, 1, 1),
    _Pm10001otu4MesrclientNetTxPwrIndex_Type()
)
pm10001otu4MesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxPwrIndex.setStatus("current")


class _Pm10001otu4MesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetTxPwrPortn_Object = MibTableColumn
pm10001otu4MesrclientNetTxPwrPortn = _Pm10001otu4MesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 48, 1, 2),
    _Pm10001otu4MesrclientNetTxPwrPortn_Type()
)
pm10001otu4MesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetTxPwrPortn.setStatus("current")
_Pm10001otu4MesrclientNetRxPwrTable_Object = MibTable
pm10001otu4MesrclientNetRxPwrTable = _Pm10001otu4MesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetRxPwrTable.setStatus("current")
_Pm10001otu4MesrclientNetRxPwrEntry_Object = MibTableRow
pm10001otu4MesrclientNetRxPwrEntry = _Pm10001otu4MesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 64, 1)
)
pm10001otu4MesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetRxPwrEntry.setStatus("current")


class _Pm10001otu4MesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetRxPwrIndex_Object = MibTableColumn
pm10001otu4MesrclientNetRxPwrIndex = _Pm10001otu4MesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 64, 1, 1),
    _Pm10001otu4MesrclientNetRxPwrIndex_Type()
)
pm10001otu4MesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetRxPwrIndex.setStatus("current")


class _Pm10001otu4MesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pm10001otu4MesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrclientNetRxPwrPortn_Object = MibTableColumn
pm10001otu4MesrclientNetRxPwrPortn = _Pm10001otu4MesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 2, 64, 1, 2),
    _Pm10001otu4MesrclientNetRxPwrPortn_Type()
)
pm10001otu4MesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrclientNetRxPwrPortn.setStatus("current")
_Pm10001otu4MesrLine_ObjectIdentity = ObjectIdentity
pm10001otu4MesrLine = _Pm10001otu4MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3)
)


class _Pm10001otu4MesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineMsaTemp_Object = MibScalar
pm10001otu4MesrlineMsaTemp = _Pm10001otu4MesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 12),
    _Pm10001otu4MesrlineMsaTemp_Type()
)
pm10001otu4MesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineMsaTemp.setStatus("current")


class _Pm10001otu4MesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineMsa3v3Voltage_Object = MibScalar
pm10001otu4MesrlineMsa3v3Voltage = _Pm10001otu4MesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 13),
    _Pm10001otu4MesrlineMsa3v3Voltage_Type()
)
pm10001otu4MesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineMsa3v3Voltage.setStatus("current")


class _Pm10001otu4MesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10001otu4MesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10001otu4MesrlineSoaBiasCurrent_Object = MibScalar
pm10001otu4MesrlineSoaBiasCurrent = _Pm10001otu4MesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 14),
    _Pm10001otu4MesrlineSoaBiasCurrent_Type()
)
pm10001otu4MesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineSoaBiasCurrent.setStatus("current")
_Pm10001otu4MesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm10001otu4MesrlineNetTxLaserOutputPwrTable = _Pm10001otu4MesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm10001otu4MesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm10001otu4MesrlineNetTxLaserOutputPwrEntry = _Pm10001otu4MesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 80, 1)
)
pm10001otu4MesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm10001otu4MesrlineNetTxLaserOutputPwrIndex = _Pm10001otu4MesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 80, 1, 1),
    _Pm10001otu4MesrlineNetTxLaserOutputPwrIndex_Type()
)
pm10001otu4MesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm10001otu4MesrlineNetTxLaserOutputPwrPortn = _Pm10001otu4MesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 80, 1, 2),
    _Pm10001otu4MesrlineNetTxLaserOutputPwrPortn_Type()
)
pm10001otu4MesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm10001otu4MesrlineNetTxLaserTempTable_Object = MibTable
pm10001otu4MesrlineNetTxLaserTempTable = _Pm10001otu4MesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempTable.setStatus("current")
_Pm10001otu4MesrlineNetTxLaserTempEntry_Object = MibTableRow
pm10001otu4MesrlineNetTxLaserTempEntry = _Pm10001otu4MesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 96, 1)
)
pm10001otu4MesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm10001otu4MesrlineNetTxLaserTempIndex = _Pm10001otu4MesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 96, 1, 1),
    _Pm10001otu4MesrlineNetTxLaserTempIndex_Type()
)
pm10001otu4MesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm10001otu4MesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm10001otu4MesrlineNetTxLaserTempPortn = _Pm10001otu4MesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 96, 1, 2),
    _Pm10001otu4MesrlineNetTxLaserTempPortn_Type()
)
pm10001otu4MesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxLaserTempPortn.setStatus("current")
_Pm10001otu4MesrlineNetTxBiasCurrentTable_Object = MibTable
pm10001otu4MesrlineNetTxBiasCurrentTable = _Pm10001otu4MesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm10001otu4MesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm10001otu4MesrlineNetTxBiasCurrentEntry = _Pm10001otu4MesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 112, 1)
)
pm10001otu4MesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm10001otu4MesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm10001otu4MesrlineNetTxBiasCurrentIndex = _Pm10001otu4MesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 112, 1, 1),
    _Pm10001otu4MesrlineNetTxBiasCurrentIndex_Type()
)
pm10001otu4MesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm10001otu4MesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm10001otu4MesrlineNetTxBiasCurrentPortn = _Pm10001otu4MesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 112, 1, 2),
    _Pm10001otu4MesrlineNetTxBiasCurrentPortn_Type()
)
pm10001otu4MesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm10001otu4MesrlineNetRxInputPwrTable_Object = MibTable
pm10001otu4MesrlineNetRxInputPwrTable = _Pm10001otu4MesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrTable.setStatus("current")
_Pm10001otu4MesrlineNetRxInputPwrEntry_Object = MibTableRow
pm10001otu4MesrlineNetRxInputPwrEntry = _Pm10001otu4MesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 128, 1)
)
pm10001otu4MesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm10001otu4MesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm10001otu4MesrlineNetRxInputPwrIndex = _Pm10001otu4MesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 128, 1, 1),
    _Pm10001otu4MesrlineNetRxInputPwrIndex_Type()
)
pm10001otu4MesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm10001otu4MesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm10001otu4MesrlineNetRxInputPwrPortn = _Pm10001otu4MesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 128, 1, 2),
    _Pm10001otu4MesrlineNetRxInputPwrPortn_Type()
)
pm10001otu4MesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineNetRxInputPwrPortn.setStatus("current")
_Pm10001otu4MesrlineResidualChromaticDispTable_Object = MibTable
pm10001otu4MesrlineResidualChromaticDispTable = _Pm10001otu4MesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispTable.setStatus("current")
_Pm10001otu4MesrlineResidualChromaticDispEntry_Object = MibTableRow
pm10001otu4MesrlineResidualChromaticDispEntry = _Pm10001otu4MesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 144, 1)
)
pm10001otu4MesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm10001otu4MesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm10001otu4MesrlineResidualChromaticDispIndex = _Pm10001otu4MesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 144, 1, 1),
    _Pm10001otu4MesrlineResidualChromaticDispIndex_Type()
)
pm10001otu4MesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm10001otu4MesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm10001otu4MesrlineResidualChromaticDispPortn = _Pm10001otu4MesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 144, 1, 2),
    _Pm10001otu4MesrlineResidualChromaticDispPortn_Type()
)
pm10001otu4MesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineResidualChromaticDispPortn.setStatus("current")
_Pm10001otu4MesrlineDiffGroupDelayTable_Object = MibTable
pm10001otu4MesrlineDiffGroupDelayTable = _Pm10001otu4MesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayTable.setStatus("current")
_Pm10001otu4MesrlineDiffGroupDelayEntry_Object = MibTableRow
pm10001otu4MesrlineDiffGroupDelayEntry = _Pm10001otu4MesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 148, 1)
)
pm10001otu4MesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm10001otu4MesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm10001otu4MesrlineDiffGroupDelayIndex = _Pm10001otu4MesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 148, 1, 1),
    _Pm10001otu4MesrlineDiffGroupDelayIndex_Type()
)
pm10001otu4MesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm10001otu4MesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm10001otu4MesrlineDiffGroupDelayPortn = _Pm10001otu4MesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 148, 1, 2),
    _Pm10001otu4MesrlineDiffGroupDelayPortn_Type()
)
pm10001otu4MesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineDiffGroupDelayPortn.setStatus("current")
_Pm10001otu4MesrlineQFactorTable_Object = MibTable
pm10001otu4MesrlineQFactorTable = _Pm10001otu4MesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorTable.setStatus("current")
_Pm10001otu4MesrlineQFactorEntry_Object = MibTableRow
pm10001otu4MesrlineQFactorEntry = _Pm10001otu4MesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 152, 1)
)
pm10001otu4MesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorEntry.setStatus("current")


class _Pm10001otu4MesrlineQFactorIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineQFactorIndex_Object = MibTableColumn
pm10001otu4MesrlineQFactorIndex = _Pm10001otu4MesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 152, 1, 1),
    _Pm10001otu4MesrlineQFactorIndex_Type()
)
pm10001otu4MesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorIndex.setStatus("current")


class _Pm10001otu4MesrlineQFactorPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineQFactorPortn_Object = MibTableColumn
pm10001otu4MesrlineQFactorPortn = _Pm10001otu4MesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 152, 1, 2),
    _Pm10001otu4MesrlineQFactorPortn_Type()
)
pm10001otu4MesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineQFactorPortn.setStatus("current")
_Pm10001otu4MesrlineCarrierFreqOffsetTable_Object = MibTable
pm10001otu4MesrlineCarrierFreqOffsetTable = _Pm10001otu4MesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm10001otu4MesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm10001otu4MesrlineCarrierFreqOffsetEntry = _Pm10001otu4MesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 156, 1)
)
pm10001otu4MesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm10001otu4MesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm10001otu4MesrlineCarrierFreqOffsetIndex = _Pm10001otu4MesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 156, 1, 1),
    _Pm10001otu4MesrlineCarrierFreqOffsetIndex_Type()
)
pm10001otu4MesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm10001otu4MesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm10001otu4MesrlineCarrierFreqOffsetPortn = _Pm10001otu4MesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 156, 1, 2),
    _Pm10001otu4MesrlineCarrierFreqOffsetPortn_Type()
)
pm10001otu4MesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm10001otu4MesrlineOsnrTable_Object = MibTable
pm10001otu4MesrlineOsnrTable = _Pm10001otu4MesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrTable.setStatus("current")
_Pm10001otu4MesrlineOsnrEntry_Object = MibTableRow
pm10001otu4MesrlineOsnrEntry = _Pm10001otu4MesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 160, 1)
)
pm10001otu4MesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrEntry.setStatus("current")


class _Pm10001otu4MesrlineOsnrIndex_Type(Integer32):
    """Custom type pm10001otu4MesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineOsnrIndex_Object = MibTableColumn
pm10001otu4MesrlineOsnrIndex = _Pm10001otu4MesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 160, 1, 1),
    _Pm10001otu4MesrlineOsnrIndex_Type()
)
pm10001otu4MesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrIndex.setStatus("current")


class _Pm10001otu4MesrlineOsnrPortn_Type(Integer32):
    """Custom type pm10001otu4MesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10001otu4MesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm10001otu4MesrlineOsnrPortn_Object = MibTableColumn
pm10001otu4MesrlineOsnrPortn = _Pm10001otu4MesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 3, 3, 160, 1, 2),
    _Pm10001otu4MesrlineOsnrPortn_Type()
)
pm10001otu4MesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MesrlineOsnrPortn.setStatus("current")
_Pm10001otu4counters_ObjectIdentity = ObjectIdentity
pm10001otu4counters = _Pm10001otu4counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4)
)
_Pm10001otu4CntOther_ObjectIdentity = ObjectIdentity
pm10001otu4CntOther = _Pm10001otu4CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 1)
)
_Pm10001otu4CntClient_ObjectIdentity = ObjectIdentity
pm10001otu4CntClient = _Pm10001otu4CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2)
)
_Pm10001otu4CntclientInputErrorCounterLaneOneTable_Object = MibTable
pm10001otu4CntclientInputErrorCounterLaneOneTable = _Pm10001otu4CntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneOneTable.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
pm10001otu4CntclientInputErrorCounterLaneOneEntry = _Pm10001otu4CntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 16, 1)
)
pm10001otu4CntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Pm10001otu4CntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type pm10001otu4CntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneOneIndex = _Pm10001otu4CntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 16, 1, 1),
    _Pm10001otu4CntclientInputErrorCounterLaneOneIndex_Type()
)
pm10001otu4CntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Pm10001otu4CntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneOneValuePortn = _Pm10001otu4CntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 16, 1, 2),
    _Pm10001otu4CntclientInputErrorCounterLaneOneValuePortn_Type()
)
pm10001otu4CntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn = _Pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 16, 1, 3),
    _Pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn_Type()
)
pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn = _Pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 16, 1, 4),
    _Pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneTwoTable_Object = MibTable
pm10001otu4CntclientInputErrorCounterLaneTwoTable = _Pm10001otu4CntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
pm10001otu4CntclientInputErrorCounterLaneTwoEntry = _Pm10001otu4CntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 32, 1)
)
pm10001otu4CntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Pm10001otu4CntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type pm10001otu4CntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneTwoIndex = _Pm10001otu4CntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 32, 1, 1),
    _Pm10001otu4CntclientInputErrorCounterLaneTwoIndex_Type()
)
pm10001otu4CntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn = _Pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 32, 1, 2),
    _Pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn_Type()
)
pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn = _Pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 32, 1, 3),
    _Pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn = _Pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 32, 1, 4),
    _Pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterTable_Object = MibTable
pm10001otu4CntclientInputErrorCounterTable = _Pm10001otu4CntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 80)
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterTable.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterEntry_Object = MibTableRow
pm10001otu4CntclientInputErrorCounterEntry = _Pm10001otu4CntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 80, 1)
)
pm10001otu4CntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterEntry.setStatus("current")


class _Pm10001otu4CntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntclientInputErrorCounterIndex_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterIndex = _Pm10001otu4CntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 80, 1, 1),
    _Pm10001otu4CntclientInputErrorCounterIndex_Type()
)
pm10001otu4CntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterIndex.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterValuePortn_Type = Counter32
_Pm10001otu4CntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterValuePortn = _Pm10001otu4CntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 80, 1, 2),
    _Pm10001otu4CntclientInputErrorCounterValuePortn_Type()
)
pm10001otu4CntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterValuePortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterErrorPortn = _Pm10001otu4CntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 80, 1, 3),
    _Pm10001otu4CntclientInputErrorCounterErrorPortn_Type()
)
pm10001otu4CntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm10001otu4CntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntclientInputErrorCounterOverloadPortn = _Pm10001otu4CntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 80, 1, 4),
    _Pm10001otu4CntclientInputErrorCounterOverloadPortn_Type()
)
pm10001otu4CntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm10001otu4CntclientCbipCounterTable_Object = MibTable
pm10001otu4CntclientCbipCounterTable = _Pm10001otu4CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientCbipCounterTable.setStatus("current")
_Pm10001otu4CntclientCbipCounterEntry_Object = MibTableRow
pm10001otu4CntclientCbipCounterEntry = _Pm10001otu4CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 96, 1)
)
pm10001otu4CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntclientCbipCounterEntry.setStatus("current")


class _Pm10001otu4CntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntclientCbipCounterIndex_Object = MibTableColumn
pm10001otu4CntclientCbipCounterIndex = _Pm10001otu4CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 96, 1, 1),
    _Pm10001otu4CntclientCbipCounterIndex_Type()
)
pm10001otu4CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientCbipCounterIndex.setStatus("current")
_Pm10001otu4CntclientCbipCounterValuePortn_Type = Counter32
_Pm10001otu4CntclientCbipCounterValuePortn_Object = MibTableColumn
pm10001otu4CntclientCbipCounterValuePortn = _Pm10001otu4CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 96, 1, 2),
    _Pm10001otu4CntclientCbipCounterValuePortn_Type()
)
pm10001otu4CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientCbipCounterValuePortn.setStatus("current")
_Pm10001otu4CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntclientCbipCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntclientCbipCounterErrorPortn = _Pm10001otu4CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 96, 1, 3),
    _Pm10001otu4CntclientCbipCounterErrorPortn_Type()
)
pm10001otu4CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientCbipCounterErrorPortn.setStatus("current")
_Pm10001otu4CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntclientCbipCounterOverloadPortn = _Pm10001otu4CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 2, 96, 1, 4),
    _Pm10001otu4CntclientCbipCounterOverloadPortn_Type()
)
pm10001otu4CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntclientCbipCounterOverloadPortn.setStatus("current")
_Pm10001otu4CntLine_ObjectIdentity = ObjectIdentity
pm10001otu4CntLine = _Pm10001otu4CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3)
)
_Pm10001otu4CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm10001otu4CntlocalLineSmBip8ErrorCounterTable = _Pm10001otu4CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10001otu4CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10001otu4CntlocalLineSmBip8ErrorCounterEntry = _Pm10001otu4CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 192, 1)
)
pm10001otu4CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10001otu4CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10001otu4CntlocalLineSmBip8ErrorCounterIndex = _Pm10001otu4CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 192, 1, 1),
    _Pm10001otu4CntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm10001otu4CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn = _Pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 192, 1, 2),
    _Pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn = _Pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 192, 1, 3),
    _Pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 192, 1, 4),
    _Pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm10001otu4CntlocalLineFecCorrectedErrorsCounterTable = _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry = _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 193, 1)
)
pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex = _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 193, 1, 1),
    _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 193, 1, 2),
    _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 193, 1, 3),
    _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 193, 1, 4),
    _Pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm10001otu4CntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm10001otu4CntremoteLineSmBip8ErrorCounterTable = _Pm10001otu4CntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm10001otu4CntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10001otu4CntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10001otu4CntremoteLineSmBip8ErrorCounterEntry = _Pm10001otu4CntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 194, 1)
)
pm10001otu4CntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10001otu4CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10001otu4CntremoteLineSmBip8ErrorCounterIndex = _Pm10001otu4CntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 194, 1, 1),
    _Pm10001otu4CntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm10001otu4CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn = _Pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 194, 1, 2),
    _Pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn = _Pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 194, 1, 3),
    _Pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 194, 1, 4),
    _Pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10001otu4CntlineDfrmTimCntTable_Object = MibTable
pm10001otu4CntlineDfrmTimCntTable = _Pm10001otu4CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm10001otu4CntlineDfrmTimCntTable.setStatus("current")
_Pm10001otu4CntlineDfrmTimCntEntry_Object = MibTableRow
pm10001otu4CntlineDfrmTimCntEntry = _Pm10001otu4CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 195, 1)
)
pm10001otu4CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntlineDfrmTimCntEntry.setStatus("current")


class _Pm10001otu4CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm10001otu4CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntlineDfrmTimCntIndex_Object = MibTableColumn
pm10001otu4CntlineDfrmTimCntIndex = _Pm10001otu4CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 195, 1, 1),
    _Pm10001otu4CntlineDfrmTimCntIndex_Type()
)
pm10001otu4CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlineDfrmTimCntIndex.setStatus("current")
_Pm10001otu4CntlineDfrmTimCntValuePortn_Type = Counter64
_Pm10001otu4CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm10001otu4CntlineDfrmTimCntValuePortn = _Pm10001otu4CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 195, 1, 2),
    _Pm10001otu4CntlineDfrmTimCntValuePortn_Type()
)
pm10001otu4CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlineDfrmTimCntValuePortn.setStatus("current")
_Pm10001otu4CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm10001otu4CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm10001otu4CntlineDfrmTimCntErrorPortn = _Pm10001otu4CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 195, 1, 3),
    _Pm10001otu4CntlineDfrmTimCntErrorPortn_Type()
)
pm10001otu4CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm10001otu4CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm10001otu4CntlineDfrmTimCntOverloadPortn = _Pm10001otu4CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 195, 1, 4),
    _Pm10001otu4CntlineDfrmTimCntOverloadPortn_Type()
)
pm10001otu4CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterTable = _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry = _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 196, 1)
)
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex = _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 196, 1, 1),
    _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 196, 1, 2),
    _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 196, 1, 3),
    _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 196, 1, 4),
    _Pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterTable = _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 197, 1)
)
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 197, 1, 1),
    _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 197, 1, 2),
    _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 197, 1, 3),
    _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 4, 3, 197, 1, 4),
    _Pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10001otu4controlsWrite_ObjectIdentity = ObjectIdentity
pm10001otu4controlsWrite = _Pm10001otu4controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6)
)
_Pm10001otu4CtrlOther_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlOther = _Pm10001otu4CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1)
)
_Pm10001otu4CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlconfMgnt1 = _Pm10001otu4CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 1)
)
_Pm10001otu4CtrlConf1Load1_Type = EkiOnOff
_Pm10001otu4CtrlConf1Load1_Object = MibScalar
pm10001otu4CtrlConf1Load1 = _Pm10001otu4CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 1, 1),
    _Pm10001otu4CtrlConf1Load1_Type()
)
pm10001otu4CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlConf1Load1.setStatus("current")
_Pm10001otu4CtrlConf2Load1_Type = EkiOnOff
_Pm10001otu4CtrlConf2Load1_Object = MibScalar
pm10001otu4CtrlConf2Load1 = _Pm10001otu4CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 1, 2),
    _Pm10001otu4CtrlConf2Load1_Type()
)
pm10001otu4CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlConf2Load1.setStatus("current")
_Pm10001otu4CtrlConf2Flash1_Type = EkiOnOff
_Pm10001otu4CtrlConf2Flash1_Object = MibScalar
pm10001otu4CtrlConf2Flash1 = _Pm10001otu4CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 1, 10),
    _Pm10001otu4CtrlConf2Flash1_Type()
)
pm10001otu4CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlConf2Flash1.setStatus("current")
_Pm10001otu4CtrlConf2Clear1_Type = EkiOnOff
_Pm10001otu4CtrlConf2Clear1_Object = MibScalar
pm10001otu4CtrlConf2Clear1 = _Pm10001otu4CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 1, 14),
    _Pm10001otu4CtrlConf2Clear1_Type()
)
pm10001otu4CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlConf2Clear1.setStatus("current")
_Pm10001otu4Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm10001otu4Ctrlsynth4 = _Pm10001otu4Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 4)
)
_Pm10001otu4CtrlCorrelatOn_Type = EkiOnOff
_Pm10001otu4CtrlCorrelatOn_Object = MibScalar
pm10001otu4CtrlCorrelatOn = _Pm10001otu4CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 4, 1),
    _Pm10001otu4CtrlCorrelatOn_Type()
)
pm10001otu4CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlCorrelatOn.setStatus("current")
_Pm10001otu4CtrlCorrelatOff_Type = EkiOnOff
_Pm10001otu4CtrlCorrelatOff_Object = MibScalar
pm10001otu4CtrlCorrelatOff = _Pm10001otu4CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 4, 2),
    _Pm10001otu4CtrlCorrelatOff_Type()
)
pm10001otu4CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlCorrelatOff.setStatus("current")
_Pm10001otu4CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlswMgnt = _Pm10001otu4CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 5)
)
_Pm10001otu4CtrlColdReset_Type = EkiOnOff
_Pm10001otu4CtrlColdReset_Object = MibScalar
pm10001otu4CtrlColdReset = _Pm10001otu4CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 5, 2),
    _Pm10001otu4CtrlColdReset_Type()
)
pm10001otu4CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlColdReset.setStatus("current")
_Pm10001otu4CtrlWarmReset_Type = EkiOnOff
_Pm10001otu4CtrlWarmReset_Object = MibScalar
pm10001otu4CtrlWarmReset = _Pm10001otu4CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 5, 3),
    _Pm10001otu4CtrlWarmReset_Type()
)
pm10001otu4CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlWarmReset.setStatus("current")
_Pm10001otu4CtrlLoadSwBank1_Type = EkiOnOff
_Pm10001otu4CtrlLoadSwBank1_Object = MibScalar
pm10001otu4CtrlLoadSwBank1 = _Pm10001otu4CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 5, 5),
    _Pm10001otu4CtrlLoadSwBank1_Type()
)
pm10001otu4CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLoadSwBank1.setStatus("current")
_Pm10001otu4CtrlLoadSwBank2_Type = EkiOnOff
_Pm10001otu4CtrlLoadSwBank2_Object = MibScalar
pm10001otu4CtrlLoadSwBank2 = _Pm10001otu4CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 5, 6),
    _Pm10001otu4CtrlLoadSwBank2_Type()
)
pm10001otu4CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLoadSwBank2.setStatus("current")
_Pm10001otu4CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlgwMgnt = _Pm10001otu4CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 6)
)
_Pm10001otu4CtrlCurrentGwReset_Type = EkiOnOff
_Pm10001otu4CtrlCurrentGwReset_Object = MibScalar
pm10001otu4CtrlCurrentGwReset = _Pm10001otu4CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 6, 1),
    _Pm10001otu4CtrlCurrentGwReset_Type()
)
pm10001otu4CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlCurrentGwReset.setStatus("current")
_Pm10001otu4CtrlLoadGwBank1_Type = EkiOnOff
_Pm10001otu4CtrlLoadGwBank1_Object = MibScalar
pm10001otu4CtrlLoadGwBank1 = _Pm10001otu4CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 6, 5),
    _Pm10001otu4CtrlLoadGwBank1_Type()
)
pm10001otu4CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLoadGwBank1.setStatus("current")
_Pm10001otu4CtrlLoadGwBank2_Type = EkiOnOff
_Pm10001otu4CtrlLoadGwBank2_Object = MibScalar
pm10001otu4CtrlLoadGwBank2 = _Pm10001otu4CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 6, 6),
    _Pm10001otu4CtrlLoadGwBank2_Type()
)
pm10001otu4CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLoadGwBank2.setStatus("current")
_Pm10001otu4CtrlLoadGwBank3_Type = EkiOnOff
_Pm10001otu4CtrlLoadGwBank3_Object = MibScalar
pm10001otu4CtrlLoadGwBank3 = _Pm10001otu4CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 6, 7),
    _Pm10001otu4CtrlLoadGwBank3_Type()
)
pm10001otu4CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLoadGwBank3.setStatus("current")
_Pm10001otu4CtrlLoadGwBank4_Type = EkiOnOff
_Pm10001otu4CtrlLoadGwBank4_Object = MibScalar
pm10001otu4CtrlLoadGwBank4 = _Pm10001otu4CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 6, 8),
    _Pm10001otu4CtrlLoadGwBank4_Type()
)
pm10001otu4CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLoadGwBank4.setStatus("current")
_Pm10001otu4CtrlledTest_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlledTest = _Pm10001otu4CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 192)
)
_Pm10001otu4CtrlGreenLed_Type = EkiOnOff
_Pm10001otu4CtrlGreenLed_Object = MibScalar
pm10001otu4CtrlGreenLed = _Pm10001otu4CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 192, 1),
    _Pm10001otu4CtrlGreenLed_Type()
)
pm10001otu4CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlGreenLed.setStatus("current")
_Pm10001otu4CtrlRedLed_Type = EkiOnOff
_Pm10001otu4CtrlRedLed_Object = MibScalar
pm10001otu4CtrlRedLed = _Pm10001otu4CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 192, 2),
    _Pm10001otu4CtrlRedLed_Type()
)
pm10001otu4CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlRedLed.setStatus("current")
_Pm10001otu4CtrlLedOff_Type = EkiOnOff
_Pm10001otu4CtrlLedOff_Object = MibScalar
pm10001otu4CtrlLedOff = _Pm10001otu4CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 192, 3),
    _Pm10001otu4CtrlLedOff_Type()
)
pm10001otu4CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlLedOff.setStatus("current")
_Pm10001otu4CtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlinitSwitchMarvell = _Pm10001otu4CtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 201)
)
_Pm10001otu4CtrlInitSwitchMarvell_Type = EkiOnOff
_Pm10001otu4CtrlInitSwitchMarvell_Object = MibScalar
pm10001otu4CtrlInitSwitchMarvell = _Pm10001otu4CtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 201, 1),
    _Pm10001otu4CtrlInitSwitchMarvell_Type()
)
pm10001otu4CtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlInitSwitchMarvell.setStatus("current")
_Pm10001otu4CtrlresetCount_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlresetCount = _Pm10001otu4CtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 259)
)
_Pm10001otu4CtrlResetcount_Type = EkiOnOff
_Pm10001otu4CtrlResetcount_Object = MibScalar
pm10001otu4CtrlResetcount = _Pm10001otu4CtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 259, 1),
    _Pm10001otu4CtrlResetcount_Type()
)
pm10001otu4CtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlResetcount.setStatus("current")
_Pm10001otu4CtrlresetRmon_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlresetRmon = _Pm10001otu4CtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 260)
)
_Pm10001otu4CtrlResetrmon_Type = EkiOnOff
_Pm10001otu4CtrlResetrmon_Object = MibScalar
pm10001otu4CtrlResetrmon = _Pm10001otu4CtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 260, 1),
    _Pm10001otu4CtrlResetrmon_Type()
)
pm10001otu4CtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlResetrmon.setStatus("current")
_Pm10001otu4CtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlresetMeasurements = _Pm10001otu4CtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 261)
)
_Pm10001otu4CtrlResetmeasurements_Type = EkiOnOff
_Pm10001otu4CtrlResetmeasurements_Object = MibScalar
pm10001otu4CtrlResetmeasurements = _Pm10001otu4CtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 1, 261, 1),
    _Pm10001otu4CtrlResetmeasurements_Type()
)
pm10001otu4CtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlResetmeasurements.setStatus("current")
_Pm10001otu4CtrlClient_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlClient = _Pm10001otu4CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2)
)
_Pm10001otu4CtrlaccessLoopTable_Object = MibTable
pm10001otu4CtrlaccessLoopTable = _Pm10001otu4CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlaccessLoopTable.setStatus("current")
_Pm10001otu4CtrlaccessLoopEntry_Object = MibTableRow
pm10001otu4CtrlaccessLoopEntry = _Pm10001otu4CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 16, 1)
)
pm10001otu4CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlaccessLoopEntry.setStatus("current")


class _Pm10001otu4CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlaccessLoopIndex_Object = MibTableColumn
pm10001otu4CtrlaccessLoopIndex = _Pm10001otu4CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 16, 1, 1),
    _Pm10001otu4CtrlaccessLoopIndex_Type()
)
pm10001otu4CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlaccessLoopIndex.setStatus("current")
_Pm10001otu4CtrlaccessLoopPortn_Type = EkiState
_Pm10001otu4CtrlaccessLoopPortn_Object = MibTableColumn
pm10001otu4CtrlaccessLoopPortn = _Pm10001otu4CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 16, 1, 2),
    _Pm10001otu4CtrlaccessLoopPortn_Type()
)
pm10001otu4CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlaccessLoopPortn.setStatus("current")
_Pm10001otu4CtrlclientLoopToLineTable_Object = MibTable
pm10001otu4CtrlclientLoopToLineTable = _Pm10001otu4CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientLoopToLineTable.setStatus("current")
_Pm10001otu4CtrlclientLoopToLineEntry_Object = MibTableRow
pm10001otu4CtrlclientLoopToLineEntry = _Pm10001otu4CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 17, 1)
)
pm10001otu4CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientLoopToLineEntry.setStatus("current")


class _Pm10001otu4CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlclientLoopToLineIndex_Object = MibTableColumn
pm10001otu4CtrlclientLoopToLineIndex = _Pm10001otu4CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 17, 1, 1),
    _Pm10001otu4CtrlclientLoopToLineIndex_Type()
)
pm10001otu4CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientLoopToLineIndex.setStatus("current")
_Pm10001otu4CtrlclientLoopToLinePortn_Type = EkiState
_Pm10001otu4CtrlclientLoopToLinePortn_Object = MibTableColumn
pm10001otu4CtrlclientLoopToLinePortn = _Pm10001otu4CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 17, 1, 2),
    _Pm10001otu4CtrlclientLoopToLinePortn_Type()
)
pm10001otu4CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientLoopToLinePortn.setStatus("current")
_Pm10001otu4CtrlcsfUpInsTable_Object = MibTable
pm10001otu4CtrlcsfUpInsTable = _Pm10001otu4CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlcsfUpInsTable.setStatus("current")
_Pm10001otu4CtrlcsfUpInsEntry_Object = MibTableRow
pm10001otu4CtrlcsfUpInsEntry = _Pm10001otu4CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 21, 1)
)
pm10001otu4CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlcsfUpInsEntry.setStatus("current")


class _Pm10001otu4CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlcsfUpInsIndex_Object = MibTableColumn
pm10001otu4CtrlcsfUpInsIndex = _Pm10001otu4CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 21, 1, 1),
    _Pm10001otu4CtrlcsfUpInsIndex_Type()
)
pm10001otu4CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlcsfUpInsIndex.setStatus("current")
_Pm10001otu4CtrlcsfUpInsPortn_Type = EkiState
_Pm10001otu4CtrlcsfUpInsPortn_Object = MibTableColumn
pm10001otu4CtrlcsfUpInsPortn = _Pm10001otu4CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 21, 1, 2),
    _Pm10001otu4CtrlcsfUpInsPortn_Type()
)
pm10001otu4CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlcsfUpInsPortn.setStatus("current")
_Pm10001otu4CtrlcaisDwInsTable_Object = MibTable
pm10001otu4CtrlcaisDwInsTable = _Pm10001otu4CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlcaisDwInsTable.setStatus("current")
_Pm10001otu4CtrlcaisDwInsEntry_Object = MibTableRow
pm10001otu4CtrlcaisDwInsEntry = _Pm10001otu4CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 22, 1)
)
pm10001otu4CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlcaisDwInsEntry.setStatus("current")


class _Pm10001otu4CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlcaisDwInsIndex_Object = MibTableColumn
pm10001otu4CtrlcaisDwInsIndex = _Pm10001otu4CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 22, 1, 1),
    _Pm10001otu4CtrlcaisDwInsIndex_Type()
)
pm10001otu4CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlcaisDwInsIndex.setStatus("current")
_Pm10001otu4CtrlcaisDwInsPortn_Type = EkiState
_Pm10001otu4CtrlcaisDwInsPortn_Object = MibTableColumn
pm10001otu4CtrlcaisDwInsPortn = _Pm10001otu4CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 22, 1, 2),
    _Pm10001otu4CtrlcaisDwInsPortn_Type()
)
pm10001otu4CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlcaisDwInsPortn.setStatus("current")
_Pm10001otu4CtrlclientResetAllCountTable_Object = MibTable
pm10001otu4CtrlclientResetAllCountTable = _Pm10001otu4CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientResetAllCountTable.setStatus("current")
_Pm10001otu4CtrlclientResetAllCountEntry_Object = MibTableRow
pm10001otu4CtrlclientResetAllCountEntry = _Pm10001otu4CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 262, 1)
)
pm10001otu4CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientResetAllCountEntry.setStatus("current")


class _Pm10001otu4CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlclientResetAllCountIndex_Object = MibTableColumn
pm10001otu4CtrlclientResetAllCountIndex = _Pm10001otu4CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 262, 1, 1),
    _Pm10001otu4CtrlclientResetAllCountIndex_Type()
)
pm10001otu4CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientResetAllCountIndex.setStatus("current")
_Pm10001otu4CtrlclientResetAllCountsPortn_Type = EkiState
_Pm10001otu4CtrlclientResetAllCountsPortn_Object = MibTableColumn
pm10001otu4CtrlclientResetAllCountsPortn = _Pm10001otu4CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 2, 262, 1, 2),
    _Pm10001otu4CtrlclientResetAllCountsPortn_Type()
)
pm10001otu4CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlclientResetAllCountsPortn.setStatus("current")
_Pm10001otu4CtrlLine_ObjectIdentity = ObjectIdentity
pm10001otu4CtrlLine = _Pm10001otu4CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3)
)
_Pm10001otu4CtrlcommAccessLoopTable_Object = MibTable
pm10001otu4CtrlcommAccessLoopTable = _Pm10001otu4CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlcommAccessLoopTable.setStatus("current")
_Pm10001otu4CtrlcommAccessLoopEntry_Object = MibTableRow
pm10001otu4CtrlcommAccessLoopEntry = _Pm10001otu4CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 64, 1)
)
pm10001otu4CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlcommAccessLoopEntry.setStatus("current")


class _Pm10001otu4CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlcommAccessLoopIndex_Object = MibTableColumn
pm10001otu4CtrlcommAccessLoopIndex = _Pm10001otu4CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 64, 1, 1),
    _Pm10001otu4CtrlcommAccessLoopIndex_Type()
)
pm10001otu4CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlcommAccessLoopIndex.setStatus("current")
_Pm10001otu4CtrlcommAccessLoopPortn_Type = EkiState
_Pm10001otu4CtrlcommAccessLoopPortn_Object = MibTableColumn
pm10001otu4CtrlcommAccessLoopPortn = _Pm10001otu4CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 64, 1, 2),
    _Pm10001otu4CtrlcommAccessLoopPortn_Type()
)
pm10001otu4CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlcommAccessLoopPortn.setStatus("current")
_Pm10001otu4CtrllineLoopTable_Object = MibTable
pm10001otu4CtrllineLoopTable = _Pm10001otu4CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrllineLoopTable.setStatus("current")
_Pm10001otu4CtrllineLoopEntry_Object = MibTableRow
pm10001otu4CtrllineLoopEntry = _Pm10001otu4CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 66, 1)
)
pm10001otu4CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrllineLoopEntry.setStatus("current")


class _Pm10001otu4CtrllineLoopIndex_Type(Integer32):
    """Custom type pm10001otu4CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrllineLoopIndex_Object = MibTableColumn
pm10001otu4CtrllineLoopIndex = _Pm10001otu4CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 66, 1, 1),
    _Pm10001otu4CtrllineLoopIndex_Type()
)
pm10001otu4CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrllineLoopIndex.setStatus("current")
_Pm10001otu4CtrllineLoopPortn_Type = EkiState
_Pm10001otu4CtrllineLoopPortn_Object = MibTableColumn
pm10001otu4CtrllineLoopPortn = _Pm10001otu4CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 66, 1, 2),
    _Pm10001otu4CtrllineLoopPortn_Type()
)
pm10001otu4CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrllineLoopPortn.setStatus("current")
_Pm10001otu4CtrlfecDisableTable_Object = MibTable
pm10001otu4CtrlfecDisableTable = _Pm10001otu4CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlfecDisableTable.setStatus("current")
_Pm10001otu4CtrlfecDisableEntry_Object = MibTableRow
pm10001otu4CtrlfecDisableEntry = _Pm10001otu4CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 69, 1)
)
pm10001otu4CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlfecDisableEntry.setStatus("current")


class _Pm10001otu4CtrlfecDisableIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlfecDisableIndex_Object = MibTableColumn
pm10001otu4CtrlfecDisableIndex = _Pm10001otu4CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 69, 1, 1),
    _Pm10001otu4CtrlfecDisableIndex_Type()
)
pm10001otu4CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlfecDisableIndex.setStatus("current")
_Pm10001otu4CtrlfecDisablePortn_Type = EkiState
_Pm10001otu4CtrlfecDisablePortn_Object = MibTableColumn
pm10001otu4CtrlfecDisablePortn = _Pm10001otu4CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 69, 1, 2),
    _Pm10001otu4CtrlfecDisablePortn_Type()
)
pm10001otu4CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlfecDisablePortn.setStatus("current")
_Pm10001otu4CtrlmsaLineLoopTable_Object = MibTable
pm10001otu4CtrlmsaLineLoopTable = _Pm10001otu4CtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaLineLoopTable.setStatus("current")
_Pm10001otu4CtrlmsaLineLoopEntry_Object = MibTableRow
pm10001otu4CtrlmsaLineLoopEntry = _Pm10001otu4CtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 209, 1)
)
pm10001otu4CtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaLineLoopEntry.setStatus("current")


class _Pm10001otu4CtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlmsaLineLoopIndex_Object = MibTableColumn
pm10001otu4CtrlmsaLineLoopIndex = _Pm10001otu4CtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 209, 1, 1),
    _Pm10001otu4CtrlmsaLineLoopIndex_Type()
)
pm10001otu4CtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaLineLoopIndex.setStatus("current")
_Pm10001otu4CtrlmsaLineLoopPortn_Type = EkiState
_Pm10001otu4CtrlmsaLineLoopPortn_Object = MibTableColumn
pm10001otu4CtrlmsaLineLoopPortn = _Pm10001otu4CtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 209, 1, 2),
    _Pm10001otu4CtrlmsaLineLoopPortn_Type()
)
pm10001otu4CtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaLineLoopPortn.setStatus("current")
_Pm10001otu4CtrlmsaTxResetTable_Object = MibTable
pm10001otu4CtrlmsaTxResetTable = _Pm10001otu4CtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaTxResetTable.setStatus("current")
_Pm10001otu4CtrlmsaTxResetEntry_Object = MibTableRow
pm10001otu4CtrlmsaTxResetEntry = _Pm10001otu4CtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 210, 1)
)
pm10001otu4CtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaTxResetEntry.setStatus("current")


class _Pm10001otu4CtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlmsaTxResetIndex_Object = MibTableColumn
pm10001otu4CtrlmsaTxResetIndex = _Pm10001otu4CtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 210, 1, 1),
    _Pm10001otu4CtrlmsaTxResetIndex_Type()
)
pm10001otu4CtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaTxResetIndex.setStatus("current")
_Pm10001otu4CtrlmsaTxResetPortn_Type = EkiState
_Pm10001otu4CtrlmsaTxResetPortn_Object = MibTableColumn
pm10001otu4CtrlmsaTxResetPortn = _Pm10001otu4CtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 210, 1, 2),
    _Pm10001otu4CtrlmsaTxResetPortn_Type()
)
pm10001otu4CtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaTxResetPortn.setStatus("current")
_Pm10001otu4CtrlmsaRxResetTable_Object = MibTable
pm10001otu4CtrlmsaRxResetTable = _Pm10001otu4CtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaRxResetTable.setStatus("current")
_Pm10001otu4CtrlmsaRxResetEntry_Object = MibTableRow
pm10001otu4CtrlmsaRxResetEntry = _Pm10001otu4CtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 211, 1)
)
pm10001otu4CtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaRxResetEntry.setStatus("current")


class _Pm10001otu4CtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlmsaRxResetIndex_Object = MibTableColumn
pm10001otu4CtrlmsaRxResetIndex = _Pm10001otu4CtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 211, 1, 1),
    _Pm10001otu4CtrlmsaRxResetIndex_Type()
)
pm10001otu4CtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaRxResetIndex.setStatus("current")
_Pm10001otu4CtrlmsaRxResetPortn_Type = EkiState
_Pm10001otu4CtrlmsaRxResetPortn_Object = MibTableColumn
pm10001otu4CtrlmsaRxResetPortn = _Pm10001otu4CtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 211, 1, 2),
    _Pm10001otu4CtrlmsaRxResetPortn_Type()
)
pm10001otu4CtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaRxResetPortn.setStatus("current")
_Pm10001otu4CtrlmsaShutdownTable_Object = MibTable
pm10001otu4CtrlmsaShutdownTable = _Pm10001otu4CtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaShutdownTable.setStatus("current")
_Pm10001otu4CtrlmsaShutdownEntry_Object = MibTableRow
pm10001otu4CtrlmsaShutdownEntry = _Pm10001otu4CtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 212, 1)
)
pm10001otu4CtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaShutdownEntry.setStatus("current")


class _Pm10001otu4CtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm10001otu4CtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrlmsaShutdownIndex_Object = MibTableColumn
pm10001otu4CtrlmsaShutdownIndex = _Pm10001otu4CtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 212, 1, 1),
    _Pm10001otu4CtrlmsaShutdownIndex_Type()
)
pm10001otu4CtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaShutdownIndex.setStatus("current")
_Pm10001otu4CtrlmsaShutdownPortn_Type = EkiState
_Pm10001otu4CtrlmsaShutdownPortn_Object = MibTableColumn
pm10001otu4CtrlmsaShutdownPortn = _Pm10001otu4CtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 212, 1, 2),
    _Pm10001otu4CtrlmsaShutdownPortn_Type()
)
pm10001otu4CtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrlmsaShutdownPortn.setStatus("current")
_Pm10001otu4CtrllineResetAllCountTable_Object = MibTable
pm10001otu4CtrllineResetAllCountTable = _Pm10001otu4CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm10001otu4CtrllineResetAllCountTable.setStatus("current")
_Pm10001otu4CtrllineResetAllCountEntry_Object = MibTableRow
pm10001otu4CtrllineResetAllCountEntry = _Pm10001otu4CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 263, 1)
)
pm10001otu4CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CtrllineResetAllCountEntry.setStatus("current")


class _Pm10001otu4CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm10001otu4CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm10001otu4CtrllineResetAllCountIndex_Object = MibTableColumn
pm10001otu4CtrllineResetAllCountIndex = _Pm10001otu4CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 263, 1, 1),
    _Pm10001otu4CtrllineResetAllCountIndex_Type()
)
pm10001otu4CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CtrllineResetAllCountIndex.setStatus("current")
_Pm10001otu4CtrllineResetAllCountsPortn_Type = EkiState
_Pm10001otu4CtrllineResetAllCountsPortn_Object = MibTableColumn
pm10001otu4CtrllineResetAllCountsPortn = _Pm10001otu4CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 6, 3, 263, 1, 2),
    _Pm10001otu4CtrllineResetAllCountsPortn_Type()
)
pm10001otu4CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CtrllineResetAllCountsPortn.setStatus("current")
_Pm10001otu4ri_ObjectIdentity = ObjectIdentity
pm10001otu4ri = _Pm10001otu4ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7)
)
_Pm10001otu4riTable_ObjectIdentity = ObjectIdentity
pm10001otu4riTable = _Pm10001otu4riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1)
)
_Pm10001otu4RinvSfpTable_Object = MibTable
pm10001otu4RinvSfpTable = _Pm10001otu4RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4RinvSfpTable.setStatus("current")
_Pm10001otu4RinvSfpEntry_Object = MibTableRow
pm10001otu4RinvSfpEntry = _Pm10001otu4RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 1, 1)
)
pm10001otu4RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4RinvSfpEntry.setStatus("current")


class _Pm10001otu4RinvSfpIndex_Type(Integer32):
    """Custom type pm10001otu4RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10001otu4RinvSfpIndex_Type.__name__ = "Integer32"
_Pm10001otu4RinvSfpIndex_Object = MibTableColumn
pm10001otu4RinvSfpIndex = _Pm10001otu4RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 1, 1, 1),
    _Pm10001otu4RinvSfpIndex_Type()
)
pm10001otu4RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvSfpIndex.setStatus("current")
_Pm10001otu4Rinvsfp_Type = DisplayString
_Pm10001otu4Rinvsfp_Object = MibTableColumn
pm10001otu4Rinvsfp = _Pm10001otu4Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 1, 1, 2),
    _Pm10001otu4Rinvsfp_Type()
)
pm10001otu4Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4Rinvsfp.setStatus("current")
_Pm10001otu4RinvLineTable_Object = MibTable
pm10001otu4RinvLineTable = _Pm10001otu4RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm10001otu4RinvLineTable.setStatus("current")
_Pm10001otu4RinvLineEntry_Object = MibTableRow
pm10001otu4RinvLineEntry = _Pm10001otu4RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 2, 1)
)
pm10001otu4RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4RinvLineEntry.setStatus("current")


class _Pm10001otu4RinvLineIndex_Type(Integer32):
    """Custom type pm10001otu4RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10001otu4RinvLineIndex_Type.__name__ = "Integer32"
_Pm10001otu4RinvLineIndex_Object = MibTableColumn
pm10001otu4RinvLineIndex = _Pm10001otu4RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 2, 1, 1),
    _Pm10001otu4RinvLineIndex_Type()
)
pm10001otu4RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvLineIndex.setStatus("current")
_Pm10001otu4RinvxfpLine_Type = DisplayString
_Pm10001otu4RinvxfpLine_Object = MibTableColumn
pm10001otu4RinvxfpLine = _Pm10001otu4RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 1, 2, 1, 2),
    _Pm10001otu4RinvxfpLine_Type()
)
pm10001otu4RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvxfpLine.setStatus("current")
_Pm10001otu4RinvReloadInventory_Type = EkiOnOff
_Pm10001otu4RinvReloadInventory_Object = MibScalar
pm10001otu4RinvReloadInventory = _Pm10001otu4RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 2),
    _Pm10001otu4RinvReloadInventory_Type()
)
pm10001otu4RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4RinvReloadInventory.setStatus("current")
_Pm10001otu4RinvHwPlatform_Type = DisplayString
_Pm10001otu4RinvHwPlatform_Object = MibScalar
pm10001otu4RinvHwPlatform = _Pm10001otu4RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 3),
    _Pm10001otu4RinvHwPlatform_Type()
)
pm10001otu4RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvHwPlatform.setStatus("current")
_Pm10001otu4RinvModulePlatform_Type = DisplayString
_Pm10001otu4RinvModulePlatform_Object = MibScalar
pm10001otu4RinvModulePlatform = _Pm10001otu4RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 4),
    _Pm10001otu4RinvModulePlatform_Type()
)
pm10001otu4RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvModulePlatform.setStatus("current")
_Pm10001otu4RinvSwPlatform_Type = DisplayString
_Pm10001otu4RinvSwPlatform_Object = MibScalar
pm10001otu4RinvSwPlatform = _Pm10001otu4RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 5),
    _Pm10001otu4RinvSwPlatform_Type()
)
pm10001otu4RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvSwPlatform.setStatus("current")
_Pm10001otu4RinvGwPlatform_Type = DisplayString
_Pm10001otu4RinvGwPlatform_Object = MibScalar
pm10001otu4RinvGwPlatform = _Pm10001otu4RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 7, 6),
    _Pm10001otu4RinvGwPlatform_Type()
)
pm10001otu4RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4RinvGwPlatform.setStatus("current")
_Pm10001otu4download_ObjectIdentity = ObjectIdentity
pm10001otu4download = _Pm10001otu4download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8)
)
_Pm10001otu4DwlOther_ObjectIdentity = ObjectIdentity
pm10001otu4DwlOther = _Pm10001otu4DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1)
)
_Pm10001otu4DwlrestartProcess_ObjectIdentity = ObjectIdentity
pm10001otu4DwlrestartProcess = _Pm10001otu4DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 0)
)
_Pm10001otu4DwlWarmRestartProcessed_Type = EkiOnOff
_Pm10001otu4DwlWarmRestartProcessed_Object = MibScalar
pm10001otu4DwlWarmRestartProcessed = _Pm10001otu4DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 0, 1),
    _Pm10001otu4DwlWarmRestartProcessed_Type()
)
pm10001otu4DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlWarmRestartProcessed.setStatus("current")
_Pm10001otu4DwlColdRestartProcessed_Type = EkiOnOff
_Pm10001otu4DwlColdRestartProcessed_Object = MibScalar
pm10001otu4DwlColdRestartProcessed = _Pm10001otu4DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 0, 2),
    _Pm10001otu4DwlColdRestartProcessed_Type()
)
pm10001otu4DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlColdRestartProcessed.setStatus("current")
_Pm10001otu4DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm10001otu4DwlswBanksUsed = _Pm10001otu4DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 1)
)
_Pm10001otu4DwlSwBank1Used_Type = EkiOnOff
_Pm10001otu4DwlSwBank1Used_Object = MibScalar
pm10001otu4DwlSwBank1Used = _Pm10001otu4DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 1, 1),
    _Pm10001otu4DwlSwBank1Used_Type()
)
pm10001otu4DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlSwBank1Used.setStatus("current")
_Pm10001otu4DwlSwBank2Used_Type = EkiOnOff
_Pm10001otu4DwlSwBank2Used_Object = MibScalar
pm10001otu4DwlSwBank2Used = _Pm10001otu4DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 1, 2),
    _Pm10001otu4DwlSwBank2Used_Type()
)
pm10001otu4DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlSwBank2Used.setStatus("current")
_Pm10001otu4DwlSwBank1Notempty_Type = EkiOnOff
_Pm10001otu4DwlSwBank1Notempty_Object = MibScalar
pm10001otu4DwlSwBank1Notempty = _Pm10001otu4DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 1, 5),
    _Pm10001otu4DwlSwBank1Notempty_Type()
)
pm10001otu4DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlSwBank1Notempty.setStatus("current")
_Pm10001otu4DwlSwBank2Notempty_Type = EkiOnOff
_Pm10001otu4DwlSwBank2Notempty_Object = MibScalar
pm10001otu4DwlSwBank2Notempty = _Pm10001otu4DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 1, 6),
    _Pm10001otu4DwlSwBank2Notempty_Type()
)
pm10001otu4DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlSwBank2Notempty.setStatus("current")
_Pm10001otu4DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm10001otu4DwlgwBanksUsed = _Pm10001otu4DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2)
)
_Pm10001otu4DwlGwBank1Used_Type = EkiOnOff
_Pm10001otu4DwlGwBank1Used_Object = MibScalar
pm10001otu4DwlGwBank1Used = _Pm10001otu4DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 1),
    _Pm10001otu4DwlGwBank1Used_Type()
)
pm10001otu4DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank1Used.setStatus("current")
_Pm10001otu4DwlGwBank2Used_Type = EkiOnOff
_Pm10001otu4DwlGwBank2Used_Object = MibScalar
pm10001otu4DwlGwBank2Used = _Pm10001otu4DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 2),
    _Pm10001otu4DwlGwBank2Used_Type()
)
pm10001otu4DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank2Used.setStatus("current")
_Pm10001otu4DwlGwBank3Used_Type = EkiOnOff
_Pm10001otu4DwlGwBank3Used_Object = MibScalar
pm10001otu4DwlGwBank3Used = _Pm10001otu4DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 3),
    _Pm10001otu4DwlGwBank3Used_Type()
)
pm10001otu4DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank3Used.setStatus("current")
_Pm10001otu4DwlGwBank4Used_Type = EkiOnOff
_Pm10001otu4DwlGwBank4Used_Object = MibScalar
pm10001otu4DwlGwBank4Used = _Pm10001otu4DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 4),
    _Pm10001otu4DwlGwBank4Used_Type()
)
pm10001otu4DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank4Used.setStatus("current")
_Pm10001otu4DwlGwBank1Notempty_Type = EkiOnOff
_Pm10001otu4DwlGwBank1Notempty_Object = MibScalar
pm10001otu4DwlGwBank1Notempty = _Pm10001otu4DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 5),
    _Pm10001otu4DwlGwBank1Notempty_Type()
)
pm10001otu4DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank1Notempty.setStatus("current")
_Pm10001otu4DwlGwBank2Notempty_Type = EkiOnOff
_Pm10001otu4DwlGwBank2Notempty_Object = MibScalar
pm10001otu4DwlGwBank2Notempty = _Pm10001otu4DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 6),
    _Pm10001otu4DwlGwBank2Notempty_Type()
)
pm10001otu4DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank2Notempty.setStatus("current")
_Pm10001otu4DwlGwBank3Notempty_Type = EkiOnOff
_Pm10001otu4DwlGwBank3Notempty_Object = MibScalar
pm10001otu4DwlGwBank3Notempty = _Pm10001otu4DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 7),
    _Pm10001otu4DwlGwBank3Notempty_Type()
)
pm10001otu4DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank3Notempty.setStatus("current")
_Pm10001otu4DwlGwBank4Notempty_Type = EkiOnOff
_Pm10001otu4DwlGwBank4Notempty_Object = MibScalar
pm10001otu4DwlGwBank4Notempty = _Pm10001otu4DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 1, 2, 8),
    _Pm10001otu4DwlGwBank4Notempty_Type()
)
pm10001otu4DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4DwlGwBank4Notempty.setStatus("current")
_Pm10001otu4DwlClient_ObjectIdentity = ObjectIdentity
pm10001otu4DwlClient = _Pm10001otu4DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 2)
)
_Pm10001otu4DwlLine_ObjectIdentity = ObjectIdentity
pm10001otu4DwlLine = _Pm10001otu4DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 8, 3)
)
_Pm10001otu4Config_ObjectIdentity = ObjectIdentity
pm10001otu4Config = _Pm10001otu4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9)
)
_Pm10001otu4CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm10001otu4CfgAccessCAisCsf = _Pm10001otu4CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 1)
)
_Pm10001otu4CfgClientcaiscsfTable_Object = MibTable
pm10001otu4CfgClientcaiscsfTable = _Pm10001otu4CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgClientcaiscsfTable.setStatus("current")
_Pm10001otu4CfgClientcaiscsfEntry_Object = MibTableRow
pm10001otu4CfgClientcaiscsfEntry = _Pm10001otu4CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 1, 1, 1)
)
pm10001otu4CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgClientcaiscsfEntry.setStatus("current")


class _Pm10001otu4CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm10001otu4CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgClientcaiscsfIndex_Object = MibTableColumn
pm10001otu4CfgClientcaiscsfIndex = _Pm10001otu4CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 1, 1, 1, 1),
    _Pm10001otu4CfgClientcaiscsfIndex_Type()
)
pm10001otu4CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgClientcaiscsfIndex.setStatus("current")


class _Pm10001otu4CfgReservePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgReservePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgReservePortn_Object = MibTableColumn
pm10001otu4CfgReservePortn = _Pm10001otu4CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 1, 1, 1, 3),
    _Pm10001otu4CfgReservePortn_Type()
)
pm10001otu4CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgReservePortn.setStatus("current")
_Pm10001otu4CfgStartup_ObjectIdentity = ObjectIdentity
pm10001otu4CfgStartup = _Pm10001otu4CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2)
)
_Pm10001otu4CfgClientStartupTable_Object = MibTable
pm10001otu4CfgClientStartupTable = _Pm10001otu4CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgClientStartupTable.setStatus("current")
_Pm10001otu4CfgClientStartupEntry_Object = MibTableRow
pm10001otu4CfgClientStartupEntry = _Pm10001otu4CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1, 1)
)
pm10001otu4CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgClientStartupEntry.setStatus("current")


class _Pm10001otu4CfgClientStartupIndex_Type(Integer32):
    """Custom type pm10001otu4CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgClientStartupIndex_Object = MibTableColumn
pm10001otu4CfgClientStartupIndex = _Pm10001otu4CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1, 1, 1),
    _Pm10001otu4CfgClientStartupIndex_Type()
)
pm10001otu4CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgClientStartupIndex.setStatus("current")


class _Pm10001otu4CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgSystConfPortPortn_Object = MibTableColumn
pm10001otu4CfgSystConfPortPortn = _Pm10001otu4CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1, 1, 3),
    _Pm10001otu4CfgSystConfPortPortn_Type()
)
pm10001otu4CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgSystConfPortPortn.setStatus("current")


class _Pm10001otu4CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgNetConfPortPortn_Object = MibTableColumn
pm10001otu4CfgNetConfPortPortn = _Pm10001otu4CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1, 1, 4),
    _Pm10001otu4CfgNetConfPortPortn_Type()
)
pm10001otu4CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgNetConfPortPortn.setStatus("current")


class _Pm10001otu4CfgIgnoreTimePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgIgnoreTimePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgIgnoreTimePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgIgnoreTimePortn_Object = MibTableColumn
pm10001otu4CfgIgnoreTimePortn = _Pm10001otu4CfgIgnoreTimePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1, 1, 6),
    _Pm10001otu4CfgIgnoreTimePortn_Type()
)
pm10001otu4CfgIgnoreTimePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgIgnoreTimePortn.setStatus("current")


class _Pm10001otu4CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgOptionsPortPortn_Object = MibTableColumn
pm10001otu4CfgOptionsPortPortn = _Pm10001otu4CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 1, 1, 14),
    _Pm10001otu4CfgOptionsPortPortn_Type()
)
pm10001otu4CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgOptionsPortPortn.setStatus("current")
_Pm10001otu4CfgLineStartupTable_Object = MibTable
pm10001otu4CfgLineStartupTable = _Pm10001otu4CfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLineStartupTable.setStatus("current")
_Pm10001otu4CfgLineStartupEntry_Object = MibTableRow
pm10001otu4CfgLineStartupEntry = _Pm10001otu4CfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 2, 1)
)
pm10001otu4CfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLineStartupEntry.setStatus("current")


class _Pm10001otu4CfgLineStartupIndex_Type(Integer32):
    """Custom type pm10001otu4CfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgLineStartupIndex_Object = MibTableColumn
pm10001otu4CfgLineStartupIndex = _Pm10001otu4CfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 2, 1, 1),
    _Pm10001otu4CfgLineStartupIndex_Type()
)
pm10001otu4CfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgLineStartupIndex.setStatus("current")


class _Pm10001otu4CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgSystConfLinePortn_Object = MibTableColumn
pm10001otu4CfgSystConfLinePortn = _Pm10001otu4CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 2, 1, 3),
    _Pm10001otu4CfgSystConfLinePortn_Type()
)
pm10001otu4CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgSystConfLinePortn.setStatus("current")


class _Pm10001otu4CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgOptionsLinePortn_Object = MibTableColumn
pm10001otu4CfgOptionsLinePortn = _Pm10001otu4CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 2, 1, 14),
    _Pm10001otu4CfgOptionsLinePortn_Type()
)
pm10001otu4CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgOptionsLinePortn.setStatus("current")
_Pm10001otu4CfgXfpTable_Object = MibTable
pm10001otu4CfgXfpTable = _Pm10001otu4CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgXfpTable.setStatus("current")
_Pm10001otu4CfgXfpEntry_Object = MibTableRow
pm10001otu4CfgXfpEntry = _Pm10001otu4CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 3, 1)
)
pm10001otu4CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgXfpEntry.setStatus("current")


class _Pm10001otu4CfgXfpIndex_Type(Integer32):
    """Custom type pm10001otu4CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgXfpIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgXfpIndex_Object = MibTableColumn
pm10001otu4CfgXfpIndex = _Pm10001otu4CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 3, 1, 1),
    _Pm10001otu4CfgXfpIndex_Type()
)
pm10001otu4CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgXfpIndex.setStatus("current")


class _Pm10001otu4CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgSystConfMsaLinePortn_Object = MibTableColumn
pm10001otu4CfgSystConfMsaLinePortn = _Pm10001otu4CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 3, 1, 3),
    _Pm10001otu4CfgSystConfMsaLinePortn_Type()
)
pm10001otu4CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgSystConfMsaLinePortn.setStatus("current")


class _Pm10001otu4CfgCompDispChromValuePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgCompDispChromValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgCompDispChromValuePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgCompDispChromValuePortn_Object = MibTableColumn
pm10001otu4CfgCompDispChromValuePortn = _Pm10001otu4CfgCompDispChromValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 2, 3, 1, 4),
    _Pm10001otu4CfgCompDispChromValuePortn_Type()
)
pm10001otu4CfgCompDispChromValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgCompDispChromValuePortn.setStatus("current")
_Pm10001otu4CfgLabels_ObjectIdentity = ObjectIdentity
pm10001otu4CfgLabels = _Pm10001otu4CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3)
)
_Pm10001otu4CfgLabelclientTable_Object = MibTable
pm10001otu4CfgLabelclientTable = _Pm10001otu4CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLabelclientTable.setStatus("current")
_Pm10001otu4CfgLabelclientEntry_Object = MibTableRow
pm10001otu4CfgLabelclientEntry = _Pm10001otu4CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 1, 1)
)
pm10001otu4CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLabelclientEntry.setStatus("current")


class _Pm10001otu4CfgLabelclientIndex_Type(Integer32):
    """Custom type pm10001otu4CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgLabelclientIndex_Object = MibTableColumn
pm10001otu4CfgLabelclientIndex = _Pm10001otu4CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 1, 1, 1),
    _Pm10001otu4CfgLabelclientIndex_Type()
)
pm10001otu4CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgLabelclientIndex.setStatus("current")


class _Pm10001otu4CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm10001otu4CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10001otu4CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm10001otu4CfgLabelclientPortn_Object = MibTableColumn
pm10001otu4CfgLabelclientPortn = _Pm10001otu4CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 1, 1, 3),
    _Pm10001otu4CfgLabelclientPortn_Type()
)
pm10001otu4CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgLabelclientPortn.setStatus("current")
_Pm10001otu4CfgLabellineTable_Object = MibTable
pm10001otu4CfgLabellineTable = _Pm10001otu4CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLabellineTable.setStatus("current")
_Pm10001otu4CfgLabellineEntry_Object = MibTableRow
pm10001otu4CfgLabellineEntry = _Pm10001otu4CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 2, 1)
)
pm10001otu4CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLabellineEntry.setStatus("current")


class _Pm10001otu4CfgLabellineIndex_Type(Integer32):
    """Custom type pm10001otu4CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgLabellineIndex_Object = MibTableColumn
pm10001otu4CfgLabellineIndex = _Pm10001otu4CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 2, 1, 1),
    _Pm10001otu4CfgLabellineIndex_Type()
)
pm10001otu4CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgLabellineIndex.setStatus("current")


class _Pm10001otu4CfgLabellinePortn_Type(DisplayString):
    """Custom type pm10001otu4CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10001otu4CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm10001otu4CfgLabellinePortn_Object = MibTableColumn
pm10001otu4CfgLabellinePortn = _Pm10001otu4CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 3, 2, 1, 3),
    _Pm10001otu4CfgLabellinePortn_Type()
)
pm10001otu4CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgLabellinePortn.setStatus("current")
_Pm10001otu4CfgStartuptlh_ObjectIdentity = ObjectIdentity
pm10001otu4CfgStartuptlh = _Pm10001otu4CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4)
)
_Pm10001otu4CfgOtxtlhTable_Object = MibTable
pm10001otu4CfgOtxtlhTable = _Pm10001otu4CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgOtxtlhTable.setStatus("current")
_Pm10001otu4CfgOtxtlhEntry_Object = MibTableRow
pm10001otu4CfgOtxtlhEntry = _Pm10001otu4CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1)
)
pm10001otu4CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgOtxtlhEntry.setStatus("current")


class _Pm10001otu4CfgOtxtlhIndex_Type(Integer32):
    """Custom type pm10001otu4CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgOtxtlhIndex_Object = MibTableColumn
pm10001otu4CfgOtxtlhIndex = _Pm10001otu4CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1, 1),
    _Pm10001otu4CfgOtxtlhIndex_Type()
)
pm10001otu4CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgOtxtlhIndex.setStatus("current")


class _Pm10001otu4CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgLinePwrLaserPortn_Object = MibTableColumn
pm10001otu4CfgLinePwrLaserPortn = _Pm10001otu4CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1, 6),
    _Pm10001otu4CfgLinePwrLaserPortn_Type()
)
pm10001otu4CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgLinePwrLaserPortn.setStatus("current")


class _Pm10001otu4CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgLineFCurrentPortn_Object = MibTableColumn
pm10001otu4CfgLineFCurrentPortn = _Pm10001otu4CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1, 7),
    _Pm10001otu4CfgLineFCurrentPortn_Type()
)
pm10001otu4CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgLineFCurrentPortn.setStatus("current")


class _Pm10001otu4CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgLineGridCurrentPortn_Object = MibTableColumn
pm10001otu4CfgLineGridCurrentPortn = _Pm10001otu4CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1, 8),
    _Pm10001otu4CfgLineGridCurrentPortn_Type()
)
pm10001otu4CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgLineGridCurrentPortn.setStatus("current")


class _Pm10001otu4CfgFPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgFPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgFPortn_Object = MibTableColumn
pm10001otu4CfgFPortn = _Pm10001otu4CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1, 9),
    _Pm10001otu4CfgFPortn_Type()
)
pm10001otu4CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgFPortn.setStatus("current")


class _Pm10001otu4CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgRxLineFCurrentPortn_Object = MibTableColumn
pm10001otu4CfgRxLineFCurrentPortn = _Pm10001otu4CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 4, 1, 1, 10),
    _Pm10001otu4CfgRxLineFCurrentPortn_Type()
)
pm10001otu4CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgRxLineFCurrentPortn.setStatus("current")
_Pm10001otu4CfgOther_ObjectIdentity = ObjectIdentity
pm10001otu4CfgOther = _Pm10001otu4CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 5)
)
_Pm10001otu4tablemoduleOther_ObjectIdentity = ObjectIdentity
pm10001otu4tablemoduleOther = _Pm10001otu4tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 5, 1)
)


class _Pm10001otu4Cfgmode_Type(Unsigned32):
    """Custom type pm10001otu4Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4Cfgmode_Type.__name__ = "Unsigned32"
_Pm10001otu4Cfgmode_Object = MibScalar
pm10001otu4Cfgmode = _Pm10001otu4Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 5, 1, 2),
    _Pm10001otu4Cfgmode_Type()
)
pm10001otu4Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Cfgmode.setStatus("current")


class _Pm10001otu4CfgnonLinearEffectsThresholds_Type(Unsigned32):
    """Custom type pm10001otu4CfgnonLinearEffectsThresholds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgnonLinearEffectsThresholds_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgnonLinearEffectsThresholds_Object = MibScalar
pm10001otu4CfgnonLinearEffectsThresholds = _Pm10001otu4CfgnonLinearEffectsThresholds_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 5, 1, 3),
    _Pm10001otu4CfgnonLinearEffectsThresholds_Type()
)
pm10001otu4CfgnonLinearEffectsThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgnonLinearEffectsThresholds.setStatus("current")


class _Pm10001otu4CfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm10001otu4CfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgfanHighSpeedThreshold_Object = MibScalar
pm10001otu4CfgfanHighSpeedThreshold = _Pm10001otu4CfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 5, 1, 4),
    _Pm10001otu4CfgfanHighSpeedThreshold_Type()
)
pm10001otu4CfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgfanHighSpeedThreshold.setStatus("current")
_Pm10001otu4CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm10001otu4CfgStartuptablefive = _Pm10001otu4CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6)
)
_Pm10001otu4CfgOtxtlhcapabilitiesTable_Object = MibTable
pm10001otu4CfgOtxtlhcapabilitiesTable = _Pm10001otu4CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm10001otu4CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm10001otu4CfgOtxtlhcapabilitiesEntry = _Pm10001otu4CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1)
)
pm10001otu4CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm10001otu4CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm10001otu4CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm10001otu4CfgOtxtlhcapabilitiesIndex = _Pm10001otu4CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1, 1),
    _Pm10001otu4CfgOtxtlhcapabilitiesIndex_Type()
)
pm10001otu4CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm10001otu4CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgComponentTypePortn_Object = MibTableColumn
pm10001otu4CfgComponentTypePortn = _Pm10001otu4CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1, 3),
    _Pm10001otu4CfgComponentTypePortn_Type()
)
pm10001otu4CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgComponentTypePortn.setStatus("current")


class _Pm10001otu4CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgMiscellaneousPortn_Object = MibTableColumn
pm10001otu4CfgMiscellaneousPortn = _Pm10001otu4CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1, 4),
    _Pm10001otu4CfgMiscellaneousPortn_Type()
)
pm10001otu4CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgMiscellaneousPortn.setStatus("current")


class _Pm10001otu4CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgFirstChannelPortn_Object = MibTableColumn
pm10001otu4CfgFirstChannelPortn = _Pm10001otu4CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1, 5),
    _Pm10001otu4CfgFirstChannelPortn_Type()
)
pm10001otu4CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgFirstChannelPortn.setStatus("current")


class _Pm10001otu4CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgLastChannelPortn_Object = MibTableColumn
pm10001otu4CfgLastChannelPortn = _Pm10001otu4CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1, 6),
    _Pm10001otu4CfgLastChannelPortn_Type()
)
pm10001otu4CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgLastChannelPortn.setStatus("current")


class _Pm10001otu4CfgGridPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgGridPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgGridPortn_Object = MibTableColumn
pm10001otu4CfgGridPortn = _Pm10001otu4CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 6, 1, 1, 7),
    _Pm10001otu4CfgGridPortn_Type()
)
pm10001otu4CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgGridPortn.setStatus("current")
_Pm10001otu4CfgStartuptableslot_ObjectIdentity = ObjectIdentity
pm10001otu4CfgStartuptableslot = _Pm10001otu4CfgStartuptableslot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7)
)
_Pm10001otu4CfgLinePtmsiAccOtnTable_Object = MibTable
pm10001otu4CfgLinePtmsiAccOtnTable = _Pm10001otu4CfgLinePtmsiAccOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1)
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLinePtmsiAccOtnTable.setStatus("current")
_Pm10001otu4CfgLinePtmsiAccOtnEntry_Object = MibTableRow
pm10001otu4CfgLinePtmsiAccOtnEntry = _Pm10001otu4CfgLinePtmsiAccOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1)
)
pm10001otu4CfgLinePtmsiAccOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4CfgLinePtmsiAccOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4CfgLinePtmsiAccOtnEntry.setStatus("current")


class _Pm10001otu4CfgLinePtmsiAccOtnIndex_Type(Integer32):
    """Custom type pm10001otu4CfgLinePtmsiAccOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4CfgLinePtmsiAccOtnIndex_Type.__name__ = "Integer32"
_Pm10001otu4CfgLinePtmsiAccOtnIndex_Object = MibTableColumn
pm10001otu4CfgLinePtmsiAccOtnIndex = _Pm10001otu4CfgLinePtmsiAccOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 1),
    _Pm10001otu4CfgLinePtmsiAccOtnIndex_Type()
)
pm10001otu4CfgLinePtmsiAccOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgLinePtmsiAccOtnIndex.setStatus("current")


class _Pm10001otu4CfgPayloadtypePortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgPayloadtypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgPayloadtypePortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgPayloadtypePortn_Object = MibTableColumn
pm10001otu4CfgPayloadtypePortn = _Pm10001otu4CfgPayloadtypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 3),
    _Pm10001otu4CfgPayloadtypePortn_Type()
)
pm10001otu4CfgPayloadtypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgPayloadtypePortn.setStatus("current")


class _Pm10001otu4CfgPtmsireservedPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgPtmsireservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgPtmsireservedPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgPtmsireservedPortn_Object = MibTableColumn
pm10001otu4CfgPtmsireservedPortn = _Pm10001otu4CfgPtmsireservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 4),
    _Pm10001otu4CfgPtmsireservedPortn_Type()
)
pm10001otu4CfgPtmsireservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgPtmsireservedPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot1valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot1valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot1valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot1valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot1valPortn = _Pm10001otu4CfgTimeslot1valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 5),
    _Pm10001otu4CfgTimeslot1valPortn_Type()
)
pm10001otu4CfgTimeslot1valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot1valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot2valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot2valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot2valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot2valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot2valPortn = _Pm10001otu4CfgTimeslot2valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 6),
    _Pm10001otu4CfgTimeslot2valPortn_Type()
)
pm10001otu4CfgTimeslot2valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot2valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot3valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot3valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot3valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot3valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot3valPortn = _Pm10001otu4CfgTimeslot3valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 7),
    _Pm10001otu4CfgTimeslot3valPortn_Type()
)
pm10001otu4CfgTimeslot3valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot3valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot4valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot4valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot4valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot4valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot4valPortn = _Pm10001otu4CfgTimeslot4valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 8),
    _Pm10001otu4CfgTimeslot4valPortn_Type()
)
pm10001otu4CfgTimeslot4valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot4valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot5valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot5valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot5valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot5valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot5valPortn = _Pm10001otu4CfgTimeslot5valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 9),
    _Pm10001otu4CfgTimeslot5valPortn_Type()
)
pm10001otu4CfgTimeslot5valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot5valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot6valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot6valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot6valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot6valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot6valPortn = _Pm10001otu4CfgTimeslot6valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 10),
    _Pm10001otu4CfgTimeslot6valPortn_Type()
)
pm10001otu4CfgTimeslot6valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot6valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot7valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot7valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot7valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot7valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot7valPortn = _Pm10001otu4CfgTimeslot7valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 11),
    _Pm10001otu4CfgTimeslot7valPortn_Type()
)
pm10001otu4CfgTimeslot7valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot7valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot8valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot8valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot8valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot8valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot8valPortn = _Pm10001otu4CfgTimeslot8valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 12),
    _Pm10001otu4CfgTimeslot8valPortn_Type()
)
pm10001otu4CfgTimeslot8valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot8valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot9valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot9valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot9valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot9valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot9valPortn = _Pm10001otu4CfgTimeslot9valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 13),
    _Pm10001otu4CfgTimeslot9valPortn_Type()
)
pm10001otu4CfgTimeslot9valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot9valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot10valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot10valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot10valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot10valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot10valPortn = _Pm10001otu4CfgTimeslot10valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 14),
    _Pm10001otu4CfgTimeslot10valPortn_Type()
)
pm10001otu4CfgTimeslot10valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot10valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot11valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot11valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot11valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot11valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot11valPortn = _Pm10001otu4CfgTimeslot11valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 15),
    _Pm10001otu4CfgTimeslot11valPortn_Type()
)
pm10001otu4CfgTimeslot11valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot11valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot12valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot12valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot12valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot12valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot12valPortn = _Pm10001otu4CfgTimeslot12valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 16),
    _Pm10001otu4CfgTimeslot12valPortn_Type()
)
pm10001otu4CfgTimeslot12valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot12valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot13valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot13valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot13valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot13valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot13valPortn = _Pm10001otu4CfgTimeslot13valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 17),
    _Pm10001otu4CfgTimeslot13valPortn_Type()
)
pm10001otu4CfgTimeslot13valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot13valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot14valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot14valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot14valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot14valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot14valPortn = _Pm10001otu4CfgTimeslot14valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 18),
    _Pm10001otu4CfgTimeslot14valPortn_Type()
)
pm10001otu4CfgTimeslot14valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot14valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot15valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot15valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot15valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot15valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot15valPortn = _Pm10001otu4CfgTimeslot15valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 19),
    _Pm10001otu4CfgTimeslot15valPortn_Type()
)
pm10001otu4CfgTimeslot15valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot15valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot16valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot16valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot16valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot16valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot16valPortn = _Pm10001otu4CfgTimeslot16valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 20),
    _Pm10001otu4CfgTimeslot16valPortn_Type()
)
pm10001otu4CfgTimeslot16valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot16valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot17valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot17valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot17valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot17valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot17valPortn = _Pm10001otu4CfgTimeslot17valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 21),
    _Pm10001otu4CfgTimeslot17valPortn_Type()
)
pm10001otu4CfgTimeslot17valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot17valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot18valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot18valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot18valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot18valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot18valPortn = _Pm10001otu4CfgTimeslot18valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 22),
    _Pm10001otu4CfgTimeslot18valPortn_Type()
)
pm10001otu4CfgTimeslot18valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot18valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot19valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot19valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot19valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot19valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot19valPortn = _Pm10001otu4CfgTimeslot19valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 23),
    _Pm10001otu4CfgTimeslot19valPortn_Type()
)
pm10001otu4CfgTimeslot19valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot19valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot20valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot20valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot20valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot20valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot20valPortn = _Pm10001otu4CfgTimeslot20valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 24),
    _Pm10001otu4CfgTimeslot20valPortn_Type()
)
pm10001otu4CfgTimeslot20valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot20valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot21valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot21valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot21valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot21valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot21valPortn = _Pm10001otu4CfgTimeslot21valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 25),
    _Pm10001otu4CfgTimeslot21valPortn_Type()
)
pm10001otu4CfgTimeslot21valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot21valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot22valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot22valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot22valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot22valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot22valPortn = _Pm10001otu4CfgTimeslot22valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 26),
    _Pm10001otu4CfgTimeslot22valPortn_Type()
)
pm10001otu4CfgTimeslot22valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot22valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot23valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot23valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot23valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot23valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot23valPortn = _Pm10001otu4CfgTimeslot23valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 27),
    _Pm10001otu4CfgTimeslot23valPortn_Type()
)
pm10001otu4CfgTimeslot23valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot23valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot24valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot24valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot24valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot24valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot24valPortn = _Pm10001otu4CfgTimeslot24valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 28),
    _Pm10001otu4CfgTimeslot24valPortn_Type()
)
pm10001otu4CfgTimeslot24valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot24valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot25valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot25valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot25valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot25valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot25valPortn = _Pm10001otu4CfgTimeslot25valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 29),
    _Pm10001otu4CfgTimeslot25valPortn_Type()
)
pm10001otu4CfgTimeslot25valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot25valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot26valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot26valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot26valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot26valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot26valPortn = _Pm10001otu4CfgTimeslot26valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 30),
    _Pm10001otu4CfgTimeslot26valPortn_Type()
)
pm10001otu4CfgTimeslot26valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot26valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot27valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot27valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot27valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot27valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot27valPortn = _Pm10001otu4CfgTimeslot27valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 31),
    _Pm10001otu4CfgTimeslot27valPortn_Type()
)
pm10001otu4CfgTimeslot27valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot27valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot28valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot28valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot28valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot28valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot28valPortn = _Pm10001otu4CfgTimeslot28valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 32),
    _Pm10001otu4CfgTimeslot28valPortn_Type()
)
pm10001otu4CfgTimeslot28valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot28valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot29valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot29valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot29valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot29valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot29valPortn = _Pm10001otu4CfgTimeslot29valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 33),
    _Pm10001otu4CfgTimeslot29valPortn_Type()
)
pm10001otu4CfgTimeslot29valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot29valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot30valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot30valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot30valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot30valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot30valPortn = _Pm10001otu4CfgTimeslot30valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 34),
    _Pm10001otu4CfgTimeslot30valPortn_Type()
)
pm10001otu4CfgTimeslot30valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot30valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot31valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot31valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot31valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot31valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot31valPortn = _Pm10001otu4CfgTimeslot31valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 35),
    _Pm10001otu4CfgTimeslot31valPortn_Type()
)
pm10001otu4CfgTimeslot31valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot31valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot32valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot32valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot32valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot32valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot32valPortn = _Pm10001otu4CfgTimeslot32valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 36),
    _Pm10001otu4CfgTimeslot32valPortn_Type()
)
pm10001otu4CfgTimeslot32valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot32valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot33valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot33valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot33valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot33valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot33valPortn = _Pm10001otu4CfgTimeslot33valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 37),
    _Pm10001otu4CfgTimeslot33valPortn_Type()
)
pm10001otu4CfgTimeslot33valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot33valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot34valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot34valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot34valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot34valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot34valPortn = _Pm10001otu4CfgTimeslot34valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 38),
    _Pm10001otu4CfgTimeslot34valPortn_Type()
)
pm10001otu4CfgTimeslot34valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot34valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot35valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot35valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot35valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot35valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot35valPortn = _Pm10001otu4CfgTimeslot35valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 39),
    _Pm10001otu4CfgTimeslot35valPortn_Type()
)
pm10001otu4CfgTimeslot35valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot35valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot36valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot36valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot36valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot36valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot36valPortn = _Pm10001otu4CfgTimeslot36valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 40),
    _Pm10001otu4CfgTimeslot36valPortn_Type()
)
pm10001otu4CfgTimeslot36valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot36valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot37valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot37valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot37valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot37valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot37valPortn = _Pm10001otu4CfgTimeslot37valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 41),
    _Pm10001otu4CfgTimeslot37valPortn_Type()
)
pm10001otu4CfgTimeslot37valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot37valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot38valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot38valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot38valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot38valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot38valPortn = _Pm10001otu4CfgTimeslot38valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 42),
    _Pm10001otu4CfgTimeslot38valPortn_Type()
)
pm10001otu4CfgTimeslot38valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot38valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot39valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot39valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot39valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot39valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot39valPortn = _Pm10001otu4CfgTimeslot39valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 43),
    _Pm10001otu4CfgTimeslot39valPortn_Type()
)
pm10001otu4CfgTimeslot39valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot39valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot40valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot40valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot40valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot40valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot40valPortn = _Pm10001otu4CfgTimeslot40valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 44),
    _Pm10001otu4CfgTimeslot40valPortn_Type()
)
pm10001otu4CfgTimeslot40valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot40valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot41valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot41valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot41valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot41valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot41valPortn = _Pm10001otu4CfgTimeslot41valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 45),
    _Pm10001otu4CfgTimeslot41valPortn_Type()
)
pm10001otu4CfgTimeslot41valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot41valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot42valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot42valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot42valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot42valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot42valPortn = _Pm10001otu4CfgTimeslot42valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 46),
    _Pm10001otu4CfgTimeslot42valPortn_Type()
)
pm10001otu4CfgTimeslot42valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot42valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot43valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot43valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot43valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot43valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot43valPortn = _Pm10001otu4CfgTimeslot43valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 47),
    _Pm10001otu4CfgTimeslot43valPortn_Type()
)
pm10001otu4CfgTimeslot43valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot43valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot44valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot44valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot44valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot44valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot44valPortn = _Pm10001otu4CfgTimeslot44valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 48),
    _Pm10001otu4CfgTimeslot44valPortn_Type()
)
pm10001otu4CfgTimeslot44valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot44valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot45valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot45valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot45valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot45valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot45valPortn = _Pm10001otu4CfgTimeslot45valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 49),
    _Pm10001otu4CfgTimeslot45valPortn_Type()
)
pm10001otu4CfgTimeslot45valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot45valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot46valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot46valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot46valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot46valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot46valPortn = _Pm10001otu4CfgTimeslot46valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 50),
    _Pm10001otu4CfgTimeslot46valPortn_Type()
)
pm10001otu4CfgTimeslot46valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot46valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot47valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot47valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot47valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot47valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot47valPortn = _Pm10001otu4CfgTimeslot47valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 51),
    _Pm10001otu4CfgTimeslot47valPortn_Type()
)
pm10001otu4CfgTimeslot47valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot47valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot48valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot48valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot48valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot48valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot48valPortn = _Pm10001otu4CfgTimeslot48valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 52),
    _Pm10001otu4CfgTimeslot48valPortn_Type()
)
pm10001otu4CfgTimeslot48valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot48valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot49valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot49valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot49valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot49valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot49valPortn = _Pm10001otu4CfgTimeslot49valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 53),
    _Pm10001otu4CfgTimeslot49valPortn_Type()
)
pm10001otu4CfgTimeslot49valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot49valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot50valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot50valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot50valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot50valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot50valPortn = _Pm10001otu4CfgTimeslot50valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 54),
    _Pm10001otu4CfgTimeslot50valPortn_Type()
)
pm10001otu4CfgTimeslot50valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot50valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot51valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot51valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot51valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot51valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot51valPortn = _Pm10001otu4CfgTimeslot51valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 55),
    _Pm10001otu4CfgTimeslot51valPortn_Type()
)
pm10001otu4CfgTimeslot51valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot51valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot52valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot52valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot52valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot52valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot52valPortn = _Pm10001otu4CfgTimeslot52valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 56),
    _Pm10001otu4CfgTimeslot52valPortn_Type()
)
pm10001otu4CfgTimeslot52valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot52valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot53valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot53valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot53valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot53valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot53valPortn = _Pm10001otu4CfgTimeslot53valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 57),
    _Pm10001otu4CfgTimeslot53valPortn_Type()
)
pm10001otu4CfgTimeslot53valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot53valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot54valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot54valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot54valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot54valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot54valPortn = _Pm10001otu4CfgTimeslot54valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 58),
    _Pm10001otu4CfgTimeslot54valPortn_Type()
)
pm10001otu4CfgTimeslot54valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot54valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot55valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot55valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot55valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot55valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot55valPortn = _Pm10001otu4CfgTimeslot55valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 59),
    _Pm10001otu4CfgTimeslot55valPortn_Type()
)
pm10001otu4CfgTimeslot55valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot55valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot56valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot56valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot56valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot56valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot56valPortn = _Pm10001otu4CfgTimeslot56valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 60),
    _Pm10001otu4CfgTimeslot56valPortn_Type()
)
pm10001otu4CfgTimeslot56valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot56valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot57valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot57valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot57valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot57valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot57valPortn = _Pm10001otu4CfgTimeslot57valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 61),
    _Pm10001otu4CfgTimeslot57valPortn_Type()
)
pm10001otu4CfgTimeslot57valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot57valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot58valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot58valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot58valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot58valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot58valPortn = _Pm10001otu4CfgTimeslot58valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 62),
    _Pm10001otu4CfgTimeslot58valPortn_Type()
)
pm10001otu4CfgTimeslot58valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot58valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot59valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot59valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot59valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot59valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot59valPortn = _Pm10001otu4CfgTimeslot59valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 63),
    _Pm10001otu4CfgTimeslot59valPortn_Type()
)
pm10001otu4CfgTimeslot59valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot59valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot60valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot60valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot60valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot60valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot60valPortn = _Pm10001otu4CfgTimeslot60valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 64),
    _Pm10001otu4CfgTimeslot60valPortn_Type()
)
pm10001otu4CfgTimeslot60valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot60valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot61valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot61valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot61valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot61valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot61valPortn = _Pm10001otu4CfgTimeslot61valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 65),
    _Pm10001otu4CfgTimeslot61valPortn_Type()
)
pm10001otu4CfgTimeslot61valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot61valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot62valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot62valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot62valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot62valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot62valPortn = _Pm10001otu4CfgTimeslot62valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 66),
    _Pm10001otu4CfgTimeslot62valPortn_Type()
)
pm10001otu4CfgTimeslot62valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot62valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot63valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot63valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot63valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot63valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot63valPortn = _Pm10001otu4CfgTimeslot63valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 67),
    _Pm10001otu4CfgTimeslot63valPortn_Type()
)
pm10001otu4CfgTimeslot63valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot63valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot64valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot64valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot64valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot64valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot64valPortn = _Pm10001otu4CfgTimeslot64valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 68),
    _Pm10001otu4CfgTimeslot64valPortn_Type()
)
pm10001otu4CfgTimeslot64valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot64valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot65valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot65valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot65valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot65valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot65valPortn = _Pm10001otu4CfgTimeslot65valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 69),
    _Pm10001otu4CfgTimeslot65valPortn_Type()
)
pm10001otu4CfgTimeslot65valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot65valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot66valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot66valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot66valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot66valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot66valPortn = _Pm10001otu4CfgTimeslot66valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 70),
    _Pm10001otu4CfgTimeslot66valPortn_Type()
)
pm10001otu4CfgTimeslot66valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot66valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot67valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot67valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot67valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot67valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot67valPortn = _Pm10001otu4CfgTimeslot67valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 71),
    _Pm10001otu4CfgTimeslot67valPortn_Type()
)
pm10001otu4CfgTimeslot67valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot67valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot68valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot68valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot68valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot68valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot68valPortn = _Pm10001otu4CfgTimeslot68valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 72),
    _Pm10001otu4CfgTimeslot68valPortn_Type()
)
pm10001otu4CfgTimeslot68valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot68valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot69valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot69valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot69valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot69valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot69valPortn = _Pm10001otu4CfgTimeslot69valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 73),
    _Pm10001otu4CfgTimeslot69valPortn_Type()
)
pm10001otu4CfgTimeslot69valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot69valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot70valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot70valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot70valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot70valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot70valPortn = _Pm10001otu4CfgTimeslot70valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 74),
    _Pm10001otu4CfgTimeslot70valPortn_Type()
)
pm10001otu4CfgTimeslot70valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot70valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot71valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot71valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot71valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot71valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot71valPortn = _Pm10001otu4CfgTimeslot71valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 75),
    _Pm10001otu4CfgTimeslot71valPortn_Type()
)
pm10001otu4CfgTimeslot71valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot71valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot72valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot72valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot72valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot72valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot72valPortn = _Pm10001otu4CfgTimeslot72valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 76),
    _Pm10001otu4CfgTimeslot72valPortn_Type()
)
pm10001otu4CfgTimeslot72valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot72valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot73valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot73valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot73valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot73valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot73valPortn = _Pm10001otu4CfgTimeslot73valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 77),
    _Pm10001otu4CfgTimeslot73valPortn_Type()
)
pm10001otu4CfgTimeslot73valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot73valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot74valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot74valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot74valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot74valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot74valPortn = _Pm10001otu4CfgTimeslot74valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 78),
    _Pm10001otu4CfgTimeslot74valPortn_Type()
)
pm10001otu4CfgTimeslot74valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot74valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot75valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot75valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot75valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot75valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot75valPortn = _Pm10001otu4CfgTimeslot75valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 79),
    _Pm10001otu4CfgTimeslot75valPortn_Type()
)
pm10001otu4CfgTimeslot75valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot75valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot76valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot76valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot76valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot76valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot76valPortn = _Pm10001otu4CfgTimeslot76valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 80),
    _Pm10001otu4CfgTimeslot76valPortn_Type()
)
pm10001otu4CfgTimeslot76valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot76valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot77valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot77valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot77valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot77valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot77valPortn = _Pm10001otu4CfgTimeslot77valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 81),
    _Pm10001otu4CfgTimeslot77valPortn_Type()
)
pm10001otu4CfgTimeslot77valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot77valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot78valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot78valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot78valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot78valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot78valPortn = _Pm10001otu4CfgTimeslot78valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 82),
    _Pm10001otu4CfgTimeslot78valPortn_Type()
)
pm10001otu4CfgTimeslot78valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot78valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot79valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot79valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot79valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot79valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot79valPortn = _Pm10001otu4CfgTimeslot79valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 83),
    _Pm10001otu4CfgTimeslot79valPortn_Type()
)
pm10001otu4CfgTimeslot79valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot79valPortn.setStatus("current")


class _Pm10001otu4CfgTimeslot80valPortn_Type(Unsigned32):
    """Custom type pm10001otu4CfgTimeslot80valPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10001otu4CfgTimeslot80valPortn_Type.__name__ = "Unsigned32"
_Pm10001otu4CfgTimeslot80valPortn_Object = MibTableColumn
pm10001otu4CfgTimeslot80valPortn = _Pm10001otu4CfgTimeslot80valPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 7, 1, 1, 84),
    _Pm10001otu4CfgTimeslot80valPortn_Type()
)
pm10001otu4CfgTimeslot80valPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4CfgTimeslot80valPortn.setStatus("current")
_Pm10001otu4CfgWriteConfiguration_Type = EkiOnOff
_Pm10001otu4CfgWriteConfiguration_Object = MibScalar
pm10001otu4CfgWriteConfiguration = _Pm10001otu4CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 9, 257),
    _Pm10001otu4CfgWriteConfiguration_Type()
)
pm10001otu4CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4CfgWriteConfiguration.setStatus("current")
_Pm10001otu4traps_ObjectIdentity = ObjectIdentity
pm10001otu4traps = _Pm10001otu4traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10)
)


class _Pm10001otu4trapPortNumber_Type(Integer32):
    """Custom type pm10001otu4trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10001otu4trapPortNumber_Type.__name__ = "Integer32"
_Pm10001otu4trapPortNumber_Object = MibScalar
pm10001otu4trapPortNumber = _Pm10001otu4trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 2),
    _Pm10001otu4trapPortNumber_Type()
)
pm10001otu4trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4trapPortNumber.setStatus("current")


class _Pm10001otu4trapLineNumber_Type(Integer32):
    """Custom type pm10001otu4trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10001otu4trapLineNumber_Type.__name__ = "Integer32"
_Pm10001otu4trapLineNumber_Object = MibScalar
pm10001otu4trapLineNumber = _Pm10001otu4trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 3),
    _Pm10001otu4trapLineNumber_Type()
)
pm10001otu4trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4trapLineNumber.setStatus("current")


class _Pm10001otu4trapBoardNumber_Type(Integer32):
    """Custom type pm10001otu4trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10001otu4trapBoardNumber_Type.__name__ = "Integer32"
_Pm10001otu4trapBoardNumber_Object = MibScalar
pm10001otu4trapBoardNumber = _Pm10001otu4trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 4),
    _Pm10001otu4trapBoardNumber_Type()
)
pm10001otu4trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4trapBoardNumber.setStatus("current")
_Pm10001otu4Monitoring_ObjectIdentity = ObjectIdentity
pm10001otu4Monitoring = _Pm10001otu4Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11)
)
_Pm10001otu4MonOther_ObjectIdentity = ObjectIdentity
pm10001otu4MonOther = _Pm10001otu4MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 1)
)
_Pm10001otu4MonRmon_ObjectIdentity = ObjectIdentity
pm10001otu4MonRmon = _Pm10001otu4MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 1, 3)
)
_Pm10001otu4MonClient_ObjectIdentity = ObjectIdentity
pm10001otu4MonClient = _Pm10001otu4MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2)
)
_Pm10001otu4MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm10001otu4MonClientRmonCounter = _Pm10001otu4MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4)
)
_Pm10001otu4MonupRmonBytesCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonBytesCounterClientInputTable = _Pm10001otu4MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonBytesCounterClientInputEntry = _Pm10001otu4MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 16, 1)
)
pm10001otu4MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonBytesCounterClientInputIndex = _Pm10001otu4MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 16, 1, 1),
    _Pm10001otu4MonupRmonBytesCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonBytesCounterClientInputValuePortn = _Pm10001otu4MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 16, 1, 2),
    _Pm10001otu4MonupRmonBytesCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonBytesCounterClientInputErrorPortn = _Pm10001otu4MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 16, 1, 3),
    _Pm10001otu4MonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 16, 1, 4),
    _Pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonCrcErrorsCounterClientInputTable = _Pm10001otu4MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry = _Pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 32, 1)
)
pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex = _Pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 32, 1, 1),
    _Pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn = _Pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 32, 1, 2),
    _Pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 32, 1, 3),
    _Pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 32, 1, 4),
    _Pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonPacketsCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonPacketsCounterClientInputTable = _Pm10001otu4MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonPacketsCounterClientInputEntry = _Pm10001otu4MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 48, 1)
)
pm10001otu4MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonPacketsCounterClientInputIndex = _Pm10001otu4MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 48, 1, 1),
    _Pm10001otu4MonupRmonPacketsCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonPacketsCounterClientInputValuePortn = _Pm10001otu4MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 48, 1, 2),
    _Pm10001otu4MonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn = _Pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 48, 1, 3),
    _Pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 48, 1, 4),
    _Pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonBroadcastCounterClientInputTable = _Pm10001otu4MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonBroadcastCounterClientInputEntry = _Pm10001otu4MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 64, 1)
)
pm10001otu4MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonBroadcastCounterClientInputIndex = _Pm10001otu4MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 64, 1, 1),
    _Pm10001otu4MonupRmonBroadcastCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn = _Pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 64, 1, 2),
    _Pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn = _Pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 64, 1, 3),
    _Pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 64, 1, 4),
    _Pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonMulticastCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonMulticastCounterClientInputTable = _Pm10001otu4MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonMulticastCounterClientInputEntry = _Pm10001otu4MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 80, 1)
)
pm10001otu4MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonMulticastCounterClientInputIndex = _Pm10001otu4MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 80, 1, 1),
    _Pm10001otu4MonupRmonMulticastCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonMulticastCounterClientInputValuePortn = _Pm10001otu4MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 80, 1, 2),
    _Pm10001otu4MonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn = _Pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 80, 1, 3),
    _Pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 80, 1, 4),
    _Pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonPauseFrameCounterClientInputTable = _Pm10001otu4MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonPauseFrameCounterClientInputEntry = _Pm10001otu4MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 96, 1)
)
pm10001otu4MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonPauseFrameCounterClientInputIndex = _Pm10001otu4MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 96, 1, 1),
    _Pm10001otu4MonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn = _Pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 96, 1, 2),
    _Pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn = _Pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 96, 1, 3),
    _Pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 96, 1, 4),
    _Pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonUnicastCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonUnicastCounterClientInputTable = _Pm10001otu4MonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 160)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonUnicastCounterClientInputEntry = _Pm10001otu4MonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 160, 1)
)
pm10001otu4MonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonUnicastCounterClientInputIndex = _Pm10001otu4MonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 160, 1, 1),
    _Pm10001otu4MonupRmonUnicastCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonUnicastCounterClientInputValuePortn = _Pm10001otu4MonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 160, 1, 2),
    _Pm10001otu4MonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn = _Pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 160, 1, 3),
    _Pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 160, 1, 4),
    _Pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm10001otu4MonupRmonNonunicastCounterClientInputTable = _Pm10001otu4MonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm10001otu4MonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm10001otu4MonupRmonNonunicastCounterClientInputEntry = _Pm10001otu4MonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 176, 1)
)
pm10001otu4MonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm10001otu4MonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10001otu4MonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm10001otu4MonupRmonNonunicastCounterClientInputIndex = _Pm10001otu4MonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 176, 1, 1),
    _Pm10001otu4MonupRmonNonunicastCounterClientInputIndex_Type()
)
pm10001otu4MonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn = _Pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 176, 1, 2),
    _Pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn = _Pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 176, 1, 3),
    _Pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn = _Pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 176, 1, 4),
    _Pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonBytesCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonBytesCounterClientOutputTable = _Pm10001otu4MondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonBytesCounterClientOutputEntry = _Pm10001otu4MondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 208, 1)
)
pm10001otu4MondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonBytesCounterClientOutputIndex = _Pm10001otu4MondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 208, 1, 1),
    _Pm10001otu4MondownRmonBytesCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonBytesCounterClientOutputValuePortn = _Pm10001otu4MondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 208, 1, 2),
    _Pm10001otu4MondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 208, 1, 3),
    _Pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 208, 1, 4),
    _Pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonCrcErrorsCounterClientOutputTable = _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry = _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 224, 1)
)
pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex = _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 224, 1, 1),
    _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 224, 1, 2),
    _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 224, 1, 3),
    _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 224, 1, 4),
    _Pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonPacketsCounterClientOutputTable = _Pm10001otu4MondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonPacketsCounterClientOutputEntry = _Pm10001otu4MondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 240, 1)
)
pm10001otu4MondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonPacketsCounterClientOutputIndex = _Pm10001otu4MondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 240, 1, 1),
    _Pm10001otu4MondownRmonPacketsCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn = _Pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 240, 1, 2),
    _Pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 240, 1, 3),
    _Pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 240, 1, 4),
    _Pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonBroadcastCounterClientOutputTable = _Pm10001otu4MondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 256)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonBroadcastCounterClientOutputEntry = _Pm10001otu4MondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 256, 1)
)
pm10001otu4MondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonBroadcastCounterClientOutputIndex = _Pm10001otu4MondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 256, 1, 1),
    _Pm10001otu4MondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn = _Pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 256, 1, 2),
    _Pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 256, 1, 3),
    _Pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 256, 1, 4),
    _Pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonMulticastCounterClientOutputTable = _Pm10001otu4MondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 272)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonMulticastCounterClientOutputEntry = _Pm10001otu4MondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 272, 1)
)
pm10001otu4MondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonMulticastCounterClientOutputIndex = _Pm10001otu4MondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 272, 1, 1),
    _Pm10001otu4MondownRmonMulticastCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn = _Pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 272, 1, 2),
    _Pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 272, 1, 3),
    _Pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 272, 1, 4),
    _Pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonPauseFrameCounterClientOutputTable = _Pm10001otu4MondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 288)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry = _Pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 288, 1)
)
pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex = _Pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 288, 1, 1),
    _Pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn = _Pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 288, 1, 2),
    _Pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 288, 1, 3),
    _Pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 288, 1, 4),
    _Pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonUnicastCounterClientOutputTable = _Pm10001otu4MondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 352)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonUnicastCounterClientOutputEntry = _Pm10001otu4MondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 352, 1)
)
pm10001otu4MondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonUnicastCounterClientOutputIndex = _Pm10001otu4MondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 352, 1, 1),
    _Pm10001otu4MondownRmonUnicastCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn = _Pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 352, 1, 2),
    _Pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 352, 1, 3),
    _Pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 352, 1, 4),
    _Pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm10001otu4MondownRmonNonunicastCounterClientOutputTable = _Pm10001otu4MondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 368)
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm10001otu4MondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm10001otu4MondownRmonNonunicastCounterClientOutputEntry = _Pm10001otu4MondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 368, 1)
)
pm10001otu4MondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4MondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm10001otu4MondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm10001otu4MondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4MondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm10001otu4MondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm10001otu4MondownRmonNonunicastCounterClientOutputIndex = _Pm10001otu4MondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 368, 1, 1),
    _Pm10001otu4MondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm10001otu4MondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn = _Pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 368, 1, 2),
    _Pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn = _Pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 368, 1, 3),
    _Pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 2, 4, 368, 1, 4),
    _Pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm10001otu4MonPerfOther_ObjectIdentity = ObjectIdentity
pm10001otu4MonPerfOther = _Pm10001otu4MonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5)
)
_Pm10001otu4MonPerfSync_ObjectIdentity = ObjectIdentity
pm10001otu4MonPerfSync = _Pm10001otu4MonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 1)
)
_Pm10001otu4PerfEnable_Type = EkiOnOff
_Pm10001otu4PerfEnable_Object = MibScalar
pm10001otu4PerfEnable = _Pm10001otu4PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 1, 257),
    _Pm10001otu4PerfEnable_Type()
)
pm10001otu4PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4PerfEnable.setStatus("current")
_Pm10001otu4Perf15minSync_Type = EkiOnOff
_Pm10001otu4Perf15minSync_Object = MibScalar
pm10001otu4Perf15minSync = _Pm10001otu4Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 1, 259),
    _Pm10001otu4Perf15minSync_Type()
)
pm10001otu4Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Perf15minSync.setStatus("current")
_Pm10001otu4Perf24hSync_Type = EkiOnOff
_Pm10001otu4Perf24hSync_Object = MibScalar
pm10001otu4Perf24hSync = _Pm10001otu4Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 1, 260),
    _Pm10001otu4Perf24hSync_Type()
)
pm10001otu4Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Perf24hSync.setStatus("current")
_Pm10001otu4MonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm10001otu4MonPerfTimeStamp = _Pm10001otu4MonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2)
)
_Pm10001otu4Perf15MinShort_Type = EkiOnOff
_Pm10001otu4Perf15MinShort_Object = MibScalar
pm10001otu4Perf15MinShort = _Pm10001otu4Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2, 1),
    _Pm10001otu4Perf15MinShort_Type()
)
pm10001otu4Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Perf15MinShort.setStatus("current")
_Pm10001otu4Perf15MinLong_Type = EkiOnOff
_Pm10001otu4Perf15MinLong_Object = MibScalar
pm10001otu4Perf15MinLong = _Pm10001otu4Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2, 2),
    _Pm10001otu4Perf15MinLong_Type()
)
pm10001otu4Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Perf15MinLong.setStatus("current")
_Pm10001otu4Perf24HoursShort_Type = Counter32
_Pm10001otu4Perf24HoursShort_Object = MibScalar
pm10001otu4Perf24HoursShort = _Pm10001otu4Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2, 5),
    _Pm10001otu4Perf24HoursShort_Type()
)
pm10001otu4Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Perf24HoursShort.setStatus("current")
_Pm10001otu4Perf24HoursLong_Type = Counter32
_Pm10001otu4Perf24HoursLong_Object = MibScalar
pm10001otu4Perf24HoursLong = _Pm10001otu4Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2, 6),
    _Pm10001otu4Perf24HoursLong_Type()
)
pm10001otu4Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4Perf24HoursLong.setStatus("current")
_Pm10001otu4PerfCurrent15MinElapsedTime_Type = Counter32
_Pm10001otu4PerfCurrent15MinElapsedTime_Object = MibScalar
pm10001otu4PerfCurrent15MinElapsedTime = _Pm10001otu4PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2, 7),
    _Pm10001otu4PerfCurrent15MinElapsedTime_Type()
)
pm10001otu4PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4PerfCurrent15MinElapsedTime.setStatus("current")
_Pm10001otu4PerfCurrent24HoursElapsedTime_Type = Counter32
_Pm10001otu4PerfCurrent24HoursElapsedTime_Object = MibScalar
pm10001otu4PerfCurrent24HoursElapsedTime = _Pm10001otu4PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 5, 2, 8),
    _Pm10001otu4PerfCurrent24HoursElapsedTime_Type()
)
pm10001otu4PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10001otu4PerfCurrent24HoursElapsedTime.setStatus("current")
_Pm10001otu4MonPerfClient_ObjectIdentity = ObjectIdentity
pm10001otu4MonPerfClient = _Pm10001otu4MonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6)
)
_Pm10001otu4PerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm10001otu4PerfTelecomInputClientCurrent15StatTable = _Pm10001otu4PerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomInputClientCurrent15StatEntry = _Pm10001otu4PerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1)
)
pm10001otu4PerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatIndex = _Pm10001otu4PerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 1),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatIndex_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 2),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 3),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 4),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 5),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 6),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 7),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 8),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 9),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 10),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 16, 1, 11),
    _Pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Table = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1)
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 1),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 2),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 3),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 4),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 5),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 6),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 7),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 8),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 9),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 10),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 32, 1, 11),
    _Pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm10001otu4PerfTelecomInputClientCurrent24StatTable = _Pm10001otu4PerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomInputClientCurrent24StatEntry = _Pm10001otu4PerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1)
)
pm10001otu4PerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatIndex = _Pm10001otu4PerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 1),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatIndex_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 2),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 3),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 4),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 5),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 6),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 7),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 8),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 9),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 10),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn = _Pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 48, 1, 11),
    _Pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Table = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1)
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 1),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 2),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 3),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 4),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 5),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 6),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 7),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 8),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 9),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 10),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 64, 1, 11),
    _Pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm10001otu4PerfTelecomOutputClientCurrent15StatTable = _Pm10001otu4PerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomOutputClientCurrent15StatEntry = _Pm10001otu4PerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1)
)
pm10001otu4PerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatIndex = _Pm10001otu4PerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 1),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 2),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 3),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 4),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 5),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 6),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 7),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 8),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 9),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 10),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 80, 1, 11),
    _Pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1)
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 1),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 2),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 3),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 4),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 5),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 6),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 7),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 8),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 9),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 10),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 96, 1, 11),
    _Pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm10001otu4PerfTelecomOutputClientCurrent24StatTable = _Pm10001otu4PerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomOutputClientCurrent24StatEntry = _Pm10001otu4PerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1)
)
pm10001otu4PerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatIndex = _Pm10001otu4PerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 1),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 2),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 3),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 4),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 5),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 6),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 7),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 8),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 9),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 10),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 112, 1, 11),
    _Pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1)
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 1),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 2),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 3),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 4),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 5),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 6),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 7),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 8),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 9),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 10),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 128, 1, 11),
    _Pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10001otu4PerfDatacomClientCurrent15StatTable_Object = MibTable
pm10001otu4PerfDatacomClientCurrent15StatTable = _Pm10001otu4PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm10001otu4PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm10001otu4PerfDatacomClientCurrent15StatEntry = _Pm10001otu4PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1)
)
pm10001otu4PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm10001otu4PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm10001otu4PerfDatacomClientCurrent15StatIndex = _Pm10001otu4PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 1),
    _Pm10001otu4PerfDatacomClientCurrent15StatIndex_Type()
)
pm10001otu4PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn = _Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 4),
    _Rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInCrcCountPortn = _Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 5),
    _Rm10010perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn = _Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 6),
    _Rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatInPacketCountPortn = _Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 7),
    _Rm10010perfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn = _Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 28),
    _Rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutCrcCountPortn = _Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 29),
    _Rm10010perfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn = _Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 30),
    _Rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent15StatOutPacketCountPortn = _Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 432, 1, 31),
    _Rm10010perfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfDatacomClientPast15StatHistoryPort1Table = _Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry = _Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1)
)
pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index = _Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 1),
    _Pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInCrcCountInvPort1 = _Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 4),
    _Rm10010perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInCrcCountPort1 = _Rm10010perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 5),
    _Rm10010perfdatacomclientPast15StatInCrcCountPort1_Type()
)
rm10010perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInPacketCountInvPort1 = _Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 6),
    _Rm10010perfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatInPacketCountPort1 = _Rm10010perfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 7),
    _Rm10010perfdatacomclientPast15StatInPacketCountPort1_Type()
)
rm10010perfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutCrcCountInvPort1 = _Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 28),
    _Rm10010perfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutCrcCountPort1 = _Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 29),
    _Rm10010perfdatacomclientPast15StatOutCrcCountPort1_Type()
)
rm10010perfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutPacketCountInvPort1 = _Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 30),
    _Rm10010perfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast15StatOutPacketCountPort1 = _Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 448, 1, 31),
    _Rm10010perfdatacomclientPast15StatOutPacketCountPort1_Type()
)
rm10010perfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm10001otu4PerfDatacomClientCurrent24StatTable_Object = MibTable
pm10001otu4PerfDatacomClientCurrent24StatTable = _Pm10001otu4PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm10001otu4PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm10001otu4PerfDatacomClientCurrent24StatEntry = _Pm10001otu4PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1)
)
pm10001otu4PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm10001otu4PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm10001otu4PerfDatacomClientCurrent24StatIndex = _Pm10001otu4PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 1),
    _Pm10001otu4PerfDatacomClientCurrent24StatIndex_Type()
)
pm10001otu4PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn = _Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 4),
    _Rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInCrcCountPortn = _Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 5),
    _Rm10010perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn = _Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 6),
    _Rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatInPacketCountPortn = _Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 7),
    _Rm10010perfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn = _Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 28),
    _Rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutCrcCountPortn = _Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 29),
    _Rm10010perfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn = _Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 30),
    _Rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
rm10010perfdatacomclientCurrent24StatOutPacketCountPortn = _Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 464, 1, 31),
    _Rm10010perfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
rm10010perfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfDatacomClientPast24StatHistoryPort1Table = _Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry = _Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1)
)
pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index = _Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 1),
    _Pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInCrcCountInvPort1 = _Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 4),
    _Rm10010perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInCrcCountPort1 = _Rm10010perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 5),
    _Rm10010perfdatacomclientPast24StatInCrcCountPort1_Type()
)
rm10010perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInPacketCountInvPort1 = _Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 6),
    _Rm10010perfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatInPacketCountPort1 = _Rm10010perfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 7),
    _Rm10010perfdatacomclientPast24StatInPacketCountPort1_Type()
)
rm10010perfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutCrcCountInvPort1 = _Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 28),
    _Rm10010perfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutCrcCountPort1 = _Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 29),
    _Rm10010perfdatacomclientPast24StatOutCrcCountPort1_Type()
)
rm10010perfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutPacketCountInvPort1 = _Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 30),
    _Rm10010perfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
rm10010perfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
rm10010perfdatacomclientPast24StatOutPacketCountPort1 = _Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 6, 480, 1, 31),
    _Rm10010perfdatacomclientPast24StatOutPacketCountPort1_Type()
)
rm10010perfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rm10010perfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm10001otu4MonPerfLine_ObjectIdentity = ObjectIdentity
pm10001otu4MonPerfLine = _Pm10001otu4MonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7)
)
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm10001otu4PerfTelecomLinePostFecCurrent15StatTable = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1)
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 1),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 2),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 3),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 4),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 5),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 6),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 7),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 8),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 9),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 10),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 192, 1, 11),
    _Pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1)
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 1),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 2),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 3),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 4),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 5),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 6),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 7),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 8),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 9),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 10),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 193, 1, 11),
    _Pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm10001otu4PerfTelecomLinePostFecCurrent24StatTable = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1)
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 1),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 2),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 3),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 4),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 5),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 6),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 7),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 8),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 9),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 10),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 194, 1, 11),
    _Pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1)
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 1),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 2),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 3),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 4),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 5),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 6),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 7),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 8),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 9),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 10),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 195, 1, 11),
    _Pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatTable = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1)
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 1),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 2),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 3),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 4),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 5),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 6),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 208, 1, 7),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1)
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 1),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 2),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 3),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 4),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 5),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 6),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 209, 1, 7),
    _Pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatTable = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1)
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 1),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 2),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 3),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 4),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 5),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 6),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 210, 1, 7),
    _Pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211)
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1)
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm10001otu4-MIB", "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 1),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 2),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 3),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 4),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 5),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 6),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 82, 11, 7, 211, 1, 7),
    _Pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm10001otu4LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 30)
)
pm10001otu4LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapLineNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10001otu4LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 31)
)
pm10001otu4LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapLineNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10001otu4LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 32)
)
pm10001otu4LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapLineNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10001otu4LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 33)
)
pm10001otu4LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapLineNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10001otu4LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 34)
)
pm10001otu4LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineFailPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineHwFailPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapLineNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4LineTrapCritGoesOn.setStatus(
        "current"
    )

pm10001otu4LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 35)
)
pm10001otu4LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineFailPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmLineHwFailPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapLineNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4LineTrapCritGoesOff.setStatus(
        "current"
    )

pm10001otu4ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 40)
)
pm10001otu4ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapPortNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10001otu4ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 41)
)
pm10001otu4ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapPortNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10001otu4ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 42)
)
pm10001otu4ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapPortNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10001otu4ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 43)
)
pm10001otu4ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapPortNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10001otu4ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 44)
)
pm10001otu4ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmFailAccPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmHwFailAccPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapPortNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4ClientTrapCritGoesOn.setStatus(
        "current"
    )

pm10001otu4ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 45)
)
pm10001otu4ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmFailAccPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmHwFailAccPortn"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapPortNumber"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4ClientTrapCritGoesOff.setStatus(
        "current"
    )

pm10001otu4PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 50)
)
pm10001otu4PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmDefFuseB"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmDefFuseA"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10001otu4PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 82, 10, 51)
)
pm10001otu4PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmDefFuseB"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4AlmDefFuseA"),
        ("EKINOPS-Pm10001otu4-MIB", "pm10001otu4trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10001otu4PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm10001otu4-MIB",
    **{"Pm10001otu4MultiRate": Pm10001otu4MultiRate,
       "Pm10001otu4OtxMode": Pm10001otu4OtxMode,
       "Pm10001otu4OtxGrid": Pm10001otu4OtxGrid,
       "Pm10001otu4AdjustValue": Pm10001otu4AdjustValue,
       "Pm10001otu4ClientProtocol": Pm10001otu4ClientProtocol,
       "Pm10001otu4ProtocolMode": Pm10001otu4ProtocolMode,
       "Pm10001otu4OtxChannel": Pm10001otu4OtxChannel,
       "Pm10001otu4OrxChannel": Pm10001otu4OrxChannel,
       "Rm10010ClientIgnoreTimer": Rm10010ClientIgnoreTimer,
       "Pm10001otu4CompensationMode": Pm10001otu4CompensationMode,
       "modulePm10001otu4": modulePm10001otu4,
       "pm10001otu4alarms": pm10001otu4alarms,
       "pm10001otu4AlmOther": pm10001otu4AlmOther,
       "pm10001otu4AlmOtherNurg": pm10001otu4AlmOtherNurg,
       "pm10001otu4AlmsynthAlm2": pm10001otu4AlmsynthAlm2,
       "pm10001otu4AlmConfTableSave": pm10001otu4AlmConfTableSave,
       "pm10001otu4AlmInvUpload": pm10001otu4AlmInvUpload,
       "pm10001otu4AlmConfTableLoad": pm10001otu4AlmConfTableLoad,
       "pm10001otu4AlmCorrelatOff": pm10001otu4AlmCorrelatOff,
       "pm10001otu4AlmMaintenanceOn": pm10001otu4AlmMaintenanceOn,
       "pm10001otu4AlmOtherUrg": pm10001otu4AlmOtherUrg,
       "pm10001otu4AlmOtherCrit": pm10001otu4AlmOtherCrit,
       "pm10001otu4AlmsynthAlm0": pm10001otu4AlmsynthAlm0,
       "pm10001otu4AlmFailFan": pm10001otu4AlmFailFan,
       "pm10001otu4AlmModGlobFail": pm10001otu4AlmModGlobFail,
       "pm10001otu4AlmDefFuseA": pm10001otu4AlmDefFuseA,
       "pm10001otu4AlmDefFuseB": pm10001otu4AlmDefFuseB,
       "pm10001otu4AlmclientModuleState": pm10001otu4AlmclientModuleState,
       "pm10001otu4AlmCfpInitialize": pm10001otu4AlmCfpInitialize,
       "pm10001otu4AlmCfpLowPower": pm10001otu4AlmCfpLowPower,
       "pm10001otu4AlmCfpHighPowerUp": pm10001otu4AlmCfpHighPowerUp,
       "pm10001otu4AlmCfpTxOff": pm10001otu4AlmCfpTxOff,
       "pm10001otu4AlmCfpTxTurnOn": pm10001otu4AlmCfpTxTurnOn,
       "pm10001otu4AlmCfpReady": pm10001otu4AlmCfpReady,
       "pm10001otu4AlmCfpFault": pm10001otu4AlmCfpFault,
       "pm10001otu4AlmCfpTxTurnOff": pm10001otu4AlmCfpTxTurnOff,
       "pm10001otu4AlmCfpHighPowerDown": pm10001otu4AlmCfpHighPowerDown,
       "pm10001otu4AlmclientModuleGeneralStatus": pm10001otu4AlmclientModuleGeneralStatus,
       "pm10001otu4AlmCfpOutOfAlignment": pm10001otu4AlmCfpOutOfAlignment,
       "pm10001otu4AlmCfpRxNetworkLol": pm10001otu4AlmCfpRxNetworkLol,
       "pm10001otu4AlmCfpRxLos": pm10001otu4AlmCfpRxLos,
       "pm10001otu4AlmCfpTxHostLol": pm10001otu4AlmCfpTxHostLol,
       "pm10001otu4AlmCfpTxLosf": pm10001otu4AlmCfpTxLosf,
       "pm10001otu4AlmCfpTxCmuLol": pm10001otu4AlmCfpTxCmuLol,
       "pm10001otu4AlmCfpTxJitterPllLol": pm10001otu4AlmCfpTxJitterPllLol,
       "pm10001otu4AlmCfpLossOfRefclk": pm10001otu4AlmCfpLossOfRefclk,
       "pm10001otu4AlmCfpHwInterlock": pm10001otu4AlmCfpHwInterlock,
       "pm10001otu4AlmclientGlobalAlarmSummary": pm10001otu4AlmclientGlobalAlarmSummary,
       "pm10001otu4AlmCfpSoftGlobAlarmTest": pm10001otu4AlmCfpSoftGlobAlarmTest,
       "pm10001otu4AlmCfpNetworkLaneAlarmWarning2": pm10001otu4AlmCfpNetworkLaneAlarmWarning2,
       "pm10001otu4AlmCfpModuleState": pm10001otu4AlmCfpModuleState,
       "pm10001otu4AlmCfpModuleGeneralStatus": pm10001otu4AlmCfpModuleGeneralStatus,
       "pm10001otu4AlmCfpModuleFault": pm10001otu4AlmCfpModuleFault,
       "pm10001otu4AlmCfpModuleAlarmWarning1": pm10001otu4AlmCfpModuleAlarmWarning1,
       "pm10001otu4AlmCfpModuleAlarmWarning2": pm10001otu4AlmCfpModuleAlarmWarning2,
       "pm10001otu4AlmCfpNetworkLaneAlarmWarning1": pm10001otu4AlmCfpNetworkLaneAlarmWarning1,
       "pm10001otu4AlmCfpNetworkLaneFaultStatus": pm10001otu4AlmCfpNetworkLaneFaultStatus,
       "pm10001otu4AlmCfpHostLaneFaultStatus": pm10001otu4AlmCfpHostLaneFaultStatus,
       "pm10001otu4AlmCfpGlobAlarmAssertion": pm10001otu4AlmCfpGlobAlarmAssertion,
       "pm10001otu4AlmmsaModuleState": pm10001otu4AlmmsaModuleState,
       "pm10001otu4AlmMsaInitialize": pm10001otu4AlmMsaInitialize,
       "pm10001otu4AlmMsaLowPower": pm10001otu4AlmMsaLowPower,
       "pm10001otu4AlmMsaHighPowerUp": pm10001otu4AlmMsaHighPowerUp,
       "pm10001otu4AlmMsaTxOff": pm10001otu4AlmMsaTxOff,
       "pm10001otu4AlmMsaTxTurnOn": pm10001otu4AlmMsaTxTurnOn,
       "pm10001otu4AlmMsaReady": pm10001otu4AlmMsaReady,
       "pm10001otu4AlmMsaFault": pm10001otu4AlmMsaFault,
       "pm10001otu4AlmMsaTxTurnOff": pm10001otu4AlmMsaTxTurnOff,
       "pm10001otu4AlmMsaHighPowerDown": pm10001otu4AlmMsaHighPowerDown,
       "pm10001otu4AlmmsaModuleGeneralStatus": pm10001otu4AlmmsaModuleGeneralStatus,
       "pm10001otu4AlmMsaOutOfAlignment": pm10001otu4AlmMsaOutOfAlignment,
       "pm10001otu4AlmMsaRxNetworkLol": pm10001otu4AlmMsaRxNetworkLol,
       "pm10001otu4AlmMsaRxLos": pm10001otu4AlmMsaRxLos,
       "pm10001otu4AlmMsaTxHostLol": pm10001otu4AlmMsaTxHostLol,
       "pm10001otu4AlmMsaTxLosf": pm10001otu4AlmMsaTxLosf,
       "pm10001otu4AlmMsaTxCmuLol": pm10001otu4AlmMsaTxCmuLol,
       "pm10001otu4AlmMsaTxJitterPllLol": pm10001otu4AlmMsaTxJitterPllLol,
       "pm10001otu4AlmMsaLossOfRefclk": pm10001otu4AlmMsaLossOfRefclk,
       "pm10001otu4AlmMsaHwInterlock": pm10001otu4AlmMsaHwInterlock,
       "pm10001otu4AlmmsaGlobalAlarmSummary": pm10001otu4AlmmsaGlobalAlarmSummary,
       "pm10001otu4AlmMsaSoftGlobAlarmTest": pm10001otu4AlmMsaSoftGlobAlarmTest,
       "pm10001otu4AlmMsaNetworkHostAlarmStatus": pm10001otu4AlmMsaNetworkHostAlarmStatus,
       "pm10001otu4AlmMsaNetworkLaneAlarmWarning2": pm10001otu4AlmMsaNetworkLaneAlarmWarning2,
       "pm10001otu4AlmMsaModuleState": pm10001otu4AlmMsaModuleState,
       "pm10001otu4AlmMsaModuleGeneralStatus": pm10001otu4AlmMsaModuleGeneralStatus,
       "pm10001otu4AlmModuleFault": pm10001otu4AlmModuleFault,
       "pm10001otu4AlmMsaModuleAlarmWarning1": pm10001otu4AlmMsaModuleAlarmWarning1,
       "pm10001otu4AlmMsaModuleAlarmWarning2": pm10001otu4AlmMsaModuleAlarmWarning2,
       "pm10001otu4AlmMsaNetworkLaneAlarmWarning1": pm10001otu4AlmMsaNetworkLaneAlarmWarning1,
       "pm10001otu4AlmMsaNetworkLaneFaultStatus": pm10001otu4AlmMsaNetworkLaneFaultStatus,
       "pm10001otu4AlmMsaHostLaneFaultStatus": pm10001otu4AlmMsaHostLaneFaultStatus,
       "pm10001otu4AlmMsaGlobAlarmAssertion": pm10001otu4AlmMsaGlobAlarmAssertion,
       "pm10001otu4AlmmsaNetworkTxAlignment": pm10001otu4AlmmsaNetworkTxAlignment,
       "pm10001otu4AlmNetTxTimingFault": pm10001otu4AlmNetTxTimingFault,
       "pm10001otu4AlmNetTxReferenceClockFault": pm10001otu4AlmNetTxReferenceClockFault,
       "pm10001otu4AlmNetTxCmuLockFault": pm10001otu4AlmNetTxCmuLockFault,
       "pm10001otu4AlmNetTxOutOfAlignment": pm10001otu4AlmNetTxOutOfAlignment,
       "pm10001otu4AlmNetTxLossOfAlignment": pm10001otu4AlmNetTxLossOfAlignment,
       "pm10001otu4AlmmsaNetworkRxAlignment": pm10001otu4AlmmsaNetworkRxAlignment,
       "pm10001otu4AlmNetRxTimingFault": pm10001otu4AlmNetRxTimingFault,
       "pm10001otu4AlmNetRxOutOfAlignment": pm10001otu4AlmNetRxOutOfAlignment,
       "pm10001otu4AlmNetRxLossOfAlignment": pm10001otu4AlmNetRxLossOfAlignment,
       "pm10001otu4AlmNetRxModemLockFault": pm10001otu4AlmNetRxModemLockFault,
       "pm10001otu4AlmNetRxModemSyncDetectFault": pm10001otu4AlmNetRxModemSyncDetectFault,
       "pm10001otu4AlmmsaNetworkHostNetworkAlarmSummary": pm10001otu4AlmmsaNetworkHostNetworkAlarmSummary,
       "pm10001otu4AlmNetworkTxAlignment": pm10001otu4AlmNetworkTxAlignment,
       "pm10001otu4AlmNetworkRxAlignment": pm10001otu4AlmNetworkRxAlignment,
       "pm10001otu4AlmNetworkRxOtn": pm10001otu4AlmNetworkRxOtn,
       "pm10001otu4AlmHostRxAlignment": pm10001otu4AlmHostRxAlignment,
       "pm10001otu4AlmHostTxAlignment": pm10001otu4AlmHostTxAlignment,
       "pm10001otu4AlmHostTxOtnStatus": pm10001otu4AlmHostTxOtnStatus,
       "pm10001otu4AlmmsaHostTxAlignment": pm10001otu4AlmmsaHostTxAlignment,
       "pm10001otu4AlmHostTxDeskewLockFault": pm10001otu4AlmHostTxDeskewLockFault,
       "pm10001otu4AlmHostTxOutOfAlignment": pm10001otu4AlmHostTxOutOfAlignment,
       "pm10001otu4AlmHostTxLossOfAlignment": pm10001otu4AlmHostTxLossOfAlignment,
       "pm10001otu4AlmHostTxCdrLockFault": pm10001otu4AlmHostTxCdrLockFault,
       "pm10001otu4AlmmsaHostRxAlignment": pm10001otu4AlmmsaHostRxAlignment,
       "pm10001otu4AlmHostRxCmuLockFault": pm10001otu4AlmHostRxCmuLockFault,
       "pm10001otu4AlmHostRxOutOfAlignment": pm10001otu4AlmHostRxOutOfAlignment,
       "pm10001otu4AlmHostRxLossOfAlignment": pm10001otu4AlmHostRxLossOfAlignment,
       "pm10001otu4AlmClient": pm10001otu4AlmClient,
       "pm10001otu4AlmClientNurg": pm10001otu4AlmClientNurg,
       "pm10001otu4AlmclientNetworkLaneAlarmWarningTable": pm10001otu4AlmclientNetworkLaneAlarmWarningTable,
       "pm10001otu4AlmclientNetworkLaneAlarmWarningEntry": pm10001otu4AlmclientNetworkLaneAlarmWarningEntry,
       "pm10001otu4AlmclientNetworkLaneAlarmWarningIndex": pm10001otu4AlmclientNetworkLaneAlarmWarningIndex,
       "pm10001otu4AlmClientRxPowerLowAlarmPortn": pm10001otu4AlmClientRxPowerLowAlarmPortn,
       "pm10001otu4AlmClientRxPowerLowWarningPortn": pm10001otu4AlmClientRxPowerLowWarningPortn,
       "pm10001otu4AlmClientRxPowerHighWarningPortn": pm10001otu4AlmClientRxPowerHighWarningPortn,
       "pm10001otu4AlmClientRxPowerHighAlarmPortn": pm10001otu4AlmClientRxPowerHighAlarmPortn,
       "pm10001otu4AlmLaserTempLowAlarmPortn": pm10001otu4AlmLaserTempLowAlarmPortn,
       "pm10001otu4AlmClientLaserTempLowWarningPortn": pm10001otu4AlmClientLaserTempLowWarningPortn,
       "pm10001otu4AlmClientLaserTempHighWarningPortn": pm10001otu4AlmClientLaserTempHighWarningPortn,
       "pm10001otu4AlmClientLaserTempHighAlarmPortn": pm10001otu4AlmClientLaserTempHighAlarmPortn,
       "pm10001otu4AlmClientTxPowerLowAlarmPortn": pm10001otu4AlmClientTxPowerLowAlarmPortn,
       "pm10001otu4AlmClientTxPowerLowWarningPortn": pm10001otu4AlmClientTxPowerLowWarningPortn,
       "pm10001otu4AlmClientTxPowerHighWarningPortn": pm10001otu4AlmClientTxPowerHighWarningPortn,
       "pm10001otu4AlmClientTxPowerHighAlarmPortn": pm10001otu4AlmClientTxPowerHighAlarmPortn,
       "pm10001otu4AlmClientBiasLowAlarmPortn": pm10001otu4AlmClientBiasLowAlarmPortn,
       "pm10001otu4AlmClientBiasLowWarningPortn": pm10001otu4AlmClientBiasLowWarningPortn,
       "pm10001otu4AlmClientBiasHighWarningPortn": pm10001otu4AlmClientBiasHighWarningPortn,
       "pm10001otu4AlmClientBiasHighAlarmPortn": pm10001otu4AlmClientBiasHighAlarmPortn,
       "pm10001otu4AlmclientSfpWarnDdmTable": pm10001otu4AlmclientSfpWarnDdmTable,
       "pm10001otu4AlmclientSfpWarnDdmEntry": pm10001otu4AlmclientSfpWarnDdmEntry,
       "pm10001otu4AlmclientSfpWarnDdmIndex": pm10001otu4AlmclientSfpWarnDdmIndex,
       "pm10001otu4AlmTxPwLowWngPortn": pm10001otu4AlmTxPwLowWngPortn,
       "pm10001otu4AlmTxPwrHighWngPortn": pm10001otu4AlmTxPwrHighWngPortn,
       "pm10001otu4AlmTxBiasLowWngPortn": pm10001otu4AlmTxBiasLowWngPortn,
       "pm10001otu4AlmTxBiasHighWngPortn": pm10001otu4AlmTxBiasHighWngPortn,
       "pm10001otu4AlmVccLowWngPortn": pm10001otu4AlmVccLowWngPortn,
       "pm10001otu4AlmVccHighWngPortn": pm10001otu4AlmVccHighWngPortn,
       "pm10001otu4AlmTempLowWngPortn": pm10001otu4AlmTempLowWngPortn,
       "pm10001otu4AlmTempHighWngPortn": pm10001otu4AlmTempHighWngPortn,
       "pm10001otu4AlmRxPwrLowWngPortn": pm10001otu4AlmRxPwrLowWngPortn,
       "pm10001otu4AlmRxPwrHighWngPortn": pm10001otu4AlmRxPwrHighWngPortn,
       "pm10001otu4AlmClientUrg": pm10001otu4AlmClientUrg,
       "pm10001otu4AlmclientNetworkLaneFaultTable": pm10001otu4AlmclientNetworkLaneFaultTable,
       "pm10001otu4AlmclientNetworkLaneFaultEntry": pm10001otu4AlmclientNetworkLaneFaultEntry,
       "pm10001otu4AlmclientNetworkLaneFaultIndex": pm10001otu4AlmclientNetworkLaneFaultIndex,
       "pm10001otu4AlmClientLaneRxFifoErrorPortn": pm10001otu4AlmClientLaneRxFifoErrorPortn,
       "pm10001otu4AlmClientLaneRxLolPortn": pm10001otu4AlmClientLaneRxLolPortn,
       "pm10001otu4AlmClientLaneRxLosPortn": pm10001otu4AlmClientLaneRxLosPortn,
       "pm10001otu4AlmClientLaneTxLolPortn": pm10001otu4AlmClientLaneTxLolPortn,
       "pm10001otu4AlmClientLaneTxLosfPortn": pm10001otu4AlmClientLaneTxLosfPortn,
       "pm10001otu4AlmClientLaneApdPowerSupplyPortn": pm10001otu4AlmClientLaneApdPowerSupplyPortn,
       "pm10001otu4AlmClientLaneWavelengthUnlockedPortn": pm10001otu4AlmClientLaneWavelengthUnlockedPortn,
       "pm10001otu4AlmClientLaneTecFaultPortn": pm10001otu4AlmClientLaneTecFaultPortn,
       "pm10001otu4AlmclientHostLaneFaultTable": pm10001otu4AlmclientHostLaneFaultTable,
       "pm10001otu4AlmclientHostLaneFaultEntry": pm10001otu4AlmclientHostLaneFaultEntry,
       "pm10001otu4AlmclientHostLaneFaultIndex": pm10001otu4AlmclientHostLaneFaultIndex,
       "pm10001otu4AlmClientLossOfSyncPortn": pm10001otu4AlmClientLossOfSyncPortn,
       "pm10001otu4AlmClientInputLossOfSigPortn": pm10001otu4AlmClientInputLossOfSigPortn,
       "pm10001otu4AlmClientLanesMarkerUnlockPortn": pm10001otu4AlmClientLanesMarkerUnlockPortn,
       "pm10001otu4AlmClientLanes6466UnlockPortn": pm10001otu4AlmClientLanes6466UnlockPortn,
       "pm10001otu4AlmClientLanesNotAlignedPortn": pm10001otu4AlmClientLanesNotAlignedPortn,
       "pm10001otu4AlmClientCsfDetectedPortn": pm10001otu4AlmClientCsfDetectedPortn,
       "pm10001otu4AlmClientTxHostLolPortn": pm10001otu4AlmClientTxHostLolPortn,
       "pm10001otu4AlmClientLaneTxFifoErrorPortn": pm10001otu4AlmClientLaneTxFifoErrorPortn,
       "pm10001otu4AlmLfDetectedPortn": pm10001otu4AlmLfDetectedPortn,
       "pm10001otu4AlmRfDetectedPortn": pm10001otu4AlmRfDetectedPortn,
       "pm10001otu4AlmclientSfpAlmDdmTable": pm10001otu4AlmclientSfpAlmDdmTable,
       "pm10001otu4AlmclientSfpAlmDdmEntry": pm10001otu4AlmclientSfpAlmDdmEntry,
       "pm10001otu4AlmclientSfpAlmDdmIndex": pm10001otu4AlmclientSfpAlmDdmIndex,
       "pm10001otu4AlmTxPwrLowAlaPortn": pm10001otu4AlmTxPwrLowAlaPortn,
       "pm10001otu4AlmTxPwrHighAlaPortn": pm10001otu4AlmTxPwrHighAlaPortn,
       "pm10001otu4AlmTxBiasLowAlaPortn": pm10001otu4AlmTxBiasLowAlaPortn,
       "pm10001otu4AlmTxBiasHighAlaPortn": pm10001otu4AlmTxBiasHighAlaPortn,
       "pm10001otu4AlmVccLowAlaPortn": pm10001otu4AlmVccLowAlaPortn,
       "pm10001otu4AlmVccHighAlaPortn": pm10001otu4AlmVccHighAlaPortn,
       "pm10001otu4AlmTempLowAlaPortn": pm10001otu4AlmTempLowAlaPortn,
       "pm10001otu4AlmTempHighAlaPortn": pm10001otu4AlmTempHighAlaPortn,
       "pm10001otu4AlmRxPwrLowAlaPortn": pm10001otu4AlmRxPwrLowAlaPortn,
       "pm10001otu4AlmRxPwrHighAlaPortn": pm10001otu4AlmRxPwrHighAlaPortn,
       "pm10001otu4AlmClientCrit": pm10001otu4AlmClientCrit,
       "pm10001otu4AlmsynthAlmPortTable": pm10001otu4AlmsynthAlmPortTable,
       "pm10001otu4AlmsynthAlmPortEntry": pm10001otu4AlmsynthAlmPortEntry,
       "pm10001otu4AlmsynthAlmPortIndex": pm10001otu4AlmsynthAlmPortIndex,
       "pm10001otu4AlmSfpAbsentPortn": pm10001otu4AlmSfpAbsentPortn,
       "pm10001otu4AlmDdmAbsentPortn": pm10001otu4AlmDdmAbsentPortn,
       "pm10001otu4AlmHwFailAccPortn": pm10001otu4AlmHwFailAccPortn,
       "pm10001otu4AlmDwLsdPortn": pm10001otu4AlmDwLsdPortn,
       "pm10001otu4AlmClientLocalOosPortn": pm10001otu4AlmClientLocalOosPortn,
       "pm10001otu4AlmClientRemoteOosPortn": pm10001otu4AlmClientRemoteOosPortn,
       "pm10001otu4AlmDwCaisPortn": pm10001otu4AlmDwCaisPortn,
       "pm10001otu4AlmSfpDdmWarningPortn": pm10001otu4AlmSfpDdmWarningPortn,
       "pm10001otu4AlmSfpDdmAlmPortn": pm10001otu4AlmSfpDdmAlmPortn,
       "pm10001otu4AlmIdleInsertedPortn": pm10001otu4AlmIdleInsertedPortn,
       "pm10001otu4AlmFailAccPortn": pm10001otu4AlmFailAccPortn,
       "pm10001otu4AlmUpCsfPortn": pm10001otu4AlmUpCsfPortn,
       "pm10001otu4AlmLine": pm10001otu4AlmLine,
       "pm10001otu4AlmLineNurg": pm10001otu4AlmLineNurg,
       "pm10001otu4AlmlineNetworkLaneAlarmWarning1Table": pm10001otu4AlmlineNetworkLaneAlarmWarning1Table,
       "pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry": pm10001otu4AlmlineNetworkLaneAlarmWarning1Entry,
       "pm10001otu4AlmlineNetworkLaneAlarmWarning1Index": pm10001otu4AlmlineNetworkLaneAlarmWarning1Index,
       "pm10001otu4AlmLineRxPowerLowAlarmPortn": pm10001otu4AlmLineRxPowerLowAlarmPortn,
       "pm10001otu4AlmLineRxPowerLowWarningPortn": pm10001otu4AlmLineRxPowerLowWarningPortn,
       "pm10001otu4AlmLineRxPowerHighWarningPortn": pm10001otu4AlmLineRxPowerHighWarningPortn,
       "pm10001otu4AlmLineRxPowerHighAlarmPortn": pm10001otu4AlmLineRxPowerHighAlarmPortn,
       "pm10001otu4AlmLineLaserTempLowAlarmPortn": pm10001otu4AlmLineLaserTempLowAlarmPortn,
       "pm10001otu4AlmLineLaserTempLowWarningPortn": pm10001otu4AlmLineLaserTempLowWarningPortn,
       "pm10001otu4AlmLineLaserTempHighWarningPortn": pm10001otu4AlmLineLaserTempHighWarningPortn,
       "pm10001otu4AlmLineLaserTempHighAlarmPortn": pm10001otu4AlmLineLaserTempHighAlarmPortn,
       "pm10001otu4AlmLineTxPowerLowAlarmPortn": pm10001otu4AlmLineTxPowerLowAlarmPortn,
       "pm10001otu4AlmLineTxPowerLowWarningPortn": pm10001otu4AlmLineTxPowerLowWarningPortn,
       "pm10001otu4AlmLineTxPowerHighWarningPortn": pm10001otu4AlmLineTxPowerHighWarningPortn,
       "pm10001otu4AlmLineTxPowerHighAlarmPortn": pm10001otu4AlmLineTxPowerHighAlarmPortn,
       "pm10001otu4AlmLineBiasLowAlarmPortn": pm10001otu4AlmLineBiasLowAlarmPortn,
       "pm10001otu4AlmLineBiasLowWarningPortn": pm10001otu4AlmLineBiasLowWarningPortn,
       "pm10001otu4AlmLineBiasHighWarningPortn": pm10001otu4AlmLineBiasHighWarningPortn,
       "pm10001otu4AlmLineBiasHighAlarmPortn": pm10001otu4AlmLineBiasHighAlarmPortn,
       "pm10001otu4AlmlineNetworkLaneAlarmWarning2Table": pm10001otu4AlmlineNetworkLaneAlarmWarning2Table,
       "pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry": pm10001otu4AlmlineNetworkLaneAlarmWarning2Entry,
       "pm10001otu4AlmlineNetworkLaneAlarmWarning2Index": pm10001otu4AlmlineNetworkLaneAlarmWarning2Index,
       "pm10001otu4AlmTxModulatorBiasLowAlarmPortn": pm10001otu4AlmTxModulatorBiasLowAlarmPortn,
       "pm10001otu4AlmTxModulatorBiasLowWarningPortn": pm10001otu4AlmTxModulatorBiasLowWarningPortn,
       "pm10001otu4AlmTxModulatorBiasHighWarningPortn": pm10001otu4AlmTxModulatorBiasHighWarningPortn,
       "pm10001otu4AlmTxModulatorBiasHighAlarmPortn": pm10001otu4AlmTxModulatorBiasHighAlarmPortn,
       "pm10001otu4AlmRxLaserTempLowAlarmPortn": pm10001otu4AlmRxLaserTempLowAlarmPortn,
       "pm10001otu4AlmRxLaserTempLowWarningPortn": pm10001otu4AlmRxLaserTempLowWarningPortn,
       "pm10001otu4AlmRxLaserTempHighWarningPortn": pm10001otu4AlmRxLaserTempHighWarningPortn,
       "pm10001otu4AlmRxLaserTempHighAlarmPortn": pm10001otu4AlmRxLaserTempHighAlarmPortn,
       "pm10001otu4AlmRxLaserOutputLowAlarmPortn": pm10001otu4AlmRxLaserOutputLowAlarmPortn,
       "pm10001otu4AlmRxLaserOutputLowWarningPortn": pm10001otu4AlmRxLaserOutputLowWarningPortn,
       "pm10001otu4AlmRxLaserOutputHighWarningPortn": pm10001otu4AlmRxLaserOutputHighWarningPortn,
       "pm10001otu4AlmRxLaserOutputHighAlarmPortn": pm10001otu4AlmRxLaserOutputHighAlarmPortn,
       "pm10001otu4AlmRxLaserBiasLowAlarmPortn": pm10001otu4AlmRxLaserBiasLowAlarmPortn,
       "pm10001otu4AlmRxLaserBiasLowWarningPortn": pm10001otu4AlmRxLaserBiasLowWarningPortn,
       "pm10001otu4AlmRxLaserBiasHighWarningPortn": pm10001otu4AlmRxLaserBiasHighWarningPortn,
       "pm10001otu4AlmRxLaserBiasHighAlarmPortn": pm10001otu4AlmRxLaserBiasHighAlarmPortn,
       "pm10001otu4AlmLineUrg": pm10001otu4AlmLineUrg,
       "pm10001otu4AlmlineNetworkLaneFaultTable": pm10001otu4AlmlineNetworkLaneFaultTable,
       "pm10001otu4AlmlineNetworkLaneFaultEntry": pm10001otu4AlmlineNetworkLaneFaultEntry,
       "pm10001otu4AlmlineNetworkLaneFaultIndex": pm10001otu4AlmlineNetworkLaneFaultIndex,
       "pm10001otu4AlmLineLaneRxTecFaultPortn": pm10001otu4AlmLineLaneRxTecFaultPortn,
       "pm10001otu4AlmLineLaneRxFifoErrorPortn": pm10001otu4AlmLineLaneRxFifoErrorPortn,
       "pm10001otu4AlmLineLaneRxLolPortn": pm10001otu4AlmLineLaneRxLolPortn,
       "pm10001otu4AlmLineLaneRxLosPortn": pm10001otu4AlmLineLaneRxLosPortn,
       "pm10001otu4AlmLineLaneTxLolPortn": pm10001otu4AlmLineLaneTxLolPortn,
       "pm10001otu4AlmLineLaneTxLosfPortn": pm10001otu4AlmLineLaneTxLosfPortn,
       "pm10001otu4AlmLineLaneApdPowerSupplyPortn": pm10001otu4AlmLineLaneApdPowerSupplyPortn,
       "pm10001otu4AlmLineLaneWavelengthUnlockedPortn": pm10001otu4AlmLineLaneWavelengthUnlockedPortn,
       "pm10001otu4AlmLineLaneTecFaultPortn": pm10001otu4AlmLineLaneTecFaultPortn,
       "pm10001otu4AlmlineHostLaneFaultTable": pm10001otu4AlmlineHostLaneFaultTable,
       "pm10001otu4AlmlineHostLaneFaultEntry": pm10001otu4AlmlineHostLaneFaultEntry,
       "pm10001otu4AlmlineHostLaneFaultIndex": pm10001otu4AlmlineHostLaneFaultIndex,
       "pm10001otu4AlmLineInputLossOfSignalPortn": pm10001otu4AlmLineInputLossOfSignalPortn,
       "pm10001otu4AlmLineLossOfFramePortn": pm10001otu4AlmLineLossOfFramePortn,
       "pm10001otu4AlmLineSmBdiInsertedPortn": pm10001otu4AlmLineSmBdiInsertedPortn,
       "pm10001otu4AlmLineSmBdiDetectedPortn": pm10001otu4AlmLineSmBdiDetectedPortn,
       "pm10001otu4AlmLineSmIaeInsertedPortn": pm10001otu4AlmLineSmIaeInsertedPortn,
       "pm10001otu4AlmLineSmIaeDetectedPortn": pm10001otu4AlmLineSmIaeDetectedPortn,
       "pm10001otu4AlmLineTxHostLolPortn": pm10001otu4AlmLineTxHostLolPortn,
       "pm10001otu4AlmLineLaneTxFifoErrorPortn": pm10001otu4AlmLineLaneTxFifoErrorPortn,
       "pm10001otu4AlmLinePowerDegradePortn": pm10001otu4AlmLinePowerDegradePortn,
       "pm10001otu4AlmLineTrxOverTempPortn": pm10001otu4AlmLineTrxOverTempPortn,
       "pm10001otu4AlmlineNetworkLaneRxOtnTable": pm10001otu4AlmlineNetworkLaneRxOtnTable,
       "pm10001otu4AlmlineNetworkLaneRxOtnEntry": pm10001otu4AlmlineNetworkLaneRxOtnEntry,
       "pm10001otu4AlmlineNetworkLaneRxOtnIndex": pm10001otu4AlmlineNetworkLaneRxOtnIndex,
       "pm10001otu4AlmLineRxOtnOduAisPortn": pm10001otu4AlmLineRxOtnOduAisPortn,
       "pm10001otu4AlmLineRxOtnOtuAisPortn": pm10001otu4AlmLineRxOtnOtuAisPortn,
       "pm10001otu4AlmLineRxSmBdiPortn": pm10001otu4AlmLineRxSmBdiPortn,
       "pm10001otu4AlmLineRxOtnIaePortn": pm10001otu4AlmLineRxOtnIaePortn,
       "pm10001otu4AlmLineRxOtnOomPortn": pm10001otu4AlmLineRxOtnOomPortn,
       "pm10001otu4AlmLineRxOtnLomPortn": pm10001otu4AlmLineRxOtnLomPortn,
       "pm10001otu4AlmLineRxOtnOofPortn": pm10001otu4AlmLineRxOtnOofPortn,
       "pm10001otu4AlmLineRxOtnLofPortn": pm10001otu4AlmLineRxOtnLofPortn,
       "pm10001otu4AlmlineHostLaneTxOtnTable": pm10001otu4AlmlineHostLaneTxOtnTable,
       "pm10001otu4AlmlineHostLaneTxOtnEntry": pm10001otu4AlmlineHostLaneTxOtnEntry,
       "pm10001otu4AlmlineHostLaneTxOtnIndex": pm10001otu4AlmlineHostLaneTxOtnIndex,
       "pm10001otu4AlmLineTxOtnOduAisPortn": pm10001otu4AlmLineTxOtnOduAisPortn,
       "pm10001otu4AlmLineTxOtnOtuAisPortn": pm10001otu4AlmLineTxOtnOtuAisPortn,
       "pm10001otu4AlmLineTxSmBdiPortn": pm10001otu4AlmLineTxSmBdiPortn,
       "pm10001otu4AlmLineTxOtnIaePortn": pm10001otu4AlmLineTxOtnIaePortn,
       "pm10001otu4AlmLineTxOtnOomPortn": pm10001otu4AlmLineTxOtnOomPortn,
       "pm10001otu4AlmLineTxOtnLomPortn": pm10001otu4AlmLineTxOtnLomPortn,
       "pm10001otu4AlmLineTxOtnOofPortn": pm10001otu4AlmLineTxOtnOofPortn,
       "pm10001otu4AlmLineTxOtnLofPortn": pm10001otu4AlmLineTxOtnLofPortn,
       "pm10001otu4AlmLineCrit": pm10001otu4AlmLineCrit,
       "pm10001otu4AlmsynthAlmLineTable": pm10001otu4AlmsynthAlmLineTable,
       "pm10001otu4AlmsynthAlmLineEntry": pm10001otu4AlmsynthAlmLineEntry,
       "pm10001otu4AlmsynthAlmLineIndex": pm10001otu4AlmsynthAlmLineIndex,
       "pm10001otu4AlmXfpAbsentPortn": pm10001otu4AlmXfpAbsentPortn,
       "pm10001otu4AlmXfpInitNotComplPortn": pm10001otu4AlmXfpInitNotComplPortn,
       "pm10001otu4AlmLineHwFailPortn": pm10001otu4AlmLineHwFailPortn,
       "pm10001otu4AlmXfpTxOffPortn": pm10001otu4AlmXfpTxOffPortn,
       "pm10001otu4AlmLineLocalOosPortn": pm10001otu4AlmLineLocalOosPortn,
       "pm10001otu4AlmUpRdiInsPortn": pm10001otu4AlmUpRdiInsPortn,
       "pm10001otu4AlmLineDdmWarningPortn": pm10001otu4AlmLineDdmWarningPortn,
       "pm10001otu4AlmLineDdmAlmPortn": pm10001otu4AlmLineDdmAlmPortn,
       "pm10001otu4AlmLineFailPortn": pm10001otu4AlmLineFailPortn,
       "pm10001otu4AlmLineActivePortn": pm10001otu4AlmLineActivePortn,
       "pm10001otu4measures": pm10001otu4measures,
       "pm10001otu4MesrOther": pm10001otu4MesrOther,
       "pm10001otu4Mesrsynth0": pm10001otu4Mesrsynth0,
       "pm10001otu4Mesrsynth1": pm10001otu4Mesrsynth1,
       "pm10001otu4MesrpmIntervalNumber": pm10001otu4MesrpmIntervalNumber,
       "pm10001otu4MesrlineNetTxLaserOutputPwrAverage": pm10001otu4MesrlineNetTxLaserOutputPwrAverage,
       "pm10001otu4MesrlineNetTxLaserTempAverage": pm10001otu4MesrlineNetTxLaserTempAverage,
       "pm10001otu4MesrlineNetTxBiasCurrentAverage": pm10001otu4MesrlineNetTxBiasCurrentAverage,
       "pm10001otu4MesrlineNetRxInputPwrAverage": pm10001otu4MesrlineNetRxInputPwrAverage,
       "pm10001otu4MesrlineResidualChromaticDispAverage": pm10001otu4MesrlineResidualChromaticDispAverage,
       "pm10001otu4MesrlineDiffGroupDelayAverage": pm10001otu4MesrlineDiffGroupDelayAverage,
       "pm10001otu4MesrlineQFactorAverage": pm10001otu4MesrlineQFactorAverage,
       "pm10001otu4MesrlineCarrierFreqOffsetAverage": pm10001otu4MesrlineCarrierFreqOffsetAverage,
       "pm10001otu4MesrlineOsnrAverage": pm10001otu4MesrlineOsnrAverage,
       "pm10001otu4MesrclientNetTxTempMin": pm10001otu4MesrclientNetTxTempMin,
       "pm10001otu4MesrclientNetTxBiasMin": pm10001otu4MesrclientNetTxBiasMin,
       "pm10001otu4MesrclientNetTxPwrMin": pm10001otu4MesrclientNetTxPwrMin,
       "pm10001otu4MesrclientNetRxPwrMin": pm10001otu4MesrclientNetRxPwrMin,
       "pm10001otu4MesrlineNetTxLaserOutputPwrMin": pm10001otu4MesrlineNetTxLaserOutputPwrMin,
       "pm10001otu4MesrlineNetTxLaserTempMin": pm10001otu4MesrlineNetTxLaserTempMin,
       "pm10001otu4MesrlineNetTxBiasCurrentMin": pm10001otu4MesrlineNetTxBiasCurrentMin,
       "pm10001otu4MesrlineNetRxInputPwrMin": pm10001otu4MesrlineNetRxInputPwrMin,
       "pm10001otu4MesrlineResidualChromaticDispMin": pm10001otu4MesrlineResidualChromaticDispMin,
       "pm10001otu4MesrlineDiffGroupDelayMin": pm10001otu4MesrlineDiffGroupDelayMin,
       "pm10001otu4MesrlineQFactorMin": pm10001otu4MesrlineQFactorMin,
       "pm10001otu4MesrlineCarrierFreqOffsetMin": pm10001otu4MesrlineCarrierFreqOffsetMin,
       "pm10001otu4MesrlineOsnrMin": pm10001otu4MesrlineOsnrMin,
       "pm10001otu4MesrclientNetTxTempMax": pm10001otu4MesrclientNetTxTempMax,
       "pm10001otu4MesrclientNetTxBiasMax": pm10001otu4MesrclientNetTxBiasMax,
       "pm10001otu4MesrclientNetTxPwrMax": pm10001otu4MesrclientNetTxPwrMax,
       "pm10001otu4MesrclientNetRxPwrMax": pm10001otu4MesrclientNetRxPwrMax,
       "pm10001otu4MesrlineNetTxLaserOutputPwrMax": pm10001otu4MesrlineNetTxLaserOutputPwrMax,
       "pm10001otu4MesrlineNetTxLaserTempMax": pm10001otu4MesrlineNetTxLaserTempMax,
       "pm10001otu4MesrlineNetTxBiasCurrentMax": pm10001otu4MesrlineNetTxBiasCurrentMax,
       "pm10001otu4MesrlineNetRxInputPwrMax": pm10001otu4MesrlineNetRxInputPwrMax,
       "pm10001otu4MesrlineResidualChromaticDispMax": pm10001otu4MesrlineResidualChromaticDispMax,
       "pm10001otu4MesrlineDiffGroupDelayMax": pm10001otu4MesrlineDiffGroupDelayMax,
       "pm10001otu4MesrlineQFactorMax": pm10001otu4MesrlineQFactorMax,
       "pm10001otu4MesrlineCarrierFreqOffsetMax": pm10001otu4MesrlineCarrierFreqOffsetMax,
       "pm10001otu4MesrlineOsnrMax": pm10001otu4MesrlineOsnrMax,
       "pm10001otu4MesrClient": pm10001otu4MesrClient,
       "pm10001otu4MesrclientCfpTemp": pm10001otu4MesrclientCfpTemp,
       "pm10001otu4MesrclientCfp3v3Voltage": pm10001otu4MesrclientCfp3v3Voltage,
       "pm10001otu4MesrclientSoaBiasCurrent": pm10001otu4MesrclientSoaBiasCurrent,
       "pm10001otu4MesrclientNetTxTempTable": pm10001otu4MesrclientNetTxTempTable,
       "pm10001otu4MesrclientNetTxTempEntry": pm10001otu4MesrclientNetTxTempEntry,
       "pm10001otu4MesrclientNetTxTempIndex": pm10001otu4MesrclientNetTxTempIndex,
       "pm10001otu4MesrclientNetTxTempPortn": pm10001otu4MesrclientNetTxTempPortn,
       "pm10001otu4MesrclientNetTxBiasTable": pm10001otu4MesrclientNetTxBiasTable,
       "pm10001otu4MesrclientNetTxBiasEntry": pm10001otu4MesrclientNetTxBiasEntry,
       "pm10001otu4MesrclientNetTxBiasIndex": pm10001otu4MesrclientNetTxBiasIndex,
       "pm10001otu4MesrclientNetTxBiasPortn": pm10001otu4MesrclientNetTxBiasPortn,
       "pm10001otu4MesrclientNetTxPwrTable": pm10001otu4MesrclientNetTxPwrTable,
       "pm10001otu4MesrclientNetTxPwrEntry": pm10001otu4MesrclientNetTxPwrEntry,
       "pm10001otu4MesrclientNetTxPwrIndex": pm10001otu4MesrclientNetTxPwrIndex,
       "pm10001otu4MesrclientNetTxPwrPortn": pm10001otu4MesrclientNetTxPwrPortn,
       "pm10001otu4MesrclientNetRxPwrTable": pm10001otu4MesrclientNetRxPwrTable,
       "pm10001otu4MesrclientNetRxPwrEntry": pm10001otu4MesrclientNetRxPwrEntry,
       "pm10001otu4MesrclientNetRxPwrIndex": pm10001otu4MesrclientNetRxPwrIndex,
       "pm10001otu4MesrclientNetRxPwrPortn": pm10001otu4MesrclientNetRxPwrPortn,
       "pm10001otu4MesrLine": pm10001otu4MesrLine,
       "pm10001otu4MesrlineMsaTemp": pm10001otu4MesrlineMsaTemp,
       "pm10001otu4MesrlineMsa3v3Voltage": pm10001otu4MesrlineMsa3v3Voltage,
       "pm10001otu4MesrlineSoaBiasCurrent": pm10001otu4MesrlineSoaBiasCurrent,
       "pm10001otu4MesrlineNetTxLaserOutputPwrTable": pm10001otu4MesrlineNetTxLaserOutputPwrTable,
       "pm10001otu4MesrlineNetTxLaserOutputPwrEntry": pm10001otu4MesrlineNetTxLaserOutputPwrEntry,
       "pm10001otu4MesrlineNetTxLaserOutputPwrIndex": pm10001otu4MesrlineNetTxLaserOutputPwrIndex,
       "pm10001otu4MesrlineNetTxLaserOutputPwrPortn": pm10001otu4MesrlineNetTxLaserOutputPwrPortn,
       "pm10001otu4MesrlineNetTxLaserTempTable": pm10001otu4MesrlineNetTxLaserTempTable,
       "pm10001otu4MesrlineNetTxLaserTempEntry": pm10001otu4MesrlineNetTxLaserTempEntry,
       "pm10001otu4MesrlineNetTxLaserTempIndex": pm10001otu4MesrlineNetTxLaserTempIndex,
       "pm10001otu4MesrlineNetTxLaserTempPortn": pm10001otu4MesrlineNetTxLaserTempPortn,
       "pm10001otu4MesrlineNetTxBiasCurrentTable": pm10001otu4MesrlineNetTxBiasCurrentTable,
       "pm10001otu4MesrlineNetTxBiasCurrentEntry": pm10001otu4MesrlineNetTxBiasCurrentEntry,
       "pm10001otu4MesrlineNetTxBiasCurrentIndex": pm10001otu4MesrlineNetTxBiasCurrentIndex,
       "pm10001otu4MesrlineNetTxBiasCurrentPortn": pm10001otu4MesrlineNetTxBiasCurrentPortn,
       "pm10001otu4MesrlineNetRxInputPwrTable": pm10001otu4MesrlineNetRxInputPwrTable,
       "pm10001otu4MesrlineNetRxInputPwrEntry": pm10001otu4MesrlineNetRxInputPwrEntry,
       "pm10001otu4MesrlineNetRxInputPwrIndex": pm10001otu4MesrlineNetRxInputPwrIndex,
       "pm10001otu4MesrlineNetRxInputPwrPortn": pm10001otu4MesrlineNetRxInputPwrPortn,
       "pm10001otu4MesrlineResidualChromaticDispTable": pm10001otu4MesrlineResidualChromaticDispTable,
       "pm10001otu4MesrlineResidualChromaticDispEntry": pm10001otu4MesrlineResidualChromaticDispEntry,
       "pm10001otu4MesrlineResidualChromaticDispIndex": pm10001otu4MesrlineResidualChromaticDispIndex,
       "pm10001otu4MesrlineResidualChromaticDispPortn": pm10001otu4MesrlineResidualChromaticDispPortn,
       "pm10001otu4MesrlineDiffGroupDelayTable": pm10001otu4MesrlineDiffGroupDelayTable,
       "pm10001otu4MesrlineDiffGroupDelayEntry": pm10001otu4MesrlineDiffGroupDelayEntry,
       "pm10001otu4MesrlineDiffGroupDelayIndex": pm10001otu4MesrlineDiffGroupDelayIndex,
       "pm10001otu4MesrlineDiffGroupDelayPortn": pm10001otu4MesrlineDiffGroupDelayPortn,
       "pm10001otu4MesrlineQFactorTable": pm10001otu4MesrlineQFactorTable,
       "pm10001otu4MesrlineQFactorEntry": pm10001otu4MesrlineQFactorEntry,
       "pm10001otu4MesrlineQFactorIndex": pm10001otu4MesrlineQFactorIndex,
       "pm10001otu4MesrlineQFactorPortn": pm10001otu4MesrlineQFactorPortn,
       "pm10001otu4MesrlineCarrierFreqOffsetTable": pm10001otu4MesrlineCarrierFreqOffsetTable,
       "pm10001otu4MesrlineCarrierFreqOffsetEntry": pm10001otu4MesrlineCarrierFreqOffsetEntry,
       "pm10001otu4MesrlineCarrierFreqOffsetIndex": pm10001otu4MesrlineCarrierFreqOffsetIndex,
       "pm10001otu4MesrlineCarrierFreqOffsetPortn": pm10001otu4MesrlineCarrierFreqOffsetPortn,
       "pm10001otu4MesrlineOsnrTable": pm10001otu4MesrlineOsnrTable,
       "pm10001otu4MesrlineOsnrEntry": pm10001otu4MesrlineOsnrEntry,
       "pm10001otu4MesrlineOsnrIndex": pm10001otu4MesrlineOsnrIndex,
       "pm10001otu4MesrlineOsnrPortn": pm10001otu4MesrlineOsnrPortn,
       "pm10001otu4counters": pm10001otu4counters,
       "pm10001otu4CntOther": pm10001otu4CntOther,
       "pm10001otu4CntClient": pm10001otu4CntClient,
       "pm10001otu4CntclientInputErrorCounterLaneOneTable": pm10001otu4CntclientInputErrorCounterLaneOneTable,
       "pm10001otu4CntclientInputErrorCounterLaneOneEntry": pm10001otu4CntclientInputErrorCounterLaneOneEntry,
       "pm10001otu4CntclientInputErrorCounterLaneOneIndex": pm10001otu4CntclientInputErrorCounterLaneOneIndex,
       "pm10001otu4CntclientInputErrorCounterLaneOneValuePortn": pm10001otu4CntclientInputErrorCounterLaneOneValuePortn,
       "pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn": pm10001otu4CntclientInputErrorCounterLaneOneErrorPortn,
       "pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn": pm10001otu4CntclientInputErrorCounterLaneOneOverloadPortn,
       "pm10001otu4CntclientInputErrorCounterLaneTwoTable": pm10001otu4CntclientInputErrorCounterLaneTwoTable,
       "pm10001otu4CntclientInputErrorCounterLaneTwoEntry": pm10001otu4CntclientInputErrorCounterLaneTwoEntry,
       "pm10001otu4CntclientInputErrorCounterLaneTwoIndex": pm10001otu4CntclientInputErrorCounterLaneTwoIndex,
       "pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn": pm10001otu4CntclientInputErrorCounterLaneTwoValuePortn,
       "pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn": pm10001otu4CntclientInputErrorCounterLaneTwoErrorPortn,
       "pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn": pm10001otu4CntclientInputErrorCounterLaneTwoOverloadPortn,
       "pm10001otu4CntclientInputErrorCounterTable": pm10001otu4CntclientInputErrorCounterTable,
       "pm10001otu4CntclientInputErrorCounterEntry": pm10001otu4CntclientInputErrorCounterEntry,
       "pm10001otu4CntclientInputErrorCounterIndex": pm10001otu4CntclientInputErrorCounterIndex,
       "pm10001otu4CntclientInputErrorCounterValuePortn": pm10001otu4CntclientInputErrorCounterValuePortn,
       "pm10001otu4CntclientInputErrorCounterErrorPortn": pm10001otu4CntclientInputErrorCounterErrorPortn,
       "pm10001otu4CntclientInputErrorCounterOverloadPortn": pm10001otu4CntclientInputErrorCounterOverloadPortn,
       "pm10001otu4CntclientCbipCounterTable": pm10001otu4CntclientCbipCounterTable,
       "pm10001otu4CntclientCbipCounterEntry": pm10001otu4CntclientCbipCounterEntry,
       "pm10001otu4CntclientCbipCounterIndex": pm10001otu4CntclientCbipCounterIndex,
       "pm10001otu4CntclientCbipCounterValuePortn": pm10001otu4CntclientCbipCounterValuePortn,
       "pm10001otu4CntclientCbipCounterErrorPortn": pm10001otu4CntclientCbipCounterErrorPortn,
       "pm10001otu4CntclientCbipCounterOverloadPortn": pm10001otu4CntclientCbipCounterOverloadPortn,
       "pm10001otu4CntLine": pm10001otu4CntLine,
       "pm10001otu4CntlocalLineSmBip8ErrorCounterTable": pm10001otu4CntlocalLineSmBip8ErrorCounterTable,
       "pm10001otu4CntlocalLineSmBip8ErrorCounterEntry": pm10001otu4CntlocalLineSmBip8ErrorCounterEntry,
       "pm10001otu4CntlocalLineSmBip8ErrorCounterIndex": pm10001otu4CntlocalLineSmBip8ErrorCounterIndex,
       "pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn": pm10001otu4CntlocalLineSmBip8ErrorCounterValuePortn,
       "pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn": pm10001otu4CntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn": pm10001otu4CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm10001otu4CntlocalLineFecCorrectedErrorsCounterTable": pm10001otu4CntlocalLineFecCorrectedErrorsCounterTable,
       "pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry": pm10001otu4CntlocalLineFecCorrectedErrorsCounterEntry,
       "pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex": pm10001otu4CntlocalLineFecCorrectedErrorsCounterIndex,
       "pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn": pm10001otu4CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn": pm10001otu4CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm10001otu4CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm10001otu4CntremoteLineSmBip8ErrorCounterTable": pm10001otu4CntremoteLineSmBip8ErrorCounterTable,
       "pm10001otu4CntremoteLineSmBip8ErrorCounterEntry": pm10001otu4CntremoteLineSmBip8ErrorCounterEntry,
       "pm10001otu4CntremoteLineSmBip8ErrorCounterIndex": pm10001otu4CntremoteLineSmBip8ErrorCounterIndex,
       "pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn": pm10001otu4CntremoteLineSmBip8ErrorCounterValuePortn,
       "pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn": pm10001otu4CntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn": pm10001otu4CntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm10001otu4CntlineDfrmTimCntTable": pm10001otu4CntlineDfrmTimCntTable,
       "pm10001otu4CntlineDfrmTimCntEntry": pm10001otu4CntlineDfrmTimCntEntry,
       "pm10001otu4CntlineDfrmTimCntIndex": pm10001otu4CntlineDfrmTimCntIndex,
       "pm10001otu4CntlineDfrmTimCntValuePortn": pm10001otu4CntlineDfrmTimCntValuePortn,
       "pm10001otu4CntlineDfrmTimCntErrorPortn": pm10001otu4CntlineDfrmTimCntErrorPortn,
       "pm10001otu4CntlineDfrmTimCntOverloadPortn": pm10001otu4CntlineDfrmTimCntOverloadPortn,
       "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterTable": pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterTable,
       "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry": pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex": pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn": pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": pm10001otu4CntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterTable": pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry": pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex": pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": pm10001otu4CntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "pm10001otu4controlsWrite": pm10001otu4controlsWrite,
       "pm10001otu4CtrlOther": pm10001otu4CtrlOther,
       "pm10001otu4CtrlconfMgnt1": pm10001otu4CtrlconfMgnt1,
       "pm10001otu4CtrlConf1Load1": pm10001otu4CtrlConf1Load1,
       "pm10001otu4CtrlConf2Load1": pm10001otu4CtrlConf2Load1,
       "pm10001otu4CtrlConf2Flash1": pm10001otu4CtrlConf2Flash1,
       "pm10001otu4CtrlConf2Clear1": pm10001otu4CtrlConf2Clear1,
       "pm10001otu4Ctrlsynth4": pm10001otu4Ctrlsynth4,
       "pm10001otu4CtrlCorrelatOn": pm10001otu4CtrlCorrelatOn,
       "pm10001otu4CtrlCorrelatOff": pm10001otu4CtrlCorrelatOff,
       "pm10001otu4CtrlswMgnt": pm10001otu4CtrlswMgnt,
       "pm10001otu4CtrlColdReset": pm10001otu4CtrlColdReset,
       "pm10001otu4CtrlWarmReset": pm10001otu4CtrlWarmReset,
       "pm10001otu4CtrlLoadSwBank1": pm10001otu4CtrlLoadSwBank1,
       "pm10001otu4CtrlLoadSwBank2": pm10001otu4CtrlLoadSwBank2,
       "pm10001otu4CtrlgwMgnt": pm10001otu4CtrlgwMgnt,
       "pm10001otu4CtrlCurrentGwReset": pm10001otu4CtrlCurrentGwReset,
       "pm10001otu4CtrlLoadGwBank1": pm10001otu4CtrlLoadGwBank1,
       "pm10001otu4CtrlLoadGwBank2": pm10001otu4CtrlLoadGwBank2,
       "pm10001otu4CtrlLoadGwBank3": pm10001otu4CtrlLoadGwBank3,
       "pm10001otu4CtrlLoadGwBank4": pm10001otu4CtrlLoadGwBank4,
       "pm10001otu4CtrlledTest": pm10001otu4CtrlledTest,
       "pm10001otu4CtrlGreenLed": pm10001otu4CtrlGreenLed,
       "pm10001otu4CtrlRedLed": pm10001otu4CtrlRedLed,
       "pm10001otu4CtrlLedOff": pm10001otu4CtrlLedOff,
       "pm10001otu4CtrlinitSwitchMarvell": pm10001otu4CtrlinitSwitchMarvell,
       "pm10001otu4CtrlInitSwitchMarvell": pm10001otu4CtrlInitSwitchMarvell,
       "pm10001otu4CtrlresetCount": pm10001otu4CtrlresetCount,
       "pm10001otu4CtrlResetcount": pm10001otu4CtrlResetcount,
       "pm10001otu4CtrlresetRmon": pm10001otu4CtrlresetRmon,
       "pm10001otu4CtrlResetrmon": pm10001otu4CtrlResetrmon,
       "pm10001otu4CtrlresetMeasurements": pm10001otu4CtrlresetMeasurements,
       "pm10001otu4CtrlResetmeasurements": pm10001otu4CtrlResetmeasurements,
       "pm10001otu4CtrlClient": pm10001otu4CtrlClient,
       "pm10001otu4CtrlaccessLoopTable": pm10001otu4CtrlaccessLoopTable,
       "pm10001otu4CtrlaccessLoopEntry": pm10001otu4CtrlaccessLoopEntry,
       "pm10001otu4CtrlaccessLoopIndex": pm10001otu4CtrlaccessLoopIndex,
       "pm10001otu4CtrlaccessLoopPortn": pm10001otu4CtrlaccessLoopPortn,
       "pm10001otu4CtrlclientLoopToLineTable": pm10001otu4CtrlclientLoopToLineTable,
       "pm10001otu4CtrlclientLoopToLineEntry": pm10001otu4CtrlclientLoopToLineEntry,
       "pm10001otu4CtrlclientLoopToLineIndex": pm10001otu4CtrlclientLoopToLineIndex,
       "pm10001otu4CtrlclientLoopToLinePortn": pm10001otu4CtrlclientLoopToLinePortn,
       "pm10001otu4CtrlcsfUpInsTable": pm10001otu4CtrlcsfUpInsTable,
       "pm10001otu4CtrlcsfUpInsEntry": pm10001otu4CtrlcsfUpInsEntry,
       "pm10001otu4CtrlcsfUpInsIndex": pm10001otu4CtrlcsfUpInsIndex,
       "pm10001otu4CtrlcsfUpInsPortn": pm10001otu4CtrlcsfUpInsPortn,
       "pm10001otu4CtrlcaisDwInsTable": pm10001otu4CtrlcaisDwInsTable,
       "pm10001otu4CtrlcaisDwInsEntry": pm10001otu4CtrlcaisDwInsEntry,
       "pm10001otu4CtrlcaisDwInsIndex": pm10001otu4CtrlcaisDwInsIndex,
       "pm10001otu4CtrlcaisDwInsPortn": pm10001otu4CtrlcaisDwInsPortn,
       "pm10001otu4CtrlclientResetAllCountTable": pm10001otu4CtrlclientResetAllCountTable,
       "pm10001otu4CtrlclientResetAllCountEntry": pm10001otu4CtrlclientResetAllCountEntry,
       "pm10001otu4CtrlclientResetAllCountIndex": pm10001otu4CtrlclientResetAllCountIndex,
       "pm10001otu4CtrlclientResetAllCountsPortn": pm10001otu4CtrlclientResetAllCountsPortn,
       "pm10001otu4CtrlLine": pm10001otu4CtrlLine,
       "pm10001otu4CtrlcommAccessLoopTable": pm10001otu4CtrlcommAccessLoopTable,
       "pm10001otu4CtrlcommAccessLoopEntry": pm10001otu4CtrlcommAccessLoopEntry,
       "pm10001otu4CtrlcommAccessLoopIndex": pm10001otu4CtrlcommAccessLoopIndex,
       "pm10001otu4CtrlcommAccessLoopPortn": pm10001otu4CtrlcommAccessLoopPortn,
       "pm10001otu4CtrllineLoopTable": pm10001otu4CtrllineLoopTable,
       "pm10001otu4CtrllineLoopEntry": pm10001otu4CtrllineLoopEntry,
       "pm10001otu4CtrllineLoopIndex": pm10001otu4CtrllineLoopIndex,
       "pm10001otu4CtrllineLoopPortn": pm10001otu4CtrllineLoopPortn,
       "pm10001otu4CtrlfecDisableTable": pm10001otu4CtrlfecDisableTable,
       "pm10001otu4CtrlfecDisableEntry": pm10001otu4CtrlfecDisableEntry,
       "pm10001otu4CtrlfecDisableIndex": pm10001otu4CtrlfecDisableIndex,
       "pm10001otu4CtrlfecDisablePortn": pm10001otu4CtrlfecDisablePortn,
       "pm10001otu4CtrlmsaLineLoopTable": pm10001otu4CtrlmsaLineLoopTable,
       "pm10001otu4CtrlmsaLineLoopEntry": pm10001otu4CtrlmsaLineLoopEntry,
       "pm10001otu4CtrlmsaLineLoopIndex": pm10001otu4CtrlmsaLineLoopIndex,
       "pm10001otu4CtrlmsaLineLoopPortn": pm10001otu4CtrlmsaLineLoopPortn,
       "pm10001otu4CtrlmsaTxResetTable": pm10001otu4CtrlmsaTxResetTable,
       "pm10001otu4CtrlmsaTxResetEntry": pm10001otu4CtrlmsaTxResetEntry,
       "pm10001otu4CtrlmsaTxResetIndex": pm10001otu4CtrlmsaTxResetIndex,
       "pm10001otu4CtrlmsaTxResetPortn": pm10001otu4CtrlmsaTxResetPortn,
       "pm10001otu4CtrlmsaRxResetTable": pm10001otu4CtrlmsaRxResetTable,
       "pm10001otu4CtrlmsaRxResetEntry": pm10001otu4CtrlmsaRxResetEntry,
       "pm10001otu4CtrlmsaRxResetIndex": pm10001otu4CtrlmsaRxResetIndex,
       "pm10001otu4CtrlmsaRxResetPortn": pm10001otu4CtrlmsaRxResetPortn,
       "pm10001otu4CtrlmsaShutdownTable": pm10001otu4CtrlmsaShutdownTable,
       "pm10001otu4CtrlmsaShutdownEntry": pm10001otu4CtrlmsaShutdownEntry,
       "pm10001otu4CtrlmsaShutdownIndex": pm10001otu4CtrlmsaShutdownIndex,
       "pm10001otu4CtrlmsaShutdownPortn": pm10001otu4CtrlmsaShutdownPortn,
       "pm10001otu4CtrllineResetAllCountTable": pm10001otu4CtrllineResetAllCountTable,
       "pm10001otu4CtrllineResetAllCountEntry": pm10001otu4CtrllineResetAllCountEntry,
       "pm10001otu4CtrllineResetAllCountIndex": pm10001otu4CtrllineResetAllCountIndex,
       "pm10001otu4CtrllineResetAllCountsPortn": pm10001otu4CtrllineResetAllCountsPortn,
       "pm10001otu4ri": pm10001otu4ri,
       "pm10001otu4riTable": pm10001otu4riTable,
       "pm10001otu4RinvSfpTable": pm10001otu4RinvSfpTable,
       "pm10001otu4RinvSfpEntry": pm10001otu4RinvSfpEntry,
       "pm10001otu4RinvSfpIndex": pm10001otu4RinvSfpIndex,
       "pm10001otu4Rinvsfp": pm10001otu4Rinvsfp,
       "pm10001otu4RinvLineTable": pm10001otu4RinvLineTable,
       "pm10001otu4RinvLineEntry": pm10001otu4RinvLineEntry,
       "pm10001otu4RinvLineIndex": pm10001otu4RinvLineIndex,
       "pm10001otu4RinvxfpLine": pm10001otu4RinvxfpLine,
       "pm10001otu4RinvReloadInventory": pm10001otu4RinvReloadInventory,
       "pm10001otu4RinvHwPlatform": pm10001otu4RinvHwPlatform,
       "pm10001otu4RinvModulePlatform": pm10001otu4RinvModulePlatform,
       "pm10001otu4RinvSwPlatform": pm10001otu4RinvSwPlatform,
       "pm10001otu4RinvGwPlatform": pm10001otu4RinvGwPlatform,
       "pm10001otu4download": pm10001otu4download,
       "pm10001otu4DwlOther": pm10001otu4DwlOther,
       "pm10001otu4DwlrestartProcess": pm10001otu4DwlrestartProcess,
       "pm10001otu4DwlWarmRestartProcessed": pm10001otu4DwlWarmRestartProcessed,
       "pm10001otu4DwlColdRestartProcessed": pm10001otu4DwlColdRestartProcessed,
       "pm10001otu4DwlswBanksUsed": pm10001otu4DwlswBanksUsed,
       "pm10001otu4DwlSwBank1Used": pm10001otu4DwlSwBank1Used,
       "pm10001otu4DwlSwBank2Used": pm10001otu4DwlSwBank2Used,
       "pm10001otu4DwlSwBank1Notempty": pm10001otu4DwlSwBank1Notempty,
       "pm10001otu4DwlSwBank2Notempty": pm10001otu4DwlSwBank2Notempty,
       "pm10001otu4DwlgwBanksUsed": pm10001otu4DwlgwBanksUsed,
       "pm10001otu4DwlGwBank1Used": pm10001otu4DwlGwBank1Used,
       "pm10001otu4DwlGwBank2Used": pm10001otu4DwlGwBank2Used,
       "pm10001otu4DwlGwBank3Used": pm10001otu4DwlGwBank3Used,
       "pm10001otu4DwlGwBank4Used": pm10001otu4DwlGwBank4Used,
       "pm10001otu4DwlGwBank1Notempty": pm10001otu4DwlGwBank1Notempty,
       "pm10001otu4DwlGwBank2Notempty": pm10001otu4DwlGwBank2Notempty,
       "pm10001otu4DwlGwBank3Notempty": pm10001otu4DwlGwBank3Notempty,
       "pm10001otu4DwlGwBank4Notempty": pm10001otu4DwlGwBank4Notempty,
       "pm10001otu4DwlClient": pm10001otu4DwlClient,
       "pm10001otu4DwlLine": pm10001otu4DwlLine,
       "pm10001otu4Config": pm10001otu4Config,
       "pm10001otu4CfgAccessCAisCsf": pm10001otu4CfgAccessCAisCsf,
       "pm10001otu4CfgClientcaiscsfTable": pm10001otu4CfgClientcaiscsfTable,
       "pm10001otu4CfgClientcaiscsfEntry": pm10001otu4CfgClientcaiscsfEntry,
       "pm10001otu4CfgClientcaiscsfIndex": pm10001otu4CfgClientcaiscsfIndex,
       "pm10001otu4CfgReservePortn": pm10001otu4CfgReservePortn,
       "pm10001otu4CfgStartup": pm10001otu4CfgStartup,
       "pm10001otu4CfgClientStartupTable": pm10001otu4CfgClientStartupTable,
       "pm10001otu4CfgClientStartupEntry": pm10001otu4CfgClientStartupEntry,
       "pm10001otu4CfgClientStartupIndex": pm10001otu4CfgClientStartupIndex,
       "pm10001otu4CfgSystConfPortPortn": pm10001otu4CfgSystConfPortPortn,
       "pm10001otu4CfgNetConfPortPortn": pm10001otu4CfgNetConfPortPortn,
       "pm10001otu4CfgIgnoreTimePortn": pm10001otu4CfgIgnoreTimePortn,
       "pm10001otu4CfgOptionsPortPortn": pm10001otu4CfgOptionsPortPortn,
       "pm10001otu4CfgLineStartupTable": pm10001otu4CfgLineStartupTable,
       "pm10001otu4CfgLineStartupEntry": pm10001otu4CfgLineStartupEntry,
       "pm10001otu4CfgLineStartupIndex": pm10001otu4CfgLineStartupIndex,
       "pm10001otu4CfgSystConfLinePortn": pm10001otu4CfgSystConfLinePortn,
       "pm10001otu4CfgOptionsLinePortn": pm10001otu4CfgOptionsLinePortn,
       "pm10001otu4CfgXfpTable": pm10001otu4CfgXfpTable,
       "pm10001otu4CfgXfpEntry": pm10001otu4CfgXfpEntry,
       "pm10001otu4CfgXfpIndex": pm10001otu4CfgXfpIndex,
       "pm10001otu4CfgSystConfMsaLinePortn": pm10001otu4CfgSystConfMsaLinePortn,
       "pm10001otu4CfgCompDispChromValuePortn": pm10001otu4CfgCompDispChromValuePortn,
       "pm10001otu4CfgLabels": pm10001otu4CfgLabels,
       "pm10001otu4CfgLabelclientTable": pm10001otu4CfgLabelclientTable,
       "pm10001otu4CfgLabelclientEntry": pm10001otu4CfgLabelclientEntry,
       "pm10001otu4CfgLabelclientIndex": pm10001otu4CfgLabelclientIndex,
       "pm10001otu4CfgLabelclientPortn": pm10001otu4CfgLabelclientPortn,
       "pm10001otu4CfgLabellineTable": pm10001otu4CfgLabellineTable,
       "pm10001otu4CfgLabellineEntry": pm10001otu4CfgLabellineEntry,
       "pm10001otu4CfgLabellineIndex": pm10001otu4CfgLabellineIndex,
       "pm10001otu4CfgLabellinePortn": pm10001otu4CfgLabellinePortn,
       "pm10001otu4CfgStartuptlh": pm10001otu4CfgStartuptlh,
       "pm10001otu4CfgOtxtlhTable": pm10001otu4CfgOtxtlhTable,
       "pm10001otu4CfgOtxtlhEntry": pm10001otu4CfgOtxtlhEntry,
       "pm10001otu4CfgOtxtlhIndex": pm10001otu4CfgOtxtlhIndex,
       "pm10001otu4CfgLinePwrLaserPortn": pm10001otu4CfgLinePwrLaserPortn,
       "pm10001otu4CfgLineFCurrentPortn": pm10001otu4CfgLineFCurrentPortn,
       "pm10001otu4CfgLineGridCurrentPortn": pm10001otu4CfgLineGridCurrentPortn,
       "pm10001otu4CfgFPortn": pm10001otu4CfgFPortn,
       "pm10001otu4CfgRxLineFCurrentPortn": pm10001otu4CfgRxLineFCurrentPortn,
       "pm10001otu4CfgOther": pm10001otu4CfgOther,
       "pm10001otu4tablemoduleOther": pm10001otu4tablemoduleOther,
       "pm10001otu4Cfgmode": pm10001otu4Cfgmode,
       "pm10001otu4CfgnonLinearEffectsThresholds": pm10001otu4CfgnonLinearEffectsThresholds,
       "pm10001otu4CfgfanHighSpeedThreshold": pm10001otu4CfgfanHighSpeedThreshold,
       "pm10001otu4CfgStartuptablefive": pm10001otu4CfgStartuptablefive,
       "pm10001otu4CfgOtxtlhcapabilitiesTable": pm10001otu4CfgOtxtlhcapabilitiesTable,
       "pm10001otu4CfgOtxtlhcapabilitiesEntry": pm10001otu4CfgOtxtlhcapabilitiesEntry,
       "pm10001otu4CfgOtxtlhcapabilitiesIndex": pm10001otu4CfgOtxtlhcapabilitiesIndex,
       "pm10001otu4CfgComponentTypePortn": pm10001otu4CfgComponentTypePortn,
       "pm10001otu4CfgMiscellaneousPortn": pm10001otu4CfgMiscellaneousPortn,
       "pm10001otu4CfgFirstChannelPortn": pm10001otu4CfgFirstChannelPortn,
       "pm10001otu4CfgLastChannelPortn": pm10001otu4CfgLastChannelPortn,
       "pm10001otu4CfgGridPortn": pm10001otu4CfgGridPortn,
       "pm10001otu4CfgStartuptableslot": pm10001otu4CfgStartuptableslot,
       "pm10001otu4CfgLinePtmsiAccOtnTable": pm10001otu4CfgLinePtmsiAccOtnTable,
       "pm10001otu4CfgLinePtmsiAccOtnEntry": pm10001otu4CfgLinePtmsiAccOtnEntry,
       "pm10001otu4CfgLinePtmsiAccOtnIndex": pm10001otu4CfgLinePtmsiAccOtnIndex,
       "pm10001otu4CfgPayloadtypePortn": pm10001otu4CfgPayloadtypePortn,
       "pm10001otu4CfgPtmsireservedPortn": pm10001otu4CfgPtmsireservedPortn,
       "pm10001otu4CfgTimeslot1valPortn": pm10001otu4CfgTimeslot1valPortn,
       "pm10001otu4CfgTimeslot2valPortn": pm10001otu4CfgTimeslot2valPortn,
       "pm10001otu4CfgTimeslot3valPortn": pm10001otu4CfgTimeslot3valPortn,
       "pm10001otu4CfgTimeslot4valPortn": pm10001otu4CfgTimeslot4valPortn,
       "pm10001otu4CfgTimeslot5valPortn": pm10001otu4CfgTimeslot5valPortn,
       "pm10001otu4CfgTimeslot6valPortn": pm10001otu4CfgTimeslot6valPortn,
       "pm10001otu4CfgTimeslot7valPortn": pm10001otu4CfgTimeslot7valPortn,
       "pm10001otu4CfgTimeslot8valPortn": pm10001otu4CfgTimeslot8valPortn,
       "pm10001otu4CfgTimeslot9valPortn": pm10001otu4CfgTimeslot9valPortn,
       "pm10001otu4CfgTimeslot10valPortn": pm10001otu4CfgTimeslot10valPortn,
       "pm10001otu4CfgTimeslot11valPortn": pm10001otu4CfgTimeslot11valPortn,
       "pm10001otu4CfgTimeslot12valPortn": pm10001otu4CfgTimeslot12valPortn,
       "pm10001otu4CfgTimeslot13valPortn": pm10001otu4CfgTimeslot13valPortn,
       "pm10001otu4CfgTimeslot14valPortn": pm10001otu4CfgTimeslot14valPortn,
       "pm10001otu4CfgTimeslot15valPortn": pm10001otu4CfgTimeslot15valPortn,
       "pm10001otu4CfgTimeslot16valPortn": pm10001otu4CfgTimeslot16valPortn,
       "pm10001otu4CfgTimeslot17valPortn": pm10001otu4CfgTimeslot17valPortn,
       "pm10001otu4CfgTimeslot18valPortn": pm10001otu4CfgTimeslot18valPortn,
       "pm10001otu4CfgTimeslot19valPortn": pm10001otu4CfgTimeslot19valPortn,
       "pm10001otu4CfgTimeslot20valPortn": pm10001otu4CfgTimeslot20valPortn,
       "pm10001otu4CfgTimeslot21valPortn": pm10001otu4CfgTimeslot21valPortn,
       "pm10001otu4CfgTimeslot22valPortn": pm10001otu4CfgTimeslot22valPortn,
       "pm10001otu4CfgTimeslot23valPortn": pm10001otu4CfgTimeslot23valPortn,
       "pm10001otu4CfgTimeslot24valPortn": pm10001otu4CfgTimeslot24valPortn,
       "pm10001otu4CfgTimeslot25valPortn": pm10001otu4CfgTimeslot25valPortn,
       "pm10001otu4CfgTimeslot26valPortn": pm10001otu4CfgTimeslot26valPortn,
       "pm10001otu4CfgTimeslot27valPortn": pm10001otu4CfgTimeslot27valPortn,
       "pm10001otu4CfgTimeslot28valPortn": pm10001otu4CfgTimeslot28valPortn,
       "pm10001otu4CfgTimeslot29valPortn": pm10001otu4CfgTimeslot29valPortn,
       "pm10001otu4CfgTimeslot30valPortn": pm10001otu4CfgTimeslot30valPortn,
       "pm10001otu4CfgTimeslot31valPortn": pm10001otu4CfgTimeslot31valPortn,
       "pm10001otu4CfgTimeslot32valPortn": pm10001otu4CfgTimeslot32valPortn,
       "pm10001otu4CfgTimeslot33valPortn": pm10001otu4CfgTimeslot33valPortn,
       "pm10001otu4CfgTimeslot34valPortn": pm10001otu4CfgTimeslot34valPortn,
       "pm10001otu4CfgTimeslot35valPortn": pm10001otu4CfgTimeslot35valPortn,
       "pm10001otu4CfgTimeslot36valPortn": pm10001otu4CfgTimeslot36valPortn,
       "pm10001otu4CfgTimeslot37valPortn": pm10001otu4CfgTimeslot37valPortn,
       "pm10001otu4CfgTimeslot38valPortn": pm10001otu4CfgTimeslot38valPortn,
       "pm10001otu4CfgTimeslot39valPortn": pm10001otu4CfgTimeslot39valPortn,
       "pm10001otu4CfgTimeslot40valPortn": pm10001otu4CfgTimeslot40valPortn,
       "pm10001otu4CfgTimeslot41valPortn": pm10001otu4CfgTimeslot41valPortn,
       "pm10001otu4CfgTimeslot42valPortn": pm10001otu4CfgTimeslot42valPortn,
       "pm10001otu4CfgTimeslot43valPortn": pm10001otu4CfgTimeslot43valPortn,
       "pm10001otu4CfgTimeslot44valPortn": pm10001otu4CfgTimeslot44valPortn,
       "pm10001otu4CfgTimeslot45valPortn": pm10001otu4CfgTimeslot45valPortn,
       "pm10001otu4CfgTimeslot46valPortn": pm10001otu4CfgTimeslot46valPortn,
       "pm10001otu4CfgTimeslot47valPortn": pm10001otu4CfgTimeslot47valPortn,
       "pm10001otu4CfgTimeslot48valPortn": pm10001otu4CfgTimeslot48valPortn,
       "pm10001otu4CfgTimeslot49valPortn": pm10001otu4CfgTimeslot49valPortn,
       "pm10001otu4CfgTimeslot50valPortn": pm10001otu4CfgTimeslot50valPortn,
       "pm10001otu4CfgTimeslot51valPortn": pm10001otu4CfgTimeslot51valPortn,
       "pm10001otu4CfgTimeslot52valPortn": pm10001otu4CfgTimeslot52valPortn,
       "pm10001otu4CfgTimeslot53valPortn": pm10001otu4CfgTimeslot53valPortn,
       "pm10001otu4CfgTimeslot54valPortn": pm10001otu4CfgTimeslot54valPortn,
       "pm10001otu4CfgTimeslot55valPortn": pm10001otu4CfgTimeslot55valPortn,
       "pm10001otu4CfgTimeslot56valPortn": pm10001otu4CfgTimeslot56valPortn,
       "pm10001otu4CfgTimeslot57valPortn": pm10001otu4CfgTimeslot57valPortn,
       "pm10001otu4CfgTimeslot58valPortn": pm10001otu4CfgTimeslot58valPortn,
       "pm10001otu4CfgTimeslot59valPortn": pm10001otu4CfgTimeslot59valPortn,
       "pm10001otu4CfgTimeslot60valPortn": pm10001otu4CfgTimeslot60valPortn,
       "pm10001otu4CfgTimeslot61valPortn": pm10001otu4CfgTimeslot61valPortn,
       "pm10001otu4CfgTimeslot62valPortn": pm10001otu4CfgTimeslot62valPortn,
       "pm10001otu4CfgTimeslot63valPortn": pm10001otu4CfgTimeslot63valPortn,
       "pm10001otu4CfgTimeslot64valPortn": pm10001otu4CfgTimeslot64valPortn,
       "pm10001otu4CfgTimeslot65valPortn": pm10001otu4CfgTimeslot65valPortn,
       "pm10001otu4CfgTimeslot66valPortn": pm10001otu4CfgTimeslot66valPortn,
       "pm10001otu4CfgTimeslot67valPortn": pm10001otu4CfgTimeslot67valPortn,
       "pm10001otu4CfgTimeslot68valPortn": pm10001otu4CfgTimeslot68valPortn,
       "pm10001otu4CfgTimeslot69valPortn": pm10001otu4CfgTimeslot69valPortn,
       "pm10001otu4CfgTimeslot70valPortn": pm10001otu4CfgTimeslot70valPortn,
       "pm10001otu4CfgTimeslot71valPortn": pm10001otu4CfgTimeslot71valPortn,
       "pm10001otu4CfgTimeslot72valPortn": pm10001otu4CfgTimeslot72valPortn,
       "pm10001otu4CfgTimeslot73valPortn": pm10001otu4CfgTimeslot73valPortn,
       "pm10001otu4CfgTimeslot74valPortn": pm10001otu4CfgTimeslot74valPortn,
       "pm10001otu4CfgTimeslot75valPortn": pm10001otu4CfgTimeslot75valPortn,
       "pm10001otu4CfgTimeslot76valPortn": pm10001otu4CfgTimeslot76valPortn,
       "pm10001otu4CfgTimeslot77valPortn": pm10001otu4CfgTimeslot77valPortn,
       "pm10001otu4CfgTimeslot78valPortn": pm10001otu4CfgTimeslot78valPortn,
       "pm10001otu4CfgTimeslot79valPortn": pm10001otu4CfgTimeslot79valPortn,
       "pm10001otu4CfgTimeslot80valPortn": pm10001otu4CfgTimeslot80valPortn,
       "pm10001otu4CfgWriteConfiguration": pm10001otu4CfgWriteConfiguration,
       "pm10001otu4traps": pm10001otu4traps,
       "pm10001otu4trapPortNumber": pm10001otu4trapPortNumber,
       "pm10001otu4trapLineNumber": pm10001otu4trapLineNumber,
       "pm10001otu4trapBoardNumber": pm10001otu4trapBoardNumber,
       "pm10001otu4LineTrapNotUrgentGoesOn": pm10001otu4LineTrapNotUrgentGoesOn,
       "pm10001otu4LineTrapNotUrgentGoesOff": pm10001otu4LineTrapNotUrgentGoesOff,
       "pm10001otu4LineTrapUrgentGoesOn": pm10001otu4LineTrapUrgentGoesOn,
       "pm10001otu4LineTrapUrgentGoesOff": pm10001otu4LineTrapUrgentGoesOff,
       "pm10001otu4LineTrapCritGoesOn": pm10001otu4LineTrapCritGoesOn,
       "pm10001otu4LineTrapCritGoesOff": pm10001otu4LineTrapCritGoesOff,
       "pm10001otu4ClientTrapNotUrgentGoesOn": pm10001otu4ClientTrapNotUrgentGoesOn,
       "pm10001otu4ClientTrapNotUrgentGoesOff": pm10001otu4ClientTrapNotUrgentGoesOff,
       "pm10001otu4ClientTrapUrgentGoesOn": pm10001otu4ClientTrapUrgentGoesOn,
       "pm10001otu4ClientTrapUrgentGoesOff": pm10001otu4ClientTrapUrgentGoesOff,
       "pm10001otu4ClientTrapCritGoesOn": pm10001otu4ClientTrapCritGoesOn,
       "pm10001otu4ClientTrapCritGoesOff": pm10001otu4ClientTrapCritGoesOff,
       "pm10001otu4PowerTrapUrgentGoesOn": pm10001otu4PowerTrapUrgentGoesOn,
       "pm10001otu4PowerTrapUrgentGoesOff": pm10001otu4PowerTrapUrgentGoesOff,
       "pm10001otu4Monitoring": pm10001otu4Monitoring,
       "pm10001otu4MonOther": pm10001otu4MonOther,
       "pm10001otu4MonRmon": pm10001otu4MonRmon,
       "pm10001otu4MonClient": pm10001otu4MonClient,
       "pm10001otu4MonClientRmonCounter": pm10001otu4MonClientRmonCounter,
       "pm10001otu4MonupRmonBytesCounterClientInputTable": pm10001otu4MonupRmonBytesCounterClientInputTable,
       "pm10001otu4MonupRmonBytesCounterClientInputEntry": pm10001otu4MonupRmonBytesCounterClientInputEntry,
       "pm10001otu4MonupRmonBytesCounterClientInputIndex": pm10001otu4MonupRmonBytesCounterClientInputIndex,
       "pm10001otu4MonupRmonBytesCounterClientInputValuePortn": pm10001otu4MonupRmonBytesCounterClientInputValuePortn,
       "pm10001otu4MonupRmonBytesCounterClientInputErrorPortn": pm10001otu4MonupRmonBytesCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn": pm10001otu4MonupRmonBytesCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonCrcErrorsCounterClientInputTable": pm10001otu4MonupRmonCrcErrorsCounterClientInputTable,
       "pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry": pm10001otu4MonupRmonCrcErrorsCounterClientInputEntry,
       "pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex": pm10001otu4MonupRmonCrcErrorsCounterClientInputIndex,
       "pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn": pm10001otu4MonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn": pm10001otu4MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn": pm10001otu4MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonPacketsCounterClientInputTable": pm10001otu4MonupRmonPacketsCounterClientInputTable,
       "pm10001otu4MonupRmonPacketsCounterClientInputEntry": pm10001otu4MonupRmonPacketsCounterClientInputEntry,
       "pm10001otu4MonupRmonPacketsCounterClientInputIndex": pm10001otu4MonupRmonPacketsCounterClientInputIndex,
       "pm10001otu4MonupRmonPacketsCounterClientInputValuePortn": pm10001otu4MonupRmonPacketsCounterClientInputValuePortn,
       "pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn": pm10001otu4MonupRmonPacketsCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn": pm10001otu4MonupRmonPacketsCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonBroadcastCounterClientInputTable": pm10001otu4MonupRmonBroadcastCounterClientInputTable,
       "pm10001otu4MonupRmonBroadcastCounterClientInputEntry": pm10001otu4MonupRmonBroadcastCounterClientInputEntry,
       "pm10001otu4MonupRmonBroadcastCounterClientInputIndex": pm10001otu4MonupRmonBroadcastCounterClientInputIndex,
       "pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn": pm10001otu4MonupRmonBroadcastCounterClientInputValuePortn,
       "pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn": pm10001otu4MonupRmonBroadcastCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn": pm10001otu4MonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonMulticastCounterClientInputTable": pm10001otu4MonupRmonMulticastCounterClientInputTable,
       "pm10001otu4MonupRmonMulticastCounterClientInputEntry": pm10001otu4MonupRmonMulticastCounterClientInputEntry,
       "pm10001otu4MonupRmonMulticastCounterClientInputIndex": pm10001otu4MonupRmonMulticastCounterClientInputIndex,
       "pm10001otu4MonupRmonMulticastCounterClientInputValuePortn": pm10001otu4MonupRmonMulticastCounterClientInputValuePortn,
       "pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn": pm10001otu4MonupRmonMulticastCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn": pm10001otu4MonupRmonMulticastCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonPauseFrameCounterClientInputTable": pm10001otu4MonupRmonPauseFrameCounterClientInputTable,
       "pm10001otu4MonupRmonPauseFrameCounterClientInputEntry": pm10001otu4MonupRmonPauseFrameCounterClientInputEntry,
       "pm10001otu4MonupRmonPauseFrameCounterClientInputIndex": pm10001otu4MonupRmonPauseFrameCounterClientInputIndex,
       "pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn": pm10001otu4MonupRmonPauseFrameCounterClientInputValuePortn,
       "pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn": pm10001otu4MonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn": pm10001otu4MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonUnicastCounterClientInputTable": pm10001otu4MonupRmonUnicastCounterClientInputTable,
       "pm10001otu4MonupRmonUnicastCounterClientInputEntry": pm10001otu4MonupRmonUnicastCounterClientInputEntry,
       "pm10001otu4MonupRmonUnicastCounterClientInputIndex": pm10001otu4MonupRmonUnicastCounterClientInputIndex,
       "pm10001otu4MonupRmonUnicastCounterClientInputValuePortn": pm10001otu4MonupRmonUnicastCounterClientInputValuePortn,
       "pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn": pm10001otu4MonupRmonUnicastCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn": pm10001otu4MonupRmonUnicastCounterClientInputOverloadPortn,
       "pm10001otu4MonupRmonNonunicastCounterClientInputTable": pm10001otu4MonupRmonNonunicastCounterClientInputTable,
       "pm10001otu4MonupRmonNonunicastCounterClientInputEntry": pm10001otu4MonupRmonNonunicastCounterClientInputEntry,
       "pm10001otu4MonupRmonNonunicastCounterClientInputIndex": pm10001otu4MonupRmonNonunicastCounterClientInputIndex,
       "pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn": pm10001otu4MonupRmonNonunicastCounterClientInputValuePortn,
       "pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn": pm10001otu4MonupRmonNonunicastCounterClientInputErrorPortn,
       "pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn": pm10001otu4MonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm10001otu4MondownRmonBytesCounterClientOutputTable": pm10001otu4MondownRmonBytesCounterClientOutputTable,
       "pm10001otu4MondownRmonBytesCounterClientOutputEntry": pm10001otu4MondownRmonBytesCounterClientOutputEntry,
       "pm10001otu4MondownRmonBytesCounterClientOutputIndex": pm10001otu4MondownRmonBytesCounterClientOutputIndex,
       "pm10001otu4MondownRmonBytesCounterClientOutputValuePortn": pm10001otu4MondownRmonBytesCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn": pm10001otu4MondownRmonBytesCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn": pm10001otu4MondownRmonBytesCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonCrcErrorsCounterClientOutputTable": pm10001otu4MondownRmonCrcErrorsCounterClientOutputTable,
       "pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry": pm10001otu4MondownRmonCrcErrorsCounterClientOutputEntry,
       "pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex": pm10001otu4MondownRmonCrcErrorsCounterClientOutputIndex,
       "pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn": pm10001otu4MondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn": pm10001otu4MondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm10001otu4MondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonPacketsCounterClientOutputTable": pm10001otu4MondownRmonPacketsCounterClientOutputTable,
       "pm10001otu4MondownRmonPacketsCounterClientOutputEntry": pm10001otu4MondownRmonPacketsCounterClientOutputEntry,
       "pm10001otu4MondownRmonPacketsCounterClientOutputIndex": pm10001otu4MondownRmonPacketsCounterClientOutputIndex,
       "pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn": pm10001otu4MondownRmonPacketsCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn": pm10001otu4MondownRmonPacketsCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn": pm10001otu4MondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonBroadcastCounterClientOutputTable": pm10001otu4MondownRmonBroadcastCounterClientOutputTable,
       "pm10001otu4MondownRmonBroadcastCounterClientOutputEntry": pm10001otu4MondownRmonBroadcastCounterClientOutputEntry,
       "pm10001otu4MondownRmonBroadcastCounterClientOutputIndex": pm10001otu4MondownRmonBroadcastCounterClientOutputIndex,
       "pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn": pm10001otu4MondownRmonBroadcastCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn": pm10001otu4MondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn": pm10001otu4MondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonMulticastCounterClientOutputTable": pm10001otu4MondownRmonMulticastCounterClientOutputTable,
       "pm10001otu4MondownRmonMulticastCounterClientOutputEntry": pm10001otu4MondownRmonMulticastCounterClientOutputEntry,
       "pm10001otu4MondownRmonMulticastCounterClientOutputIndex": pm10001otu4MondownRmonMulticastCounterClientOutputIndex,
       "pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn": pm10001otu4MondownRmonMulticastCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn": pm10001otu4MondownRmonMulticastCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn": pm10001otu4MondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonPauseFrameCounterClientOutputTable": pm10001otu4MondownRmonPauseFrameCounterClientOutputTable,
       "pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry": pm10001otu4MondownRmonPauseFrameCounterClientOutputEntry,
       "pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex": pm10001otu4MondownRmonPauseFrameCounterClientOutputIndex,
       "pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn": pm10001otu4MondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn": pm10001otu4MondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn": pm10001otu4MondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonUnicastCounterClientOutputTable": pm10001otu4MondownRmonUnicastCounterClientOutputTable,
       "pm10001otu4MondownRmonUnicastCounterClientOutputEntry": pm10001otu4MondownRmonUnicastCounterClientOutputEntry,
       "pm10001otu4MondownRmonUnicastCounterClientOutputIndex": pm10001otu4MondownRmonUnicastCounterClientOutputIndex,
       "pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn": pm10001otu4MondownRmonUnicastCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn": pm10001otu4MondownRmonUnicastCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn": pm10001otu4MondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm10001otu4MondownRmonNonunicastCounterClientOutputTable": pm10001otu4MondownRmonNonunicastCounterClientOutputTable,
       "pm10001otu4MondownRmonNonunicastCounterClientOutputEntry": pm10001otu4MondownRmonNonunicastCounterClientOutputEntry,
       "pm10001otu4MondownRmonNonunicastCounterClientOutputIndex": pm10001otu4MondownRmonNonunicastCounterClientOutputIndex,
       "pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn": pm10001otu4MondownRmonNonunicastCounterClientOutputValuePortn,
       "pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn": pm10001otu4MondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn": pm10001otu4MondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm10001otu4MonPerfOther": pm10001otu4MonPerfOther,
       "pm10001otu4MonPerfSync": pm10001otu4MonPerfSync,
       "pm10001otu4PerfEnable": pm10001otu4PerfEnable,
       "pm10001otu4Perf15minSync": pm10001otu4Perf15minSync,
       "pm10001otu4Perf24hSync": pm10001otu4Perf24hSync,
       "pm10001otu4MonPerfTimeStamp": pm10001otu4MonPerfTimeStamp,
       "pm10001otu4Perf15MinShort": pm10001otu4Perf15MinShort,
       "pm10001otu4Perf15MinLong": pm10001otu4Perf15MinLong,
       "pm10001otu4Perf24HoursShort": pm10001otu4Perf24HoursShort,
       "pm10001otu4Perf24HoursLong": pm10001otu4Perf24HoursLong,
       "pm10001otu4PerfCurrent15MinElapsedTime": pm10001otu4PerfCurrent15MinElapsedTime,
       "pm10001otu4PerfCurrent24HoursElapsedTime": pm10001otu4PerfCurrent24HoursElapsedTime,
       "pm10001otu4MonPerfClient": pm10001otu4MonPerfClient,
       "pm10001otu4PerfTelecomInputClientCurrent15StatTable": pm10001otu4PerfTelecomInputClientCurrent15StatTable,
       "pm10001otu4PerfTelecomInputClientCurrent15StatEntry": pm10001otu4PerfTelecomInputClientCurrent15StatEntry,
       "pm10001otu4PerfTelecomInputClientCurrent15StatIndex": pm10001otu4PerfTelecomInputClientCurrent15StatIndex,
       "pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn": pm10001otu4PerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn": pm10001otu4PerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn": pm10001otu4PerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn": pm10001otu4PerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn": pm10001otu4PerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn": pm10001otu4PerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn": pm10001otu4PerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn": pm10001otu4PerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn": pm10001otu4PerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn": pm10001otu4PerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Table": pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry": pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index": pm10001otu4PerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1": pm10001otu4PerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1": pm10001otu4PerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1": pm10001otu4PerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm10001otu4PerfTelecomInputClientCurrent24StatTable": pm10001otu4PerfTelecomInputClientCurrent24StatTable,
       "pm10001otu4PerfTelecomInputClientCurrent24StatEntry": pm10001otu4PerfTelecomInputClientCurrent24StatEntry,
       "pm10001otu4PerfTelecomInputClientCurrent24StatIndex": pm10001otu4PerfTelecomInputClientCurrent24StatIndex,
       "pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn": pm10001otu4PerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn": pm10001otu4PerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn": pm10001otu4PerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn": pm10001otu4PerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn": pm10001otu4PerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn": pm10001otu4PerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn": pm10001otu4PerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn": pm10001otu4PerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn": pm10001otu4PerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn": pm10001otu4PerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Table": pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry": pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index": pm10001otu4PerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1": pm10001otu4PerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1": pm10001otu4PerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1": pm10001otu4PerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatTable": pm10001otu4PerfTelecomOutputClientCurrent15StatTable,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatEntry": pm10001otu4PerfTelecomOutputClientCurrent15StatEntry,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatIndex": pm10001otu4PerfTelecomOutputClientCurrent15StatIndex,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn": pm10001otu4PerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn": pm10001otu4PerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn": pm10001otu4PerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn": pm10001otu4PerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn": pm10001otu4PerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn": pm10001otu4PerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn": pm10001otu4PerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn": pm10001otu4PerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn": pm10001otu4PerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn": pm10001otu4PerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Table": pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry": pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index": pm10001otu4PerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1": pm10001otu4PerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm10001otu4PerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm10001otu4PerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatTable": pm10001otu4PerfTelecomOutputClientCurrent24StatTable,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatEntry": pm10001otu4PerfTelecomOutputClientCurrent24StatEntry,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatIndex": pm10001otu4PerfTelecomOutputClientCurrent24StatIndex,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn": pm10001otu4PerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn": pm10001otu4PerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn": pm10001otu4PerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn": pm10001otu4PerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn": pm10001otu4PerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn": pm10001otu4PerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn": pm10001otu4PerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn": pm10001otu4PerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn": pm10001otu4PerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn": pm10001otu4PerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Table": pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry": pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index": pm10001otu4PerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1": pm10001otu4PerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm10001otu4PerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm10001otu4PerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm10001otu4PerfDatacomClientCurrent15StatTable": pm10001otu4PerfDatacomClientCurrent15StatTable,
       "pm10001otu4PerfDatacomClientCurrent15StatEntry": pm10001otu4PerfDatacomClientCurrent15StatEntry,
       "pm10001otu4PerfDatacomClientCurrent15StatIndex": pm10001otu4PerfDatacomClientCurrent15StatIndex,
       "rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn": rm10010perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatInCrcCountPortn": rm10010perfdatacomclientCurrent15StatInCrcCountPortn,
       "rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn": rm10010perfdatacomclientCurrent15StatInPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatInPacketCountPortn": rm10010perfdatacomclientCurrent15StatInPacketCountPortn,
       "rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn": rm10010perfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatOutCrcCountPortn": rm10010perfdatacomclientCurrent15StatOutCrcCountPortn,
       "rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn": rm10010perfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent15StatOutPacketCountPortn": rm10010perfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm10001otu4PerfDatacomClientPast15StatHistoryPort1Table": pm10001otu4PerfDatacomClientPast15StatHistoryPort1Table,
       "pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry": pm10001otu4PerfDatacomClientPast15StatHistoryPort1Entry,
       "pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index": pm10001otu4PerfDatacomClientPast15StatHistoryPort1Index,
       "rm10010perfdatacomclientPast15StatInCrcCountInvPort1": rm10010perfdatacomclientPast15StatInCrcCountInvPort1,
       "rm10010perfdatacomclientPast15StatInCrcCountPort1": rm10010perfdatacomclientPast15StatInCrcCountPort1,
       "rm10010perfdatacomclientPast15StatInPacketCountInvPort1": rm10010perfdatacomclientPast15StatInPacketCountInvPort1,
       "rm10010perfdatacomclientPast15StatInPacketCountPort1": rm10010perfdatacomclientPast15StatInPacketCountPort1,
       "rm10010perfdatacomclientPast15StatOutCrcCountInvPort1": rm10010perfdatacomclientPast15StatOutCrcCountInvPort1,
       "rm10010perfdatacomclientPast15StatOutCrcCountPort1": rm10010perfdatacomclientPast15StatOutCrcCountPort1,
       "rm10010perfdatacomclientPast15StatOutPacketCountInvPort1": rm10010perfdatacomclientPast15StatOutPacketCountInvPort1,
       "rm10010perfdatacomclientPast15StatOutPacketCountPort1": rm10010perfdatacomclientPast15StatOutPacketCountPort1,
       "pm10001otu4PerfDatacomClientCurrent24StatTable": pm10001otu4PerfDatacomClientCurrent24StatTable,
       "pm10001otu4PerfDatacomClientCurrent24StatEntry": pm10001otu4PerfDatacomClientCurrent24StatEntry,
       "pm10001otu4PerfDatacomClientCurrent24StatIndex": pm10001otu4PerfDatacomClientCurrent24StatIndex,
       "rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn": rm10010perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatInCrcCountPortn": rm10010perfdatacomclientCurrent24StatInCrcCountPortn,
       "rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn": rm10010perfdatacomclientCurrent24StatInPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatInPacketCountPortn": rm10010perfdatacomclientCurrent24StatInPacketCountPortn,
       "rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn": rm10010perfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatOutCrcCountPortn": rm10010perfdatacomclientCurrent24StatOutCrcCountPortn,
       "rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn": rm10010perfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "rm10010perfdatacomclientCurrent24StatOutPacketCountPortn": rm10010perfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm10001otu4PerfDatacomClientPast24StatHistoryPort1Table": pm10001otu4PerfDatacomClientPast24StatHistoryPort1Table,
       "pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry": pm10001otu4PerfDatacomClientPast24StatHistoryPort1Entry,
       "pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index": pm10001otu4PerfDatacomClientPast24StatHistoryPort1Index,
       "rm10010perfdatacomclientPast24StatInCrcCountInvPort1": rm10010perfdatacomclientPast24StatInCrcCountInvPort1,
       "rm10010perfdatacomclientPast24StatInCrcCountPort1": rm10010perfdatacomclientPast24StatInCrcCountPort1,
       "rm10010perfdatacomclientPast24StatInPacketCountInvPort1": rm10010perfdatacomclientPast24StatInPacketCountInvPort1,
       "rm10010perfdatacomclientPast24StatInPacketCountPort1": rm10010perfdatacomclientPast24StatInPacketCountPort1,
       "rm10010perfdatacomclientPast24StatOutCrcCountInvPort1": rm10010perfdatacomclientPast24StatOutCrcCountInvPort1,
       "rm10010perfdatacomclientPast24StatOutCrcCountPort1": rm10010perfdatacomclientPast24StatOutCrcCountPort1,
       "rm10010perfdatacomclientPast24StatOutPacketCountInvPort1": rm10010perfdatacomclientPast24StatOutPacketCountInvPort1,
       "rm10010perfdatacomclientPast24StatOutPacketCountPort1": rm10010perfdatacomclientPast24StatOutPacketCountPort1,
       "pm10001otu4MonPerfLine": pm10001otu4MonPerfLine,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatTable": pm10001otu4PerfTelecomLinePostFecCurrent15StatTable,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry": pm10001otu4PerfTelecomLinePostFecCurrent15StatEntry,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex": pm10001otu4PerfTelecomLinePostFecCurrent15StatIndex,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Table": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm10001otu4PerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatTable": pm10001otu4PerfTelecomLinePostFecCurrent24StatTable,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry": pm10001otu4PerfTelecomLinePostFecCurrent24StatEntry,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex": pm10001otu4PerfTelecomLinePostFecCurrent24StatIndex,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn": pm10001otu4PerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Table": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm10001otu4PerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatTable": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatTable,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm10001otu4PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm10001otu4PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatTable": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatTable,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm10001otu4PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm10001otu4PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
