# SNMP MIB module (EKINOPS-Pm10010mr-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm10010mr-MIB.mib
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

modulePm10010mr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63)
)
if mibBuilder.loadTexts:
    modulePm10010mr.setRevisions(
        ("2014-04-10 00:00",
         "2014-10-14 00:00",
         "2015-01-23 00:00",
         "2015-10-21 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm10010mrMultiRate(TextualConvention, Integer32):
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



class Pm10010mrOtxMode(TextualConvention, Integer32):
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



class Pm10010mrOtxGrid(TextualConvention, Integer32):
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



class Pm10010mrAdjustValue(TextualConvention, Integer32):
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



class Pm10010mrClientProtocol(TextualConvention, Integer32):
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



class Pm10010mrProtocolMode(TextualConvention, Integer32):
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



class Pm10010mrOtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm10010mrOrxChannel(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_Pm10010mralarms_ObjectIdentity = ObjectIdentity
pm10010mralarms = _Pm10010mralarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2)
)
_Pm10010mrAlmOther_ObjectIdentity = ObjectIdentity
pm10010mrAlmOther = _Pm10010mrAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1)
)
_Pm10010mrAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm10010mrAlmOtherNurg = _Pm10010mrAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1)
)
_Pm10010mrAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm10010mrAlmsynthAlm2 = _Pm10010mrAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1, 2)
)
_Pm10010mrAlmConfTableSave_Type = EkiOnOff
_Pm10010mrAlmConfTableSave_Object = MibScalar
pm10010mrAlmConfTableSave = _Pm10010mrAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1, 2, 1),
    _Pm10010mrAlmConfTableSave_Type()
)
pm10010mrAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmConfTableSave.setStatus("current")
_Pm10010mrAlmInvUpload_Type = EkiOnOff
_Pm10010mrAlmInvUpload_Object = MibScalar
pm10010mrAlmInvUpload = _Pm10010mrAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1, 2, 2),
    _Pm10010mrAlmInvUpload_Type()
)
pm10010mrAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmInvUpload.setStatus("current")
_Pm10010mrAlmConfTableLoad_Type = EkiOnOff
_Pm10010mrAlmConfTableLoad_Object = MibScalar
pm10010mrAlmConfTableLoad = _Pm10010mrAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1, 2, 3),
    _Pm10010mrAlmConfTableLoad_Type()
)
pm10010mrAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmConfTableLoad.setStatus("current")
_Pm10010mrAlmCorrelatOff_Type = EkiOnOff
_Pm10010mrAlmCorrelatOff_Object = MibScalar
pm10010mrAlmCorrelatOff = _Pm10010mrAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1, 2, 4),
    _Pm10010mrAlmCorrelatOff_Type()
)
pm10010mrAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCorrelatOff.setStatus("current")
_Pm10010mrAlmMaintenanceOn_Type = EkiOnOff
_Pm10010mrAlmMaintenanceOn_Object = MibScalar
pm10010mrAlmMaintenanceOn = _Pm10010mrAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 1, 2, 5),
    _Pm10010mrAlmMaintenanceOn_Type()
)
pm10010mrAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMaintenanceOn.setStatus("current")
_Pm10010mrAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm10010mrAlmOtherUrg = _Pm10010mrAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 2)
)
_Pm10010mrAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm10010mrAlmOtherCrit = _Pm10010mrAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3)
)
_Pm10010mrAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm10010mrAlmsynthAlm0 = _Pm10010mrAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 0)
)
_Pm10010mrAlmFailFan_Type = EkiOnOff
_Pm10010mrAlmFailFan_Object = MibScalar
pm10010mrAlmFailFan = _Pm10010mrAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 0, 2),
    _Pm10010mrAlmFailFan_Type()
)
pm10010mrAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmFailFan.setStatus("current")
_Pm10010mrAlmModGlobFail_Type = EkiOnOff
_Pm10010mrAlmModGlobFail_Object = MibScalar
pm10010mrAlmModGlobFail = _Pm10010mrAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 0, 9),
    _Pm10010mrAlmModGlobFail_Type()
)
pm10010mrAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmModGlobFail.setStatus("current")
_Pm10010mrAlmDefFuseA_Type = EkiOnOff
_Pm10010mrAlmDefFuseA_Object = MibScalar
pm10010mrAlmDefFuseA = _Pm10010mrAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 0, 15),
    _Pm10010mrAlmDefFuseA_Type()
)
pm10010mrAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmDefFuseA.setStatus("current")
_Pm10010mrAlmDefFuseB_Type = EkiOnOff
_Pm10010mrAlmDefFuseB_Object = MibScalar
pm10010mrAlmDefFuseB = _Pm10010mrAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 0, 16),
    _Pm10010mrAlmDefFuseB_Type()
)
pm10010mrAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmDefFuseB.setStatus("current")
_Pm10010mrAlmclientModuleState_ObjectIdentity = ObjectIdentity
pm10010mrAlmclientModuleState = _Pm10010mrAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40)
)
_Pm10010mrAlmCfpInitialize_Type = EkiOnOff
_Pm10010mrAlmCfpInitialize_Object = MibScalar
pm10010mrAlmCfpInitialize = _Pm10010mrAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 1),
    _Pm10010mrAlmCfpInitialize_Type()
)
pm10010mrAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpInitialize.setStatus("current")
_Pm10010mrAlmCfpLowPower_Type = EkiOnOff
_Pm10010mrAlmCfpLowPower_Object = MibScalar
pm10010mrAlmCfpLowPower = _Pm10010mrAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 2),
    _Pm10010mrAlmCfpLowPower_Type()
)
pm10010mrAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpLowPower.setStatus("current")
_Pm10010mrAlmCfpHighPowerUp_Type = EkiOnOff
_Pm10010mrAlmCfpHighPowerUp_Object = MibScalar
pm10010mrAlmCfpHighPowerUp = _Pm10010mrAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 3),
    _Pm10010mrAlmCfpHighPowerUp_Type()
)
pm10010mrAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpHighPowerUp.setStatus("current")
_Pm10010mrAlmCfpTxOff_Type = EkiOnOff
_Pm10010mrAlmCfpTxOff_Object = MibScalar
pm10010mrAlmCfpTxOff = _Pm10010mrAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 4),
    _Pm10010mrAlmCfpTxOff_Type()
)
pm10010mrAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxOff.setStatus("current")
_Pm10010mrAlmCfpTxTurnOn_Type = EkiOnOff
_Pm10010mrAlmCfpTxTurnOn_Object = MibScalar
pm10010mrAlmCfpTxTurnOn = _Pm10010mrAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 5),
    _Pm10010mrAlmCfpTxTurnOn_Type()
)
pm10010mrAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxTurnOn.setStatus("current")
_Pm10010mrAlmCfpReady_Type = EkiOnOff
_Pm10010mrAlmCfpReady_Object = MibScalar
pm10010mrAlmCfpReady = _Pm10010mrAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 6),
    _Pm10010mrAlmCfpReady_Type()
)
pm10010mrAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpReady.setStatus("current")
_Pm10010mrAlmCfpFault_Type = EkiOnOff
_Pm10010mrAlmCfpFault_Object = MibScalar
pm10010mrAlmCfpFault = _Pm10010mrAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 7),
    _Pm10010mrAlmCfpFault_Type()
)
pm10010mrAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpFault.setStatus("current")
_Pm10010mrAlmCfpTxTurnOff_Type = EkiOnOff
_Pm10010mrAlmCfpTxTurnOff_Object = MibScalar
pm10010mrAlmCfpTxTurnOff = _Pm10010mrAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 8),
    _Pm10010mrAlmCfpTxTurnOff_Type()
)
pm10010mrAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxTurnOff.setStatus("current")
_Pm10010mrAlmCfpHighPowerDown_Type = EkiOnOff
_Pm10010mrAlmCfpHighPowerDown_Object = MibScalar
pm10010mrAlmCfpHighPowerDown = _Pm10010mrAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 40, 9),
    _Pm10010mrAlmCfpHighPowerDown_Type()
)
pm10010mrAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpHighPowerDown.setStatus("current")
_Pm10010mrAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010mrAlmclientModuleGeneralStatus = _Pm10010mrAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41)
)
_Pm10010mrAlmCfpOutOfAlignment_Type = EkiOnOff
_Pm10010mrAlmCfpOutOfAlignment_Object = MibScalar
pm10010mrAlmCfpOutOfAlignment = _Pm10010mrAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 4),
    _Pm10010mrAlmCfpOutOfAlignment_Type()
)
pm10010mrAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpOutOfAlignment.setStatus("current")
_Pm10010mrAlmCfpRxNetworkLol_Type = EkiOnOff
_Pm10010mrAlmCfpRxNetworkLol_Object = MibScalar
pm10010mrAlmCfpRxNetworkLol = _Pm10010mrAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 5),
    _Pm10010mrAlmCfpRxNetworkLol_Type()
)
pm10010mrAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpRxNetworkLol.setStatus("current")
_Pm10010mrAlmCfpRxLos_Type = EkiOnOff
_Pm10010mrAlmCfpRxLos_Object = MibScalar
pm10010mrAlmCfpRxLos = _Pm10010mrAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 6),
    _Pm10010mrAlmCfpRxLos_Type()
)
pm10010mrAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpRxLos.setStatus("current")
_Pm10010mrAlmCfpTxHostLol_Type = EkiOnOff
_Pm10010mrAlmCfpTxHostLol_Object = MibScalar
pm10010mrAlmCfpTxHostLol = _Pm10010mrAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 7),
    _Pm10010mrAlmCfpTxHostLol_Type()
)
pm10010mrAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxHostLol.setStatus("current")
_Pm10010mrAlmCfpTxLosf_Type = EkiOnOff
_Pm10010mrAlmCfpTxLosf_Object = MibScalar
pm10010mrAlmCfpTxLosf = _Pm10010mrAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 8),
    _Pm10010mrAlmCfpTxLosf_Type()
)
pm10010mrAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxLosf.setStatus("current")
_Pm10010mrAlmCfpTxCmuLol_Type = EkiOnOff
_Pm10010mrAlmCfpTxCmuLol_Object = MibScalar
pm10010mrAlmCfpTxCmuLol = _Pm10010mrAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 9),
    _Pm10010mrAlmCfpTxCmuLol_Type()
)
pm10010mrAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxCmuLol.setStatus("current")
_Pm10010mrAlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm10010mrAlmCfpTxJitterPllLol_Object = MibScalar
pm10010mrAlmCfpTxJitterPllLol = _Pm10010mrAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 10),
    _Pm10010mrAlmCfpTxJitterPllLol_Type()
)
pm10010mrAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpTxJitterPllLol.setStatus("current")
_Pm10010mrAlmCfpLossOfRefclk_Type = EkiOnOff
_Pm10010mrAlmCfpLossOfRefclk_Object = MibScalar
pm10010mrAlmCfpLossOfRefclk = _Pm10010mrAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 11),
    _Pm10010mrAlmCfpLossOfRefclk_Type()
)
pm10010mrAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpLossOfRefclk.setStatus("current")
_Pm10010mrAlmCfpHwInterlock_Type = EkiOnOff
_Pm10010mrAlmCfpHwInterlock_Object = MibScalar
pm10010mrAlmCfpHwInterlock = _Pm10010mrAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 41, 14),
    _Pm10010mrAlmCfpHwInterlock_Type()
)
pm10010mrAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpHwInterlock.setStatus("current")
_Pm10010mrAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mrAlmclientGlobalAlarmSummary = _Pm10010mrAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42)
)
_Pm10010mrAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010mrAlmCfpSoftGlobAlarmTest_Object = MibScalar
pm10010mrAlmCfpSoftGlobAlarmTest = _Pm10010mrAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 1),
    _Pm10010mrAlmCfpSoftGlobAlarmTest_Type()
)
pm10010mrAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm10010mrAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010mrAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm10010mrAlmCfpNetworkLaneAlarmWarning2 = _Pm10010mrAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 7),
    _Pm10010mrAlmCfpNetworkLaneAlarmWarning2_Type()
)
pm10010mrAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010mrAlmCfpModuleState_Type = EkiOnOff
_Pm10010mrAlmCfpModuleState_Object = MibScalar
pm10010mrAlmCfpModuleState = _Pm10010mrAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 8),
    _Pm10010mrAlmCfpModuleState_Type()
)
pm10010mrAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpModuleState.setStatus("current")
_Pm10010mrAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm10010mrAlmCfpModuleGeneralStatus_Object = MibScalar
pm10010mrAlmCfpModuleGeneralStatus = _Pm10010mrAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 9),
    _Pm10010mrAlmCfpModuleGeneralStatus_Type()
)
pm10010mrAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpModuleGeneralStatus.setStatus("current")
_Pm10010mrAlmCfpModuleFault_Type = EkiOnOff
_Pm10010mrAlmCfpModuleFault_Object = MibScalar
pm10010mrAlmCfpModuleFault = _Pm10010mrAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 10),
    _Pm10010mrAlmCfpModuleFault_Type()
)
pm10010mrAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpModuleFault.setStatus("current")
_Pm10010mrAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm10010mrAlmCfpModuleAlarmWarning1_Object = MibScalar
pm10010mrAlmCfpModuleAlarmWarning1 = _Pm10010mrAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 11),
    _Pm10010mrAlmCfpModuleAlarmWarning1_Type()
)
pm10010mrAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpModuleAlarmWarning1.setStatus("current")
_Pm10010mrAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm10010mrAlmCfpModuleAlarmWarning2_Object = MibScalar
pm10010mrAlmCfpModuleAlarmWarning2 = _Pm10010mrAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 12),
    _Pm10010mrAlmCfpModuleAlarmWarning2_Type()
)
pm10010mrAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpModuleAlarmWarning2.setStatus("current")
_Pm10010mrAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010mrAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm10010mrAlmCfpNetworkLaneAlarmWarning1 = _Pm10010mrAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 13),
    _Pm10010mrAlmCfpNetworkLaneAlarmWarning1_Type()
)
pm10010mrAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010mrAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010mrAlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm10010mrAlmCfpNetworkLaneFaultStatus = _Pm10010mrAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 14),
    _Pm10010mrAlmCfpNetworkLaneFaultStatus_Type()
)
pm10010mrAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm10010mrAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm10010mrAlmCfpHostLaneFaultStatus_Object = MibScalar
pm10010mrAlmCfpHostLaneFaultStatus = _Pm10010mrAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 15),
    _Pm10010mrAlmCfpHostLaneFaultStatus_Type()
)
pm10010mrAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpHostLaneFaultStatus.setStatus("current")
_Pm10010mrAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm10010mrAlmCfpGlobAlarmAssertion_Object = MibScalar
pm10010mrAlmCfpGlobAlarmAssertion = _Pm10010mrAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 42, 16),
    _Pm10010mrAlmCfpGlobAlarmAssertion_Type()
)
pm10010mrAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmCfpGlobAlarmAssertion.setStatus("current")
_Pm10010mrAlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaModuleState = _Pm10010mrAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46)
)
_Pm10010mrAlmMsaInitialize_Type = EkiOnOff
_Pm10010mrAlmMsaInitialize_Object = MibScalar
pm10010mrAlmMsaInitialize = _Pm10010mrAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 1),
    _Pm10010mrAlmMsaInitialize_Type()
)
pm10010mrAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaInitialize.setStatus("current")
_Pm10010mrAlmMsaLowPower_Type = EkiOnOff
_Pm10010mrAlmMsaLowPower_Object = MibScalar
pm10010mrAlmMsaLowPower = _Pm10010mrAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 2),
    _Pm10010mrAlmMsaLowPower_Type()
)
pm10010mrAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaLowPower.setStatus("current")
_Pm10010mrAlmMsaHighPowerUp_Type = EkiOnOff
_Pm10010mrAlmMsaHighPowerUp_Object = MibScalar
pm10010mrAlmMsaHighPowerUp = _Pm10010mrAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 3),
    _Pm10010mrAlmMsaHighPowerUp_Type()
)
pm10010mrAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaHighPowerUp.setStatus("current")
_Pm10010mrAlmMsaTxOff_Type = EkiOnOff
_Pm10010mrAlmMsaTxOff_Object = MibScalar
pm10010mrAlmMsaTxOff = _Pm10010mrAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 4),
    _Pm10010mrAlmMsaTxOff_Type()
)
pm10010mrAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxOff.setStatus("current")
_Pm10010mrAlmMsaTxTurnOn_Type = EkiOnOff
_Pm10010mrAlmMsaTxTurnOn_Object = MibScalar
pm10010mrAlmMsaTxTurnOn = _Pm10010mrAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 5),
    _Pm10010mrAlmMsaTxTurnOn_Type()
)
pm10010mrAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxTurnOn.setStatus("current")
_Pm10010mrAlmMsaReady_Type = EkiOnOff
_Pm10010mrAlmMsaReady_Object = MibScalar
pm10010mrAlmMsaReady = _Pm10010mrAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 6),
    _Pm10010mrAlmMsaReady_Type()
)
pm10010mrAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaReady.setStatus("current")
_Pm10010mrAlmMsaFault_Type = EkiOnOff
_Pm10010mrAlmMsaFault_Object = MibScalar
pm10010mrAlmMsaFault = _Pm10010mrAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 7),
    _Pm10010mrAlmMsaFault_Type()
)
pm10010mrAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaFault.setStatus("current")
_Pm10010mrAlmMsaTxTurnOff_Type = EkiOnOff
_Pm10010mrAlmMsaTxTurnOff_Object = MibScalar
pm10010mrAlmMsaTxTurnOff = _Pm10010mrAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 8),
    _Pm10010mrAlmMsaTxTurnOff_Type()
)
pm10010mrAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxTurnOff.setStatus("current")
_Pm10010mrAlmMsaHighPowerDown_Type = EkiOnOff
_Pm10010mrAlmMsaHighPowerDown_Object = MibScalar
pm10010mrAlmMsaHighPowerDown = _Pm10010mrAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 46, 9),
    _Pm10010mrAlmMsaHighPowerDown_Type()
)
pm10010mrAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaHighPowerDown.setStatus("current")
_Pm10010mrAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaModuleGeneralStatus = _Pm10010mrAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47)
)
_Pm10010mrAlmMsaOutOfAlignment_Type = EkiOnOff
_Pm10010mrAlmMsaOutOfAlignment_Object = MibScalar
pm10010mrAlmMsaOutOfAlignment = _Pm10010mrAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 4),
    _Pm10010mrAlmMsaOutOfAlignment_Type()
)
pm10010mrAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaOutOfAlignment.setStatus("current")
_Pm10010mrAlmMsaRxNetworkLol_Type = EkiOnOff
_Pm10010mrAlmMsaRxNetworkLol_Object = MibScalar
pm10010mrAlmMsaRxNetworkLol = _Pm10010mrAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 5),
    _Pm10010mrAlmMsaRxNetworkLol_Type()
)
pm10010mrAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaRxNetworkLol.setStatus("current")
_Pm10010mrAlmMsaRxLos_Type = EkiOnOff
_Pm10010mrAlmMsaRxLos_Object = MibScalar
pm10010mrAlmMsaRxLos = _Pm10010mrAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 6),
    _Pm10010mrAlmMsaRxLos_Type()
)
pm10010mrAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaRxLos.setStatus("current")
_Pm10010mrAlmMsaTxHostLol_Type = EkiOnOff
_Pm10010mrAlmMsaTxHostLol_Object = MibScalar
pm10010mrAlmMsaTxHostLol = _Pm10010mrAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 7),
    _Pm10010mrAlmMsaTxHostLol_Type()
)
pm10010mrAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxHostLol.setStatus("current")
_Pm10010mrAlmMsaTxLosf_Type = EkiOnOff
_Pm10010mrAlmMsaTxLosf_Object = MibScalar
pm10010mrAlmMsaTxLosf = _Pm10010mrAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 8),
    _Pm10010mrAlmMsaTxLosf_Type()
)
pm10010mrAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxLosf.setStatus("current")
_Pm10010mrAlmMsaTxCmuLol_Type = EkiOnOff
_Pm10010mrAlmMsaTxCmuLol_Object = MibScalar
pm10010mrAlmMsaTxCmuLol = _Pm10010mrAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 9),
    _Pm10010mrAlmMsaTxCmuLol_Type()
)
pm10010mrAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxCmuLol.setStatus("current")
_Pm10010mrAlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm10010mrAlmMsaTxJitterPllLol_Object = MibScalar
pm10010mrAlmMsaTxJitterPllLol = _Pm10010mrAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 10),
    _Pm10010mrAlmMsaTxJitterPllLol_Type()
)
pm10010mrAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaTxJitterPllLol.setStatus("current")
_Pm10010mrAlmMsaLossOfRefclk_Type = EkiOnOff
_Pm10010mrAlmMsaLossOfRefclk_Object = MibScalar
pm10010mrAlmMsaLossOfRefclk = _Pm10010mrAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 11),
    _Pm10010mrAlmMsaLossOfRefclk_Type()
)
pm10010mrAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaLossOfRefclk.setStatus("current")
_Pm10010mrAlmMsaHwInterlock_Type = EkiOnOff
_Pm10010mrAlmMsaHwInterlock_Object = MibScalar
pm10010mrAlmMsaHwInterlock = _Pm10010mrAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 47, 14),
    _Pm10010mrAlmMsaHwInterlock_Type()
)
pm10010mrAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaHwInterlock.setStatus("current")
_Pm10010mrAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaGlobalAlarmSummary = _Pm10010mrAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48)
)
_Pm10010mrAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010mrAlmMsaSoftGlobAlarmTest_Object = MibScalar
pm10010mrAlmMsaSoftGlobAlarmTest = _Pm10010mrAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 1),
    _Pm10010mrAlmMsaSoftGlobAlarmTest_Type()
)
pm10010mrAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm10010mrAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm10010mrAlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm10010mrAlmMsaNetworkHostAlarmStatus = _Pm10010mrAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 6),
    _Pm10010mrAlmMsaNetworkHostAlarmStatus_Type()
)
pm10010mrAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm10010mrAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010mrAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm10010mrAlmMsaNetworkLaneAlarmWarning2 = _Pm10010mrAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 7),
    _Pm10010mrAlmMsaNetworkLaneAlarmWarning2_Type()
)
pm10010mrAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010mrAlmMsaModuleState_Type = EkiOnOff
_Pm10010mrAlmMsaModuleState_Object = MibScalar
pm10010mrAlmMsaModuleState = _Pm10010mrAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 8),
    _Pm10010mrAlmMsaModuleState_Type()
)
pm10010mrAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaModuleState.setStatus("current")
_Pm10010mrAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm10010mrAlmMsaModuleGeneralStatus_Object = MibScalar
pm10010mrAlmMsaModuleGeneralStatus = _Pm10010mrAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 9),
    _Pm10010mrAlmMsaModuleGeneralStatus_Type()
)
pm10010mrAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaModuleGeneralStatus.setStatus("current")
_Pm10010mrAlmModuleFault_Type = EkiOnOff
_Pm10010mrAlmModuleFault_Object = MibScalar
pm10010mrAlmModuleFault = _Pm10010mrAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 10),
    _Pm10010mrAlmModuleFault_Type()
)
pm10010mrAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmModuleFault.setStatus("current")
_Pm10010mrAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm10010mrAlmMsaModuleAlarmWarning1_Object = MibScalar
pm10010mrAlmMsaModuleAlarmWarning1 = _Pm10010mrAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 11),
    _Pm10010mrAlmMsaModuleAlarmWarning1_Type()
)
pm10010mrAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaModuleAlarmWarning1.setStatus("current")
_Pm10010mrAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm10010mrAlmMsaModuleAlarmWarning2_Object = MibScalar
pm10010mrAlmMsaModuleAlarmWarning2 = _Pm10010mrAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 12),
    _Pm10010mrAlmMsaModuleAlarmWarning2_Type()
)
pm10010mrAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaModuleAlarmWarning2.setStatus("current")
_Pm10010mrAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010mrAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm10010mrAlmMsaNetworkLaneAlarmWarning1 = _Pm10010mrAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 13),
    _Pm10010mrAlmMsaNetworkLaneAlarmWarning1_Type()
)
pm10010mrAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010mrAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010mrAlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm10010mrAlmMsaNetworkLaneFaultStatus = _Pm10010mrAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 14),
    _Pm10010mrAlmMsaNetworkLaneFaultStatus_Type()
)
pm10010mrAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm10010mrAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm10010mrAlmMsaHostLaneFaultStatus_Object = MibScalar
pm10010mrAlmMsaHostLaneFaultStatus = _Pm10010mrAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 15),
    _Pm10010mrAlmMsaHostLaneFaultStatus_Type()
)
pm10010mrAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaHostLaneFaultStatus.setStatus("current")
_Pm10010mrAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm10010mrAlmMsaGlobAlarmAssertion_Object = MibScalar
pm10010mrAlmMsaGlobAlarmAssertion = _Pm10010mrAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 48, 16),
    _Pm10010mrAlmMsaGlobAlarmAssertion_Type()
)
pm10010mrAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmMsaGlobAlarmAssertion.setStatus("current")
_Pm10010mrAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaNetworkTxAlignment = _Pm10010mrAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 49)
)
_Pm10010mrAlmNetTxTimingFault_Type = EkiOnOff
_Pm10010mrAlmNetTxTimingFault_Object = MibScalar
pm10010mrAlmNetTxTimingFault = _Pm10010mrAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 49, 12),
    _Pm10010mrAlmNetTxTimingFault_Type()
)
pm10010mrAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetTxTimingFault.setStatus("current")
_Pm10010mrAlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm10010mrAlmNetTxReferenceClockFault_Object = MibScalar
pm10010mrAlmNetTxReferenceClockFault = _Pm10010mrAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 49, 13),
    _Pm10010mrAlmNetTxReferenceClockFault_Type()
)
pm10010mrAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetTxReferenceClockFault.setStatus("current")
_Pm10010mrAlmNetTxCmuLockFault_Type = EkiOnOff
_Pm10010mrAlmNetTxCmuLockFault_Object = MibScalar
pm10010mrAlmNetTxCmuLockFault = _Pm10010mrAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 49, 14),
    _Pm10010mrAlmNetTxCmuLockFault_Type()
)
pm10010mrAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetTxCmuLockFault.setStatus("current")
_Pm10010mrAlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm10010mrAlmNetTxOutOfAlignment_Object = MibScalar
pm10010mrAlmNetTxOutOfAlignment = _Pm10010mrAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 49, 15),
    _Pm10010mrAlmNetTxOutOfAlignment_Type()
)
pm10010mrAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetTxOutOfAlignment.setStatus("current")
_Pm10010mrAlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm10010mrAlmNetTxLossOfAlignment_Object = MibScalar
pm10010mrAlmNetTxLossOfAlignment = _Pm10010mrAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 49, 16),
    _Pm10010mrAlmNetTxLossOfAlignment_Type()
)
pm10010mrAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetTxLossOfAlignment.setStatus("current")
_Pm10010mrAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaNetworkRxAlignment = _Pm10010mrAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 50)
)
_Pm10010mrAlmNetRxTimingFault_Type = EkiOnOff
_Pm10010mrAlmNetRxTimingFault_Object = MibScalar
pm10010mrAlmNetRxTimingFault = _Pm10010mrAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 50, 12),
    _Pm10010mrAlmNetRxTimingFault_Type()
)
pm10010mrAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetRxTimingFault.setStatus("current")
_Pm10010mrAlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm10010mrAlmNetRxOutOfAlignment_Object = MibScalar
pm10010mrAlmNetRxOutOfAlignment = _Pm10010mrAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 50, 13),
    _Pm10010mrAlmNetRxOutOfAlignment_Type()
)
pm10010mrAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetRxOutOfAlignment.setStatus("current")
_Pm10010mrAlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm10010mrAlmNetRxLossOfAlignment_Object = MibScalar
pm10010mrAlmNetRxLossOfAlignment = _Pm10010mrAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 50, 14),
    _Pm10010mrAlmNetRxLossOfAlignment_Type()
)
pm10010mrAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetRxLossOfAlignment.setStatus("current")
_Pm10010mrAlmNetRxModemLockFault_Type = EkiOnOff
_Pm10010mrAlmNetRxModemLockFault_Object = MibScalar
pm10010mrAlmNetRxModemLockFault = _Pm10010mrAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 50, 15),
    _Pm10010mrAlmNetRxModemLockFault_Type()
)
pm10010mrAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetRxModemLockFault.setStatus("current")
_Pm10010mrAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm10010mrAlmNetRxModemSyncDetectFault_Object = MibScalar
pm10010mrAlmNetRxModemSyncDetectFault = _Pm10010mrAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 50, 16),
    _Pm10010mrAlmNetRxModemSyncDetectFault_Type()
)
pm10010mrAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetRxModemSyncDetectFault.setStatus("current")
_Pm10010mrAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaNetworkHostNetworkAlarmSummary = _Pm10010mrAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51)
)
_Pm10010mrAlmNetworkTxAlignment_Type = EkiOnOff
_Pm10010mrAlmNetworkTxAlignment_Object = MibScalar
pm10010mrAlmNetworkTxAlignment = _Pm10010mrAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51, 11),
    _Pm10010mrAlmNetworkTxAlignment_Type()
)
pm10010mrAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetworkTxAlignment.setStatus("current")
_Pm10010mrAlmNetworkRxAlignment_Type = EkiOnOff
_Pm10010mrAlmNetworkRxAlignment_Object = MibScalar
pm10010mrAlmNetworkRxAlignment = _Pm10010mrAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51, 12),
    _Pm10010mrAlmNetworkRxAlignment_Type()
)
pm10010mrAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetworkRxAlignment.setStatus("current")
_Pm10010mrAlmNetworkRxOtn_Type = EkiOnOff
_Pm10010mrAlmNetworkRxOtn_Object = MibScalar
pm10010mrAlmNetworkRxOtn = _Pm10010mrAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51, 13),
    _Pm10010mrAlmNetworkRxOtn_Type()
)
pm10010mrAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmNetworkRxOtn.setStatus("current")
_Pm10010mrAlmHostRxAlignment_Type = EkiOnOff
_Pm10010mrAlmHostRxAlignment_Object = MibScalar
pm10010mrAlmHostRxAlignment = _Pm10010mrAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51, 14),
    _Pm10010mrAlmHostRxAlignment_Type()
)
pm10010mrAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostRxAlignment.setStatus("current")
_Pm10010mrAlmHostTxAlignment_Type = EkiOnOff
_Pm10010mrAlmHostTxAlignment_Object = MibScalar
pm10010mrAlmHostTxAlignment = _Pm10010mrAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51, 15),
    _Pm10010mrAlmHostTxAlignment_Type()
)
pm10010mrAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostTxAlignment.setStatus("current")
_Pm10010mrAlmHostTxOtnStatus_Type = EkiOnOff
_Pm10010mrAlmHostTxOtnStatus_Object = MibScalar
pm10010mrAlmHostTxOtnStatus = _Pm10010mrAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 51, 16),
    _Pm10010mrAlmHostTxOtnStatus_Type()
)
pm10010mrAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostTxOtnStatus.setStatus("current")
_Pm10010mrAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaHostTxAlignment = _Pm10010mrAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 52)
)
_Pm10010mrAlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm10010mrAlmHostTxDeskewLockFault_Object = MibScalar
pm10010mrAlmHostTxDeskewLockFault = _Pm10010mrAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 52, 13),
    _Pm10010mrAlmHostTxDeskewLockFault_Type()
)
pm10010mrAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostTxDeskewLockFault.setStatus("current")
_Pm10010mrAlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm10010mrAlmHostTxOutOfAlignment_Object = MibScalar
pm10010mrAlmHostTxOutOfAlignment = _Pm10010mrAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 52, 14),
    _Pm10010mrAlmHostTxOutOfAlignment_Type()
)
pm10010mrAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostTxOutOfAlignment.setStatus("current")
_Pm10010mrAlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm10010mrAlmHostTxLossOfAlignment_Object = MibScalar
pm10010mrAlmHostTxLossOfAlignment = _Pm10010mrAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 52, 15),
    _Pm10010mrAlmHostTxLossOfAlignment_Type()
)
pm10010mrAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostTxLossOfAlignment.setStatus("current")
_Pm10010mrAlmHostTxCdrLockFault_Type = EkiOnOff
_Pm10010mrAlmHostTxCdrLockFault_Object = MibScalar
pm10010mrAlmHostTxCdrLockFault = _Pm10010mrAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 52, 16),
    _Pm10010mrAlmHostTxCdrLockFault_Type()
)
pm10010mrAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostTxCdrLockFault.setStatus("current")
_Pm10010mrAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm10010mrAlmmsaHostRxAlignment = _Pm10010mrAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 53)
)
_Pm10010mrAlmHostRxCmuLockFault_Type = EkiOnOff
_Pm10010mrAlmHostRxCmuLockFault_Object = MibScalar
pm10010mrAlmHostRxCmuLockFault = _Pm10010mrAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 53, 14),
    _Pm10010mrAlmHostRxCmuLockFault_Type()
)
pm10010mrAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostRxCmuLockFault.setStatus("current")
_Pm10010mrAlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm10010mrAlmHostRxOutOfAlignment_Object = MibScalar
pm10010mrAlmHostRxOutOfAlignment = _Pm10010mrAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 53, 15),
    _Pm10010mrAlmHostRxOutOfAlignment_Type()
)
pm10010mrAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostRxOutOfAlignment.setStatus("current")
_Pm10010mrAlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm10010mrAlmHostRxLossOfAlignment_Object = MibScalar
pm10010mrAlmHostRxLossOfAlignment = _Pm10010mrAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 1, 3, 53, 16),
    _Pm10010mrAlmHostRxLossOfAlignment_Type()
)
pm10010mrAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHostRxLossOfAlignment.setStatus("current")
_Pm10010mrAlmClient_ObjectIdentity = ObjectIdentity
pm10010mrAlmClient = _Pm10010mrAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2)
)
_Pm10010mrAlmClientNurg_ObjectIdentity = ObjectIdentity
pm10010mrAlmClientNurg = _Pm10010mrAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1)
)
_Pm10010mrAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pm10010mrAlmclientNetworkLaneAlarmWarningTable = _Pm10010mrAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pm10010mrAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pm10010mrAlmclientNetworkLaneAlarmWarningEntry = _Pm10010mrAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1)
)
pm10010mrAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pm10010mrAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pm10010mrAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pm10010mrAlmclientNetworkLaneAlarmWarningIndex = _Pm10010mrAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 1),
    _Pm10010mrAlmclientNetworkLaneAlarmWarningIndex_Type()
)
pm10010mrAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pm10010mrAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientRxPowerLowAlarmPortn = _Pm10010mrAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 2),
    _Pm10010mrAlmClientRxPowerLowAlarmPortn_Type()
)
pm10010mrAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pm10010mrAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pm10010mrAlmClientRxPowerLowWarningPortn = _Pm10010mrAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 3),
    _Pm10010mrAlmClientRxPowerLowWarningPortn_Type()
)
pm10010mrAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientRxPowerLowWarningPortn.setStatus("current")
_Pm10010mrAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pm10010mrAlmClientRxPowerHighWarningPortn = _Pm10010mrAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 4),
    _Pm10010mrAlmClientRxPowerHighWarningPortn_Type()
)
pm10010mrAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientRxPowerHighWarningPortn.setStatus("current")
_Pm10010mrAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientRxPowerHighAlarmPortn = _Pm10010mrAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 5),
    _Pm10010mrAlmClientRxPowerHighAlarmPortn_Type()
)
pm10010mrAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pm10010mrAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmLaserTempLowAlarmPortn = _Pm10010mrAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 6),
    _Pm10010mrAlmLaserTempLowAlarmPortn_Type()
)
pm10010mrAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mrAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mrAlmClientLaserTempLowWarningPortn = _Pm10010mrAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 7),
    _Pm10010mrAlmClientLaserTempLowWarningPortn_Type()
)
pm10010mrAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaserTempLowWarningPortn.setStatus("current")
_Pm10010mrAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mrAlmClientLaserTempHighWarningPortn = _Pm10010mrAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 8),
    _Pm10010mrAlmClientLaserTempHighWarningPortn_Type()
)
pm10010mrAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaserTempHighWarningPortn.setStatus("current")
_Pm10010mrAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientLaserTempHighAlarmPortn = _Pm10010mrAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 9),
    _Pm10010mrAlmClientLaserTempHighAlarmPortn_Type()
)
pm10010mrAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mrAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientTxPowerLowAlarmPortn = _Pm10010mrAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 10),
    _Pm10010mrAlmClientTxPowerLowAlarmPortn_Type()
)
pm10010mrAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pm10010mrAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pm10010mrAlmClientTxPowerLowWarningPortn = _Pm10010mrAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 11),
    _Pm10010mrAlmClientTxPowerLowWarningPortn_Type()
)
pm10010mrAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientTxPowerLowWarningPortn.setStatus("current")
_Pm10010mrAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pm10010mrAlmClientTxPowerHighWarningPortn = _Pm10010mrAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 12),
    _Pm10010mrAlmClientTxPowerHighWarningPortn_Type()
)
pm10010mrAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientTxPowerHighWarningPortn.setStatus("current")
_Pm10010mrAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientTxPowerHighAlarmPortn = _Pm10010mrAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 13),
    _Pm10010mrAlmClientTxPowerHighAlarmPortn_Type()
)
pm10010mrAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pm10010mrAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientBiasLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientBiasLowAlarmPortn = _Pm10010mrAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 14),
    _Pm10010mrAlmClientBiasLowAlarmPortn_Type()
)
pm10010mrAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientBiasLowAlarmPortn.setStatus("current")
_Pm10010mrAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientBiasLowWarningPortn_Object = MibTableColumn
pm10010mrAlmClientBiasLowWarningPortn = _Pm10010mrAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 15),
    _Pm10010mrAlmClientBiasLowWarningPortn_Type()
)
pm10010mrAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientBiasLowWarningPortn.setStatus("current")
_Pm10010mrAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmClientBiasHighWarningPortn_Object = MibTableColumn
pm10010mrAlmClientBiasHighWarningPortn = _Pm10010mrAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 16),
    _Pm10010mrAlmClientBiasHighWarningPortn_Type()
)
pm10010mrAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientBiasHighWarningPortn.setStatus("current")
_Pm10010mrAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmClientBiasHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmClientBiasHighAlarmPortn = _Pm10010mrAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 56, 1, 17),
    _Pm10010mrAlmClientBiasHighAlarmPortn_Type()
)
pm10010mrAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientBiasHighAlarmPortn.setStatus("current")
_Pm10010mrAlmclientSfpWarnDdmTable_Object = MibTable
pm10010mrAlmclientSfpWarnDdmTable = _Pm10010mrAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientSfpWarnDdmTable.setStatus("current")
_Pm10010mrAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm10010mrAlmclientSfpWarnDdmEntry = _Pm10010mrAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1)
)
pm10010mrAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm10010mrAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm10010mrAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm10010mrAlmclientSfpWarnDdmIndex = _Pm10010mrAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 1),
    _Pm10010mrAlmclientSfpWarnDdmIndex_Type()
)
pm10010mrAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm10010mrAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm10010mrAlmTxPwLowWngPortn_Object = MibTableColumn
pm10010mrAlmTxPwLowWngPortn = _Pm10010mrAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 2),
    _Pm10010mrAlmTxPwLowWngPortn_Type()
)
pm10010mrAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxPwLowWngPortn.setStatus("current")
_Pm10010mrAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm10010mrAlmTxPwrHighWngPortn_Object = MibTableColumn
pm10010mrAlmTxPwrHighWngPortn = _Pm10010mrAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 3),
    _Pm10010mrAlmTxPwrHighWngPortn_Type()
)
pm10010mrAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxPwrHighWngPortn.setStatus("current")
_Pm10010mrAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm10010mrAlmTxBiasLowWngPortn_Object = MibTableColumn
pm10010mrAlmTxBiasLowWngPortn = _Pm10010mrAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 4),
    _Pm10010mrAlmTxBiasLowWngPortn_Type()
)
pm10010mrAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxBiasLowWngPortn.setStatus("current")
_Pm10010mrAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm10010mrAlmTxBiasHighWngPortn_Object = MibTableColumn
pm10010mrAlmTxBiasHighWngPortn = _Pm10010mrAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 5),
    _Pm10010mrAlmTxBiasHighWngPortn_Type()
)
pm10010mrAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxBiasHighWngPortn.setStatus("current")
_Pm10010mrAlmVccLowWngPortn_Type = EkiOnOff
_Pm10010mrAlmVccLowWngPortn_Object = MibTableColumn
pm10010mrAlmVccLowWngPortn = _Pm10010mrAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 6),
    _Pm10010mrAlmVccLowWngPortn_Type()
)
pm10010mrAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmVccLowWngPortn.setStatus("current")
_Pm10010mrAlmVccHighWngPortn_Type = EkiOnOff
_Pm10010mrAlmVccHighWngPortn_Object = MibTableColumn
pm10010mrAlmVccHighWngPortn = _Pm10010mrAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 7),
    _Pm10010mrAlmVccHighWngPortn_Type()
)
pm10010mrAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmVccHighWngPortn.setStatus("current")
_Pm10010mrAlmTempLowWngPortn_Type = EkiOnOff
_Pm10010mrAlmTempLowWngPortn_Object = MibTableColumn
pm10010mrAlmTempLowWngPortn = _Pm10010mrAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 8),
    _Pm10010mrAlmTempLowWngPortn_Type()
)
pm10010mrAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTempLowWngPortn.setStatus("current")
_Pm10010mrAlmTempHighWngPortn_Type = EkiOnOff
_Pm10010mrAlmTempHighWngPortn_Object = MibTableColumn
pm10010mrAlmTempHighWngPortn = _Pm10010mrAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 9),
    _Pm10010mrAlmTempHighWngPortn_Type()
)
pm10010mrAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTempHighWngPortn.setStatus("current")
_Pm10010mrAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm10010mrAlmRxPwrLowWngPortn_Object = MibTableColumn
pm10010mrAlmRxPwrLowWngPortn = _Pm10010mrAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 16),
    _Pm10010mrAlmRxPwrLowWngPortn_Type()
)
pm10010mrAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxPwrLowWngPortn.setStatus("current")
_Pm10010mrAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm10010mrAlmRxPwrHighWngPortn_Object = MibTableColumn
pm10010mrAlmRxPwrHighWngPortn = _Pm10010mrAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 1, 232, 1, 17),
    _Pm10010mrAlmRxPwrHighWngPortn_Type()
)
pm10010mrAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxPwrHighWngPortn.setStatus("current")
_Pm10010mrAlmClientUrg_ObjectIdentity = ObjectIdentity
pm10010mrAlmClientUrg = _Pm10010mrAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2)
)
_Pm10010mrAlmclientNetworkLaneFaultTable_Object = MibTable
pm10010mrAlmclientNetworkLaneFaultTable = _Pm10010mrAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientNetworkLaneFaultTable.setStatus("current")
_Pm10010mrAlmclientNetworkLaneFaultEntry_Object = MibTableRow
pm10010mrAlmclientNetworkLaneFaultEntry = _Pm10010mrAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1)
)
pm10010mrAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pm10010mrAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mrAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pm10010mrAlmclientNetworkLaneFaultIndex = _Pm10010mrAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 1),
    _Pm10010mrAlmclientNetworkLaneFaultIndex_Type()
)
pm10010mrAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmclientNetworkLaneFaultIndex.setStatus("current")
_Pm10010mrAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010mrAlmClientLaneRxFifoErrorPortn = _Pm10010mrAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 4),
    _Pm10010mrAlmClientLaneRxFifoErrorPortn_Type()
)
pm10010mrAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pm10010mrAlmClientLaneRxLolPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneRxLolPortn_Object = MibTableColumn
pm10010mrAlmClientLaneRxLolPortn = _Pm10010mrAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 5),
    _Pm10010mrAlmClientLaneRxLolPortn_Type()
)
pm10010mrAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneRxLolPortn.setStatus("current")
_Pm10010mrAlmClientLaneRxLosPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneRxLosPortn_Object = MibTableColumn
pm10010mrAlmClientLaneRxLosPortn = _Pm10010mrAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 6),
    _Pm10010mrAlmClientLaneRxLosPortn_Type()
)
pm10010mrAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneRxLosPortn.setStatus("current")
_Pm10010mrAlmClientLaneTxLolPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneTxLolPortn_Object = MibTableColumn
pm10010mrAlmClientLaneTxLolPortn = _Pm10010mrAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 8),
    _Pm10010mrAlmClientLaneTxLolPortn_Type()
)
pm10010mrAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneTxLolPortn.setStatus("current")
_Pm10010mrAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneTxLosfPortn_Object = MibTableColumn
pm10010mrAlmClientLaneTxLosfPortn = _Pm10010mrAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 9),
    _Pm10010mrAlmClientLaneTxLosfPortn_Type()
)
pm10010mrAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneTxLosfPortn.setStatus("current")
_Pm10010mrAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010mrAlmClientLaneApdPowerSupplyPortn = _Pm10010mrAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 15),
    _Pm10010mrAlmClientLaneApdPowerSupplyPortn_Type()
)
pm10010mrAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010mrAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010mrAlmClientLaneWavelengthUnlockedPortn = _Pm10010mrAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 16),
    _Pm10010mrAlmClientLaneWavelengthUnlockedPortn_Type()
)
pm10010mrAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010mrAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneTecFaultPortn_Object = MibTableColumn
pm10010mrAlmClientLaneTecFaultPortn = _Pm10010mrAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 72, 1, 17),
    _Pm10010mrAlmClientLaneTecFaultPortn_Type()
)
pm10010mrAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneTecFaultPortn.setStatus("current")
_Pm10010mrAlmclientHostLaneFaultTable_Object = MibTable
pm10010mrAlmclientHostLaneFaultTable = _Pm10010mrAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientHostLaneFaultTable.setStatus("current")
_Pm10010mrAlmclientHostLaneFaultEntry_Object = MibTableRow
pm10010mrAlmclientHostLaneFaultEntry = _Pm10010mrAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1)
)
pm10010mrAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientHostLaneFaultEntry.setStatus("current")


class _Pm10010mrAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mrAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmclientHostLaneFaultIndex_Object = MibTableColumn
pm10010mrAlmclientHostLaneFaultIndex = _Pm10010mrAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 1),
    _Pm10010mrAlmclientHostLaneFaultIndex_Type()
)
pm10010mrAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmclientHostLaneFaultIndex.setStatus("current")
_Pm10010mrAlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm10010mrAlmClientLossOfSyncPortn_Object = MibTableColumn
pm10010mrAlmClientLossOfSyncPortn = _Pm10010mrAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 2),
    _Pm10010mrAlmClientLossOfSyncPortn_Type()
)
pm10010mrAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLossOfSyncPortn.setStatus("current")
_Pm10010mrAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm10010mrAlmClientInputLossOfSigPortn_Object = MibTableColumn
pm10010mrAlmClientInputLossOfSigPortn = _Pm10010mrAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 3),
    _Pm10010mrAlmClientInputLossOfSigPortn_Type()
)
pm10010mrAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientInputLossOfSigPortn.setStatus("current")
_Pm10010mrAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm10010mrAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm10010mrAlmClientLanesMarkerUnlockPortn = _Pm10010mrAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 4),
    _Pm10010mrAlmClientLanesMarkerUnlockPortn_Type()
)
pm10010mrAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm10010mrAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm10010mrAlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm10010mrAlmClientLanes6466UnlockPortn = _Pm10010mrAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 5),
    _Pm10010mrAlmClientLanes6466UnlockPortn_Type()
)
pm10010mrAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLanes6466UnlockPortn.setStatus("current")
_Pm10010mrAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm10010mrAlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm10010mrAlmClientLanesNotAlignedPortn = _Pm10010mrAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 6),
    _Pm10010mrAlmClientLanesNotAlignedPortn_Type()
)
pm10010mrAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLanesNotAlignedPortn.setStatus("current")
_Pm10010mrAlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm10010mrAlmClientCsfDetectedPortn_Object = MibTableColumn
pm10010mrAlmClientCsfDetectedPortn = _Pm10010mrAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 7),
    _Pm10010mrAlmClientCsfDetectedPortn_Type()
)
pm10010mrAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientCsfDetectedPortn.setStatus("current")
_Pm10010mrAlmClientTxHostLolPortn_Type = EkiOnOff
_Pm10010mrAlmClientTxHostLolPortn_Object = MibTableColumn
pm10010mrAlmClientTxHostLolPortn = _Pm10010mrAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 10),
    _Pm10010mrAlmClientTxHostLolPortn_Type()
)
pm10010mrAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientTxHostLolPortn.setStatus("current")
_Pm10010mrAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010mrAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010mrAlmClientLaneTxFifoErrorPortn = _Pm10010mrAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 11),
    _Pm10010mrAlmClientLaneTxFifoErrorPortn_Type()
)
pm10010mrAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm10010mrAlmLfDetectedPortn_Type = EkiOnOff
_Pm10010mrAlmLfDetectedPortn_Object = MibTableColumn
pm10010mrAlmLfDetectedPortn = _Pm10010mrAlmLfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 12),
    _Pm10010mrAlmLfDetectedPortn_Type()
)
pm10010mrAlmLfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLfDetectedPortn.setStatus("current")
_Pm10010mrAlmRfDetectedPortn_Type = EkiOnOff
_Pm10010mrAlmRfDetectedPortn_Object = MibTableColumn
pm10010mrAlmRfDetectedPortn = _Pm10010mrAlmRfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 88, 1, 13),
    _Pm10010mrAlmRfDetectedPortn_Type()
)
pm10010mrAlmRfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRfDetectedPortn.setStatus("current")
_Pm10010mrAlmclientSfpAlmDdmTable_Object = MibTable
pm10010mrAlmclientSfpAlmDdmTable = _Pm10010mrAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientSfpAlmDdmTable.setStatus("current")
_Pm10010mrAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm10010mrAlmclientSfpAlmDdmEntry = _Pm10010mrAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1)
)
pm10010mrAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm10010mrAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm10010mrAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm10010mrAlmclientSfpAlmDdmIndex = _Pm10010mrAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 1),
    _Pm10010mrAlmclientSfpAlmDdmIndex_Type()
)
pm10010mrAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm10010mrAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010mrAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm10010mrAlmTxPwrLowAlaPortn = _Pm10010mrAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 2),
    _Pm10010mrAlmTxPwrLowAlaPortn_Type()
)
pm10010mrAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxPwrLowAlaPortn.setStatus("current")
_Pm10010mrAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010mrAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm10010mrAlmTxPwrHighAlaPortn = _Pm10010mrAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 3),
    _Pm10010mrAlmTxPwrHighAlaPortn_Type()
)
pm10010mrAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxPwrHighAlaPortn.setStatus("current")
_Pm10010mrAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm10010mrAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm10010mrAlmTxBiasLowAlaPortn = _Pm10010mrAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 4),
    _Pm10010mrAlmTxBiasLowAlaPortn_Type()
)
pm10010mrAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxBiasLowAlaPortn.setStatus("current")
_Pm10010mrAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm10010mrAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm10010mrAlmTxBiasHighAlaPortn = _Pm10010mrAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 5),
    _Pm10010mrAlmTxBiasHighAlaPortn_Type()
)
pm10010mrAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxBiasHighAlaPortn.setStatus("current")
_Pm10010mrAlmVccLowAlaPortn_Type = EkiOnOff
_Pm10010mrAlmVccLowAlaPortn_Object = MibTableColumn
pm10010mrAlmVccLowAlaPortn = _Pm10010mrAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 6),
    _Pm10010mrAlmVccLowAlaPortn_Type()
)
pm10010mrAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmVccLowAlaPortn.setStatus("current")
_Pm10010mrAlmVccHighAlaPortn_Type = EkiOnOff
_Pm10010mrAlmVccHighAlaPortn_Object = MibTableColumn
pm10010mrAlmVccHighAlaPortn = _Pm10010mrAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 7),
    _Pm10010mrAlmVccHighAlaPortn_Type()
)
pm10010mrAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmVccHighAlaPortn.setStatus("current")
_Pm10010mrAlmTempLowAlaPortn_Type = EkiOnOff
_Pm10010mrAlmTempLowAlaPortn_Object = MibTableColumn
pm10010mrAlmTempLowAlaPortn = _Pm10010mrAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 8),
    _Pm10010mrAlmTempLowAlaPortn_Type()
)
pm10010mrAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTempLowAlaPortn.setStatus("current")
_Pm10010mrAlmTempHighAlaPortn_Type = EkiOnOff
_Pm10010mrAlmTempHighAlaPortn_Object = MibTableColumn
pm10010mrAlmTempHighAlaPortn = _Pm10010mrAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 9),
    _Pm10010mrAlmTempHighAlaPortn_Type()
)
pm10010mrAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTempHighAlaPortn.setStatus("current")
_Pm10010mrAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010mrAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm10010mrAlmRxPwrLowAlaPortn = _Pm10010mrAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 16),
    _Pm10010mrAlmRxPwrLowAlaPortn_Type()
)
pm10010mrAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxPwrLowAlaPortn.setStatus("current")
_Pm10010mrAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010mrAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm10010mrAlmRxPwrHighAlaPortn = _Pm10010mrAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 2, 216, 1, 17),
    _Pm10010mrAlmRxPwrHighAlaPortn_Type()
)
pm10010mrAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxPwrHighAlaPortn.setStatus("current")
_Pm10010mrAlmClientCrit_ObjectIdentity = ObjectIdentity
pm10010mrAlmClientCrit = _Pm10010mrAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3)
)
_Pm10010mrAlmsynthAlmPortTable_Object = MibTable
pm10010mrAlmsynthAlmPortTable = _Pm10010mrAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm10010mrAlmsynthAlmPortTable.setStatus("current")
_Pm10010mrAlmsynthAlmPortEntry_Object = MibTableRow
pm10010mrAlmsynthAlmPortEntry = _Pm10010mrAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1)
)
pm10010mrAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmsynthAlmPortEntry.setStatus("current")


class _Pm10010mrAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm10010mrAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmsynthAlmPortIndex_Object = MibTableColumn
pm10010mrAlmsynthAlmPortIndex = _Pm10010mrAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 1),
    _Pm10010mrAlmsynthAlmPortIndex_Type()
)
pm10010mrAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmsynthAlmPortIndex.setStatus("current")
_Pm10010mrAlmSfpAbsentPortn_Type = EkiOnOff
_Pm10010mrAlmSfpAbsentPortn_Object = MibTableColumn
pm10010mrAlmSfpAbsentPortn = _Pm10010mrAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 2),
    _Pm10010mrAlmSfpAbsentPortn_Type()
)
pm10010mrAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmSfpAbsentPortn.setStatus("current")
_Pm10010mrAlmDdmAbsentPortn_Type = EkiOnOff
_Pm10010mrAlmDdmAbsentPortn_Object = MibTableColumn
pm10010mrAlmDdmAbsentPortn = _Pm10010mrAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 3),
    _Pm10010mrAlmDdmAbsentPortn_Type()
)
pm10010mrAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmDdmAbsentPortn.setStatus("current")
_Pm10010mrAlmHwFailAccPortn_Type = EkiOnOff
_Pm10010mrAlmHwFailAccPortn_Object = MibTableColumn
pm10010mrAlmHwFailAccPortn = _Pm10010mrAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 5),
    _Pm10010mrAlmHwFailAccPortn_Type()
)
pm10010mrAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmHwFailAccPortn.setStatus("current")
_Pm10010mrAlmDwLsdPortn_Type = EkiOnOff
_Pm10010mrAlmDwLsdPortn_Object = MibTableColumn
pm10010mrAlmDwLsdPortn = _Pm10010mrAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 6),
    _Pm10010mrAlmDwLsdPortn_Type()
)
pm10010mrAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmDwLsdPortn.setStatus("current")
_Pm10010mrAlmClientLocalOosPortn_Type = EkiOnOff
_Pm10010mrAlmClientLocalOosPortn_Object = MibTableColumn
pm10010mrAlmClientLocalOosPortn = _Pm10010mrAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 7),
    _Pm10010mrAlmClientLocalOosPortn_Type()
)
pm10010mrAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientLocalOosPortn.setStatus("current")
_Pm10010mrAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm10010mrAlmClientRemoteOosPortn_Object = MibTableColumn
pm10010mrAlmClientRemoteOosPortn = _Pm10010mrAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 8),
    _Pm10010mrAlmClientRemoteOosPortn_Type()
)
pm10010mrAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmClientRemoteOosPortn.setStatus("current")
_Pm10010mrAlmDwCaisPortn_Type = EkiOnOff
_Pm10010mrAlmDwCaisPortn_Object = MibTableColumn
pm10010mrAlmDwCaisPortn = _Pm10010mrAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 9),
    _Pm10010mrAlmDwCaisPortn_Type()
)
pm10010mrAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmDwCaisPortn.setStatus("current")
_Pm10010mrAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm10010mrAlmSfpDdmWarningPortn_Object = MibTableColumn
pm10010mrAlmSfpDdmWarningPortn = _Pm10010mrAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 10),
    _Pm10010mrAlmSfpDdmWarningPortn_Type()
)
pm10010mrAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmSfpDdmWarningPortn.setStatus("current")
_Pm10010mrAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm10010mrAlmSfpDdmAlmPortn_Object = MibTableColumn
pm10010mrAlmSfpDdmAlmPortn = _Pm10010mrAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 11),
    _Pm10010mrAlmSfpDdmAlmPortn_Type()
)
pm10010mrAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmSfpDdmAlmPortn.setStatus("current")
_Pm10010mrAlmIdleInsertedPortn_Type = EkiOnOff
_Pm10010mrAlmIdleInsertedPortn_Object = MibTableColumn
pm10010mrAlmIdleInsertedPortn = _Pm10010mrAlmIdleInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 12),
    _Pm10010mrAlmIdleInsertedPortn_Type()
)
pm10010mrAlmIdleInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmIdleInsertedPortn.setStatus("current")
_Pm10010mrAlmFailAccPortn_Type = EkiOnOff
_Pm10010mrAlmFailAccPortn_Object = MibTableColumn
pm10010mrAlmFailAccPortn = _Pm10010mrAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 13),
    _Pm10010mrAlmFailAccPortn_Type()
)
pm10010mrAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmFailAccPortn.setStatus("current")
_Pm10010mrAlmUpCsfPortn_Type = EkiOnOff
_Pm10010mrAlmUpCsfPortn_Object = MibTableColumn
pm10010mrAlmUpCsfPortn = _Pm10010mrAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 2, 3, 8, 1, 17),
    _Pm10010mrAlmUpCsfPortn_Type()
)
pm10010mrAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmUpCsfPortn.setStatus("current")
_Pm10010mrAlmLine_ObjectIdentity = ObjectIdentity
pm10010mrAlmLine = _Pm10010mrAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3)
)
_Pm10010mrAlmLineNurg_ObjectIdentity = ObjectIdentity
pm10010mrAlmLineNurg = _Pm10010mrAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1)
)
_Pm10010mrAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm10010mrAlmlineNetworkLaneAlarmWarning1Table = _Pm10010mrAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm10010mrAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm10010mrAlmlineNetworkLaneAlarmWarning1Entry = _Pm10010mrAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1)
)
pm10010mrAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm10010mrAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm10010mrAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm10010mrAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm10010mrAlmlineNetworkLaneAlarmWarning1Index = _Pm10010mrAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 1),
    _Pm10010mrAlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm10010mrAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm10010mrAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineRxPowerLowAlarmPortn = _Pm10010mrAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 2),
    _Pm10010mrAlmLineRxPowerLowAlarmPortn_Type()
)
pm10010mrAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm10010mrAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm10010mrAlmLineRxPowerLowWarningPortn = _Pm10010mrAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 3),
    _Pm10010mrAlmLineRxPowerLowWarningPortn_Type()
)
pm10010mrAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm10010mrAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm10010mrAlmLineRxPowerHighWarningPortn = _Pm10010mrAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 4),
    _Pm10010mrAlmLineRxPowerHighWarningPortn_Type()
)
pm10010mrAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm10010mrAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineRxPowerHighAlarmPortn = _Pm10010mrAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 5),
    _Pm10010mrAlmLineRxPowerHighAlarmPortn_Type()
)
pm10010mrAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm10010mrAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineLaserTempLowAlarmPortn = _Pm10010mrAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 6),
    _Pm10010mrAlmLineLaserTempLowAlarmPortn_Type()
)
pm10010mrAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mrAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mrAlmLineLaserTempLowWarningPortn = _Pm10010mrAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 7),
    _Pm10010mrAlmLineLaserTempLowWarningPortn_Type()
)
pm10010mrAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm10010mrAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mrAlmLineLaserTempHighWarningPortn = _Pm10010mrAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 8),
    _Pm10010mrAlmLineLaserTempHighWarningPortn_Type()
)
pm10010mrAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm10010mrAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineLaserTempHighAlarmPortn = _Pm10010mrAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 9),
    _Pm10010mrAlmLineLaserTempHighAlarmPortn_Type()
)
pm10010mrAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mrAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineTxPowerLowAlarmPortn = _Pm10010mrAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 10),
    _Pm10010mrAlmLineTxPowerLowAlarmPortn_Type()
)
pm10010mrAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm10010mrAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm10010mrAlmLineTxPowerLowWarningPortn = _Pm10010mrAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 11),
    _Pm10010mrAlmLineTxPowerLowWarningPortn_Type()
)
pm10010mrAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm10010mrAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm10010mrAlmLineTxPowerHighWarningPortn = _Pm10010mrAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 12),
    _Pm10010mrAlmLineTxPowerHighWarningPortn_Type()
)
pm10010mrAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm10010mrAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineTxPowerHighAlarmPortn = _Pm10010mrAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 13),
    _Pm10010mrAlmLineTxPowerHighAlarmPortn_Type()
)
pm10010mrAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm10010mrAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineBiasLowAlarmPortn = _Pm10010mrAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 14),
    _Pm10010mrAlmLineBiasLowAlarmPortn_Type()
)
pm10010mrAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineBiasLowAlarmPortn.setStatus("current")
_Pm10010mrAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineBiasLowWarningPortn_Object = MibTableColumn
pm10010mrAlmLineBiasLowWarningPortn = _Pm10010mrAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 15),
    _Pm10010mrAlmLineBiasLowWarningPortn_Type()
)
pm10010mrAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineBiasLowWarningPortn.setStatus("current")
_Pm10010mrAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineBiasHighWarningPortn_Object = MibTableColumn
pm10010mrAlmLineBiasHighWarningPortn = _Pm10010mrAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 16),
    _Pm10010mrAlmLineBiasHighWarningPortn_Type()
)
pm10010mrAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineBiasHighWarningPortn.setStatus("current")
_Pm10010mrAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmLineBiasHighAlarmPortn = _Pm10010mrAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 104, 1, 17),
    _Pm10010mrAlmLineBiasHighAlarmPortn_Type()
)
pm10010mrAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineBiasHighAlarmPortn.setStatus("current")
_Pm10010mrAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm10010mrAlmlineNetworkLaneAlarmWarning2Table = _Pm10010mrAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm10010mrAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm10010mrAlmlineNetworkLaneAlarmWarning2Entry = _Pm10010mrAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1)
)
pm10010mrAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm10010mrAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm10010mrAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm10010mrAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm10010mrAlmlineNetworkLaneAlarmWarning2Index = _Pm10010mrAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 1),
    _Pm10010mrAlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm10010mrAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm10010mrAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmTxModulatorBiasLowAlarmPortn = _Pm10010mrAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 2),
    _Pm10010mrAlmTxModulatorBiasLowAlarmPortn_Type()
)
pm10010mrAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm10010mrAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm10010mrAlmTxModulatorBiasLowWarningPortn = _Pm10010mrAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 3),
    _Pm10010mrAlmTxModulatorBiasLowWarningPortn_Type()
)
pm10010mrAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm10010mrAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm10010mrAlmTxModulatorBiasHighWarningPortn = _Pm10010mrAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 4),
    _Pm10010mrAlmTxModulatorBiasHighWarningPortn_Type()
)
pm10010mrAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm10010mrAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmTxModulatorBiasHighAlarmPortn = _Pm10010mrAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 5),
    _Pm10010mrAlmTxModulatorBiasHighAlarmPortn_Type()
)
pm10010mrAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm10010mrAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmRxLaserTempLowAlarmPortn = _Pm10010mrAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 6),
    _Pm10010mrAlmRxLaserTempLowAlarmPortn_Type()
)
pm10010mrAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mrAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mrAlmRxLaserTempLowWarningPortn = _Pm10010mrAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 7),
    _Pm10010mrAlmRxLaserTempLowWarningPortn_Type()
)
pm10010mrAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm10010mrAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mrAlmRxLaserTempHighWarningPortn = _Pm10010mrAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 8),
    _Pm10010mrAlmRxLaserTempHighWarningPortn_Type()
)
pm10010mrAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm10010mrAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmRxLaserTempHighAlarmPortn = _Pm10010mrAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 9),
    _Pm10010mrAlmRxLaserTempHighAlarmPortn_Type()
)
pm10010mrAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mrAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmRxLaserOutputLowAlarmPortn = _Pm10010mrAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 10),
    _Pm10010mrAlmRxLaserOutputLowAlarmPortn_Type()
)
pm10010mrAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm10010mrAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm10010mrAlmRxLaserOutputLowWarningPortn = _Pm10010mrAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 11),
    _Pm10010mrAlmRxLaserOutputLowWarningPortn_Type()
)
pm10010mrAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm10010mrAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm10010mrAlmRxLaserOutputHighWarningPortn = _Pm10010mrAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 12),
    _Pm10010mrAlmRxLaserOutputHighWarningPortn_Type()
)
pm10010mrAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm10010mrAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmRxLaserOutputHighAlarmPortn = _Pm10010mrAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 13),
    _Pm10010mrAlmRxLaserOutputHighAlarmPortn_Type()
)
pm10010mrAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm10010mrAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm10010mrAlmRxLaserBiasLowAlarmPortn = _Pm10010mrAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 14),
    _Pm10010mrAlmRxLaserBiasLowAlarmPortn_Type()
)
pm10010mrAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm10010mrAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm10010mrAlmRxLaserBiasLowWarningPortn = _Pm10010mrAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 15),
    _Pm10010mrAlmRxLaserBiasLowWarningPortn_Type()
)
pm10010mrAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm10010mrAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm10010mrAlmRxLaserBiasHighWarningPortn = _Pm10010mrAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 16),
    _Pm10010mrAlmRxLaserBiasHighWarningPortn_Type()
)
pm10010mrAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm10010mrAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mrAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm10010mrAlmRxLaserBiasHighAlarmPortn = _Pm10010mrAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 1, 120, 1, 17),
    _Pm10010mrAlmRxLaserBiasHighAlarmPortn_Type()
)
pm10010mrAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm10010mrAlmLineUrg_ObjectIdentity = ObjectIdentity
pm10010mrAlmLineUrg = _Pm10010mrAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2)
)
_Pm10010mrAlmlineNetworkLaneFaultTable_Object = MibTable
pm10010mrAlmlineNetworkLaneFaultTable = _Pm10010mrAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneFaultTable.setStatus("current")
_Pm10010mrAlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm10010mrAlmlineNetworkLaneFaultEntry = _Pm10010mrAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1)
)
pm10010mrAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm10010mrAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mrAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm10010mrAlmlineNetworkLaneFaultIndex = _Pm10010mrAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 1),
    _Pm10010mrAlmlineNetworkLaneFaultIndex_Type()
)
pm10010mrAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm10010mrAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm10010mrAlmLineLaneRxTecFaultPortn = _Pm10010mrAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 3),
    _Pm10010mrAlmLineLaneRxTecFaultPortn_Type()
)
pm10010mrAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm10010mrAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010mrAlmLineLaneRxFifoErrorPortn = _Pm10010mrAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 4),
    _Pm10010mrAlmLineLaneRxFifoErrorPortn_Type()
)
pm10010mrAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm10010mrAlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneRxLolPortn_Object = MibTableColumn
pm10010mrAlmLineLaneRxLolPortn = _Pm10010mrAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 5),
    _Pm10010mrAlmLineLaneRxLolPortn_Type()
)
pm10010mrAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneRxLolPortn.setStatus("current")
_Pm10010mrAlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneRxLosPortn_Object = MibTableColumn
pm10010mrAlmLineLaneRxLosPortn = _Pm10010mrAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 6),
    _Pm10010mrAlmLineLaneRxLosPortn_Type()
)
pm10010mrAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneRxLosPortn.setStatus("current")
_Pm10010mrAlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneTxLolPortn_Object = MibTableColumn
pm10010mrAlmLineLaneTxLolPortn = _Pm10010mrAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 8),
    _Pm10010mrAlmLineLaneTxLolPortn_Type()
)
pm10010mrAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneTxLolPortn.setStatus("current")
_Pm10010mrAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneTxLosfPortn_Object = MibTableColumn
pm10010mrAlmLineLaneTxLosfPortn = _Pm10010mrAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 9),
    _Pm10010mrAlmLineLaneTxLosfPortn_Type()
)
pm10010mrAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneTxLosfPortn.setStatus("current")
_Pm10010mrAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010mrAlmLineLaneApdPowerSupplyPortn = _Pm10010mrAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 15),
    _Pm10010mrAlmLineLaneApdPowerSupplyPortn_Type()
)
pm10010mrAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010mrAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010mrAlmLineLaneWavelengthUnlockedPortn = _Pm10010mrAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 16),
    _Pm10010mrAlmLineLaneWavelengthUnlockedPortn_Type()
)
pm10010mrAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010mrAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneTecFaultPortn_Object = MibTableColumn
pm10010mrAlmLineLaneTecFaultPortn = _Pm10010mrAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 136, 1, 17),
    _Pm10010mrAlmLineLaneTecFaultPortn_Type()
)
pm10010mrAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneTecFaultPortn.setStatus("current")
_Pm10010mrAlmlineHostLaneFaultTable_Object = MibTable
pm10010mrAlmlineHostLaneFaultTable = _Pm10010mrAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineHostLaneFaultTable.setStatus("current")
_Pm10010mrAlmlineHostLaneFaultEntry_Object = MibTableRow
pm10010mrAlmlineHostLaneFaultEntry = _Pm10010mrAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1)
)
pm10010mrAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineHostLaneFaultEntry.setStatus("current")


class _Pm10010mrAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mrAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmlineHostLaneFaultIndex_Object = MibTableColumn
pm10010mrAlmlineHostLaneFaultIndex = _Pm10010mrAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 1),
    _Pm10010mrAlmlineHostLaneFaultIndex_Type()
)
pm10010mrAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmlineHostLaneFaultIndex.setStatus("current")
_Pm10010mrAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm10010mrAlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm10010mrAlmLineInputLossOfSignalPortn = _Pm10010mrAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 2),
    _Pm10010mrAlmLineInputLossOfSignalPortn_Type()
)
pm10010mrAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineInputLossOfSignalPortn.setStatus("current")
_Pm10010mrAlmLineLossOfFramePortn_Type = EkiOnOff
_Pm10010mrAlmLineLossOfFramePortn_Object = MibTableColumn
pm10010mrAlmLineLossOfFramePortn = _Pm10010mrAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 3),
    _Pm10010mrAlmLineLossOfFramePortn_Type()
)
pm10010mrAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLossOfFramePortn.setStatus("current")
_Pm10010mrAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm10010mrAlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm10010mrAlmLineSmBdiInsertedPortn = _Pm10010mrAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 4),
    _Pm10010mrAlmLineSmBdiInsertedPortn_Type()
)
pm10010mrAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineSmBdiInsertedPortn.setStatus("current")
_Pm10010mrAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm10010mrAlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm10010mrAlmLineSmBdiDetectedPortn = _Pm10010mrAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 5),
    _Pm10010mrAlmLineSmBdiDetectedPortn_Type()
)
pm10010mrAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineSmBdiDetectedPortn.setStatus("current")
_Pm10010mrAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm10010mrAlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm10010mrAlmLineSmIaeInsertedPortn = _Pm10010mrAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 6),
    _Pm10010mrAlmLineSmIaeInsertedPortn_Type()
)
pm10010mrAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineSmIaeInsertedPortn.setStatus("current")
_Pm10010mrAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm10010mrAlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm10010mrAlmLineSmIaeDetectedPortn = _Pm10010mrAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 7),
    _Pm10010mrAlmLineSmIaeDetectedPortn_Type()
)
pm10010mrAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineSmIaeDetectedPortn.setStatus("current")
_Pm10010mrAlmLineTxHostLolPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxHostLolPortn_Object = MibTableColumn
pm10010mrAlmLineTxHostLolPortn = _Pm10010mrAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 10),
    _Pm10010mrAlmLineTxHostLolPortn_Type()
)
pm10010mrAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxHostLolPortn.setStatus("current")
_Pm10010mrAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010mrAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010mrAlmLineLaneTxFifoErrorPortn = _Pm10010mrAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 11),
    _Pm10010mrAlmLineLaneTxFifoErrorPortn_Type()
)
pm10010mrAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm10010mrAlmLinePowerDegradePortn_Type = EkiOnOff
_Pm10010mrAlmLinePowerDegradePortn_Object = MibTableColumn
pm10010mrAlmLinePowerDegradePortn = _Pm10010mrAlmLinePowerDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 16),
    _Pm10010mrAlmLinePowerDegradePortn_Type()
)
pm10010mrAlmLinePowerDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLinePowerDegradePortn.setStatus("current")
_Pm10010mrAlmLineTrxOverTempPortn_Type = EkiOnOff
_Pm10010mrAlmLineTrxOverTempPortn_Object = MibTableColumn
pm10010mrAlmLineTrxOverTempPortn = _Pm10010mrAlmLineTrxOverTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 152, 1, 17),
    _Pm10010mrAlmLineTrxOverTempPortn_Type()
)
pm10010mrAlmLineTrxOverTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTrxOverTempPortn.setStatus("current")
_Pm10010mrAlmlineNetworkLaneRxOtnTable_Object = MibTable
pm10010mrAlmlineNetworkLaneRxOtnTable = _Pm10010mrAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm10010mrAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm10010mrAlmlineNetworkLaneRxOtnEntry = _Pm10010mrAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1)
)
pm10010mrAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm10010mrAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm10010mrAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm10010mrAlmlineNetworkLaneRxOtnIndex = _Pm10010mrAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 1),
    _Pm10010mrAlmlineNetworkLaneRxOtnIndex_Type()
)
pm10010mrAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm10010mrAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnOduAisPortn = _Pm10010mrAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 10),
    _Pm10010mrAlmLineRxOtnOduAisPortn_Type()
)
pm10010mrAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnOduAisPortn.setStatus("current")
_Pm10010mrAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnOtuAisPortn = _Pm10010mrAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 11),
    _Pm10010mrAlmLineRxOtnOtuAisPortn_Type()
)
pm10010mrAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm10010mrAlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxSmBdiPortn_Object = MibTableColumn
pm10010mrAlmLineRxSmBdiPortn = _Pm10010mrAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 12),
    _Pm10010mrAlmLineRxSmBdiPortn_Type()
)
pm10010mrAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxSmBdiPortn.setStatus("current")
_Pm10010mrAlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnIaePortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnIaePortn = _Pm10010mrAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 13),
    _Pm10010mrAlmLineRxOtnIaePortn_Type()
)
pm10010mrAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnIaePortn.setStatus("current")
_Pm10010mrAlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnOomPortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnOomPortn = _Pm10010mrAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 14),
    _Pm10010mrAlmLineRxOtnOomPortn_Type()
)
pm10010mrAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnOomPortn.setStatus("current")
_Pm10010mrAlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnLomPortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnLomPortn = _Pm10010mrAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 15),
    _Pm10010mrAlmLineRxOtnLomPortn_Type()
)
pm10010mrAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnLomPortn.setStatus("current")
_Pm10010mrAlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnOofPortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnOofPortn = _Pm10010mrAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 16),
    _Pm10010mrAlmLineRxOtnOofPortn_Type()
)
pm10010mrAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnOofPortn.setStatus("current")
_Pm10010mrAlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm10010mrAlmLineRxOtnLofPortn_Object = MibTableColumn
pm10010mrAlmLineRxOtnLofPortn = _Pm10010mrAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 168, 1, 17),
    _Pm10010mrAlmLineRxOtnLofPortn_Type()
)
pm10010mrAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineRxOtnLofPortn.setStatus("current")
_Pm10010mrAlmlineHostLaneTxOtnTable_Object = MibTable
pm10010mrAlmlineHostLaneTxOtnTable = _Pm10010mrAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineHostLaneTxOtnTable.setStatus("current")
_Pm10010mrAlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm10010mrAlmlineHostLaneTxOtnEntry = _Pm10010mrAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1)
)
pm10010mrAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm10010mrAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm10010mrAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm10010mrAlmlineHostLaneTxOtnIndex = _Pm10010mrAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 1),
    _Pm10010mrAlmlineHostLaneTxOtnIndex_Type()
)
pm10010mrAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm10010mrAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnOduAisPortn = _Pm10010mrAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 10),
    _Pm10010mrAlmLineTxOtnOduAisPortn_Type()
)
pm10010mrAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnOduAisPortn.setStatus("current")
_Pm10010mrAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnOtuAisPortn = _Pm10010mrAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 11),
    _Pm10010mrAlmLineTxOtnOtuAisPortn_Type()
)
pm10010mrAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm10010mrAlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxSmBdiPortn_Object = MibTableColumn
pm10010mrAlmLineTxSmBdiPortn = _Pm10010mrAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 12),
    _Pm10010mrAlmLineTxSmBdiPortn_Type()
)
pm10010mrAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxSmBdiPortn.setStatus("current")
_Pm10010mrAlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnIaePortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnIaePortn = _Pm10010mrAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 13),
    _Pm10010mrAlmLineTxOtnIaePortn_Type()
)
pm10010mrAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnIaePortn.setStatus("current")
_Pm10010mrAlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnOomPortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnOomPortn = _Pm10010mrAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 14),
    _Pm10010mrAlmLineTxOtnOomPortn_Type()
)
pm10010mrAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnOomPortn.setStatus("current")
_Pm10010mrAlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnLomPortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnLomPortn = _Pm10010mrAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 15),
    _Pm10010mrAlmLineTxOtnLomPortn_Type()
)
pm10010mrAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnLomPortn.setStatus("current")
_Pm10010mrAlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnOofPortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnOofPortn = _Pm10010mrAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 16),
    _Pm10010mrAlmLineTxOtnOofPortn_Type()
)
pm10010mrAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnOofPortn.setStatus("current")
_Pm10010mrAlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm10010mrAlmLineTxOtnLofPortn_Object = MibTableColumn
pm10010mrAlmLineTxOtnLofPortn = _Pm10010mrAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 2, 184, 1, 17),
    _Pm10010mrAlmLineTxOtnLofPortn_Type()
)
pm10010mrAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineTxOtnLofPortn.setStatus("current")
_Pm10010mrAlmLineCrit_ObjectIdentity = ObjectIdentity
pm10010mrAlmLineCrit = _Pm10010mrAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3)
)
_Pm10010mrAlmsynthAlmLineTable_Object = MibTable
pm10010mrAlmsynthAlmLineTable = _Pm10010mrAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pm10010mrAlmsynthAlmLineTable.setStatus("current")
_Pm10010mrAlmsynthAlmLineEntry_Object = MibTableRow
pm10010mrAlmsynthAlmLineEntry = _Pm10010mrAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1)
)
pm10010mrAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrAlmsynthAlmLineEntry.setStatus("current")


class _Pm10010mrAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm10010mrAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm10010mrAlmsynthAlmLineIndex_Object = MibTableColumn
pm10010mrAlmsynthAlmLineIndex = _Pm10010mrAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 1),
    _Pm10010mrAlmsynthAlmLineIndex_Type()
)
pm10010mrAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmsynthAlmLineIndex.setStatus("current")
_Pm10010mrAlmXfpAbsentPortn_Type = EkiOnOff
_Pm10010mrAlmXfpAbsentPortn_Object = MibTableColumn
pm10010mrAlmXfpAbsentPortn = _Pm10010mrAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 2),
    _Pm10010mrAlmXfpAbsentPortn_Type()
)
pm10010mrAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmXfpAbsentPortn.setStatus("current")
_Pm10010mrAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm10010mrAlmXfpInitNotComplPortn_Object = MibTableColumn
pm10010mrAlmXfpInitNotComplPortn = _Pm10010mrAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 3),
    _Pm10010mrAlmXfpInitNotComplPortn_Type()
)
pm10010mrAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmXfpInitNotComplPortn.setStatus("current")
_Pm10010mrAlmLineHwFailPortn_Type = EkiOnOff
_Pm10010mrAlmLineHwFailPortn_Object = MibTableColumn
pm10010mrAlmLineHwFailPortn = _Pm10010mrAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 5),
    _Pm10010mrAlmLineHwFailPortn_Type()
)
pm10010mrAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineHwFailPortn.setStatus("current")
_Pm10010mrAlmXfpTxOffPortn_Type = EkiOnOff
_Pm10010mrAlmXfpTxOffPortn_Object = MibTableColumn
pm10010mrAlmXfpTxOffPortn = _Pm10010mrAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 6),
    _Pm10010mrAlmXfpTxOffPortn_Type()
)
pm10010mrAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmXfpTxOffPortn.setStatus("current")
_Pm10010mrAlmLineLocalOosPortn_Type = EkiOnOff
_Pm10010mrAlmLineLocalOosPortn_Object = MibTableColumn
pm10010mrAlmLineLocalOosPortn = _Pm10010mrAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 7),
    _Pm10010mrAlmLineLocalOosPortn_Type()
)
pm10010mrAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineLocalOosPortn.setStatus("current")
_Pm10010mrAlmUpRdiInsPortn_Type = EkiOnOff
_Pm10010mrAlmUpRdiInsPortn_Object = MibTableColumn
pm10010mrAlmUpRdiInsPortn = _Pm10010mrAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 9),
    _Pm10010mrAlmUpRdiInsPortn_Type()
)
pm10010mrAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmUpRdiInsPortn.setStatus("current")
_Pm10010mrAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm10010mrAlmLineDdmWarningPortn_Object = MibTableColumn
pm10010mrAlmLineDdmWarningPortn = _Pm10010mrAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 10),
    _Pm10010mrAlmLineDdmWarningPortn_Type()
)
pm10010mrAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineDdmWarningPortn.setStatus("current")
_Pm10010mrAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm10010mrAlmLineDdmAlmPortn_Object = MibTableColumn
pm10010mrAlmLineDdmAlmPortn = _Pm10010mrAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 11),
    _Pm10010mrAlmLineDdmAlmPortn_Type()
)
pm10010mrAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineDdmAlmPortn.setStatus("current")
_Pm10010mrAlmLineFailPortn_Type = EkiOnOff
_Pm10010mrAlmLineFailPortn_Object = MibTableColumn
pm10010mrAlmLineFailPortn = _Pm10010mrAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 13),
    _Pm10010mrAlmLineFailPortn_Type()
)
pm10010mrAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineFailPortn.setStatus("current")
_Pm10010mrAlmLineActivePortn_Type = EkiOnOff
_Pm10010mrAlmLineActivePortn_Object = MibTableColumn
pm10010mrAlmLineActivePortn = _Pm10010mrAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 2, 3, 3, 24, 1, 17),
    _Pm10010mrAlmLineActivePortn_Type()
)
pm10010mrAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrAlmLineActivePortn.setStatus("current")
_Pm10010mrmeasures_ObjectIdentity = ObjectIdentity
pm10010mrmeasures = _Pm10010mrmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3)
)
_Pm10010mrMesrOther_ObjectIdentity = ObjectIdentity
pm10010mrMesrOther = _Pm10010mrMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1)
)
_Pm10010mrMesrsynth0_Type = EkiMeasureType
_Pm10010mrMesrsynth0_Object = MibScalar
pm10010mrMesrsynth0 = _Pm10010mrMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 0),
    _Pm10010mrMesrsynth0_Type()
)
pm10010mrMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrsynth0.setStatus("deprecated")
_Pm10010mrMesrsynth1_Type = EkiMeasureType
_Pm10010mrMesrsynth1_Object = MibScalar
pm10010mrMesrsynth1 = _Pm10010mrMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 1),
    _Pm10010mrMesrsynth1_Type()
)
pm10010mrMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrsynth1.setStatus("deprecated")


class _Pm10010mrMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm10010mrMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm10010mrMesrpmIntervalNumber_Object = MibScalar
pm10010mrMesrpmIntervalNumber = _Pm10010mrMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 7),
    _Pm10010mrMesrpmIntervalNumber_Type()
)
pm10010mrMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrpmIntervalNumber.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm10010mrMesrlineNetTxLaserOutputPwrAverage = _Pm10010mrMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 180),
    _Pm10010mrMesrlineNetTxLaserOutputPwrAverage_Type()
)
pm10010mrMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxLaserTempAverage_Object = MibScalar
pm10010mrMesrlineNetTxLaserTempAverage = _Pm10010mrMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 181),
    _Pm10010mrMesrlineNetTxLaserTempAverage_Type()
)
pm10010mrMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm10010mrMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm10010mrMesrlineNetTxBiasCurrentAverage = _Pm10010mrMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 182),
    _Pm10010mrMesrlineNetTxBiasCurrentAverage_Type()
)
pm10010mrMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm10010mrMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetRxInputPwrAverage_Object = MibScalar
pm10010mrMesrlineNetRxInputPwrAverage = _Pm10010mrMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 183),
    _Pm10010mrMesrlineNetRxInputPwrAverage_Type()
)
pm10010mrMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm10010mrMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineResidualChromaticDispAverage_Object = MibScalar
pm10010mrMesrlineResidualChromaticDispAverage = _Pm10010mrMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 184),
    _Pm10010mrMesrlineResidualChromaticDispAverage_Type()
)
pm10010mrMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm10010mrMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineDiffGroupDelayAverage_Object = MibScalar
pm10010mrMesrlineDiffGroupDelayAverage = _Pm10010mrMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 185),
    _Pm10010mrMesrlineDiffGroupDelayAverage_Type()
)
pm10010mrMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm10010mrMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineQFactorAverage_Object = MibScalar
pm10010mrMesrlineQFactorAverage = _Pm10010mrMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 186),
    _Pm10010mrMesrlineQFactorAverage_Type()
)
pm10010mrMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorAverage.setStatus("current")


class _Pm10010mrMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm10010mrMesrlineCarrierFreqOffsetAverage = _Pm10010mrMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 187),
    _Pm10010mrMesrlineCarrierFreqOffsetAverage_Type()
)
pm10010mrMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm10010mrMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineOsnrAverage_Object = MibScalar
pm10010mrMesrlineOsnrAverage = _Pm10010mrMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 188),
    _Pm10010mrMesrlineOsnrAverage_Type()
)
pm10010mrMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrAverage.setStatus("current")


class _Pm10010mrMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetTxTempMin_Object = MibScalar
pm10010mrMesrclientNetTxTempMin = _Pm10010mrMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 192),
    _Pm10010mrMesrclientNetTxTempMin_Type()
)
pm10010mrMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxTempMin.setStatus("current")


class _Pm10010mrMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetTxBiasMin_Object = MibScalar
pm10010mrMesrclientNetTxBiasMin = _Pm10010mrMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 193),
    _Pm10010mrMesrclientNetTxBiasMin_Type()
)
pm10010mrMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxBiasMin.setStatus("current")


class _Pm10010mrMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetTxPwrMin_Object = MibScalar
pm10010mrMesrclientNetTxPwrMin = _Pm10010mrMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 194),
    _Pm10010mrMesrclientNetTxPwrMin_Type()
)
pm10010mrMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxPwrMin.setStatus("current")


class _Pm10010mrMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetRxPwrMin_Object = MibScalar
pm10010mrMesrclientNetRxPwrMin = _Pm10010mrMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 195),
    _Pm10010mrMesrclientNetRxPwrMin_Type()
)
pm10010mrMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetRxPwrMin.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm10010mrMesrlineNetTxLaserOutputPwrMin = _Pm10010mrMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 196),
    _Pm10010mrMesrlineNetTxLaserOutputPwrMin_Type()
)
pm10010mrMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxLaserTempMin_Object = MibScalar
pm10010mrMesrlineNetTxLaserTempMin = _Pm10010mrMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 197),
    _Pm10010mrMesrlineNetTxLaserTempMin_Type()
)
pm10010mrMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempMin.setStatus("current")


class _Pm10010mrMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxBiasCurrentMin_Object = MibScalar
pm10010mrMesrlineNetTxBiasCurrentMin = _Pm10010mrMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 198),
    _Pm10010mrMesrlineNetTxBiasCurrentMin_Type()
)
pm10010mrMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm10010mrMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetRxInputPwrMin_Object = MibScalar
pm10010mrMesrlineNetRxInputPwrMin = _Pm10010mrMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 199),
    _Pm10010mrMesrlineNetRxInputPwrMin_Type()
)
pm10010mrMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrMin.setStatus("current")


class _Pm10010mrMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineResidualChromaticDispMin_Object = MibScalar
pm10010mrMesrlineResidualChromaticDispMin = _Pm10010mrMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 200),
    _Pm10010mrMesrlineResidualChromaticDispMin_Type()
)
pm10010mrMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispMin.setStatus("current")


class _Pm10010mrMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineDiffGroupDelayMin_Object = MibScalar
pm10010mrMesrlineDiffGroupDelayMin = _Pm10010mrMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 201),
    _Pm10010mrMesrlineDiffGroupDelayMin_Type()
)
pm10010mrMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayMin.setStatus("current")


class _Pm10010mrMesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineQFactorMin_Object = MibScalar
pm10010mrMesrlineQFactorMin = _Pm10010mrMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 202),
    _Pm10010mrMesrlineQFactorMin_Type()
)
pm10010mrMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorMin.setStatus("current")


class _Pm10010mrMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineCarrierFreqOffsetMin_Object = MibScalar
pm10010mrMesrlineCarrierFreqOffsetMin = _Pm10010mrMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 203),
    _Pm10010mrMesrlineCarrierFreqOffsetMin_Type()
)
pm10010mrMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm10010mrMesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm10010mrMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineOsnrMin_Object = MibScalar
pm10010mrMesrlineOsnrMin = _Pm10010mrMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 204),
    _Pm10010mrMesrlineOsnrMin_Type()
)
pm10010mrMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrMin.setStatus("current")


class _Pm10010mrMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetTxTempMax_Object = MibScalar
pm10010mrMesrclientNetTxTempMax = _Pm10010mrMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 208),
    _Pm10010mrMesrclientNetTxTempMax_Type()
)
pm10010mrMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxTempMax.setStatus("current")


class _Pm10010mrMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetTxBiasMax_Object = MibScalar
pm10010mrMesrclientNetTxBiasMax = _Pm10010mrMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 209),
    _Pm10010mrMesrclientNetTxBiasMax_Type()
)
pm10010mrMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxBiasMax.setStatus("current")


class _Pm10010mrMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetTxPwrMax_Object = MibScalar
pm10010mrMesrclientNetTxPwrMax = _Pm10010mrMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 210),
    _Pm10010mrMesrclientNetTxPwrMax_Type()
)
pm10010mrMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxPwrMax.setStatus("current")


class _Pm10010mrMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm10010mrMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientNetRxPwrMax_Object = MibScalar
pm10010mrMesrclientNetRxPwrMax = _Pm10010mrMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 211),
    _Pm10010mrMesrclientNetRxPwrMax_Type()
)
pm10010mrMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetRxPwrMax.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm10010mrMesrlineNetTxLaserOutputPwrMax = _Pm10010mrMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 212),
    _Pm10010mrMesrlineNetTxLaserOutputPwrMax_Type()
)
pm10010mrMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxLaserTempMax_Object = MibScalar
pm10010mrMesrlineNetTxLaserTempMax = _Pm10010mrMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 213),
    _Pm10010mrMesrlineNetTxLaserTempMax_Type()
)
pm10010mrMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempMax.setStatus("current")


class _Pm10010mrMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetTxBiasCurrentMax_Object = MibScalar
pm10010mrMesrlineNetTxBiasCurrentMax = _Pm10010mrMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 214),
    _Pm10010mrMesrlineNetTxBiasCurrentMax_Type()
)
pm10010mrMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm10010mrMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineNetRxInputPwrMax_Object = MibScalar
pm10010mrMesrlineNetRxInputPwrMax = _Pm10010mrMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 215),
    _Pm10010mrMesrlineNetRxInputPwrMax_Type()
)
pm10010mrMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrMax.setStatus("current")


class _Pm10010mrMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineResidualChromaticDispMax_Object = MibScalar
pm10010mrMesrlineResidualChromaticDispMax = _Pm10010mrMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 216),
    _Pm10010mrMesrlineResidualChromaticDispMax_Type()
)
pm10010mrMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispMax.setStatus("current")


class _Pm10010mrMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineDiffGroupDelayMax_Object = MibScalar
pm10010mrMesrlineDiffGroupDelayMax = _Pm10010mrMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 217),
    _Pm10010mrMesrlineDiffGroupDelayMax_Type()
)
pm10010mrMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayMax.setStatus("current")


class _Pm10010mrMesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineQFactorMax_Object = MibScalar
pm10010mrMesrlineQFactorMax = _Pm10010mrMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 218),
    _Pm10010mrMesrlineQFactorMax_Type()
)
pm10010mrMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorMax.setStatus("current")


class _Pm10010mrMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineCarrierFreqOffsetMax_Object = MibScalar
pm10010mrMesrlineCarrierFreqOffsetMax = _Pm10010mrMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 219),
    _Pm10010mrMesrlineCarrierFreqOffsetMax_Type()
)
pm10010mrMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm10010mrMesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm10010mrMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineOsnrMax_Object = MibScalar
pm10010mrMesrlineOsnrMax = _Pm10010mrMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 1, 220),
    _Pm10010mrMesrlineOsnrMax_Type()
)
pm10010mrMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrMax.setStatus("current")
_Pm10010mrMesrClient_ObjectIdentity = ObjectIdentity
pm10010mrMesrClient = _Pm10010mrMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2)
)


class _Pm10010mrMesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm10010mrMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientCfpTemp_Object = MibScalar
pm10010mrMesrclientCfpTemp = _Pm10010mrMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 8),
    _Pm10010mrMesrclientCfpTemp_Type()
)
pm10010mrMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientCfpTemp.setStatus("current")


class _Pm10010mrMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm10010mrMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientCfp3v3Voltage_Object = MibScalar
pm10010mrMesrclientCfp3v3Voltage = _Pm10010mrMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 9),
    _Pm10010mrMesrclientCfp3v3Voltage_Type()
)
pm10010mrMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientCfp3v3Voltage.setStatus("current")


class _Pm10010mrMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010mrMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010mrMesrclientSoaBiasCurrent_Object = MibScalar
pm10010mrMesrclientSoaBiasCurrent = _Pm10010mrMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 10),
    _Pm10010mrMesrclientSoaBiasCurrent_Type()
)
pm10010mrMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientSoaBiasCurrent.setStatus("current")
_Pm10010mrMesrclientNetTxTempTable_Object = MibTable
pm10010mrMesrclientNetTxTempTable = _Pm10010mrMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxTempTable.setStatus("current")
_Pm10010mrMesrclientNetTxTempEntry_Object = MibTableRow
pm10010mrMesrclientNetTxTempEntry = _Pm10010mrMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 16, 1)
)
pm10010mrMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxTempEntry.setStatus("current")


class _Pm10010mrMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pm10010mrMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetTxTempIndex_Object = MibTableColumn
pm10010mrMesrclientNetTxTempIndex = _Pm10010mrMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 16, 1, 1),
    _Pm10010mrMesrclientNetTxTempIndex_Type()
)
pm10010mrMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxTempIndex.setStatus("current")


class _Pm10010mrMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pm10010mrMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetTxTempPortn_Object = MibTableColumn
pm10010mrMesrclientNetTxTempPortn = _Pm10010mrMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 16, 1, 2),
    _Pm10010mrMesrclientNetTxTempPortn_Type()
)
pm10010mrMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxTempPortn.setStatus("current")
_Pm10010mrMesrclientNetTxBiasTable_Object = MibTable
pm10010mrMesrclientNetTxBiasTable = _Pm10010mrMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxBiasTable.setStatus("current")
_Pm10010mrMesrclientNetTxBiasEntry_Object = MibTableRow
pm10010mrMesrclientNetTxBiasEntry = _Pm10010mrMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 32, 1)
)
pm10010mrMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxBiasEntry.setStatus("current")


class _Pm10010mrMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pm10010mrMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetTxBiasIndex_Object = MibTableColumn
pm10010mrMesrclientNetTxBiasIndex = _Pm10010mrMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 32, 1, 1),
    _Pm10010mrMesrclientNetTxBiasIndex_Type()
)
pm10010mrMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxBiasIndex.setStatus("current")


class _Pm10010mrMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pm10010mrMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetTxBiasPortn_Object = MibTableColumn
pm10010mrMesrclientNetTxBiasPortn = _Pm10010mrMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 32, 1, 2),
    _Pm10010mrMesrclientNetTxBiasPortn_Type()
)
pm10010mrMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxBiasPortn.setStatus("current")
_Pm10010mrMesrclientNetTxPwrTable_Object = MibTable
pm10010mrMesrclientNetTxPwrTable = _Pm10010mrMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxPwrTable.setStatus("current")
_Pm10010mrMesrclientNetTxPwrEntry_Object = MibTableRow
pm10010mrMesrclientNetTxPwrEntry = _Pm10010mrMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 48, 1)
)
pm10010mrMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxPwrEntry.setStatus("current")


class _Pm10010mrMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pm10010mrMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetTxPwrIndex_Object = MibTableColumn
pm10010mrMesrclientNetTxPwrIndex = _Pm10010mrMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 48, 1, 1),
    _Pm10010mrMesrclientNetTxPwrIndex_Type()
)
pm10010mrMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxPwrIndex.setStatus("current")


class _Pm10010mrMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pm10010mrMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetTxPwrPortn_Object = MibTableColumn
pm10010mrMesrclientNetTxPwrPortn = _Pm10010mrMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 48, 1, 2),
    _Pm10010mrMesrclientNetTxPwrPortn_Type()
)
pm10010mrMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetTxPwrPortn.setStatus("current")
_Pm10010mrMesrclientNetRxPwrTable_Object = MibTable
pm10010mrMesrclientNetRxPwrTable = _Pm10010mrMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetRxPwrTable.setStatus("current")
_Pm10010mrMesrclientNetRxPwrEntry_Object = MibTableRow
pm10010mrMesrclientNetRxPwrEntry = _Pm10010mrMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 64, 1)
)
pm10010mrMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetRxPwrEntry.setStatus("current")


class _Pm10010mrMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pm10010mrMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetRxPwrIndex_Object = MibTableColumn
pm10010mrMesrclientNetRxPwrIndex = _Pm10010mrMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 64, 1, 1),
    _Pm10010mrMesrclientNetRxPwrIndex_Type()
)
pm10010mrMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetRxPwrIndex.setStatus("current")


class _Pm10010mrMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pm10010mrMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrclientNetRxPwrPortn_Object = MibTableColumn
pm10010mrMesrclientNetRxPwrPortn = _Pm10010mrMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 2, 64, 1, 2),
    _Pm10010mrMesrclientNetRxPwrPortn_Type()
)
pm10010mrMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrclientNetRxPwrPortn.setStatus("current")
_Pm10010mrMesrLine_ObjectIdentity = ObjectIdentity
pm10010mrMesrLine = _Pm10010mrMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3)
)


class _Pm10010mrMesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm10010mrMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineMsaTemp_Object = MibScalar
pm10010mrMesrlineMsaTemp = _Pm10010mrMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 12),
    _Pm10010mrMesrlineMsaTemp_Type()
)
pm10010mrMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineMsaTemp.setStatus("current")


class _Pm10010mrMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm10010mrMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineMsa3v3Voltage_Object = MibScalar
pm10010mrMesrlineMsa3v3Voltage = _Pm10010mrMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 13),
    _Pm10010mrMesrlineMsa3v3Voltage_Type()
)
pm10010mrMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineMsa3v3Voltage.setStatus("current")


class _Pm10010mrMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010mrMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010mrMesrlineSoaBiasCurrent_Object = MibScalar
pm10010mrMesrlineSoaBiasCurrent = _Pm10010mrMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 14),
    _Pm10010mrMesrlineSoaBiasCurrent_Type()
)
pm10010mrMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineSoaBiasCurrent.setStatus("current")
_Pm10010mrMesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm10010mrMesrlineNetTxLaserOutputPwrTable = _Pm10010mrMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm10010mrMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm10010mrMesrlineNetTxLaserOutputPwrEntry = _Pm10010mrMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 80, 1)
)
pm10010mrMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm10010mrMesrlineNetTxLaserOutputPwrIndex = _Pm10010mrMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 80, 1, 1),
    _Pm10010mrMesrlineNetTxLaserOutputPwrIndex_Type()
)
pm10010mrMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm10010mrMesrlineNetTxLaserOutputPwrPortn = _Pm10010mrMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 80, 1, 2),
    _Pm10010mrMesrlineNetTxLaserOutputPwrPortn_Type()
)
pm10010mrMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm10010mrMesrlineNetTxLaserTempTable_Object = MibTable
pm10010mrMesrlineNetTxLaserTempTable = _Pm10010mrMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempTable.setStatus("current")
_Pm10010mrMesrlineNetTxLaserTempEntry_Object = MibTableRow
pm10010mrMesrlineNetTxLaserTempEntry = _Pm10010mrMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 96, 1)
)
pm10010mrMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm10010mrMesrlineNetTxLaserTempIndex = _Pm10010mrMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 96, 1, 1),
    _Pm10010mrMesrlineNetTxLaserTempIndex_Type()
)
pm10010mrMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm10010mrMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm10010mrMesrlineNetTxLaserTempPortn = _Pm10010mrMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 96, 1, 2),
    _Pm10010mrMesrlineNetTxLaserTempPortn_Type()
)
pm10010mrMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxLaserTempPortn.setStatus("current")
_Pm10010mrMesrlineNetTxBiasCurrentTable_Object = MibTable
pm10010mrMesrlineNetTxBiasCurrentTable = _Pm10010mrMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm10010mrMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm10010mrMesrlineNetTxBiasCurrentEntry = _Pm10010mrMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 112, 1)
)
pm10010mrMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm10010mrMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm10010mrMesrlineNetTxBiasCurrentIndex = _Pm10010mrMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 112, 1, 1),
    _Pm10010mrMesrlineNetTxBiasCurrentIndex_Type()
)
pm10010mrMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm10010mrMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm10010mrMesrlineNetTxBiasCurrentPortn = _Pm10010mrMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 112, 1, 2),
    _Pm10010mrMesrlineNetTxBiasCurrentPortn_Type()
)
pm10010mrMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm10010mrMesrlineNetRxInputPwrTable_Object = MibTable
pm10010mrMesrlineNetRxInputPwrTable = _Pm10010mrMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrTable.setStatus("current")
_Pm10010mrMesrlineNetRxInputPwrEntry_Object = MibTableRow
pm10010mrMesrlineNetRxInputPwrEntry = _Pm10010mrMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 128, 1)
)
pm10010mrMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm10010mrMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm10010mrMesrlineNetRxInputPwrIndex = _Pm10010mrMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 128, 1, 1),
    _Pm10010mrMesrlineNetRxInputPwrIndex_Type()
)
pm10010mrMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm10010mrMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm10010mrMesrlineNetRxInputPwrPortn = _Pm10010mrMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 128, 1, 2),
    _Pm10010mrMesrlineNetRxInputPwrPortn_Type()
)
pm10010mrMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineNetRxInputPwrPortn.setStatus("current")
_Pm10010mrMesrlineResidualChromaticDispTable_Object = MibTable
pm10010mrMesrlineResidualChromaticDispTable = _Pm10010mrMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispTable.setStatus("current")
_Pm10010mrMesrlineResidualChromaticDispEntry_Object = MibTableRow
pm10010mrMesrlineResidualChromaticDispEntry = _Pm10010mrMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 144, 1)
)
pm10010mrMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm10010mrMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm10010mrMesrlineResidualChromaticDispIndex = _Pm10010mrMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 144, 1, 1),
    _Pm10010mrMesrlineResidualChromaticDispIndex_Type()
)
pm10010mrMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm10010mrMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm10010mrMesrlineResidualChromaticDispPortn = _Pm10010mrMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 144, 1, 2),
    _Pm10010mrMesrlineResidualChromaticDispPortn_Type()
)
pm10010mrMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineResidualChromaticDispPortn.setStatus("current")
_Pm10010mrMesrlineDiffGroupDelayTable_Object = MibTable
pm10010mrMesrlineDiffGroupDelayTable = _Pm10010mrMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayTable.setStatus("current")
_Pm10010mrMesrlineDiffGroupDelayEntry_Object = MibTableRow
pm10010mrMesrlineDiffGroupDelayEntry = _Pm10010mrMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 148, 1)
)
pm10010mrMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm10010mrMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm10010mrMesrlineDiffGroupDelayIndex = _Pm10010mrMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 148, 1, 1),
    _Pm10010mrMesrlineDiffGroupDelayIndex_Type()
)
pm10010mrMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm10010mrMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm10010mrMesrlineDiffGroupDelayPortn = _Pm10010mrMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 148, 1, 2),
    _Pm10010mrMesrlineDiffGroupDelayPortn_Type()
)
pm10010mrMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineDiffGroupDelayPortn.setStatus("current")
_Pm10010mrMesrlineQFactorTable_Object = MibTable
pm10010mrMesrlineQFactorTable = _Pm10010mrMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorTable.setStatus("current")
_Pm10010mrMesrlineQFactorEntry_Object = MibTableRow
pm10010mrMesrlineQFactorEntry = _Pm10010mrMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 152, 1)
)
pm10010mrMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorEntry.setStatus("current")


class _Pm10010mrMesrlineQFactorIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineQFactorIndex_Object = MibTableColumn
pm10010mrMesrlineQFactorIndex = _Pm10010mrMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 152, 1, 1),
    _Pm10010mrMesrlineQFactorIndex_Type()
)
pm10010mrMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorIndex.setStatus("current")


class _Pm10010mrMesrlineQFactorPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineQFactorPortn_Object = MibTableColumn
pm10010mrMesrlineQFactorPortn = _Pm10010mrMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 152, 1, 2),
    _Pm10010mrMesrlineQFactorPortn_Type()
)
pm10010mrMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineQFactorPortn.setStatus("current")
_Pm10010mrMesrlineCarrierFreqOffsetTable_Object = MibTable
pm10010mrMesrlineCarrierFreqOffsetTable = _Pm10010mrMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm10010mrMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm10010mrMesrlineCarrierFreqOffsetEntry = _Pm10010mrMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 156, 1)
)
pm10010mrMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm10010mrMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm10010mrMesrlineCarrierFreqOffsetIndex = _Pm10010mrMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 156, 1, 1),
    _Pm10010mrMesrlineCarrierFreqOffsetIndex_Type()
)
pm10010mrMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm10010mrMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm10010mrMesrlineCarrierFreqOffsetPortn = _Pm10010mrMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 156, 1, 2),
    _Pm10010mrMesrlineCarrierFreqOffsetPortn_Type()
)
pm10010mrMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm10010mrMesrlineOsnrTable_Object = MibTable
pm10010mrMesrlineOsnrTable = _Pm10010mrMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrTable.setStatus("current")
_Pm10010mrMesrlineOsnrEntry_Object = MibTableRow
pm10010mrMesrlineOsnrEntry = _Pm10010mrMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 160, 1)
)
pm10010mrMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrEntry.setStatus("current")


class _Pm10010mrMesrlineOsnrIndex_Type(Integer32):
    """Custom type pm10010mrMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm10010mrMesrlineOsnrIndex_Object = MibTableColumn
pm10010mrMesrlineOsnrIndex = _Pm10010mrMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 160, 1, 1),
    _Pm10010mrMesrlineOsnrIndex_Type()
)
pm10010mrMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrIndex.setStatus("current")


class _Pm10010mrMesrlineOsnrPortn_Type(Integer32):
    """Custom type pm10010mrMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mrMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm10010mrMesrlineOsnrPortn_Object = MibTableColumn
pm10010mrMesrlineOsnrPortn = _Pm10010mrMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 3, 3, 160, 1, 2),
    _Pm10010mrMesrlineOsnrPortn_Type()
)
pm10010mrMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMesrlineOsnrPortn.setStatus("current")
_Pm10010mrcounters_ObjectIdentity = ObjectIdentity
pm10010mrcounters = _Pm10010mrcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4)
)
_Pm10010mrCntOther_ObjectIdentity = ObjectIdentity
pm10010mrCntOther = _Pm10010mrCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 1)
)
_Pm10010mrCntClient_ObjectIdentity = ObjectIdentity
pm10010mrCntClient = _Pm10010mrCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2)
)
_Pm10010mrCntclientInputErrorCounterLaneOneTable_Object = MibTable
pm10010mrCntclientInputErrorCounterLaneOneTable = _Pm10010mrCntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneOneTable.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
pm10010mrCntclientInputErrorCounterLaneOneEntry = _Pm10010mrCntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 16, 1)
)
pm10010mrCntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Pm10010mrCntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type pm10010mrCntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Pm10010mrCntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneOneIndex = _Pm10010mrCntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 16, 1, 1),
    _Pm10010mrCntclientInputErrorCounterLaneOneIndex_Type()
)
pm10010mrCntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Pm10010mrCntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneOneValuePortn = _Pm10010mrCntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 16, 1, 2),
    _Pm10010mrCntclientInputErrorCounterLaneOneValuePortn_Type()
)
pm10010mrCntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Pm10010mrCntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneOneErrorPortn = _Pm10010mrCntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 16, 1, 3),
    _Pm10010mrCntclientInputErrorCounterLaneOneErrorPortn_Type()
)
pm10010mrCntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn = _Pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 16, 1, 4),
    _Pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneTwoTable_Object = MibTable
pm10010mrCntclientInputErrorCounterLaneTwoTable = _Pm10010mrCntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
pm10010mrCntclientInputErrorCounterLaneTwoEntry = _Pm10010mrCntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 32, 1)
)
pm10010mrCntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Pm10010mrCntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type pm10010mrCntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Pm10010mrCntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneTwoIndex = _Pm10010mrCntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 32, 1, 1),
    _Pm10010mrCntclientInputErrorCounterLaneTwoIndex_Type()
)
pm10010mrCntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Pm10010mrCntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneTwoValuePortn = _Pm10010mrCntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 32, 1, 2),
    _Pm10010mrCntclientInputErrorCounterLaneTwoValuePortn_Type()
)
pm10010mrCntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn = _Pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 32, 1, 3),
    _Pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn = _Pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 32, 1, 4),
    _Pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterTable_Object = MibTable
pm10010mrCntclientInputErrorCounterTable = _Pm10010mrCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 80)
)
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterTable.setStatus("current")
_Pm10010mrCntclientInputErrorCounterEntry_Object = MibTableRow
pm10010mrCntclientInputErrorCounterEntry = _Pm10010mrCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 80, 1)
)
pm10010mrCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterEntry.setStatus("current")


class _Pm10010mrCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntclientInputErrorCounterIndex_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterIndex = _Pm10010mrCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 80, 1, 1),
    _Pm10010mrCntclientInputErrorCounterIndex_Type()
)
pm10010mrCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterIndex.setStatus("current")
_Pm10010mrCntclientInputErrorCounterValuePortn_Type = Counter32
_Pm10010mrCntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterValuePortn = _Pm10010mrCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 80, 1, 2),
    _Pm10010mrCntclientInputErrorCounterValuePortn_Type()
)
pm10010mrCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterValuePortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterErrorPortn = _Pm10010mrCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 80, 1, 3),
    _Pm10010mrCntclientInputErrorCounterErrorPortn_Type()
)
pm10010mrCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm10010mrCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntclientInputErrorCounterOverloadPortn = _Pm10010mrCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 80, 1, 4),
    _Pm10010mrCntclientInputErrorCounterOverloadPortn_Type()
)
pm10010mrCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm10010mrCntclientCbipCounterTable_Object = MibTable
pm10010mrCntclientCbipCounterTable = _Pm10010mrCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pm10010mrCntclientCbipCounterTable.setStatus("current")
_Pm10010mrCntclientCbipCounterEntry_Object = MibTableRow
pm10010mrCntclientCbipCounterEntry = _Pm10010mrCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 96, 1)
)
pm10010mrCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntclientCbipCounterEntry.setStatus("current")


class _Pm10010mrCntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntclientCbipCounterIndex_Object = MibTableColumn
pm10010mrCntclientCbipCounterIndex = _Pm10010mrCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 96, 1, 1),
    _Pm10010mrCntclientCbipCounterIndex_Type()
)
pm10010mrCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientCbipCounterIndex.setStatus("current")
_Pm10010mrCntclientCbipCounterValuePortn_Type = Counter32
_Pm10010mrCntclientCbipCounterValuePortn_Object = MibTableColumn
pm10010mrCntclientCbipCounterValuePortn = _Pm10010mrCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 96, 1, 2),
    _Pm10010mrCntclientCbipCounterValuePortn_Type()
)
pm10010mrCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientCbipCounterValuePortn.setStatus("current")
_Pm10010mrCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntclientCbipCounterErrorPortn_Object = MibTableColumn
pm10010mrCntclientCbipCounterErrorPortn = _Pm10010mrCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 96, 1, 3),
    _Pm10010mrCntclientCbipCounterErrorPortn_Type()
)
pm10010mrCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientCbipCounterErrorPortn.setStatus("current")
_Pm10010mrCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntclientCbipCounterOverloadPortn = _Pm10010mrCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 2, 96, 1, 4),
    _Pm10010mrCntclientCbipCounterOverloadPortn_Type()
)
pm10010mrCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntclientCbipCounterOverloadPortn.setStatus("current")
_Pm10010mrCntLine_ObjectIdentity = ObjectIdentity
pm10010mrCntLine = _Pm10010mrCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3)
)
_Pm10010mrCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm10010mrCntlocalLineSmBip8ErrorCounterTable = _Pm10010mrCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010mrCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010mrCntlocalLineSmBip8ErrorCounterEntry = _Pm10010mrCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 192, 1)
)
pm10010mrCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010mrCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010mrCntlocalLineSmBip8ErrorCounterIndex = _Pm10010mrCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 192, 1, 1),
    _Pm10010mrCntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm10010mrCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn = _Pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 192, 1, 2),
    _Pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn = _Pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 192, 1, 3),
    _Pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 192, 1, 4),
    _Pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm10010mrCntlocalLineFecCorrectedErrorsCounterTable = _Pm10010mrCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry = _Pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 193, 1)
)
pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex = _Pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 193, 1, 1),
    _Pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 193, 1, 2),
    _Pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 193, 1, 3),
    _Pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 193, 1, 4),
    _Pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm10010mrCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm10010mrCntremoteLineSmBip8ErrorCounterTable = _Pm10010mrCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm10010mrCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010mrCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010mrCntremoteLineSmBip8ErrorCounterEntry = _Pm10010mrCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 194, 1)
)
pm10010mrCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010mrCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010mrCntremoteLineSmBip8ErrorCounterIndex = _Pm10010mrCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 194, 1, 1),
    _Pm10010mrCntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm10010mrCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn = _Pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 194, 1, 2),
    _Pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn = _Pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 194, 1, 3),
    _Pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 194, 1, 4),
    _Pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010mrCntlineDfrmTimCntTable_Object = MibTable
pm10010mrCntlineDfrmTimCntTable = _Pm10010mrCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm10010mrCntlineDfrmTimCntTable.setStatus("current")
_Pm10010mrCntlineDfrmTimCntEntry_Object = MibTableRow
pm10010mrCntlineDfrmTimCntEntry = _Pm10010mrCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 195, 1)
)
pm10010mrCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntlineDfrmTimCntEntry.setStatus("current")


class _Pm10010mrCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm10010mrCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm10010mrCntlineDfrmTimCntIndex_Object = MibTableColumn
pm10010mrCntlineDfrmTimCntIndex = _Pm10010mrCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 195, 1, 1),
    _Pm10010mrCntlineDfrmTimCntIndex_Type()
)
pm10010mrCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlineDfrmTimCntIndex.setStatus("current")
_Pm10010mrCntlineDfrmTimCntValuePortn_Type = Counter64
_Pm10010mrCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm10010mrCntlineDfrmTimCntValuePortn = _Pm10010mrCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 195, 1, 2),
    _Pm10010mrCntlineDfrmTimCntValuePortn_Type()
)
pm10010mrCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm10010mrCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm10010mrCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm10010mrCntlineDfrmTimCntErrorPortn = _Pm10010mrCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 195, 1, 3),
    _Pm10010mrCntlineDfrmTimCntErrorPortn_Type()
)
pm10010mrCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm10010mrCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm10010mrCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm10010mrCntlineDfrmTimCntOverloadPortn = _Pm10010mrCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 195, 1, 4),
    _Pm10010mrCntlineDfrmTimCntOverloadPortn_Type()
)
pm10010mrCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterTable = _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry = _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 196, 1)
)
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex = _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 196, 1, 1),
    _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 196, 1, 2),
    _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 196, 1, 3),
    _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 196, 1, 4),
    _Pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterTable = _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 197, 1)
)
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 197, 1, 1),
    _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 197, 1, 2),
    _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 197, 1, 3),
    _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 4, 3, 197, 1, 4),
    _Pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10010mrcontrolsWrite_ObjectIdentity = ObjectIdentity
pm10010mrcontrolsWrite = _Pm10010mrcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6)
)
_Pm10010mrCtrlOther_ObjectIdentity = ObjectIdentity
pm10010mrCtrlOther = _Pm10010mrCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1)
)
_Pm10010mrCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm10010mrCtrlconfMgnt1 = _Pm10010mrCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 1)
)
_Pm10010mrCtrlConf1Load1_Type = EkiOnOff
_Pm10010mrCtrlConf1Load1_Object = MibScalar
pm10010mrCtrlConf1Load1 = _Pm10010mrCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 1, 1),
    _Pm10010mrCtrlConf1Load1_Type()
)
pm10010mrCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlConf1Load1.setStatus("current")
_Pm10010mrCtrlConf2Load1_Type = EkiOnOff
_Pm10010mrCtrlConf2Load1_Object = MibScalar
pm10010mrCtrlConf2Load1 = _Pm10010mrCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 1, 2),
    _Pm10010mrCtrlConf2Load1_Type()
)
pm10010mrCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlConf2Load1.setStatus("current")
_Pm10010mrCtrlConf2Flash1_Type = EkiOnOff
_Pm10010mrCtrlConf2Flash1_Object = MibScalar
pm10010mrCtrlConf2Flash1 = _Pm10010mrCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 1, 10),
    _Pm10010mrCtrlConf2Flash1_Type()
)
pm10010mrCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlConf2Flash1.setStatus("current")
_Pm10010mrCtrlConf2Clear1_Type = EkiOnOff
_Pm10010mrCtrlConf2Clear1_Object = MibScalar
pm10010mrCtrlConf2Clear1 = _Pm10010mrCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 1, 14),
    _Pm10010mrCtrlConf2Clear1_Type()
)
pm10010mrCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlConf2Clear1.setStatus("current")
_Pm10010mrCtrlsynth4_ObjectIdentity = ObjectIdentity
pm10010mrCtrlsynth4 = _Pm10010mrCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 4)
)
_Pm10010mrCtrlCorrelatOn_Type = EkiOnOff
_Pm10010mrCtrlCorrelatOn_Object = MibScalar
pm10010mrCtrlCorrelatOn = _Pm10010mrCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 4, 1),
    _Pm10010mrCtrlCorrelatOn_Type()
)
pm10010mrCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlCorrelatOn.setStatus("current")
_Pm10010mrCtrlCorrelatOff_Type = EkiOnOff
_Pm10010mrCtrlCorrelatOff_Object = MibScalar
pm10010mrCtrlCorrelatOff = _Pm10010mrCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 4, 2),
    _Pm10010mrCtrlCorrelatOff_Type()
)
pm10010mrCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlCorrelatOff.setStatus("current")
_Pm10010mrCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm10010mrCtrlswMgnt = _Pm10010mrCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 5)
)
_Pm10010mrCtrlColdReset_Type = EkiOnOff
_Pm10010mrCtrlColdReset_Object = MibScalar
pm10010mrCtrlColdReset = _Pm10010mrCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 5, 2),
    _Pm10010mrCtrlColdReset_Type()
)
pm10010mrCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlColdReset.setStatus("current")
_Pm10010mrCtrlWarmReset_Type = EkiOnOff
_Pm10010mrCtrlWarmReset_Object = MibScalar
pm10010mrCtrlWarmReset = _Pm10010mrCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 5, 3),
    _Pm10010mrCtrlWarmReset_Type()
)
pm10010mrCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlWarmReset.setStatus("current")
_Pm10010mrCtrlLoadSwBank1_Type = EkiOnOff
_Pm10010mrCtrlLoadSwBank1_Object = MibScalar
pm10010mrCtrlLoadSwBank1 = _Pm10010mrCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 5, 5),
    _Pm10010mrCtrlLoadSwBank1_Type()
)
pm10010mrCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLoadSwBank1.setStatus("current")
_Pm10010mrCtrlLoadSwBank2_Type = EkiOnOff
_Pm10010mrCtrlLoadSwBank2_Object = MibScalar
pm10010mrCtrlLoadSwBank2 = _Pm10010mrCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 5, 6),
    _Pm10010mrCtrlLoadSwBank2_Type()
)
pm10010mrCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLoadSwBank2.setStatus("current")
_Pm10010mrCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm10010mrCtrlgwMgnt = _Pm10010mrCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 6)
)
_Pm10010mrCtrlCurrentGwReset_Type = EkiOnOff
_Pm10010mrCtrlCurrentGwReset_Object = MibScalar
pm10010mrCtrlCurrentGwReset = _Pm10010mrCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 6, 1),
    _Pm10010mrCtrlCurrentGwReset_Type()
)
pm10010mrCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlCurrentGwReset.setStatus("current")
_Pm10010mrCtrlLoadGwBank1_Type = EkiOnOff
_Pm10010mrCtrlLoadGwBank1_Object = MibScalar
pm10010mrCtrlLoadGwBank1 = _Pm10010mrCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 6, 5),
    _Pm10010mrCtrlLoadGwBank1_Type()
)
pm10010mrCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLoadGwBank1.setStatus("current")
_Pm10010mrCtrlLoadGwBank2_Type = EkiOnOff
_Pm10010mrCtrlLoadGwBank2_Object = MibScalar
pm10010mrCtrlLoadGwBank2 = _Pm10010mrCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 6, 6),
    _Pm10010mrCtrlLoadGwBank2_Type()
)
pm10010mrCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLoadGwBank2.setStatus("current")
_Pm10010mrCtrlLoadGwBank3_Type = EkiOnOff
_Pm10010mrCtrlLoadGwBank3_Object = MibScalar
pm10010mrCtrlLoadGwBank3 = _Pm10010mrCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 6, 7),
    _Pm10010mrCtrlLoadGwBank3_Type()
)
pm10010mrCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLoadGwBank3.setStatus("current")
_Pm10010mrCtrlLoadGwBank4_Type = EkiOnOff
_Pm10010mrCtrlLoadGwBank4_Object = MibScalar
pm10010mrCtrlLoadGwBank4 = _Pm10010mrCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 6, 8),
    _Pm10010mrCtrlLoadGwBank4_Type()
)
pm10010mrCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLoadGwBank4.setStatus("current")
_Pm10010mrCtrlledTest_ObjectIdentity = ObjectIdentity
pm10010mrCtrlledTest = _Pm10010mrCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 192)
)
_Pm10010mrCtrlGreenLed_Type = EkiOnOff
_Pm10010mrCtrlGreenLed_Object = MibScalar
pm10010mrCtrlGreenLed = _Pm10010mrCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 192, 1),
    _Pm10010mrCtrlGreenLed_Type()
)
pm10010mrCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlGreenLed.setStatus("current")
_Pm10010mrCtrlRedLed_Type = EkiOnOff
_Pm10010mrCtrlRedLed_Object = MibScalar
pm10010mrCtrlRedLed = _Pm10010mrCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 192, 2),
    _Pm10010mrCtrlRedLed_Type()
)
pm10010mrCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlRedLed.setStatus("current")
_Pm10010mrCtrlLedOff_Type = EkiOnOff
_Pm10010mrCtrlLedOff_Object = MibScalar
pm10010mrCtrlLedOff = _Pm10010mrCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 192, 3),
    _Pm10010mrCtrlLedOff_Type()
)
pm10010mrCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlLedOff.setStatus("current")
_Pm10010mrCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm10010mrCtrlinitSwitchMarvell = _Pm10010mrCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 201)
)
_Pm10010mrCtrlInitSwitchMarvell_Type = EkiOnOff
_Pm10010mrCtrlInitSwitchMarvell_Object = MibScalar
pm10010mrCtrlInitSwitchMarvell = _Pm10010mrCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 201, 1),
    _Pm10010mrCtrlInitSwitchMarvell_Type()
)
pm10010mrCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlInitSwitchMarvell.setStatus("current")
_Pm10010mrCtrlresetCount_ObjectIdentity = ObjectIdentity
pm10010mrCtrlresetCount = _Pm10010mrCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 259)
)
_Pm10010mrCtrlResetcount_Type = EkiOnOff
_Pm10010mrCtrlResetcount_Object = MibScalar
pm10010mrCtrlResetcount = _Pm10010mrCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 259, 1),
    _Pm10010mrCtrlResetcount_Type()
)
pm10010mrCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlResetcount.setStatus("current")
_Pm10010mrCtrlresetRmon_ObjectIdentity = ObjectIdentity
pm10010mrCtrlresetRmon = _Pm10010mrCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 260)
)
_Pm10010mrCtrlResetrmon_Type = EkiOnOff
_Pm10010mrCtrlResetrmon_Object = MibScalar
pm10010mrCtrlResetrmon = _Pm10010mrCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 260, 1),
    _Pm10010mrCtrlResetrmon_Type()
)
pm10010mrCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlResetrmon.setStatus("current")
_Pm10010mrCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm10010mrCtrlresetMeasurements = _Pm10010mrCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 261)
)
_Pm10010mrCtrlResetmeasurements_Type = EkiOnOff
_Pm10010mrCtrlResetmeasurements_Object = MibScalar
pm10010mrCtrlResetmeasurements = _Pm10010mrCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 1, 261, 1),
    _Pm10010mrCtrlResetmeasurements_Type()
)
pm10010mrCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlResetmeasurements.setStatus("current")
_Pm10010mrCtrlClient_ObjectIdentity = ObjectIdentity
pm10010mrCtrlClient = _Pm10010mrCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2)
)
_Pm10010mrCtrlaccessLoopTable_Object = MibTable
pm10010mrCtrlaccessLoopTable = _Pm10010mrCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlaccessLoopTable.setStatus("current")
_Pm10010mrCtrlaccessLoopEntry_Object = MibTableRow
pm10010mrCtrlaccessLoopEntry = _Pm10010mrCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 16, 1)
)
pm10010mrCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlaccessLoopEntry.setStatus("current")


class _Pm10010mrCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm10010mrCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlaccessLoopIndex_Object = MibTableColumn
pm10010mrCtrlaccessLoopIndex = _Pm10010mrCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 16, 1, 1),
    _Pm10010mrCtrlaccessLoopIndex_Type()
)
pm10010mrCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlaccessLoopIndex.setStatus("current")
_Pm10010mrCtrlaccessLoopPortn_Type = EkiState
_Pm10010mrCtrlaccessLoopPortn_Object = MibTableColumn
pm10010mrCtrlaccessLoopPortn = _Pm10010mrCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 16, 1, 2),
    _Pm10010mrCtrlaccessLoopPortn_Type()
)
pm10010mrCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlaccessLoopPortn.setStatus("current")
_Pm10010mrCtrlclientLoopToLineTable_Object = MibTable
pm10010mrCtrlclientLoopToLineTable = _Pm10010mrCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlclientLoopToLineTable.setStatus("current")
_Pm10010mrCtrlclientLoopToLineEntry_Object = MibTableRow
pm10010mrCtrlclientLoopToLineEntry = _Pm10010mrCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 17, 1)
)
pm10010mrCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlclientLoopToLineEntry.setStatus("current")


class _Pm10010mrCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm10010mrCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlclientLoopToLineIndex_Object = MibTableColumn
pm10010mrCtrlclientLoopToLineIndex = _Pm10010mrCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 17, 1, 1),
    _Pm10010mrCtrlclientLoopToLineIndex_Type()
)
pm10010mrCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlclientLoopToLineIndex.setStatus("current")
_Pm10010mrCtrlclientLoopToLinePortn_Type = EkiState
_Pm10010mrCtrlclientLoopToLinePortn_Object = MibTableColumn
pm10010mrCtrlclientLoopToLinePortn = _Pm10010mrCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 17, 1, 2),
    _Pm10010mrCtrlclientLoopToLinePortn_Type()
)
pm10010mrCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlclientLoopToLinePortn.setStatus("current")
_Pm10010mrCtrlcsfUpInsTable_Object = MibTable
pm10010mrCtrlcsfUpInsTable = _Pm10010mrCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlcsfUpInsTable.setStatus("current")
_Pm10010mrCtrlcsfUpInsEntry_Object = MibTableRow
pm10010mrCtrlcsfUpInsEntry = _Pm10010mrCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 21, 1)
)
pm10010mrCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlcsfUpInsEntry.setStatus("current")


class _Pm10010mrCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm10010mrCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlcsfUpInsIndex_Object = MibTableColumn
pm10010mrCtrlcsfUpInsIndex = _Pm10010mrCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 21, 1, 1),
    _Pm10010mrCtrlcsfUpInsIndex_Type()
)
pm10010mrCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlcsfUpInsIndex.setStatus("current")
_Pm10010mrCtrlcsfUpInsPortn_Type = EkiState
_Pm10010mrCtrlcsfUpInsPortn_Object = MibTableColumn
pm10010mrCtrlcsfUpInsPortn = _Pm10010mrCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 21, 1, 2),
    _Pm10010mrCtrlcsfUpInsPortn_Type()
)
pm10010mrCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlcsfUpInsPortn.setStatus("current")
_Pm10010mrCtrlcaisDwInsTable_Object = MibTable
pm10010mrCtrlcaisDwInsTable = _Pm10010mrCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlcaisDwInsTable.setStatus("current")
_Pm10010mrCtrlcaisDwInsEntry_Object = MibTableRow
pm10010mrCtrlcaisDwInsEntry = _Pm10010mrCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 22, 1)
)
pm10010mrCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlcaisDwInsEntry.setStatus("current")


class _Pm10010mrCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm10010mrCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlcaisDwInsIndex_Object = MibTableColumn
pm10010mrCtrlcaisDwInsIndex = _Pm10010mrCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 22, 1, 1),
    _Pm10010mrCtrlcaisDwInsIndex_Type()
)
pm10010mrCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlcaisDwInsIndex.setStatus("current")
_Pm10010mrCtrlcaisDwInsPortn_Type = EkiState
_Pm10010mrCtrlcaisDwInsPortn_Object = MibTableColumn
pm10010mrCtrlcaisDwInsPortn = _Pm10010mrCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 2, 22, 1, 2),
    _Pm10010mrCtrlcaisDwInsPortn_Type()
)
pm10010mrCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlcaisDwInsPortn.setStatus("current")
_Pm10010mrCtrlLine_ObjectIdentity = ObjectIdentity
pm10010mrCtrlLine = _Pm10010mrCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3)
)
_Pm10010mrCtrlcommAccessLoopTable_Object = MibTable
pm10010mrCtrlcommAccessLoopTable = _Pm10010mrCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlcommAccessLoopTable.setStatus("current")
_Pm10010mrCtrlcommAccessLoopEntry_Object = MibTableRow
pm10010mrCtrlcommAccessLoopEntry = _Pm10010mrCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 64, 1)
)
pm10010mrCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlcommAccessLoopEntry.setStatus("current")


class _Pm10010mrCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm10010mrCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlcommAccessLoopIndex_Object = MibTableColumn
pm10010mrCtrlcommAccessLoopIndex = _Pm10010mrCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 64, 1, 1),
    _Pm10010mrCtrlcommAccessLoopIndex_Type()
)
pm10010mrCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlcommAccessLoopIndex.setStatus("current")
_Pm10010mrCtrlcommAccessLoopPortn_Type = EkiState
_Pm10010mrCtrlcommAccessLoopPortn_Object = MibTableColumn
pm10010mrCtrlcommAccessLoopPortn = _Pm10010mrCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 64, 1, 2),
    _Pm10010mrCtrlcommAccessLoopPortn_Type()
)
pm10010mrCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlcommAccessLoopPortn.setStatus("current")
_Pm10010mrCtrllineLoopTable_Object = MibTable
pm10010mrCtrllineLoopTable = _Pm10010mrCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm10010mrCtrllineLoopTable.setStatus("current")
_Pm10010mrCtrllineLoopEntry_Object = MibTableRow
pm10010mrCtrllineLoopEntry = _Pm10010mrCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 66, 1)
)
pm10010mrCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrllineLoopEntry.setStatus("current")


class _Pm10010mrCtrllineLoopIndex_Type(Integer32):
    """Custom type pm10010mrCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrllineLoopIndex_Object = MibTableColumn
pm10010mrCtrllineLoopIndex = _Pm10010mrCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 66, 1, 1),
    _Pm10010mrCtrllineLoopIndex_Type()
)
pm10010mrCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrllineLoopIndex.setStatus("current")
_Pm10010mrCtrllineLoopPortn_Type = EkiState
_Pm10010mrCtrllineLoopPortn_Object = MibTableColumn
pm10010mrCtrllineLoopPortn = _Pm10010mrCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 66, 1, 2),
    _Pm10010mrCtrllineLoopPortn_Type()
)
pm10010mrCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrllineLoopPortn.setStatus("current")
_Pm10010mrCtrlfecDisableTable_Object = MibTable
pm10010mrCtrlfecDisableTable = _Pm10010mrCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlfecDisableTable.setStatus("current")
_Pm10010mrCtrlfecDisableEntry_Object = MibTableRow
pm10010mrCtrlfecDisableEntry = _Pm10010mrCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 69, 1)
)
pm10010mrCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlfecDisableEntry.setStatus("current")


class _Pm10010mrCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm10010mrCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlfecDisableIndex_Object = MibTableColumn
pm10010mrCtrlfecDisableIndex = _Pm10010mrCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 69, 1, 1),
    _Pm10010mrCtrlfecDisableIndex_Type()
)
pm10010mrCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlfecDisableIndex.setStatus("current")
_Pm10010mrCtrlfecDisablePortn_Type = EkiState
_Pm10010mrCtrlfecDisablePortn_Object = MibTableColumn
pm10010mrCtrlfecDisablePortn = _Pm10010mrCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 69, 1, 2),
    _Pm10010mrCtrlfecDisablePortn_Type()
)
pm10010mrCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlfecDisablePortn.setStatus("current")
_Pm10010mrCtrlmsaLineLoopTable_Object = MibTable
pm10010mrCtrlmsaLineLoopTable = _Pm10010mrCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaLineLoopTable.setStatus("current")
_Pm10010mrCtrlmsaLineLoopEntry_Object = MibTableRow
pm10010mrCtrlmsaLineLoopEntry = _Pm10010mrCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 209, 1)
)
pm10010mrCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaLineLoopEntry.setStatus("current")


class _Pm10010mrCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm10010mrCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlmsaLineLoopIndex_Object = MibTableColumn
pm10010mrCtrlmsaLineLoopIndex = _Pm10010mrCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 209, 1, 1),
    _Pm10010mrCtrlmsaLineLoopIndex_Type()
)
pm10010mrCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaLineLoopIndex.setStatus("current")
_Pm10010mrCtrlmsaLineLoopPortn_Type = EkiState
_Pm10010mrCtrlmsaLineLoopPortn_Object = MibTableColumn
pm10010mrCtrlmsaLineLoopPortn = _Pm10010mrCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 209, 1, 2),
    _Pm10010mrCtrlmsaLineLoopPortn_Type()
)
pm10010mrCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaLineLoopPortn.setStatus("current")
_Pm10010mrCtrlmsaTxResetTable_Object = MibTable
pm10010mrCtrlmsaTxResetTable = _Pm10010mrCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaTxResetTable.setStatus("current")
_Pm10010mrCtrlmsaTxResetEntry_Object = MibTableRow
pm10010mrCtrlmsaTxResetEntry = _Pm10010mrCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 210, 1)
)
pm10010mrCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaTxResetEntry.setStatus("current")


class _Pm10010mrCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm10010mrCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlmsaTxResetIndex_Object = MibTableColumn
pm10010mrCtrlmsaTxResetIndex = _Pm10010mrCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 210, 1, 1),
    _Pm10010mrCtrlmsaTxResetIndex_Type()
)
pm10010mrCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaTxResetIndex.setStatus("current")
_Pm10010mrCtrlmsaTxResetPortn_Type = EkiState
_Pm10010mrCtrlmsaTxResetPortn_Object = MibTableColumn
pm10010mrCtrlmsaTxResetPortn = _Pm10010mrCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 210, 1, 2),
    _Pm10010mrCtrlmsaTxResetPortn_Type()
)
pm10010mrCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaTxResetPortn.setStatus("current")
_Pm10010mrCtrlmsaRxResetTable_Object = MibTable
pm10010mrCtrlmsaRxResetTable = _Pm10010mrCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaRxResetTable.setStatus("current")
_Pm10010mrCtrlmsaRxResetEntry_Object = MibTableRow
pm10010mrCtrlmsaRxResetEntry = _Pm10010mrCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 211, 1)
)
pm10010mrCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaRxResetEntry.setStatus("current")


class _Pm10010mrCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm10010mrCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlmsaRxResetIndex_Object = MibTableColumn
pm10010mrCtrlmsaRxResetIndex = _Pm10010mrCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 211, 1, 1),
    _Pm10010mrCtrlmsaRxResetIndex_Type()
)
pm10010mrCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaRxResetIndex.setStatus("current")
_Pm10010mrCtrlmsaRxResetPortn_Type = EkiState
_Pm10010mrCtrlmsaRxResetPortn_Object = MibTableColumn
pm10010mrCtrlmsaRxResetPortn = _Pm10010mrCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 211, 1, 2),
    _Pm10010mrCtrlmsaRxResetPortn_Type()
)
pm10010mrCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaRxResetPortn.setStatus("current")
_Pm10010mrCtrlmsaShutdownTable_Object = MibTable
pm10010mrCtrlmsaShutdownTable = _Pm10010mrCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaShutdownTable.setStatus("current")
_Pm10010mrCtrlmsaShutdownEntry_Object = MibTableRow
pm10010mrCtrlmsaShutdownEntry = _Pm10010mrCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 212, 1)
)
pm10010mrCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaShutdownEntry.setStatus("current")


class _Pm10010mrCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm10010mrCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm10010mrCtrlmsaShutdownIndex_Object = MibTableColumn
pm10010mrCtrlmsaShutdownIndex = _Pm10010mrCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 212, 1, 1),
    _Pm10010mrCtrlmsaShutdownIndex_Type()
)
pm10010mrCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaShutdownIndex.setStatus("current")
_Pm10010mrCtrlmsaShutdownPortn_Type = EkiState
_Pm10010mrCtrlmsaShutdownPortn_Object = MibTableColumn
pm10010mrCtrlmsaShutdownPortn = _Pm10010mrCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 6, 3, 212, 1, 2),
    _Pm10010mrCtrlmsaShutdownPortn_Type()
)
pm10010mrCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCtrlmsaShutdownPortn.setStatus("current")
_Pm10010mrri_ObjectIdentity = ObjectIdentity
pm10010mrri = _Pm10010mrri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7)
)
_Pm10010mrriTable_ObjectIdentity = ObjectIdentity
pm10010mrriTable = _Pm10010mrriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1)
)
_Pm10010mrRinvSfpTable_Object = MibTable
pm10010mrRinvSfpTable = _Pm10010mrRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010mrRinvSfpTable.setStatus("current")
_Pm10010mrRinvSfpEntry_Object = MibTableRow
pm10010mrRinvSfpEntry = _Pm10010mrRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 1, 1)
)
pm10010mrRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrRinvSfpEntry.setStatus("current")


class _Pm10010mrRinvSfpIndex_Type(Integer32):
    """Custom type pm10010mrRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010mrRinvSfpIndex_Type.__name__ = "Integer32"
_Pm10010mrRinvSfpIndex_Object = MibTableColumn
pm10010mrRinvSfpIndex = _Pm10010mrRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 1, 1, 1),
    _Pm10010mrRinvSfpIndex_Type()
)
pm10010mrRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvSfpIndex.setStatus("current")
_Pm10010mrRinvsfp_Type = DisplayString
_Pm10010mrRinvsfp_Object = MibTableColumn
pm10010mrRinvsfp = _Pm10010mrRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 1, 1, 2),
    _Pm10010mrRinvsfp_Type()
)
pm10010mrRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvsfp.setStatus("current")
_Pm10010mrRinvLineTable_Object = MibTable
pm10010mrRinvLineTable = _Pm10010mrRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm10010mrRinvLineTable.setStatus("current")
_Pm10010mrRinvLineEntry_Object = MibTableRow
pm10010mrRinvLineEntry = _Pm10010mrRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 2, 1)
)
pm10010mrRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrRinvLineEntry.setStatus("current")


class _Pm10010mrRinvLineIndex_Type(Integer32):
    """Custom type pm10010mrRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010mrRinvLineIndex_Type.__name__ = "Integer32"
_Pm10010mrRinvLineIndex_Object = MibTableColumn
pm10010mrRinvLineIndex = _Pm10010mrRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 2, 1, 1),
    _Pm10010mrRinvLineIndex_Type()
)
pm10010mrRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvLineIndex.setStatus("current")
_Pm10010mrRinvxfpLine_Type = DisplayString
_Pm10010mrRinvxfpLine_Object = MibTableColumn
pm10010mrRinvxfpLine = _Pm10010mrRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 1, 2, 1, 2),
    _Pm10010mrRinvxfpLine_Type()
)
pm10010mrRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvxfpLine.setStatus("current")
_Pm10010mrRinvReloadInventory_Type = EkiOnOff
_Pm10010mrRinvReloadInventory_Object = MibScalar
pm10010mrRinvReloadInventory = _Pm10010mrRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 2),
    _Pm10010mrRinvReloadInventory_Type()
)
pm10010mrRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrRinvReloadInventory.setStatus("current")
_Pm10010mrRinvHwPlatform_Type = DisplayString
_Pm10010mrRinvHwPlatform_Object = MibScalar
pm10010mrRinvHwPlatform = _Pm10010mrRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 3),
    _Pm10010mrRinvHwPlatform_Type()
)
pm10010mrRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvHwPlatform.setStatus("current")
_Pm10010mrRinvModulePlatform_Type = DisplayString
_Pm10010mrRinvModulePlatform_Object = MibScalar
pm10010mrRinvModulePlatform = _Pm10010mrRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 4),
    _Pm10010mrRinvModulePlatform_Type()
)
pm10010mrRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvModulePlatform.setStatus("current")
_Pm10010mrRinvSwPlatform_Type = DisplayString
_Pm10010mrRinvSwPlatform_Object = MibScalar
pm10010mrRinvSwPlatform = _Pm10010mrRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 5),
    _Pm10010mrRinvSwPlatform_Type()
)
pm10010mrRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvSwPlatform.setStatus("current")
_Pm10010mrRinvGwPlatform_Type = DisplayString
_Pm10010mrRinvGwPlatform_Object = MibScalar
pm10010mrRinvGwPlatform = _Pm10010mrRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 7, 6),
    _Pm10010mrRinvGwPlatform_Type()
)
pm10010mrRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrRinvGwPlatform.setStatus("current")
_Pm10010mrdownload_ObjectIdentity = ObjectIdentity
pm10010mrdownload = _Pm10010mrdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8)
)
_Pm10010mrDwlOther_ObjectIdentity = ObjectIdentity
pm10010mrDwlOther = _Pm10010mrDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1)
)
_Pm10010mrDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm10010mrDwlrestartProcess = _Pm10010mrDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 0)
)
_Pm10010mrDwlWarmRestartProcessed_Type = EkiOnOff
_Pm10010mrDwlWarmRestartProcessed_Object = MibScalar
pm10010mrDwlWarmRestartProcessed = _Pm10010mrDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 0, 1),
    _Pm10010mrDwlWarmRestartProcessed_Type()
)
pm10010mrDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlWarmRestartProcessed.setStatus("current")
_Pm10010mrDwlColdRestartProcessed_Type = EkiOnOff
_Pm10010mrDwlColdRestartProcessed_Object = MibScalar
pm10010mrDwlColdRestartProcessed = _Pm10010mrDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 0, 2),
    _Pm10010mrDwlColdRestartProcessed_Type()
)
pm10010mrDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlColdRestartProcessed.setStatus("current")
_Pm10010mrDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm10010mrDwlswBanksUsed = _Pm10010mrDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 1)
)
_Pm10010mrDwlSwBank1Used_Type = EkiOnOff
_Pm10010mrDwlSwBank1Used_Object = MibScalar
pm10010mrDwlSwBank1Used = _Pm10010mrDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 1, 1),
    _Pm10010mrDwlSwBank1Used_Type()
)
pm10010mrDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlSwBank1Used.setStatus("current")
_Pm10010mrDwlSwBank2Used_Type = EkiOnOff
_Pm10010mrDwlSwBank2Used_Object = MibScalar
pm10010mrDwlSwBank2Used = _Pm10010mrDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 1, 2),
    _Pm10010mrDwlSwBank2Used_Type()
)
pm10010mrDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlSwBank2Used.setStatus("current")
_Pm10010mrDwlSwBank1Notempty_Type = EkiOnOff
_Pm10010mrDwlSwBank1Notempty_Object = MibScalar
pm10010mrDwlSwBank1Notempty = _Pm10010mrDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 1, 5),
    _Pm10010mrDwlSwBank1Notempty_Type()
)
pm10010mrDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlSwBank1Notempty.setStatus("current")
_Pm10010mrDwlSwBank2Notempty_Type = EkiOnOff
_Pm10010mrDwlSwBank2Notempty_Object = MibScalar
pm10010mrDwlSwBank2Notempty = _Pm10010mrDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 1, 6),
    _Pm10010mrDwlSwBank2Notempty_Type()
)
pm10010mrDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlSwBank2Notempty.setStatus("current")
_Pm10010mrDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm10010mrDwlgwBanksUsed = _Pm10010mrDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2)
)
_Pm10010mrDwlGwBank1Used_Type = EkiOnOff
_Pm10010mrDwlGwBank1Used_Object = MibScalar
pm10010mrDwlGwBank1Used = _Pm10010mrDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 1),
    _Pm10010mrDwlGwBank1Used_Type()
)
pm10010mrDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank1Used.setStatus("current")
_Pm10010mrDwlGwBank2Used_Type = EkiOnOff
_Pm10010mrDwlGwBank2Used_Object = MibScalar
pm10010mrDwlGwBank2Used = _Pm10010mrDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 2),
    _Pm10010mrDwlGwBank2Used_Type()
)
pm10010mrDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank2Used.setStatus("current")
_Pm10010mrDwlGwBank3Used_Type = EkiOnOff
_Pm10010mrDwlGwBank3Used_Object = MibScalar
pm10010mrDwlGwBank3Used = _Pm10010mrDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 3),
    _Pm10010mrDwlGwBank3Used_Type()
)
pm10010mrDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank3Used.setStatus("current")
_Pm10010mrDwlGwBank4Used_Type = EkiOnOff
_Pm10010mrDwlGwBank4Used_Object = MibScalar
pm10010mrDwlGwBank4Used = _Pm10010mrDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 4),
    _Pm10010mrDwlGwBank4Used_Type()
)
pm10010mrDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank4Used.setStatus("current")
_Pm10010mrDwlGwBank1Notempty_Type = EkiOnOff
_Pm10010mrDwlGwBank1Notempty_Object = MibScalar
pm10010mrDwlGwBank1Notempty = _Pm10010mrDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 5),
    _Pm10010mrDwlGwBank1Notempty_Type()
)
pm10010mrDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank1Notempty.setStatus("current")
_Pm10010mrDwlGwBank2Notempty_Type = EkiOnOff
_Pm10010mrDwlGwBank2Notempty_Object = MibScalar
pm10010mrDwlGwBank2Notempty = _Pm10010mrDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 6),
    _Pm10010mrDwlGwBank2Notempty_Type()
)
pm10010mrDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank2Notempty.setStatus("current")
_Pm10010mrDwlGwBank3Notempty_Type = EkiOnOff
_Pm10010mrDwlGwBank3Notempty_Object = MibScalar
pm10010mrDwlGwBank3Notempty = _Pm10010mrDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 7),
    _Pm10010mrDwlGwBank3Notempty_Type()
)
pm10010mrDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank3Notempty.setStatus("current")
_Pm10010mrDwlGwBank4Notempty_Type = EkiOnOff
_Pm10010mrDwlGwBank4Notempty_Object = MibScalar
pm10010mrDwlGwBank4Notempty = _Pm10010mrDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 1, 2, 8),
    _Pm10010mrDwlGwBank4Notempty_Type()
)
pm10010mrDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrDwlGwBank4Notempty.setStatus("current")
_Pm10010mrDwlClient_ObjectIdentity = ObjectIdentity
pm10010mrDwlClient = _Pm10010mrDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 2)
)
_Pm10010mrDwlLine_ObjectIdentity = ObjectIdentity
pm10010mrDwlLine = _Pm10010mrDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 8, 3)
)
_Pm10010mrConfig_ObjectIdentity = ObjectIdentity
pm10010mrConfig = _Pm10010mrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9)
)
_Pm10010mrCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm10010mrCfgAccessCAisCsf = _Pm10010mrCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 1)
)
_Pm10010mrCfgClientcaiscsfTable_Object = MibTable
pm10010mrCfgClientcaiscsfTable = _Pm10010mrCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010mrCfgClientcaiscsfTable.setStatus("current")
_Pm10010mrCfgClientcaiscsfEntry_Object = MibTableRow
pm10010mrCfgClientcaiscsfEntry = _Pm10010mrCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 1, 1, 1)
)
pm10010mrCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgClientcaiscsfEntry.setStatus("current")


class _Pm10010mrCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm10010mrCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgClientcaiscsfIndex_Object = MibTableColumn
pm10010mrCfgClientcaiscsfIndex = _Pm10010mrCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 1, 1, 1, 1),
    _Pm10010mrCfgClientcaiscsfIndex_Type()
)
pm10010mrCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgClientcaiscsfIndex.setStatus("current")


class _Pm10010mrCfgReservePortn_Type(Unsigned32):
    """Custom type pm10010mrCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgReservePortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgReservePortn_Object = MibTableColumn
pm10010mrCfgReservePortn = _Pm10010mrCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 1, 1, 1, 3),
    _Pm10010mrCfgReservePortn_Type()
)
pm10010mrCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgReservePortn.setStatus("current")
_Pm10010mrCfgStartup_ObjectIdentity = ObjectIdentity
pm10010mrCfgStartup = _Pm10010mrCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2)
)
_Pm10010mrCfgClientStartupTable_Object = MibTable
pm10010mrCfgClientStartupTable = _Pm10010mrCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm10010mrCfgClientStartupTable.setStatus("current")
_Pm10010mrCfgClientStartupEntry_Object = MibTableRow
pm10010mrCfgClientStartupEntry = _Pm10010mrCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1, 1)
)
pm10010mrCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgClientStartupEntry.setStatus("current")


class _Pm10010mrCfgClientStartupIndex_Type(Integer32):
    """Custom type pm10010mrCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgClientStartupIndex_Object = MibTableColumn
pm10010mrCfgClientStartupIndex = _Pm10010mrCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1, 1, 1),
    _Pm10010mrCfgClientStartupIndex_Type()
)
pm10010mrCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgClientStartupIndex.setStatus("current")


class _Pm10010mrCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgSystConfPortPortn_Object = MibTableColumn
pm10010mrCfgSystConfPortPortn = _Pm10010mrCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1, 1, 3),
    _Pm10010mrCfgSystConfPortPortn_Type()
)
pm10010mrCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgSystConfPortPortn.setStatus("current")


class _Pm10010mrCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgNetConfPortPortn_Object = MibTableColumn
pm10010mrCfgNetConfPortPortn = _Pm10010mrCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1, 1, 4),
    _Pm10010mrCfgNetConfPortPortn_Type()
)
pm10010mrCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgNetConfPortPortn.setStatus("current")


class _Pm10010mrCfgIgnoreTimePortn_Type(Unsigned32):
    """Custom type pm10010mrCfgIgnoreTimePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgIgnoreTimePortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgIgnoreTimePortn_Object = MibTableColumn
pm10010mrCfgIgnoreTimePortn = _Pm10010mrCfgIgnoreTimePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1, 1, 6),
    _Pm10010mrCfgIgnoreTimePortn_Type()
)
pm10010mrCfgIgnoreTimePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgIgnoreTimePortn.setStatus("current")


class _Pm10010mrCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgOptionsPortPortn_Object = MibTableColumn
pm10010mrCfgOptionsPortPortn = _Pm10010mrCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 1, 1, 14),
    _Pm10010mrCfgOptionsPortPortn_Type()
)
pm10010mrCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgOptionsPortPortn.setStatus("current")
_Pm10010mrCfgLineStartupTable_Object = MibTable
pm10010mrCfgLineStartupTable = _Pm10010mrCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm10010mrCfgLineStartupTable.setStatus("current")
_Pm10010mrCfgLineStartupEntry_Object = MibTableRow
pm10010mrCfgLineStartupEntry = _Pm10010mrCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 2, 1)
)
pm10010mrCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgLineStartupEntry.setStatus("current")


class _Pm10010mrCfgLineStartupIndex_Type(Integer32):
    """Custom type pm10010mrCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgLineStartupIndex_Object = MibTableColumn
pm10010mrCfgLineStartupIndex = _Pm10010mrCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 2, 1, 1),
    _Pm10010mrCfgLineStartupIndex_Type()
)
pm10010mrCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgLineStartupIndex.setStatus("current")


class _Pm10010mrCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm10010mrCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgSystConfLinePortn_Object = MibTableColumn
pm10010mrCfgSystConfLinePortn = _Pm10010mrCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 2, 1, 3),
    _Pm10010mrCfgSystConfLinePortn_Type()
)
pm10010mrCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgSystConfLinePortn.setStatus("current")


class _Pm10010mrCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm10010mrCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgOptionsLinePortn_Object = MibTableColumn
pm10010mrCfgOptionsLinePortn = _Pm10010mrCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 2, 1, 14),
    _Pm10010mrCfgOptionsLinePortn_Type()
)
pm10010mrCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgOptionsLinePortn.setStatus("current")
_Pm10010mrCfgXfpTable_Object = MibTable
pm10010mrCfgXfpTable = _Pm10010mrCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm10010mrCfgXfpTable.setStatus("current")
_Pm10010mrCfgXfpEntry_Object = MibTableRow
pm10010mrCfgXfpEntry = _Pm10010mrCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 3, 1)
)
pm10010mrCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgXfpEntry.setStatus("current")


class _Pm10010mrCfgXfpIndex_Type(Integer32):
    """Custom type pm10010mrCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgXfpIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgXfpIndex_Object = MibTableColumn
pm10010mrCfgXfpIndex = _Pm10010mrCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 3, 1, 1),
    _Pm10010mrCfgXfpIndex_Type()
)
pm10010mrCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgXfpIndex.setStatus("current")


class _Pm10010mrCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm10010mrCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgSystConfMsaLinePortn_Object = MibTableColumn
pm10010mrCfgSystConfMsaLinePortn = _Pm10010mrCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 2, 3, 1, 3),
    _Pm10010mrCfgSystConfMsaLinePortn_Type()
)
pm10010mrCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgSystConfMsaLinePortn.setStatus("current")
_Pm10010mrCfgLabels_ObjectIdentity = ObjectIdentity
pm10010mrCfgLabels = _Pm10010mrCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3)
)
_Pm10010mrCfgLabelclientTable_Object = MibTable
pm10010mrCfgLabelclientTable = _Pm10010mrCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm10010mrCfgLabelclientTable.setStatus("current")
_Pm10010mrCfgLabelclientEntry_Object = MibTableRow
pm10010mrCfgLabelclientEntry = _Pm10010mrCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 1, 1)
)
pm10010mrCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgLabelclientEntry.setStatus("current")


class _Pm10010mrCfgLabelclientIndex_Type(Integer32):
    """Custom type pm10010mrCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgLabelclientIndex_Object = MibTableColumn
pm10010mrCfgLabelclientIndex = _Pm10010mrCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 1, 1, 1),
    _Pm10010mrCfgLabelclientIndex_Type()
)
pm10010mrCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgLabelclientIndex.setStatus("current")


class _Pm10010mrCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm10010mrCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010mrCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm10010mrCfgLabelclientPortn_Object = MibTableColumn
pm10010mrCfgLabelclientPortn = _Pm10010mrCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 1, 1, 3),
    _Pm10010mrCfgLabelclientPortn_Type()
)
pm10010mrCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgLabelclientPortn.setStatus("current")
_Pm10010mrCfgLabellineTable_Object = MibTable
pm10010mrCfgLabellineTable = _Pm10010mrCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm10010mrCfgLabellineTable.setStatus("current")
_Pm10010mrCfgLabellineEntry_Object = MibTableRow
pm10010mrCfgLabellineEntry = _Pm10010mrCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 2, 1)
)
pm10010mrCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgLabellineEntry.setStatus("current")


class _Pm10010mrCfgLabellineIndex_Type(Integer32):
    """Custom type pm10010mrCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgLabellineIndex_Object = MibTableColumn
pm10010mrCfgLabellineIndex = _Pm10010mrCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 2, 1, 1),
    _Pm10010mrCfgLabellineIndex_Type()
)
pm10010mrCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgLabellineIndex.setStatus("current")


class _Pm10010mrCfgLabellinePortn_Type(DisplayString):
    """Custom type pm10010mrCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010mrCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm10010mrCfgLabellinePortn_Object = MibTableColumn
pm10010mrCfgLabellinePortn = _Pm10010mrCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 3, 2, 1, 3),
    _Pm10010mrCfgLabellinePortn_Type()
)
pm10010mrCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgLabellinePortn.setStatus("current")
_Pm10010mrCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm10010mrCfgStartuptlh = _Pm10010mrCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4)
)
_Pm10010mrCfgOtxtlhTable_Object = MibTable
pm10010mrCfgOtxtlhTable = _Pm10010mrCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm10010mrCfgOtxtlhTable.setStatus("current")
_Pm10010mrCfgOtxtlhEntry_Object = MibTableRow
pm10010mrCfgOtxtlhEntry = _Pm10010mrCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1)
)
pm10010mrCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgOtxtlhEntry.setStatus("current")


class _Pm10010mrCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm10010mrCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgOtxtlhIndex_Object = MibTableColumn
pm10010mrCfgOtxtlhIndex = _Pm10010mrCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1, 1),
    _Pm10010mrCfgOtxtlhIndex_Type()
)
pm10010mrCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgOtxtlhIndex.setStatus("current")


class _Pm10010mrCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgLinePwrLaserPortn_Object = MibTableColumn
pm10010mrCfgLinePwrLaserPortn = _Pm10010mrCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1, 6),
    _Pm10010mrCfgLinePwrLaserPortn_Type()
)
pm10010mrCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgLinePwrLaserPortn.setStatus("current")


class _Pm10010mrCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgLineFCurrentPortn_Object = MibTableColumn
pm10010mrCfgLineFCurrentPortn = _Pm10010mrCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1, 7),
    _Pm10010mrCfgLineFCurrentPortn_Type()
)
pm10010mrCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgLineFCurrentPortn.setStatus("current")


class _Pm10010mrCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgLineGridCurrentPortn_Object = MibTableColumn
pm10010mrCfgLineGridCurrentPortn = _Pm10010mrCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1, 8),
    _Pm10010mrCfgLineGridCurrentPortn_Type()
)
pm10010mrCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgLineGridCurrentPortn.setStatus("current")


class _Pm10010mrCfgFPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgFPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgFPortn_Object = MibTableColumn
pm10010mrCfgFPortn = _Pm10010mrCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1, 9),
    _Pm10010mrCfgFPortn_Type()
)
pm10010mrCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgFPortn.setStatus("current")


class _Pm10010mrCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgRxLineFCurrentPortn_Object = MibTableColumn
pm10010mrCfgRxLineFCurrentPortn = _Pm10010mrCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 4, 1, 1, 10),
    _Pm10010mrCfgRxLineFCurrentPortn_Type()
)
pm10010mrCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgRxLineFCurrentPortn.setStatus("current")
_Pm10010mrCfgOther_ObjectIdentity = ObjectIdentity
pm10010mrCfgOther = _Pm10010mrCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 5)
)
_Pm10010mrtablemoduleOther_ObjectIdentity = ObjectIdentity
pm10010mrtablemoduleOther = _Pm10010mrtablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 5, 1)
)


class _Pm10010mrCfgmode_Type(Unsigned32):
    """Custom type pm10010mrCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgmode_Type.__name__ = "Unsigned32"
_Pm10010mrCfgmode_Object = MibScalar
pm10010mrCfgmode = _Pm10010mrCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 5, 1, 2),
    _Pm10010mrCfgmode_Type()
)
pm10010mrCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgmode.setStatus("current")


class _Pm10010mrCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010mrCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010mrCfgfanLowSpeedThreshold_Object = MibScalar
pm10010mrCfgfanLowSpeedThreshold = _Pm10010mrCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 5, 1, 3),
    _Pm10010mrCfgfanLowSpeedThreshold_Type()
)
pm10010mrCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgfanLowSpeedThreshold.setStatus("current")


class _Pm10010mrCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010mrCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010mrCfgfanHighSpeedThreshold_Object = MibScalar
pm10010mrCfgfanHighSpeedThreshold = _Pm10010mrCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 5, 1, 4),
    _Pm10010mrCfgfanHighSpeedThreshold_Type()
)
pm10010mrCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgfanHighSpeedThreshold.setStatus("current")
_Pm10010mrCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm10010mrCfgStartuptablefive = _Pm10010mrCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6)
)
_Pm10010mrCfgOtxtlhcapabilitiesTable_Object = MibTable
pm10010mrCfgOtxtlhcapabilitiesTable = _Pm10010mrCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm10010mrCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm10010mrCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm10010mrCfgOtxtlhcapabilitiesEntry = _Pm10010mrCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1)
)
pm10010mrCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm10010mrCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm10010mrCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm10010mrCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm10010mrCfgOtxtlhcapabilitiesIndex = _Pm10010mrCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1, 1),
    _Pm10010mrCfgOtxtlhcapabilitiesIndex_Type()
)
pm10010mrCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm10010mrCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm10010mrCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgComponentTypePortn_Object = MibTableColumn
pm10010mrCfgComponentTypePortn = _Pm10010mrCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1, 3),
    _Pm10010mrCfgComponentTypePortn_Type()
)
pm10010mrCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgComponentTypePortn.setStatus("current")


class _Pm10010mrCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgMiscellaneousPortn_Object = MibTableColumn
pm10010mrCfgMiscellaneousPortn = _Pm10010mrCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1, 4),
    _Pm10010mrCfgMiscellaneousPortn_Type()
)
pm10010mrCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgMiscellaneousPortn.setStatus("current")


class _Pm10010mrCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgFirstChannelPortn_Object = MibTableColumn
pm10010mrCfgFirstChannelPortn = _Pm10010mrCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1, 5),
    _Pm10010mrCfgFirstChannelPortn_Type()
)
pm10010mrCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgFirstChannelPortn.setStatus("current")


class _Pm10010mrCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgLastChannelPortn_Object = MibTableColumn
pm10010mrCfgLastChannelPortn = _Pm10010mrCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1, 6),
    _Pm10010mrCfgLastChannelPortn_Type()
)
pm10010mrCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgLastChannelPortn.setStatus("current")


class _Pm10010mrCfgGridPortn_Type(Unsigned32):
    """Custom type pm10010mrCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mrCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm10010mrCfgGridPortn_Object = MibTableColumn
pm10010mrCfgGridPortn = _Pm10010mrCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 6, 1, 1, 7),
    _Pm10010mrCfgGridPortn_Type()
)
pm10010mrCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrCfgGridPortn.setStatus("current")
_Pm10010mrCfgWriteConfiguration_Type = EkiOnOff
_Pm10010mrCfgWriteConfiguration_Object = MibScalar
pm10010mrCfgWriteConfiguration = _Pm10010mrCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 9, 257),
    _Pm10010mrCfgWriteConfiguration_Type()
)
pm10010mrCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mrCfgWriteConfiguration.setStatus("current")
_Pm10010mrtraps_ObjectIdentity = ObjectIdentity
pm10010mrtraps = _Pm10010mrtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10)
)


class _Pm10010mrtrapPortNumber_Type(Integer32):
    """Custom type pm10010mrtrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mrtrapPortNumber_Type.__name__ = "Integer32"
_Pm10010mrtrapPortNumber_Object = MibScalar
pm10010mrtrapPortNumber = _Pm10010mrtrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 2),
    _Pm10010mrtrapPortNumber_Type()
)
pm10010mrtrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrtrapPortNumber.setStatus("current")


class _Pm10010mrtrapLineNumber_Type(Integer32):
    """Custom type pm10010mrtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mrtrapLineNumber_Type.__name__ = "Integer32"
_Pm10010mrtrapLineNumber_Object = MibScalar
pm10010mrtrapLineNumber = _Pm10010mrtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 3),
    _Pm10010mrtrapLineNumber_Type()
)
pm10010mrtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrtrapLineNumber.setStatus("current")


class _Pm10010mrtrapBoardNumber_Type(Integer32):
    """Custom type pm10010mrtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mrtrapBoardNumber_Type.__name__ = "Integer32"
_Pm10010mrtrapBoardNumber_Object = MibScalar
pm10010mrtrapBoardNumber = _Pm10010mrtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 4),
    _Pm10010mrtrapBoardNumber_Type()
)
pm10010mrtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrtrapBoardNumber.setStatus("current")
_Pm10010mrMonitoring_ObjectIdentity = ObjectIdentity
pm10010mrMonitoring = _Pm10010mrMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11)
)
_Pm10010mrMonOther_ObjectIdentity = ObjectIdentity
pm10010mrMonOther = _Pm10010mrMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 1)
)
_Pm10010mrMonRmon_ObjectIdentity = ObjectIdentity
pm10010mrMonRmon = _Pm10010mrMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 1, 3)
)
_Pm10010mrMonClient_ObjectIdentity = ObjectIdentity
pm10010mrMonClient = _Pm10010mrMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2)
)
_Pm10010mrMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm10010mrMonClientRmonCounter = _Pm10010mrMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4)
)
_Pm10010mrMonupRmonBytesCounterClientInputTable_Object = MibTable
pm10010mrMonupRmonBytesCounterClientInputTable = _Pm10010mrMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm10010mrMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm10010mrMonupRmonBytesCounterClientInputEntry = _Pm10010mrMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 16, 1)
)
pm10010mrMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm10010mrMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm10010mrMonupRmonBytesCounterClientInputIndex = _Pm10010mrMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 16, 1, 1),
    _Pm10010mrMonupRmonBytesCounterClientInputIndex_Type()
)
pm10010mrMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm10010mrMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMonupRmonBytesCounterClientInputValuePortn = _Pm10010mrMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 16, 1, 2),
    _Pm10010mrMonupRmonBytesCounterClientInputValuePortn_Type()
)
pm10010mrMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMonupRmonBytesCounterClientInputErrorPortn = _Pm10010mrMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 16, 1, 3),
    _Pm10010mrMonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm10010mrMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMonupRmonBytesCounterClientInputOverloadPortn = _Pm10010mrMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 16, 1, 4),
    _Pm10010mrMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm10010mrMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm10010mrMonupRmonCrcErrorsCounterClientInputTable = _Pm10010mrMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm10010mrMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm10010mrMonupRmonCrcErrorsCounterClientInputEntry = _Pm10010mrMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 32, 1)
)
pm10010mrMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm10010mrMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm10010mrMonupRmonCrcErrorsCounterClientInputIndex = _Pm10010mrMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 32, 1, 1),
    _Pm10010mrMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm10010mrMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn = _Pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 32, 1, 2),
    _Pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 32, 1, 3),
    _Pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 32, 1, 4),
    _Pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMonupRmonPacketsCounterClientInputTable_Object = MibTable
pm10010mrMonupRmonPacketsCounterClientInputTable = _Pm10010mrMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm10010mrMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm10010mrMonupRmonPacketsCounterClientInputEntry = _Pm10010mrMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 48, 1)
)
pm10010mrMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm10010mrMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm10010mrMonupRmonPacketsCounterClientInputIndex = _Pm10010mrMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 48, 1, 1),
    _Pm10010mrMonupRmonPacketsCounterClientInputIndex_Type()
)
pm10010mrMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm10010mrMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMonupRmonPacketsCounterClientInputValuePortn = _Pm10010mrMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 48, 1, 2),
    _Pm10010mrMonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm10010mrMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMonupRmonPacketsCounterClientInputErrorPortn = _Pm10010mrMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 48, 1, 3),
    _Pm10010mrMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm10010mrMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn = _Pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 48, 1, 4),
    _Pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm10010mrMonupRmonBroadcastCounterClientInputTable = _Pm10010mrMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm10010mrMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm10010mrMonupRmonBroadcastCounterClientInputEntry = _Pm10010mrMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 64, 1)
)
pm10010mrMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm10010mrMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm10010mrMonupRmonBroadcastCounterClientInputIndex = _Pm10010mrMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 64, 1, 1),
    _Pm10010mrMonupRmonBroadcastCounterClientInputIndex_Type()
)
pm10010mrMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm10010mrMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMonupRmonBroadcastCounterClientInputValuePortn = _Pm10010mrMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 64, 1, 2),
    _Pm10010mrMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm10010mrMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn = _Pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 64, 1, 3),
    _Pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn = _Pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 64, 1, 4),
    _Pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMonupRmonMulticastCounterClientInputTable_Object = MibTable
pm10010mrMonupRmonMulticastCounterClientInputTable = _Pm10010mrMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm10010mrMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm10010mrMonupRmonMulticastCounterClientInputEntry = _Pm10010mrMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 80, 1)
)
pm10010mrMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm10010mrMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm10010mrMonupRmonMulticastCounterClientInputIndex = _Pm10010mrMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 80, 1, 1),
    _Pm10010mrMonupRmonMulticastCounterClientInputIndex_Type()
)
pm10010mrMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm10010mrMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMonupRmonMulticastCounterClientInputValuePortn = _Pm10010mrMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 80, 1, 2),
    _Pm10010mrMonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm10010mrMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMonupRmonMulticastCounterClientInputErrorPortn = _Pm10010mrMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 80, 1, 3),
    _Pm10010mrMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm10010mrMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn = _Pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 80, 1, 4),
    _Pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm10010mrMonupRmonPauseFrameCounterClientInputTable = _Pm10010mrMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm10010mrMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm10010mrMonupRmonPauseFrameCounterClientInputEntry = _Pm10010mrMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 96, 1)
)
pm10010mrMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm10010mrMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm10010mrMonupRmonPauseFrameCounterClientInputIndex = _Pm10010mrMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 96, 1, 1),
    _Pm10010mrMonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm10010mrMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn = _Pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 96, 1, 2),
    _Pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn = _Pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 96, 1, 3),
    _Pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 96, 1, 4),
    _Pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMondwRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm10010mrMondwRmonCrcErrorsCounterClientInputTable = _Pm10010mrMondwRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    pm10010mrMondwRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm10010mrMondwRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm10010mrMondwRmonCrcErrorsCounterClientInputEntry = _Pm10010mrMondwRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 224, 1)
)
pm10010mrMondwRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMondwRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMondwRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm10010mrMondwRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMondwRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMondwRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMondwRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm10010mrMondwRmonCrcErrorsCounterClientInputIndex = _Pm10010mrMondwRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 224, 1, 1),
    _Pm10010mrMondwRmonCrcErrorsCounterClientInputIndex_Type()
)
pm10010mrMondwRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn = _Pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 224, 1, 2),
    _Pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn = _Pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 224, 1, 3),
    _Pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn = _Pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 224, 1, 4),
    _Pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mrMondwRmonPacketsCounterClientInputTable_Object = MibTable
pm10010mrMondwRmonPacketsCounterClientInputTable = _Pm10010mrMondwRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    pm10010mrMondwRmonPacketsCounterClientInputTable.setStatus("current")
_Pm10010mrMondwRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm10010mrMondwRmonPacketsCounterClientInputEntry = _Pm10010mrMondwRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 240, 1)
)
pm10010mrMondwRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mr-MIB", "pm10010mrMondwRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mrMondwRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm10010mrMondwRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mrMondwRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mrMondwRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mrMondwRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm10010mrMondwRmonPacketsCounterClientInputIndex = _Pm10010mrMondwRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 240, 1, 1),
    _Pm10010mrMondwRmonPacketsCounterClientInputIndex_Type()
)
pm10010mrMondwRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm10010mrMondwRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm10010mrMondwRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mrMondwRmonPacketsCounterClientInputValuePortn = _Pm10010mrMondwRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 240, 1, 2),
    _Pm10010mrMondwRmonPacketsCounterClientInputValuePortn_Type()
)
pm10010mrMondwRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm10010mrMondwRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mrMondwRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mrMondwRmonPacketsCounterClientInputErrorPortn = _Pm10010mrMondwRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 240, 1, 3),
    _Pm10010mrMondwRmonPacketsCounterClientInputErrorPortn_Type()
)
pm10010mrMondwRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn = _Pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 63, 11, 2, 4, 240, 1, 4),
    _Pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pm10010mrLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 30)
)
pm10010mrLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapLineNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010mrLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 31)
)
pm10010mrLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapLineNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010mrLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 32)
)
pm10010mrLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapLineNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mrLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 33)
)
pm10010mrLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapLineNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010mrLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 34)
)
pm10010mrLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineFailPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapLineNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrLineTrapCritGoesOn.setStatus(
        "current"
    )

pm10010mrLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 35)
)
pm10010mrLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineFailPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapLineNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrLineTrapCritGoesOff.setStatus(
        "current"
    )

pm10010mrClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 40)
)
pm10010mrClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapPortNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010mrClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 41)
)
pm10010mrClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapPortNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010mrClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 42)
)
pm10010mrClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapPortNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mrClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 43)
)
pm10010mrClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapPortNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010mrClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 44)
)
pm10010mrClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmFailAccPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapPortNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrClientTrapCritGoesOn.setStatus(
        "current"
    )

pm10010mrClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 45)
)
pm10010mrClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmFailAccPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapPortNumber"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrClientTrapCritGoesOff.setStatus(
        "current"
    )

pm10010mrPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 50)
)
pm10010mrPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmDefFuseB"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmDefFuseA"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mrPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 63, 10, 51)
)
pm10010mrPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmDefFuseB"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrAlmDefFuseA"),
        ("EKINOPS-Pm10010mr-MIB", "pm10010mrtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mrPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm10010mr-MIB",
    **{"Pm10010mrMultiRate": Pm10010mrMultiRate,
       "Pm10010mrOtxMode": Pm10010mrOtxMode,
       "Pm10010mrOtxGrid": Pm10010mrOtxGrid,
       "Pm10010mrAdjustValue": Pm10010mrAdjustValue,
       "Pm10010mrClientProtocol": Pm10010mrClientProtocol,
       "Pm10010mrProtocolMode": Pm10010mrProtocolMode,
       "Pm10010mrOtxChannel": Pm10010mrOtxChannel,
       "Pm10010mrOrxChannel": Pm10010mrOrxChannel,
       "Rm10010ClientIgnoreTimer": Rm10010ClientIgnoreTimer,
       "modulePm10010mr": modulePm10010mr,
       "pm10010mralarms": pm10010mralarms,
       "pm10010mrAlmOther": pm10010mrAlmOther,
       "pm10010mrAlmOtherNurg": pm10010mrAlmOtherNurg,
       "pm10010mrAlmsynthAlm2": pm10010mrAlmsynthAlm2,
       "pm10010mrAlmConfTableSave": pm10010mrAlmConfTableSave,
       "pm10010mrAlmInvUpload": pm10010mrAlmInvUpload,
       "pm10010mrAlmConfTableLoad": pm10010mrAlmConfTableLoad,
       "pm10010mrAlmCorrelatOff": pm10010mrAlmCorrelatOff,
       "pm10010mrAlmMaintenanceOn": pm10010mrAlmMaintenanceOn,
       "pm10010mrAlmOtherUrg": pm10010mrAlmOtherUrg,
       "pm10010mrAlmOtherCrit": pm10010mrAlmOtherCrit,
       "pm10010mrAlmsynthAlm0": pm10010mrAlmsynthAlm0,
       "pm10010mrAlmFailFan": pm10010mrAlmFailFan,
       "pm10010mrAlmModGlobFail": pm10010mrAlmModGlobFail,
       "pm10010mrAlmDefFuseA": pm10010mrAlmDefFuseA,
       "pm10010mrAlmDefFuseB": pm10010mrAlmDefFuseB,
       "pm10010mrAlmclientModuleState": pm10010mrAlmclientModuleState,
       "pm10010mrAlmCfpInitialize": pm10010mrAlmCfpInitialize,
       "pm10010mrAlmCfpLowPower": pm10010mrAlmCfpLowPower,
       "pm10010mrAlmCfpHighPowerUp": pm10010mrAlmCfpHighPowerUp,
       "pm10010mrAlmCfpTxOff": pm10010mrAlmCfpTxOff,
       "pm10010mrAlmCfpTxTurnOn": pm10010mrAlmCfpTxTurnOn,
       "pm10010mrAlmCfpReady": pm10010mrAlmCfpReady,
       "pm10010mrAlmCfpFault": pm10010mrAlmCfpFault,
       "pm10010mrAlmCfpTxTurnOff": pm10010mrAlmCfpTxTurnOff,
       "pm10010mrAlmCfpHighPowerDown": pm10010mrAlmCfpHighPowerDown,
       "pm10010mrAlmclientModuleGeneralStatus": pm10010mrAlmclientModuleGeneralStatus,
       "pm10010mrAlmCfpOutOfAlignment": pm10010mrAlmCfpOutOfAlignment,
       "pm10010mrAlmCfpRxNetworkLol": pm10010mrAlmCfpRxNetworkLol,
       "pm10010mrAlmCfpRxLos": pm10010mrAlmCfpRxLos,
       "pm10010mrAlmCfpTxHostLol": pm10010mrAlmCfpTxHostLol,
       "pm10010mrAlmCfpTxLosf": pm10010mrAlmCfpTxLosf,
       "pm10010mrAlmCfpTxCmuLol": pm10010mrAlmCfpTxCmuLol,
       "pm10010mrAlmCfpTxJitterPllLol": pm10010mrAlmCfpTxJitterPllLol,
       "pm10010mrAlmCfpLossOfRefclk": pm10010mrAlmCfpLossOfRefclk,
       "pm10010mrAlmCfpHwInterlock": pm10010mrAlmCfpHwInterlock,
       "pm10010mrAlmclientGlobalAlarmSummary": pm10010mrAlmclientGlobalAlarmSummary,
       "pm10010mrAlmCfpSoftGlobAlarmTest": pm10010mrAlmCfpSoftGlobAlarmTest,
       "pm10010mrAlmCfpNetworkLaneAlarmWarning2": pm10010mrAlmCfpNetworkLaneAlarmWarning2,
       "pm10010mrAlmCfpModuleState": pm10010mrAlmCfpModuleState,
       "pm10010mrAlmCfpModuleGeneralStatus": pm10010mrAlmCfpModuleGeneralStatus,
       "pm10010mrAlmCfpModuleFault": pm10010mrAlmCfpModuleFault,
       "pm10010mrAlmCfpModuleAlarmWarning1": pm10010mrAlmCfpModuleAlarmWarning1,
       "pm10010mrAlmCfpModuleAlarmWarning2": pm10010mrAlmCfpModuleAlarmWarning2,
       "pm10010mrAlmCfpNetworkLaneAlarmWarning1": pm10010mrAlmCfpNetworkLaneAlarmWarning1,
       "pm10010mrAlmCfpNetworkLaneFaultStatus": pm10010mrAlmCfpNetworkLaneFaultStatus,
       "pm10010mrAlmCfpHostLaneFaultStatus": pm10010mrAlmCfpHostLaneFaultStatus,
       "pm10010mrAlmCfpGlobAlarmAssertion": pm10010mrAlmCfpGlobAlarmAssertion,
       "pm10010mrAlmmsaModuleState": pm10010mrAlmmsaModuleState,
       "pm10010mrAlmMsaInitialize": pm10010mrAlmMsaInitialize,
       "pm10010mrAlmMsaLowPower": pm10010mrAlmMsaLowPower,
       "pm10010mrAlmMsaHighPowerUp": pm10010mrAlmMsaHighPowerUp,
       "pm10010mrAlmMsaTxOff": pm10010mrAlmMsaTxOff,
       "pm10010mrAlmMsaTxTurnOn": pm10010mrAlmMsaTxTurnOn,
       "pm10010mrAlmMsaReady": pm10010mrAlmMsaReady,
       "pm10010mrAlmMsaFault": pm10010mrAlmMsaFault,
       "pm10010mrAlmMsaTxTurnOff": pm10010mrAlmMsaTxTurnOff,
       "pm10010mrAlmMsaHighPowerDown": pm10010mrAlmMsaHighPowerDown,
       "pm10010mrAlmmsaModuleGeneralStatus": pm10010mrAlmmsaModuleGeneralStatus,
       "pm10010mrAlmMsaOutOfAlignment": pm10010mrAlmMsaOutOfAlignment,
       "pm10010mrAlmMsaRxNetworkLol": pm10010mrAlmMsaRxNetworkLol,
       "pm10010mrAlmMsaRxLos": pm10010mrAlmMsaRxLos,
       "pm10010mrAlmMsaTxHostLol": pm10010mrAlmMsaTxHostLol,
       "pm10010mrAlmMsaTxLosf": pm10010mrAlmMsaTxLosf,
       "pm10010mrAlmMsaTxCmuLol": pm10010mrAlmMsaTxCmuLol,
       "pm10010mrAlmMsaTxJitterPllLol": pm10010mrAlmMsaTxJitterPllLol,
       "pm10010mrAlmMsaLossOfRefclk": pm10010mrAlmMsaLossOfRefclk,
       "pm10010mrAlmMsaHwInterlock": pm10010mrAlmMsaHwInterlock,
       "pm10010mrAlmmsaGlobalAlarmSummary": pm10010mrAlmmsaGlobalAlarmSummary,
       "pm10010mrAlmMsaSoftGlobAlarmTest": pm10010mrAlmMsaSoftGlobAlarmTest,
       "pm10010mrAlmMsaNetworkHostAlarmStatus": pm10010mrAlmMsaNetworkHostAlarmStatus,
       "pm10010mrAlmMsaNetworkLaneAlarmWarning2": pm10010mrAlmMsaNetworkLaneAlarmWarning2,
       "pm10010mrAlmMsaModuleState": pm10010mrAlmMsaModuleState,
       "pm10010mrAlmMsaModuleGeneralStatus": pm10010mrAlmMsaModuleGeneralStatus,
       "pm10010mrAlmModuleFault": pm10010mrAlmModuleFault,
       "pm10010mrAlmMsaModuleAlarmWarning1": pm10010mrAlmMsaModuleAlarmWarning1,
       "pm10010mrAlmMsaModuleAlarmWarning2": pm10010mrAlmMsaModuleAlarmWarning2,
       "pm10010mrAlmMsaNetworkLaneAlarmWarning1": pm10010mrAlmMsaNetworkLaneAlarmWarning1,
       "pm10010mrAlmMsaNetworkLaneFaultStatus": pm10010mrAlmMsaNetworkLaneFaultStatus,
       "pm10010mrAlmMsaHostLaneFaultStatus": pm10010mrAlmMsaHostLaneFaultStatus,
       "pm10010mrAlmMsaGlobAlarmAssertion": pm10010mrAlmMsaGlobAlarmAssertion,
       "pm10010mrAlmmsaNetworkTxAlignment": pm10010mrAlmmsaNetworkTxAlignment,
       "pm10010mrAlmNetTxTimingFault": pm10010mrAlmNetTxTimingFault,
       "pm10010mrAlmNetTxReferenceClockFault": pm10010mrAlmNetTxReferenceClockFault,
       "pm10010mrAlmNetTxCmuLockFault": pm10010mrAlmNetTxCmuLockFault,
       "pm10010mrAlmNetTxOutOfAlignment": pm10010mrAlmNetTxOutOfAlignment,
       "pm10010mrAlmNetTxLossOfAlignment": pm10010mrAlmNetTxLossOfAlignment,
       "pm10010mrAlmmsaNetworkRxAlignment": pm10010mrAlmmsaNetworkRxAlignment,
       "pm10010mrAlmNetRxTimingFault": pm10010mrAlmNetRxTimingFault,
       "pm10010mrAlmNetRxOutOfAlignment": pm10010mrAlmNetRxOutOfAlignment,
       "pm10010mrAlmNetRxLossOfAlignment": pm10010mrAlmNetRxLossOfAlignment,
       "pm10010mrAlmNetRxModemLockFault": pm10010mrAlmNetRxModemLockFault,
       "pm10010mrAlmNetRxModemSyncDetectFault": pm10010mrAlmNetRxModemSyncDetectFault,
       "pm10010mrAlmmsaNetworkHostNetworkAlarmSummary": pm10010mrAlmmsaNetworkHostNetworkAlarmSummary,
       "pm10010mrAlmNetworkTxAlignment": pm10010mrAlmNetworkTxAlignment,
       "pm10010mrAlmNetworkRxAlignment": pm10010mrAlmNetworkRxAlignment,
       "pm10010mrAlmNetworkRxOtn": pm10010mrAlmNetworkRxOtn,
       "pm10010mrAlmHostRxAlignment": pm10010mrAlmHostRxAlignment,
       "pm10010mrAlmHostTxAlignment": pm10010mrAlmHostTxAlignment,
       "pm10010mrAlmHostTxOtnStatus": pm10010mrAlmHostTxOtnStatus,
       "pm10010mrAlmmsaHostTxAlignment": pm10010mrAlmmsaHostTxAlignment,
       "pm10010mrAlmHostTxDeskewLockFault": pm10010mrAlmHostTxDeskewLockFault,
       "pm10010mrAlmHostTxOutOfAlignment": pm10010mrAlmHostTxOutOfAlignment,
       "pm10010mrAlmHostTxLossOfAlignment": pm10010mrAlmHostTxLossOfAlignment,
       "pm10010mrAlmHostTxCdrLockFault": pm10010mrAlmHostTxCdrLockFault,
       "pm10010mrAlmmsaHostRxAlignment": pm10010mrAlmmsaHostRxAlignment,
       "pm10010mrAlmHostRxCmuLockFault": pm10010mrAlmHostRxCmuLockFault,
       "pm10010mrAlmHostRxOutOfAlignment": pm10010mrAlmHostRxOutOfAlignment,
       "pm10010mrAlmHostRxLossOfAlignment": pm10010mrAlmHostRxLossOfAlignment,
       "pm10010mrAlmClient": pm10010mrAlmClient,
       "pm10010mrAlmClientNurg": pm10010mrAlmClientNurg,
       "pm10010mrAlmclientNetworkLaneAlarmWarningTable": pm10010mrAlmclientNetworkLaneAlarmWarningTable,
       "pm10010mrAlmclientNetworkLaneAlarmWarningEntry": pm10010mrAlmclientNetworkLaneAlarmWarningEntry,
       "pm10010mrAlmclientNetworkLaneAlarmWarningIndex": pm10010mrAlmclientNetworkLaneAlarmWarningIndex,
       "pm10010mrAlmClientRxPowerLowAlarmPortn": pm10010mrAlmClientRxPowerLowAlarmPortn,
       "pm10010mrAlmClientRxPowerLowWarningPortn": pm10010mrAlmClientRxPowerLowWarningPortn,
       "pm10010mrAlmClientRxPowerHighWarningPortn": pm10010mrAlmClientRxPowerHighWarningPortn,
       "pm10010mrAlmClientRxPowerHighAlarmPortn": pm10010mrAlmClientRxPowerHighAlarmPortn,
       "pm10010mrAlmLaserTempLowAlarmPortn": pm10010mrAlmLaserTempLowAlarmPortn,
       "pm10010mrAlmClientLaserTempLowWarningPortn": pm10010mrAlmClientLaserTempLowWarningPortn,
       "pm10010mrAlmClientLaserTempHighWarningPortn": pm10010mrAlmClientLaserTempHighWarningPortn,
       "pm10010mrAlmClientLaserTempHighAlarmPortn": pm10010mrAlmClientLaserTempHighAlarmPortn,
       "pm10010mrAlmClientTxPowerLowAlarmPortn": pm10010mrAlmClientTxPowerLowAlarmPortn,
       "pm10010mrAlmClientTxPowerLowWarningPortn": pm10010mrAlmClientTxPowerLowWarningPortn,
       "pm10010mrAlmClientTxPowerHighWarningPortn": pm10010mrAlmClientTxPowerHighWarningPortn,
       "pm10010mrAlmClientTxPowerHighAlarmPortn": pm10010mrAlmClientTxPowerHighAlarmPortn,
       "pm10010mrAlmClientBiasLowAlarmPortn": pm10010mrAlmClientBiasLowAlarmPortn,
       "pm10010mrAlmClientBiasLowWarningPortn": pm10010mrAlmClientBiasLowWarningPortn,
       "pm10010mrAlmClientBiasHighWarningPortn": pm10010mrAlmClientBiasHighWarningPortn,
       "pm10010mrAlmClientBiasHighAlarmPortn": pm10010mrAlmClientBiasHighAlarmPortn,
       "pm10010mrAlmclientSfpWarnDdmTable": pm10010mrAlmclientSfpWarnDdmTable,
       "pm10010mrAlmclientSfpWarnDdmEntry": pm10010mrAlmclientSfpWarnDdmEntry,
       "pm10010mrAlmclientSfpWarnDdmIndex": pm10010mrAlmclientSfpWarnDdmIndex,
       "pm10010mrAlmTxPwLowWngPortn": pm10010mrAlmTxPwLowWngPortn,
       "pm10010mrAlmTxPwrHighWngPortn": pm10010mrAlmTxPwrHighWngPortn,
       "pm10010mrAlmTxBiasLowWngPortn": pm10010mrAlmTxBiasLowWngPortn,
       "pm10010mrAlmTxBiasHighWngPortn": pm10010mrAlmTxBiasHighWngPortn,
       "pm10010mrAlmVccLowWngPortn": pm10010mrAlmVccLowWngPortn,
       "pm10010mrAlmVccHighWngPortn": pm10010mrAlmVccHighWngPortn,
       "pm10010mrAlmTempLowWngPortn": pm10010mrAlmTempLowWngPortn,
       "pm10010mrAlmTempHighWngPortn": pm10010mrAlmTempHighWngPortn,
       "pm10010mrAlmRxPwrLowWngPortn": pm10010mrAlmRxPwrLowWngPortn,
       "pm10010mrAlmRxPwrHighWngPortn": pm10010mrAlmRxPwrHighWngPortn,
       "pm10010mrAlmClientUrg": pm10010mrAlmClientUrg,
       "pm10010mrAlmclientNetworkLaneFaultTable": pm10010mrAlmclientNetworkLaneFaultTable,
       "pm10010mrAlmclientNetworkLaneFaultEntry": pm10010mrAlmclientNetworkLaneFaultEntry,
       "pm10010mrAlmclientNetworkLaneFaultIndex": pm10010mrAlmclientNetworkLaneFaultIndex,
       "pm10010mrAlmClientLaneRxFifoErrorPortn": pm10010mrAlmClientLaneRxFifoErrorPortn,
       "pm10010mrAlmClientLaneRxLolPortn": pm10010mrAlmClientLaneRxLolPortn,
       "pm10010mrAlmClientLaneRxLosPortn": pm10010mrAlmClientLaneRxLosPortn,
       "pm10010mrAlmClientLaneTxLolPortn": pm10010mrAlmClientLaneTxLolPortn,
       "pm10010mrAlmClientLaneTxLosfPortn": pm10010mrAlmClientLaneTxLosfPortn,
       "pm10010mrAlmClientLaneApdPowerSupplyPortn": pm10010mrAlmClientLaneApdPowerSupplyPortn,
       "pm10010mrAlmClientLaneWavelengthUnlockedPortn": pm10010mrAlmClientLaneWavelengthUnlockedPortn,
       "pm10010mrAlmClientLaneTecFaultPortn": pm10010mrAlmClientLaneTecFaultPortn,
       "pm10010mrAlmclientHostLaneFaultTable": pm10010mrAlmclientHostLaneFaultTable,
       "pm10010mrAlmclientHostLaneFaultEntry": pm10010mrAlmclientHostLaneFaultEntry,
       "pm10010mrAlmclientHostLaneFaultIndex": pm10010mrAlmclientHostLaneFaultIndex,
       "pm10010mrAlmClientLossOfSyncPortn": pm10010mrAlmClientLossOfSyncPortn,
       "pm10010mrAlmClientInputLossOfSigPortn": pm10010mrAlmClientInputLossOfSigPortn,
       "pm10010mrAlmClientLanesMarkerUnlockPortn": pm10010mrAlmClientLanesMarkerUnlockPortn,
       "pm10010mrAlmClientLanes6466UnlockPortn": pm10010mrAlmClientLanes6466UnlockPortn,
       "pm10010mrAlmClientLanesNotAlignedPortn": pm10010mrAlmClientLanesNotAlignedPortn,
       "pm10010mrAlmClientCsfDetectedPortn": pm10010mrAlmClientCsfDetectedPortn,
       "pm10010mrAlmClientTxHostLolPortn": pm10010mrAlmClientTxHostLolPortn,
       "pm10010mrAlmClientLaneTxFifoErrorPortn": pm10010mrAlmClientLaneTxFifoErrorPortn,
       "pm10010mrAlmLfDetectedPortn": pm10010mrAlmLfDetectedPortn,
       "pm10010mrAlmRfDetectedPortn": pm10010mrAlmRfDetectedPortn,
       "pm10010mrAlmclientSfpAlmDdmTable": pm10010mrAlmclientSfpAlmDdmTable,
       "pm10010mrAlmclientSfpAlmDdmEntry": pm10010mrAlmclientSfpAlmDdmEntry,
       "pm10010mrAlmclientSfpAlmDdmIndex": pm10010mrAlmclientSfpAlmDdmIndex,
       "pm10010mrAlmTxPwrLowAlaPortn": pm10010mrAlmTxPwrLowAlaPortn,
       "pm10010mrAlmTxPwrHighAlaPortn": pm10010mrAlmTxPwrHighAlaPortn,
       "pm10010mrAlmTxBiasLowAlaPortn": pm10010mrAlmTxBiasLowAlaPortn,
       "pm10010mrAlmTxBiasHighAlaPortn": pm10010mrAlmTxBiasHighAlaPortn,
       "pm10010mrAlmVccLowAlaPortn": pm10010mrAlmVccLowAlaPortn,
       "pm10010mrAlmVccHighAlaPortn": pm10010mrAlmVccHighAlaPortn,
       "pm10010mrAlmTempLowAlaPortn": pm10010mrAlmTempLowAlaPortn,
       "pm10010mrAlmTempHighAlaPortn": pm10010mrAlmTempHighAlaPortn,
       "pm10010mrAlmRxPwrLowAlaPortn": pm10010mrAlmRxPwrLowAlaPortn,
       "pm10010mrAlmRxPwrHighAlaPortn": pm10010mrAlmRxPwrHighAlaPortn,
       "pm10010mrAlmClientCrit": pm10010mrAlmClientCrit,
       "pm10010mrAlmsynthAlmPortTable": pm10010mrAlmsynthAlmPortTable,
       "pm10010mrAlmsynthAlmPortEntry": pm10010mrAlmsynthAlmPortEntry,
       "pm10010mrAlmsynthAlmPortIndex": pm10010mrAlmsynthAlmPortIndex,
       "pm10010mrAlmSfpAbsentPortn": pm10010mrAlmSfpAbsentPortn,
       "pm10010mrAlmDdmAbsentPortn": pm10010mrAlmDdmAbsentPortn,
       "pm10010mrAlmHwFailAccPortn": pm10010mrAlmHwFailAccPortn,
       "pm10010mrAlmDwLsdPortn": pm10010mrAlmDwLsdPortn,
       "pm10010mrAlmClientLocalOosPortn": pm10010mrAlmClientLocalOosPortn,
       "pm10010mrAlmClientRemoteOosPortn": pm10010mrAlmClientRemoteOosPortn,
       "pm10010mrAlmDwCaisPortn": pm10010mrAlmDwCaisPortn,
       "pm10010mrAlmSfpDdmWarningPortn": pm10010mrAlmSfpDdmWarningPortn,
       "pm10010mrAlmSfpDdmAlmPortn": pm10010mrAlmSfpDdmAlmPortn,
       "pm10010mrAlmIdleInsertedPortn": pm10010mrAlmIdleInsertedPortn,
       "pm10010mrAlmFailAccPortn": pm10010mrAlmFailAccPortn,
       "pm10010mrAlmUpCsfPortn": pm10010mrAlmUpCsfPortn,
       "pm10010mrAlmLine": pm10010mrAlmLine,
       "pm10010mrAlmLineNurg": pm10010mrAlmLineNurg,
       "pm10010mrAlmlineNetworkLaneAlarmWarning1Table": pm10010mrAlmlineNetworkLaneAlarmWarning1Table,
       "pm10010mrAlmlineNetworkLaneAlarmWarning1Entry": pm10010mrAlmlineNetworkLaneAlarmWarning1Entry,
       "pm10010mrAlmlineNetworkLaneAlarmWarning1Index": pm10010mrAlmlineNetworkLaneAlarmWarning1Index,
       "pm10010mrAlmLineRxPowerLowAlarmPortn": pm10010mrAlmLineRxPowerLowAlarmPortn,
       "pm10010mrAlmLineRxPowerLowWarningPortn": pm10010mrAlmLineRxPowerLowWarningPortn,
       "pm10010mrAlmLineRxPowerHighWarningPortn": pm10010mrAlmLineRxPowerHighWarningPortn,
       "pm10010mrAlmLineRxPowerHighAlarmPortn": pm10010mrAlmLineRxPowerHighAlarmPortn,
       "pm10010mrAlmLineLaserTempLowAlarmPortn": pm10010mrAlmLineLaserTempLowAlarmPortn,
       "pm10010mrAlmLineLaserTempLowWarningPortn": pm10010mrAlmLineLaserTempLowWarningPortn,
       "pm10010mrAlmLineLaserTempHighWarningPortn": pm10010mrAlmLineLaserTempHighWarningPortn,
       "pm10010mrAlmLineLaserTempHighAlarmPortn": pm10010mrAlmLineLaserTempHighAlarmPortn,
       "pm10010mrAlmLineTxPowerLowAlarmPortn": pm10010mrAlmLineTxPowerLowAlarmPortn,
       "pm10010mrAlmLineTxPowerLowWarningPortn": pm10010mrAlmLineTxPowerLowWarningPortn,
       "pm10010mrAlmLineTxPowerHighWarningPortn": pm10010mrAlmLineTxPowerHighWarningPortn,
       "pm10010mrAlmLineTxPowerHighAlarmPortn": pm10010mrAlmLineTxPowerHighAlarmPortn,
       "pm10010mrAlmLineBiasLowAlarmPortn": pm10010mrAlmLineBiasLowAlarmPortn,
       "pm10010mrAlmLineBiasLowWarningPortn": pm10010mrAlmLineBiasLowWarningPortn,
       "pm10010mrAlmLineBiasHighWarningPortn": pm10010mrAlmLineBiasHighWarningPortn,
       "pm10010mrAlmLineBiasHighAlarmPortn": pm10010mrAlmLineBiasHighAlarmPortn,
       "pm10010mrAlmlineNetworkLaneAlarmWarning2Table": pm10010mrAlmlineNetworkLaneAlarmWarning2Table,
       "pm10010mrAlmlineNetworkLaneAlarmWarning2Entry": pm10010mrAlmlineNetworkLaneAlarmWarning2Entry,
       "pm10010mrAlmlineNetworkLaneAlarmWarning2Index": pm10010mrAlmlineNetworkLaneAlarmWarning2Index,
       "pm10010mrAlmTxModulatorBiasLowAlarmPortn": pm10010mrAlmTxModulatorBiasLowAlarmPortn,
       "pm10010mrAlmTxModulatorBiasLowWarningPortn": pm10010mrAlmTxModulatorBiasLowWarningPortn,
       "pm10010mrAlmTxModulatorBiasHighWarningPortn": pm10010mrAlmTxModulatorBiasHighWarningPortn,
       "pm10010mrAlmTxModulatorBiasHighAlarmPortn": pm10010mrAlmTxModulatorBiasHighAlarmPortn,
       "pm10010mrAlmRxLaserTempLowAlarmPortn": pm10010mrAlmRxLaserTempLowAlarmPortn,
       "pm10010mrAlmRxLaserTempLowWarningPortn": pm10010mrAlmRxLaserTempLowWarningPortn,
       "pm10010mrAlmRxLaserTempHighWarningPortn": pm10010mrAlmRxLaserTempHighWarningPortn,
       "pm10010mrAlmRxLaserTempHighAlarmPortn": pm10010mrAlmRxLaserTempHighAlarmPortn,
       "pm10010mrAlmRxLaserOutputLowAlarmPortn": pm10010mrAlmRxLaserOutputLowAlarmPortn,
       "pm10010mrAlmRxLaserOutputLowWarningPortn": pm10010mrAlmRxLaserOutputLowWarningPortn,
       "pm10010mrAlmRxLaserOutputHighWarningPortn": pm10010mrAlmRxLaserOutputHighWarningPortn,
       "pm10010mrAlmRxLaserOutputHighAlarmPortn": pm10010mrAlmRxLaserOutputHighAlarmPortn,
       "pm10010mrAlmRxLaserBiasLowAlarmPortn": pm10010mrAlmRxLaserBiasLowAlarmPortn,
       "pm10010mrAlmRxLaserBiasLowWarningPortn": pm10010mrAlmRxLaserBiasLowWarningPortn,
       "pm10010mrAlmRxLaserBiasHighWarningPortn": pm10010mrAlmRxLaserBiasHighWarningPortn,
       "pm10010mrAlmRxLaserBiasHighAlarmPortn": pm10010mrAlmRxLaserBiasHighAlarmPortn,
       "pm10010mrAlmLineUrg": pm10010mrAlmLineUrg,
       "pm10010mrAlmlineNetworkLaneFaultTable": pm10010mrAlmlineNetworkLaneFaultTable,
       "pm10010mrAlmlineNetworkLaneFaultEntry": pm10010mrAlmlineNetworkLaneFaultEntry,
       "pm10010mrAlmlineNetworkLaneFaultIndex": pm10010mrAlmlineNetworkLaneFaultIndex,
       "pm10010mrAlmLineLaneRxTecFaultPortn": pm10010mrAlmLineLaneRxTecFaultPortn,
       "pm10010mrAlmLineLaneRxFifoErrorPortn": pm10010mrAlmLineLaneRxFifoErrorPortn,
       "pm10010mrAlmLineLaneRxLolPortn": pm10010mrAlmLineLaneRxLolPortn,
       "pm10010mrAlmLineLaneRxLosPortn": pm10010mrAlmLineLaneRxLosPortn,
       "pm10010mrAlmLineLaneTxLolPortn": pm10010mrAlmLineLaneTxLolPortn,
       "pm10010mrAlmLineLaneTxLosfPortn": pm10010mrAlmLineLaneTxLosfPortn,
       "pm10010mrAlmLineLaneApdPowerSupplyPortn": pm10010mrAlmLineLaneApdPowerSupplyPortn,
       "pm10010mrAlmLineLaneWavelengthUnlockedPortn": pm10010mrAlmLineLaneWavelengthUnlockedPortn,
       "pm10010mrAlmLineLaneTecFaultPortn": pm10010mrAlmLineLaneTecFaultPortn,
       "pm10010mrAlmlineHostLaneFaultTable": pm10010mrAlmlineHostLaneFaultTable,
       "pm10010mrAlmlineHostLaneFaultEntry": pm10010mrAlmlineHostLaneFaultEntry,
       "pm10010mrAlmlineHostLaneFaultIndex": pm10010mrAlmlineHostLaneFaultIndex,
       "pm10010mrAlmLineInputLossOfSignalPortn": pm10010mrAlmLineInputLossOfSignalPortn,
       "pm10010mrAlmLineLossOfFramePortn": pm10010mrAlmLineLossOfFramePortn,
       "pm10010mrAlmLineSmBdiInsertedPortn": pm10010mrAlmLineSmBdiInsertedPortn,
       "pm10010mrAlmLineSmBdiDetectedPortn": pm10010mrAlmLineSmBdiDetectedPortn,
       "pm10010mrAlmLineSmIaeInsertedPortn": pm10010mrAlmLineSmIaeInsertedPortn,
       "pm10010mrAlmLineSmIaeDetectedPortn": pm10010mrAlmLineSmIaeDetectedPortn,
       "pm10010mrAlmLineTxHostLolPortn": pm10010mrAlmLineTxHostLolPortn,
       "pm10010mrAlmLineLaneTxFifoErrorPortn": pm10010mrAlmLineLaneTxFifoErrorPortn,
       "pm10010mrAlmLinePowerDegradePortn": pm10010mrAlmLinePowerDegradePortn,
       "pm10010mrAlmLineTrxOverTempPortn": pm10010mrAlmLineTrxOverTempPortn,
       "pm10010mrAlmlineNetworkLaneRxOtnTable": pm10010mrAlmlineNetworkLaneRxOtnTable,
       "pm10010mrAlmlineNetworkLaneRxOtnEntry": pm10010mrAlmlineNetworkLaneRxOtnEntry,
       "pm10010mrAlmlineNetworkLaneRxOtnIndex": pm10010mrAlmlineNetworkLaneRxOtnIndex,
       "pm10010mrAlmLineRxOtnOduAisPortn": pm10010mrAlmLineRxOtnOduAisPortn,
       "pm10010mrAlmLineRxOtnOtuAisPortn": pm10010mrAlmLineRxOtnOtuAisPortn,
       "pm10010mrAlmLineRxSmBdiPortn": pm10010mrAlmLineRxSmBdiPortn,
       "pm10010mrAlmLineRxOtnIaePortn": pm10010mrAlmLineRxOtnIaePortn,
       "pm10010mrAlmLineRxOtnOomPortn": pm10010mrAlmLineRxOtnOomPortn,
       "pm10010mrAlmLineRxOtnLomPortn": pm10010mrAlmLineRxOtnLomPortn,
       "pm10010mrAlmLineRxOtnOofPortn": pm10010mrAlmLineRxOtnOofPortn,
       "pm10010mrAlmLineRxOtnLofPortn": pm10010mrAlmLineRxOtnLofPortn,
       "pm10010mrAlmlineHostLaneTxOtnTable": pm10010mrAlmlineHostLaneTxOtnTable,
       "pm10010mrAlmlineHostLaneTxOtnEntry": pm10010mrAlmlineHostLaneTxOtnEntry,
       "pm10010mrAlmlineHostLaneTxOtnIndex": pm10010mrAlmlineHostLaneTxOtnIndex,
       "pm10010mrAlmLineTxOtnOduAisPortn": pm10010mrAlmLineTxOtnOduAisPortn,
       "pm10010mrAlmLineTxOtnOtuAisPortn": pm10010mrAlmLineTxOtnOtuAisPortn,
       "pm10010mrAlmLineTxSmBdiPortn": pm10010mrAlmLineTxSmBdiPortn,
       "pm10010mrAlmLineTxOtnIaePortn": pm10010mrAlmLineTxOtnIaePortn,
       "pm10010mrAlmLineTxOtnOomPortn": pm10010mrAlmLineTxOtnOomPortn,
       "pm10010mrAlmLineTxOtnLomPortn": pm10010mrAlmLineTxOtnLomPortn,
       "pm10010mrAlmLineTxOtnOofPortn": pm10010mrAlmLineTxOtnOofPortn,
       "pm10010mrAlmLineTxOtnLofPortn": pm10010mrAlmLineTxOtnLofPortn,
       "pm10010mrAlmLineCrit": pm10010mrAlmLineCrit,
       "pm10010mrAlmsynthAlmLineTable": pm10010mrAlmsynthAlmLineTable,
       "pm10010mrAlmsynthAlmLineEntry": pm10010mrAlmsynthAlmLineEntry,
       "pm10010mrAlmsynthAlmLineIndex": pm10010mrAlmsynthAlmLineIndex,
       "pm10010mrAlmXfpAbsentPortn": pm10010mrAlmXfpAbsentPortn,
       "pm10010mrAlmXfpInitNotComplPortn": pm10010mrAlmXfpInitNotComplPortn,
       "pm10010mrAlmLineHwFailPortn": pm10010mrAlmLineHwFailPortn,
       "pm10010mrAlmXfpTxOffPortn": pm10010mrAlmXfpTxOffPortn,
       "pm10010mrAlmLineLocalOosPortn": pm10010mrAlmLineLocalOosPortn,
       "pm10010mrAlmUpRdiInsPortn": pm10010mrAlmUpRdiInsPortn,
       "pm10010mrAlmLineDdmWarningPortn": pm10010mrAlmLineDdmWarningPortn,
       "pm10010mrAlmLineDdmAlmPortn": pm10010mrAlmLineDdmAlmPortn,
       "pm10010mrAlmLineFailPortn": pm10010mrAlmLineFailPortn,
       "pm10010mrAlmLineActivePortn": pm10010mrAlmLineActivePortn,
       "pm10010mrmeasures": pm10010mrmeasures,
       "pm10010mrMesrOther": pm10010mrMesrOther,
       "pm10010mrMesrsynth0": pm10010mrMesrsynth0,
       "pm10010mrMesrsynth1": pm10010mrMesrsynth1,
       "pm10010mrMesrpmIntervalNumber": pm10010mrMesrpmIntervalNumber,
       "pm10010mrMesrlineNetTxLaserOutputPwrAverage": pm10010mrMesrlineNetTxLaserOutputPwrAverage,
       "pm10010mrMesrlineNetTxLaserTempAverage": pm10010mrMesrlineNetTxLaserTempAverage,
       "pm10010mrMesrlineNetTxBiasCurrentAverage": pm10010mrMesrlineNetTxBiasCurrentAverage,
       "pm10010mrMesrlineNetRxInputPwrAverage": pm10010mrMesrlineNetRxInputPwrAverage,
       "pm10010mrMesrlineResidualChromaticDispAverage": pm10010mrMesrlineResidualChromaticDispAverage,
       "pm10010mrMesrlineDiffGroupDelayAverage": pm10010mrMesrlineDiffGroupDelayAverage,
       "pm10010mrMesrlineQFactorAverage": pm10010mrMesrlineQFactorAverage,
       "pm10010mrMesrlineCarrierFreqOffsetAverage": pm10010mrMesrlineCarrierFreqOffsetAverage,
       "pm10010mrMesrlineOsnrAverage": pm10010mrMesrlineOsnrAverage,
       "pm10010mrMesrclientNetTxTempMin": pm10010mrMesrclientNetTxTempMin,
       "pm10010mrMesrclientNetTxBiasMin": pm10010mrMesrclientNetTxBiasMin,
       "pm10010mrMesrclientNetTxPwrMin": pm10010mrMesrclientNetTxPwrMin,
       "pm10010mrMesrclientNetRxPwrMin": pm10010mrMesrclientNetRxPwrMin,
       "pm10010mrMesrlineNetTxLaserOutputPwrMin": pm10010mrMesrlineNetTxLaserOutputPwrMin,
       "pm10010mrMesrlineNetTxLaserTempMin": pm10010mrMesrlineNetTxLaserTempMin,
       "pm10010mrMesrlineNetTxBiasCurrentMin": pm10010mrMesrlineNetTxBiasCurrentMin,
       "pm10010mrMesrlineNetRxInputPwrMin": pm10010mrMesrlineNetRxInputPwrMin,
       "pm10010mrMesrlineResidualChromaticDispMin": pm10010mrMesrlineResidualChromaticDispMin,
       "pm10010mrMesrlineDiffGroupDelayMin": pm10010mrMesrlineDiffGroupDelayMin,
       "pm10010mrMesrlineQFactorMin": pm10010mrMesrlineQFactorMin,
       "pm10010mrMesrlineCarrierFreqOffsetMin": pm10010mrMesrlineCarrierFreqOffsetMin,
       "pm10010mrMesrlineOsnrMin": pm10010mrMesrlineOsnrMin,
       "pm10010mrMesrclientNetTxTempMax": pm10010mrMesrclientNetTxTempMax,
       "pm10010mrMesrclientNetTxBiasMax": pm10010mrMesrclientNetTxBiasMax,
       "pm10010mrMesrclientNetTxPwrMax": pm10010mrMesrclientNetTxPwrMax,
       "pm10010mrMesrclientNetRxPwrMax": pm10010mrMesrclientNetRxPwrMax,
       "pm10010mrMesrlineNetTxLaserOutputPwrMax": pm10010mrMesrlineNetTxLaserOutputPwrMax,
       "pm10010mrMesrlineNetTxLaserTempMax": pm10010mrMesrlineNetTxLaserTempMax,
       "pm10010mrMesrlineNetTxBiasCurrentMax": pm10010mrMesrlineNetTxBiasCurrentMax,
       "pm10010mrMesrlineNetRxInputPwrMax": pm10010mrMesrlineNetRxInputPwrMax,
       "pm10010mrMesrlineResidualChromaticDispMax": pm10010mrMesrlineResidualChromaticDispMax,
       "pm10010mrMesrlineDiffGroupDelayMax": pm10010mrMesrlineDiffGroupDelayMax,
       "pm10010mrMesrlineQFactorMax": pm10010mrMesrlineQFactorMax,
       "pm10010mrMesrlineCarrierFreqOffsetMax": pm10010mrMesrlineCarrierFreqOffsetMax,
       "pm10010mrMesrlineOsnrMax": pm10010mrMesrlineOsnrMax,
       "pm10010mrMesrClient": pm10010mrMesrClient,
       "pm10010mrMesrclientCfpTemp": pm10010mrMesrclientCfpTemp,
       "pm10010mrMesrclientCfp3v3Voltage": pm10010mrMesrclientCfp3v3Voltage,
       "pm10010mrMesrclientSoaBiasCurrent": pm10010mrMesrclientSoaBiasCurrent,
       "pm10010mrMesrclientNetTxTempTable": pm10010mrMesrclientNetTxTempTable,
       "pm10010mrMesrclientNetTxTempEntry": pm10010mrMesrclientNetTxTempEntry,
       "pm10010mrMesrclientNetTxTempIndex": pm10010mrMesrclientNetTxTempIndex,
       "pm10010mrMesrclientNetTxTempPortn": pm10010mrMesrclientNetTxTempPortn,
       "pm10010mrMesrclientNetTxBiasTable": pm10010mrMesrclientNetTxBiasTable,
       "pm10010mrMesrclientNetTxBiasEntry": pm10010mrMesrclientNetTxBiasEntry,
       "pm10010mrMesrclientNetTxBiasIndex": pm10010mrMesrclientNetTxBiasIndex,
       "pm10010mrMesrclientNetTxBiasPortn": pm10010mrMesrclientNetTxBiasPortn,
       "pm10010mrMesrclientNetTxPwrTable": pm10010mrMesrclientNetTxPwrTable,
       "pm10010mrMesrclientNetTxPwrEntry": pm10010mrMesrclientNetTxPwrEntry,
       "pm10010mrMesrclientNetTxPwrIndex": pm10010mrMesrclientNetTxPwrIndex,
       "pm10010mrMesrclientNetTxPwrPortn": pm10010mrMesrclientNetTxPwrPortn,
       "pm10010mrMesrclientNetRxPwrTable": pm10010mrMesrclientNetRxPwrTable,
       "pm10010mrMesrclientNetRxPwrEntry": pm10010mrMesrclientNetRxPwrEntry,
       "pm10010mrMesrclientNetRxPwrIndex": pm10010mrMesrclientNetRxPwrIndex,
       "pm10010mrMesrclientNetRxPwrPortn": pm10010mrMesrclientNetRxPwrPortn,
       "pm10010mrMesrLine": pm10010mrMesrLine,
       "pm10010mrMesrlineMsaTemp": pm10010mrMesrlineMsaTemp,
       "pm10010mrMesrlineMsa3v3Voltage": pm10010mrMesrlineMsa3v3Voltage,
       "pm10010mrMesrlineSoaBiasCurrent": pm10010mrMesrlineSoaBiasCurrent,
       "pm10010mrMesrlineNetTxLaserOutputPwrTable": pm10010mrMesrlineNetTxLaserOutputPwrTable,
       "pm10010mrMesrlineNetTxLaserOutputPwrEntry": pm10010mrMesrlineNetTxLaserOutputPwrEntry,
       "pm10010mrMesrlineNetTxLaserOutputPwrIndex": pm10010mrMesrlineNetTxLaserOutputPwrIndex,
       "pm10010mrMesrlineNetTxLaserOutputPwrPortn": pm10010mrMesrlineNetTxLaserOutputPwrPortn,
       "pm10010mrMesrlineNetTxLaserTempTable": pm10010mrMesrlineNetTxLaserTempTable,
       "pm10010mrMesrlineNetTxLaserTempEntry": pm10010mrMesrlineNetTxLaserTempEntry,
       "pm10010mrMesrlineNetTxLaserTempIndex": pm10010mrMesrlineNetTxLaserTempIndex,
       "pm10010mrMesrlineNetTxLaserTempPortn": pm10010mrMesrlineNetTxLaserTempPortn,
       "pm10010mrMesrlineNetTxBiasCurrentTable": pm10010mrMesrlineNetTxBiasCurrentTable,
       "pm10010mrMesrlineNetTxBiasCurrentEntry": pm10010mrMesrlineNetTxBiasCurrentEntry,
       "pm10010mrMesrlineNetTxBiasCurrentIndex": pm10010mrMesrlineNetTxBiasCurrentIndex,
       "pm10010mrMesrlineNetTxBiasCurrentPortn": pm10010mrMesrlineNetTxBiasCurrentPortn,
       "pm10010mrMesrlineNetRxInputPwrTable": pm10010mrMesrlineNetRxInputPwrTable,
       "pm10010mrMesrlineNetRxInputPwrEntry": pm10010mrMesrlineNetRxInputPwrEntry,
       "pm10010mrMesrlineNetRxInputPwrIndex": pm10010mrMesrlineNetRxInputPwrIndex,
       "pm10010mrMesrlineNetRxInputPwrPortn": pm10010mrMesrlineNetRxInputPwrPortn,
       "pm10010mrMesrlineResidualChromaticDispTable": pm10010mrMesrlineResidualChromaticDispTable,
       "pm10010mrMesrlineResidualChromaticDispEntry": pm10010mrMesrlineResidualChromaticDispEntry,
       "pm10010mrMesrlineResidualChromaticDispIndex": pm10010mrMesrlineResidualChromaticDispIndex,
       "pm10010mrMesrlineResidualChromaticDispPortn": pm10010mrMesrlineResidualChromaticDispPortn,
       "pm10010mrMesrlineDiffGroupDelayTable": pm10010mrMesrlineDiffGroupDelayTable,
       "pm10010mrMesrlineDiffGroupDelayEntry": pm10010mrMesrlineDiffGroupDelayEntry,
       "pm10010mrMesrlineDiffGroupDelayIndex": pm10010mrMesrlineDiffGroupDelayIndex,
       "pm10010mrMesrlineDiffGroupDelayPortn": pm10010mrMesrlineDiffGroupDelayPortn,
       "pm10010mrMesrlineQFactorTable": pm10010mrMesrlineQFactorTable,
       "pm10010mrMesrlineQFactorEntry": pm10010mrMesrlineQFactorEntry,
       "pm10010mrMesrlineQFactorIndex": pm10010mrMesrlineQFactorIndex,
       "pm10010mrMesrlineQFactorPortn": pm10010mrMesrlineQFactorPortn,
       "pm10010mrMesrlineCarrierFreqOffsetTable": pm10010mrMesrlineCarrierFreqOffsetTable,
       "pm10010mrMesrlineCarrierFreqOffsetEntry": pm10010mrMesrlineCarrierFreqOffsetEntry,
       "pm10010mrMesrlineCarrierFreqOffsetIndex": pm10010mrMesrlineCarrierFreqOffsetIndex,
       "pm10010mrMesrlineCarrierFreqOffsetPortn": pm10010mrMesrlineCarrierFreqOffsetPortn,
       "pm10010mrMesrlineOsnrTable": pm10010mrMesrlineOsnrTable,
       "pm10010mrMesrlineOsnrEntry": pm10010mrMesrlineOsnrEntry,
       "pm10010mrMesrlineOsnrIndex": pm10010mrMesrlineOsnrIndex,
       "pm10010mrMesrlineOsnrPortn": pm10010mrMesrlineOsnrPortn,
       "pm10010mrcounters": pm10010mrcounters,
       "pm10010mrCntOther": pm10010mrCntOther,
       "pm10010mrCntClient": pm10010mrCntClient,
       "pm10010mrCntclientInputErrorCounterLaneOneTable": pm10010mrCntclientInputErrorCounterLaneOneTable,
       "pm10010mrCntclientInputErrorCounterLaneOneEntry": pm10010mrCntclientInputErrorCounterLaneOneEntry,
       "pm10010mrCntclientInputErrorCounterLaneOneIndex": pm10010mrCntclientInputErrorCounterLaneOneIndex,
       "pm10010mrCntclientInputErrorCounterLaneOneValuePortn": pm10010mrCntclientInputErrorCounterLaneOneValuePortn,
       "pm10010mrCntclientInputErrorCounterLaneOneErrorPortn": pm10010mrCntclientInputErrorCounterLaneOneErrorPortn,
       "pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn": pm10010mrCntclientInputErrorCounterLaneOneOverloadPortn,
       "pm10010mrCntclientInputErrorCounterLaneTwoTable": pm10010mrCntclientInputErrorCounterLaneTwoTable,
       "pm10010mrCntclientInputErrorCounterLaneTwoEntry": pm10010mrCntclientInputErrorCounterLaneTwoEntry,
       "pm10010mrCntclientInputErrorCounterLaneTwoIndex": pm10010mrCntclientInputErrorCounterLaneTwoIndex,
       "pm10010mrCntclientInputErrorCounterLaneTwoValuePortn": pm10010mrCntclientInputErrorCounterLaneTwoValuePortn,
       "pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn": pm10010mrCntclientInputErrorCounterLaneTwoErrorPortn,
       "pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn": pm10010mrCntclientInputErrorCounterLaneTwoOverloadPortn,
       "pm10010mrCntclientInputErrorCounterTable": pm10010mrCntclientInputErrorCounterTable,
       "pm10010mrCntclientInputErrorCounterEntry": pm10010mrCntclientInputErrorCounterEntry,
       "pm10010mrCntclientInputErrorCounterIndex": pm10010mrCntclientInputErrorCounterIndex,
       "pm10010mrCntclientInputErrorCounterValuePortn": pm10010mrCntclientInputErrorCounterValuePortn,
       "pm10010mrCntclientInputErrorCounterErrorPortn": pm10010mrCntclientInputErrorCounterErrorPortn,
       "pm10010mrCntclientInputErrorCounterOverloadPortn": pm10010mrCntclientInputErrorCounterOverloadPortn,
       "pm10010mrCntclientCbipCounterTable": pm10010mrCntclientCbipCounterTable,
       "pm10010mrCntclientCbipCounterEntry": pm10010mrCntclientCbipCounterEntry,
       "pm10010mrCntclientCbipCounterIndex": pm10010mrCntclientCbipCounterIndex,
       "pm10010mrCntclientCbipCounterValuePortn": pm10010mrCntclientCbipCounterValuePortn,
       "pm10010mrCntclientCbipCounterErrorPortn": pm10010mrCntclientCbipCounterErrorPortn,
       "pm10010mrCntclientCbipCounterOverloadPortn": pm10010mrCntclientCbipCounterOverloadPortn,
       "pm10010mrCntLine": pm10010mrCntLine,
       "pm10010mrCntlocalLineSmBip8ErrorCounterTable": pm10010mrCntlocalLineSmBip8ErrorCounterTable,
       "pm10010mrCntlocalLineSmBip8ErrorCounterEntry": pm10010mrCntlocalLineSmBip8ErrorCounterEntry,
       "pm10010mrCntlocalLineSmBip8ErrorCounterIndex": pm10010mrCntlocalLineSmBip8ErrorCounterIndex,
       "pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn": pm10010mrCntlocalLineSmBip8ErrorCounterValuePortn,
       "pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn": pm10010mrCntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn": pm10010mrCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm10010mrCntlocalLineFecCorrectedErrorsCounterTable": pm10010mrCntlocalLineFecCorrectedErrorsCounterTable,
       "pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry": pm10010mrCntlocalLineFecCorrectedErrorsCounterEntry,
       "pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex": pm10010mrCntlocalLineFecCorrectedErrorsCounterIndex,
       "pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn": pm10010mrCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn": pm10010mrCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm10010mrCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm10010mrCntremoteLineSmBip8ErrorCounterTable": pm10010mrCntremoteLineSmBip8ErrorCounterTable,
       "pm10010mrCntremoteLineSmBip8ErrorCounterEntry": pm10010mrCntremoteLineSmBip8ErrorCounterEntry,
       "pm10010mrCntremoteLineSmBip8ErrorCounterIndex": pm10010mrCntremoteLineSmBip8ErrorCounterIndex,
       "pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn": pm10010mrCntremoteLineSmBip8ErrorCounterValuePortn,
       "pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn": pm10010mrCntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn": pm10010mrCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm10010mrCntlineDfrmTimCntTable": pm10010mrCntlineDfrmTimCntTable,
       "pm10010mrCntlineDfrmTimCntEntry": pm10010mrCntlineDfrmTimCntEntry,
       "pm10010mrCntlineDfrmTimCntIndex": pm10010mrCntlineDfrmTimCntIndex,
       "pm10010mrCntlineDfrmTimCntValuePortn": pm10010mrCntlineDfrmTimCntValuePortn,
       "pm10010mrCntlineDfrmTimCntErrorPortn": pm10010mrCntlineDfrmTimCntErrorPortn,
       "pm10010mrCntlineDfrmTimCntOverloadPortn": pm10010mrCntlineDfrmTimCntOverloadPortn,
       "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterTable": pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterTable,
       "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry": pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex": pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn": pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": pm10010mrCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterTable": pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry": pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex": pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": pm10010mrCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "pm10010mrcontrolsWrite": pm10010mrcontrolsWrite,
       "pm10010mrCtrlOther": pm10010mrCtrlOther,
       "pm10010mrCtrlconfMgnt1": pm10010mrCtrlconfMgnt1,
       "pm10010mrCtrlConf1Load1": pm10010mrCtrlConf1Load1,
       "pm10010mrCtrlConf2Load1": pm10010mrCtrlConf2Load1,
       "pm10010mrCtrlConf2Flash1": pm10010mrCtrlConf2Flash1,
       "pm10010mrCtrlConf2Clear1": pm10010mrCtrlConf2Clear1,
       "pm10010mrCtrlsynth4": pm10010mrCtrlsynth4,
       "pm10010mrCtrlCorrelatOn": pm10010mrCtrlCorrelatOn,
       "pm10010mrCtrlCorrelatOff": pm10010mrCtrlCorrelatOff,
       "pm10010mrCtrlswMgnt": pm10010mrCtrlswMgnt,
       "pm10010mrCtrlColdReset": pm10010mrCtrlColdReset,
       "pm10010mrCtrlWarmReset": pm10010mrCtrlWarmReset,
       "pm10010mrCtrlLoadSwBank1": pm10010mrCtrlLoadSwBank1,
       "pm10010mrCtrlLoadSwBank2": pm10010mrCtrlLoadSwBank2,
       "pm10010mrCtrlgwMgnt": pm10010mrCtrlgwMgnt,
       "pm10010mrCtrlCurrentGwReset": pm10010mrCtrlCurrentGwReset,
       "pm10010mrCtrlLoadGwBank1": pm10010mrCtrlLoadGwBank1,
       "pm10010mrCtrlLoadGwBank2": pm10010mrCtrlLoadGwBank2,
       "pm10010mrCtrlLoadGwBank3": pm10010mrCtrlLoadGwBank3,
       "pm10010mrCtrlLoadGwBank4": pm10010mrCtrlLoadGwBank4,
       "pm10010mrCtrlledTest": pm10010mrCtrlledTest,
       "pm10010mrCtrlGreenLed": pm10010mrCtrlGreenLed,
       "pm10010mrCtrlRedLed": pm10010mrCtrlRedLed,
       "pm10010mrCtrlLedOff": pm10010mrCtrlLedOff,
       "pm10010mrCtrlinitSwitchMarvell": pm10010mrCtrlinitSwitchMarvell,
       "pm10010mrCtrlInitSwitchMarvell": pm10010mrCtrlInitSwitchMarvell,
       "pm10010mrCtrlresetCount": pm10010mrCtrlresetCount,
       "pm10010mrCtrlResetcount": pm10010mrCtrlResetcount,
       "pm10010mrCtrlresetRmon": pm10010mrCtrlresetRmon,
       "pm10010mrCtrlResetrmon": pm10010mrCtrlResetrmon,
       "pm10010mrCtrlresetMeasurements": pm10010mrCtrlresetMeasurements,
       "pm10010mrCtrlResetmeasurements": pm10010mrCtrlResetmeasurements,
       "pm10010mrCtrlClient": pm10010mrCtrlClient,
       "pm10010mrCtrlaccessLoopTable": pm10010mrCtrlaccessLoopTable,
       "pm10010mrCtrlaccessLoopEntry": pm10010mrCtrlaccessLoopEntry,
       "pm10010mrCtrlaccessLoopIndex": pm10010mrCtrlaccessLoopIndex,
       "pm10010mrCtrlaccessLoopPortn": pm10010mrCtrlaccessLoopPortn,
       "pm10010mrCtrlclientLoopToLineTable": pm10010mrCtrlclientLoopToLineTable,
       "pm10010mrCtrlclientLoopToLineEntry": pm10010mrCtrlclientLoopToLineEntry,
       "pm10010mrCtrlclientLoopToLineIndex": pm10010mrCtrlclientLoopToLineIndex,
       "pm10010mrCtrlclientLoopToLinePortn": pm10010mrCtrlclientLoopToLinePortn,
       "pm10010mrCtrlcsfUpInsTable": pm10010mrCtrlcsfUpInsTable,
       "pm10010mrCtrlcsfUpInsEntry": pm10010mrCtrlcsfUpInsEntry,
       "pm10010mrCtrlcsfUpInsIndex": pm10010mrCtrlcsfUpInsIndex,
       "pm10010mrCtrlcsfUpInsPortn": pm10010mrCtrlcsfUpInsPortn,
       "pm10010mrCtrlcaisDwInsTable": pm10010mrCtrlcaisDwInsTable,
       "pm10010mrCtrlcaisDwInsEntry": pm10010mrCtrlcaisDwInsEntry,
       "pm10010mrCtrlcaisDwInsIndex": pm10010mrCtrlcaisDwInsIndex,
       "pm10010mrCtrlcaisDwInsPortn": pm10010mrCtrlcaisDwInsPortn,
       "pm10010mrCtrlLine": pm10010mrCtrlLine,
       "pm10010mrCtrlcommAccessLoopTable": pm10010mrCtrlcommAccessLoopTable,
       "pm10010mrCtrlcommAccessLoopEntry": pm10010mrCtrlcommAccessLoopEntry,
       "pm10010mrCtrlcommAccessLoopIndex": pm10010mrCtrlcommAccessLoopIndex,
       "pm10010mrCtrlcommAccessLoopPortn": pm10010mrCtrlcommAccessLoopPortn,
       "pm10010mrCtrllineLoopTable": pm10010mrCtrllineLoopTable,
       "pm10010mrCtrllineLoopEntry": pm10010mrCtrllineLoopEntry,
       "pm10010mrCtrllineLoopIndex": pm10010mrCtrllineLoopIndex,
       "pm10010mrCtrllineLoopPortn": pm10010mrCtrllineLoopPortn,
       "pm10010mrCtrlfecDisableTable": pm10010mrCtrlfecDisableTable,
       "pm10010mrCtrlfecDisableEntry": pm10010mrCtrlfecDisableEntry,
       "pm10010mrCtrlfecDisableIndex": pm10010mrCtrlfecDisableIndex,
       "pm10010mrCtrlfecDisablePortn": pm10010mrCtrlfecDisablePortn,
       "pm10010mrCtrlmsaLineLoopTable": pm10010mrCtrlmsaLineLoopTable,
       "pm10010mrCtrlmsaLineLoopEntry": pm10010mrCtrlmsaLineLoopEntry,
       "pm10010mrCtrlmsaLineLoopIndex": pm10010mrCtrlmsaLineLoopIndex,
       "pm10010mrCtrlmsaLineLoopPortn": pm10010mrCtrlmsaLineLoopPortn,
       "pm10010mrCtrlmsaTxResetTable": pm10010mrCtrlmsaTxResetTable,
       "pm10010mrCtrlmsaTxResetEntry": pm10010mrCtrlmsaTxResetEntry,
       "pm10010mrCtrlmsaTxResetIndex": pm10010mrCtrlmsaTxResetIndex,
       "pm10010mrCtrlmsaTxResetPortn": pm10010mrCtrlmsaTxResetPortn,
       "pm10010mrCtrlmsaRxResetTable": pm10010mrCtrlmsaRxResetTable,
       "pm10010mrCtrlmsaRxResetEntry": pm10010mrCtrlmsaRxResetEntry,
       "pm10010mrCtrlmsaRxResetIndex": pm10010mrCtrlmsaRxResetIndex,
       "pm10010mrCtrlmsaRxResetPortn": pm10010mrCtrlmsaRxResetPortn,
       "pm10010mrCtrlmsaShutdownTable": pm10010mrCtrlmsaShutdownTable,
       "pm10010mrCtrlmsaShutdownEntry": pm10010mrCtrlmsaShutdownEntry,
       "pm10010mrCtrlmsaShutdownIndex": pm10010mrCtrlmsaShutdownIndex,
       "pm10010mrCtrlmsaShutdownPortn": pm10010mrCtrlmsaShutdownPortn,
       "pm10010mrri": pm10010mrri,
       "pm10010mrriTable": pm10010mrriTable,
       "pm10010mrRinvSfpTable": pm10010mrRinvSfpTable,
       "pm10010mrRinvSfpEntry": pm10010mrRinvSfpEntry,
       "pm10010mrRinvSfpIndex": pm10010mrRinvSfpIndex,
       "pm10010mrRinvsfp": pm10010mrRinvsfp,
       "pm10010mrRinvLineTable": pm10010mrRinvLineTable,
       "pm10010mrRinvLineEntry": pm10010mrRinvLineEntry,
       "pm10010mrRinvLineIndex": pm10010mrRinvLineIndex,
       "pm10010mrRinvxfpLine": pm10010mrRinvxfpLine,
       "pm10010mrRinvReloadInventory": pm10010mrRinvReloadInventory,
       "pm10010mrRinvHwPlatform": pm10010mrRinvHwPlatform,
       "pm10010mrRinvModulePlatform": pm10010mrRinvModulePlatform,
       "pm10010mrRinvSwPlatform": pm10010mrRinvSwPlatform,
       "pm10010mrRinvGwPlatform": pm10010mrRinvGwPlatform,
       "pm10010mrdownload": pm10010mrdownload,
       "pm10010mrDwlOther": pm10010mrDwlOther,
       "pm10010mrDwlrestartProcess": pm10010mrDwlrestartProcess,
       "pm10010mrDwlWarmRestartProcessed": pm10010mrDwlWarmRestartProcessed,
       "pm10010mrDwlColdRestartProcessed": pm10010mrDwlColdRestartProcessed,
       "pm10010mrDwlswBanksUsed": pm10010mrDwlswBanksUsed,
       "pm10010mrDwlSwBank1Used": pm10010mrDwlSwBank1Used,
       "pm10010mrDwlSwBank2Used": pm10010mrDwlSwBank2Used,
       "pm10010mrDwlSwBank1Notempty": pm10010mrDwlSwBank1Notempty,
       "pm10010mrDwlSwBank2Notempty": pm10010mrDwlSwBank2Notempty,
       "pm10010mrDwlgwBanksUsed": pm10010mrDwlgwBanksUsed,
       "pm10010mrDwlGwBank1Used": pm10010mrDwlGwBank1Used,
       "pm10010mrDwlGwBank2Used": pm10010mrDwlGwBank2Used,
       "pm10010mrDwlGwBank3Used": pm10010mrDwlGwBank3Used,
       "pm10010mrDwlGwBank4Used": pm10010mrDwlGwBank4Used,
       "pm10010mrDwlGwBank1Notempty": pm10010mrDwlGwBank1Notempty,
       "pm10010mrDwlGwBank2Notempty": pm10010mrDwlGwBank2Notempty,
       "pm10010mrDwlGwBank3Notempty": pm10010mrDwlGwBank3Notempty,
       "pm10010mrDwlGwBank4Notempty": pm10010mrDwlGwBank4Notempty,
       "pm10010mrDwlClient": pm10010mrDwlClient,
       "pm10010mrDwlLine": pm10010mrDwlLine,
       "pm10010mrConfig": pm10010mrConfig,
       "pm10010mrCfgAccessCAisCsf": pm10010mrCfgAccessCAisCsf,
       "pm10010mrCfgClientcaiscsfTable": pm10010mrCfgClientcaiscsfTable,
       "pm10010mrCfgClientcaiscsfEntry": pm10010mrCfgClientcaiscsfEntry,
       "pm10010mrCfgClientcaiscsfIndex": pm10010mrCfgClientcaiscsfIndex,
       "pm10010mrCfgReservePortn": pm10010mrCfgReservePortn,
       "pm10010mrCfgStartup": pm10010mrCfgStartup,
       "pm10010mrCfgClientStartupTable": pm10010mrCfgClientStartupTable,
       "pm10010mrCfgClientStartupEntry": pm10010mrCfgClientStartupEntry,
       "pm10010mrCfgClientStartupIndex": pm10010mrCfgClientStartupIndex,
       "pm10010mrCfgSystConfPortPortn": pm10010mrCfgSystConfPortPortn,
       "pm10010mrCfgNetConfPortPortn": pm10010mrCfgNetConfPortPortn,
       "pm10010mrCfgIgnoreTimePortn": pm10010mrCfgIgnoreTimePortn,
       "pm10010mrCfgOptionsPortPortn": pm10010mrCfgOptionsPortPortn,
       "pm10010mrCfgLineStartupTable": pm10010mrCfgLineStartupTable,
       "pm10010mrCfgLineStartupEntry": pm10010mrCfgLineStartupEntry,
       "pm10010mrCfgLineStartupIndex": pm10010mrCfgLineStartupIndex,
       "pm10010mrCfgSystConfLinePortn": pm10010mrCfgSystConfLinePortn,
       "pm10010mrCfgOptionsLinePortn": pm10010mrCfgOptionsLinePortn,
       "pm10010mrCfgXfpTable": pm10010mrCfgXfpTable,
       "pm10010mrCfgXfpEntry": pm10010mrCfgXfpEntry,
       "pm10010mrCfgXfpIndex": pm10010mrCfgXfpIndex,
       "pm10010mrCfgSystConfMsaLinePortn": pm10010mrCfgSystConfMsaLinePortn,
       "pm10010mrCfgLabels": pm10010mrCfgLabels,
       "pm10010mrCfgLabelclientTable": pm10010mrCfgLabelclientTable,
       "pm10010mrCfgLabelclientEntry": pm10010mrCfgLabelclientEntry,
       "pm10010mrCfgLabelclientIndex": pm10010mrCfgLabelclientIndex,
       "pm10010mrCfgLabelclientPortn": pm10010mrCfgLabelclientPortn,
       "pm10010mrCfgLabellineTable": pm10010mrCfgLabellineTable,
       "pm10010mrCfgLabellineEntry": pm10010mrCfgLabellineEntry,
       "pm10010mrCfgLabellineIndex": pm10010mrCfgLabellineIndex,
       "pm10010mrCfgLabellinePortn": pm10010mrCfgLabellinePortn,
       "pm10010mrCfgStartuptlh": pm10010mrCfgStartuptlh,
       "pm10010mrCfgOtxtlhTable": pm10010mrCfgOtxtlhTable,
       "pm10010mrCfgOtxtlhEntry": pm10010mrCfgOtxtlhEntry,
       "pm10010mrCfgOtxtlhIndex": pm10010mrCfgOtxtlhIndex,
       "pm10010mrCfgLinePwrLaserPortn": pm10010mrCfgLinePwrLaserPortn,
       "pm10010mrCfgLineFCurrentPortn": pm10010mrCfgLineFCurrentPortn,
       "pm10010mrCfgLineGridCurrentPortn": pm10010mrCfgLineGridCurrentPortn,
       "pm10010mrCfgFPortn": pm10010mrCfgFPortn,
       "pm10010mrCfgRxLineFCurrentPortn": pm10010mrCfgRxLineFCurrentPortn,
       "pm10010mrCfgOther": pm10010mrCfgOther,
       "pm10010mrtablemoduleOther": pm10010mrtablemoduleOther,
       "pm10010mrCfgmode": pm10010mrCfgmode,
       "pm10010mrCfgfanLowSpeedThreshold": pm10010mrCfgfanLowSpeedThreshold,
       "pm10010mrCfgfanHighSpeedThreshold": pm10010mrCfgfanHighSpeedThreshold,
       "pm10010mrCfgStartuptablefive": pm10010mrCfgStartuptablefive,
       "pm10010mrCfgOtxtlhcapabilitiesTable": pm10010mrCfgOtxtlhcapabilitiesTable,
       "pm10010mrCfgOtxtlhcapabilitiesEntry": pm10010mrCfgOtxtlhcapabilitiesEntry,
       "pm10010mrCfgOtxtlhcapabilitiesIndex": pm10010mrCfgOtxtlhcapabilitiesIndex,
       "pm10010mrCfgComponentTypePortn": pm10010mrCfgComponentTypePortn,
       "pm10010mrCfgMiscellaneousPortn": pm10010mrCfgMiscellaneousPortn,
       "pm10010mrCfgFirstChannelPortn": pm10010mrCfgFirstChannelPortn,
       "pm10010mrCfgLastChannelPortn": pm10010mrCfgLastChannelPortn,
       "pm10010mrCfgGridPortn": pm10010mrCfgGridPortn,
       "pm10010mrCfgWriteConfiguration": pm10010mrCfgWriteConfiguration,
       "pm10010mrtraps": pm10010mrtraps,
       "pm10010mrtrapPortNumber": pm10010mrtrapPortNumber,
       "pm10010mrtrapLineNumber": pm10010mrtrapLineNumber,
       "pm10010mrtrapBoardNumber": pm10010mrtrapBoardNumber,
       "pm10010mrLineTrapNotUrgentGoesOn": pm10010mrLineTrapNotUrgentGoesOn,
       "pm10010mrLineTrapNotUrgentGoesOff": pm10010mrLineTrapNotUrgentGoesOff,
       "pm10010mrLineTrapUrgentGoesOn": pm10010mrLineTrapUrgentGoesOn,
       "pm10010mrLineTrapUrgentGoesOff": pm10010mrLineTrapUrgentGoesOff,
       "pm10010mrLineTrapCritGoesOn": pm10010mrLineTrapCritGoesOn,
       "pm10010mrLineTrapCritGoesOff": pm10010mrLineTrapCritGoesOff,
       "pm10010mrClientTrapNotUrgentGoesOn": pm10010mrClientTrapNotUrgentGoesOn,
       "pm10010mrClientTrapNotUrgentGoesOff": pm10010mrClientTrapNotUrgentGoesOff,
       "pm10010mrClientTrapUrgentGoesOn": pm10010mrClientTrapUrgentGoesOn,
       "pm10010mrClientTrapUrgentGoesOff": pm10010mrClientTrapUrgentGoesOff,
       "pm10010mrClientTrapCritGoesOn": pm10010mrClientTrapCritGoesOn,
       "pm10010mrClientTrapCritGoesOff": pm10010mrClientTrapCritGoesOff,
       "pm10010mrPowerTrapUrgentGoesOn": pm10010mrPowerTrapUrgentGoesOn,
       "pm10010mrPowerTrapUrgentGoesOff": pm10010mrPowerTrapUrgentGoesOff,
       "pm10010mrMonitoring": pm10010mrMonitoring,
       "pm10010mrMonOther": pm10010mrMonOther,
       "pm10010mrMonRmon": pm10010mrMonRmon,
       "pm10010mrMonClient": pm10010mrMonClient,
       "pm10010mrMonClientRmonCounter": pm10010mrMonClientRmonCounter,
       "pm10010mrMonupRmonBytesCounterClientInputTable": pm10010mrMonupRmonBytesCounterClientInputTable,
       "pm10010mrMonupRmonBytesCounterClientInputEntry": pm10010mrMonupRmonBytesCounterClientInputEntry,
       "pm10010mrMonupRmonBytesCounterClientInputIndex": pm10010mrMonupRmonBytesCounterClientInputIndex,
       "pm10010mrMonupRmonBytesCounterClientInputValuePortn": pm10010mrMonupRmonBytesCounterClientInputValuePortn,
       "pm10010mrMonupRmonBytesCounterClientInputErrorPortn": pm10010mrMonupRmonBytesCounterClientInputErrorPortn,
       "pm10010mrMonupRmonBytesCounterClientInputOverloadPortn": pm10010mrMonupRmonBytesCounterClientInputOverloadPortn,
       "pm10010mrMonupRmonCrcErrorsCounterClientInputTable": pm10010mrMonupRmonCrcErrorsCounterClientInputTable,
       "pm10010mrMonupRmonCrcErrorsCounterClientInputEntry": pm10010mrMonupRmonCrcErrorsCounterClientInputEntry,
       "pm10010mrMonupRmonCrcErrorsCounterClientInputIndex": pm10010mrMonupRmonCrcErrorsCounterClientInputIndex,
       "pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn": pm10010mrMonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn": pm10010mrMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn": pm10010mrMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm10010mrMonupRmonPacketsCounterClientInputTable": pm10010mrMonupRmonPacketsCounterClientInputTable,
       "pm10010mrMonupRmonPacketsCounterClientInputEntry": pm10010mrMonupRmonPacketsCounterClientInputEntry,
       "pm10010mrMonupRmonPacketsCounterClientInputIndex": pm10010mrMonupRmonPacketsCounterClientInputIndex,
       "pm10010mrMonupRmonPacketsCounterClientInputValuePortn": pm10010mrMonupRmonPacketsCounterClientInputValuePortn,
       "pm10010mrMonupRmonPacketsCounterClientInputErrorPortn": pm10010mrMonupRmonPacketsCounterClientInputErrorPortn,
       "pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn": pm10010mrMonupRmonPacketsCounterClientInputOverloadPortn,
       "pm10010mrMonupRmonBroadcastCounterClientInputTable": pm10010mrMonupRmonBroadcastCounterClientInputTable,
       "pm10010mrMonupRmonBroadcastCounterClientInputEntry": pm10010mrMonupRmonBroadcastCounterClientInputEntry,
       "pm10010mrMonupRmonBroadcastCounterClientInputIndex": pm10010mrMonupRmonBroadcastCounterClientInputIndex,
       "pm10010mrMonupRmonBroadcastCounterClientInputValuePortn": pm10010mrMonupRmonBroadcastCounterClientInputValuePortn,
       "pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn": pm10010mrMonupRmonBroadcastCounterClientInputErrorPortn,
       "pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn": pm10010mrMonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm10010mrMonupRmonMulticastCounterClientInputTable": pm10010mrMonupRmonMulticastCounterClientInputTable,
       "pm10010mrMonupRmonMulticastCounterClientInputEntry": pm10010mrMonupRmonMulticastCounterClientInputEntry,
       "pm10010mrMonupRmonMulticastCounterClientInputIndex": pm10010mrMonupRmonMulticastCounterClientInputIndex,
       "pm10010mrMonupRmonMulticastCounterClientInputValuePortn": pm10010mrMonupRmonMulticastCounterClientInputValuePortn,
       "pm10010mrMonupRmonMulticastCounterClientInputErrorPortn": pm10010mrMonupRmonMulticastCounterClientInputErrorPortn,
       "pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn": pm10010mrMonupRmonMulticastCounterClientInputOverloadPortn,
       "pm10010mrMonupRmonPauseFrameCounterClientInputTable": pm10010mrMonupRmonPauseFrameCounterClientInputTable,
       "pm10010mrMonupRmonPauseFrameCounterClientInputEntry": pm10010mrMonupRmonPauseFrameCounterClientInputEntry,
       "pm10010mrMonupRmonPauseFrameCounterClientInputIndex": pm10010mrMonupRmonPauseFrameCounterClientInputIndex,
       "pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn": pm10010mrMonupRmonPauseFrameCounterClientInputValuePortn,
       "pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn": pm10010mrMonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn": pm10010mrMonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm10010mrMondwRmonCrcErrorsCounterClientInputTable": pm10010mrMondwRmonCrcErrorsCounterClientInputTable,
       "pm10010mrMondwRmonCrcErrorsCounterClientInputEntry": pm10010mrMondwRmonCrcErrorsCounterClientInputEntry,
       "pm10010mrMondwRmonCrcErrorsCounterClientInputIndex": pm10010mrMondwRmonCrcErrorsCounterClientInputIndex,
       "pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn": pm10010mrMondwRmonCrcErrorsCounterClientInputValuePortn,
       "pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn": pm10010mrMondwRmonCrcErrorsCounterClientInputErrorPortn,
       "pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn": pm10010mrMondwRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm10010mrMondwRmonPacketsCounterClientInputTable": pm10010mrMondwRmonPacketsCounterClientInputTable,
       "pm10010mrMondwRmonPacketsCounterClientInputEntry": pm10010mrMondwRmonPacketsCounterClientInputEntry,
       "pm10010mrMondwRmonPacketsCounterClientInputIndex": pm10010mrMondwRmonPacketsCounterClientInputIndex,
       "pm10010mrMondwRmonPacketsCounterClientInputValuePortn": pm10010mrMondwRmonPacketsCounterClientInputValuePortn,
       "pm10010mrMondwRmonPacketsCounterClientInputErrorPortn": pm10010mrMondwRmonPacketsCounterClientInputErrorPortn,
       "pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn": pm10010mrMondwRmonPacketsCounterClientInputOverloadPortn}
)
