# SNMP MIB module (EKINOPS-Pm10010mp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm10010mp-MIB.mib
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

modulePm10010mp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58)
)
if mibBuilder.loadTexts:
    modulePm10010mp.setRevisions(
        ("2013-09-26 00:00",
         "2014-01-16 00:00",
         "2014-04-01 00:00",
         "2014-10-14 00:00",
         "2015-01-22 00:00",
         "2015-04-23 00:00",
         "2015-10-21 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm10010mpMultiRate(TextualConvention, Integer32):
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



class Pm10010mpOtxMode(TextualConvention, Integer32):
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



class Pm10010mpOtxGrid(TextualConvention, Integer32):
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



class Pm10010mpAdjustValue(TextualConvention, Integer32):
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



class Pm10010mpClientProtocol(TextualConvention, Integer32):
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



class Pm10010mpProtocolMode(TextualConvention, Integer32):
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



class Pm10010mpOtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm10010mpOrxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm10010mpalarms_ObjectIdentity = ObjectIdentity
pm10010mpalarms = _Pm10010mpalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2)
)
_Pm10010mpAlmOther_ObjectIdentity = ObjectIdentity
pm10010mpAlmOther = _Pm10010mpAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1)
)
_Pm10010mpAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm10010mpAlmOtherNurg = _Pm10010mpAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1)
)
_Pm10010mpAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm10010mpAlmsynthAlm2 = _Pm10010mpAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1, 2)
)
_Pm10010mpAlmConfTableSave_Type = EkiOnOff
_Pm10010mpAlmConfTableSave_Object = MibScalar
pm10010mpAlmConfTableSave = _Pm10010mpAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1, 2, 1),
    _Pm10010mpAlmConfTableSave_Type()
)
pm10010mpAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmConfTableSave.setStatus("current")
_Pm10010mpAlmInvUpload_Type = EkiOnOff
_Pm10010mpAlmInvUpload_Object = MibScalar
pm10010mpAlmInvUpload = _Pm10010mpAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1, 2, 2),
    _Pm10010mpAlmInvUpload_Type()
)
pm10010mpAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmInvUpload.setStatus("current")
_Pm10010mpAlmConfTableLoad_Type = EkiOnOff
_Pm10010mpAlmConfTableLoad_Object = MibScalar
pm10010mpAlmConfTableLoad = _Pm10010mpAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1, 2, 3),
    _Pm10010mpAlmConfTableLoad_Type()
)
pm10010mpAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmConfTableLoad.setStatus("current")
_Pm10010mpAlmCorrelatOff_Type = EkiOnOff
_Pm10010mpAlmCorrelatOff_Object = MibScalar
pm10010mpAlmCorrelatOff = _Pm10010mpAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1, 2, 4),
    _Pm10010mpAlmCorrelatOff_Type()
)
pm10010mpAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCorrelatOff.setStatus("current")
_Pm10010mpAlmMaintenanceOn_Type = EkiOnOff
_Pm10010mpAlmMaintenanceOn_Object = MibScalar
pm10010mpAlmMaintenanceOn = _Pm10010mpAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 1, 2, 5),
    _Pm10010mpAlmMaintenanceOn_Type()
)
pm10010mpAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMaintenanceOn.setStatus("current")
_Pm10010mpAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm10010mpAlmOtherUrg = _Pm10010mpAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 2)
)
_Pm10010mpAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm10010mpAlmOtherCrit = _Pm10010mpAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3)
)
_Pm10010mpAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm10010mpAlmsynthAlm0 = _Pm10010mpAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 0)
)
_Pm10010mpAlmFailFan_Type = EkiOnOff
_Pm10010mpAlmFailFan_Object = MibScalar
pm10010mpAlmFailFan = _Pm10010mpAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 0, 2),
    _Pm10010mpAlmFailFan_Type()
)
pm10010mpAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmFailFan.setStatus("current")
_Pm10010mpAlmModGlobFail_Type = EkiOnOff
_Pm10010mpAlmModGlobFail_Object = MibScalar
pm10010mpAlmModGlobFail = _Pm10010mpAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 0, 9),
    _Pm10010mpAlmModGlobFail_Type()
)
pm10010mpAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmModGlobFail.setStatus("current")
_Pm10010mpAlmDefFuseA_Type = EkiOnOff
_Pm10010mpAlmDefFuseA_Object = MibScalar
pm10010mpAlmDefFuseA = _Pm10010mpAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 0, 15),
    _Pm10010mpAlmDefFuseA_Type()
)
pm10010mpAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmDefFuseA.setStatus("current")
_Pm10010mpAlmDefFuseB_Type = EkiOnOff
_Pm10010mpAlmDefFuseB_Object = MibScalar
pm10010mpAlmDefFuseB = _Pm10010mpAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 0, 16),
    _Pm10010mpAlmDefFuseB_Type()
)
pm10010mpAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmDefFuseB.setStatus("current")
_Pm10010mpAlmclientModuleState_ObjectIdentity = ObjectIdentity
pm10010mpAlmclientModuleState = _Pm10010mpAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40)
)
_Pm10010mpAlmCfpInitialize_Type = EkiOnOff
_Pm10010mpAlmCfpInitialize_Object = MibScalar
pm10010mpAlmCfpInitialize = _Pm10010mpAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 1),
    _Pm10010mpAlmCfpInitialize_Type()
)
pm10010mpAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpInitialize.setStatus("current")
_Pm10010mpAlmCfpLowPower_Type = EkiOnOff
_Pm10010mpAlmCfpLowPower_Object = MibScalar
pm10010mpAlmCfpLowPower = _Pm10010mpAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 2),
    _Pm10010mpAlmCfpLowPower_Type()
)
pm10010mpAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpLowPower.setStatus("current")
_Pm10010mpAlmCfpHighPowerUp_Type = EkiOnOff
_Pm10010mpAlmCfpHighPowerUp_Object = MibScalar
pm10010mpAlmCfpHighPowerUp = _Pm10010mpAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 3),
    _Pm10010mpAlmCfpHighPowerUp_Type()
)
pm10010mpAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpHighPowerUp.setStatus("current")
_Pm10010mpAlmCfpTxOff_Type = EkiOnOff
_Pm10010mpAlmCfpTxOff_Object = MibScalar
pm10010mpAlmCfpTxOff = _Pm10010mpAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 4),
    _Pm10010mpAlmCfpTxOff_Type()
)
pm10010mpAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxOff.setStatus("current")
_Pm10010mpAlmCfpTxTurnOn_Type = EkiOnOff
_Pm10010mpAlmCfpTxTurnOn_Object = MibScalar
pm10010mpAlmCfpTxTurnOn = _Pm10010mpAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 5),
    _Pm10010mpAlmCfpTxTurnOn_Type()
)
pm10010mpAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxTurnOn.setStatus("current")
_Pm10010mpAlmCfpReady_Type = EkiOnOff
_Pm10010mpAlmCfpReady_Object = MibScalar
pm10010mpAlmCfpReady = _Pm10010mpAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 6),
    _Pm10010mpAlmCfpReady_Type()
)
pm10010mpAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpReady.setStatus("current")
_Pm10010mpAlmCfpFault_Type = EkiOnOff
_Pm10010mpAlmCfpFault_Object = MibScalar
pm10010mpAlmCfpFault = _Pm10010mpAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 7),
    _Pm10010mpAlmCfpFault_Type()
)
pm10010mpAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpFault.setStatus("current")
_Pm10010mpAlmCfpTxTurnOff_Type = EkiOnOff
_Pm10010mpAlmCfpTxTurnOff_Object = MibScalar
pm10010mpAlmCfpTxTurnOff = _Pm10010mpAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 8),
    _Pm10010mpAlmCfpTxTurnOff_Type()
)
pm10010mpAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxTurnOff.setStatus("current")
_Pm10010mpAlmCfpHighPowerDown_Type = EkiOnOff
_Pm10010mpAlmCfpHighPowerDown_Object = MibScalar
pm10010mpAlmCfpHighPowerDown = _Pm10010mpAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 40, 9),
    _Pm10010mpAlmCfpHighPowerDown_Type()
)
pm10010mpAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpHighPowerDown.setStatus("current")
_Pm10010mpAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010mpAlmclientModuleGeneralStatus = _Pm10010mpAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41)
)
_Pm10010mpAlmCfpOutOfAlignment_Type = EkiOnOff
_Pm10010mpAlmCfpOutOfAlignment_Object = MibScalar
pm10010mpAlmCfpOutOfAlignment = _Pm10010mpAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 4),
    _Pm10010mpAlmCfpOutOfAlignment_Type()
)
pm10010mpAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpOutOfAlignment.setStatus("current")
_Pm10010mpAlmCfpRxNetworkLol_Type = EkiOnOff
_Pm10010mpAlmCfpRxNetworkLol_Object = MibScalar
pm10010mpAlmCfpRxNetworkLol = _Pm10010mpAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 5),
    _Pm10010mpAlmCfpRxNetworkLol_Type()
)
pm10010mpAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpRxNetworkLol.setStatus("current")
_Pm10010mpAlmCfpRxLos_Type = EkiOnOff
_Pm10010mpAlmCfpRxLos_Object = MibScalar
pm10010mpAlmCfpRxLos = _Pm10010mpAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 6),
    _Pm10010mpAlmCfpRxLos_Type()
)
pm10010mpAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpRxLos.setStatus("current")
_Pm10010mpAlmCfpTxHostLol_Type = EkiOnOff
_Pm10010mpAlmCfpTxHostLol_Object = MibScalar
pm10010mpAlmCfpTxHostLol = _Pm10010mpAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 7),
    _Pm10010mpAlmCfpTxHostLol_Type()
)
pm10010mpAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxHostLol.setStatus("current")
_Pm10010mpAlmCfpTxLosf_Type = EkiOnOff
_Pm10010mpAlmCfpTxLosf_Object = MibScalar
pm10010mpAlmCfpTxLosf = _Pm10010mpAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 8),
    _Pm10010mpAlmCfpTxLosf_Type()
)
pm10010mpAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxLosf.setStatus("current")
_Pm10010mpAlmCfpTxCmuLol_Type = EkiOnOff
_Pm10010mpAlmCfpTxCmuLol_Object = MibScalar
pm10010mpAlmCfpTxCmuLol = _Pm10010mpAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 9),
    _Pm10010mpAlmCfpTxCmuLol_Type()
)
pm10010mpAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxCmuLol.setStatus("current")
_Pm10010mpAlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm10010mpAlmCfpTxJitterPllLol_Object = MibScalar
pm10010mpAlmCfpTxJitterPllLol = _Pm10010mpAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 10),
    _Pm10010mpAlmCfpTxJitterPllLol_Type()
)
pm10010mpAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpTxJitterPllLol.setStatus("current")
_Pm10010mpAlmCfpLossOfRefclk_Type = EkiOnOff
_Pm10010mpAlmCfpLossOfRefclk_Object = MibScalar
pm10010mpAlmCfpLossOfRefclk = _Pm10010mpAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 11),
    _Pm10010mpAlmCfpLossOfRefclk_Type()
)
pm10010mpAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpLossOfRefclk.setStatus("current")
_Pm10010mpAlmCfpHwInterlock_Type = EkiOnOff
_Pm10010mpAlmCfpHwInterlock_Object = MibScalar
pm10010mpAlmCfpHwInterlock = _Pm10010mpAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 41, 14),
    _Pm10010mpAlmCfpHwInterlock_Type()
)
pm10010mpAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpHwInterlock.setStatus("current")
_Pm10010mpAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mpAlmclientGlobalAlarmSummary = _Pm10010mpAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42)
)
_Pm10010mpAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010mpAlmCfpSoftGlobAlarmTest_Object = MibScalar
pm10010mpAlmCfpSoftGlobAlarmTest = _Pm10010mpAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 1),
    _Pm10010mpAlmCfpSoftGlobAlarmTest_Type()
)
pm10010mpAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm10010mpAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010mpAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm10010mpAlmCfpNetworkLaneAlarmWarning2 = _Pm10010mpAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 7),
    _Pm10010mpAlmCfpNetworkLaneAlarmWarning2_Type()
)
pm10010mpAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010mpAlmCfpModuleState_Type = EkiOnOff
_Pm10010mpAlmCfpModuleState_Object = MibScalar
pm10010mpAlmCfpModuleState = _Pm10010mpAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 8),
    _Pm10010mpAlmCfpModuleState_Type()
)
pm10010mpAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpModuleState.setStatus("current")
_Pm10010mpAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm10010mpAlmCfpModuleGeneralStatus_Object = MibScalar
pm10010mpAlmCfpModuleGeneralStatus = _Pm10010mpAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 9),
    _Pm10010mpAlmCfpModuleGeneralStatus_Type()
)
pm10010mpAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpModuleGeneralStatus.setStatus("current")
_Pm10010mpAlmCfpModuleFault_Type = EkiOnOff
_Pm10010mpAlmCfpModuleFault_Object = MibScalar
pm10010mpAlmCfpModuleFault = _Pm10010mpAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 10),
    _Pm10010mpAlmCfpModuleFault_Type()
)
pm10010mpAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpModuleFault.setStatus("current")
_Pm10010mpAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm10010mpAlmCfpModuleAlarmWarning1_Object = MibScalar
pm10010mpAlmCfpModuleAlarmWarning1 = _Pm10010mpAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 11),
    _Pm10010mpAlmCfpModuleAlarmWarning1_Type()
)
pm10010mpAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpModuleAlarmWarning1.setStatus("current")
_Pm10010mpAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm10010mpAlmCfpModuleAlarmWarning2_Object = MibScalar
pm10010mpAlmCfpModuleAlarmWarning2 = _Pm10010mpAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 12),
    _Pm10010mpAlmCfpModuleAlarmWarning2_Type()
)
pm10010mpAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpModuleAlarmWarning2.setStatus("current")
_Pm10010mpAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010mpAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm10010mpAlmCfpNetworkLaneAlarmWarning1 = _Pm10010mpAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 13),
    _Pm10010mpAlmCfpNetworkLaneAlarmWarning1_Type()
)
pm10010mpAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010mpAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010mpAlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm10010mpAlmCfpNetworkLaneFaultStatus = _Pm10010mpAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 14),
    _Pm10010mpAlmCfpNetworkLaneFaultStatus_Type()
)
pm10010mpAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm10010mpAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm10010mpAlmCfpHostLaneFaultStatus_Object = MibScalar
pm10010mpAlmCfpHostLaneFaultStatus = _Pm10010mpAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 15),
    _Pm10010mpAlmCfpHostLaneFaultStatus_Type()
)
pm10010mpAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpHostLaneFaultStatus.setStatus("current")
_Pm10010mpAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm10010mpAlmCfpGlobAlarmAssertion_Object = MibScalar
pm10010mpAlmCfpGlobAlarmAssertion = _Pm10010mpAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 42, 16),
    _Pm10010mpAlmCfpGlobAlarmAssertion_Type()
)
pm10010mpAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmCfpGlobAlarmAssertion.setStatus("current")
_Pm10010mpAlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaModuleState = _Pm10010mpAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46)
)
_Pm10010mpAlmMsaInitialize_Type = EkiOnOff
_Pm10010mpAlmMsaInitialize_Object = MibScalar
pm10010mpAlmMsaInitialize = _Pm10010mpAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 1),
    _Pm10010mpAlmMsaInitialize_Type()
)
pm10010mpAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaInitialize.setStatus("current")
_Pm10010mpAlmMsaLowPower_Type = EkiOnOff
_Pm10010mpAlmMsaLowPower_Object = MibScalar
pm10010mpAlmMsaLowPower = _Pm10010mpAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 2),
    _Pm10010mpAlmMsaLowPower_Type()
)
pm10010mpAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaLowPower.setStatus("current")
_Pm10010mpAlmMsaHighPowerUp_Type = EkiOnOff
_Pm10010mpAlmMsaHighPowerUp_Object = MibScalar
pm10010mpAlmMsaHighPowerUp = _Pm10010mpAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 3),
    _Pm10010mpAlmMsaHighPowerUp_Type()
)
pm10010mpAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaHighPowerUp.setStatus("current")
_Pm10010mpAlmMsaTxOff_Type = EkiOnOff
_Pm10010mpAlmMsaTxOff_Object = MibScalar
pm10010mpAlmMsaTxOff = _Pm10010mpAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 4),
    _Pm10010mpAlmMsaTxOff_Type()
)
pm10010mpAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxOff.setStatus("current")
_Pm10010mpAlmMsaTxTurnOn_Type = EkiOnOff
_Pm10010mpAlmMsaTxTurnOn_Object = MibScalar
pm10010mpAlmMsaTxTurnOn = _Pm10010mpAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 5),
    _Pm10010mpAlmMsaTxTurnOn_Type()
)
pm10010mpAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxTurnOn.setStatus("current")
_Pm10010mpAlmMsaReady_Type = EkiOnOff
_Pm10010mpAlmMsaReady_Object = MibScalar
pm10010mpAlmMsaReady = _Pm10010mpAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 6),
    _Pm10010mpAlmMsaReady_Type()
)
pm10010mpAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaReady.setStatus("current")
_Pm10010mpAlmMsaFault_Type = EkiOnOff
_Pm10010mpAlmMsaFault_Object = MibScalar
pm10010mpAlmMsaFault = _Pm10010mpAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 7),
    _Pm10010mpAlmMsaFault_Type()
)
pm10010mpAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaFault.setStatus("current")
_Pm10010mpAlmMsaTxTurnOff_Type = EkiOnOff
_Pm10010mpAlmMsaTxTurnOff_Object = MibScalar
pm10010mpAlmMsaTxTurnOff = _Pm10010mpAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 8),
    _Pm10010mpAlmMsaTxTurnOff_Type()
)
pm10010mpAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxTurnOff.setStatus("current")
_Pm10010mpAlmMsaHighPowerDown_Type = EkiOnOff
_Pm10010mpAlmMsaHighPowerDown_Object = MibScalar
pm10010mpAlmMsaHighPowerDown = _Pm10010mpAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 46, 9),
    _Pm10010mpAlmMsaHighPowerDown_Type()
)
pm10010mpAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaHighPowerDown.setStatus("current")
_Pm10010mpAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaModuleGeneralStatus = _Pm10010mpAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47)
)
_Pm10010mpAlmMsaOutOfAlignment_Type = EkiOnOff
_Pm10010mpAlmMsaOutOfAlignment_Object = MibScalar
pm10010mpAlmMsaOutOfAlignment = _Pm10010mpAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 4),
    _Pm10010mpAlmMsaOutOfAlignment_Type()
)
pm10010mpAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaOutOfAlignment.setStatus("current")
_Pm10010mpAlmMsaRxNetworkLol_Type = EkiOnOff
_Pm10010mpAlmMsaRxNetworkLol_Object = MibScalar
pm10010mpAlmMsaRxNetworkLol = _Pm10010mpAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 5),
    _Pm10010mpAlmMsaRxNetworkLol_Type()
)
pm10010mpAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaRxNetworkLol.setStatus("current")
_Pm10010mpAlmMsaRxLos_Type = EkiOnOff
_Pm10010mpAlmMsaRxLos_Object = MibScalar
pm10010mpAlmMsaRxLos = _Pm10010mpAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 6),
    _Pm10010mpAlmMsaRxLos_Type()
)
pm10010mpAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaRxLos.setStatus("current")
_Pm10010mpAlmMsaTxHostLol_Type = EkiOnOff
_Pm10010mpAlmMsaTxHostLol_Object = MibScalar
pm10010mpAlmMsaTxHostLol = _Pm10010mpAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 7),
    _Pm10010mpAlmMsaTxHostLol_Type()
)
pm10010mpAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxHostLol.setStatus("current")
_Pm10010mpAlmMsaTxLosf_Type = EkiOnOff
_Pm10010mpAlmMsaTxLosf_Object = MibScalar
pm10010mpAlmMsaTxLosf = _Pm10010mpAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 8),
    _Pm10010mpAlmMsaTxLosf_Type()
)
pm10010mpAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxLosf.setStatus("current")
_Pm10010mpAlmMsaTxCmuLol_Type = EkiOnOff
_Pm10010mpAlmMsaTxCmuLol_Object = MibScalar
pm10010mpAlmMsaTxCmuLol = _Pm10010mpAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 9),
    _Pm10010mpAlmMsaTxCmuLol_Type()
)
pm10010mpAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxCmuLol.setStatus("current")
_Pm10010mpAlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm10010mpAlmMsaTxJitterPllLol_Object = MibScalar
pm10010mpAlmMsaTxJitterPllLol = _Pm10010mpAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 10),
    _Pm10010mpAlmMsaTxJitterPllLol_Type()
)
pm10010mpAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaTxJitterPllLol.setStatus("current")
_Pm10010mpAlmMsaLossOfRefclk_Type = EkiOnOff
_Pm10010mpAlmMsaLossOfRefclk_Object = MibScalar
pm10010mpAlmMsaLossOfRefclk = _Pm10010mpAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 11),
    _Pm10010mpAlmMsaLossOfRefclk_Type()
)
pm10010mpAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaLossOfRefclk.setStatus("current")
_Pm10010mpAlmMsaHwInterlock_Type = EkiOnOff
_Pm10010mpAlmMsaHwInterlock_Object = MibScalar
pm10010mpAlmMsaHwInterlock = _Pm10010mpAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 47, 14),
    _Pm10010mpAlmMsaHwInterlock_Type()
)
pm10010mpAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaHwInterlock.setStatus("current")
_Pm10010mpAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaGlobalAlarmSummary = _Pm10010mpAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48)
)
_Pm10010mpAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm10010mpAlmMsaSoftGlobAlarmTest_Object = MibScalar
pm10010mpAlmMsaSoftGlobAlarmTest = _Pm10010mpAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 1),
    _Pm10010mpAlmMsaSoftGlobAlarmTest_Type()
)
pm10010mpAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm10010mpAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm10010mpAlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm10010mpAlmMsaNetworkHostAlarmStatus = _Pm10010mpAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 6),
    _Pm10010mpAlmMsaNetworkHostAlarmStatus_Type()
)
pm10010mpAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm10010mpAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm10010mpAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm10010mpAlmMsaNetworkLaneAlarmWarning2 = _Pm10010mpAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 7),
    _Pm10010mpAlmMsaNetworkLaneAlarmWarning2_Type()
)
pm10010mpAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm10010mpAlmMsaModuleState_Type = EkiOnOff
_Pm10010mpAlmMsaModuleState_Object = MibScalar
pm10010mpAlmMsaModuleState = _Pm10010mpAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 8),
    _Pm10010mpAlmMsaModuleState_Type()
)
pm10010mpAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaModuleState.setStatus("current")
_Pm10010mpAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm10010mpAlmMsaModuleGeneralStatus_Object = MibScalar
pm10010mpAlmMsaModuleGeneralStatus = _Pm10010mpAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 9),
    _Pm10010mpAlmMsaModuleGeneralStatus_Type()
)
pm10010mpAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaModuleGeneralStatus.setStatus("current")
_Pm10010mpAlmModuleFault_Type = EkiOnOff
_Pm10010mpAlmModuleFault_Object = MibScalar
pm10010mpAlmModuleFault = _Pm10010mpAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 10),
    _Pm10010mpAlmModuleFault_Type()
)
pm10010mpAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmModuleFault.setStatus("current")
_Pm10010mpAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm10010mpAlmMsaModuleAlarmWarning1_Object = MibScalar
pm10010mpAlmMsaModuleAlarmWarning1 = _Pm10010mpAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 11),
    _Pm10010mpAlmMsaModuleAlarmWarning1_Type()
)
pm10010mpAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaModuleAlarmWarning1.setStatus("current")
_Pm10010mpAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm10010mpAlmMsaModuleAlarmWarning2_Object = MibScalar
pm10010mpAlmMsaModuleAlarmWarning2 = _Pm10010mpAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 12),
    _Pm10010mpAlmMsaModuleAlarmWarning2_Type()
)
pm10010mpAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaModuleAlarmWarning2.setStatus("current")
_Pm10010mpAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm10010mpAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm10010mpAlmMsaNetworkLaneAlarmWarning1 = _Pm10010mpAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 13),
    _Pm10010mpAlmMsaNetworkLaneAlarmWarning1_Type()
)
pm10010mpAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm10010mpAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm10010mpAlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm10010mpAlmMsaNetworkLaneFaultStatus = _Pm10010mpAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 14),
    _Pm10010mpAlmMsaNetworkLaneFaultStatus_Type()
)
pm10010mpAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm10010mpAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm10010mpAlmMsaHostLaneFaultStatus_Object = MibScalar
pm10010mpAlmMsaHostLaneFaultStatus = _Pm10010mpAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 15),
    _Pm10010mpAlmMsaHostLaneFaultStatus_Type()
)
pm10010mpAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaHostLaneFaultStatus.setStatus("current")
_Pm10010mpAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm10010mpAlmMsaGlobAlarmAssertion_Object = MibScalar
pm10010mpAlmMsaGlobAlarmAssertion = _Pm10010mpAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 48, 16),
    _Pm10010mpAlmMsaGlobAlarmAssertion_Type()
)
pm10010mpAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmMsaGlobAlarmAssertion.setStatus("current")
_Pm10010mpAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaNetworkTxAlignment = _Pm10010mpAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 49)
)
_Pm10010mpAlmNetTxTimingFault_Type = EkiOnOff
_Pm10010mpAlmNetTxTimingFault_Object = MibScalar
pm10010mpAlmNetTxTimingFault = _Pm10010mpAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 49, 12),
    _Pm10010mpAlmNetTxTimingFault_Type()
)
pm10010mpAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetTxTimingFault.setStatus("current")
_Pm10010mpAlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm10010mpAlmNetTxReferenceClockFault_Object = MibScalar
pm10010mpAlmNetTxReferenceClockFault = _Pm10010mpAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 49, 13),
    _Pm10010mpAlmNetTxReferenceClockFault_Type()
)
pm10010mpAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetTxReferenceClockFault.setStatus("current")
_Pm10010mpAlmNetTxCmuLockFault_Type = EkiOnOff
_Pm10010mpAlmNetTxCmuLockFault_Object = MibScalar
pm10010mpAlmNetTxCmuLockFault = _Pm10010mpAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 49, 14),
    _Pm10010mpAlmNetTxCmuLockFault_Type()
)
pm10010mpAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetTxCmuLockFault.setStatus("current")
_Pm10010mpAlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm10010mpAlmNetTxOutOfAlignment_Object = MibScalar
pm10010mpAlmNetTxOutOfAlignment = _Pm10010mpAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 49, 15),
    _Pm10010mpAlmNetTxOutOfAlignment_Type()
)
pm10010mpAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetTxOutOfAlignment.setStatus("current")
_Pm10010mpAlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm10010mpAlmNetTxLossOfAlignment_Object = MibScalar
pm10010mpAlmNetTxLossOfAlignment = _Pm10010mpAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 49, 16),
    _Pm10010mpAlmNetTxLossOfAlignment_Type()
)
pm10010mpAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetTxLossOfAlignment.setStatus("current")
_Pm10010mpAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaNetworkRxAlignment = _Pm10010mpAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 50)
)
_Pm10010mpAlmNetRxTimingFault_Type = EkiOnOff
_Pm10010mpAlmNetRxTimingFault_Object = MibScalar
pm10010mpAlmNetRxTimingFault = _Pm10010mpAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 50, 12),
    _Pm10010mpAlmNetRxTimingFault_Type()
)
pm10010mpAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetRxTimingFault.setStatus("current")
_Pm10010mpAlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm10010mpAlmNetRxOutOfAlignment_Object = MibScalar
pm10010mpAlmNetRxOutOfAlignment = _Pm10010mpAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 50, 13),
    _Pm10010mpAlmNetRxOutOfAlignment_Type()
)
pm10010mpAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetRxOutOfAlignment.setStatus("current")
_Pm10010mpAlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm10010mpAlmNetRxLossOfAlignment_Object = MibScalar
pm10010mpAlmNetRxLossOfAlignment = _Pm10010mpAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 50, 14),
    _Pm10010mpAlmNetRxLossOfAlignment_Type()
)
pm10010mpAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetRxLossOfAlignment.setStatus("current")
_Pm10010mpAlmNetRxModemLockFault_Type = EkiOnOff
_Pm10010mpAlmNetRxModemLockFault_Object = MibScalar
pm10010mpAlmNetRxModemLockFault = _Pm10010mpAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 50, 15),
    _Pm10010mpAlmNetRxModemLockFault_Type()
)
pm10010mpAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetRxModemLockFault.setStatus("current")
_Pm10010mpAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm10010mpAlmNetRxModemSyncDetectFault_Object = MibScalar
pm10010mpAlmNetRxModemSyncDetectFault = _Pm10010mpAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 50, 16),
    _Pm10010mpAlmNetRxModemSyncDetectFault_Type()
)
pm10010mpAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetRxModemSyncDetectFault.setStatus("current")
_Pm10010mpAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaNetworkHostNetworkAlarmSummary = _Pm10010mpAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51)
)
_Pm10010mpAlmNetworkTxAlignment_Type = EkiOnOff
_Pm10010mpAlmNetworkTxAlignment_Object = MibScalar
pm10010mpAlmNetworkTxAlignment = _Pm10010mpAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51, 11),
    _Pm10010mpAlmNetworkTxAlignment_Type()
)
pm10010mpAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetworkTxAlignment.setStatus("current")
_Pm10010mpAlmNetworkRxAlignment_Type = EkiOnOff
_Pm10010mpAlmNetworkRxAlignment_Object = MibScalar
pm10010mpAlmNetworkRxAlignment = _Pm10010mpAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51, 12),
    _Pm10010mpAlmNetworkRxAlignment_Type()
)
pm10010mpAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetworkRxAlignment.setStatus("current")
_Pm10010mpAlmNetworkRxOtn_Type = EkiOnOff
_Pm10010mpAlmNetworkRxOtn_Object = MibScalar
pm10010mpAlmNetworkRxOtn = _Pm10010mpAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51, 13),
    _Pm10010mpAlmNetworkRxOtn_Type()
)
pm10010mpAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmNetworkRxOtn.setStatus("current")
_Pm10010mpAlmHostRxAlignment_Type = EkiOnOff
_Pm10010mpAlmHostRxAlignment_Object = MibScalar
pm10010mpAlmHostRxAlignment = _Pm10010mpAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51, 14),
    _Pm10010mpAlmHostRxAlignment_Type()
)
pm10010mpAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostRxAlignment.setStatus("current")
_Pm10010mpAlmHostTxAlignment_Type = EkiOnOff
_Pm10010mpAlmHostTxAlignment_Object = MibScalar
pm10010mpAlmHostTxAlignment = _Pm10010mpAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51, 15),
    _Pm10010mpAlmHostTxAlignment_Type()
)
pm10010mpAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostTxAlignment.setStatus("current")
_Pm10010mpAlmHostTxOtnStatus_Type = EkiOnOff
_Pm10010mpAlmHostTxOtnStatus_Object = MibScalar
pm10010mpAlmHostTxOtnStatus = _Pm10010mpAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 51, 16),
    _Pm10010mpAlmHostTxOtnStatus_Type()
)
pm10010mpAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostTxOtnStatus.setStatus("current")
_Pm10010mpAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaHostTxAlignment = _Pm10010mpAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 52)
)
_Pm10010mpAlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm10010mpAlmHostTxDeskewLockFault_Object = MibScalar
pm10010mpAlmHostTxDeskewLockFault = _Pm10010mpAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 52, 13),
    _Pm10010mpAlmHostTxDeskewLockFault_Type()
)
pm10010mpAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostTxDeskewLockFault.setStatus("current")
_Pm10010mpAlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm10010mpAlmHostTxOutOfAlignment_Object = MibScalar
pm10010mpAlmHostTxOutOfAlignment = _Pm10010mpAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 52, 14),
    _Pm10010mpAlmHostTxOutOfAlignment_Type()
)
pm10010mpAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostTxOutOfAlignment.setStatus("current")
_Pm10010mpAlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm10010mpAlmHostTxLossOfAlignment_Object = MibScalar
pm10010mpAlmHostTxLossOfAlignment = _Pm10010mpAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 52, 15),
    _Pm10010mpAlmHostTxLossOfAlignment_Type()
)
pm10010mpAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostTxLossOfAlignment.setStatus("current")
_Pm10010mpAlmHostTxCdrLockFault_Type = EkiOnOff
_Pm10010mpAlmHostTxCdrLockFault_Object = MibScalar
pm10010mpAlmHostTxCdrLockFault = _Pm10010mpAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 52, 16),
    _Pm10010mpAlmHostTxCdrLockFault_Type()
)
pm10010mpAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostTxCdrLockFault.setStatus("current")
_Pm10010mpAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm10010mpAlmmsaHostRxAlignment = _Pm10010mpAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 53)
)
_Pm10010mpAlmHostRxCmuLockFault_Type = EkiOnOff
_Pm10010mpAlmHostRxCmuLockFault_Object = MibScalar
pm10010mpAlmHostRxCmuLockFault = _Pm10010mpAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 53, 14),
    _Pm10010mpAlmHostRxCmuLockFault_Type()
)
pm10010mpAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostRxCmuLockFault.setStatus("current")
_Pm10010mpAlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm10010mpAlmHostRxOutOfAlignment_Object = MibScalar
pm10010mpAlmHostRxOutOfAlignment = _Pm10010mpAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 53, 15),
    _Pm10010mpAlmHostRxOutOfAlignment_Type()
)
pm10010mpAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostRxOutOfAlignment.setStatus("current")
_Pm10010mpAlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm10010mpAlmHostRxLossOfAlignment_Object = MibScalar
pm10010mpAlmHostRxLossOfAlignment = _Pm10010mpAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 1, 3, 53, 16),
    _Pm10010mpAlmHostRxLossOfAlignment_Type()
)
pm10010mpAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHostRxLossOfAlignment.setStatus("current")
_Pm10010mpAlmClient_ObjectIdentity = ObjectIdentity
pm10010mpAlmClient = _Pm10010mpAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2)
)
_Pm10010mpAlmClientNurg_ObjectIdentity = ObjectIdentity
pm10010mpAlmClientNurg = _Pm10010mpAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1)
)
_Pm10010mpAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pm10010mpAlmclientNetworkLaneAlarmWarningTable = _Pm10010mpAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pm10010mpAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pm10010mpAlmclientNetworkLaneAlarmWarningEntry = _Pm10010mpAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1)
)
pm10010mpAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pm10010mpAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pm10010mpAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pm10010mpAlmclientNetworkLaneAlarmWarningIndex = _Pm10010mpAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 1),
    _Pm10010mpAlmclientNetworkLaneAlarmWarningIndex_Type()
)
pm10010mpAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pm10010mpAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientRxPowerLowAlarmPortn = _Pm10010mpAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 2),
    _Pm10010mpAlmClientRxPowerLowAlarmPortn_Type()
)
pm10010mpAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pm10010mpAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pm10010mpAlmClientRxPowerLowWarningPortn = _Pm10010mpAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 3),
    _Pm10010mpAlmClientRxPowerLowWarningPortn_Type()
)
pm10010mpAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientRxPowerLowWarningPortn.setStatus("current")
_Pm10010mpAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pm10010mpAlmClientRxPowerHighWarningPortn = _Pm10010mpAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 4),
    _Pm10010mpAlmClientRxPowerHighWarningPortn_Type()
)
pm10010mpAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientRxPowerHighWarningPortn.setStatus("current")
_Pm10010mpAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientRxPowerHighAlarmPortn = _Pm10010mpAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 5),
    _Pm10010mpAlmClientRxPowerHighAlarmPortn_Type()
)
pm10010mpAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pm10010mpAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmLaserTempLowAlarmPortn = _Pm10010mpAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 6),
    _Pm10010mpAlmLaserTempLowAlarmPortn_Type()
)
pm10010mpAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mpAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mpAlmClientLaserTempLowWarningPortn = _Pm10010mpAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 7),
    _Pm10010mpAlmClientLaserTempLowWarningPortn_Type()
)
pm10010mpAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaserTempLowWarningPortn.setStatus("current")
_Pm10010mpAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mpAlmClientLaserTempHighWarningPortn = _Pm10010mpAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 8),
    _Pm10010mpAlmClientLaserTempHighWarningPortn_Type()
)
pm10010mpAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaserTempHighWarningPortn.setStatus("current")
_Pm10010mpAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientLaserTempHighAlarmPortn = _Pm10010mpAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 9),
    _Pm10010mpAlmClientLaserTempHighAlarmPortn_Type()
)
pm10010mpAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mpAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientTxPowerLowAlarmPortn = _Pm10010mpAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 10),
    _Pm10010mpAlmClientTxPowerLowAlarmPortn_Type()
)
pm10010mpAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pm10010mpAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pm10010mpAlmClientTxPowerLowWarningPortn = _Pm10010mpAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 11),
    _Pm10010mpAlmClientTxPowerLowWarningPortn_Type()
)
pm10010mpAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientTxPowerLowWarningPortn.setStatus("current")
_Pm10010mpAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pm10010mpAlmClientTxPowerHighWarningPortn = _Pm10010mpAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 12),
    _Pm10010mpAlmClientTxPowerHighWarningPortn_Type()
)
pm10010mpAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientTxPowerHighWarningPortn.setStatus("current")
_Pm10010mpAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientTxPowerHighAlarmPortn = _Pm10010mpAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 13),
    _Pm10010mpAlmClientTxPowerHighAlarmPortn_Type()
)
pm10010mpAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pm10010mpAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientBiasLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientBiasLowAlarmPortn = _Pm10010mpAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 14),
    _Pm10010mpAlmClientBiasLowAlarmPortn_Type()
)
pm10010mpAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientBiasLowAlarmPortn.setStatus("current")
_Pm10010mpAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientBiasLowWarningPortn_Object = MibTableColumn
pm10010mpAlmClientBiasLowWarningPortn = _Pm10010mpAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 15),
    _Pm10010mpAlmClientBiasLowWarningPortn_Type()
)
pm10010mpAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientBiasLowWarningPortn.setStatus("current")
_Pm10010mpAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmClientBiasHighWarningPortn_Object = MibTableColumn
pm10010mpAlmClientBiasHighWarningPortn = _Pm10010mpAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 16),
    _Pm10010mpAlmClientBiasHighWarningPortn_Type()
)
pm10010mpAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientBiasHighWarningPortn.setStatus("current")
_Pm10010mpAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmClientBiasHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmClientBiasHighAlarmPortn = _Pm10010mpAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 56, 1, 17),
    _Pm10010mpAlmClientBiasHighAlarmPortn_Type()
)
pm10010mpAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientBiasHighAlarmPortn.setStatus("current")
_Pm10010mpAlmclientSfpWarnDdmTable_Object = MibTable
pm10010mpAlmclientSfpWarnDdmTable = _Pm10010mpAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientSfpWarnDdmTable.setStatus("current")
_Pm10010mpAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm10010mpAlmclientSfpWarnDdmEntry = _Pm10010mpAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1)
)
pm10010mpAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm10010mpAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm10010mpAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm10010mpAlmclientSfpWarnDdmIndex = _Pm10010mpAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 1),
    _Pm10010mpAlmclientSfpWarnDdmIndex_Type()
)
pm10010mpAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm10010mpAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm10010mpAlmTxPwLowWngPortn_Object = MibTableColumn
pm10010mpAlmTxPwLowWngPortn = _Pm10010mpAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 2),
    _Pm10010mpAlmTxPwLowWngPortn_Type()
)
pm10010mpAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxPwLowWngPortn.setStatus("current")
_Pm10010mpAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm10010mpAlmTxPwrHighWngPortn_Object = MibTableColumn
pm10010mpAlmTxPwrHighWngPortn = _Pm10010mpAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 3),
    _Pm10010mpAlmTxPwrHighWngPortn_Type()
)
pm10010mpAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxPwrHighWngPortn.setStatus("current")
_Pm10010mpAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm10010mpAlmTxBiasLowWngPortn_Object = MibTableColumn
pm10010mpAlmTxBiasLowWngPortn = _Pm10010mpAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 4),
    _Pm10010mpAlmTxBiasLowWngPortn_Type()
)
pm10010mpAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxBiasLowWngPortn.setStatus("current")
_Pm10010mpAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm10010mpAlmTxBiasHighWngPortn_Object = MibTableColumn
pm10010mpAlmTxBiasHighWngPortn = _Pm10010mpAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 5),
    _Pm10010mpAlmTxBiasHighWngPortn_Type()
)
pm10010mpAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxBiasHighWngPortn.setStatus("current")
_Pm10010mpAlmVccLowWngPortn_Type = EkiOnOff
_Pm10010mpAlmVccLowWngPortn_Object = MibTableColumn
pm10010mpAlmVccLowWngPortn = _Pm10010mpAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 6),
    _Pm10010mpAlmVccLowWngPortn_Type()
)
pm10010mpAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmVccLowWngPortn.setStatus("current")
_Pm10010mpAlmVccHighWngPortn_Type = EkiOnOff
_Pm10010mpAlmVccHighWngPortn_Object = MibTableColumn
pm10010mpAlmVccHighWngPortn = _Pm10010mpAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 7),
    _Pm10010mpAlmVccHighWngPortn_Type()
)
pm10010mpAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmVccHighWngPortn.setStatus("current")
_Pm10010mpAlmTempLowWngPortn_Type = EkiOnOff
_Pm10010mpAlmTempLowWngPortn_Object = MibTableColumn
pm10010mpAlmTempLowWngPortn = _Pm10010mpAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 8),
    _Pm10010mpAlmTempLowWngPortn_Type()
)
pm10010mpAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTempLowWngPortn.setStatus("current")
_Pm10010mpAlmTempHighWngPortn_Type = EkiOnOff
_Pm10010mpAlmTempHighWngPortn_Object = MibTableColumn
pm10010mpAlmTempHighWngPortn = _Pm10010mpAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 9),
    _Pm10010mpAlmTempHighWngPortn_Type()
)
pm10010mpAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTempHighWngPortn.setStatus("current")
_Pm10010mpAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm10010mpAlmRxPwrLowWngPortn_Object = MibTableColumn
pm10010mpAlmRxPwrLowWngPortn = _Pm10010mpAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 16),
    _Pm10010mpAlmRxPwrLowWngPortn_Type()
)
pm10010mpAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxPwrLowWngPortn.setStatus("current")
_Pm10010mpAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm10010mpAlmRxPwrHighWngPortn_Object = MibTableColumn
pm10010mpAlmRxPwrHighWngPortn = _Pm10010mpAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 1, 232, 1, 17),
    _Pm10010mpAlmRxPwrHighWngPortn_Type()
)
pm10010mpAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxPwrHighWngPortn.setStatus("current")
_Pm10010mpAlmClientUrg_ObjectIdentity = ObjectIdentity
pm10010mpAlmClientUrg = _Pm10010mpAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2)
)
_Pm10010mpAlmclientNetworkLaneFaultTable_Object = MibTable
pm10010mpAlmclientNetworkLaneFaultTable = _Pm10010mpAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientNetworkLaneFaultTable.setStatus("current")
_Pm10010mpAlmclientNetworkLaneFaultEntry_Object = MibTableRow
pm10010mpAlmclientNetworkLaneFaultEntry = _Pm10010mpAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1)
)
pm10010mpAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pm10010mpAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mpAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pm10010mpAlmclientNetworkLaneFaultIndex = _Pm10010mpAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 1),
    _Pm10010mpAlmclientNetworkLaneFaultIndex_Type()
)
pm10010mpAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmclientNetworkLaneFaultIndex.setStatus("current")
_Pm10010mpAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010mpAlmClientLaneRxFifoErrorPortn = _Pm10010mpAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 4),
    _Pm10010mpAlmClientLaneRxFifoErrorPortn_Type()
)
pm10010mpAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pm10010mpAlmClientLaneRxLolPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneRxLolPortn_Object = MibTableColumn
pm10010mpAlmClientLaneRxLolPortn = _Pm10010mpAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 5),
    _Pm10010mpAlmClientLaneRxLolPortn_Type()
)
pm10010mpAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneRxLolPortn.setStatus("current")
_Pm10010mpAlmClientLaneRxLosPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneRxLosPortn_Object = MibTableColumn
pm10010mpAlmClientLaneRxLosPortn = _Pm10010mpAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 6),
    _Pm10010mpAlmClientLaneRxLosPortn_Type()
)
pm10010mpAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneRxLosPortn.setStatus("current")
_Pm10010mpAlmClientLaneTxLolPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneTxLolPortn_Object = MibTableColumn
pm10010mpAlmClientLaneTxLolPortn = _Pm10010mpAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 8),
    _Pm10010mpAlmClientLaneTxLolPortn_Type()
)
pm10010mpAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneTxLolPortn.setStatus("current")
_Pm10010mpAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneTxLosfPortn_Object = MibTableColumn
pm10010mpAlmClientLaneTxLosfPortn = _Pm10010mpAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 9),
    _Pm10010mpAlmClientLaneTxLosfPortn_Type()
)
pm10010mpAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneTxLosfPortn.setStatus("current")
_Pm10010mpAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010mpAlmClientLaneApdPowerSupplyPortn = _Pm10010mpAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 15),
    _Pm10010mpAlmClientLaneApdPowerSupplyPortn_Type()
)
pm10010mpAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010mpAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010mpAlmClientLaneWavelengthUnlockedPortn = _Pm10010mpAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 16),
    _Pm10010mpAlmClientLaneWavelengthUnlockedPortn_Type()
)
pm10010mpAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010mpAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneTecFaultPortn_Object = MibTableColumn
pm10010mpAlmClientLaneTecFaultPortn = _Pm10010mpAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 72, 1, 17),
    _Pm10010mpAlmClientLaneTecFaultPortn_Type()
)
pm10010mpAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneTecFaultPortn.setStatus("current")
_Pm10010mpAlmclientHostLaneFaultTable_Object = MibTable
pm10010mpAlmclientHostLaneFaultTable = _Pm10010mpAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientHostLaneFaultTable.setStatus("current")
_Pm10010mpAlmclientHostLaneFaultEntry_Object = MibTableRow
pm10010mpAlmclientHostLaneFaultEntry = _Pm10010mpAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1)
)
pm10010mpAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientHostLaneFaultEntry.setStatus("current")


class _Pm10010mpAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mpAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmclientHostLaneFaultIndex_Object = MibTableColumn
pm10010mpAlmclientHostLaneFaultIndex = _Pm10010mpAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 1),
    _Pm10010mpAlmclientHostLaneFaultIndex_Type()
)
pm10010mpAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmclientHostLaneFaultIndex.setStatus("current")
_Pm10010mpAlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm10010mpAlmClientLossOfSyncPortn_Object = MibTableColumn
pm10010mpAlmClientLossOfSyncPortn = _Pm10010mpAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 2),
    _Pm10010mpAlmClientLossOfSyncPortn_Type()
)
pm10010mpAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLossOfSyncPortn.setStatus("current")
_Pm10010mpAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm10010mpAlmClientInputLossOfSigPortn_Object = MibTableColumn
pm10010mpAlmClientInputLossOfSigPortn = _Pm10010mpAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 3),
    _Pm10010mpAlmClientInputLossOfSigPortn_Type()
)
pm10010mpAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientInputLossOfSigPortn.setStatus("current")
_Pm10010mpAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm10010mpAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm10010mpAlmClientLanesMarkerUnlockPortn = _Pm10010mpAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 4),
    _Pm10010mpAlmClientLanesMarkerUnlockPortn_Type()
)
pm10010mpAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm10010mpAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm10010mpAlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm10010mpAlmClientLanes6466UnlockPortn = _Pm10010mpAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 5),
    _Pm10010mpAlmClientLanes6466UnlockPortn_Type()
)
pm10010mpAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLanes6466UnlockPortn.setStatus("current")
_Pm10010mpAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm10010mpAlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm10010mpAlmClientLanesNotAlignedPortn = _Pm10010mpAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 6),
    _Pm10010mpAlmClientLanesNotAlignedPortn_Type()
)
pm10010mpAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLanesNotAlignedPortn.setStatus("current")
_Pm10010mpAlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm10010mpAlmClientCsfDetectedPortn_Object = MibTableColumn
pm10010mpAlmClientCsfDetectedPortn = _Pm10010mpAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 7),
    _Pm10010mpAlmClientCsfDetectedPortn_Type()
)
pm10010mpAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientCsfDetectedPortn.setStatus("current")
_Pm10010mpAlmClientTxHostLolPortn_Type = EkiOnOff
_Pm10010mpAlmClientTxHostLolPortn_Object = MibTableColumn
pm10010mpAlmClientTxHostLolPortn = _Pm10010mpAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 10),
    _Pm10010mpAlmClientTxHostLolPortn_Type()
)
pm10010mpAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientTxHostLolPortn.setStatus("current")
_Pm10010mpAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010mpAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010mpAlmClientLaneTxFifoErrorPortn = _Pm10010mpAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 88, 1, 11),
    _Pm10010mpAlmClientLaneTxFifoErrorPortn_Type()
)
pm10010mpAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm10010mpAlmclientSfpAlmDdmTable_Object = MibTable
pm10010mpAlmclientSfpAlmDdmTable = _Pm10010mpAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientSfpAlmDdmTable.setStatus("current")
_Pm10010mpAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm10010mpAlmclientSfpAlmDdmEntry = _Pm10010mpAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1)
)
pm10010mpAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm10010mpAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm10010mpAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm10010mpAlmclientSfpAlmDdmIndex = _Pm10010mpAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 1),
    _Pm10010mpAlmclientSfpAlmDdmIndex_Type()
)
pm10010mpAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm10010mpAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010mpAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm10010mpAlmTxPwrLowAlaPortn = _Pm10010mpAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 2),
    _Pm10010mpAlmTxPwrLowAlaPortn_Type()
)
pm10010mpAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxPwrLowAlaPortn.setStatus("current")
_Pm10010mpAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010mpAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm10010mpAlmTxPwrHighAlaPortn = _Pm10010mpAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 3),
    _Pm10010mpAlmTxPwrHighAlaPortn_Type()
)
pm10010mpAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxPwrHighAlaPortn.setStatus("current")
_Pm10010mpAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm10010mpAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm10010mpAlmTxBiasLowAlaPortn = _Pm10010mpAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 4),
    _Pm10010mpAlmTxBiasLowAlaPortn_Type()
)
pm10010mpAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxBiasLowAlaPortn.setStatus("current")
_Pm10010mpAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm10010mpAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm10010mpAlmTxBiasHighAlaPortn = _Pm10010mpAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 5),
    _Pm10010mpAlmTxBiasHighAlaPortn_Type()
)
pm10010mpAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxBiasHighAlaPortn.setStatus("current")
_Pm10010mpAlmVccLowAlaPortn_Type = EkiOnOff
_Pm10010mpAlmVccLowAlaPortn_Object = MibTableColumn
pm10010mpAlmVccLowAlaPortn = _Pm10010mpAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 6),
    _Pm10010mpAlmVccLowAlaPortn_Type()
)
pm10010mpAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmVccLowAlaPortn.setStatus("current")
_Pm10010mpAlmVccHighAlaPortn_Type = EkiOnOff
_Pm10010mpAlmVccHighAlaPortn_Object = MibTableColumn
pm10010mpAlmVccHighAlaPortn = _Pm10010mpAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 7),
    _Pm10010mpAlmVccHighAlaPortn_Type()
)
pm10010mpAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmVccHighAlaPortn.setStatus("current")
_Pm10010mpAlmTempLowAlaPortn_Type = EkiOnOff
_Pm10010mpAlmTempLowAlaPortn_Object = MibTableColumn
pm10010mpAlmTempLowAlaPortn = _Pm10010mpAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 8),
    _Pm10010mpAlmTempLowAlaPortn_Type()
)
pm10010mpAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTempLowAlaPortn.setStatus("current")
_Pm10010mpAlmTempHighAlaPortn_Type = EkiOnOff
_Pm10010mpAlmTempHighAlaPortn_Object = MibTableColumn
pm10010mpAlmTempHighAlaPortn = _Pm10010mpAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 9),
    _Pm10010mpAlmTempHighAlaPortn_Type()
)
pm10010mpAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTempHighAlaPortn.setStatus("current")
_Pm10010mpAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm10010mpAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm10010mpAlmRxPwrLowAlaPortn = _Pm10010mpAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 16),
    _Pm10010mpAlmRxPwrLowAlaPortn_Type()
)
pm10010mpAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxPwrLowAlaPortn.setStatus("current")
_Pm10010mpAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm10010mpAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm10010mpAlmRxPwrHighAlaPortn = _Pm10010mpAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 2, 216, 1, 17),
    _Pm10010mpAlmRxPwrHighAlaPortn_Type()
)
pm10010mpAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxPwrHighAlaPortn.setStatus("current")
_Pm10010mpAlmClientCrit_ObjectIdentity = ObjectIdentity
pm10010mpAlmClientCrit = _Pm10010mpAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3)
)
_Pm10010mpAlmsynthAlmPortTable_Object = MibTable
pm10010mpAlmsynthAlmPortTable = _Pm10010mpAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm10010mpAlmsynthAlmPortTable.setStatus("current")
_Pm10010mpAlmsynthAlmPortEntry_Object = MibTableRow
pm10010mpAlmsynthAlmPortEntry = _Pm10010mpAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1)
)
pm10010mpAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmsynthAlmPortEntry.setStatus("current")


class _Pm10010mpAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm10010mpAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmsynthAlmPortIndex_Object = MibTableColumn
pm10010mpAlmsynthAlmPortIndex = _Pm10010mpAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 1),
    _Pm10010mpAlmsynthAlmPortIndex_Type()
)
pm10010mpAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmsynthAlmPortIndex.setStatus("current")
_Pm10010mpAlmSfpAbsentPortn_Type = EkiOnOff
_Pm10010mpAlmSfpAbsentPortn_Object = MibTableColumn
pm10010mpAlmSfpAbsentPortn = _Pm10010mpAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 2),
    _Pm10010mpAlmSfpAbsentPortn_Type()
)
pm10010mpAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmSfpAbsentPortn.setStatus("current")
_Pm10010mpAlmDdmAbsentPortn_Type = EkiOnOff
_Pm10010mpAlmDdmAbsentPortn_Object = MibTableColumn
pm10010mpAlmDdmAbsentPortn = _Pm10010mpAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 3),
    _Pm10010mpAlmDdmAbsentPortn_Type()
)
pm10010mpAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmDdmAbsentPortn.setStatus("current")
_Pm10010mpAlmHwFailAccPortn_Type = EkiOnOff
_Pm10010mpAlmHwFailAccPortn_Object = MibTableColumn
pm10010mpAlmHwFailAccPortn = _Pm10010mpAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 5),
    _Pm10010mpAlmHwFailAccPortn_Type()
)
pm10010mpAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmHwFailAccPortn.setStatus("current")
_Pm10010mpAlmDwLsdPortn_Type = EkiOnOff
_Pm10010mpAlmDwLsdPortn_Object = MibTableColumn
pm10010mpAlmDwLsdPortn = _Pm10010mpAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 6),
    _Pm10010mpAlmDwLsdPortn_Type()
)
pm10010mpAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmDwLsdPortn.setStatus("current")
_Pm10010mpAlmClientLocalOosPortn_Type = EkiOnOff
_Pm10010mpAlmClientLocalOosPortn_Object = MibTableColumn
pm10010mpAlmClientLocalOosPortn = _Pm10010mpAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 7),
    _Pm10010mpAlmClientLocalOosPortn_Type()
)
pm10010mpAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientLocalOosPortn.setStatus("current")
_Pm10010mpAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm10010mpAlmClientRemoteOosPortn_Object = MibTableColumn
pm10010mpAlmClientRemoteOosPortn = _Pm10010mpAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 8),
    _Pm10010mpAlmClientRemoteOosPortn_Type()
)
pm10010mpAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmClientRemoteOosPortn.setStatus("current")
_Pm10010mpAlmDwCaisPortn_Type = EkiOnOff
_Pm10010mpAlmDwCaisPortn_Object = MibTableColumn
pm10010mpAlmDwCaisPortn = _Pm10010mpAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 9),
    _Pm10010mpAlmDwCaisPortn_Type()
)
pm10010mpAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmDwCaisPortn.setStatus("current")
_Pm10010mpAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm10010mpAlmSfpDdmWarningPortn_Object = MibTableColumn
pm10010mpAlmSfpDdmWarningPortn = _Pm10010mpAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 10),
    _Pm10010mpAlmSfpDdmWarningPortn_Type()
)
pm10010mpAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmSfpDdmWarningPortn.setStatus("current")
_Pm10010mpAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm10010mpAlmSfpDdmAlmPortn_Object = MibTableColumn
pm10010mpAlmSfpDdmAlmPortn = _Pm10010mpAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 11),
    _Pm10010mpAlmSfpDdmAlmPortn_Type()
)
pm10010mpAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmSfpDdmAlmPortn.setStatus("current")
_Pm10010mpAlmFailAccPortn_Type = EkiOnOff
_Pm10010mpAlmFailAccPortn_Object = MibTableColumn
pm10010mpAlmFailAccPortn = _Pm10010mpAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 13),
    _Pm10010mpAlmFailAccPortn_Type()
)
pm10010mpAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmFailAccPortn.setStatus("current")
_Pm10010mpAlmUpCsfPortn_Type = EkiOnOff
_Pm10010mpAlmUpCsfPortn_Object = MibTableColumn
pm10010mpAlmUpCsfPortn = _Pm10010mpAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 2, 3, 8, 1, 17),
    _Pm10010mpAlmUpCsfPortn_Type()
)
pm10010mpAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmUpCsfPortn.setStatus("current")
_Pm10010mpAlmLine_ObjectIdentity = ObjectIdentity
pm10010mpAlmLine = _Pm10010mpAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3)
)
_Pm10010mpAlmLineNurg_ObjectIdentity = ObjectIdentity
pm10010mpAlmLineNurg = _Pm10010mpAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1)
)
_Pm10010mpAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm10010mpAlmlineNetworkLaneAlarmWarning1Table = _Pm10010mpAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104)
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm10010mpAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm10010mpAlmlineNetworkLaneAlarmWarning1Entry = _Pm10010mpAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1)
)
pm10010mpAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm10010mpAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm10010mpAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm10010mpAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm10010mpAlmlineNetworkLaneAlarmWarning1Index = _Pm10010mpAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 1),
    _Pm10010mpAlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm10010mpAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm10010mpAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineRxPowerLowAlarmPortn = _Pm10010mpAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 2),
    _Pm10010mpAlmLineRxPowerLowAlarmPortn_Type()
)
pm10010mpAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm10010mpAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm10010mpAlmLineRxPowerLowWarningPortn = _Pm10010mpAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 3),
    _Pm10010mpAlmLineRxPowerLowWarningPortn_Type()
)
pm10010mpAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm10010mpAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm10010mpAlmLineRxPowerHighWarningPortn = _Pm10010mpAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 4),
    _Pm10010mpAlmLineRxPowerHighWarningPortn_Type()
)
pm10010mpAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm10010mpAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineRxPowerHighAlarmPortn = _Pm10010mpAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 5),
    _Pm10010mpAlmLineRxPowerHighAlarmPortn_Type()
)
pm10010mpAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm10010mpAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineLaserTempLowAlarmPortn = _Pm10010mpAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 6),
    _Pm10010mpAlmLineLaserTempLowAlarmPortn_Type()
)
pm10010mpAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mpAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mpAlmLineLaserTempLowWarningPortn = _Pm10010mpAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 7),
    _Pm10010mpAlmLineLaserTempLowWarningPortn_Type()
)
pm10010mpAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm10010mpAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mpAlmLineLaserTempHighWarningPortn = _Pm10010mpAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 8),
    _Pm10010mpAlmLineLaserTempHighWarningPortn_Type()
)
pm10010mpAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm10010mpAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineLaserTempHighAlarmPortn = _Pm10010mpAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 9),
    _Pm10010mpAlmLineLaserTempHighAlarmPortn_Type()
)
pm10010mpAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mpAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineTxPowerLowAlarmPortn = _Pm10010mpAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 10),
    _Pm10010mpAlmLineTxPowerLowAlarmPortn_Type()
)
pm10010mpAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm10010mpAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm10010mpAlmLineTxPowerLowWarningPortn = _Pm10010mpAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 11),
    _Pm10010mpAlmLineTxPowerLowWarningPortn_Type()
)
pm10010mpAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm10010mpAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm10010mpAlmLineTxPowerHighWarningPortn = _Pm10010mpAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 12),
    _Pm10010mpAlmLineTxPowerHighWarningPortn_Type()
)
pm10010mpAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm10010mpAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineTxPowerHighAlarmPortn = _Pm10010mpAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 13),
    _Pm10010mpAlmLineTxPowerHighAlarmPortn_Type()
)
pm10010mpAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm10010mpAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineBiasLowAlarmPortn = _Pm10010mpAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 14),
    _Pm10010mpAlmLineBiasLowAlarmPortn_Type()
)
pm10010mpAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineBiasLowAlarmPortn.setStatus("current")
_Pm10010mpAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineBiasLowWarningPortn_Object = MibTableColumn
pm10010mpAlmLineBiasLowWarningPortn = _Pm10010mpAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 15),
    _Pm10010mpAlmLineBiasLowWarningPortn_Type()
)
pm10010mpAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineBiasLowWarningPortn.setStatus("current")
_Pm10010mpAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineBiasHighWarningPortn_Object = MibTableColumn
pm10010mpAlmLineBiasHighWarningPortn = _Pm10010mpAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 16),
    _Pm10010mpAlmLineBiasHighWarningPortn_Type()
)
pm10010mpAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineBiasHighWarningPortn.setStatus("current")
_Pm10010mpAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmLineBiasHighAlarmPortn = _Pm10010mpAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 104, 1, 17),
    _Pm10010mpAlmLineBiasHighAlarmPortn_Type()
)
pm10010mpAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineBiasHighAlarmPortn.setStatus("current")
_Pm10010mpAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm10010mpAlmlineNetworkLaneAlarmWarning2Table = _Pm10010mpAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120)
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm10010mpAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm10010mpAlmlineNetworkLaneAlarmWarning2Entry = _Pm10010mpAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1)
)
pm10010mpAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm10010mpAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm10010mpAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm10010mpAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm10010mpAlmlineNetworkLaneAlarmWarning2Index = _Pm10010mpAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 1),
    _Pm10010mpAlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm10010mpAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm10010mpAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmTxModulatorBiasLowAlarmPortn = _Pm10010mpAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 2),
    _Pm10010mpAlmTxModulatorBiasLowAlarmPortn_Type()
)
pm10010mpAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm10010mpAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm10010mpAlmTxModulatorBiasLowWarningPortn = _Pm10010mpAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 3),
    _Pm10010mpAlmTxModulatorBiasLowWarningPortn_Type()
)
pm10010mpAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm10010mpAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm10010mpAlmTxModulatorBiasHighWarningPortn = _Pm10010mpAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 4),
    _Pm10010mpAlmTxModulatorBiasHighWarningPortn_Type()
)
pm10010mpAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm10010mpAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmTxModulatorBiasHighAlarmPortn = _Pm10010mpAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 5),
    _Pm10010mpAlmTxModulatorBiasHighAlarmPortn_Type()
)
pm10010mpAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm10010mpAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmRxLaserTempLowAlarmPortn = _Pm10010mpAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 6),
    _Pm10010mpAlmRxLaserTempLowAlarmPortn_Type()
)
pm10010mpAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm10010mpAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm10010mpAlmRxLaserTempLowWarningPortn = _Pm10010mpAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 7),
    _Pm10010mpAlmRxLaserTempLowWarningPortn_Type()
)
pm10010mpAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm10010mpAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm10010mpAlmRxLaserTempHighWarningPortn = _Pm10010mpAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 8),
    _Pm10010mpAlmRxLaserTempHighWarningPortn_Type()
)
pm10010mpAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm10010mpAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmRxLaserTempHighAlarmPortn = _Pm10010mpAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 9),
    _Pm10010mpAlmRxLaserTempHighAlarmPortn_Type()
)
pm10010mpAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm10010mpAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmRxLaserOutputLowAlarmPortn = _Pm10010mpAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 10),
    _Pm10010mpAlmRxLaserOutputLowAlarmPortn_Type()
)
pm10010mpAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm10010mpAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm10010mpAlmRxLaserOutputLowWarningPortn = _Pm10010mpAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 11),
    _Pm10010mpAlmRxLaserOutputLowWarningPortn_Type()
)
pm10010mpAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm10010mpAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm10010mpAlmRxLaserOutputHighWarningPortn = _Pm10010mpAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 12),
    _Pm10010mpAlmRxLaserOutputHighWarningPortn_Type()
)
pm10010mpAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm10010mpAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmRxLaserOutputHighAlarmPortn = _Pm10010mpAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 13),
    _Pm10010mpAlmRxLaserOutputHighAlarmPortn_Type()
)
pm10010mpAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm10010mpAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm10010mpAlmRxLaserBiasLowAlarmPortn = _Pm10010mpAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 14),
    _Pm10010mpAlmRxLaserBiasLowAlarmPortn_Type()
)
pm10010mpAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm10010mpAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm10010mpAlmRxLaserBiasLowWarningPortn = _Pm10010mpAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 15),
    _Pm10010mpAlmRxLaserBiasLowWarningPortn_Type()
)
pm10010mpAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm10010mpAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm10010mpAlmRxLaserBiasHighWarningPortn = _Pm10010mpAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 16),
    _Pm10010mpAlmRxLaserBiasHighWarningPortn_Type()
)
pm10010mpAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm10010mpAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm10010mpAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm10010mpAlmRxLaserBiasHighAlarmPortn = _Pm10010mpAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 1, 120, 1, 17),
    _Pm10010mpAlmRxLaserBiasHighAlarmPortn_Type()
)
pm10010mpAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm10010mpAlmLineUrg_ObjectIdentity = ObjectIdentity
pm10010mpAlmLineUrg = _Pm10010mpAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2)
)
_Pm10010mpAlmlineNetworkLaneFaultTable_Object = MibTable
pm10010mpAlmlineNetworkLaneFaultTable = _Pm10010mpAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136)
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneFaultTable.setStatus("current")
_Pm10010mpAlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm10010mpAlmlineNetworkLaneFaultEntry = _Pm10010mpAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1)
)
pm10010mpAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm10010mpAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mpAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm10010mpAlmlineNetworkLaneFaultIndex = _Pm10010mpAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 1),
    _Pm10010mpAlmlineNetworkLaneFaultIndex_Type()
)
pm10010mpAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm10010mpAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm10010mpAlmLineLaneRxTecFaultPortn = _Pm10010mpAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 3),
    _Pm10010mpAlmLineLaneRxTecFaultPortn_Type()
)
pm10010mpAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm10010mpAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm10010mpAlmLineLaneRxFifoErrorPortn = _Pm10010mpAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 4),
    _Pm10010mpAlmLineLaneRxFifoErrorPortn_Type()
)
pm10010mpAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm10010mpAlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneRxLolPortn_Object = MibTableColumn
pm10010mpAlmLineLaneRxLolPortn = _Pm10010mpAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 5),
    _Pm10010mpAlmLineLaneRxLolPortn_Type()
)
pm10010mpAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneRxLolPortn.setStatus("current")
_Pm10010mpAlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneRxLosPortn_Object = MibTableColumn
pm10010mpAlmLineLaneRxLosPortn = _Pm10010mpAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 6),
    _Pm10010mpAlmLineLaneRxLosPortn_Type()
)
pm10010mpAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneRxLosPortn.setStatus("current")
_Pm10010mpAlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneTxLolPortn_Object = MibTableColumn
pm10010mpAlmLineLaneTxLolPortn = _Pm10010mpAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 8),
    _Pm10010mpAlmLineLaneTxLolPortn_Type()
)
pm10010mpAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneTxLolPortn.setStatus("current")
_Pm10010mpAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneTxLosfPortn_Object = MibTableColumn
pm10010mpAlmLineLaneTxLosfPortn = _Pm10010mpAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 9),
    _Pm10010mpAlmLineLaneTxLosfPortn_Type()
)
pm10010mpAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneTxLosfPortn.setStatus("current")
_Pm10010mpAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm10010mpAlmLineLaneApdPowerSupplyPortn = _Pm10010mpAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 15),
    _Pm10010mpAlmLineLaneApdPowerSupplyPortn_Type()
)
pm10010mpAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm10010mpAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm10010mpAlmLineLaneWavelengthUnlockedPortn = _Pm10010mpAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 16),
    _Pm10010mpAlmLineLaneWavelengthUnlockedPortn_Type()
)
pm10010mpAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm10010mpAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneTecFaultPortn_Object = MibTableColumn
pm10010mpAlmLineLaneTecFaultPortn = _Pm10010mpAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 136, 1, 17),
    _Pm10010mpAlmLineLaneTecFaultPortn_Type()
)
pm10010mpAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneTecFaultPortn.setStatus("current")
_Pm10010mpAlmlineHostLaneFaultTable_Object = MibTable
pm10010mpAlmlineHostLaneFaultTable = _Pm10010mpAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineHostLaneFaultTable.setStatus("current")
_Pm10010mpAlmlineHostLaneFaultEntry_Object = MibTableRow
pm10010mpAlmlineHostLaneFaultEntry = _Pm10010mpAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1)
)
pm10010mpAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineHostLaneFaultEntry.setStatus("current")


class _Pm10010mpAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm10010mpAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmlineHostLaneFaultIndex_Object = MibTableColumn
pm10010mpAlmlineHostLaneFaultIndex = _Pm10010mpAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 1),
    _Pm10010mpAlmlineHostLaneFaultIndex_Type()
)
pm10010mpAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmlineHostLaneFaultIndex.setStatus("current")
_Pm10010mpAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm10010mpAlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm10010mpAlmLineInputLossOfSignalPortn = _Pm10010mpAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 2),
    _Pm10010mpAlmLineInputLossOfSignalPortn_Type()
)
pm10010mpAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineInputLossOfSignalPortn.setStatus("current")
_Pm10010mpAlmLineLossOfFramePortn_Type = EkiOnOff
_Pm10010mpAlmLineLossOfFramePortn_Object = MibTableColumn
pm10010mpAlmLineLossOfFramePortn = _Pm10010mpAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 3),
    _Pm10010mpAlmLineLossOfFramePortn_Type()
)
pm10010mpAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLossOfFramePortn.setStatus("current")
_Pm10010mpAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm10010mpAlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm10010mpAlmLineSmBdiInsertedPortn = _Pm10010mpAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 4),
    _Pm10010mpAlmLineSmBdiInsertedPortn_Type()
)
pm10010mpAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineSmBdiInsertedPortn.setStatus("current")
_Pm10010mpAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm10010mpAlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm10010mpAlmLineSmBdiDetectedPortn = _Pm10010mpAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 5),
    _Pm10010mpAlmLineSmBdiDetectedPortn_Type()
)
pm10010mpAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineSmBdiDetectedPortn.setStatus("current")
_Pm10010mpAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm10010mpAlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm10010mpAlmLineSmIaeInsertedPortn = _Pm10010mpAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 6),
    _Pm10010mpAlmLineSmIaeInsertedPortn_Type()
)
pm10010mpAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineSmIaeInsertedPortn.setStatus("current")
_Pm10010mpAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm10010mpAlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm10010mpAlmLineSmIaeDetectedPortn = _Pm10010mpAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 7),
    _Pm10010mpAlmLineSmIaeDetectedPortn_Type()
)
pm10010mpAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineSmIaeDetectedPortn.setStatus("current")
_Pm10010mpAlmLineTxHostLolPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxHostLolPortn_Object = MibTableColumn
pm10010mpAlmLineTxHostLolPortn = _Pm10010mpAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 10),
    _Pm10010mpAlmLineTxHostLolPortn_Type()
)
pm10010mpAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxHostLolPortn.setStatus("current")
_Pm10010mpAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm10010mpAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm10010mpAlmLineLaneTxFifoErrorPortn = _Pm10010mpAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 152, 1, 11),
    _Pm10010mpAlmLineLaneTxFifoErrorPortn_Type()
)
pm10010mpAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm10010mpAlmlineNetworkLaneRxOtnTable_Object = MibTable
pm10010mpAlmlineNetworkLaneRxOtnTable = _Pm10010mpAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168)
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm10010mpAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm10010mpAlmlineNetworkLaneRxOtnEntry = _Pm10010mpAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1)
)
pm10010mpAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm10010mpAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm10010mpAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm10010mpAlmlineNetworkLaneRxOtnIndex = _Pm10010mpAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 1),
    _Pm10010mpAlmlineNetworkLaneRxOtnIndex_Type()
)
pm10010mpAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm10010mpAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnOduAisPortn = _Pm10010mpAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 10),
    _Pm10010mpAlmLineRxOtnOduAisPortn_Type()
)
pm10010mpAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnOduAisPortn.setStatus("current")
_Pm10010mpAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnOtuAisPortn = _Pm10010mpAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 11),
    _Pm10010mpAlmLineRxOtnOtuAisPortn_Type()
)
pm10010mpAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm10010mpAlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxSmBdiPortn_Object = MibTableColumn
pm10010mpAlmLineRxSmBdiPortn = _Pm10010mpAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 12),
    _Pm10010mpAlmLineRxSmBdiPortn_Type()
)
pm10010mpAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxSmBdiPortn.setStatus("current")
_Pm10010mpAlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnIaePortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnIaePortn = _Pm10010mpAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 13),
    _Pm10010mpAlmLineRxOtnIaePortn_Type()
)
pm10010mpAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnIaePortn.setStatus("current")
_Pm10010mpAlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnOomPortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnOomPortn = _Pm10010mpAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 14),
    _Pm10010mpAlmLineRxOtnOomPortn_Type()
)
pm10010mpAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnOomPortn.setStatus("current")
_Pm10010mpAlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnLomPortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnLomPortn = _Pm10010mpAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 15),
    _Pm10010mpAlmLineRxOtnLomPortn_Type()
)
pm10010mpAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnLomPortn.setStatus("current")
_Pm10010mpAlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnOofPortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnOofPortn = _Pm10010mpAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 16),
    _Pm10010mpAlmLineRxOtnOofPortn_Type()
)
pm10010mpAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnOofPortn.setStatus("current")
_Pm10010mpAlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm10010mpAlmLineRxOtnLofPortn_Object = MibTableColumn
pm10010mpAlmLineRxOtnLofPortn = _Pm10010mpAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 168, 1, 17),
    _Pm10010mpAlmLineRxOtnLofPortn_Type()
)
pm10010mpAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineRxOtnLofPortn.setStatus("current")
_Pm10010mpAlmlineHostLaneTxOtnTable_Object = MibTable
pm10010mpAlmlineHostLaneTxOtnTable = _Pm10010mpAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184)
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineHostLaneTxOtnTable.setStatus("current")
_Pm10010mpAlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm10010mpAlmlineHostLaneTxOtnEntry = _Pm10010mpAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1)
)
pm10010mpAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm10010mpAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm10010mpAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm10010mpAlmlineHostLaneTxOtnIndex = _Pm10010mpAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 1),
    _Pm10010mpAlmlineHostLaneTxOtnIndex_Type()
)
pm10010mpAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm10010mpAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnOduAisPortn = _Pm10010mpAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 10),
    _Pm10010mpAlmLineTxOtnOduAisPortn_Type()
)
pm10010mpAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnOduAisPortn.setStatus("current")
_Pm10010mpAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnOtuAisPortn = _Pm10010mpAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 11),
    _Pm10010mpAlmLineTxOtnOtuAisPortn_Type()
)
pm10010mpAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm10010mpAlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxSmBdiPortn_Object = MibTableColumn
pm10010mpAlmLineTxSmBdiPortn = _Pm10010mpAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 12),
    _Pm10010mpAlmLineTxSmBdiPortn_Type()
)
pm10010mpAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxSmBdiPortn.setStatus("current")
_Pm10010mpAlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnIaePortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnIaePortn = _Pm10010mpAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 13),
    _Pm10010mpAlmLineTxOtnIaePortn_Type()
)
pm10010mpAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnIaePortn.setStatus("current")
_Pm10010mpAlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnOomPortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnOomPortn = _Pm10010mpAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 14),
    _Pm10010mpAlmLineTxOtnOomPortn_Type()
)
pm10010mpAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnOomPortn.setStatus("current")
_Pm10010mpAlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnLomPortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnLomPortn = _Pm10010mpAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 15),
    _Pm10010mpAlmLineTxOtnLomPortn_Type()
)
pm10010mpAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnLomPortn.setStatus("current")
_Pm10010mpAlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnOofPortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnOofPortn = _Pm10010mpAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 16),
    _Pm10010mpAlmLineTxOtnOofPortn_Type()
)
pm10010mpAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnOofPortn.setStatus("current")
_Pm10010mpAlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm10010mpAlmLineTxOtnLofPortn_Object = MibTableColumn
pm10010mpAlmLineTxOtnLofPortn = _Pm10010mpAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 2, 184, 1, 17),
    _Pm10010mpAlmLineTxOtnLofPortn_Type()
)
pm10010mpAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineTxOtnLofPortn.setStatus("current")
_Pm10010mpAlmLineCrit_ObjectIdentity = ObjectIdentity
pm10010mpAlmLineCrit = _Pm10010mpAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3)
)
_Pm10010mpAlmsynthAlmLineTable_Object = MibTable
pm10010mpAlmsynthAlmLineTable = _Pm10010mpAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pm10010mpAlmsynthAlmLineTable.setStatus("current")
_Pm10010mpAlmsynthAlmLineEntry_Object = MibTableRow
pm10010mpAlmsynthAlmLineEntry = _Pm10010mpAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1)
)
pm10010mpAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpAlmsynthAlmLineEntry.setStatus("current")


class _Pm10010mpAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm10010mpAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm10010mpAlmsynthAlmLineIndex_Object = MibTableColumn
pm10010mpAlmsynthAlmLineIndex = _Pm10010mpAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 1),
    _Pm10010mpAlmsynthAlmLineIndex_Type()
)
pm10010mpAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmsynthAlmLineIndex.setStatus("current")
_Pm10010mpAlmXfpAbsentPortn_Type = EkiOnOff
_Pm10010mpAlmXfpAbsentPortn_Object = MibTableColumn
pm10010mpAlmXfpAbsentPortn = _Pm10010mpAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 2),
    _Pm10010mpAlmXfpAbsentPortn_Type()
)
pm10010mpAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmXfpAbsentPortn.setStatus("current")
_Pm10010mpAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm10010mpAlmXfpInitNotComplPortn_Object = MibTableColumn
pm10010mpAlmXfpInitNotComplPortn = _Pm10010mpAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 3),
    _Pm10010mpAlmXfpInitNotComplPortn_Type()
)
pm10010mpAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmXfpInitNotComplPortn.setStatus("current")
_Pm10010mpAlmLineHwFailPortn_Type = EkiOnOff
_Pm10010mpAlmLineHwFailPortn_Object = MibTableColumn
pm10010mpAlmLineHwFailPortn = _Pm10010mpAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 5),
    _Pm10010mpAlmLineHwFailPortn_Type()
)
pm10010mpAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineHwFailPortn.setStatus("current")
_Pm10010mpAlmXfpTxOffPortn_Type = EkiOnOff
_Pm10010mpAlmXfpTxOffPortn_Object = MibTableColumn
pm10010mpAlmXfpTxOffPortn = _Pm10010mpAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 6),
    _Pm10010mpAlmXfpTxOffPortn_Type()
)
pm10010mpAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmXfpTxOffPortn.setStatus("current")
_Pm10010mpAlmLineLocalOosPortn_Type = EkiOnOff
_Pm10010mpAlmLineLocalOosPortn_Object = MibTableColumn
pm10010mpAlmLineLocalOosPortn = _Pm10010mpAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 7),
    _Pm10010mpAlmLineLocalOosPortn_Type()
)
pm10010mpAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineLocalOosPortn.setStatus("current")
_Pm10010mpAlmUpRdiInsPortn_Type = EkiOnOff
_Pm10010mpAlmUpRdiInsPortn_Object = MibTableColumn
pm10010mpAlmUpRdiInsPortn = _Pm10010mpAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 9),
    _Pm10010mpAlmUpRdiInsPortn_Type()
)
pm10010mpAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmUpRdiInsPortn.setStatus("current")
_Pm10010mpAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm10010mpAlmLineDdmWarningPortn_Object = MibTableColumn
pm10010mpAlmLineDdmWarningPortn = _Pm10010mpAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 10),
    _Pm10010mpAlmLineDdmWarningPortn_Type()
)
pm10010mpAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineDdmWarningPortn.setStatus("current")
_Pm10010mpAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm10010mpAlmLineDdmAlmPortn_Object = MibTableColumn
pm10010mpAlmLineDdmAlmPortn = _Pm10010mpAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 11),
    _Pm10010mpAlmLineDdmAlmPortn_Type()
)
pm10010mpAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineDdmAlmPortn.setStatus("current")
_Pm10010mpAlmLineFailPortn_Type = EkiOnOff
_Pm10010mpAlmLineFailPortn_Object = MibTableColumn
pm10010mpAlmLineFailPortn = _Pm10010mpAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 13),
    _Pm10010mpAlmLineFailPortn_Type()
)
pm10010mpAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineFailPortn.setStatus("current")
_Pm10010mpAlmLineActivePortn_Type = EkiOnOff
_Pm10010mpAlmLineActivePortn_Object = MibTableColumn
pm10010mpAlmLineActivePortn = _Pm10010mpAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 2, 3, 3, 24, 1, 17),
    _Pm10010mpAlmLineActivePortn_Type()
)
pm10010mpAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpAlmLineActivePortn.setStatus("current")
_Pm10010mpmeasures_ObjectIdentity = ObjectIdentity
pm10010mpmeasures = _Pm10010mpmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3)
)
_Pm10010mpMesrOther_ObjectIdentity = ObjectIdentity
pm10010mpMesrOther = _Pm10010mpMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1)
)
_Pm10010mpMesrsynth0_Type = EkiMeasureType
_Pm10010mpMesrsynth0_Object = MibScalar
pm10010mpMesrsynth0 = _Pm10010mpMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 0),
    _Pm10010mpMesrsynth0_Type()
)
pm10010mpMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrsynth0.setStatus("deprecated")
_Pm10010mpMesrsynth1_Type = EkiMeasureType
_Pm10010mpMesrsynth1_Object = MibScalar
pm10010mpMesrsynth1 = _Pm10010mpMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 1),
    _Pm10010mpMesrsynth1_Type()
)
pm10010mpMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrsynth1.setStatus("deprecated")


class _Pm10010mpMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm10010mpMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm10010mpMesrpmIntervalNumber_Object = MibScalar
pm10010mpMesrpmIntervalNumber = _Pm10010mpMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 7),
    _Pm10010mpMesrpmIntervalNumber_Type()
)
pm10010mpMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrpmIntervalNumber.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm10010mpMesrlineNetTxLaserOutputPwrAverage = _Pm10010mpMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 180),
    _Pm10010mpMesrlineNetTxLaserOutputPwrAverage_Type()
)
pm10010mpMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxLaserTempAverage_Object = MibScalar
pm10010mpMesrlineNetTxLaserTempAverage = _Pm10010mpMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 181),
    _Pm10010mpMesrlineNetTxLaserTempAverage_Type()
)
pm10010mpMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm10010mpMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm10010mpMesrlineNetTxBiasCurrentAverage = _Pm10010mpMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 182),
    _Pm10010mpMesrlineNetTxBiasCurrentAverage_Type()
)
pm10010mpMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm10010mpMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetRxInputPwrAverage_Object = MibScalar
pm10010mpMesrlineNetRxInputPwrAverage = _Pm10010mpMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 183),
    _Pm10010mpMesrlineNetRxInputPwrAverage_Type()
)
pm10010mpMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm10010mpMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineResidualChromaticDispAverage_Object = MibScalar
pm10010mpMesrlineResidualChromaticDispAverage = _Pm10010mpMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 184),
    _Pm10010mpMesrlineResidualChromaticDispAverage_Type()
)
pm10010mpMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm10010mpMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineDiffGroupDelayAverage_Object = MibScalar
pm10010mpMesrlineDiffGroupDelayAverage = _Pm10010mpMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 185),
    _Pm10010mpMesrlineDiffGroupDelayAverage_Type()
)
pm10010mpMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm10010mpMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineQFactorAverage_Object = MibScalar
pm10010mpMesrlineQFactorAverage = _Pm10010mpMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 186),
    _Pm10010mpMesrlineQFactorAverage_Type()
)
pm10010mpMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorAverage.setStatus("current")


class _Pm10010mpMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm10010mpMesrlineCarrierFreqOffsetAverage = _Pm10010mpMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 187),
    _Pm10010mpMesrlineCarrierFreqOffsetAverage_Type()
)
pm10010mpMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm10010mpMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineOsnrAverage_Object = MibScalar
pm10010mpMesrlineOsnrAverage = _Pm10010mpMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 188),
    _Pm10010mpMesrlineOsnrAverage_Type()
)
pm10010mpMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrAverage.setStatus("current")


class _Pm10010mpMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetTxTempMin_Object = MibScalar
pm10010mpMesrclientNetTxTempMin = _Pm10010mpMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 192),
    _Pm10010mpMesrclientNetTxTempMin_Type()
)
pm10010mpMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxTempMin.setStatus("current")


class _Pm10010mpMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetTxBiasMin_Object = MibScalar
pm10010mpMesrclientNetTxBiasMin = _Pm10010mpMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 193),
    _Pm10010mpMesrclientNetTxBiasMin_Type()
)
pm10010mpMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxBiasMin.setStatus("current")


class _Pm10010mpMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetTxPwrMin_Object = MibScalar
pm10010mpMesrclientNetTxPwrMin = _Pm10010mpMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 194),
    _Pm10010mpMesrclientNetTxPwrMin_Type()
)
pm10010mpMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxPwrMin.setStatus("current")


class _Pm10010mpMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetRxPwrMin_Object = MibScalar
pm10010mpMesrclientNetRxPwrMin = _Pm10010mpMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 195),
    _Pm10010mpMesrclientNetRxPwrMin_Type()
)
pm10010mpMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetRxPwrMin.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm10010mpMesrlineNetTxLaserOutputPwrMin = _Pm10010mpMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 196),
    _Pm10010mpMesrlineNetTxLaserOutputPwrMin_Type()
)
pm10010mpMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxLaserTempMin_Object = MibScalar
pm10010mpMesrlineNetTxLaserTempMin = _Pm10010mpMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 197),
    _Pm10010mpMesrlineNetTxLaserTempMin_Type()
)
pm10010mpMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempMin.setStatus("current")


class _Pm10010mpMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxBiasCurrentMin_Object = MibScalar
pm10010mpMesrlineNetTxBiasCurrentMin = _Pm10010mpMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 198),
    _Pm10010mpMesrlineNetTxBiasCurrentMin_Type()
)
pm10010mpMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm10010mpMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetRxInputPwrMin_Object = MibScalar
pm10010mpMesrlineNetRxInputPwrMin = _Pm10010mpMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 199),
    _Pm10010mpMesrlineNetRxInputPwrMin_Type()
)
pm10010mpMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrMin.setStatus("current")


class _Pm10010mpMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineResidualChromaticDispMin_Object = MibScalar
pm10010mpMesrlineResidualChromaticDispMin = _Pm10010mpMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 200),
    _Pm10010mpMesrlineResidualChromaticDispMin_Type()
)
pm10010mpMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispMin.setStatus("current")


class _Pm10010mpMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineDiffGroupDelayMin_Object = MibScalar
pm10010mpMesrlineDiffGroupDelayMin = _Pm10010mpMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 201),
    _Pm10010mpMesrlineDiffGroupDelayMin_Type()
)
pm10010mpMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayMin.setStatus("current")


class _Pm10010mpMesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineQFactorMin_Object = MibScalar
pm10010mpMesrlineQFactorMin = _Pm10010mpMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 202),
    _Pm10010mpMesrlineQFactorMin_Type()
)
pm10010mpMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorMin.setStatus("current")


class _Pm10010mpMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineCarrierFreqOffsetMin_Object = MibScalar
pm10010mpMesrlineCarrierFreqOffsetMin = _Pm10010mpMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 203),
    _Pm10010mpMesrlineCarrierFreqOffsetMin_Type()
)
pm10010mpMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm10010mpMesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm10010mpMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineOsnrMin_Object = MibScalar
pm10010mpMesrlineOsnrMin = _Pm10010mpMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 204),
    _Pm10010mpMesrlineOsnrMin_Type()
)
pm10010mpMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrMin.setStatus("current")


class _Pm10010mpMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetTxTempMax_Object = MibScalar
pm10010mpMesrclientNetTxTempMax = _Pm10010mpMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 208),
    _Pm10010mpMesrclientNetTxTempMax_Type()
)
pm10010mpMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxTempMax.setStatus("current")


class _Pm10010mpMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetTxBiasMax_Object = MibScalar
pm10010mpMesrclientNetTxBiasMax = _Pm10010mpMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 209),
    _Pm10010mpMesrclientNetTxBiasMax_Type()
)
pm10010mpMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxBiasMax.setStatus("current")


class _Pm10010mpMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetTxPwrMax_Object = MibScalar
pm10010mpMesrclientNetTxPwrMax = _Pm10010mpMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 210),
    _Pm10010mpMesrclientNetTxPwrMax_Type()
)
pm10010mpMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxPwrMax.setStatus("current")


class _Pm10010mpMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm10010mpMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientNetRxPwrMax_Object = MibScalar
pm10010mpMesrclientNetRxPwrMax = _Pm10010mpMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 211),
    _Pm10010mpMesrclientNetRxPwrMax_Type()
)
pm10010mpMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetRxPwrMax.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm10010mpMesrlineNetTxLaserOutputPwrMax = _Pm10010mpMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 212),
    _Pm10010mpMesrlineNetTxLaserOutputPwrMax_Type()
)
pm10010mpMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxLaserTempMax_Object = MibScalar
pm10010mpMesrlineNetTxLaserTempMax = _Pm10010mpMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 213),
    _Pm10010mpMesrlineNetTxLaserTempMax_Type()
)
pm10010mpMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempMax.setStatus("current")


class _Pm10010mpMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetTxBiasCurrentMax_Object = MibScalar
pm10010mpMesrlineNetTxBiasCurrentMax = _Pm10010mpMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 214),
    _Pm10010mpMesrlineNetTxBiasCurrentMax_Type()
)
pm10010mpMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm10010mpMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineNetRxInputPwrMax_Object = MibScalar
pm10010mpMesrlineNetRxInputPwrMax = _Pm10010mpMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 215),
    _Pm10010mpMesrlineNetRxInputPwrMax_Type()
)
pm10010mpMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrMax.setStatus("current")


class _Pm10010mpMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineResidualChromaticDispMax_Object = MibScalar
pm10010mpMesrlineResidualChromaticDispMax = _Pm10010mpMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 216),
    _Pm10010mpMesrlineResidualChromaticDispMax_Type()
)
pm10010mpMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispMax.setStatus("current")


class _Pm10010mpMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineDiffGroupDelayMax_Object = MibScalar
pm10010mpMesrlineDiffGroupDelayMax = _Pm10010mpMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 217),
    _Pm10010mpMesrlineDiffGroupDelayMax_Type()
)
pm10010mpMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayMax.setStatus("current")


class _Pm10010mpMesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineQFactorMax_Object = MibScalar
pm10010mpMesrlineQFactorMax = _Pm10010mpMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 218),
    _Pm10010mpMesrlineQFactorMax_Type()
)
pm10010mpMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorMax.setStatus("current")


class _Pm10010mpMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineCarrierFreqOffsetMax_Object = MibScalar
pm10010mpMesrlineCarrierFreqOffsetMax = _Pm10010mpMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 219),
    _Pm10010mpMesrlineCarrierFreqOffsetMax_Type()
)
pm10010mpMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm10010mpMesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm10010mpMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineOsnrMax_Object = MibScalar
pm10010mpMesrlineOsnrMax = _Pm10010mpMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 1, 220),
    _Pm10010mpMesrlineOsnrMax_Type()
)
pm10010mpMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrMax.setStatus("current")
_Pm10010mpMesrClient_ObjectIdentity = ObjectIdentity
pm10010mpMesrClient = _Pm10010mpMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2)
)


class _Pm10010mpMesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm10010mpMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientCfpTemp_Object = MibScalar
pm10010mpMesrclientCfpTemp = _Pm10010mpMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 8),
    _Pm10010mpMesrclientCfpTemp_Type()
)
pm10010mpMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientCfpTemp.setStatus("current")


class _Pm10010mpMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm10010mpMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientCfp3v3Voltage_Object = MibScalar
pm10010mpMesrclientCfp3v3Voltage = _Pm10010mpMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 9),
    _Pm10010mpMesrclientCfp3v3Voltage_Type()
)
pm10010mpMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientCfp3v3Voltage.setStatus("current")


class _Pm10010mpMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010mpMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010mpMesrclientSoaBiasCurrent_Object = MibScalar
pm10010mpMesrclientSoaBiasCurrent = _Pm10010mpMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 10),
    _Pm10010mpMesrclientSoaBiasCurrent_Type()
)
pm10010mpMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientSoaBiasCurrent.setStatus("current")
_Pm10010mpMesrclientNetTxTempTable_Object = MibTable
pm10010mpMesrclientNetTxTempTable = _Pm10010mpMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxTempTable.setStatus("current")
_Pm10010mpMesrclientNetTxTempEntry_Object = MibTableRow
pm10010mpMesrclientNetTxTempEntry = _Pm10010mpMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 16, 1)
)
pm10010mpMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxTempEntry.setStatus("current")


class _Pm10010mpMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pm10010mpMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetTxTempIndex_Object = MibTableColumn
pm10010mpMesrclientNetTxTempIndex = _Pm10010mpMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 16, 1, 1),
    _Pm10010mpMesrclientNetTxTempIndex_Type()
)
pm10010mpMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxTempIndex.setStatus("current")


class _Pm10010mpMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pm10010mpMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetTxTempPortn_Object = MibTableColumn
pm10010mpMesrclientNetTxTempPortn = _Pm10010mpMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 16, 1, 2),
    _Pm10010mpMesrclientNetTxTempPortn_Type()
)
pm10010mpMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxTempPortn.setStatus("current")
_Pm10010mpMesrclientNetTxBiasTable_Object = MibTable
pm10010mpMesrclientNetTxBiasTable = _Pm10010mpMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxBiasTable.setStatus("current")
_Pm10010mpMesrclientNetTxBiasEntry_Object = MibTableRow
pm10010mpMesrclientNetTxBiasEntry = _Pm10010mpMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 32, 1)
)
pm10010mpMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxBiasEntry.setStatus("current")


class _Pm10010mpMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pm10010mpMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetTxBiasIndex_Object = MibTableColumn
pm10010mpMesrclientNetTxBiasIndex = _Pm10010mpMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 32, 1, 1),
    _Pm10010mpMesrclientNetTxBiasIndex_Type()
)
pm10010mpMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxBiasIndex.setStatus("current")


class _Pm10010mpMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pm10010mpMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetTxBiasPortn_Object = MibTableColumn
pm10010mpMesrclientNetTxBiasPortn = _Pm10010mpMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 32, 1, 2),
    _Pm10010mpMesrclientNetTxBiasPortn_Type()
)
pm10010mpMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxBiasPortn.setStatus("current")
_Pm10010mpMesrclientNetTxPwrTable_Object = MibTable
pm10010mpMesrclientNetTxPwrTable = _Pm10010mpMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxPwrTable.setStatus("current")
_Pm10010mpMesrclientNetTxPwrEntry_Object = MibTableRow
pm10010mpMesrclientNetTxPwrEntry = _Pm10010mpMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 48, 1)
)
pm10010mpMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxPwrEntry.setStatus("current")


class _Pm10010mpMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pm10010mpMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetTxPwrIndex_Object = MibTableColumn
pm10010mpMesrclientNetTxPwrIndex = _Pm10010mpMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 48, 1, 1),
    _Pm10010mpMesrclientNetTxPwrIndex_Type()
)
pm10010mpMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxPwrIndex.setStatus("current")


class _Pm10010mpMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pm10010mpMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetTxPwrPortn_Object = MibTableColumn
pm10010mpMesrclientNetTxPwrPortn = _Pm10010mpMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 48, 1, 2),
    _Pm10010mpMesrclientNetTxPwrPortn_Type()
)
pm10010mpMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetTxPwrPortn.setStatus("current")
_Pm10010mpMesrclientNetRxPwrTable_Object = MibTable
pm10010mpMesrclientNetRxPwrTable = _Pm10010mpMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetRxPwrTable.setStatus("current")
_Pm10010mpMesrclientNetRxPwrEntry_Object = MibTableRow
pm10010mpMesrclientNetRxPwrEntry = _Pm10010mpMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 64, 1)
)
pm10010mpMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetRxPwrEntry.setStatus("current")


class _Pm10010mpMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pm10010mpMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetRxPwrIndex_Object = MibTableColumn
pm10010mpMesrclientNetRxPwrIndex = _Pm10010mpMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 64, 1, 1),
    _Pm10010mpMesrclientNetRxPwrIndex_Type()
)
pm10010mpMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetRxPwrIndex.setStatus("current")


class _Pm10010mpMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pm10010mpMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrclientNetRxPwrPortn_Object = MibTableColumn
pm10010mpMesrclientNetRxPwrPortn = _Pm10010mpMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 2, 64, 1, 2),
    _Pm10010mpMesrclientNetRxPwrPortn_Type()
)
pm10010mpMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrclientNetRxPwrPortn.setStatus("current")
_Pm10010mpMesrLine_ObjectIdentity = ObjectIdentity
pm10010mpMesrLine = _Pm10010mpMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3)
)


class _Pm10010mpMesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm10010mpMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineMsaTemp_Object = MibScalar
pm10010mpMesrlineMsaTemp = _Pm10010mpMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 12),
    _Pm10010mpMesrlineMsaTemp_Type()
)
pm10010mpMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineMsaTemp.setStatus("current")


class _Pm10010mpMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm10010mpMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineMsa3v3Voltage_Object = MibScalar
pm10010mpMesrlineMsa3v3Voltage = _Pm10010mpMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 13),
    _Pm10010mpMesrlineMsa3v3Voltage_Type()
)
pm10010mpMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineMsa3v3Voltage.setStatus("current")


class _Pm10010mpMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm10010mpMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm10010mpMesrlineSoaBiasCurrent_Object = MibScalar
pm10010mpMesrlineSoaBiasCurrent = _Pm10010mpMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 14),
    _Pm10010mpMesrlineSoaBiasCurrent_Type()
)
pm10010mpMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineSoaBiasCurrent.setStatus("current")
_Pm10010mpMesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm10010mpMesrlineNetTxLaserOutputPwrTable = _Pm10010mpMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm10010mpMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm10010mpMesrlineNetTxLaserOutputPwrEntry = _Pm10010mpMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 80, 1)
)
pm10010mpMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm10010mpMesrlineNetTxLaserOutputPwrIndex = _Pm10010mpMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 80, 1, 1),
    _Pm10010mpMesrlineNetTxLaserOutputPwrIndex_Type()
)
pm10010mpMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm10010mpMesrlineNetTxLaserOutputPwrPortn = _Pm10010mpMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 80, 1, 2),
    _Pm10010mpMesrlineNetTxLaserOutputPwrPortn_Type()
)
pm10010mpMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm10010mpMesrlineNetTxLaserTempTable_Object = MibTable
pm10010mpMesrlineNetTxLaserTempTable = _Pm10010mpMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempTable.setStatus("current")
_Pm10010mpMesrlineNetTxLaserTempEntry_Object = MibTableRow
pm10010mpMesrlineNetTxLaserTempEntry = _Pm10010mpMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 96, 1)
)
pm10010mpMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm10010mpMesrlineNetTxLaserTempIndex = _Pm10010mpMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 96, 1, 1),
    _Pm10010mpMesrlineNetTxLaserTempIndex_Type()
)
pm10010mpMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm10010mpMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm10010mpMesrlineNetTxLaserTempPortn = _Pm10010mpMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 96, 1, 2),
    _Pm10010mpMesrlineNetTxLaserTempPortn_Type()
)
pm10010mpMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxLaserTempPortn.setStatus("current")
_Pm10010mpMesrlineNetTxBiasCurrentTable_Object = MibTable
pm10010mpMesrlineNetTxBiasCurrentTable = _Pm10010mpMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm10010mpMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm10010mpMesrlineNetTxBiasCurrentEntry = _Pm10010mpMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 112, 1)
)
pm10010mpMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm10010mpMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm10010mpMesrlineNetTxBiasCurrentIndex = _Pm10010mpMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 112, 1, 1),
    _Pm10010mpMesrlineNetTxBiasCurrentIndex_Type()
)
pm10010mpMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm10010mpMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm10010mpMesrlineNetTxBiasCurrentPortn = _Pm10010mpMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 112, 1, 2),
    _Pm10010mpMesrlineNetTxBiasCurrentPortn_Type()
)
pm10010mpMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm10010mpMesrlineNetRxInputPwrTable_Object = MibTable
pm10010mpMesrlineNetRxInputPwrTable = _Pm10010mpMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrTable.setStatus("current")
_Pm10010mpMesrlineNetRxInputPwrEntry_Object = MibTableRow
pm10010mpMesrlineNetRxInputPwrEntry = _Pm10010mpMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 128, 1)
)
pm10010mpMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm10010mpMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm10010mpMesrlineNetRxInputPwrIndex = _Pm10010mpMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 128, 1, 1),
    _Pm10010mpMesrlineNetRxInputPwrIndex_Type()
)
pm10010mpMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm10010mpMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm10010mpMesrlineNetRxInputPwrPortn = _Pm10010mpMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 128, 1, 2),
    _Pm10010mpMesrlineNetRxInputPwrPortn_Type()
)
pm10010mpMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineNetRxInputPwrPortn.setStatus("current")
_Pm10010mpMesrlineResidualChromaticDispTable_Object = MibTable
pm10010mpMesrlineResidualChromaticDispTable = _Pm10010mpMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispTable.setStatus("current")
_Pm10010mpMesrlineResidualChromaticDispEntry_Object = MibTableRow
pm10010mpMesrlineResidualChromaticDispEntry = _Pm10010mpMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 144, 1)
)
pm10010mpMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm10010mpMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm10010mpMesrlineResidualChromaticDispIndex = _Pm10010mpMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 144, 1, 1),
    _Pm10010mpMesrlineResidualChromaticDispIndex_Type()
)
pm10010mpMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm10010mpMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm10010mpMesrlineResidualChromaticDispPortn = _Pm10010mpMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 144, 1, 2),
    _Pm10010mpMesrlineResidualChromaticDispPortn_Type()
)
pm10010mpMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineResidualChromaticDispPortn.setStatus("current")
_Pm10010mpMesrlineDiffGroupDelayTable_Object = MibTable
pm10010mpMesrlineDiffGroupDelayTable = _Pm10010mpMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayTable.setStatus("current")
_Pm10010mpMesrlineDiffGroupDelayEntry_Object = MibTableRow
pm10010mpMesrlineDiffGroupDelayEntry = _Pm10010mpMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 148, 1)
)
pm10010mpMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm10010mpMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm10010mpMesrlineDiffGroupDelayIndex = _Pm10010mpMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 148, 1, 1),
    _Pm10010mpMesrlineDiffGroupDelayIndex_Type()
)
pm10010mpMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm10010mpMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm10010mpMesrlineDiffGroupDelayPortn = _Pm10010mpMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 148, 1, 2),
    _Pm10010mpMesrlineDiffGroupDelayPortn_Type()
)
pm10010mpMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineDiffGroupDelayPortn.setStatus("current")
_Pm10010mpMesrlineQFactorTable_Object = MibTable
pm10010mpMesrlineQFactorTable = _Pm10010mpMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorTable.setStatus("current")
_Pm10010mpMesrlineQFactorEntry_Object = MibTableRow
pm10010mpMesrlineQFactorEntry = _Pm10010mpMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 152, 1)
)
pm10010mpMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorEntry.setStatus("current")


class _Pm10010mpMesrlineQFactorIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineQFactorIndex_Object = MibTableColumn
pm10010mpMesrlineQFactorIndex = _Pm10010mpMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 152, 1, 1),
    _Pm10010mpMesrlineQFactorIndex_Type()
)
pm10010mpMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorIndex.setStatus("current")


class _Pm10010mpMesrlineQFactorPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineQFactorPortn_Object = MibTableColumn
pm10010mpMesrlineQFactorPortn = _Pm10010mpMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 152, 1, 2),
    _Pm10010mpMesrlineQFactorPortn_Type()
)
pm10010mpMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineQFactorPortn.setStatus("current")
_Pm10010mpMesrlineCarrierFreqOffsetTable_Object = MibTable
pm10010mpMesrlineCarrierFreqOffsetTable = _Pm10010mpMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm10010mpMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm10010mpMesrlineCarrierFreqOffsetEntry = _Pm10010mpMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 156, 1)
)
pm10010mpMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm10010mpMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm10010mpMesrlineCarrierFreqOffsetIndex = _Pm10010mpMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 156, 1, 1),
    _Pm10010mpMesrlineCarrierFreqOffsetIndex_Type()
)
pm10010mpMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm10010mpMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm10010mpMesrlineCarrierFreqOffsetPortn = _Pm10010mpMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 156, 1, 2),
    _Pm10010mpMesrlineCarrierFreqOffsetPortn_Type()
)
pm10010mpMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm10010mpMesrlineOsnrTable_Object = MibTable
pm10010mpMesrlineOsnrTable = _Pm10010mpMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrTable.setStatus("current")
_Pm10010mpMesrlineOsnrEntry_Object = MibTableRow
pm10010mpMesrlineOsnrEntry = _Pm10010mpMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 160, 1)
)
pm10010mpMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrEntry.setStatus("current")


class _Pm10010mpMesrlineOsnrIndex_Type(Integer32):
    """Custom type pm10010mpMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm10010mpMesrlineOsnrIndex_Object = MibTableColumn
pm10010mpMesrlineOsnrIndex = _Pm10010mpMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 160, 1, 1),
    _Pm10010mpMesrlineOsnrIndex_Type()
)
pm10010mpMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrIndex.setStatus("current")


class _Pm10010mpMesrlineOsnrPortn_Type(Integer32):
    """Custom type pm10010mpMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm10010mpMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm10010mpMesrlineOsnrPortn_Object = MibTableColumn
pm10010mpMesrlineOsnrPortn = _Pm10010mpMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 3, 3, 160, 1, 2),
    _Pm10010mpMesrlineOsnrPortn_Type()
)
pm10010mpMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMesrlineOsnrPortn.setStatus("current")
_Pm10010mpcounters_ObjectIdentity = ObjectIdentity
pm10010mpcounters = _Pm10010mpcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4)
)
_Pm10010mpCntOther_ObjectIdentity = ObjectIdentity
pm10010mpCntOther = _Pm10010mpCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 1)
)
_Pm10010mpCntClient_ObjectIdentity = ObjectIdentity
pm10010mpCntClient = _Pm10010mpCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2)
)
_Pm10010mpCntclientInputErrorCounterLaneOneTable_Object = MibTable
pm10010mpCntclientInputErrorCounterLaneOneTable = _Pm10010mpCntclientInputErrorCounterLaneOneTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneOneTable.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneOneEntry_Object = MibTableRow
pm10010mpCntclientInputErrorCounterLaneOneEntry = _Pm10010mpCntclientInputErrorCounterLaneOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 16, 1)
)
pm10010mpCntclientInputErrorCounterLaneOneEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntclientInputErrorCounterLaneOneIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneOneEntry.setStatus("current")


class _Pm10010mpCntclientInputErrorCounterLaneOneIndex_Type(Integer32):
    """Custom type pm10010mpCntclientInputErrorCounterLaneOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntclientInputErrorCounterLaneOneIndex_Type.__name__ = "Integer32"
_Pm10010mpCntclientInputErrorCounterLaneOneIndex_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneOneIndex = _Pm10010mpCntclientInputErrorCounterLaneOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 16, 1, 1),
    _Pm10010mpCntclientInputErrorCounterLaneOneIndex_Type()
)
pm10010mpCntclientInputErrorCounterLaneOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneOneIndex.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneOneValuePortn_Type = Counter32
_Pm10010mpCntclientInputErrorCounterLaneOneValuePortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneOneValuePortn = _Pm10010mpCntclientInputErrorCounterLaneOneValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 16, 1, 2),
    _Pm10010mpCntclientInputErrorCounterLaneOneValuePortn_Type()
)
pm10010mpCntclientInputErrorCounterLaneOneValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneOneValuePortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Type = EkiOnOff
_Pm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneOneErrorPortn = _Pm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 16, 1, 3),
    _Pm10010mpCntclientInputErrorCounterLaneOneErrorPortn_Type()
)
pm10010mpCntclientInputErrorCounterLaneOneErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneOneErrorPortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Type = EkiOnOff
_Pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn = _Pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 16, 1, 4),
    _Pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn_Type()
)
pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneTwoTable_Object = MibTable
pm10010mpCntclientInputErrorCounterLaneTwoTable = _Pm10010mpCntclientInputErrorCounterLaneTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneTwoTable.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneTwoEntry_Object = MibTableRow
pm10010mpCntclientInputErrorCounterLaneTwoEntry = _Pm10010mpCntclientInputErrorCounterLaneTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 32, 1)
)
pm10010mpCntclientInputErrorCounterLaneTwoEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntclientInputErrorCounterLaneTwoIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneTwoEntry.setStatus("current")


class _Pm10010mpCntclientInputErrorCounterLaneTwoIndex_Type(Integer32):
    """Custom type pm10010mpCntclientInputErrorCounterLaneTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntclientInputErrorCounterLaneTwoIndex_Type.__name__ = "Integer32"
_Pm10010mpCntclientInputErrorCounterLaneTwoIndex_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneTwoIndex = _Pm10010mpCntclientInputErrorCounterLaneTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 32, 1, 1),
    _Pm10010mpCntclientInputErrorCounterLaneTwoIndex_Type()
)
pm10010mpCntclientInputErrorCounterLaneTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneTwoIndex.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Type = Counter32
_Pm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneTwoValuePortn = _Pm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 32, 1, 2),
    _Pm10010mpCntclientInputErrorCounterLaneTwoValuePortn_Type()
)
pm10010mpCntclientInputErrorCounterLaneTwoValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneTwoValuePortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Type = EkiOnOff
_Pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn = _Pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 32, 1, 3),
    _Pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn_Type()
)
pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Type = EkiOnOff
_Pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn = _Pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 32, 1, 4),
    _Pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn_Type()
)
pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterTable_Object = MibTable
pm10010mpCntclientInputErrorCounterTable = _Pm10010mpCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 80)
)
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterTable.setStatus("current")
_Pm10010mpCntclientInputErrorCounterEntry_Object = MibTableRow
pm10010mpCntclientInputErrorCounterEntry = _Pm10010mpCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 80, 1)
)
pm10010mpCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterEntry.setStatus("current")


class _Pm10010mpCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntclientInputErrorCounterIndex_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterIndex = _Pm10010mpCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 80, 1, 1),
    _Pm10010mpCntclientInputErrorCounterIndex_Type()
)
pm10010mpCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterIndex.setStatus("current")
_Pm10010mpCntclientInputErrorCounterValuePortn_Type = Counter32
_Pm10010mpCntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterValuePortn = _Pm10010mpCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 80, 1, 2),
    _Pm10010mpCntclientInputErrorCounterValuePortn_Type()
)
pm10010mpCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterValuePortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterErrorPortn = _Pm10010mpCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 80, 1, 3),
    _Pm10010mpCntclientInputErrorCounterErrorPortn_Type()
)
pm10010mpCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm10010mpCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntclientInputErrorCounterOverloadPortn = _Pm10010mpCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 80, 1, 4),
    _Pm10010mpCntclientInputErrorCounterOverloadPortn_Type()
)
pm10010mpCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm10010mpCntclientCbipCounterTable_Object = MibTable
pm10010mpCntclientCbipCounterTable = _Pm10010mpCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pm10010mpCntclientCbipCounterTable.setStatus("current")
_Pm10010mpCntclientCbipCounterEntry_Object = MibTableRow
pm10010mpCntclientCbipCounterEntry = _Pm10010mpCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 96, 1)
)
pm10010mpCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntclientCbipCounterEntry.setStatus("current")


class _Pm10010mpCntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntclientCbipCounterIndex_Object = MibTableColumn
pm10010mpCntclientCbipCounterIndex = _Pm10010mpCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 96, 1, 1),
    _Pm10010mpCntclientCbipCounterIndex_Type()
)
pm10010mpCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientCbipCounterIndex.setStatus("current")
_Pm10010mpCntclientCbipCounterValuePortn_Type = Counter32
_Pm10010mpCntclientCbipCounterValuePortn_Object = MibTableColumn
pm10010mpCntclientCbipCounterValuePortn = _Pm10010mpCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 96, 1, 2),
    _Pm10010mpCntclientCbipCounterValuePortn_Type()
)
pm10010mpCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientCbipCounterValuePortn.setStatus("current")
_Pm10010mpCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntclientCbipCounterErrorPortn_Object = MibTableColumn
pm10010mpCntclientCbipCounterErrorPortn = _Pm10010mpCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 96, 1, 3),
    _Pm10010mpCntclientCbipCounterErrorPortn_Type()
)
pm10010mpCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientCbipCounterErrorPortn.setStatus("current")
_Pm10010mpCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntclientCbipCounterOverloadPortn = _Pm10010mpCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 2, 96, 1, 4),
    _Pm10010mpCntclientCbipCounterOverloadPortn_Type()
)
pm10010mpCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntclientCbipCounterOverloadPortn.setStatus("current")
_Pm10010mpCntLine_ObjectIdentity = ObjectIdentity
pm10010mpCntLine = _Pm10010mpCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3)
)
_Pm10010mpCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm10010mpCntlocalLineSmBip8ErrorCounterTable = _Pm10010mpCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010mpCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010mpCntlocalLineSmBip8ErrorCounterEntry = _Pm10010mpCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 192, 1)
)
pm10010mpCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010mpCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010mpCntlocalLineSmBip8ErrorCounterIndex = _Pm10010mpCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 192, 1, 1),
    _Pm10010mpCntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm10010mpCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn = _Pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 192, 1, 2),
    _Pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn = _Pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 192, 1, 3),
    _Pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 192, 1, 4),
    _Pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm10010mpCntlocalLineFecCorrectedErrorsCounterTable = _Pm10010mpCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry = _Pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 193, 1)
)
pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex = _Pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 193, 1, 1),
    _Pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 193, 1, 2),
    _Pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 193, 1, 3),
    _Pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 193, 1, 4),
    _Pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm10010mpCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm10010mpCntremoteLineSmBip8ErrorCounterTable = _Pm10010mpCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm10010mpCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm10010mpCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm10010mpCntremoteLineSmBip8ErrorCounterEntry = _Pm10010mpCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 194, 1)
)
pm10010mpCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm10010mpCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm10010mpCntremoteLineSmBip8ErrorCounterIndex = _Pm10010mpCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 194, 1, 1),
    _Pm10010mpCntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm10010mpCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn = _Pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 194, 1, 2),
    _Pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn = _Pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 194, 1, 3),
    _Pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 194, 1, 4),
    _Pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm10010mpCntlineDfrmTimCntTable_Object = MibTable
pm10010mpCntlineDfrmTimCntTable = _Pm10010mpCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm10010mpCntlineDfrmTimCntTable.setStatus("current")
_Pm10010mpCntlineDfrmTimCntEntry_Object = MibTableRow
pm10010mpCntlineDfrmTimCntEntry = _Pm10010mpCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 195, 1)
)
pm10010mpCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntlineDfrmTimCntEntry.setStatus("current")


class _Pm10010mpCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm10010mpCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm10010mpCntlineDfrmTimCntIndex_Object = MibTableColumn
pm10010mpCntlineDfrmTimCntIndex = _Pm10010mpCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 195, 1, 1),
    _Pm10010mpCntlineDfrmTimCntIndex_Type()
)
pm10010mpCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlineDfrmTimCntIndex.setStatus("current")
_Pm10010mpCntlineDfrmTimCntValuePortn_Type = Counter64
_Pm10010mpCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm10010mpCntlineDfrmTimCntValuePortn = _Pm10010mpCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 195, 1, 2),
    _Pm10010mpCntlineDfrmTimCntValuePortn_Type()
)
pm10010mpCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm10010mpCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm10010mpCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm10010mpCntlineDfrmTimCntErrorPortn = _Pm10010mpCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 195, 1, 3),
    _Pm10010mpCntlineDfrmTimCntErrorPortn_Type()
)
pm10010mpCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm10010mpCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm10010mpCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm10010mpCntlineDfrmTimCntOverloadPortn = _Pm10010mpCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 195, 1, 4),
    _Pm10010mpCntlineDfrmTimCntOverloadPortn_Type()
)
pm10010mpCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable_Object = MibTable
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable = _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object = MibTableRow
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry = _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 196, 1)
)
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry.setStatus("current")


class _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex = _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 196, 1, 1),
    _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex_Type()
)
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type = Counter64
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn = _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 196, 1, 2),
    _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn_Type()
)
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn = _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 196, 1, 3),
    _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn_Type()
)
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn = _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 196, 1, 4),
    _Pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn_Type()
)
pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object = MibTable
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable = _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object = MibTableRow
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry = _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 197, 1)
)
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry.setStatus("current")


class _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type(Integer32):
    """Custom type pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type.__name__ = "Integer32"
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex = _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 197, 1, 1),
    _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex_Type()
)
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type = Counter64
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn = _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 197, 1, 2),
    _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn_Type()
)
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn = _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 197, 1, 3),
    _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn_Type()
)
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn.setStatus("current")
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type = EkiOnOff
_Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object = MibTableColumn
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn = _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 4, 3, 197, 1, 4),
    _Pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn_Type()
)
pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn.setStatus("current")
_Pm10010mpcontrolsWrite_ObjectIdentity = ObjectIdentity
pm10010mpcontrolsWrite = _Pm10010mpcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6)
)
_Pm10010mpCtrlOther_ObjectIdentity = ObjectIdentity
pm10010mpCtrlOther = _Pm10010mpCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1)
)
_Pm10010mpCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm10010mpCtrlconfMgnt1 = _Pm10010mpCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 1)
)
_Pm10010mpCtrlConf1Load1_Type = EkiOnOff
_Pm10010mpCtrlConf1Load1_Object = MibScalar
pm10010mpCtrlConf1Load1 = _Pm10010mpCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 1, 1),
    _Pm10010mpCtrlConf1Load1_Type()
)
pm10010mpCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlConf1Load1.setStatus("current")
_Pm10010mpCtrlConf2Load1_Type = EkiOnOff
_Pm10010mpCtrlConf2Load1_Object = MibScalar
pm10010mpCtrlConf2Load1 = _Pm10010mpCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 1, 2),
    _Pm10010mpCtrlConf2Load1_Type()
)
pm10010mpCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlConf2Load1.setStatus("current")
_Pm10010mpCtrlConf2Flash1_Type = EkiOnOff
_Pm10010mpCtrlConf2Flash1_Object = MibScalar
pm10010mpCtrlConf2Flash1 = _Pm10010mpCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 1, 10),
    _Pm10010mpCtrlConf2Flash1_Type()
)
pm10010mpCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlConf2Flash1.setStatus("current")
_Pm10010mpCtrlConf2Clear1_Type = EkiOnOff
_Pm10010mpCtrlConf2Clear1_Object = MibScalar
pm10010mpCtrlConf2Clear1 = _Pm10010mpCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 1, 14),
    _Pm10010mpCtrlConf2Clear1_Type()
)
pm10010mpCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlConf2Clear1.setStatus("current")
_Pm10010mpCtrlsynth4_ObjectIdentity = ObjectIdentity
pm10010mpCtrlsynth4 = _Pm10010mpCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 4)
)
_Pm10010mpCtrlCorrelatOn_Type = EkiOnOff
_Pm10010mpCtrlCorrelatOn_Object = MibScalar
pm10010mpCtrlCorrelatOn = _Pm10010mpCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 4, 1),
    _Pm10010mpCtrlCorrelatOn_Type()
)
pm10010mpCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlCorrelatOn.setStatus("current")
_Pm10010mpCtrlCorrelatOff_Type = EkiOnOff
_Pm10010mpCtrlCorrelatOff_Object = MibScalar
pm10010mpCtrlCorrelatOff = _Pm10010mpCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 4, 2),
    _Pm10010mpCtrlCorrelatOff_Type()
)
pm10010mpCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlCorrelatOff.setStatus("current")
_Pm10010mpCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm10010mpCtrlswMgnt = _Pm10010mpCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 5)
)
_Pm10010mpCtrlColdReset_Type = EkiOnOff
_Pm10010mpCtrlColdReset_Object = MibScalar
pm10010mpCtrlColdReset = _Pm10010mpCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 5, 2),
    _Pm10010mpCtrlColdReset_Type()
)
pm10010mpCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlColdReset.setStatus("current")
_Pm10010mpCtrlWarmReset_Type = EkiOnOff
_Pm10010mpCtrlWarmReset_Object = MibScalar
pm10010mpCtrlWarmReset = _Pm10010mpCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 5, 3),
    _Pm10010mpCtrlWarmReset_Type()
)
pm10010mpCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlWarmReset.setStatus("current")
_Pm10010mpCtrlLoadSwBank1_Type = EkiOnOff
_Pm10010mpCtrlLoadSwBank1_Object = MibScalar
pm10010mpCtrlLoadSwBank1 = _Pm10010mpCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 5, 5),
    _Pm10010mpCtrlLoadSwBank1_Type()
)
pm10010mpCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLoadSwBank1.setStatus("current")
_Pm10010mpCtrlLoadSwBank2_Type = EkiOnOff
_Pm10010mpCtrlLoadSwBank2_Object = MibScalar
pm10010mpCtrlLoadSwBank2 = _Pm10010mpCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 5, 6),
    _Pm10010mpCtrlLoadSwBank2_Type()
)
pm10010mpCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLoadSwBank2.setStatus("current")
_Pm10010mpCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm10010mpCtrlgwMgnt = _Pm10010mpCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 6)
)
_Pm10010mpCtrlCurrentGwReset_Type = EkiOnOff
_Pm10010mpCtrlCurrentGwReset_Object = MibScalar
pm10010mpCtrlCurrentGwReset = _Pm10010mpCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 6, 1),
    _Pm10010mpCtrlCurrentGwReset_Type()
)
pm10010mpCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlCurrentGwReset.setStatus("current")
_Pm10010mpCtrlLoadGwBank1_Type = EkiOnOff
_Pm10010mpCtrlLoadGwBank1_Object = MibScalar
pm10010mpCtrlLoadGwBank1 = _Pm10010mpCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 6, 5),
    _Pm10010mpCtrlLoadGwBank1_Type()
)
pm10010mpCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLoadGwBank1.setStatus("current")
_Pm10010mpCtrlLoadGwBank2_Type = EkiOnOff
_Pm10010mpCtrlLoadGwBank2_Object = MibScalar
pm10010mpCtrlLoadGwBank2 = _Pm10010mpCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 6, 6),
    _Pm10010mpCtrlLoadGwBank2_Type()
)
pm10010mpCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLoadGwBank2.setStatus("current")
_Pm10010mpCtrlLoadGwBank3_Type = EkiOnOff
_Pm10010mpCtrlLoadGwBank3_Object = MibScalar
pm10010mpCtrlLoadGwBank3 = _Pm10010mpCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 6, 7),
    _Pm10010mpCtrlLoadGwBank3_Type()
)
pm10010mpCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLoadGwBank3.setStatus("current")
_Pm10010mpCtrlLoadGwBank4_Type = EkiOnOff
_Pm10010mpCtrlLoadGwBank4_Object = MibScalar
pm10010mpCtrlLoadGwBank4 = _Pm10010mpCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 6, 8),
    _Pm10010mpCtrlLoadGwBank4_Type()
)
pm10010mpCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLoadGwBank4.setStatus("current")
_Pm10010mpCtrlledTest_ObjectIdentity = ObjectIdentity
pm10010mpCtrlledTest = _Pm10010mpCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 192)
)
_Pm10010mpCtrlGreenLed_Type = EkiOnOff
_Pm10010mpCtrlGreenLed_Object = MibScalar
pm10010mpCtrlGreenLed = _Pm10010mpCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 192, 1),
    _Pm10010mpCtrlGreenLed_Type()
)
pm10010mpCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlGreenLed.setStatus("current")
_Pm10010mpCtrlRedLed_Type = EkiOnOff
_Pm10010mpCtrlRedLed_Object = MibScalar
pm10010mpCtrlRedLed = _Pm10010mpCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 192, 2),
    _Pm10010mpCtrlRedLed_Type()
)
pm10010mpCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlRedLed.setStatus("current")
_Pm10010mpCtrlLedOff_Type = EkiOnOff
_Pm10010mpCtrlLedOff_Object = MibScalar
pm10010mpCtrlLedOff = _Pm10010mpCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 192, 3),
    _Pm10010mpCtrlLedOff_Type()
)
pm10010mpCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlLedOff.setStatus("current")
_Pm10010mpCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm10010mpCtrlinitSwitchMarvell = _Pm10010mpCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 201)
)
_Pm10010mpCtrlInitSwitchMarvell_Type = EkiOnOff
_Pm10010mpCtrlInitSwitchMarvell_Object = MibScalar
pm10010mpCtrlInitSwitchMarvell = _Pm10010mpCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 201, 1),
    _Pm10010mpCtrlInitSwitchMarvell_Type()
)
pm10010mpCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlInitSwitchMarvell.setStatus("current")
_Pm10010mpCtrlresetCount_ObjectIdentity = ObjectIdentity
pm10010mpCtrlresetCount = _Pm10010mpCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 259)
)
_Pm10010mpCtrlResetcount_Type = EkiOnOff
_Pm10010mpCtrlResetcount_Object = MibScalar
pm10010mpCtrlResetcount = _Pm10010mpCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 259, 1),
    _Pm10010mpCtrlResetcount_Type()
)
pm10010mpCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlResetcount.setStatus("current")
_Pm10010mpCtrlresetRmon_ObjectIdentity = ObjectIdentity
pm10010mpCtrlresetRmon = _Pm10010mpCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 260)
)
_Pm10010mpCtrlResetrmon_Type = EkiOnOff
_Pm10010mpCtrlResetrmon_Object = MibScalar
pm10010mpCtrlResetrmon = _Pm10010mpCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 260, 1),
    _Pm10010mpCtrlResetrmon_Type()
)
pm10010mpCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlResetrmon.setStatus("current")
_Pm10010mpCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm10010mpCtrlresetMeasurements = _Pm10010mpCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 261)
)
_Pm10010mpCtrlResetmeasurements_Type = EkiOnOff
_Pm10010mpCtrlResetmeasurements_Object = MibScalar
pm10010mpCtrlResetmeasurements = _Pm10010mpCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 1, 261, 1),
    _Pm10010mpCtrlResetmeasurements_Type()
)
pm10010mpCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlResetmeasurements.setStatus("current")
_Pm10010mpCtrlClient_ObjectIdentity = ObjectIdentity
pm10010mpCtrlClient = _Pm10010mpCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2)
)
_Pm10010mpCtrlaccessLoopTable_Object = MibTable
pm10010mpCtrlaccessLoopTable = _Pm10010mpCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlaccessLoopTable.setStatus("current")
_Pm10010mpCtrlaccessLoopEntry_Object = MibTableRow
pm10010mpCtrlaccessLoopEntry = _Pm10010mpCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 16, 1)
)
pm10010mpCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlaccessLoopEntry.setStatus("current")


class _Pm10010mpCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm10010mpCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlaccessLoopIndex_Object = MibTableColumn
pm10010mpCtrlaccessLoopIndex = _Pm10010mpCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 16, 1, 1),
    _Pm10010mpCtrlaccessLoopIndex_Type()
)
pm10010mpCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlaccessLoopIndex.setStatus("current")
_Pm10010mpCtrlaccessLoopPortn_Type = EkiState
_Pm10010mpCtrlaccessLoopPortn_Object = MibTableColumn
pm10010mpCtrlaccessLoopPortn = _Pm10010mpCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 16, 1, 2),
    _Pm10010mpCtrlaccessLoopPortn_Type()
)
pm10010mpCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlaccessLoopPortn.setStatus("current")
_Pm10010mpCtrlclientLoopToLineTable_Object = MibTable
pm10010mpCtrlclientLoopToLineTable = _Pm10010mpCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlclientLoopToLineTable.setStatus("current")
_Pm10010mpCtrlclientLoopToLineEntry_Object = MibTableRow
pm10010mpCtrlclientLoopToLineEntry = _Pm10010mpCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 17, 1)
)
pm10010mpCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlclientLoopToLineEntry.setStatus("current")


class _Pm10010mpCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm10010mpCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlclientLoopToLineIndex_Object = MibTableColumn
pm10010mpCtrlclientLoopToLineIndex = _Pm10010mpCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 17, 1, 1),
    _Pm10010mpCtrlclientLoopToLineIndex_Type()
)
pm10010mpCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlclientLoopToLineIndex.setStatus("current")
_Pm10010mpCtrlclientLoopToLinePortn_Type = EkiState
_Pm10010mpCtrlclientLoopToLinePortn_Object = MibTableColumn
pm10010mpCtrlclientLoopToLinePortn = _Pm10010mpCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 17, 1, 2),
    _Pm10010mpCtrlclientLoopToLinePortn_Type()
)
pm10010mpCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlclientLoopToLinePortn.setStatus("current")
_Pm10010mpCtrlcsfUpInsTable_Object = MibTable
pm10010mpCtrlcsfUpInsTable = _Pm10010mpCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlcsfUpInsTable.setStatus("current")
_Pm10010mpCtrlcsfUpInsEntry_Object = MibTableRow
pm10010mpCtrlcsfUpInsEntry = _Pm10010mpCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 21, 1)
)
pm10010mpCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlcsfUpInsEntry.setStatus("current")


class _Pm10010mpCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm10010mpCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlcsfUpInsIndex_Object = MibTableColumn
pm10010mpCtrlcsfUpInsIndex = _Pm10010mpCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 21, 1, 1),
    _Pm10010mpCtrlcsfUpInsIndex_Type()
)
pm10010mpCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlcsfUpInsIndex.setStatus("current")
_Pm10010mpCtrlcsfUpInsPortn_Type = EkiState
_Pm10010mpCtrlcsfUpInsPortn_Object = MibTableColumn
pm10010mpCtrlcsfUpInsPortn = _Pm10010mpCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 21, 1, 2),
    _Pm10010mpCtrlcsfUpInsPortn_Type()
)
pm10010mpCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlcsfUpInsPortn.setStatus("current")
_Pm10010mpCtrlcaisDwInsTable_Object = MibTable
pm10010mpCtrlcaisDwInsTable = _Pm10010mpCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlcaisDwInsTable.setStatus("current")
_Pm10010mpCtrlcaisDwInsEntry_Object = MibTableRow
pm10010mpCtrlcaisDwInsEntry = _Pm10010mpCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 22, 1)
)
pm10010mpCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlcaisDwInsEntry.setStatus("current")


class _Pm10010mpCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm10010mpCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlcaisDwInsIndex_Object = MibTableColumn
pm10010mpCtrlcaisDwInsIndex = _Pm10010mpCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 22, 1, 1),
    _Pm10010mpCtrlcaisDwInsIndex_Type()
)
pm10010mpCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlcaisDwInsIndex.setStatus("current")
_Pm10010mpCtrlcaisDwInsPortn_Type = EkiState
_Pm10010mpCtrlcaisDwInsPortn_Object = MibTableColumn
pm10010mpCtrlcaisDwInsPortn = _Pm10010mpCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 2, 22, 1, 2),
    _Pm10010mpCtrlcaisDwInsPortn_Type()
)
pm10010mpCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlcaisDwInsPortn.setStatus("current")
_Pm10010mpCtrlLine_ObjectIdentity = ObjectIdentity
pm10010mpCtrlLine = _Pm10010mpCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3)
)
_Pm10010mpCtrlcommAccessLoopTable_Object = MibTable
pm10010mpCtrlcommAccessLoopTable = _Pm10010mpCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlcommAccessLoopTable.setStatus("current")
_Pm10010mpCtrlcommAccessLoopEntry_Object = MibTableRow
pm10010mpCtrlcommAccessLoopEntry = _Pm10010mpCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 64, 1)
)
pm10010mpCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlcommAccessLoopEntry.setStatus("current")


class _Pm10010mpCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm10010mpCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlcommAccessLoopIndex_Object = MibTableColumn
pm10010mpCtrlcommAccessLoopIndex = _Pm10010mpCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 64, 1, 1),
    _Pm10010mpCtrlcommAccessLoopIndex_Type()
)
pm10010mpCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlcommAccessLoopIndex.setStatus("current")
_Pm10010mpCtrlcommAccessLoopPortn_Type = EkiState
_Pm10010mpCtrlcommAccessLoopPortn_Object = MibTableColumn
pm10010mpCtrlcommAccessLoopPortn = _Pm10010mpCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 64, 1, 2),
    _Pm10010mpCtrlcommAccessLoopPortn_Type()
)
pm10010mpCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlcommAccessLoopPortn.setStatus("current")
_Pm10010mpCtrllineLoopTable_Object = MibTable
pm10010mpCtrllineLoopTable = _Pm10010mpCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm10010mpCtrllineLoopTable.setStatus("current")
_Pm10010mpCtrllineLoopEntry_Object = MibTableRow
pm10010mpCtrllineLoopEntry = _Pm10010mpCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 66, 1)
)
pm10010mpCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrllineLoopEntry.setStatus("current")


class _Pm10010mpCtrllineLoopIndex_Type(Integer32):
    """Custom type pm10010mpCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrllineLoopIndex_Object = MibTableColumn
pm10010mpCtrllineLoopIndex = _Pm10010mpCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 66, 1, 1),
    _Pm10010mpCtrllineLoopIndex_Type()
)
pm10010mpCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrllineLoopIndex.setStatus("current")
_Pm10010mpCtrllineLoopPortn_Type = EkiState
_Pm10010mpCtrllineLoopPortn_Object = MibTableColumn
pm10010mpCtrllineLoopPortn = _Pm10010mpCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 66, 1, 2),
    _Pm10010mpCtrllineLoopPortn_Type()
)
pm10010mpCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrllineLoopPortn.setStatus("current")
_Pm10010mpCtrlfecDisableTable_Object = MibTable
pm10010mpCtrlfecDisableTable = _Pm10010mpCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlfecDisableTable.setStatus("current")
_Pm10010mpCtrlfecDisableEntry_Object = MibTableRow
pm10010mpCtrlfecDisableEntry = _Pm10010mpCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 69, 1)
)
pm10010mpCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlfecDisableEntry.setStatus("current")


class _Pm10010mpCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm10010mpCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlfecDisableIndex_Object = MibTableColumn
pm10010mpCtrlfecDisableIndex = _Pm10010mpCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 69, 1, 1),
    _Pm10010mpCtrlfecDisableIndex_Type()
)
pm10010mpCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlfecDisableIndex.setStatus("current")
_Pm10010mpCtrlfecDisablePortn_Type = EkiState
_Pm10010mpCtrlfecDisablePortn_Object = MibTableColumn
pm10010mpCtrlfecDisablePortn = _Pm10010mpCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 69, 1, 2),
    _Pm10010mpCtrlfecDisablePortn_Type()
)
pm10010mpCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlfecDisablePortn.setStatus("current")
_Pm10010mpCtrlmsaLineLoopTable_Object = MibTable
pm10010mpCtrlmsaLineLoopTable = _Pm10010mpCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaLineLoopTable.setStatus("current")
_Pm10010mpCtrlmsaLineLoopEntry_Object = MibTableRow
pm10010mpCtrlmsaLineLoopEntry = _Pm10010mpCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 209, 1)
)
pm10010mpCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaLineLoopEntry.setStatus("current")


class _Pm10010mpCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm10010mpCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlmsaLineLoopIndex_Object = MibTableColumn
pm10010mpCtrlmsaLineLoopIndex = _Pm10010mpCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 209, 1, 1),
    _Pm10010mpCtrlmsaLineLoopIndex_Type()
)
pm10010mpCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaLineLoopIndex.setStatus("current")
_Pm10010mpCtrlmsaLineLoopPortn_Type = EkiState
_Pm10010mpCtrlmsaLineLoopPortn_Object = MibTableColumn
pm10010mpCtrlmsaLineLoopPortn = _Pm10010mpCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 209, 1, 2),
    _Pm10010mpCtrlmsaLineLoopPortn_Type()
)
pm10010mpCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaLineLoopPortn.setStatus("current")
_Pm10010mpCtrlmsaTxResetTable_Object = MibTable
pm10010mpCtrlmsaTxResetTable = _Pm10010mpCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaTxResetTable.setStatus("current")
_Pm10010mpCtrlmsaTxResetEntry_Object = MibTableRow
pm10010mpCtrlmsaTxResetEntry = _Pm10010mpCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 210, 1)
)
pm10010mpCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaTxResetEntry.setStatus("current")


class _Pm10010mpCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm10010mpCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlmsaTxResetIndex_Object = MibTableColumn
pm10010mpCtrlmsaTxResetIndex = _Pm10010mpCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 210, 1, 1),
    _Pm10010mpCtrlmsaTxResetIndex_Type()
)
pm10010mpCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaTxResetIndex.setStatus("current")
_Pm10010mpCtrlmsaTxResetPortn_Type = EkiState
_Pm10010mpCtrlmsaTxResetPortn_Object = MibTableColumn
pm10010mpCtrlmsaTxResetPortn = _Pm10010mpCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 210, 1, 2),
    _Pm10010mpCtrlmsaTxResetPortn_Type()
)
pm10010mpCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaTxResetPortn.setStatus("current")
_Pm10010mpCtrlmsaRxResetTable_Object = MibTable
pm10010mpCtrlmsaRxResetTable = _Pm10010mpCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaRxResetTable.setStatus("current")
_Pm10010mpCtrlmsaRxResetEntry_Object = MibTableRow
pm10010mpCtrlmsaRxResetEntry = _Pm10010mpCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 211, 1)
)
pm10010mpCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaRxResetEntry.setStatus("current")


class _Pm10010mpCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm10010mpCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlmsaRxResetIndex_Object = MibTableColumn
pm10010mpCtrlmsaRxResetIndex = _Pm10010mpCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 211, 1, 1),
    _Pm10010mpCtrlmsaRxResetIndex_Type()
)
pm10010mpCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaRxResetIndex.setStatus("current")
_Pm10010mpCtrlmsaRxResetPortn_Type = EkiState
_Pm10010mpCtrlmsaRxResetPortn_Object = MibTableColumn
pm10010mpCtrlmsaRxResetPortn = _Pm10010mpCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 211, 1, 2),
    _Pm10010mpCtrlmsaRxResetPortn_Type()
)
pm10010mpCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaRxResetPortn.setStatus("current")
_Pm10010mpCtrlmsaShutdownTable_Object = MibTable
pm10010mpCtrlmsaShutdownTable = _Pm10010mpCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaShutdownTable.setStatus("current")
_Pm10010mpCtrlmsaShutdownEntry_Object = MibTableRow
pm10010mpCtrlmsaShutdownEntry = _Pm10010mpCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 212, 1)
)
pm10010mpCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaShutdownEntry.setStatus("current")


class _Pm10010mpCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm10010mpCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm10010mpCtrlmsaShutdownIndex_Object = MibTableColumn
pm10010mpCtrlmsaShutdownIndex = _Pm10010mpCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 212, 1, 1),
    _Pm10010mpCtrlmsaShutdownIndex_Type()
)
pm10010mpCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaShutdownIndex.setStatus("current")
_Pm10010mpCtrlmsaShutdownPortn_Type = EkiState
_Pm10010mpCtrlmsaShutdownPortn_Object = MibTableColumn
pm10010mpCtrlmsaShutdownPortn = _Pm10010mpCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 6, 3, 212, 1, 2),
    _Pm10010mpCtrlmsaShutdownPortn_Type()
)
pm10010mpCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCtrlmsaShutdownPortn.setStatus("current")
_Pm10010mpri_ObjectIdentity = ObjectIdentity
pm10010mpri = _Pm10010mpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7)
)
_Pm10010mpriTable_ObjectIdentity = ObjectIdentity
pm10010mpriTable = _Pm10010mpriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1)
)
_Pm10010mpRinvSfpTable_Object = MibTable
pm10010mpRinvSfpTable = _Pm10010mpRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010mpRinvSfpTable.setStatus("current")
_Pm10010mpRinvSfpEntry_Object = MibTableRow
pm10010mpRinvSfpEntry = _Pm10010mpRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 1, 1)
)
pm10010mpRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpRinvSfpEntry.setStatus("current")


class _Pm10010mpRinvSfpIndex_Type(Integer32):
    """Custom type pm10010mpRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010mpRinvSfpIndex_Type.__name__ = "Integer32"
_Pm10010mpRinvSfpIndex_Object = MibTableColumn
pm10010mpRinvSfpIndex = _Pm10010mpRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 1, 1, 1),
    _Pm10010mpRinvSfpIndex_Type()
)
pm10010mpRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvSfpIndex.setStatus("current")
_Pm10010mpRinvsfp_Type = DisplayString
_Pm10010mpRinvsfp_Object = MibTableColumn
pm10010mpRinvsfp = _Pm10010mpRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 1, 1, 2),
    _Pm10010mpRinvsfp_Type()
)
pm10010mpRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvsfp.setStatus("current")
_Pm10010mpRinvLineTable_Object = MibTable
pm10010mpRinvLineTable = _Pm10010mpRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm10010mpRinvLineTable.setStatus("current")
_Pm10010mpRinvLineEntry_Object = MibTableRow
pm10010mpRinvLineEntry = _Pm10010mpRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 2, 1)
)
pm10010mpRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpRinvLineEntry.setStatus("current")


class _Pm10010mpRinvLineIndex_Type(Integer32):
    """Custom type pm10010mpRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm10010mpRinvLineIndex_Type.__name__ = "Integer32"
_Pm10010mpRinvLineIndex_Object = MibTableColumn
pm10010mpRinvLineIndex = _Pm10010mpRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 2, 1, 1),
    _Pm10010mpRinvLineIndex_Type()
)
pm10010mpRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvLineIndex.setStatus("current")
_Pm10010mpRinvxfpLine_Type = DisplayString
_Pm10010mpRinvxfpLine_Object = MibTableColumn
pm10010mpRinvxfpLine = _Pm10010mpRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 1, 2, 1, 2),
    _Pm10010mpRinvxfpLine_Type()
)
pm10010mpRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvxfpLine.setStatus("current")
_Pm10010mpRinvReloadInventory_Type = EkiOnOff
_Pm10010mpRinvReloadInventory_Object = MibScalar
pm10010mpRinvReloadInventory = _Pm10010mpRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 2),
    _Pm10010mpRinvReloadInventory_Type()
)
pm10010mpRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpRinvReloadInventory.setStatus("current")
_Pm10010mpRinvHwPlatform_Type = DisplayString
_Pm10010mpRinvHwPlatform_Object = MibScalar
pm10010mpRinvHwPlatform = _Pm10010mpRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 3),
    _Pm10010mpRinvHwPlatform_Type()
)
pm10010mpRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvHwPlatform.setStatus("current")
_Pm10010mpRinvModulePlatform_Type = DisplayString
_Pm10010mpRinvModulePlatform_Object = MibScalar
pm10010mpRinvModulePlatform = _Pm10010mpRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 4),
    _Pm10010mpRinvModulePlatform_Type()
)
pm10010mpRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvModulePlatform.setStatus("current")
_Pm10010mpRinvSwPlatform_Type = DisplayString
_Pm10010mpRinvSwPlatform_Object = MibScalar
pm10010mpRinvSwPlatform = _Pm10010mpRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 5),
    _Pm10010mpRinvSwPlatform_Type()
)
pm10010mpRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvSwPlatform.setStatus("current")
_Pm10010mpRinvGwPlatform_Type = DisplayString
_Pm10010mpRinvGwPlatform_Object = MibScalar
pm10010mpRinvGwPlatform = _Pm10010mpRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 7, 6),
    _Pm10010mpRinvGwPlatform_Type()
)
pm10010mpRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpRinvGwPlatform.setStatus("current")
_Pm10010mpdownload_ObjectIdentity = ObjectIdentity
pm10010mpdownload = _Pm10010mpdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8)
)
_Pm10010mpDwlOther_ObjectIdentity = ObjectIdentity
pm10010mpDwlOther = _Pm10010mpDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1)
)
_Pm10010mpDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm10010mpDwlrestartProcess = _Pm10010mpDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 0)
)
_Pm10010mpDwlWarmRestartProcessed_Type = EkiOnOff
_Pm10010mpDwlWarmRestartProcessed_Object = MibScalar
pm10010mpDwlWarmRestartProcessed = _Pm10010mpDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 0, 1),
    _Pm10010mpDwlWarmRestartProcessed_Type()
)
pm10010mpDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlWarmRestartProcessed.setStatus("current")
_Pm10010mpDwlColdRestartProcessed_Type = EkiOnOff
_Pm10010mpDwlColdRestartProcessed_Object = MibScalar
pm10010mpDwlColdRestartProcessed = _Pm10010mpDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 0, 2),
    _Pm10010mpDwlColdRestartProcessed_Type()
)
pm10010mpDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlColdRestartProcessed.setStatus("current")
_Pm10010mpDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm10010mpDwlswBanksUsed = _Pm10010mpDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 1)
)
_Pm10010mpDwlSwBank1Used_Type = EkiOnOff
_Pm10010mpDwlSwBank1Used_Object = MibScalar
pm10010mpDwlSwBank1Used = _Pm10010mpDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 1, 1),
    _Pm10010mpDwlSwBank1Used_Type()
)
pm10010mpDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlSwBank1Used.setStatus("current")
_Pm10010mpDwlSwBank2Used_Type = EkiOnOff
_Pm10010mpDwlSwBank2Used_Object = MibScalar
pm10010mpDwlSwBank2Used = _Pm10010mpDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 1, 2),
    _Pm10010mpDwlSwBank2Used_Type()
)
pm10010mpDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlSwBank2Used.setStatus("current")
_Pm10010mpDwlSwBank1Notempty_Type = EkiOnOff
_Pm10010mpDwlSwBank1Notempty_Object = MibScalar
pm10010mpDwlSwBank1Notempty = _Pm10010mpDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 1, 5),
    _Pm10010mpDwlSwBank1Notempty_Type()
)
pm10010mpDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlSwBank1Notempty.setStatus("current")
_Pm10010mpDwlSwBank2Notempty_Type = EkiOnOff
_Pm10010mpDwlSwBank2Notempty_Object = MibScalar
pm10010mpDwlSwBank2Notempty = _Pm10010mpDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 1, 6),
    _Pm10010mpDwlSwBank2Notempty_Type()
)
pm10010mpDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlSwBank2Notempty.setStatus("current")
_Pm10010mpDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm10010mpDwlgwBanksUsed = _Pm10010mpDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2)
)
_Pm10010mpDwlGwBank1Used_Type = EkiOnOff
_Pm10010mpDwlGwBank1Used_Object = MibScalar
pm10010mpDwlGwBank1Used = _Pm10010mpDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 1),
    _Pm10010mpDwlGwBank1Used_Type()
)
pm10010mpDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank1Used.setStatus("current")
_Pm10010mpDwlGwBank2Used_Type = EkiOnOff
_Pm10010mpDwlGwBank2Used_Object = MibScalar
pm10010mpDwlGwBank2Used = _Pm10010mpDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 2),
    _Pm10010mpDwlGwBank2Used_Type()
)
pm10010mpDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank2Used.setStatus("current")
_Pm10010mpDwlGwBank3Used_Type = EkiOnOff
_Pm10010mpDwlGwBank3Used_Object = MibScalar
pm10010mpDwlGwBank3Used = _Pm10010mpDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 3),
    _Pm10010mpDwlGwBank3Used_Type()
)
pm10010mpDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank3Used.setStatus("current")
_Pm10010mpDwlGwBank4Used_Type = EkiOnOff
_Pm10010mpDwlGwBank4Used_Object = MibScalar
pm10010mpDwlGwBank4Used = _Pm10010mpDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 4),
    _Pm10010mpDwlGwBank4Used_Type()
)
pm10010mpDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank4Used.setStatus("current")
_Pm10010mpDwlGwBank1Notempty_Type = EkiOnOff
_Pm10010mpDwlGwBank1Notempty_Object = MibScalar
pm10010mpDwlGwBank1Notempty = _Pm10010mpDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 5),
    _Pm10010mpDwlGwBank1Notempty_Type()
)
pm10010mpDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank1Notempty.setStatus("current")
_Pm10010mpDwlGwBank2Notempty_Type = EkiOnOff
_Pm10010mpDwlGwBank2Notempty_Object = MibScalar
pm10010mpDwlGwBank2Notempty = _Pm10010mpDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 6),
    _Pm10010mpDwlGwBank2Notempty_Type()
)
pm10010mpDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank2Notempty.setStatus("current")
_Pm10010mpDwlGwBank3Notempty_Type = EkiOnOff
_Pm10010mpDwlGwBank3Notempty_Object = MibScalar
pm10010mpDwlGwBank3Notempty = _Pm10010mpDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 7),
    _Pm10010mpDwlGwBank3Notempty_Type()
)
pm10010mpDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank3Notempty.setStatus("current")
_Pm10010mpDwlGwBank4Notempty_Type = EkiOnOff
_Pm10010mpDwlGwBank4Notempty_Object = MibScalar
pm10010mpDwlGwBank4Notempty = _Pm10010mpDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 1, 2, 8),
    _Pm10010mpDwlGwBank4Notempty_Type()
)
pm10010mpDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpDwlGwBank4Notempty.setStatus("current")
_Pm10010mpDwlClient_ObjectIdentity = ObjectIdentity
pm10010mpDwlClient = _Pm10010mpDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 2)
)
_Pm10010mpDwlLine_ObjectIdentity = ObjectIdentity
pm10010mpDwlLine = _Pm10010mpDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 8, 3)
)
_Pm10010mpConfig_ObjectIdentity = ObjectIdentity
pm10010mpConfig = _Pm10010mpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9)
)
_Pm10010mpCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm10010mpCfgAccessCAisCsf = _Pm10010mpCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 1)
)
_Pm10010mpCfgClientcaiscsfTable_Object = MibTable
pm10010mpCfgClientcaiscsfTable = _Pm10010mpCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm10010mpCfgClientcaiscsfTable.setStatus("current")
_Pm10010mpCfgClientcaiscsfEntry_Object = MibTableRow
pm10010mpCfgClientcaiscsfEntry = _Pm10010mpCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 1, 1, 1)
)
pm10010mpCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgClientcaiscsfEntry.setStatus("current")


class _Pm10010mpCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm10010mpCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgClientcaiscsfIndex_Object = MibTableColumn
pm10010mpCfgClientcaiscsfIndex = _Pm10010mpCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 1, 1, 1, 1),
    _Pm10010mpCfgClientcaiscsfIndex_Type()
)
pm10010mpCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgClientcaiscsfIndex.setStatus("current")


class _Pm10010mpCfgReservePortn_Type(Unsigned32):
    """Custom type pm10010mpCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgReservePortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgReservePortn_Object = MibTableColumn
pm10010mpCfgReservePortn = _Pm10010mpCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 1, 1, 1, 3),
    _Pm10010mpCfgReservePortn_Type()
)
pm10010mpCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgReservePortn.setStatus("current")
_Pm10010mpCfgStartup_ObjectIdentity = ObjectIdentity
pm10010mpCfgStartup = _Pm10010mpCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2)
)
_Pm10010mpCfgClientStartupTable_Object = MibTable
pm10010mpCfgClientStartupTable = _Pm10010mpCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm10010mpCfgClientStartupTable.setStatus("current")
_Pm10010mpCfgClientStartupEntry_Object = MibTableRow
pm10010mpCfgClientStartupEntry = _Pm10010mpCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 1, 1)
)
pm10010mpCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgClientStartupEntry.setStatus("current")


class _Pm10010mpCfgClientStartupIndex_Type(Integer32):
    """Custom type pm10010mpCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgClientStartupIndex_Object = MibTableColumn
pm10010mpCfgClientStartupIndex = _Pm10010mpCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 1, 1, 1),
    _Pm10010mpCfgClientStartupIndex_Type()
)
pm10010mpCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgClientStartupIndex.setStatus("current")


class _Pm10010mpCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgSystConfPortPortn_Object = MibTableColumn
pm10010mpCfgSystConfPortPortn = _Pm10010mpCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 1, 1, 3),
    _Pm10010mpCfgSystConfPortPortn_Type()
)
pm10010mpCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgSystConfPortPortn.setStatus("current")


class _Pm10010mpCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgNetConfPortPortn_Object = MibTableColumn
pm10010mpCfgNetConfPortPortn = _Pm10010mpCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 1, 1, 4),
    _Pm10010mpCfgNetConfPortPortn_Type()
)
pm10010mpCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgNetConfPortPortn.setStatus("current")


class _Pm10010mpCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgOptionsPortPortn_Object = MibTableColumn
pm10010mpCfgOptionsPortPortn = _Pm10010mpCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 1, 1, 14),
    _Pm10010mpCfgOptionsPortPortn_Type()
)
pm10010mpCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgOptionsPortPortn.setStatus("current")
_Pm10010mpCfgLineStartupTable_Object = MibTable
pm10010mpCfgLineStartupTable = _Pm10010mpCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm10010mpCfgLineStartupTable.setStatus("current")
_Pm10010mpCfgLineStartupEntry_Object = MibTableRow
pm10010mpCfgLineStartupEntry = _Pm10010mpCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 2, 1)
)
pm10010mpCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgLineStartupEntry.setStatus("current")


class _Pm10010mpCfgLineStartupIndex_Type(Integer32):
    """Custom type pm10010mpCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgLineStartupIndex_Object = MibTableColumn
pm10010mpCfgLineStartupIndex = _Pm10010mpCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 2, 1, 1),
    _Pm10010mpCfgLineStartupIndex_Type()
)
pm10010mpCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgLineStartupIndex.setStatus("current")


class _Pm10010mpCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm10010mpCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgSystConfLinePortn_Object = MibTableColumn
pm10010mpCfgSystConfLinePortn = _Pm10010mpCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 2, 1, 3),
    _Pm10010mpCfgSystConfLinePortn_Type()
)
pm10010mpCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgSystConfLinePortn.setStatus("current")


class _Pm10010mpCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm10010mpCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgOptionsLinePortn_Object = MibTableColumn
pm10010mpCfgOptionsLinePortn = _Pm10010mpCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 2, 1, 14),
    _Pm10010mpCfgOptionsLinePortn_Type()
)
pm10010mpCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgOptionsLinePortn.setStatus("current")
_Pm10010mpCfgXfpTable_Object = MibTable
pm10010mpCfgXfpTable = _Pm10010mpCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm10010mpCfgXfpTable.setStatus("current")
_Pm10010mpCfgXfpEntry_Object = MibTableRow
pm10010mpCfgXfpEntry = _Pm10010mpCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 3, 1)
)
pm10010mpCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgXfpEntry.setStatus("current")


class _Pm10010mpCfgXfpIndex_Type(Integer32):
    """Custom type pm10010mpCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgXfpIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgXfpIndex_Object = MibTableColumn
pm10010mpCfgXfpIndex = _Pm10010mpCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 3, 1, 1),
    _Pm10010mpCfgXfpIndex_Type()
)
pm10010mpCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgXfpIndex.setStatus("current")


class _Pm10010mpCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm10010mpCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgSystConfMsaLinePortn_Object = MibTableColumn
pm10010mpCfgSystConfMsaLinePortn = _Pm10010mpCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 3, 1, 3),
    _Pm10010mpCfgSystConfMsaLinePortn_Type()
)
pm10010mpCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgSystConfMsaLinePortn.setStatus("current")
_Pm10010mpCfgClientOtxtlhTable_Object = MibTable
pm10010mpCfgClientOtxtlhTable = _Pm10010mpCfgClientOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4)
)
if mibBuilder.loadTexts:
    pm10010mpCfgClientOtxtlhTable.setStatus("current")
_Pm10010mpCfgClientOtxtlhEntry_Object = MibTableRow
pm10010mpCfgClientOtxtlhEntry = _Pm10010mpCfgClientOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1)
)
pm10010mpCfgClientOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgClientOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgClientOtxtlhEntry.setStatus("current")


class _Pm10010mpCfgClientOtxtlhIndex_Type(Integer32):
    """Custom type pm10010mpCfgClientOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgClientOtxtlhIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgClientOtxtlhIndex_Object = MibTableColumn
pm10010mpCfgClientOtxtlhIndex = _Pm10010mpCfgClientOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1, 1),
    _Pm10010mpCfgClientOtxtlhIndex_Type()
)
pm10010mpCfgClientOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgClientOtxtlhIndex.setStatus("current")


class _Pm10010mpCfgControlsPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgControlsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgControlsPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgControlsPortn_Object = MibTableColumn
pm10010mpCfgControlsPortn = _Pm10010mpCfgControlsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1, 3),
    _Pm10010mpCfgControlsPortn_Type()
)
pm10010mpCfgControlsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgControlsPortn.setStatus("deprecated")


class _Pm10010mpCfgClientPwrLaserPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgClientPwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgClientPwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgClientPwrLaserPortn_Object = MibTableColumn
pm10010mpCfgClientPwrLaserPortn = _Pm10010mpCfgClientPwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1, 6),
    _Pm10010mpCfgClientPwrLaserPortn_Type()
)
pm10010mpCfgClientPwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgClientPwrLaserPortn.setStatus("current")


class _Pm10010mpCfgClientFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgClientFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgClientFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgClientFCurrentPortn_Object = MibTableColumn
pm10010mpCfgClientFCurrentPortn = _Pm10010mpCfgClientFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1, 7),
    _Pm10010mpCfgClientFCurrentPortn_Type()
)
pm10010mpCfgClientFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgClientFCurrentPortn.setStatus("current")


class _Pm10010mpCfgClientGridCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgClientGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgClientGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgClientGridCurrentPortn_Object = MibTableColumn
pm10010mpCfgClientGridCurrentPortn = _Pm10010mpCfgClientGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1, 8),
    _Pm10010mpCfgClientGridCurrentPortn_Type()
)
pm10010mpCfgClientGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgClientGridCurrentPortn.setStatus("current")


class _Pm10010mpCfgClientFoPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgClientFoPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgClientFoPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgClientFoPortn_Object = MibTableColumn
pm10010mpCfgClientFoPortn = _Pm10010mpCfgClientFoPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 2, 4, 1, 9),
    _Pm10010mpCfgClientFoPortn_Type()
)
pm10010mpCfgClientFoPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgClientFoPortn.setStatus("current")
_Pm10010mpCfgLabels_ObjectIdentity = ObjectIdentity
pm10010mpCfgLabels = _Pm10010mpCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3)
)
_Pm10010mpCfgLabelclientTable_Object = MibTable
pm10010mpCfgLabelclientTable = _Pm10010mpCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm10010mpCfgLabelclientTable.setStatus("current")
_Pm10010mpCfgLabelclientEntry_Object = MibTableRow
pm10010mpCfgLabelclientEntry = _Pm10010mpCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 1, 1)
)
pm10010mpCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgLabelclientEntry.setStatus("current")


class _Pm10010mpCfgLabelclientIndex_Type(Integer32):
    """Custom type pm10010mpCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgLabelclientIndex_Object = MibTableColumn
pm10010mpCfgLabelclientIndex = _Pm10010mpCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 1, 1, 1),
    _Pm10010mpCfgLabelclientIndex_Type()
)
pm10010mpCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgLabelclientIndex.setStatus("current")


class _Pm10010mpCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm10010mpCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010mpCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm10010mpCfgLabelclientPortn_Object = MibTableColumn
pm10010mpCfgLabelclientPortn = _Pm10010mpCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 1, 1, 3),
    _Pm10010mpCfgLabelclientPortn_Type()
)
pm10010mpCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgLabelclientPortn.setStatus("current")
_Pm10010mpCfgLabellineTable_Object = MibTable
pm10010mpCfgLabellineTable = _Pm10010mpCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm10010mpCfgLabellineTable.setStatus("current")
_Pm10010mpCfgLabellineEntry_Object = MibTableRow
pm10010mpCfgLabellineEntry = _Pm10010mpCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 2, 1)
)
pm10010mpCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgLabellineEntry.setStatus("current")


class _Pm10010mpCfgLabellineIndex_Type(Integer32):
    """Custom type pm10010mpCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgLabellineIndex_Object = MibTableColumn
pm10010mpCfgLabellineIndex = _Pm10010mpCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 2, 1, 1),
    _Pm10010mpCfgLabellineIndex_Type()
)
pm10010mpCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgLabellineIndex.setStatus("current")


class _Pm10010mpCfgLabellinePortn_Type(DisplayString):
    """Custom type pm10010mpCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm10010mpCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm10010mpCfgLabellinePortn_Object = MibTableColumn
pm10010mpCfgLabellinePortn = _Pm10010mpCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 3, 2, 1, 3),
    _Pm10010mpCfgLabellinePortn_Type()
)
pm10010mpCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgLabellinePortn.setStatus("current")
_Pm10010mpCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm10010mpCfgStartuptlh = _Pm10010mpCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4)
)
_Pm10010mpCfgOtxtlhTable_Object = MibTable
pm10010mpCfgOtxtlhTable = _Pm10010mpCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm10010mpCfgOtxtlhTable.setStatus("current")
_Pm10010mpCfgOtxtlhEntry_Object = MibTableRow
pm10010mpCfgOtxtlhEntry = _Pm10010mpCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1)
)
pm10010mpCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgOtxtlhEntry.setStatus("current")


class _Pm10010mpCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm10010mpCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgOtxtlhIndex_Object = MibTableColumn
pm10010mpCfgOtxtlhIndex = _Pm10010mpCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1, 1),
    _Pm10010mpCfgOtxtlhIndex_Type()
)
pm10010mpCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgOtxtlhIndex.setStatus("current")


class _Pm10010mpCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgLinePwrLaserPortn_Object = MibTableColumn
pm10010mpCfgLinePwrLaserPortn = _Pm10010mpCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1, 6),
    _Pm10010mpCfgLinePwrLaserPortn_Type()
)
pm10010mpCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgLinePwrLaserPortn.setStatus("current")


class _Pm10010mpCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgLineFCurrentPortn_Object = MibTableColumn
pm10010mpCfgLineFCurrentPortn = _Pm10010mpCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1, 7),
    _Pm10010mpCfgLineFCurrentPortn_Type()
)
pm10010mpCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgLineFCurrentPortn.setStatus("current")


class _Pm10010mpCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgLineGridCurrentPortn_Object = MibTableColumn
pm10010mpCfgLineGridCurrentPortn = _Pm10010mpCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1, 8),
    _Pm10010mpCfgLineGridCurrentPortn_Type()
)
pm10010mpCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgLineGridCurrentPortn.setStatus("current")


class _Pm10010mpCfgFPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgFPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgFPortn_Object = MibTableColumn
pm10010mpCfgFPortn = _Pm10010mpCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1, 9),
    _Pm10010mpCfgFPortn_Type()
)
pm10010mpCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgFPortn.setStatus("current")


class _Pm10010mpCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgRxLineFCurrentPortn_Object = MibTableColumn
pm10010mpCfgRxLineFCurrentPortn = _Pm10010mpCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 4, 1, 1, 10),
    _Pm10010mpCfgRxLineFCurrentPortn_Type()
)
pm10010mpCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgRxLineFCurrentPortn.setStatus("current")
_Pm10010mpCfgOther_ObjectIdentity = ObjectIdentity
pm10010mpCfgOther = _Pm10010mpCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 5)
)
_Pm10010mptablemoduleOther_ObjectIdentity = ObjectIdentity
pm10010mptablemoduleOther = _Pm10010mptablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 5, 1)
)


class _Pm10010mpCfgmode_Type(Unsigned32):
    """Custom type pm10010mpCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgmode_Type.__name__ = "Unsigned32"
_Pm10010mpCfgmode_Object = MibScalar
pm10010mpCfgmode = _Pm10010mpCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 5, 1, 2),
    _Pm10010mpCfgmode_Type()
)
pm10010mpCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgmode.setStatus("current")


class _Pm10010mpCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010mpCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010mpCfgfanLowSpeedThreshold_Object = MibScalar
pm10010mpCfgfanLowSpeedThreshold = _Pm10010mpCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 5, 1, 3),
    _Pm10010mpCfgfanLowSpeedThreshold_Type()
)
pm10010mpCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgfanLowSpeedThreshold.setStatus("current")


class _Pm10010mpCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm10010mpCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm10010mpCfgfanHighSpeedThreshold_Object = MibScalar
pm10010mpCfgfanHighSpeedThreshold = _Pm10010mpCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 5, 1, 4),
    _Pm10010mpCfgfanHighSpeedThreshold_Type()
)
pm10010mpCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgfanHighSpeedThreshold.setStatus("current")
_Pm10010mpCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm10010mpCfgStartuptablefive = _Pm10010mpCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6)
)
_Pm10010mpCfgOtxtlhcapabilitiesTable_Object = MibTable
pm10010mpCfgOtxtlhcapabilitiesTable = _Pm10010mpCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm10010mpCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm10010mpCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm10010mpCfgOtxtlhcapabilitiesEntry = _Pm10010mpCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1)
)
pm10010mpCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm10010mpCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm10010mpCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm10010mpCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm10010mpCfgOtxtlhcapabilitiesIndex = _Pm10010mpCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1, 1),
    _Pm10010mpCfgOtxtlhcapabilitiesIndex_Type()
)
pm10010mpCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm10010mpCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm10010mpCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgComponentTypePortn_Object = MibTableColumn
pm10010mpCfgComponentTypePortn = _Pm10010mpCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1, 3),
    _Pm10010mpCfgComponentTypePortn_Type()
)
pm10010mpCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgComponentTypePortn.setStatus("current")


class _Pm10010mpCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgMiscellaneousPortn_Object = MibTableColumn
pm10010mpCfgMiscellaneousPortn = _Pm10010mpCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1, 4),
    _Pm10010mpCfgMiscellaneousPortn_Type()
)
pm10010mpCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgMiscellaneousPortn.setStatus("current")


class _Pm10010mpCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgFirstChannelPortn_Object = MibTableColumn
pm10010mpCfgFirstChannelPortn = _Pm10010mpCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1, 5),
    _Pm10010mpCfgFirstChannelPortn_Type()
)
pm10010mpCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgFirstChannelPortn.setStatus("current")


class _Pm10010mpCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgLastChannelPortn_Object = MibTableColumn
pm10010mpCfgLastChannelPortn = _Pm10010mpCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1, 6),
    _Pm10010mpCfgLastChannelPortn_Type()
)
pm10010mpCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgLastChannelPortn.setStatus("current")


class _Pm10010mpCfgGridPortn_Type(Unsigned32):
    """Custom type pm10010mpCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm10010mpCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm10010mpCfgGridPortn_Object = MibTableColumn
pm10010mpCfgGridPortn = _Pm10010mpCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 6, 1, 1, 7),
    _Pm10010mpCfgGridPortn_Type()
)
pm10010mpCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpCfgGridPortn.setStatus("current")
_Pm10010mpCfgWriteConfiguration_Type = EkiOnOff
_Pm10010mpCfgWriteConfiguration_Object = MibScalar
pm10010mpCfgWriteConfiguration = _Pm10010mpCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 9, 257),
    _Pm10010mpCfgWriteConfiguration_Type()
)
pm10010mpCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm10010mpCfgWriteConfiguration.setStatus("current")
_Pm10010mptraps_ObjectIdentity = ObjectIdentity
pm10010mptraps = _Pm10010mptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10)
)


class _Pm10010mptrapPortNumber_Type(Integer32):
    """Custom type pm10010mptrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mptrapPortNumber_Type.__name__ = "Integer32"
_Pm10010mptrapPortNumber_Object = MibScalar
pm10010mptrapPortNumber = _Pm10010mptrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 2),
    _Pm10010mptrapPortNumber_Type()
)
pm10010mptrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptrapPortNumber.setStatus("current")


class _Pm10010mptrapLineNumber_Type(Integer32):
    """Custom type pm10010mptrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mptrapLineNumber_Type.__name__ = "Integer32"
_Pm10010mptrapLineNumber_Object = MibScalar
pm10010mptrapLineNumber = _Pm10010mptrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 3),
    _Pm10010mptrapLineNumber_Type()
)
pm10010mptrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptrapLineNumber.setStatus("current")


class _Pm10010mptrapBoardNumber_Type(Integer32):
    """Custom type pm10010mptrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm10010mptrapBoardNumber_Type.__name__ = "Integer32"
_Pm10010mptrapBoardNumber_Object = MibScalar
pm10010mptrapBoardNumber = _Pm10010mptrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 4),
    _Pm10010mptrapBoardNumber_Type()
)
pm10010mptrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mptrapBoardNumber.setStatus("current")
_Pm10010mpMonitoring_ObjectIdentity = ObjectIdentity
pm10010mpMonitoring = _Pm10010mpMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11)
)
_Pm10010mpMonOther_ObjectIdentity = ObjectIdentity
pm10010mpMonOther = _Pm10010mpMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 1)
)
_Pm10010mpMonRmon_ObjectIdentity = ObjectIdentity
pm10010mpMonRmon = _Pm10010mpMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 1, 3)
)
_Pm10010mpMonClient_ObjectIdentity = ObjectIdentity
pm10010mpMonClient = _Pm10010mpMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2)
)
_Pm10010mpMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm10010mpMonClientRmonCounter = _Pm10010mpMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4)
)
_Pm10010mpMonupRmonBytesCounterClientInputTable_Object = MibTable
pm10010mpMonupRmonBytesCounterClientInputTable = _Pm10010mpMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm10010mpMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm10010mpMonupRmonBytesCounterClientInputEntry = _Pm10010mpMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 16, 1)
)
pm10010mpMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm10010mpMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mpMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mpMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm10010mpMonupRmonBytesCounterClientInputIndex = _Pm10010mpMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 16, 1, 1),
    _Pm10010mpMonupRmonBytesCounterClientInputIndex_Type()
)
pm10010mpMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm10010mpMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm10010mpMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm10010mpMonupRmonBytesCounterClientInputValuePortn = _Pm10010mpMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 16, 1, 2),
    _Pm10010mpMonupRmonBytesCounterClientInputValuePortn_Type()
)
pm10010mpMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm10010mpMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mpMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mpMonupRmonBytesCounterClientInputErrorPortn = _Pm10010mpMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 16, 1, 3),
    _Pm10010mpMonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm10010mpMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mpMonupRmonBytesCounterClientInputOverloadPortn = _Pm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 16, 1, 4),
    _Pm10010mpMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm10010mpMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mpMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm10010mpMonupRmonCrcErrorsCounterClientInputTable = _Pm10010mpMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm10010mpMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm10010mpMonupRmonCrcErrorsCounterClientInputEntry = _Pm10010mpMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 32, 1)
)
pm10010mpMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mpMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm10010mpMonupRmonCrcErrorsCounterClientInputIndex = _Pm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 32, 1, 1),
    _Pm10010mpMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm10010mpMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn = _Pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 32, 1, 2),
    _Pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 32, 1, 3),
    _Pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 32, 1, 4),
    _Pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mpMonupRmonPacketsCounterClientInputTable_Object = MibTable
pm10010mpMonupRmonPacketsCounterClientInputTable = _Pm10010mpMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm10010mpMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm10010mpMonupRmonPacketsCounterClientInputEntry = _Pm10010mpMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 48, 1)
)
pm10010mpMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm10010mpMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mpMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mpMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm10010mpMonupRmonPacketsCounterClientInputIndex = _Pm10010mpMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 48, 1, 1),
    _Pm10010mpMonupRmonPacketsCounterClientInputIndex_Type()
)
pm10010mpMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm10010mpMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm10010mpMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm10010mpMonupRmonPacketsCounterClientInputValuePortn = _Pm10010mpMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 48, 1, 2),
    _Pm10010mpMonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm10010mpMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mpMonupRmonPacketsCounterClientInputErrorPortn = _Pm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 48, 1, 3),
    _Pm10010mpMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm10010mpMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn = _Pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 48, 1, 4),
    _Pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mpMonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm10010mpMonupRmonBroadcastCounterClientInputTable = _Pm10010mpMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm10010mpMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm10010mpMonupRmonBroadcastCounterClientInputEntry = _Pm10010mpMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 64, 1)
)
pm10010mpMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm10010mpMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mpMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mpMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm10010mpMonupRmonBroadcastCounterClientInputIndex = _Pm10010mpMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 64, 1, 1),
    _Pm10010mpMonupRmonBroadcastCounterClientInputIndex_Type()
)
pm10010mpMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mpMonupRmonBroadcastCounterClientInputValuePortn = _Pm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 64, 1, 2),
    _Pm10010mpMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm10010mpMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn = _Pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 64, 1, 3),
    _Pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn = _Pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 64, 1, 4),
    _Pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mpMonupRmonMulticastCounterClientInputTable_Object = MibTable
pm10010mpMonupRmonMulticastCounterClientInputTable = _Pm10010mpMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm10010mpMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm10010mpMonupRmonMulticastCounterClientInputEntry = _Pm10010mpMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 80, 1)
)
pm10010mpMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm10010mpMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mpMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mpMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm10010mpMonupRmonMulticastCounterClientInputIndex = _Pm10010mpMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 80, 1, 1),
    _Pm10010mpMonupRmonMulticastCounterClientInputIndex_Type()
)
pm10010mpMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm10010mpMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm10010mpMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm10010mpMonupRmonMulticastCounterClientInputValuePortn = _Pm10010mpMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 80, 1, 2),
    _Pm10010mpMonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm10010mpMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mpMonupRmonMulticastCounterClientInputErrorPortn = _Pm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 80, 1, 3),
    _Pm10010mpMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm10010mpMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn = _Pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 80, 1, 4),
    _Pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm10010mpMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm10010mpMonupRmonPauseFrameCounterClientInputTable = _Pm10010mpMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm10010mpMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm10010mpMonupRmonPauseFrameCounterClientInputEntry = _Pm10010mpMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 96, 1)
)
pm10010mpMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm10010mp-MIB", "pm10010mpMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm10010mpMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm10010mpMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm10010mpMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm10010mpMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm10010mpMonupRmonPauseFrameCounterClientInputIndex = _Pm10010mpMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 96, 1, 1),
    _Pm10010mpMonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm10010mpMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn = _Pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 96, 1, 2),
    _Pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn = _Pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 96, 1, 3),
    _Pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 58, 11, 2, 4, 96, 1, 4),
    _Pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pm10010mpLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 30)
)
pm10010mpLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapLineNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010mpLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 31)
)
pm10010mpLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapLineNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010mpLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 32)
)
pm10010mpLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapLineNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mpLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 33)
)
pm10010mpLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapLineNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010mpLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 34)
)
pm10010mpLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineFailPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapLineNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpLineTrapCritGoesOn.setStatus(
        "current"
    )

pm10010mpLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 35)
)
pm10010mpLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineFailPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmLineHwFailPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapLineNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpLineTrapCritGoesOff.setStatus(
        "current"
    )

pm10010mpClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 40)
)
pm10010mpClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapPortNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm10010mpClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 41)
)
pm10010mpClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapPortNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm10010mpClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 42)
)
pm10010mpClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapPortNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mpClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 43)
)
pm10010mpClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapPortNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm10010mpClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 44)
)
pm10010mpClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmFailAccPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapPortNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpClientTrapCritGoesOn.setStatus(
        "current"
    )

pm10010mpClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 45)
)
pm10010mpClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmFailAccPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmHwFailAccPortn"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapPortNumber"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpClientTrapCritGoesOff.setStatus(
        "current"
    )

pm10010mpPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 50)
)
pm10010mpPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmDefFuseB"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmDefFuseA"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm10010mpPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 58, 10, 51)
)
pm10010mpPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmDefFuseB"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mpAlmDefFuseA"),
        ("EKINOPS-Pm10010mp-MIB", "pm10010mptrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm10010mpPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm10010mp-MIB",
    **{"Pm10010mpMultiRate": Pm10010mpMultiRate,
       "Pm10010mpOtxMode": Pm10010mpOtxMode,
       "Pm10010mpOtxGrid": Pm10010mpOtxGrid,
       "Pm10010mpAdjustValue": Pm10010mpAdjustValue,
       "Pm10010mpClientProtocol": Pm10010mpClientProtocol,
       "Pm10010mpProtocolMode": Pm10010mpProtocolMode,
       "Pm10010mpOtxChannel": Pm10010mpOtxChannel,
       "Pm10010mpOrxChannel": Pm10010mpOrxChannel,
       "modulePm10010mp": modulePm10010mp,
       "pm10010mpalarms": pm10010mpalarms,
       "pm10010mpAlmOther": pm10010mpAlmOther,
       "pm10010mpAlmOtherNurg": pm10010mpAlmOtherNurg,
       "pm10010mpAlmsynthAlm2": pm10010mpAlmsynthAlm2,
       "pm10010mpAlmConfTableSave": pm10010mpAlmConfTableSave,
       "pm10010mpAlmInvUpload": pm10010mpAlmInvUpload,
       "pm10010mpAlmConfTableLoad": pm10010mpAlmConfTableLoad,
       "pm10010mpAlmCorrelatOff": pm10010mpAlmCorrelatOff,
       "pm10010mpAlmMaintenanceOn": pm10010mpAlmMaintenanceOn,
       "pm10010mpAlmOtherUrg": pm10010mpAlmOtherUrg,
       "pm10010mpAlmOtherCrit": pm10010mpAlmOtherCrit,
       "pm10010mpAlmsynthAlm0": pm10010mpAlmsynthAlm0,
       "pm10010mpAlmFailFan": pm10010mpAlmFailFan,
       "pm10010mpAlmModGlobFail": pm10010mpAlmModGlobFail,
       "pm10010mpAlmDefFuseA": pm10010mpAlmDefFuseA,
       "pm10010mpAlmDefFuseB": pm10010mpAlmDefFuseB,
       "pm10010mpAlmclientModuleState": pm10010mpAlmclientModuleState,
       "pm10010mpAlmCfpInitialize": pm10010mpAlmCfpInitialize,
       "pm10010mpAlmCfpLowPower": pm10010mpAlmCfpLowPower,
       "pm10010mpAlmCfpHighPowerUp": pm10010mpAlmCfpHighPowerUp,
       "pm10010mpAlmCfpTxOff": pm10010mpAlmCfpTxOff,
       "pm10010mpAlmCfpTxTurnOn": pm10010mpAlmCfpTxTurnOn,
       "pm10010mpAlmCfpReady": pm10010mpAlmCfpReady,
       "pm10010mpAlmCfpFault": pm10010mpAlmCfpFault,
       "pm10010mpAlmCfpTxTurnOff": pm10010mpAlmCfpTxTurnOff,
       "pm10010mpAlmCfpHighPowerDown": pm10010mpAlmCfpHighPowerDown,
       "pm10010mpAlmclientModuleGeneralStatus": pm10010mpAlmclientModuleGeneralStatus,
       "pm10010mpAlmCfpOutOfAlignment": pm10010mpAlmCfpOutOfAlignment,
       "pm10010mpAlmCfpRxNetworkLol": pm10010mpAlmCfpRxNetworkLol,
       "pm10010mpAlmCfpRxLos": pm10010mpAlmCfpRxLos,
       "pm10010mpAlmCfpTxHostLol": pm10010mpAlmCfpTxHostLol,
       "pm10010mpAlmCfpTxLosf": pm10010mpAlmCfpTxLosf,
       "pm10010mpAlmCfpTxCmuLol": pm10010mpAlmCfpTxCmuLol,
       "pm10010mpAlmCfpTxJitterPllLol": pm10010mpAlmCfpTxJitterPllLol,
       "pm10010mpAlmCfpLossOfRefclk": pm10010mpAlmCfpLossOfRefclk,
       "pm10010mpAlmCfpHwInterlock": pm10010mpAlmCfpHwInterlock,
       "pm10010mpAlmclientGlobalAlarmSummary": pm10010mpAlmclientGlobalAlarmSummary,
       "pm10010mpAlmCfpSoftGlobAlarmTest": pm10010mpAlmCfpSoftGlobAlarmTest,
       "pm10010mpAlmCfpNetworkLaneAlarmWarning2": pm10010mpAlmCfpNetworkLaneAlarmWarning2,
       "pm10010mpAlmCfpModuleState": pm10010mpAlmCfpModuleState,
       "pm10010mpAlmCfpModuleGeneralStatus": pm10010mpAlmCfpModuleGeneralStatus,
       "pm10010mpAlmCfpModuleFault": pm10010mpAlmCfpModuleFault,
       "pm10010mpAlmCfpModuleAlarmWarning1": pm10010mpAlmCfpModuleAlarmWarning1,
       "pm10010mpAlmCfpModuleAlarmWarning2": pm10010mpAlmCfpModuleAlarmWarning2,
       "pm10010mpAlmCfpNetworkLaneAlarmWarning1": pm10010mpAlmCfpNetworkLaneAlarmWarning1,
       "pm10010mpAlmCfpNetworkLaneFaultStatus": pm10010mpAlmCfpNetworkLaneFaultStatus,
       "pm10010mpAlmCfpHostLaneFaultStatus": pm10010mpAlmCfpHostLaneFaultStatus,
       "pm10010mpAlmCfpGlobAlarmAssertion": pm10010mpAlmCfpGlobAlarmAssertion,
       "pm10010mpAlmmsaModuleState": pm10010mpAlmmsaModuleState,
       "pm10010mpAlmMsaInitialize": pm10010mpAlmMsaInitialize,
       "pm10010mpAlmMsaLowPower": pm10010mpAlmMsaLowPower,
       "pm10010mpAlmMsaHighPowerUp": pm10010mpAlmMsaHighPowerUp,
       "pm10010mpAlmMsaTxOff": pm10010mpAlmMsaTxOff,
       "pm10010mpAlmMsaTxTurnOn": pm10010mpAlmMsaTxTurnOn,
       "pm10010mpAlmMsaReady": pm10010mpAlmMsaReady,
       "pm10010mpAlmMsaFault": pm10010mpAlmMsaFault,
       "pm10010mpAlmMsaTxTurnOff": pm10010mpAlmMsaTxTurnOff,
       "pm10010mpAlmMsaHighPowerDown": pm10010mpAlmMsaHighPowerDown,
       "pm10010mpAlmmsaModuleGeneralStatus": pm10010mpAlmmsaModuleGeneralStatus,
       "pm10010mpAlmMsaOutOfAlignment": pm10010mpAlmMsaOutOfAlignment,
       "pm10010mpAlmMsaRxNetworkLol": pm10010mpAlmMsaRxNetworkLol,
       "pm10010mpAlmMsaRxLos": pm10010mpAlmMsaRxLos,
       "pm10010mpAlmMsaTxHostLol": pm10010mpAlmMsaTxHostLol,
       "pm10010mpAlmMsaTxLosf": pm10010mpAlmMsaTxLosf,
       "pm10010mpAlmMsaTxCmuLol": pm10010mpAlmMsaTxCmuLol,
       "pm10010mpAlmMsaTxJitterPllLol": pm10010mpAlmMsaTxJitterPllLol,
       "pm10010mpAlmMsaLossOfRefclk": pm10010mpAlmMsaLossOfRefclk,
       "pm10010mpAlmMsaHwInterlock": pm10010mpAlmMsaHwInterlock,
       "pm10010mpAlmmsaGlobalAlarmSummary": pm10010mpAlmmsaGlobalAlarmSummary,
       "pm10010mpAlmMsaSoftGlobAlarmTest": pm10010mpAlmMsaSoftGlobAlarmTest,
       "pm10010mpAlmMsaNetworkHostAlarmStatus": pm10010mpAlmMsaNetworkHostAlarmStatus,
       "pm10010mpAlmMsaNetworkLaneAlarmWarning2": pm10010mpAlmMsaNetworkLaneAlarmWarning2,
       "pm10010mpAlmMsaModuleState": pm10010mpAlmMsaModuleState,
       "pm10010mpAlmMsaModuleGeneralStatus": pm10010mpAlmMsaModuleGeneralStatus,
       "pm10010mpAlmModuleFault": pm10010mpAlmModuleFault,
       "pm10010mpAlmMsaModuleAlarmWarning1": pm10010mpAlmMsaModuleAlarmWarning1,
       "pm10010mpAlmMsaModuleAlarmWarning2": pm10010mpAlmMsaModuleAlarmWarning2,
       "pm10010mpAlmMsaNetworkLaneAlarmWarning1": pm10010mpAlmMsaNetworkLaneAlarmWarning1,
       "pm10010mpAlmMsaNetworkLaneFaultStatus": pm10010mpAlmMsaNetworkLaneFaultStatus,
       "pm10010mpAlmMsaHostLaneFaultStatus": pm10010mpAlmMsaHostLaneFaultStatus,
       "pm10010mpAlmMsaGlobAlarmAssertion": pm10010mpAlmMsaGlobAlarmAssertion,
       "pm10010mpAlmmsaNetworkTxAlignment": pm10010mpAlmmsaNetworkTxAlignment,
       "pm10010mpAlmNetTxTimingFault": pm10010mpAlmNetTxTimingFault,
       "pm10010mpAlmNetTxReferenceClockFault": pm10010mpAlmNetTxReferenceClockFault,
       "pm10010mpAlmNetTxCmuLockFault": pm10010mpAlmNetTxCmuLockFault,
       "pm10010mpAlmNetTxOutOfAlignment": pm10010mpAlmNetTxOutOfAlignment,
       "pm10010mpAlmNetTxLossOfAlignment": pm10010mpAlmNetTxLossOfAlignment,
       "pm10010mpAlmmsaNetworkRxAlignment": pm10010mpAlmmsaNetworkRxAlignment,
       "pm10010mpAlmNetRxTimingFault": pm10010mpAlmNetRxTimingFault,
       "pm10010mpAlmNetRxOutOfAlignment": pm10010mpAlmNetRxOutOfAlignment,
       "pm10010mpAlmNetRxLossOfAlignment": pm10010mpAlmNetRxLossOfAlignment,
       "pm10010mpAlmNetRxModemLockFault": pm10010mpAlmNetRxModemLockFault,
       "pm10010mpAlmNetRxModemSyncDetectFault": pm10010mpAlmNetRxModemSyncDetectFault,
       "pm10010mpAlmmsaNetworkHostNetworkAlarmSummary": pm10010mpAlmmsaNetworkHostNetworkAlarmSummary,
       "pm10010mpAlmNetworkTxAlignment": pm10010mpAlmNetworkTxAlignment,
       "pm10010mpAlmNetworkRxAlignment": pm10010mpAlmNetworkRxAlignment,
       "pm10010mpAlmNetworkRxOtn": pm10010mpAlmNetworkRxOtn,
       "pm10010mpAlmHostRxAlignment": pm10010mpAlmHostRxAlignment,
       "pm10010mpAlmHostTxAlignment": pm10010mpAlmHostTxAlignment,
       "pm10010mpAlmHostTxOtnStatus": pm10010mpAlmHostTxOtnStatus,
       "pm10010mpAlmmsaHostTxAlignment": pm10010mpAlmmsaHostTxAlignment,
       "pm10010mpAlmHostTxDeskewLockFault": pm10010mpAlmHostTxDeskewLockFault,
       "pm10010mpAlmHostTxOutOfAlignment": pm10010mpAlmHostTxOutOfAlignment,
       "pm10010mpAlmHostTxLossOfAlignment": pm10010mpAlmHostTxLossOfAlignment,
       "pm10010mpAlmHostTxCdrLockFault": pm10010mpAlmHostTxCdrLockFault,
       "pm10010mpAlmmsaHostRxAlignment": pm10010mpAlmmsaHostRxAlignment,
       "pm10010mpAlmHostRxCmuLockFault": pm10010mpAlmHostRxCmuLockFault,
       "pm10010mpAlmHostRxOutOfAlignment": pm10010mpAlmHostRxOutOfAlignment,
       "pm10010mpAlmHostRxLossOfAlignment": pm10010mpAlmHostRxLossOfAlignment,
       "pm10010mpAlmClient": pm10010mpAlmClient,
       "pm10010mpAlmClientNurg": pm10010mpAlmClientNurg,
       "pm10010mpAlmclientNetworkLaneAlarmWarningTable": pm10010mpAlmclientNetworkLaneAlarmWarningTable,
       "pm10010mpAlmclientNetworkLaneAlarmWarningEntry": pm10010mpAlmclientNetworkLaneAlarmWarningEntry,
       "pm10010mpAlmclientNetworkLaneAlarmWarningIndex": pm10010mpAlmclientNetworkLaneAlarmWarningIndex,
       "pm10010mpAlmClientRxPowerLowAlarmPortn": pm10010mpAlmClientRxPowerLowAlarmPortn,
       "pm10010mpAlmClientRxPowerLowWarningPortn": pm10010mpAlmClientRxPowerLowWarningPortn,
       "pm10010mpAlmClientRxPowerHighWarningPortn": pm10010mpAlmClientRxPowerHighWarningPortn,
       "pm10010mpAlmClientRxPowerHighAlarmPortn": pm10010mpAlmClientRxPowerHighAlarmPortn,
       "pm10010mpAlmLaserTempLowAlarmPortn": pm10010mpAlmLaserTempLowAlarmPortn,
       "pm10010mpAlmClientLaserTempLowWarningPortn": pm10010mpAlmClientLaserTempLowWarningPortn,
       "pm10010mpAlmClientLaserTempHighWarningPortn": pm10010mpAlmClientLaserTempHighWarningPortn,
       "pm10010mpAlmClientLaserTempHighAlarmPortn": pm10010mpAlmClientLaserTempHighAlarmPortn,
       "pm10010mpAlmClientTxPowerLowAlarmPortn": pm10010mpAlmClientTxPowerLowAlarmPortn,
       "pm10010mpAlmClientTxPowerLowWarningPortn": pm10010mpAlmClientTxPowerLowWarningPortn,
       "pm10010mpAlmClientTxPowerHighWarningPortn": pm10010mpAlmClientTxPowerHighWarningPortn,
       "pm10010mpAlmClientTxPowerHighAlarmPortn": pm10010mpAlmClientTxPowerHighAlarmPortn,
       "pm10010mpAlmClientBiasLowAlarmPortn": pm10010mpAlmClientBiasLowAlarmPortn,
       "pm10010mpAlmClientBiasLowWarningPortn": pm10010mpAlmClientBiasLowWarningPortn,
       "pm10010mpAlmClientBiasHighWarningPortn": pm10010mpAlmClientBiasHighWarningPortn,
       "pm10010mpAlmClientBiasHighAlarmPortn": pm10010mpAlmClientBiasHighAlarmPortn,
       "pm10010mpAlmclientSfpWarnDdmTable": pm10010mpAlmclientSfpWarnDdmTable,
       "pm10010mpAlmclientSfpWarnDdmEntry": pm10010mpAlmclientSfpWarnDdmEntry,
       "pm10010mpAlmclientSfpWarnDdmIndex": pm10010mpAlmclientSfpWarnDdmIndex,
       "pm10010mpAlmTxPwLowWngPortn": pm10010mpAlmTxPwLowWngPortn,
       "pm10010mpAlmTxPwrHighWngPortn": pm10010mpAlmTxPwrHighWngPortn,
       "pm10010mpAlmTxBiasLowWngPortn": pm10010mpAlmTxBiasLowWngPortn,
       "pm10010mpAlmTxBiasHighWngPortn": pm10010mpAlmTxBiasHighWngPortn,
       "pm10010mpAlmVccLowWngPortn": pm10010mpAlmVccLowWngPortn,
       "pm10010mpAlmVccHighWngPortn": pm10010mpAlmVccHighWngPortn,
       "pm10010mpAlmTempLowWngPortn": pm10010mpAlmTempLowWngPortn,
       "pm10010mpAlmTempHighWngPortn": pm10010mpAlmTempHighWngPortn,
       "pm10010mpAlmRxPwrLowWngPortn": pm10010mpAlmRxPwrLowWngPortn,
       "pm10010mpAlmRxPwrHighWngPortn": pm10010mpAlmRxPwrHighWngPortn,
       "pm10010mpAlmClientUrg": pm10010mpAlmClientUrg,
       "pm10010mpAlmclientNetworkLaneFaultTable": pm10010mpAlmclientNetworkLaneFaultTable,
       "pm10010mpAlmclientNetworkLaneFaultEntry": pm10010mpAlmclientNetworkLaneFaultEntry,
       "pm10010mpAlmclientNetworkLaneFaultIndex": pm10010mpAlmclientNetworkLaneFaultIndex,
       "pm10010mpAlmClientLaneRxFifoErrorPortn": pm10010mpAlmClientLaneRxFifoErrorPortn,
       "pm10010mpAlmClientLaneRxLolPortn": pm10010mpAlmClientLaneRxLolPortn,
       "pm10010mpAlmClientLaneRxLosPortn": pm10010mpAlmClientLaneRxLosPortn,
       "pm10010mpAlmClientLaneTxLolPortn": pm10010mpAlmClientLaneTxLolPortn,
       "pm10010mpAlmClientLaneTxLosfPortn": pm10010mpAlmClientLaneTxLosfPortn,
       "pm10010mpAlmClientLaneApdPowerSupplyPortn": pm10010mpAlmClientLaneApdPowerSupplyPortn,
       "pm10010mpAlmClientLaneWavelengthUnlockedPortn": pm10010mpAlmClientLaneWavelengthUnlockedPortn,
       "pm10010mpAlmClientLaneTecFaultPortn": pm10010mpAlmClientLaneTecFaultPortn,
       "pm10010mpAlmclientHostLaneFaultTable": pm10010mpAlmclientHostLaneFaultTable,
       "pm10010mpAlmclientHostLaneFaultEntry": pm10010mpAlmclientHostLaneFaultEntry,
       "pm10010mpAlmclientHostLaneFaultIndex": pm10010mpAlmclientHostLaneFaultIndex,
       "pm10010mpAlmClientLossOfSyncPortn": pm10010mpAlmClientLossOfSyncPortn,
       "pm10010mpAlmClientInputLossOfSigPortn": pm10010mpAlmClientInputLossOfSigPortn,
       "pm10010mpAlmClientLanesMarkerUnlockPortn": pm10010mpAlmClientLanesMarkerUnlockPortn,
       "pm10010mpAlmClientLanes6466UnlockPortn": pm10010mpAlmClientLanes6466UnlockPortn,
       "pm10010mpAlmClientLanesNotAlignedPortn": pm10010mpAlmClientLanesNotAlignedPortn,
       "pm10010mpAlmClientCsfDetectedPortn": pm10010mpAlmClientCsfDetectedPortn,
       "pm10010mpAlmClientTxHostLolPortn": pm10010mpAlmClientTxHostLolPortn,
       "pm10010mpAlmClientLaneTxFifoErrorPortn": pm10010mpAlmClientLaneTxFifoErrorPortn,
       "pm10010mpAlmclientSfpAlmDdmTable": pm10010mpAlmclientSfpAlmDdmTable,
       "pm10010mpAlmclientSfpAlmDdmEntry": pm10010mpAlmclientSfpAlmDdmEntry,
       "pm10010mpAlmclientSfpAlmDdmIndex": pm10010mpAlmclientSfpAlmDdmIndex,
       "pm10010mpAlmTxPwrLowAlaPortn": pm10010mpAlmTxPwrLowAlaPortn,
       "pm10010mpAlmTxPwrHighAlaPortn": pm10010mpAlmTxPwrHighAlaPortn,
       "pm10010mpAlmTxBiasLowAlaPortn": pm10010mpAlmTxBiasLowAlaPortn,
       "pm10010mpAlmTxBiasHighAlaPortn": pm10010mpAlmTxBiasHighAlaPortn,
       "pm10010mpAlmVccLowAlaPortn": pm10010mpAlmVccLowAlaPortn,
       "pm10010mpAlmVccHighAlaPortn": pm10010mpAlmVccHighAlaPortn,
       "pm10010mpAlmTempLowAlaPortn": pm10010mpAlmTempLowAlaPortn,
       "pm10010mpAlmTempHighAlaPortn": pm10010mpAlmTempHighAlaPortn,
       "pm10010mpAlmRxPwrLowAlaPortn": pm10010mpAlmRxPwrLowAlaPortn,
       "pm10010mpAlmRxPwrHighAlaPortn": pm10010mpAlmRxPwrHighAlaPortn,
       "pm10010mpAlmClientCrit": pm10010mpAlmClientCrit,
       "pm10010mpAlmsynthAlmPortTable": pm10010mpAlmsynthAlmPortTable,
       "pm10010mpAlmsynthAlmPortEntry": pm10010mpAlmsynthAlmPortEntry,
       "pm10010mpAlmsynthAlmPortIndex": pm10010mpAlmsynthAlmPortIndex,
       "pm10010mpAlmSfpAbsentPortn": pm10010mpAlmSfpAbsentPortn,
       "pm10010mpAlmDdmAbsentPortn": pm10010mpAlmDdmAbsentPortn,
       "pm10010mpAlmHwFailAccPortn": pm10010mpAlmHwFailAccPortn,
       "pm10010mpAlmDwLsdPortn": pm10010mpAlmDwLsdPortn,
       "pm10010mpAlmClientLocalOosPortn": pm10010mpAlmClientLocalOosPortn,
       "pm10010mpAlmClientRemoteOosPortn": pm10010mpAlmClientRemoteOosPortn,
       "pm10010mpAlmDwCaisPortn": pm10010mpAlmDwCaisPortn,
       "pm10010mpAlmSfpDdmWarningPortn": pm10010mpAlmSfpDdmWarningPortn,
       "pm10010mpAlmSfpDdmAlmPortn": pm10010mpAlmSfpDdmAlmPortn,
       "pm10010mpAlmFailAccPortn": pm10010mpAlmFailAccPortn,
       "pm10010mpAlmUpCsfPortn": pm10010mpAlmUpCsfPortn,
       "pm10010mpAlmLine": pm10010mpAlmLine,
       "pm10010mpAlmLineNurg": pm10010mpAlmLineNurg,
       "pm10010mpAlmlineNetworkLaneAlarmWarning1Table": pm10010mpAlmlineNetworkLaneAlarmWarning1Table,
       "pm10010mpAlmlineNetworkLaneAlarmWarning1Entry": pm10010mpAlmlineNetworkLaneAlarmWarning1Entry,
       "pm10010mpAlmlineNetworkLaneAlarmWarning1Index": pm10010mpAlmlineNetworkLaneAlarmWarning1Index,
       "pm10010mpAlmLineRxPowerLowAlarmPortn": pm10010mpAlmLineRxPowerLowAlarmPortn,
       "pm10010mpAlmLineRxPowerLowWarningPortn": pm10010mpAlmLineRxPowerLowWarningPortn,
       "pm10010mpAlmLineRxPowerHighWarningPortn": pm10010mpAlmLineRxPowerHighWarningPortn,
       "pm10010mpAlmLineRxPowerHighAlarmPortn": pm10010mpAlmLineRxPowerHighAlarmPortn,
       "pm10010mpAlmLineLaserTempLowAlarmPortn": pm10010mpAlmLineLaserTempLowAlarmPortn,
       "pm10010mpAlmLineLaserTempLowWarningPortn": pm10010mpAlmLineLaserTempLowWarningPortn,
       "pm10010mpAlmLineLaserTempHighWarningPortn": pm10010mpAlmLineLaserTempHighWarningPortn,
       "pm10010mpAlmLineLaserTempHighAlarmPortn": pm10010mpAlmLineLaserTempHighAlarmPortn,
       "pm10010mpAlmLineTxPowerLowAlarmPortn": pm10010mpAlmLineTxPowerLowAlarmPortn,
       "pm10010mpAlmLineTxPowerLowWarningPortn": pm10010mpAlmLineTxPowerLowWarningPortn,
       "pm10010mpAlmLineTxPowerHighWarningPortn": pm10010mpAlmLineTxPowerHighWarningPortn,
       "pm10010mpAlmLineTxPowerHighAlarmPortn": pm10010mpAlmLineTxPowerHighAlarmPortn,
       "pm10010mpAlmLineBiasLowAlarmPortn": pm10010mpAlmLineBiasLowAlarmPortn,
       "pm10010mpAlmLineBiasLowWarningPortn": pm10010mpAlmLineBiasLowWarningPortn,
       "pm10010mpAlmLineBiasHighWarningPortn": pm10010mpAlmLineBiasHighWarningPortn,
       "pm10010mpAlmLineBiasHighAlarmPortn": pm10010mpAlmLineBiasHighAlarmPortn,
       "pm10010mpAlmlineNetworkLaneAlarmWarning2Table": pm10010mpAlmlineNetworkLaneAlarmWarning2Table,
       "pm10010mpAlmlineNetworkLaneAlarmWarning2Entry": pm10010mpAlmlineNetworkLaneAlarmWarning2Entry,
       "pm10010mpAlmlineNetworkLaneAlarmWarning2Index": pm10010mpAlmlineNetworkLaneAlarmWarning2Index,
       "pm10010mpAlmTxModulatorBiasLowAlarmPortn": pm10010mpAlmTxModulatorBiasLowAlarmPortn,
       "pm10010mpAlmTxModulatorBiasLowWarningPortn": pm10010mpAlmTxModulatorBiasLowWarningPortn,
       "pm10010mpAlmTxModulatorBiasHighWarningPortn": pm10010mpAlmTxModulatorBiasHighWarningPortn,
       "pm10010mpAlmTxModulatorBiasHighAlarmPortn": pm10010mpAlmTxModulatorBiasHighAlarmPortn,
       "pm10010mpAlmRxLaserTempLowAlarmPortn": pm10010mpAlmRxLaserTempLowAlarmPortn,
       "pm10010mpAlmRxLaserTempLowWarningPortn": pm10010mpAlmRxLaserTempLowWarningPortn,
       "pm10010mpAlmRxLaserTempHighWarningPortn": pm10010mpAlmRxLaserTempHighWarningPortn,
       "pm10010mpAlmRxLaserTempHighAlarmPortn": pm10010mpAlmRxLaserTempHighAlarmPortn,
       "pm10010mpAlmRxLaserOutputLowAlarmPortn": pm10010mpAlmRxLaserOutputLowAlarmPortn,
       "pm10010mpAlmRxLaserOutputLowWarningPortn": pm10010mpAlmRxLaserOutputLowWarningPortn,
       "pm10010mpAlmRxLaserOutputHighWarningPortn": pm10010mpAlmRxLaserOutputHighWarningPortn,
       "pm10010mpAlmRxLaserOutputHighAlarmPortn": pm10010mpAlmRxLaserOutputHighAlarmPortn,
       "pm10010mpAlmRxLaserBiasLowAlarmPortn": pm10010mpAlmRxLaserBiasLowAlarmPortn,
       "pm10010mpAlmRxLaserBiasLowWarningPortn": pm10010mpAlmRxLaserBiasLowWarningPortn,
       "pm10010mpAlmRxLaserBiasHighWarningPortn": pm10010mpAlmRxLaserBiasHighWarningPortn,
       "pm10010mpAlmRxLaserBiasHighAlarmPortn": pm10010mpAlmRxLaserBiasHighAlarmPortn,
       "pm10010mpAlmLineUrg": pm10010mpAlmLineUrg,
       "pm10010mpAlmlineNetworkLaneFaultTable": pm10010mpAlmlineNetworkLaneFaultTable,
       "pm10010mpAlmlineNetworkLaneFaultEntry": pm10010mpAlmlineNetworkLaneFaultEntry,
       "pm10010mpAlmlineNetworkLaneFaultIndex": pm10010mpAlmlineNetworkLaneFaultIndex,
       "pm10010mpAlmLineLaneRxTecFaultPortn": pm10010mpAlmLineLaneRxTecFaultPortn,
       "pm10010mpAlmLineLaneRxFifoErrorPortn": pm10010mpAlmLineLaneRxFifoErrorPortn,
       "pm10010mpAlmLineLaneRxLolPortn": pm10010mpAlmLineLaneRxLolPortn,
       "pm10010mpAlmLineLaneRxLosPortn": pm10010mpAlmLineLaneRxLosPortn,
       "pm10010mpAlmLineLaneTxLolPortn": pm10010mpAlmLineLaneTxLolPortn,
       "pm10010mpAlmLineLaneTxLosfPortn": pm10010mpAlmLineLaneTxLosfPortn,
       "pm10010mpAlmLineLaneApdPowerSupplyPortn": pm10010mpAlmLineLaneApdPowerSupplyPortn,
       "pm10010mpAlmLineLaneWavelengthUnlockedPortn": pm10010mpAlmLineLaneWavelengthUnlockedPortn,
       "pm10010mpAlmLineLaneTecFaultPortn": pm10010mpAlmLineLaneTecFaultPortn,
       "pm10010mpAlmlineHostLaneFaultTable": pm10010mpAlmlineHostLaneFaultTable,
       "pm10010mpAlmlineHostLaneFaultEntry": pm10010mpAlmlineHostLaneFaultEntry,
       "pm10010mpAlmlineHostLaneFaultIndex": pm10010mpAlmlineHostLaneFaultIndex,
       "pm10010mpAlmLineInputLossOfSignalPortn": pm10010mpAlmLineInputLossOfSignalPortn,
       "pm10010mpAlmLineLossOfFramePortn": pm10010mpAlmLineLossOfFramePortn,
       "pm10010mpAlmLineSmBdiInsertedPortn": pm10010mpAlmLineSmBdiInsertedPortn,
       "pm10010mpAlmLineSmBdiDetectedPortn": pm10010mpAlmLineSmBdiDetectedPortn,
       "pm10010mpAlmLineSmIaeInsertedPortn": pm10010mpAlmLineSmIaeInsertedPortn,
       "pm10010mpAlmLineSmIaeDetectedPortn": pm10010mpAlmLineSmIaeDetectedPortn,
       "pm10010mpAlmLineTxHostLolPortn": pm10010mpAlmLineTxHostLolPortn,
       "pm10010mpAlmLineLaneTxFifoErrorPortn": pm10010mpAlmLineLaneTxFifoErrorPortn,
       "pm10010mpAlmlineNetworkLaneRxOtnTable": pm10010mpAlmlineNetworkLaneRxOtnTable,
       "pm10010mpAlmlineNetworkLaneRxOtnEntry": pm10010mpAlmlineNetworkLaneRxOtnEntry,
       "pm10010mpAlmlineNetworkLaneRxOtnIndex": pm10010mpAlmlineNetworkLaneRxOtnIndex,
       "pm10010mpAlmLineRxOtnOduAisPortn": pm10010mpAlmLineRxOtnOduAisPortn,
       "pm10010mpAlmLineRxOtnOtuAisPortn": pm10010mpAlmLineRxOtnOtuAisPortn,
       "pm10010mpAlmLineRxSmBdiPortn": pm10010mpAlmLineRxSmBdiPortn,
       "pm10010mpAlmLineRxOtnIaePortn": pm10010mpAlmLineRxOtnIaePortn,
       "pm10010mpAlmLineRxOtnOomPortn": pm10010mpAlmLineRxOtnOomPortn,
       "pm10010mpAlmLineRxOtnLomPortn": pm10010mpAlmLineRxOtnLomPortn,
       "pm10010mpAlmLineRxOtnOofPortn": pm10010mpAlmLineRxOtnOofPortn,
       "pm10010mpAlmLineRxOtnLofPortn": pm10010mpAlmLineRxOtnLofPortn,
       "pm10010mpAlmlineHostLaneTxOtnTable": pm10010mpAlmlineHostLaneTxOtnTable,
       "pm10010mpAlmlineHostLaneTxOtnEntry": pm10010mpAlmlineHostLaneTxOtnEntry,
       "pm10010mpAlmlineHostLaneTxOtnIndex": pm10010mpAlmlineHostLaneTxOtnIndex,
       "pm10010mpAlmLineTxOtnOduAisPortn": pm10010mpAlmLineTxOtnOduAisPortn,
       "pm10010mpAlmLineTxOtnOtuAisPortn": pm10010mpAlmLineTxOtnOtuAisPortn,
       "pm10010mpAlmLineTxSmBdiPortn": pm10010mpAlmLineTxSmBdiPortn,
       "pm10010mpAlmLineTxOtnIaePortn": pm10010mpAlmLineTxOtnIaePortn,
       "pm10010mpAlmLineTxOtnOomPortn": pm10010mpAlmLineTxOtnOomPortn,
       "pm10010mpAlmLineTxOtnLomPortn": pm10010mpAlmLineTxOtnLomPortn,
       "pm10010mpAlmLineTxOtnOofPortn": pm10010mpAlmLineTxOtnOofPortn,
       "pm10010mpAlmLineTxOtnLofPortn": pm10010mpAlmLineTxOtnLofPortn,
       "pm10010mpAlmLineCrit": pm10010mpAlmLineCrit,
       "pm10010mpAlmsynthAlmLineTable": pm10010mpAlmsynthAlmLineTable,
       "pm10010mpAlmsynthAlmLineEntry": pm10010mpAlmsynthAlmLineEntry,
       "pm10010mpAlmsynthAlmLineIndex": pm10010mpAlmsynthAlmLineIndex,
       "pm10010mpAlmXfpAbsentPortn": pm10010mpAlmXfpAbsentPortn,
       "pm10010mpAlmXfpInitNotComplPortn": pm10010mpAlmXfpInitNotComplPortn,
       "pm10010mpAlmLineHwFailPortn": pm10010mpAlmLineHwFailPortn,
       "pm10010mpAlmXfpTxOffPortn": pm10010mpAlmXfpTxOffPortn,
       "pm10010mpAlmLineLocalOosPortn": pm10010mpAlmLineLocalOosPortn,
       "pm10010mpAlmUpRdiInsPortn": pm10010mpAlmUpRdiInsPortn,
       "pm10010mpAlmLineDdmWarningPortn": pm10010mpAlmLineDdmWarningPortn,
       "pm10010mpAlmLineDdmAlmPortn": pm10010mpAlmLineDdmAlmPortn,
       "pm10010mpAlmLineFailPortn": pm10010mpAlmLineFailPortn,
       "pm10010mpAlmLineActivePortn": pm10010mpAlmLineActivePortn,
       "pm10010mpmeasures": pm10010mpmeasures,
       "pm10010mpMesrOther": pm10010mpMesrOther,
       "pm10010mpMesrsynth0": pm10010mpMesrsynth0,
       "pm10010mpMesrsynth1": pm10010mpMesrsynth1,
       "pm10010mpMesrpmIntervalNumber": pm10010mpMesrpmIntervalNumber,
       "pm10010mpMesrlineNetTxLaserOutputPwrAverage": pm10010mpMesrlineNetTxLaserOutputPwrAverage,
       "pm10010mpMesrlineNetTxLaserTempAverage": pm10010mpMesrlineNetTxLaserTempAverage,
       "pm10010mpMesrlineNetTxBiasCurrentAverage": pm10010mpMesrlineNetTxBiasCurrentAverage,
       "pm10010mpMesrlineNetRxInputPwrAverage": pm10010mpMesrlineNetRxInputPwrAverage,
       "pm10010mpMesrlineResidualChromaticDispAverage": pm10010mpMesrlineResidualChromaticDispAverage,
       "pm10010mpMesrlineDiffGroupDelayAverage": pm10010mpMesrlineDiffGroupDelayAverage,
       "pm10010mpMesrlineQFactorAverage": pm10010mpMesrlineQFactorAverage,
       "pm10010mpMesrlineCarrierFreqOffsetAverage": pm10010mpMesrlineCarrierFreqOffsetAverage,
       "pm10010mpMesrlineOsnrAverage": pm10010mpMesrlineOsnrAverage,
       "pm10010mpMesrclientNetTxTempMin": pm10010mpMesrclientNetTxTempMin,
       "pm10010mpMesrclientNetTxBiasMin": pm10010mpMesrclientNetTxBiasMin,
       "pm10010mpMesrclientNetTxPwrMin": pm10010mpMesrclientNetTxPwrMin,
       "pm10010mpMesrclientNetRxPwrMin": pm10010mpMesrclientNetRxPwrMin,
       "pm10010mpMesrlineNetTxLaserOutputPwrMin": pm10010mpMesrlineNetTxLaserOutputPwrMin,
       "pm10010mpMesrlineNetTxLaserTempMin": pm10010mpMesrlineNetTxLaserTempMin,
       "pm10010mpMesrlineNetTxBiasCurrentMin": pm10010mpMesrlineNetTxBiasCurrentMin,
       "pm10010mpMesrlineNetRxInputPwrMin": pm10010mpMesrlineNetRxInputPwrMin,
       "pm10010mpMesrlineResidualChromaticDispMin": pm10010mpMesrlineResidualChromaticDispMin,
       "pm10010mpMesrlineDiffGroupDelayMin": pm10010mpMesrlineDiffGroupDelayMin,
       "pm10010mpMesrlineQFactorMin": pm10010mpMesrlineQFactorMin,
       "pm10010mpMesrlineCarrierFreqOffsetMin": pm10010mpMesrlineCarrierFreqOffsetMin,
       "pm10010mpMesrlineOsnrMin": pm10010mpMesrlineOsnrMin,
       "pm10010mpMesrclientNetTxTempMax": pm10010mpMesrclientNetTxTempMax,
       "pm10010mpMesrclientNetTxBiasMax": pm10010mpMesrclientNetTxBiasMax,
       "pm10010mpMesrclientNetTxPwrMax": pm10010mpMesrclientNetTxPwrMax,
       "pm10010mpMesrclientNetRxPwrMax": pm10010mpMesrclientNetRxPwrMax,
       "pm10010mpMesrlineNetTxLaserOutputPwrMax": pm10010mpMesrlineNetTxLaserOutputPwrMax,
       "pm10010mpMesrlineNetTxLaserTempMax": pm10010mpMesrlineNetTxLaserTempMax,
       "pm10010mpMesrlineNetTxBiasCurrentMax": pm10010mpMesrlineNetTxBiasCurrentMax,
       "pm10010mpMesrlineNetRxInputPwrMax": pm10010mpMesrlineNetRxInputPwrMax,
       "pm10010mpMesrlineResidualChromaticDispMax": pm10010mpMesrlineResidualChromaticDispMax,
       "pm10010mpMesrlineDiffGroupDelayMax": pm10010mpMesrlineDiffGroupDelayMax,
       "pm10010mpMesrlineQFactorMax": pm10010mpMesrlineQFactorMax,
       "pm10010mpMesrlineCarrierFreqOffsetMax": pm10010mpMesrlineCarrierFreqOffsetMax,
       "pm10010mpMesrlineOsnrMax": pm10010mpMesrlineOsnrMax,
       "pm10010mpMesrClient": pm10010mpMesrClient,
       "pm10010mpMesrclientCfpTemp": pm10010mpMesrclientCfpTemp,
       "pm10010mpMesrclientCfp3v3Voltage": pm10010mpMesrclientCfp3v3Voltage,
       "pm10010mpMesrclientSoaBiasCurrent": pm10010mpMesrclientSoaBiasCurrent,
       "pm10010mpMesrclientNetTxTempTable": pm10010mpMesrclientNetTxTempTable,
       "pm10010mpMesrclientNetTxTempEntry": pm10010mpMesrclientNetTxTempEntry,
       "pm10010mpMesrclientNetTxTempIndex": pm10010mpMesrclientNetTxTempIndex,
       "pm10010mpMesrclientNetTxTempPortn": pm10010mpMesrclientNetTxTempPortn,
       "pm10010mpMesrclientNetTxBiasTable": pm10010mpMesrclientNetTxBiasTable,
       "pm10010mpMesrclientNetTxBiasEntry": pm10010mpMesrclientNetTxBiasEntry,
       "pm10010mpMesrclientNetTxBiasIndex": pm10010mpMesrclientNetTxBiasIndex,
       "pm10010mpMesrclientNetTxBiasPortn": pm10010mpMesrclientNetTxBiasPortn,
       "pm10010mpMesrclientNetTxPwrTable": pm10010mpMesrclientNetTxPwrTable,
       "pm10010mpMesrclientNetTxPwrEntry": pm10010mpMesrclientNetTxPwrEntry,
       "pm10010mpMesrclientNetTxPwrIndex": pm10010mpMesrclientNetTxPwrIndex,
       "pm10010mpMesrclientNetTxPwrPortn": pm10010mpMesrclientNetTxPwrPortn,
       "pm10010mpMesrclientNetRxPwrTable": pm10010mpMesrclientNetRxPwrTable,
       "pm10010mpMesrclientNetRxPwrEntry": pm10010mpMesrclientNetRxPwrEntry,
       "pm10010mpMesrclientNetRxPwrIndex": pm10010mpMesrclientNetRxPwrIndex,
       "pm10010mpMesrclientNetRxPwrPortn": pm10010mpMesrclientNetRxPwrPortn,
       "pm10010mpMesrLine": pm10010mpMesrLine,
       "pm10010mpMesrlineMsaTemp": pm10010mpMesrlineMsaTemp,
       "pm10010mpMesrlineMsa3v3Voltage": pm10010mpMesrlineMsa3v3Voltage,
       "pm10010mpMesrlineSoaBiasCurrent": pm10010mpMesrlineSoaBiasCurrent,
       "pm10010mpMesrlineNetTxLaserOutputPwrTable": pm10010mpMesrlineNetTxLaserOutputPwrTable,
       "pm10010mpMesrlineNetTxLaserOutputPwrEntry": pm10010mpMesrlineNetTxLaserOutputPwrEntry,
       "pm10010mpMesrlineNetTxLaserOutputPwrIndex": pm10010mpMesrlineNetTxLaserOutputPwrIndex,
       "pm10010mpMesrlineNetTxLaserOutputPwrPortn": pm10010mpMesrlineNetTxLaserOutputPwrPortn,
       "pm10010mpMesrlineNetTxLaserTempTable": pm10010mpMesrlineNetTxLaserTempTable,
       "pm10010mpMesrlineNetTxLaserTempEntry": pm10010mpMesrlineNetTxLaserTempEntry,
       "pm10010mpMesrlineNetTxLaserTempIndex": pm10010mpMesrlineNetTxLaserTempIndex,
       "pm10010mpMesrlineNetTxLaserTempPortn": pm10010mpMesrlineNetTxLaserTempPortn,
       "pm10010mpMesrlineNetTxBiasCurrentTable": pm10010mpMesrlineNetTxBiasCurrentTable,
       "pm10010mpMesrlineNetTxBiasCurrentEntry": pm10010mpMesrlineNetTxBiasCurrentEntry,
       "pm10010mpMesrlineNetTxBiasCurrentIndex": pm10010mpMesrlineNetTxBiasCurrentIndex,
       "pm10010mpMesrlineNetTxBiasCurrentPortn": pm10010mpMesrlineNetTxBiasCurrentPortn,
       "pm10010mpMesrlineNetRxInputPwrTable": pm10010mpMesrlineNetRxInputPwrTable,
       "pm10010mpMesrlineNetRxInputPwrEntry": pm10010mpMesrlineNetRxInputPwrEntry,
       "pm10010mpMesrlineNetRxInputPwrIndex": pm10010mpMesrlineNetRxInputPwrIndex,
       "pm10010mpMesrlineNetRxInputPwrPortn": pm10010mpMesrlineNetRxInputPwrPortn,
       "pm10010mpMesrlineResidualChromaticDispTable": pm10010mpMesrlineResidualChromaticDispTable,
       "pm10010mpMesrlineResidualChromaticDispEntry": pm10010mpMesrlineResidualChromaticDispEntry,
       "pm10010mpMesrlineResidualChromaticDispIndex": pm10010mpMesrlineResidualChromaticDispIndex,
       "pm10010mpMesrlineResidualChromaticDispPortn": pm10010mpMesrlineResidualChromaticDispPortn,
       "pm10010mpMesrlineDiffGroupDelayTable": pm10010mpMesrlineDiffGroupDelayTable,
       "pm10010mpMesrlineDiffGroupDelayEntry": pm10010mpMesrlineDiffGroupDelayEntry,
       "pm10010mpMesrlineDiffGroupDelayIndex": pm10010mpMesrlineDiffGroupDelayIndex,
       "pm10010mpMesrlineDiffGroupDelayPortn": pm10010mpMesrlineDiffGroupDelayPortn,
       "pm10010mpMesrlineQFactorTable": pm10010mpMesrlineQFactorTable,
       "pm10010mpMesrlineQFactorEntry": pm10010mpMesrlineQFactorEntry,
       "pm10010mpMesrlineQFactorIndex": pm10010mpMesrlineQFactorIndex,
       "pm10010mpMesrlineQFactorPortn": pm10010mpMesrlineQFactorPortn,
       "pm10010mpMesrlineCarrierFreqOffsetTable": pm10010mpMesrlineCarrierFreqOffsetTable,
       "pm10010mpMesrlineCarrierFreqOffsetEntry": pm10010mpMesrlineCarrierFreqOffsetEntry,
       "pm10010mpMesrlineCarrierFreqOffsetIndex": pm10010mpMesrlineCarrierFreqOffsetIndex,
       "pm10010mpMesrlineCarrierFreqOffsetPortn": pm10010mpMesrlineCarrierFreqOffsetPortn,
       "pm10010mpMesrlineOsnrTable": pm10010mpMesrlineOsnrTable,
       "pm10010mpMesrlineOsnrEntry": pm10010mpMesrlineOsnrEntry,
       "pm10010mpMesrlineOsnrIndex": pm10010mpMesrlineOsnrIndex,
       "pm10010mpMesrlineOsnrPortn": pm10010mpMesrlineOsnrPortn,
       "pm10010mpcounters": pm10010mpcounters,
       "pm10010mpCntOther": pm10010mpCntOther,
       "pm10010mpCntClient": pm10010mpCntClient,
       "pm10010mpCntclientInputErrorCounterLaneOneTable": pm10010mpCntclientInputErrorCounterLaneOneTable,
       "pm10010mpCntclientInputErrorCounterLaneOneEntry": pm10010mpCntclientInputErrorCounterLaneOneEntry,
       "pm10010mpCntclientInputErrorCounterLaneOneIndex": pm10010mpCntclientInputErrorCounterLaneOneIndex,
       "pm10010mpCntclientInputErrorCounterLaneOneValuePortn": pm10010mpCntclientInputErrorCounterLaneOneValuePortn,
       "pm10010mpCntclientInputErrorCounterLaneOneErrorPortn": pm10010mpCntclientInputErrorCounterLaneOneErrorPortn,
       "pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn": pm10010mpCntclientInputErrorCounterLaneOneOverloadPortn,
       "pm10010mpCntclientInputErrorCounterLaneTwoTable": pm10010mpCntclientInputErrorCounterLaneTwoTable,
       "pm10010mpCntclientInputErrorCounterLaneTwoEntry": pm10010mpCntclientInputErrorCounterLaneTwoEntry,
       "pm10010mpCntclientInputErrorCounterLaneTwoIndex": pm10010mpCntclientInputErrorCounterLaneTwoIndex,
       "pm10010mpCntclientInputErrorCounterLaneTwoValuePortn": pm10010mpCntclientInputErrorCounterLaneTwoValuePortn,
       "pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn": pm10010mpCntclientInputErrorCounterLaneTwoErrorPortn,
       "pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn": pm10010mpCntclientInputErrorCounterLaneTwoOverloadPortn,
       "pm10010mpCntclientInputErrorCounterTable": pm10010mpCntclientInputErrorCounterTable,
       "pm10010mpCntclientInputErrorCounterEntry": pm10010mpCntclientInputErrorCounterEntry,
       "pm10010mpCntclientInputErrorCounterIndex": pm10010mpCntclientInputErrorCounterIndex,
       "pm10010mpCntclientInputErrorCounterValuePortn": pm10010mpCntclientInputErrorCounterValuePortn,
       "pm10010mpCntclientInputErrorCounterErrorPortn": pm10010mpCntclientInputErrorCounterErrorPortn,
       "pm10010mpCntclientInputErrorCounterOverloadPortn": pm10010mpCntclientInputErrorCounterOverloadPortn,
       "pm10010mpCntclientCbipCounterTable": pm10010mpCntclientCbipCounterTable,
       "pm10010mpCntclientCbipCounterEntry": pm10010mpCntclientCbipCounterEntry,
       "pm10010mpCntclientCbipCounterIndex": pm10010mpCntclientCbipCounterIndex,
       "pm10010mpCntclientCbipCounterValuePortn": pm10010mpCntclientCbipCounterValuePortn,
       "pm10010mpCntclientCbipCounterErrorPortn": pm10010mpCntclientCbipCounterErrorPortn,
       "pm10010mpCntclientCbipCounterOverloadPortn": pm10010mpCntclientCbipCounterOverloadPortn,
       "pm10010mpCntLine": pm10010mpCntLine,
       "pm10010mpCntlocalLineSmBip8ErrorCounterTable": pm10010mpCntlocalLineSmBip8ErrorCounterTable,
       "pm10010mpCntlocalLineSmBip8ErrorCounterEntry": pm10010mpCntlocalLineSmBip8ErrorCounterEntry,
       "pm10010mpCntlocalLineSmBip8ErrorCounterIndex": pm10010mpCntlocalLineSmBip8ErrorCounterIndex,
       "pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn": pm10010mpCntlocalLineSmBip8ErrorCounterValuePortn,
       "pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn": pm10010mpCntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn": pm10010mpCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm10010mpCntlocalLineFecCorrectedErrorsCounterTable": pm10010mpCntlocalLineFecCorrectedErrorsCounterTable,
       "pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry": pm10010mpCntlocalLineFecCorrectedErrorsCounterEntry,
       "pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex": pm10010mpCntlocalLineFecCorrectedErrorsCounterIndex,
       "pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn": pm10010mpCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn": pm10010mpCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm10010mpCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm10010mpCntremoteLineSmBip8ErrorCounterTable": pm10010mpCntremoteLineSmBip8ErrorCounterTable,
       "pm10010mpCntremoteLineSmBip8ErrorCounterEntry": pm10010mpCntremoteLineSmBip8ErrorCounterEntry,
       "pm10010mpCntremoteLineSmBip8ErrorCounterIndex": pm10010mpCntremoteLineSmBip8ErrorCounterIndex,
       "pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn": pm10010mpCntremoteLineSmBip8ErrorCounterValuePortn,
       "pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn": pm10010mpCntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn": pm10010mpCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm10010mpCntlineDfrmTimCntTable": pm10010mpCntlineDfrmTimCntTable,
       "pm10010mpCntlineDfrmTimCntEntry": pm10010mpCntlineDfrmTimCntEntry,
       "pm10010mpCntlineDfrmTimCntIndex": pm10010mpCntlineDfrmTimCntIndex,
       "pm10010mpCntlineDfrmTimCntValuePortn": pm10010mpCntlineDfrmTimCntValuePortn,
       "pm10010mpCntlineDfrmTimCntErrorPortn": pm10010mpCntlineDfrmTimCntErrorPortn,
       "pm10010mpCntlineDfrmTimCntOverloadPortn": pm10010mpCntlineDfrmTimCntOverloadPortn,
       "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable": pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterTable,
       "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry": pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterEntry,
       "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex": pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterIndex,
       "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn": pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterValuePortn,
       "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn": pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterErrorPortn,
       "pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn": pm10010mpCntlocalLineTrscvFecCorrectedErrorCounterOverloadPortn,
       "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable": pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterTable,
       "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry": pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterEntry,
       "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex": pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterIndex,
       "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn": pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterValuePortn,
       "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn": pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterErrorPortn,
       "pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn": pm10010mpCntlocalLineTrscvFecUncorrectedErrorCounterOverloadPortn,
       "pm10010mpcontrolsWrite": pm10010mpcontrolsWrite,
       "pm10010mpCtrlOther": pm10010mpCtrlOther,
       "pm10010mpCtrlconfMgnt1": pm10010mpCtrlconfMgnt1,
       "pm10010mpCtrlConf1Load1": pm10010mpCtrlConf1Load1,
       "pm10010mpCtrlConf2Load1": pm10010mpCtrlConf2Load1,
       "pm10010mpCtrlConf2Flash1": pm10010mpCtrlConf2Flash1,
       "pm10010mpCtrlConf2Clear1": pm10010mpCtrlConf2Clear1,
       "pm10010mpCtrlsynth4": pm10010mpCtrlsynth4,
       "pm10010mpCtrlCorrelatOn": pm10010mpCtrlCorrelatOn,
       "pm10010mpCtrlCorrelatOff": pm10010mpCtrlCorrelatOff,
       "pm10010mpCtrlswMgnt": pm10010mpCtrlswMgnt,
       "pm10010mpCtrlColdReset": pm10010mpCtrlColdReset,
       "pm10010mpCtrlWarmReset": pm10010mpCtrlWarmReset,
       "pm10010mpCtrlLoadSwBank1": pm10010mpCtrlLoadSwBank1,
       "pm10010mpCtrlLoadSwBank2": pm10010mpCtrlLoadSwBank2,
       "pm10010mpCtrlgwMgnt": pm10010mpCtrlgwMgnt,
       "pm10010mpCtrlCurrentGwReset": pm10010mpCtrlCurrentGwReset,
       "pm10010mpCtrlLoadGwBank1": pm10010mpCtrlLoadGwBank1,
       "pm10010mpCtrlLoadGwBank2": pm10010mpCtrlLoadGwBank2,
       "pm10010mpCtrlLoadGwBank3": pm10010mpCtrlLoadGwBank3,
       "pm10010mpCtrlLoadGwBank4": pm10010mpCtrlLoadGwBank4,
       "pm10010mpCtrlledTest": pm10010mpCtrlledTest,
       "pm10010mpCtrlGreenLed": pm10010mpCtrlGreenLed,
       "pm10010mpCtrlRedLed": pm10010mpCtrlRedLed,
       "pm10010mpCtrlLedOff": pm10010mpCtrlLedOff,
       "pm10010mpCtrlinitSwitchMarvell": pm10010mpCtrlinitSwitchMarvell,
       "pm10010mpCtrlInitSwitchMarvell": pm10010mpCtrlInitSwitchMarvell,
       "pm10010mpCtrlresetCount": pm10010mpCtrlresetCount,
       "pm10010mpCtrlResetcount": pm10010mpCtrlResetcount,
       "pm10010mpCtrlresetRmon": pm10010mpCtrlresetRmon,
       "pm10010mpCtrlResetrmon": pm10010mpCtrlResetrmon,
       "pm10010mpCtrlresetMeasurements": pm10010mpCtrlresetMeasurements,
       "pm10010mpCtrlResetmeasurements": pm10010mpCtrlResetmeasurements,
       "pm10010mpCtrlClient": pm10010mpCtrlClient,
       "pm10010mpCtrlaccessLoopTable": pm10010mpCtrlaccessLoopTable,
       "pm10010mpCtrlaccessLoopEntry": pm10010mpCtrlaccessLoopEntry,
       "pm10010mpCtrlaccessLoopIndex": pm10010mpCtrlaccessLoopIndex,
       "pm10010mpCtrlaccessLoopPortn": pm10010mpCtrlaccessLoopPortn,
       "pm10010mpCtrlclientLoopToLineTable": pm10010mpCtrlclientLoopToLineTable,
       "pm10010mpCtrlclientLoopToLineEntry": pm10010mpCtrlclientLoopToLineEntry,
       "pm10010mpCtrlclientLoopToLineIndex": pm10010mpCtrlclientLoopToLineIndex,
       "pm10010mpCtrlclientLoopToLinePortn": pm10010mpCtrlclientLoopToLinePortn,
       "pm10010mpCtrlcsfUpInsTable": pm10010mpCtrlcsfUpInsTable,
       "pm10010mpCtrlcsfUpInsEntry": pm10010mpCtrlcsfUpInsEntry,
       "pm10010mpCtrlcsfUpInsIndex": pm10010mpCtrlcsfUpInsIndex,
       "pm10010mpCtrlcsfUpInsPortn": pm10010mpCtrlcsfUpInsPortn,
       "pm10010mpCtrlcaisDwInsTable": pm10010mpCtrlcaisDwInsTable,
       "pm10010mpCtrlcaisDwInsEntry": pm10010mpCtrlcaisDwInsEntry,
       "pm10010mpCtrlcaisDwInsIndex": pm10010mpCtrlcaisDwInsIndex,
       "pm10010mpCtrlcaisDwInsPortn": pm10010mpCtrlcaisDwInsPortn,
       "pm10010mpCtrlLine": pm10010mpCtrlLine,
       "pm10010mpCtrlcommAccessLoopTable": pm10010mpCtrlcommAccessLoopTable,
       "pm10010mpCtrlcommAccessLoopEntry": pm10010mpCtrlcommAccessLoopEntry,
       "pm10010mpCtrlcommAccessLoopIndex": pm10010mpCtrlcommAccessLoopIndex,
       "pm10010mpCtrlcommAccessLoopPortn": pm10010mpCtrlcommAccessLoopPortn,
       "pm10010mpCtrllineLoopTable": pm10010mpCtrllineLoopTable,
       "pm10010mpCtrllineLoopEntry": pm10010mpCtrllineLoopEntry,
       "pm10010mpCtrllineLoopIndex": pm10010mpCtrllineLoopIndex,
       "pm10010mpCtrllineLoopPortn": pm10010mpCtrllineLoopPortn,
       "pm10010mpCtrlfecDisableTable": pm10010mpCtrlfecDisableTable,
       "pm10010mpCtrlfecDisableEntry": pm10010mpCtrlfecDisableEntry,
       "pm10010mpCtrlfecDisableIndex": pm10010mpCtrlfecDisableIndex,
       "pm10010mpCtrlfecDisablePortn": pm10010mpCtrlfecDisablePortn,
       "pm10010mpCtrlmsaLineLoopTable": pm10010mpCtrlmsaLineLoopTable,
       "pm10010mpCtrlmsaLineLoopEntry": pm10010mpCtrlmsaLineLoopEntry,
       "pm10010mpCtrlmsaLineLoopIndex": pm10010mpCtrlmsaLineLoopIndex,
       "pm10010mpCtrlmsaLineLoopPortn": pm10010mpCtrlmsaLineLoopPortn,
       "pm10010mpCtrlmsaTxResetTable": pm10010mpCtrlmsaTxResetTable,
       "pm10010mpCtrlmsaTxResetEntry": pm10010mpCtrlmsaTxResetEntry,
       "pm10010mpCtrlmsaTxResetIndex": pm10010mpCtrlmsaTxResetIndex,
       "pm10010mpCtrlmsaTxResetPortn": pm10010mpCtrlmsaTxResetPortn,
       "pm10010mpCtrlmsaRxResetTable": pm10010mpCtrlmsaRxResetTable,
       "pm10010mpCtrlmsaRxResetEntry": pm10010mpCtrlmsaRxResetEntry,
       "pm10010mpCtrlmsaRxResetIndex": pm10010mpCtrlmsaRxResetIndex,
       "pm10010mpCtrlmsaRxResetPortn": pm10010mpCtrlmsaRxResetPortn,
       "pm10010mpCtrlmsaShutdownTable": pm10010mpCtrlmsaShutdownTable,
       "pm10010mpCtrlmsaShutdownEntry": pm10010mpCtrlmsaShutdownEntry,
       "pm10010mpCtrlmsaShutdownIndex": pm10010mpCtrlmsaShutdownIndex,
       "pm10010mpCtrlmsaShutdownPortn": pm10010mpCtrlmsaShutdownPortn,
       "pm10010mpri": pm10010mpri,
       "pm10010mpriTable": pm10010mpriTable,
       "pm10010mpRinvSfpTable": pm10010mpRinvSfpTable,
       "pm10010mpRinvSfpEntry": pm10010mpRinvSfpEntry,
       "pm10010mpRinvSfpIndex": pm10010mpRinvSfpIndex,
       "pm10010mpRinvsfp": pm10010mpRinvsfp,
       "pm10010mpRinvLineTable": pm10010mpRinvLineTable,
       "pm10010mpRinvLineEntry": pm10010mpRinvLineEntry,
       "pm10010mpRinvLineIndex": pm10010mpRinvLineIndex,
       "pm10010mpRinvxfpLine": pm10010mpRinvxfpLine,
       "pm10010mpRinvReloadInventory": pm10010mpRinvReloadInventory,
       "pm10010mpRinvHwPlatform": pm10010mpRinvHwPlatform,
       "pm10010mpRinvModulePlatform": pm10010mpRinvModulePlatform,
       "pm10010mpRinvSwPlatform": pm10010mpRinvSwPlatform,
       "pm10010mpRinvGwPlatform": pm10010mpRinvGwPlatform,
       "pm10010mpdownload": pm10010mpdownload,
       "pm10010mpDwlOther": pm10010mpDwlOther,
       "pm10010mpDwlrestartProcess": pm10010mpDwlrestartProcess,
       "pm10010mpDwlWarmRestartProcessed": pm10010mpDwlWarmRestartProcessed,
       "pm10010mpDwlColdRestartProcessed": pm10010mpDwlColdRestartProcessed,
       "pm10010mpDwlswBanksUsed": pm10010mpDwlswBanksUsed,
       "pm10010mpDwlSwBank1Used": pm10010mpDwlSwBank1Used,
       "pm10010mpDwlSwBank2Used": pm10010mpDwlSwBank2Used,
       "pm10010mpDwlSwBank1Notempty": pm10010mpDwlSwBank1Notempty,
       "pm10010mpDwlSwBank2Notempty": pm10010mpDwlSwBank2Notempty,
       "pm10010mpDwlgwBanksUsed": pm10010mpDwlgwBanksUsed,
       "pm10010mpDwlGwBank1Used": pm10010mpDwlGwBank1Used,
       "pm10010mpDwlGwBank2Used": pm10010mpDwlGwBank2Used,
       "pm10010mpDwlGwBank3Used": pm10010mpDwlGwBank3Used,
       "pm10010mpDwlGwBank4Used": pm10010mpDwlGwBank4Used,
       "pm10010mpDwlGwBank1Notempty": pm10010mpDwlGwBank1Notempty,
       "pm10010mpDwlGwBank2Notempty": pm10010mpDwlGwBank2Notempty,
       "pm10010mpDwlGwBank3Notempty": pm10010mpDwlGwBank3Notempty,
       "pm10010mpDwlGwBank4Notempty": pm10010mpDwlGwBank4Notempty,
       "pm10010mpDwlClient": pm10010mpDwlClient,
       "pm10010mpDwlLine": pm10010mpDwlLine,
       "pm10010mpConfig": pm10010mpConfig,
       "pm10010mpCfgAccessCAisCsf": pm10010mpCfgAccessCAisCsf,
       "pm10010mpCfgClientcaiscsfTable": pm10010mpCfgClientcaiscsfTable,
       "pm10010mpCfgClientcaiscsfEntry": pm10010mpCfgClientcaiscsfEntry,
       "pm10010mpCfgClientcaiscsfIndex": pm10010mpCfgClientcaiscsfIndex,
       "pm10010mpCfgReservePortn": pm10010mpCfgReservePortn,
       "pm10010mpCfgStartup": pm10010mpCfgStartup,
       "pm10010mpCfgClientStartupTable": pm10010mpCfgClientStartupTable,
       "pm10010mpCfgClientStartupEntry": pm10010mpCfgClientStartupEntry,
       "pm10010mpCfgClientStartupIndex": pm10010mpCfgClientStartupIndex,
       "pm10010mpCfgSystConfPortPortn": pm10010mpCfgSystConfPortPortn,
       "pm10010mpCfgNetConfPortPortn": pm10010mpCfgNetConfPortPortn,
       "pm10010mpCfgOptionsPortPortn": pm10010mpCfgOptionsPortPortn,
       "pm10010mpCfgLineStartupTable": pm10010mpCfgLineStartupTable,
       "pm10010mpCfgLineStartupEntry": pm10010mpCfgLineStartupEntry,
       "pm10010mpCfgLineStartupIndex": pm10010mpCfgLineStartupIndex,
       "pm10010mpCfgSystConfLinePortn": pm10010mpCfgSystConfLinePortn,
       "pm10010mpCfgOptionsLinePortn": pm10010mpCfgOptionsLinePortn,
       "pm10010mpCfgXfpTable": pm10010mpCfgXfpTable,
       "pm10010mpCfgXfpEntry": pm10010mpCfgXfpEntry,
       "pm10010mpCfgXfpIndex": pm10010mpCfgXfpIndex,
       "pm10010mpCfgSystConfMsaLinePortn": pm10010mpCfgSystConfMsaLinePortn,
       "pm10010mpCfgClientOtxtlhTable": pm10010mpCfgClientOtxtlhTable,
       "pm10010mpCfgClientOtxtlhEntry": pm10010mpCfgClientOtxtlhEntry,
       "pm10010mpCfgClientOtxtlhIndex": pm10010mpCfgClientOtxtlhIndex,
       "pm10010mpCfgControlsPortn": pm10010mpCfgControlsPortn,
       "pm10010mpCfgClientPwrLaserPortn": pm10010mpCfgClientPwrLaserPortn,
       "pm10010mpCfgClientFCurrentPortn": pm10010mpCfgClientFCurrentPortn,
       "pm10010mpCfgClientGridCurrentPortn": pm10010mpCfgClientGridCurrentPortn,
       "pm10010mpCfgClientFoPortn": pm10010mpCfgClientFoPortn,
       "pm10010mpCfgLabels": pm10010mpCfgLabels,
       "pm10010mpCfgLabelclientTable": pm10010mpCfgLabelclientTable,
       "pm10010mpCfgLabelclientEntry": pm10010mpCfgLabelclientEntry,
       "pm10010mpCfgLabelclientIndex": pm10010mpCfgLabelclientIndex,
       "pm10010mpCfgLabelclientPortn": pm10010mpCfgLabelclientPortn,
       "pm10010mpCfgLabellineTable": pm10010mpCfgLabellineTable,
       "pm10010mpCfgLabellineEntry": pm10010mpCfgLabellineEntry,
       "pm10010mpCfgLabellineIndex": pm10010mpCfgLabellineIndex,
       "pm10010mpCfgLabellinePortn": pm10010mpCfgLabellinePortn,
       "pm10010mpCfgStartuptlh": pm10010mpCfgStartuptlh,
       "pm10010mpCfgOtxtlhTable": pm10010mpCfgOtxtlhTable,
       "pm10010mpCfgOtxtlhEntry": pm10010mpCfgOtxtlhEntry,
       "pm10010mpCfgOtxtlhIndex": pm10010mpCfgOtxtlhIndex,
       "pm10010mpCfgLinePwrLaserPortn": pm10010mpCfgLinePwrLaserPortn,
       "pm10010mpCfgLineFCurrentPortn": pm10010mpCfgLineFCurrentPortn,
       "pm10010mpCfgLineGridCurrentPortn": pm10010mpCfgLineGridCurrentPortn,
       "pm10010mpCfgFPortn": pm10010mpCfgFPortn,
       "pm10010mpCfgRxLineFCurrentPortn": pm10010mpCfgRxLineFCurrentPortn,
       "pm10010mpCfgOther": pm10010mpCfgOther,
       "pm10010mptablemoduleOther": pm10010mptablemoduleOther,
       "pm10010mpCfgmode": pm10010mpCfgmode,
       "pm10010mpCfgfanLowSpeedThreshold": pm10010mpCfgfanLowSpeedThreshold,
       "pm10010mpCfgfanHighSpeedThreshold": pm10010mpCfgfanHighSpeedThreshold,
       "pm10010mpCfgStartuptablefive": pm10010mpCfgStartuptablefive,
       "pm10010mpCfgOtxtlhcapabilitiesTable": pm10010mpCfgOtxtlhcapabilitiesTable,
       "pm10010mpCfgOtxtlhcapabilitiesEntry": pm10010mpCfgOtxtlhcapabilitiesEntry,
       "pm10010mpCfgOtxtlhcapabilitiesIndex": pm10010mpCfgOtxtlhcapabilitiesIndex,
       "pm10010mpCfgComponentTypePortn": pm10010mpCfgComponentTypePortn,
       "pm10010mpCfgMiscellaneousPortn": pm10010mpCfgMiscellaneousPortn,
       "pm10010mpCfgFirstChannelPortn": pm10010mpCfgFirstChannelPortn,
       "pm10010mpCfgLastChannelPortn": pm10010mpCfgLastChannelPortn,
       "pm10010mpCfgGridPortn": pm10010mpCfgGridPortn,
       "pm10010mpCfgWriteConfiguration": pm10010mpCfgWriteConfiguration,
       "pm10010mptraps": pm10010mptraps,
       "pm10010mptrapPortNumber": pm10010mptrapPortNumber,
       "pm10010mptrapLineNumber": pm10010mptrapLineNumber,
       "pm10010mptrapBoardNumber": pm10010mptrapBoardNumber,
       "pm10010mpLineTrapNotUrgentGoesOn": pm10010mpLineTrapNotUrgentGoesOn,
       "pm10010mpLineTrapNotUrgentGoesOff": pm10010mpLineTrapNotUrgentGoesOff,
       "pm10010mpLineTrapUrgentGoesOn": pm10010mpLineTrapUrgentGoesOn,
       "pm10010mpLineTrapUrgentGoesOff": pm10010mpLineTrapUrgentGoesOff,
       "pm10010mpLineTrapCritGoesOn": pm10010mpLineTrapCritGoesOn,
       "pm10010mpLineTrapCritGoesOff": pm10010mpLineTrapCritGoesOff,
       "pm10010mpClientTrapNotUrgentGoesOn": pm10010mpClientTrapNotUrgentGoesOn,
       "pm10010mpClientTrapNotUrgentGoesOff": pm10010mpClientTrapNotUrgentGoesOff,
       "pm10010mpClientTrapUrgentGoesOn": pm10010mpClientTrapUrgentGoesOn,
       "pm10010mpClientTrapUrgentGoesOff": pm10010mpClientTrapUrgentGoesOff,
       "pm10010mpClientTrapCritGoesOn": pm10010mpClientTrapCritGoesOn,
       "pm10010mpClientTrapCritGoesOff": pm10010mpClientTrapCritGoesOff,
       "pm10010mpPowerTrapUrgentGoesOn": pm10010mpPowerTrapUrgentGoesOn,
       "pm10010mpPowerTrapUrgentGoesOff": pm10010mpPowerTrapUrgentGoesOff,
       "pm10010mpMonitoring": pm10010mpMonitoring,
       "pm10010mpMonOther": pm10010mpMonOther,
       "pm10010mpMonRmon": pm10010mpMonRmon,
       "pm10010mpMonClient": pm10010mpMonClient,
       "pm10010mpMonClientRmonCounter": pm10010mpMonClientRmonCounter,
       "pm10010mpMonupRmonBytesCounterClientInputTable": pm10010mpMonupRmonBytesCounterClientInputTable,
       "pm10010mpMonupRmonBytesCounterClientInputEntry": pm10010mpMonupRmonBytesCounterClientInputEntry,
       "pm10010mpMonupRmonBytesCounterClientInputIndex": pm10010mpMonupRmonBytesCounterClientInputIndex,
       "pm10010mpMonupRmonBytesCounterClientInputValuePortn": pm10010mpMonupRmonBytesCounterClientInputValuePortn,
       "pm10010mpMonupRmonBytesCounterClientInputErrorPortn": pm10010mpMonupRmonBytesCounterClientInputErrorPortn,
       "pm10010mpMonupRmonBytesCounterClientInputOverloadPortn": pm10010mpMonupRmonBytesCounterClientInputOverloadPortn,
       "pm10010mpMonupRmonCrcErrorsCounterClientInputTable": pm10010mpMonupRmonCrcErrorsCounterClientInputTable,
       "pm10010mpMonupRmonCrcErrorsCounterClientInputEntry": pm10010mpMonupRmonCrcErrorsCounterClientInputEntry,
       "pm10010mpMonupRmonCrcErrorsCounterClientInputIndex": pm10010mpMonupRmonCrcErrorsCounterClientInputIndex,
       "pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn": pm10010mpMonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn": pm10010mpMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn": pm10010mpMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm10010mpMonupRmonPacketsCounterClientInputTable": pm10010mpMonupRmonPacketsCounterClientInputTable,
       "pm10010mpMonupRmonPacketsCounterClientInputEntry": pm10010mpMonupRmonPacketsCounterClientInputEntry,
       "pm10010mpMonupRmonPacketsCounterClientInputIndex": pm10010mpMonupRmonPacketsCounterClientInputIndex,
       "pm10010mpMonupRmonPacketsCounterClientInputValuePortn": pm10010mpMonupRmonPacketsCounterClientInputValuePortn,
       "pm10010mpMonupRmonPacketsCounterClientInputErrorPortn": pm10010mpMonupRmonPacketsCounterClientInputErrorPortn,
       "pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn": pm10010mpMonupRmonPacketsCounterClientInputOverloadPortn,
       "pm10010mpMonupRmonBroadcastCounterClientInputTable": pm10010mpMonupRmonBroadcastCounterClientInputTable,
       "pm10010mpMonupRmonBroadcastCounterClientInputEntry": pm10010mpMonupRmonBroadcastCounterClientInputEntry,
       "pm10010mpMonupRmonBroadcastCounterClientInputIndex": pm10010mpMonupRmonBroadcastCounterClientInputIndex,
       "pm10010mpMonupRmonBroadcastCounterClientInputValuePortn": pm10010mpMonupRmonBroadcastCounterClientInputValuePortn,
       "pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn": pm10010mpMonupRmonBroadcastCounterClientInputErrorPortn,
       "pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn": pm10010mpMonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm10010mpMonupRmonMulticastCounterClientInputTable": pm10010mpMonupRmonMulticastCounterClientInputTable,
       "pm10010mpMonupRmonMulticastCounterClientInputEntry": pm10010mpMonupRmonMulticastCounterClientInputEntry,
       "pm10010mpMonupRmonMulticastCounterClientInputIndex": pm10010mpMonupRmonMulticastCounterClientInputIndex,
       "pm10010mpMonupRmonMulticastCounterClientInputValuePortn": pm10010mpMonupRmonMulticastCounterClientInputValuePortn,
       "pm10010mpMonupRmonMulticastCounterClientInputErrorPortn": pm10010mpMonupRmonMulticastCounterClientInputErrorPortn,
       "pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn": pm10010mpMonupRmonMulticastCounterClientInputOverloadPortn,
       "pm10010mpMonupRmonPauseFrameCounterClientInputTable": pm10010mpMonupRmonPauseFrameCounterClientInputTable,
       "pm10010mpMonupRmonPauseFrameCounterClientInputEntry": pm10010mpMonupRmonPauseFrameCounterClientInputEntry,
       "pm10010mpMonupRmonPauseFrameCounterClientInputIndex": pm10010mpMonupRmonPauseFrameCounterClientInputIndex,
       "pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn": pm10010mpMonupRmonPauseFrameCounterClientInputValuePortn,
       "pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn": pm10010mpMonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn": pm10010mpMonupRmonPauseFrameCounterClientInputOverloadPortn}
)
