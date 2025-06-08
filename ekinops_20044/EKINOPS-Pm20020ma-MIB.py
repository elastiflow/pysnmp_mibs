# SNMP MIB module (EKINOPS-Pm20020ma-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm20020ma-MIB.mib
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

modulePm20020ma = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69)
)
if mibBuilder.loadTexts:
    modulePm20020ma.setRevisions(
        ("2015-03-19 00:00",
         "2016-01-05 00:00",
         "2016-02-29 00:00",
         "2016-04-20 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00",
         "2017-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm20020maMultiRate(TextualConvention, Integer32):
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



class Pm20020maOtxMode(TextualConvention, Integer32):
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



class Pm20020maOtxGrid(TextualConvention, Integer32):
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



class Pm20020maAdjustValue(TextualConvention, Integer32):
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



class Pm20020maClientProtocol(TextualConvention, Integer32):
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



class Pm20020maProtocolMode(TextualConvention, Integer32):
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



class Pm20020maOtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm20020maOrxChannel(TextualConvention, Integer32):
    status = "current"


class Pm20020maDccMode(TextualConvention, Integer32):
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
        *(("dccNo", 0),
          ("dccLine1", 1),
          ("dccLine2", 2))
    )



class Pm20020maModuleMode(TextualConvention, Integer32):
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
        *(("unusedmode", 0),
          ("mode200gma", 1),
          ("mode200gmr", 2),
          ("mode100gulh", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Pm20020maalarms_ObjectIdentity = ObjectIdentity
pm20020maalarms = _Pm20020maalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2)
)
_Pm20020maAlmOther_ObjectIdentity = ObjectIdentity
pm20020maAlmOther = _Pm20020maAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1)
)
_Pm20020maAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm20020maAlmOtherNurg = _Pm20020maAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1)
)
_Pm20020maAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm20020maAlmsynthAlm2 = _Pm20020maAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1, 2)
)
_Pm20020maAlmConfTableSave_Type = EkiOnOff
_Pm20020maAlmConfTableSave_Object = MibScalar
pm20020maAlmConfTableSave = _Pm20020maAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1, 2, 1),
    _Pm20020maAlmConfTableSave_Type()
)
pm20020maAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmConfTableSave.setStatus("current")
_Pm20020maAlmInvUpload_Type = EkiOnOff
_Pm20020maAlmInvUpload_Object = MibScalar
pm20020maAlmInvUpload = _Pm20020maAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1, 2, 2),
    _Pm20020maAlmInvUpload_Type()
)
pm20020maAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmInvUpload.setStatus("current")
_Pm20020maAlmConfTableLoad_Type = EkiOnOff
_Pm20020maAlmConfTableLoad_Object = MibScalar
pm20020maAlmConfTableLoad = _Pm20020maAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1, 2, 3),
    _Pm20020maAlmConfTableLoad_Type()
)
pm20020maAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmConfTableLoad.setStatus("current")
_Pm20020maAlmCorrelatOff_Type = EkiOnOff
_Pm20020maAlmCorrelatOff_Object = MibScalar
pm20020maAlmCorrelatOff = _Pm20020maAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1, 2, 4),
    _Pm20020maAlmCorrelatOff_Type()
)
pm20020maAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCorrelatOff.setStatus("current")
_Pm20020maAlmMaintenanceOn_Type = EkiOnOff
_Pm20020maAlmMaintenanceOn_Object = MibScalar
pm20020maAlmMaintenanceOn = _Pm20020maAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 1, 2, 5),
    _Pm20020maAlmMaintenanceOn_Type()
)
pm20020maAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMaintenanceOn.setStatus("current")
_Pm20020maAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm20020maAlmOtherUrg = _Pm20020maAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 2)
)
_Pm20020maAlmmodFanFail_ObjectIdentity = ObjectIdentity
pm20020maAlmmodFanFail = _Pm20020maAlmmodFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 2, 336)
)
_Pm20020maAlmFanFail_Type = EkiOnOff
_Pm20020maAlmFanFail_Object = MibScalar
pm20020maAlmFanFail = _Pm20020maAlmFanFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 2, 336, 1),
    _Pm20020maAlmFanFail_Type()
)
pm20020maAlmFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmFanFail.setStatus("current")
_Pm20020maAlmFanHighSpeed_Type = EkiOnOff
_Pm20020maAlmFanHighSpeed_Object = MibScalar
pm20020maAlmFanHighSpeed = _Pm20020maAlmFanHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 2, 336, 2),
    _Pm20020maAlmFanHighSpeed_Type()
)
pm20020maAlmFanHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmFanHighSpeed.setStatus("current")
_Pm20020maAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm20020maAlmOtherCrit = _Pm20020maAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3)
)
_Pm20020maAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm20020maAlmsynthAlm0 = _Pm20020maAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 0)
)
_Pm20020maAlmFailFan_Type = EkiOnOff
_Pm20020maAlmFailFan_Object = MibScalar
pm20020maAlmFailFan = _Pm20020maAlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 0, 2),
    _Pm20020maAlmFailFan_Type()
)
pm20020maAlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmFailFan.setStatus("current")
_Pm20020maAlmModGlobFail_Type = EkiOnOff
_Pm20020maAlmModGlobFail_Object = MibScalar
pm20020maAlmModGlobFail = _Pm20020maAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 0, 9),
    _Pm20020maAlmModGlobFail_Type()
)
pm20020maAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmModGlobFail.setStatus("current")
_Pm20020maAlmDefFuseA_Type = EkiOnOff
_Pm20020maAlmDefFuseA_Object = MibScalar
pm20020maAlmDefFuseA = _Pm20020maAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 0, 15),
    _Pm20020maAlmDefFuseA_Type()
)
pm20020maAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmDefFuseA.setStatus("current")
_Pm20020maAlmDefFuseB_Type = EkiOnOff
_Pm20020maAlmDefFuseB_Object = MibScalar
pm20020maAlmDefFuseB = _Pm20020maAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 0, 16),
    _Pm20020maAlmDefFuseB_Type()
)
pm20020maAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmDefFuseB.setStatus("current")
_Pm20020maAlmclientModuleState_ObjectIdentity = ObjectIdentity
pm20020maAlmclientModuleState = _Pm20020maAlmclientModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72)
)
_Pm20020maAlmCfpInitialize_Type = EkiOnOff
_Pm20020maAlmCfpInitialize_Object = MibScalar
pm20020maAlmCfpInitialize = _Pm20020maAlmCfpInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 1),
    _Pm20020maAlmCfpInitialize_Type()
)
pm20020maAlmCfpInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpInitialize.setStatus("current")
_Pm20020maAlmCfpLowPower_Type = EkiOnOff
_Pm20020maAlmCfpLowPower_Object = MibScalar
pm20020maAlmCfpLowPower = _Pm20020maAlmCfpLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 2),
    _Pm20020maAlmCfpLowPower_Type()
)
pm20020maAlmCfpLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpLowPower.setStatus("current")
_Pm20020maAlmCfpHighPowerUp_Type = EkiOnOff
_Pm20020maAlmCfpHighPowerUp_Object = MibScalar
pm20020maAlmCfpHighPowerUp = _Pm20020maAlmCfpHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 3),
    _Pm20020maAlmCfpHighPowerUp_Type()
)
pm20020maAlmCfpHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpHighPowerUp.setStatus("current")
_Pm20020maAlmCfpTxOff_Type = EkiOnOff
_Pm20020maAlmCfpTxOff_Object = MibScalar
pm20020maAlmCfpTxOff = _Pm20020maAlmCfpTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 4),
    _Pm20020maAlmCfpTxOff_Type()
)
pm20020maAlmCfpTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxOff.setStatus("current")
_Pm20020maAlmCfpTxTurnOn_Type = EkiOnOff
_Pm20020maAlmCfpTxTurnOn_Object = MibScalar
pm20020maAlmCfpTxTurnOn = _Pm20020maAlmCfpTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 5),
    _Pm20020maAlmCfpTxTurnOn_Type()
)
pm20020maAlmCfpTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxTurnOn.setStatus("current")
_Pm20020maAlmCfpReady_Type = EkiOnOff
_Pm20020maAlmCfpReady_Object = MibScalar
pm20020maAlmCfpReady = _Pm20020maAlmCfpReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 6),
    _Pm20020maAlmCfpReady_Type()
)
pm20020maAlmCfpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpReady.setStatus("current")
_Pm20020maAlmCfpFault_Type = EkiOnOff
_Pm20020maAlmCfpFault_Object = MibScalar
pm20020maAlmCfpFault = _Pm20020maAlmCfpFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 7),
    _Pm20020maAlmCfpFault_Type()
)
pm20020maAlmCfpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpFault.setStatus("current")
_Pm20020maAlmCfpTxTurnOff_Type = EkiOnOff
_Pm20020maAlmCfpTxTurnOff_Object = MibScalar
pm20020maAlmCfpTxTurnOff = _Pm20020maAlmCfpTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 8),
    _Pm20020maAlmCfpTxTurnOff_Type()
)
pm20020maAlmCfpTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxTurnOff.setStatus("current")
_Pm20020maAlmCfpHighPowerDown_Type = EkiOnOff
_Pm20020maAlmCfpHighPowerDown_Object = MibScalar
pm20020maAlmCfpHighPowerDown = _Pm20020maAlmCfpHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 72, 9),
    _Pm20020maAlmCfpHighPowerDown_Type()
)
pm20020maAlmCfpHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpHighPowerDown.setStatus("current")
_Pm20020maAlmclientModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm20020maAlmclientModuleGeneralStatus = _Pm20020maAlmclientModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73)
)
_Pm20020maAlmCfpOutOfAlignment_Type = EkiOnOff
_Pm20020maAlmCfpOutOfAlignment_Object = MibScalar
pm20020maAlmCfpOutOfAlignment = _Pm20020maAlmCfpOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 4),
    _Pm20020maAlmCfpOutOfAlignment_Type()
)
pm20020maAlmCfpOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpOutOfAlignment.setStatus("current")
_Pm20020maAlmCfpRxNetworkLol_Type = EkiOnOff
_Pm20020maAlmCfpRxNetworkLol_Object = MibScalar
pm20020maAlmCfpRxNetworkLol = _Pm20020maAlmCfpRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 5),
    _Pm20020maAlmCfpRxNetworkLol_Type()
)
pm20020maAlmCfpRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpRxNetworkLol.setStatus("current")
_Pm20020maAlmCfpRxLos_Type = EkiOnOff
_Pm20020maAlmCfpRxLos_Object = MibScalar
pm20020maAlmCfpRxLos = _Pm20020maAlmCfpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 6),
    _Pm20020maAlmCfpRxLos_Type()
)
pm20020maAlmCfpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpRxLos.setStatus("current")
_Pm20020maAlmCfpTxHostLol_Type = EkiOnOff
_Pm20020maAlmCfpTxHostLol_Object = MibScalar
pm20020maAlmCfpTxHostLol = _Pm20020maAlmCfpTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 7),
    _Pm20020maAlmCfpTxHostLol_Type()
)
pm20020maAlmCfpTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxHostLol.setStatus("current")
_Pm20020maAlmCfpTxLosf_Type = EkiOnOff
_Pm20020maAlmCfpTxLosf_Object = MibScalar
pm20020maAlmCfpTxLosf = _Pm20020maAlmCfpTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 8),
    _Pm20020maAlmCfpTxLosf_Type()
)
pm20020maAlmCfpTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxLosf.setStatus("current")
_Pm20020maAlmCfpTxCmuLol_Type = EkiOnOff
_Pm20020maAlmCfpTxCmuLol_Object = MibScalar
pm20020maAlmCfpTxCmuLol = _Pm20020maAlmCfpTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 9),
    _Pm20020maAlmCfpTxCmuLol_Type()
)
pm20020maAlmCfpTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxCmuLol.setStatus("current")
_Pm20020maAlmCfpTxJitterPllLol_Type = EkiOnOff
_Pm20020maAlmCfpTxJitterPllLol_Object = MibScalar
pm20020maAlmCfpTxJitterPllLol = _Pm20020maAlmCfpTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 10),
    _Pm20020maAlmCfpTxJitterPllLol_Type()
)
pm20020maAlmCfpTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpTxJitterPllLol.setStatus("current")
_Pm20020maAlmCfpLossOfRefclk_Type = EkiOnOff
_Pm20020maAlmCfpLossOfRefclk_Object = MibScalar
pm20020maAlmCfpLossOfRefclk = _Pm20020maAlmCfpLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 11),
    _Pm20020maAlmCfpLossOfRefclk_Type()
)
pm20020maAlmCfpLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpLossOfRefclk.setStatus("current")
_Pm20020maAlmCfpHwInterlock_Type = EkiOnOff
_Pm20020maAlmCfpHwInterlock_Object = MibScalar
pm20020maAlmCfpHwInterlock = _Pm20020maAlmCfpHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 73, 14),
    _Pm20020maAlmCfpHwInterlock_Type()
)
pm20020maAlmCfpHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpHwInterlock.setStatus("current")
_Pm20020maAlmclientGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm20020maAlmclientGlobalAlarmSummary = _Pm20020maAlmclientGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74)
)
_Pm20020maAlmCfpSoftGlobAlarmTest_Type = EkiOnOff
_Pm20020maAlmCfpSoftGlobAlarmTest_Object = MibScalar
pm20020maAlmCfpSoftGlobAlarmTest = _Pm20020maAlmCfpSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 1),
    _Pm20020maAlmCfpSoftGlobAlarmTest_Type()
)
pm20020maAlmCfpSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpSoftGlobAlarmTest.setStatus("current")
_Pm20020maAlmCfpNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm20020maAlmCfpNetworkLaneAlarmWarning2_Object = MibScalar
pm20020maAlmCfpNetworkLaneAlarmWarning2 = _Pm20020maAlmCfpNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 7),
    _Pm20020maAlmCfpNetworkLaneAlarmWarning2_Type()
)
pm20020maAlmCfpNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpNetworkLaneAlarmWarning2.setStatus("current")
_Pm20020maAlmCfpModuleState_Type = EkiOnOff
_Pm20020maAlmCfpModuleState_Object = MibScalar
pm20020maAlmCfpModuleState = _Pm20020maAlmCfpModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 8),
    _Pm20020maAlmCfpModuleState_Type()
)
pm20020maAlmCfpModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpModuleState.setStatus("current")
_Pm20020maAlmCfpModuleGeneralStatus_Type = EkiOnOff
_Pm20020maAlmCfpModuleGeneralStatus_Object = MibScalar
pm20020maAlmCfpModuleGeneralStatus = _Pm20020maAlmCfpModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 9),
    _Pm20020maAlmCfpModuleGeneralStatus_Type()
)
pm20020maAlmCfpModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpModuleGeneralStatus.setStatus("current")
_Pm20020maAlmCfpModuleFault_Type = EkiOnOff
_Pm20020maAlmCfpModuleFault_Object = MibScalar
pm20020maAlmCfpModuleFault = _Pm20020maAlmCfpModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 10),
    _Pm20020maAlmCfpModuleFault_Type()
)
pm20020maAlmCfpModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpModuleFault.setStatus("current")
_Pm20020maAlmCfpModuleAlarmWarning1_Type = EkiOnOff
_Pm20020maAlmCfpModuleAlarmWarning1_Object = MibScalar
pm20020maAlmCfpModuleAlarmWarning1 = _Pm20020maAlmCfpModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 11),
    _Pm20020maAlmCfpModuleAlarmWarning1_Type()
)
pm20020maAlmCfpModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpModuleAlarmWarning1.setStatus("current")
_Pm20020maAlmCfpModuleAlarmWarning2_Type = EkiOnOff
_Pm20020maAlmCfpModuleAlarmWarning2_Object = MibScalar
pm20020maAlmCfpModuleAlarmWarning2 = _Pm20020maAlmCfpModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 12),
    _Pm20020maAlmCfpModuleAlarmWarning2_Type()
)
pm20020maAlmCfpModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpModuleAlarmWarning2.setStatus("current")
_Pm20020maAlmCfpNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm20020maAlmCfpNetworkLaneAlarmWarning1_Object = MibScalar
pm20020maAlmCfpNetworkLaneAlarmWarning1 = _Pm20020maAlmCfpNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 13),
    _Pm20020maAlmCfpNetworkLaneAlarmWarning1_Type()
)
pm20020maAlmCfpNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpNetworkLaneAlarmWarning1.setStatus("current")
_Pm20020maAlmCfpNetworkLaneFaultStatus_Type = EkiOnOff
_Pm20020maAlmCfpNetworkLaneFaultStatus_Object = MibScalar
pm20020maAlmCfpNetworkLaneFaultStatus = _Pm20020maAlmCfpNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 14),
    _Pm20020maAlmCfpNetworkLaneFaultStatus_Type()
)
pm20020maAlmCfpNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpNetworkLaneFaultStatus.setStatus("current")
_Pm20020maAlmCfpHostLaneFaultStatus_Type = EkiOnOff
_Pm20020maAlmCfpHostLaneFaultStatus_Object = MibScalar
pm20020maAlmCfpHostLaneFaultStatus = _Pm20020maAlmCfpHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 15),
    _Pm20020maAlmCfpHostLaneFaultStatus_Type()
)
pm20020maAlmCfpHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpHostLaneFaultStatus.setStatus("current")
_Pm20020maAlmCfpGlobAlarmAssertion_Type = EkiOnOff
_Pm20020maAlmCfpGlobAlarmAssertion_Object = MibScalar
pm20020maAlmCfpGlobAlarmAssertion = _Pm20020maAlmCfpGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 74, 16),
    _Pm20020maAlmCfpGlobAlarmAssertion_Type()
)
pm20020maAlmCfpGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmCfpGlobAlarmAssertion.setStatus("current")
_Pm20020maAlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaModuleState = _Pm20020maAlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78)
)
_Pm20020maAlmMsaInitialize_Type = EkiOnOff
_Pm20020maAlmMsaInitialize_Object = MibScalar
pm20020maAlmMsaInitialize = _Pm20020maAlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 1),
    _Pm20020maAlmMsaInitialize_Type()
)
pm20020maAlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaInitialize.setStatus("current")
_Pm20020maAlmMsaLowPower_Type = EkiOnOff
_Pm20020maAlmMsaLowPower_Object = MibScalar
pm20020maAlmMsaLowPower = _Pm20020maAlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 2),
    _Pm20020maAlmMsaLowPower_Type()
)
pm20020maAlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaLowPower.setStatus("current")
_Pm20020maAlmMsaHighPowerUp_Type = EkiOnOff
_Pm20020maAlmMsaHighPowerUp_Object = MibScalar
pm20020maAlmMsaHighPowerUp = _Pm20020maAlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 3),
    _Pm20020maAlmMsaHighPowerUp_Type()
)
pm20020maAlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaHighPowerUp.setStatus("current")
_Pm20020maAlmMsaTxOff_Type = EkiOnOff
_Pm20020maAlmMsaTxOff_Object = MibScalar
pm20020maAlmMsaTxOff = _Pm20020maAlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 4),
    _Pm20020maAlmMsaTxOff_Type()
)
pm20020maAlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxOff.setStatus("current")
_Pm20020maAlmMsaTxTurnOn_Type = EkiOnOff
_Pm20020maAlmMsaTxTurnOn_Object = MibScalar
pm20020maAlmMsaTxTurnOn = _Pm20020maAlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 5),
    _Pm20020maAlmMsaTxTurnOn_Type()
)
pm20020maAlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxTurnOn.setStatus("current")
_Pm20020maAlmMsaReady_Type = EkiOnOff
_Pm20020maAlmMsaReady_Object = MibScalar
pm20020maAlmMsaReady = _Pm20020maAlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 6),
    _Pm20020maAlmMsaReady_Type()
)
pm20020maAlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaReady.setStatus("current")
_Pm20020maAlmMsaFault_Type = EkiOnOff
_Pm20020maAlmMsaFault_Object = MibScalar
pm20020maAlmMsaFault = _Pm20020maAlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 7),
    _Pm20020maAlmMsaFault_Type()
)
pm20020maAlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaFault.setStatus("current")
_Pm20020maAlmMsaTxTurnOff_Type = EkiOnOff
_Pm20020maAlmMsaTxTurnOff_Object = MibScalar
pm20020maAlmMsaTxTurnOff = _Pm20020maAlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 8),
    _Pm20020maAlmMsaTxTurnOff_Type()
)
pm20020maAlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxTurnOff.setStatus("current")
_Pm20020maAlmMsaHighPowerDown_Type = EkiOnOff
_Pm20020maAlmMsaHighPowerDown_Object = MibScalar
pm20020maAlmMsaHighPowerDown = _Pm20020maAlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 78, 9),
    _Pm20020maAlmMsaHighPowerDown_Type()
)
pm20020maAlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaHighPowerDown.setStatus("current")
_Pm20020maAlmmsaModuleGeneralStatus_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaModuleGeneralStatus = _Pm20020maAlmmsaModuleGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79)
)
_Pm20020maAlmMsaOutOfAlignment_Type = EkiOnOff
_Pm20020maAlmMsaOutOfAlignment_Object = MibScalar
pm20020maAlmMsaOutOfAlignment = _Pm20020maAlmMsaOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 4),
    _Pm20020maAlmMsaOutOfAlignment_Type()
)
pm20020maAlmMsaOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaOutOfAlignment.setStatus("current")
_Pm20020maAlmMsaRxNetworkLol_Type = EkiOnOff
_Pm20020maAlmMsaRxNetworkLol_Object = MibScalar
pm20020maAlmMsaRxNetworkLol = _Pm20020maAlmMsaRxNetworkLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 5),
    _Pm20020maAlmMsaRxNetworkLol_Type()
)
pm20020maAlmMsaRxNetworkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaRxNetworkLol.setStatus("current")
_Pm20020maAlmMsaRxLos_Type = EkiOnOff
_Pm20020maAlmMsaRxLos_Object = MibScalar
pm20020maAlmMsaRxLos = _Pm20020maAlmMsaRxLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 6),
    _Pm20020maAlmMsaRxLos_Type()
)
pm20020maAlmMsaRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaRxLos.setStatus("current")
_Pm20020maAlmMsaTxHostLol_Type = EkiOnOff
_Pm20020maAlmMsaTxHostLol_Object = MibScalar
pm20020maAlmMsaTxHostLol = _Pm20020maAlmMsaTxHostLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 7),
    _Pm20020maAlmMsaTxHostLol_Type()
)
pm20020maAlmMsaTxHostLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxHostLol.setStatus("current")
_Pm20020maAlmMsaTxLosf_Type = EkiOnOff
_Pm20020maAlmMsaTxLosf_Object = MibScalar
pm20020maAlmMsaTxLosf = _Pm20020maAlmMsaTxLosf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 8),
    _Pm20020maAlmMsaTxLosf_Type()
)
pm20020maAlmMsaTxLosf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxLosf.setStatus("current")
_Pm20020maAlmMsaTxCmuLol_Type = EkiOnOff
_Pm20020maAlmMsaTxCmuLol_Object = MibScalar
pm20020maAlmMsaTxCmuLol = _Pm20020maAlmMsaTxCmuLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 9),
    _Pm20020maAlmMsaTxCmuLol_Type()
)
pm20020maAlmMsaTxCmuLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxCmuLol.setStatus("current")
_Pm20020maAlmMsaTxJitterPllLol_Type = EkiOnOff
_Pm20020maAlmMsaTxJitterPllLol_Object = MibScalar
pm20020maAlmMsaTxJitterPllLol = _Pm20020maAlmMsaTxJitterPllLol_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 10),
    _Pm20020maAlmMsaTxJitterPllLol_Type()
)
pm20020maAlmMsaTxJitterPllLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaTxJitterPllLol.setStatus("current")
_Pm20020maAlmMsaLossOfRefclk_Type = EkiOnOff
_Pm20020maAlmMsaLossOfRefclk_Object = MibScalar
pm20020maAlmMsaLossOfRefclk = _Pm20020maAlmMsaLossOfRefclk_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 11),
    _Pm20020maAlmMsaLossOfRefclk_Type()
)
pm20020maAlmMsaLossOfRefclk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaLossOfRefclk.setStatus("current")
_Pm20020maAlmMsaHwInterlock_Type = EkiOnOff
_Pm20020maAlmMsaHwInterlock_Object = MibScalar
pm20020maAlmMsaHwInterlock = _Pm20020maAlmMsaHwInterlock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 79, 14),
    _Pm20020maAlmMsaHwInterlock_Type()
)
pm20020maAlmMsaHwInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaHwInterlock.setStatus("current")
_Pm20020maAlmmsaGlobalAlarmSummary_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaGlobalAlarmSummary = _Pm20020maAlmmsaGlobalAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80)
)
_Pm20020maAlmMsaSoftGlobAlarmTest_Type = EkiOnOff
_Pm20020maAlmMsaSoftGlobAlarmTest_Object = MibScalar
pm20020maAlmMsaSoftGlobAlarmTest = _Pm20020maAlmMsaSoftGlobAlarmTest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 1),
    _Pm20020maAlmMsaSoftGlobAlarmTest_Type()
)
pm20020maAlmMsaSoftGlobAlarmTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaSoftGlobAlarmTest.setStatus("current")
_Pm20020maAlmMsaNetworkHostAlarmStatus_Type = EkiOnOff
_Pm20020maAlmMsaNetworkHostAlarmStatus_Object = MibScalar
pm20020maAlmMsaNetworkHostAlarmStatus = _Pm20020maAlmMsaNetworkHostAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 6),
    _Pm20020maAlmMsaNetworkHostAlarmStatus_Type()
)
pm20020maAlmMsaNetworkHostAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaNetworkHostAlarmStatus.setStatus("current")
_Pm20020maAlmMsaNetworkLaneAlarmWarning2_Type = EkiOnOff
_Pm20020maAlmMsaNetworkLaneAlarmWarning2_Object = MibScalar
pm20020maAlmMsaNetworkLaneAlarmWarning2 = _Pm20020maAlmMsaNetworkLaneAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 7),
    _Pm20020maAlmMsaNetworkLaneAlarmWarning2_Type()
)
pm20020maAlmMsaNetworkLaneAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaNetworkLaneAlarmWarning2.setStatus("current")
_Pm20020maAlmMsaModuleState_Type = EkiOnOff
_Pm20020maAlmMsaModuleState_Object = MibScalar
pm20020maAlmMsaModuleState = _Pm20020maAlmMsaModuleState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 8),
    _Pm20020maAlmMsaModuleState_Type()
)
pm20020maAlmMsaModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaModuleState.setStatus("current")
_Pm20020maAlmMsaModuleGeneralStatus_Type = EkiOnOff
_Pm20020maAlmMsaModuleGeneralStatus_Object = MibScalar
pm20020maAlmMsaModuleGeneralStatus = _Pm20020maAlmMsaModuleGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 9),
    _Pm20020maAlmMsaModuleGeneralStatus_Type()
)
pm20020maAlmMsaModuleGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaModuleGeneralStatus.setStatus("current")
_Pm20020maAlmModuleFault_Type = EkiOnOff
_Pm20020maAlmModuleFault_Object = MibScalar
pm20020maAlmModuleFault = _Pm20020maAlmModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 10),
    _Pm20020maAlmModuleFault_Type()
)
pm20020maAlmModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmModuleFault.setStatus("current")
_Pm20020maAlmMsaModuleAlarmWarning1_Type = EkiOnOff
_Pm20020maAlmMsaModuleAlarmWarning1_Object = MibScalar
pm20020maAlmMsaModuleAlarmWarning1 = _Pm20020maAlmMsaModuleAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 11),
    _Pm20020maAlmMsaModuleAlarmWarning1_Type()
)
pm20020maAlmMsaModuleAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaModuleAlarmWarning1.setStatus("current")
_Pm20020maAlmMsaModuleAlarmWarning2_Type = EkiOnOff
_Pm20020maAlmMsaModuleAlarmWarning2_Object = MibScalar
pm20020maAlmMsaModuleAlarmWarning2 = _Pm20020maAlmMsaModuleAlarmWarning2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 12),
    _Pm20020maAlmMsaModuleAlarmWarning2_Type()
)
pm20020maAlmMsaModuleAlarmWarning2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaModuleAlarmWarning2.setStatus("current")
_Pm20020maAlmMsaNetworkLaneAlarmWarning1_Type = EkiOnOff
_Pm20020maAlmMsaNetworkLaneAlarmWarning1_Object = MibScalar
pm20020maAlmMsaNetworkLaneAlarmWarning1 = _Pm20020maAlmMsaNetworkLaneAlarmWarning1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 13),
    _Pm20020maAlmMsaNetworkLaneAlarmWarning1_Type()
)
pm20020maAlmMsaNetworkLaneAlarmWarning1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaNetworkLaneAlarmWarning1.setStatus("current")
_Pm20020maAlmMsaNetworkLaneFaultStatus_Type = EkiOnOff
_Pm20020maAlmMsaNetworkLaneFaultStatus_Object = MibScalar
pm20020maAlmMsaNetworkLaneFaultStatus = _Pm20020maAlmMsaNetworkLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 14),
    _Pm20020maAlmMsaNetworkLaneFaultStatus_Type()
)
pm20020maAlmMsaNetworkLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaNetworkLaneFaultStatus.setStatus("current")
_Pm20020maAlmMsaHostLaneFaultStatus_Type = EkiOnOff
_Pm20020maAlmMsaHostLaneFaultStatus_Object = MibScalar
pm20020maAlmMsaHostLaneFaultStatus = _Pm20020maAlmMsaHostLaneFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 15),
    _Pm20020maAlmMsaHostLaneFaultStatus_Type()
)
pm20020maAlmMsaHostLaneFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaHostLaneFaultStatus.setStatus("current")
_Pm20020maAlmMsaGlobAlarmAssertion_Type = EkiOnOff
_Pm20020maAlmMsaGlobAlarmAssertion_Object = MibScalar
pm20020maAlmMsaGlobAlarmAssertion = _Pm20020maAlmMsaGlobAlarmAssertion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 80, 16),
    _Pm20020maAlmMsaGlobAlarmAssertion_Type()
)
pm20020maAlmMsaGlobAlarmAssertion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmMsaGlobAlarmAssertion.setStatus("current")
_Pm20020maAlmmsaNetworkTxAlignment_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaNetworkTxAlignment = _Pm20020maAlmmsaNetworkTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 81)
)
_Pm20020maAlmNetTxTimingFault_Type = EkiOnOff
_Pm20020maAlmNetTxTimingFault_Object = MibScalar
pm20020maAlmNetTxTimingFault = _Pm20020maAlmNetTxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 81, 12),
    _Pm20020maAlmNetTxTimingFault_Type()
)
pm20020maAlmNetTxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetTxTimingFault.setStatus("current")
_Pm20020maAlmNetTxReferenceClockFault_Type = EkiOnOff
_Pm20020maAlmNetTxReferenceClockFault_Object = MibScalar
pm20020maAlmNetTxReferenceClockFault = _Pm20020maAlmNetTxReferenceClockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 81, 13),
    _Pm20020maAlmNetTxReferenceClockFault_Type()
)
pm20020maAlmNetTxReferenceClockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetTxReferenceClockFault.setStatus("current")
_Pm20020maAlmNetTxCmuLockFault_Type = EkiOnOff
_Pm20020maAlmNetTxCmuLockFault_Object = MibScalar
pm20020maAlmNetTxCmuLockFault = _Pm20020maAlmNetTxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 81, 14),
    _Pm20020maAlmNetTxCmuLockFault_Type()
)
pm20020maAlmNetTxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetTxCmuLockFault.setStatus("current")
_Pm20020maAlmNetTxOutOfAlignment_Type = EkiOnOff
_Pm20020maAlmNetTxOutOfAlignment_Object = MibScalar
pm20020maAlmNetTxOutOfAlignment = _Pm20020maAlmNetTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 81, 15),
    _Pm20020maAlmNetTxOutOfAlignment_Type()
)
pm20020maAlmNetTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetTxOutOfAlignment.setStatus("current")
_Pm20020maAlmNetTxLossOfAlignment_Type = EkiOnOff
_Pm20020maAlmNetTxLossOfAlignment_Object = MibScalar
pm20020maAlmNetTxLossOfAlignment = _Pm20020maAlmNetTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 81, 16),
    _Pm20020maAlmNetTxLossOfAlignment_Type()
)
pm20020maAlmNetTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetTxLossOfAlignment.setStatus("current")
_Pm20020maAlmmsaNetworkRxAlignment_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaNetworkRxAlignment = _Pm20020maAlmmsaNetworkRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 82)
)
_Pm20020maAlmNetRxTimingFault_Type = EkiOnOff
_Pm20020maAlmNetRxTimingFault_Object = MibScalar
pm20020maAlmNetRxTimingFault = _Pm20020maAlmNetRxTimingFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 82, 12),
    _Pm20020maAlmNetRxTimingFault_Type()
)
pm20020maAlmNetRxTimingFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetRxTimingFault.setStatus("current")
_Pm20020maAlmNetRxOutOfAlignment_Type = EkiOnOff
_Pm20020maAlmNetRxOutOfAlignment_Object = MibScalar
pm20020maAlmNetRxOutOfAlignment = _Pm20020maAlmNetRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 82, 13),
    _Pm20020maAlmNetRxOutOfAlignment_Type()
)
pm20020maAlmNetRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetRxOutOfAlignment.setStatus("current")
_Pm20020maAlmNetRxLossOfAlignment_Type = EkiOnOff
_Pm20020maAlmNetRxLossOfAlignment_Object = MibScalar
pm20020maAlmNetRxLossOfAlignment = _Pm20020maAlmNetRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 82, 14),
    _Pm20020maAlmNetRxLossOfAlignment_Type()
)
pm20020maAlmNetRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetRxLossOfAlignment.setStatus("current")
_Pm20020maAlmNetRxModemLockFault_Type = EkiOnOff
_Pm20020maAlmNetRxModemLockFault_Object = MibScalar
pm20020maAlmNetRxModemLockFault = _Pm20020maAlmNetRxModemLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 82, 15),
    _Pm20020maAlmNetRxModemLockFault_Type()
)
pm20020maAlmNetRxModemLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetRxModemLockFault.setStatus("current")
_Pm20020maAlmNetRxModemSyncDetectFault_Type = EkiOnOff
_Pm20020maAlmNetRxModemSyncDetectFault_Object = MibScalar
pm20020maAlmNetRxModemSyncDetectFault = _Pm20020maAlmNetRxModemSyncDetectFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 82, 16),
    _Pm20020maAlmNetRxModemSyncDetectFault_Type()
)
pm20020maAlmNetRxModemSyncDetectFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetRxModemSyncDetectFault.setStatus("current")
_Pm20020maAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaNetworkHostNetworkAlarmSummary = _Pm20020maAlmmsaNetworkHostNetworkAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83)
)
_Pm20020maAlmNetworkTxAlignment_Type = EkiOnOff
_Pm20020maAlmNetworkTxAlignment_Object = MibScalar
pm20020maAlmNetworkTxAlignment = _Pm20020maAlmNetworkTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83, 11),
    _Pm20020maAlmNetworkTxAlignment_Type()
)
pm20020maAlmNetworkTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetworkTxAlignment.setStatus("current")
_Pm20020maAlmNetworkRxAlignment_Type = EkiOnOff
_Pm20020maAlmNetworkRxAlignment_Object = MibScalar
pm20020maAlmNetworkRxAlignment = _Pm20020maAlmNetworkRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83, 12),
    _Pm20020maAlmNetworkRxAlignment_Type()
)
pm20020maAlmNetworkRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetworkRxAlignment.setStatus("current")
_Pm20020maAlmNetworkRxOtn_Type = EkiOnOff
_Pm20020maAlmNetworkRxOtn_Object = MibScalar
pm20020maAlmNetworkRxOtn = _Pm20020maAlmNetworkRxOtn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83, 13),
    _Pm20020maAlmNetworkRxOtn_Type()
)
pm20020maAlmNetworkRxOtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmNetworkRxOtn.setStatus("current")
_Pm20020maAlmHostRxAlignment_Type = EkiOnOff
_Pm20020maAlmHostRxAlignment_Object = MibScalar
pm20020maAlmHostRxAlignment = _Pm20020maAlmHostRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83, 14),
    _Pm20020maAlmHostRxAlignment_Type()
)
pm20020maAlmHostRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostRxAlignment.setStatus("current")
_Pm20020maAlmHostTxAlignment_Type = EkiOnOff
_Pm20020maAlmHostTxAlignment_Object = MibScalar
pm20020maAlmHostTxAlignment = _Pm20020maAlmHostTxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83, 15),
    _Pm20020maAlmHostTxAlignment_Type()
)
pm20020maAlmHostTxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostTxAlignment.setStatus("current")
_Pm20020maAlmHostTxOtnStatus_Type = EkiOnOff
_Pm20020maAlmHostTxOtnStatus_Object = MibScalar
pm20020maAlmHostTxOtnStatus = _Pm20020maAlmHostTxOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 83, 16),
    _Pm20020maAlmHostTxOtnStatus_Type()
)
pm20020maAlmHostTxOtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostTxOtnStatus.setStatus("current")
_Pm20020maAlmmsaHostTxAlignment_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaHostTxAlignment = _Pm20020maAlmmsaHostTxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 84)
)
_Pm20020maAlmHostTxDeskewLockFault_Type = EkiOnOff
_Pm20020maAlmHostTxDeskewLockFault_Object = MibScalar
pm20020maAlmHostTxDeskewLockFault = _Pm20020maAlmHostTxDeskewLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 84, 13),
    _Pm20020maAlmHostTxDeskewLockFault_Type()
)
pm20020maAlmHostTxDeskewLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostTxDeskewLockFault.setStatus("current")
_Pm20020maAlmHostTxOutOfAlignment_Type = EkiOnOff
_Pm20020maAlmHostTxOutOfAlignment_Object = MibScalar
pm20020maAlmHostTxOutOfAlignment = _Pm20020maAlmHostTxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 84, 14),
    _Pm20020maAlmHostTxOutOfAlignment_Type()
)
pm20020maAlmHostTxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostTxOutOfAlignment.setStatus("current")
_Pm20020maAlmHostTxLossOfAlignment_Type = EkiOnOff
_Pm20020maAlmHostTxLossOfAlignment_Object = MibScalar
pm20020maAlmHostTxLossOfAlignment = _Pm20020maAlmHostTxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 84, 15),
    _Pm20020maAlmHostTxLossOfAlignment_Type()
)
pm20020maAlmHostTxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostTxLossOfAlignment.setStatus("current")
_Pm20020maAlmHostTxCdrLockFault_Type = EkiOnOff
_Pm20020maAlmHostTxCdrLockFault_Object = MibScalar
pm20020maAlmHostTxCdrLockFault = _Pm20020maAlmHostTxCdrLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 84, 16),
    _Pm20020maAlmHostTxCdrLockFault_Type()
)
pm20020maAlmHostTxCdrLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostTxCdrLockFault.setStatus("current")
_Pm20020maAlmmsaHostRxAlignment_ObjectIdentity = ObjectIdentity
pm20020maAlmmsaHostRxAlignment = _Pm20020maAlmmsaHostRxAlignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 85)
)
_Pm20020maAlmHostRxCmuLockFault_Type = EkiOnOff
_Pm20020maAlmHostRxCmuLockFault_Object = MibScalar
pm20020maAlmHostRxCmuLockFault = _Pm20020maAlmHostRxCmuLockFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 85, 14),
    _Pm20020maAlmHostRxCmuLockFault_Type()
)
pm20020maAlmHostRxCmuLockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostRxCmuLockFault.setStatus("current")
_Pm20020maAlmHostRxOutOfAlignment_Type = EkiOnOff
_Pm20020maAlmHostRxOutOfAlignment_Object = MibScalar
pm20020maAlmHostRxOutOfAlignment = _Pm20020maAlmHostRxOutOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 85, 15),
    _Pm20020maAlmHostRxOutOfAlignment_Type()
)
pm20020maAlmHostRxOutOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostRxOutOfAlignment.setStatus("current")
_Pm20020maAlmHostRxLossOfAlignment_Type = EkiOnOff
_Pm20020maAlmHostRxLossOfAlignment_Object = MibScalar
pm20020maAlmHostRxLossOfAlignment = _Pm20020maAlmHostRxLossOfAlignment_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 1, 3, 85, 16),
    _Pm20020maAlmHostRxLossOfAlignment_Type()
)
pm20020maAlmHostRxLossOfAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHostRxLossOfAlignment.setStatus("current")
_Pm20020maAlmClient_ObjectIdentity = ObjectIdentity
pm20020maAlmClient = _Pm20020maAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2)
)
_Pm20020maAlmClientNurg_ObjectIdentity = ObjectIdentity
pm20020maAlmClientNurg = _Pm20020maAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1)
)
_Pm20020maAlmclientNetworkLaneAlarmWarningTable_Object = MibTable
pm20020maAlmclientNetworkLaneAlarmWarningTable = _Pm20020maAlmclientNetworkLaneAlarmWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88)
)
if mibBuilder.loadTexts:
    pm20020maAlmclientNetworkLaneAlarmWarningTable.setStatus("current")
_Pm20020maAlmclientNetworkLaneAlarmWarningEntry_Object = MibTableRow
pm20020maAlmclientNetworkLaneAlarmWarningEntry = _Pm20020maAlmclientNetworkLaneAlarmWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1)
)
pm20020maAlmclientNetworkLaneAlarmWarningEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmclientNetworkLaneAlarmWarningIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmclientNetworkLaneAlarmWarningEntry.setStatus("current")


class _Pm20020maAlmclientNetworkLaneAlarmWarningIndex_Type(Integer32):
    """Custom type pm20020maAlmclientNetworkLaneAlarmWarningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmclientNetworkLaneAlarmWarningIndex_Type.__name__ = "Integer32"
_Pm20020maAlmclientNetworkLaneAlarmWarningIndex_Object = MibTableColumn
pm20020maAlmclientNetworkLaneAlarmWarningIndex = _Pm20020maAlmclientNetworkLaneAlarmWarningIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 1),
    _Pm20020maAlmclientNetworkLaneAlarmWarningIndex_Type()
)
pm20020maAlmclientNetworkLaneAlarmWarningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmclientNetworkLaneAlarmWarningIndex.setStatus("current")
_Pm20020maAlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pm20020maAlmClientRxPowerLowAlarmPortn = _Pm20020maAlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 2),
    _Pm20020maAlmClientRxPowerLowAlarmPortn_Type()
)
pm20020maAlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pm20020maAlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pm20020maAlmClientRxPowerLowWarningPortn = _Pm20020maAlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 3),
    _Pm20020maAlmClientRxPowerLowWarningPortn_Type()
)
pm20020maAlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientRxPowerLowWarningPortn.setStatus("current")
_Pm20020maAlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pm20020maAlmClientRxPowerHighWarningPortn = _Pm20020maAlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 4),
    _Pm20020maAlmClientRxPowerHighWarningPortn_Type()
)
pm20020maAlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientRxPowerHighWarningPortn.setStatus("current")
_Pm20020maAlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pm20020maAlmClientRxPowerHighAlarmPortn = _Pm20020maAlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 5),
    _Pm20020maAlmClientRxPowerHighAlarmPortn_Type()
)
pm20020maAlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pm20020maAlmLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLaserTempLowAlarmPortn_Object = MibTableColumn
pm20020maAlmLaserTempLowAlarmPortn = _Pm20020maAlmLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 6),
    _Pm20020maAlmLaserTempLowAlarmPortn_Type()
)
pm20020maAlmLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLaserTempLowAlarmPortn.setStatus("current")
_Pm20020maAlmClientLaserTempLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientLaserTempLowWarningPortn_Object = MibTableColumn
pm20020maAlmClientLaserTempLowWarningPortn = _Pm20020maAlmClientLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 7),
    _Pm20020maAlmClientLaserTempLowWarningPortn_Type()
)
pm20020maAlmClientLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaserTempLowWarningPortn.setStatus("current")
_Pm20020maAlmClientLaserTempHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientLaserTempHighWarningPortn_Object = MibTableColumn
pm20020maAlmClientLaserTempHighWarningPortn = _Pm20020maAlmClientLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 8),
    _Pm20020maAlmClientLaserTempHighWarningPortn_Type()
)
pm20020maAlmClientLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaserTempHighWarningPortn.setStatus("current")
_Pm20020maAlmClientLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientLaserTempHighAlarmPortn_Object = MibTableColumn
pm20020maAlmClientLaserTempHighAlarmPortn = _Pm20020maAlmClientLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 9),
    _Pm20020maAlmClientLaserTempHighAlarmPortn_Type()
)
pm20020maAlmClientLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaserTempHighAlarmPortn.setStatus("current")
_Pm20020maAlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pm20020maAlmClientTxPowerLowAlarmPortn = _Pm20020maAlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 10),
    _Pm20020maAlmClientTxPowerLowAlarmPortn_Type()
)
pm20020maAlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pm20020maAlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pm20020maAlmClientTxPowerLowWarningPortn = _Pm20020maAlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 11),
    _Pm20020maAlmClientTxPowerLowWarningPortn_Type()
)
pm20020maAlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientTxPowerLowWarningPortn.setStatus("current")
_Pm20020maAlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pm20020maAlmClientTxPowerHighWarningPortn = _Pm20020maAlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 12),
    _Pm20020maAlmClientTxPowerHighWarningPortn_Type()
)
pm20020maAlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientTxPowerHighWarningPortn.setStatus("current")
_Pm20020maAlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pm20020maAlmClientTxPowerHighAlarmPortn = _Pm20020maAlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 13),
    _Pm20020maAlmClientTxPowerHighAlarmPortn_Type()
)
pm20020maAlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pm20020maAlmClientBiasLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientBiasLowAlarmPortn_Object = MibTableColumn
pm20020maAlmClientBiasLowAlarmPortn = _Pm20020maAlmClientBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 14),
    _Pm20020maAlmClientBiasLowAlarmPortn_Type()
)
pm20020maAlmClientBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientBiasLowAlarmPortn.setStatus("current")
_Pm20020maAlmClientBiasLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientBiasLowWarningPortn_Object = MibTableColumn
pm20020maAlmClientBiasLowWarningPortn = _Pm20020maAlmClientBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 15),
    _Pm20020maAlmClientBiasLowWarningPortn_Type()
)
pm20020maAlmClientBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientBiasLowWarningPortn.setStatus("current")
_Pm20020maAlmClientBiasHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmClientBiasHighWarningPortn_Object = MibTableColumn
pm20020maAlmClientBiasHighWarningPortn = _Pm20020maAlmClientBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 16),
    _Pm20020maAlmClientBiasHighWarningPortn_Type()
)
pm20020maAlmClientBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientBiasHighWarningPortn.setStatus("current")
_Pm20020maAlmClientBiasHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmClientBiasHighAlarmPortn_Object = MibTableColumn
pm20020maAlmClientBiasHighAlarmPortn = _Pm20020maAlmClientBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 88, 1, 17),
    _Pm20020maAlmClientBiasHighAlarmPortn_Type()
)
pm20020maAlmClientBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientBiasHighAlarmPortn.setStatus("current")
_Pm20020maAlmclientSfpWarnDdmTable_Object = MibTable
pm20020maAlmclientSfpWarnDdmTable = _Pm20020maAlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272)
)
if mibBuilder.loadTexts:
    pm20020maAlmclientSfpWarnDdmTable.setStatus("current")
_Pm20020maAlmclientSfpWarnDdmEntry_Object = MibTableRow
pm20020maAlmclientSfpWarnDdmEntry = _Pm20020maAlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1)
)
pm20020maAlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmclientSfpWarnDdmEntry.setStatus("current")


class _Pm20020maAlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm20020maAlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm20020maAlmclientSfpWarnDdmIndex_Object = MibTableColumn
pm20020maAlmclientSfpWarnDdmIndex = _Pm20020maAlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 1),
    _Pm20020maAlmclientSfpWarnDdmIndex_Type()
)
pm20020maAlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmclientSfpWarnDdmIndex.setStatus("current")
_Pm20020maAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm20020maAlmTxPwLowWngPortn_Object = MibTableColumn
pm20020maAlmTxPwLowWngPortn = _Pm20020maAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 2),
    _Pm20020maAlmTxPwLowWngPortn_Type()
)
pm20020maAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxPwLowWngPortn.setStatus("current")
_Pm20020maAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm20020maAlmTxPwrHighWngPortn_Object = MibTableColumn
pm20020maAlmTxPwrHighWngPortn = _Pm20020maAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 3),
    _Pm20020maAlmTxPwrHighWngPortn_Type()
)
pm20020maAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxPwrHighWngPortn.setStatus("current")
_Pm20020maAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm20020maAlmTxBiasLowWngPortn_Object = MibTableColumn
pm20020maAlmTxBiasLowWngPortn = _Pm20020maAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 4),
    _Pm20020maAlmTxBiasLowWngPortn_Type()
)
pm20020maAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxBiasLowWngPortn.setStatus("current")
_Pm20020maAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm20020maAlmTxBiasHighWngPortn_Object = MibTableColumn
pm20020maAlmTxBiasHighWngPortn = _Pm20020maAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 5),
    _Pm20020maAlmTxBiasHighWngPortn_Type()
)
pm20020maAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxBiasHighWngPortn.setStatus("current")
_Pm20020maAlmVccLowWngPortn_Type = EkiOnOff
_Pm20020maAlmVccLowWngPortn_Object = MibTableColumn
pm20020maAlmVccLowWngPortn = _Pm20020maAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 6),
    _Pm20020maAlmVccLowWngPortn_Type()
)
pm20020maAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmVccLowWngPortn.setStatus("current")
_Pm20020maAlmVccHighWngPortn_Type = EkiOnOff
_Pm20020maAlmVccHighWngPortn_Object = MibTableColumn
pm20020maAlmVccHighWngPortn = _Pm20020maAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 7),
    _Pm20020maAlmVccHighWngPortn_Type()
)
pm20020maAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmVccHighWngPortn.setStatus("current")
_Pm20020maAlmTempLowWngPortn_Type = EkiOnOff
_Pm20020maAlmTempLowWngPortn_Object = MibTableColumn
pm20020maAlmTempLowWngPortn = _Pm20020maAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 8),
    _Pm20020maAlmTempLowWngPortn_Type()
)
pm20020maAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTempLowWngPortn.setStatus("current")
_Pm20020maAlmTempHighWngPortn_Type = EkiOnOff
_Pm20020maAlmTempHighWngPortn_Object = MibTableColumn
pm20020maAlmTempHighWngPortn = _Pm20020maAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 9),
    _Pm20020maAlmTempHighWngPortn_Type()
)
pm20020maAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTempHighWngPortn.setStatus("current")
_Pm20020maAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm20020maAlmRxPwrLowWngPortn_Object = MibTableColumn
pm20020maAlmRxPwrLowWngPortn = _Pm20020maAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 16),
    _Pm20020maAlmRxPwrLowWngPortn_Type()
)
pm20020maAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxPwrLowWngPortn.setStatus("current")
_Pm20020maAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm20020maAlmRxPwrHighWngPortn_Object = MibTableColumn
pm20020maAlmRxPwrHighWngPortn = _Pm20020maAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 1, 272, 1, 17),
    _Pm20020maAlmRxPwrHighWngPortn_Type()
)
pm20020maAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxPwrHighWngPortn.setStatus("current")
_Pm20020maAlmClientUrg_ObjectIdentity = ObjectIdentity
pm20020maAlmClientUrg = _Pm20020maAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2)
)
_Pm20020maAlmclientNetworkLaneFaultTable_Object = MibTable
pm20020maAlmclientNetworkLaneFaultTable = _Pm20020maAlmclientNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120)
)
if mibBuilder.loadTexts:
    pm20020maAlmclientNetworkLaneFaultTable.setStatus("current")
_Pm20020maAlmclientNetworkLaneFaultEntry_Object = MibTableRow
pm20020maAlmclientNetworkLaneFaultEntry = _Pm20020maAlmclientNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1)
)
pm20020maAlmclientNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmclientNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmclientNetworkLaneFaultEntry.setStatus("current")


class _Pm20020maAlmclientNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm20020maAlmclientNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmclientNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20020maAlmclientNetworkLaneFaultIndex_Object = MibTableColumn
pm20020maAlmclientNetworkLaneFaultIndex = _Pm20020maAlmclientNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 1),
    _Pm20020maAlmclientNetworkLaneFaultIndex_Type()
)
pm20020maAlmclientNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmclientNetworkLaneFaultIndex.setStatus("current")
_Pm20020maAlmClientLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneRxFifoErrorPortn_Object = MibTableColumn
pm20020maAlmClientLaneRxFifoErrorPortn = _Pm20020maAlmClientLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 4),
    _Pm20020maAlmClientLaneRxFifoErrorPortn_Type()
)
pm20020maAlmClientLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneRxFifoErrorPortn.setStatus("current")
_Pm20020maAlmClientLaneRxLolPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneRxLolPortn_Object = MibTableColumn
pm20020maAlmClientLaneRxLolPortn = _Pm20020maAlmClientLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 5),
    _Pm20020maAlmClientLaneRxLolPortn_Type()
)
pm20020maAlmClientLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneRxLolPortn.setStatus("current")
_Pm20020maAlmClientLaneRxLosPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneRxLosPortn_Object = MibTableColumn
pm20020maAlmClientLaneRxLosPortn = _Pm20020maAlmClientLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 6),
    _Pm20020maAlmClientLaneRxLosPortn_Type()
)
pm20020maAlmClientLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneRxLosPortn.setStatus("current")
_Pm20020maAlmClientLaneTxLolPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneTxLolPortn_Object = MibTableColumn
pm20020maAlmClientLaneTxLolPortn = _Pm20020maAlmClientLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 8),
    _Pm20020maAlmClientLaneTxLolPortn_Type()
)
pm20020maAlmClientLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneTxLolPortn.setStatus("current")
_Pm20020maAlmClientLaneTxLosfPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneTxLosfPortn_Object = MibTableColumn
pm20020maAlmClientLaneTxLosfPortn = _Pm20020maAlmClientLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 9),
    _Pm20020maAlmClientLaneTxLosfPortn_Type()
)
pm20020maAlmClientLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneTxLosfPortn.setStatus("current")
_Pm20020maAlmClientLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneApdPowerSupplyPortn_Object = MibTableColumn
pm20020maAlmClientLaneApdPowerSupplyPortn = _Pm20020maAlmClientLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 15),
    _Pm20020maAlmClientLaneApdPowerSupplyPortn_Type()
)
pm20020maAlmClientLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneApdPowerSupplyPortn.setStatus("current")
_Pm20020maAlmClientLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm20020maAlmClientLaneWavelengthUnlockedPortn = _Pm20020maAlmClientLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 16),
    _Pm20020maAlmClientLaneWavelengthUnlockedPortn_Type()
)
pm20020maAlmClientLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneWavelengthUnlockedPortn.setStatus("current")
_Pm20020maAlmClientLaneTecFaultPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneTecFaultPortn_Object = MibTableColumn
pm20020maAlmClientLaneTecFaultPortn = _Pm20020maAlmClientLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 120, 1, 17),
    _Pm20020maAlmClientLaneTecFaultPortn_Type()
)
pm20020maAlmClientLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneTecFaultPortn.setStatus("current")
_Pm20020maAlmclientHostLaneFaultTable_Object = MibTable
pm20020maAlmclientHostLaneFaultTable = _Pm20020maAlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152)
)
if mibBuilder.loadTexts:
    pm20020maAlmclientHostLaneFaultTable.setStatus("current")
_Pm20020maAlmclientHostLaneFaultEntry_Object = MibTableRow
pm20020maAlmclientHostLaneFaultEntry = _Pm20020maAlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1)
)
pm20020maAlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmclientHostLaneFaultEntry.setStatus("current")


class _Pm20020maAlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm20020maAlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20020maAlmclientHostLaneFaultIndex_Object = MibTableColumn
pm20020maAlmclientHostLaneFaultIndex = _Pm20020maAlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 1),
    _Pm20020maAlmclientHostLaneFaultIndex_Type()
)
pm20020maAlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmclientHostLaneFaultIndex.setStatus("current")
_Pm20020maAlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm20020maAlmClientLossOfSyncPortn_Object = MibTableColumn
pm20020maAlmClientLossOfSyncPortn = _Pm20020maAlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 2),
    _Pm20020maAlmClientLossOfSyncPortn_Type()
)
pm20020maAlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLossOfSyncPortn.setStatus("current")
_Pm20020maAlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm20020maAlmClientInputLossOfSigPortn_Object = MibTableColumn
pm20020maAlmClientInputLossOfSigPortn = _Pm20020maAlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 3),
    _Pm20020maAlmClientInputLossOfSigPortn_Type()
)
pm20020maAlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientInputLossOfSigPortn.setStatus("current")
_Pm20020maAlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm20020maAlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm20020maAlmClientLanesMarkerUnlockPortn = _Pm20020maAlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 4),
    _Pm20020maAlmClientLanesMarkerUnlockPortn_Type()
)
pm20020maAlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm20020maAlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm20020maAlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm20020maAlmClientLanes6466UnlockPortn = _Pm20020maAlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 5),
    _Pm20020maAlmClientLanes6466UnlockPortn_Type()
)
pm20020maAlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLanes6466UnlockPortn.setStatus("current")
_Pm20020maAlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm20020maAlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm20020maAlmClientLanesNotAlignedPortn = _Pm20020maAlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 6),
    _Pm20020maAlmClientLanesNotAlignedPortn_Type()
)
pm20020maAlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLanesNotAlignedPortn.setStatus("current")
_Pm20020maAlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm20020maAlmClientCsfDetectedPortn_Object = MibTableColumn
pm20020maAlmClientCsfDetectedPortn = _Pm20020maAlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 7),
    _Pm20020maAlmClientCsfDetectedPortn_Type()
)
pm20020maAlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientCsfDetectedPortn.setStatus("current")
_Pm20020maAlmClientTxHostLolPortn_Type = EkiOnOff
_Pm20020maAlmClientTxHostLolPortn_Object = MibTableColumn
pm20020maAlmClientTxHostLolPortn = _Pm20020maAlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 10),
    _Pm20020maAlmClientTxHostLolPortn_Type()
)
pm20020maAlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientTxHostLolPortn.setStatus("current")
_Pm20020maAlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm20020maAlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm20020maAlmClientLaneTxFifoErrorPortn = _Pm20020maAlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 152, 1, 11),
    _Pm20020maAlmClientLaneTxFifoErrorPortn_Type()
)
pm20020maAlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm20020maAlmclientSfpAlmDdmTable_Object = MibTable
pm20020maAlmclientSfpAlmDdmTable = _Pm20020maAlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240)
)
if mibBuilder.loadTexts:
    pm20020maAlmclientSfpAlmDdmTable.setStatus("current")
_Pm20020maAlmclientSfpAlmDdmEntry_Object = MibTableRow
pm20020maAlmclientSfpAlmDdmEntry = _Pm20020maAlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1)
)
pm20020maAlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmclientSfpAlmDdmEntry.setStatus("current")


class _Pm20020maAlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm20020maAlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm20020maAlmclientSfpAlmDdmIndex_Object = MibTableColumn
pm20020maAlmclientSfpAlmDdmIndex = _Pm20020maAlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 1),
    _Pm20020maAlmclientSfpAlmDdmIndex_Type()
)
pm20020maAlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmclientSfpAlmDdmIndex.setStatus("current")
_Pm20020maAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm20020maAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm20020maAlmTxPwrLowAlaPortn = _Pm20020maAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 2),
    _Pm20020maAlmTxPwrLowAlaPortn_Type()
)
pm20020maAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxPwrLowAlaPortn.setStatus("current")
_Pm20020maAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm20020maAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm20020maAlmTxPwrHighAlaPortn = _Pm20020maAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 3),
    _Pm20020maAlmTxPwrHighAlaPortn_Type()
)
pm20020maAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxPwrHighAlaPortn.setStatus("current")
_Pm20020maAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm20020maAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm20020maAlmTxBiasLowAlaPortn = _Pm20020maAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 4),
    _Pm20020maAlmTxBiasLowAlaPortn_Type()
)
pm20020maAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxBiasLowAlaPortn.setStatus("current")
_Pm20020maAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm20020maAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm20020maAlmTxBiasHighAlaPortn = _Pm20020maAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 5),
    _Pm20020maAlmTxBiasHighAlaPortn_Type()
)
pm20020maAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxBiasHighAlaPortn.setStatus("current")
_Pm20020maAlmVccLowAlaPortn_Type = EkiOnOff
_Pm20020maAlmVccLowAlaPortn_Object = MibTableColumn
pm20020maAlmVccLowAlaPortn = _Pm20020maAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 6),
    _Pm20020maAlmVccLowAlaPortn_Type()
)
pm20020maAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmVccLowAlaPortn.setStatus("current")
_Pm20020maAlmVccHighAlaPortn_Type = EkiOnOff
_Pm20020maAlmVccHighAlaPortn_Object = MibTableColumn
pm20020maAlmVccHighAlaPortn = _Pm20020maAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 7),
    _Pm20020maAlmVccHighAlaPortn_Type()
)
pm20020maAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmVccHighAlaPortn.setStatus("current")
_Pm20020maAlmTempLowAlaPortn_Type = EkiOnOff
_Pm20020maAlmTempLowAlaPortn_Object = MibTableColumn
pm20020maAlmTempLowAlaPortn = _Pm20020maAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 8),
    _Pm20020maAlmTempLowAlaPortn_Type()
)
pm20020maAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTempLowAlaPortn.setStatus("current")
_Pm20020maAlmTempHighAlaPortn_Type = EkiOnOff
_Pm20020maAlmTempHighAlaPortn_Object = MibTableColumn
pm20020maAlmTempHighAlaPortn = _Pm20020maAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 9),
    _Pm20020maAlmTempHighAlaPortn_Type()
)
pm20020maAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTempHighAlaPortn.setStatus("current")
_Pm20020maAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm20020maAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm20020maAlmRxPwrLowAlaPortn = _Pm20020maAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 16),
    _Pm20020maAlmRxPwrLowAlaPortn_Type()
)
pm20020maAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxPwrLowAlaPortn.setStatus("current")
_Pm20020maAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm20020maAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm20020maAlmRxPwrHighAlaPortn = _Pm20020maAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 2, 240, 1, 17),
    _Pm20020maAlmRxPwrHighAlaPortn_Type()
)
pm20020maAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxPwrHighAlaPortn.setStatus("current")
_Pm20020maAlmClientCrit_ObjectIdentity = ObjectIdentity
pm20020maAlmClientCrit = _Pm20020maAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3)
)
_Pm20020maAlmsynthAlmPortTable_Object = MibTable
pm20020maAlmsynthAlmPortTable = _Pm20020maAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm20020maAlmsynthAlmPortTable.setStatus("current")
_Pm20020maAlmsynthAlmPortEntry_Object = MibTableRow
pm20020maAlmsynthAlmPortEntry = _Pm20020maAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1)
)
pm20020maAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmsynthAlmPortEntry.setStatus("current")


class _Pm20020maAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm20020maAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm20020maAlmsynthAlmPortIndex_Object = MibTableColumn
pm20020maAlmsynthAlmPortIndex = _Pm20020maAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 1),
    _Pm20020maAlmsynthAlmPortIndex_Type()
)
pm20020maAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmsynthAlmPortIndex.setStatus("current")
_Pm20020maAlmSfpAbsentPortn_Type = EkiOnOff
_Pm20020maAlmSfpAbsentPortn_Object = MibTableColumn
pm20020maAlmSfpAbsentPortn = _Pm20020maAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 2),
    _Pm20020maAlmSfpAbsentPortn_Type()
)
pm20020maAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmSfpAbsentPortn.setStatus("current")
_Pm20020maAlmDdmAbsentPortn_Type = EkiOnOff
_Pm20020maAlmDdmAbsentPortn_Object = MibTableColumn
pm20020maAlmDdmAbsentPortn = _Pm20020maAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 3),
    _Pm20020maAlmDdmAbsentPortn_Type()
)
pm20020maAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmDdmAbsentPortn.setStatus("current")
_Pm20020maAlmHwFailAccPortn_Type = EkiOnOff
_Pm20020maAlmHwFailAccPortn_Object = MibTableColumn
pm20020maAlmHwFailAccPortn = _Pm20020maAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 5),
    _Pm20020maAlmHwFailAccPortn_Type()
)
pm20020maAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmHwFailAccPortn.setStatus("current")
_Pm20020maAlmDwLsdPortn_Type = EkiOnOff
_Pm20020maAlmDwLsdPortn_Object = MibTableColumn
pm20020maAlmDwLsdPortn = _Pm20020maAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 6),
    _Pm20020maAlmDwLsdPortn_Type()
)
pm20020maAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmDwLsdPortn.setStatus("current")
_Pm20020maAlmClientLocalOosPortn_Type = EkiOnOff
_Pm20020maAlmClientLocalOosPortn_Object = MibTableColumn
pm20020maAlmClientLocalOosPortn = _Pm20020maAlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 7),
    _Pm20020maAlmClientLocalOosPortn_Type()
)
pm20020maAlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientLocalOosPortn.setStatus("current")
_Pm20020maAlmClientRemoteOosPortn_Type = EkiOnOff
_Pm20020maAlmClientRemoteOosPortn_Object = MibTableColumn
pm20020maAlmClientRemoteOosPortn = _Pm20020maAlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 8),
    _Pm20020maAlmClientRemoteOosPortn_Type()
)
pm20020maAlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmClientRemoteOosPortn.setStatus("current")
_Pm20020maAlmDwCaisPortn_Type = EkiOnOff
_Pm20020maAlmDwCaisPortn_Object = MibTableColumn
pm20020maAlmDwCaisPortn = _Pm20020maAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 9),
    _Pm20020maAlmDwCaisPortn_Type()
)
pm20020maAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmDwCaisPortn.setStatus("current")
_Pm20020maAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm20020maAlmSfpDdmWarningPortn_Object = MibTableColumn
pm20020maAlmSfpDdmWarningPortn = _Pm20020maAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 10),
    _Pm20020maAlmSfpDdmWarningPortn_Type()
)
pm20020maAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmSfpDdmWarningPortn.setStatus("current")
_Pm20020maAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm20020maAlmSfpDdmAlmPortn_Object = MibTableColumn
pm20020maAlmSfpDdmAlmPortn = _Pm20020maAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 11),
    _Pm20020maAlmSfpDdmAlmPortn_Type()
)
pm20020maAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmSfpDdmAlmPortn.setStatus("current")
_Pm20020maAlmFailAccPortn_Type = EkiOnOff
_Pm20020maAlmFailAccPortn_Object = MibTableColumn
pm20020maAlmFailAccPortn = _Pm20020maAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 13),
    _Pm20020maAlmFailAccPortn_Type()
)
pm20020maAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmFailAccPortn.setStatus("current")
_Pm20020maAlmUpCsfPortn_Type = EkiOnOff
_Pm20020maAlmUpCsfPortn_Object = MibTableColumn
pm20020maAlmUpCsfPortn = _Pm20020maAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 2, 3, 8, 1, 17),
    _Pm20020maAlmUpCsfPortn_Type()
)
pm20020maAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmUpCsfPortn.setStatus("current")
_Pm20020maAlmLine_ObjectIdentity = ObjectIdentity
pm20020maAlmLine = _Pm20020maAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3)
)
_Pm20020maAlmLineNurg_ObjectIdentity = ObjectIdentity
pm20020maAlmLineNurg = _Pm20020maAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1)
)
_Pm20020maAlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm20020maAlmlineNetworkLaneAlarmWarning1Table = _Pm20020maAlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184)
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm20020maAlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm20020maAlmlineNetworkLaneAlarmWarning1Entry = _Pm20020maAlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1)
)
pm20020maAlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm20020maAlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm20020maAlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm20020maAlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm20020maAlmlineNetworkLaneAlarmWarning1Index = _Pm20020maAlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 1),
    _Pm20020maAlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm20020maAlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm20020maAlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm20020maAlmLineRxPowerLowAlarmPortn = _Pm20020maAlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 2),
    _Pm20020maAlmLineRxPowerLowAlarmPortn_Type()
)
pm20020maAlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm20020maAlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm20020maAlmLineRxPowerLowWarningPortn = _Pm20020maAlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 3),
    _Pm20020maAlmLineRxPowerLowWarningPortn_Type()
)
pm20020maAlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm20020maAlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm20020maAlmLineRxPowerHighWarningPortn = _Pm20020maAlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 4),
    _Pm20020maAlmLineRxPowerHighWarningPortn_Type()
)
pm20020maAlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm20020maAlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm20020maAlmLineRxPowerHighAlarmPortn = _Pm20020maAlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 5),
    _Pm20020maAlmLineRxPowerHighAlarmPortn_Type()
)
pm20020maAlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm20020maAlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm20020maAlmLineLaserTempLowAlarmPortn = _Pm20020maAlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 6),
    _Pm20020maAlmLineLaserTempLowAlarmPortn_Type()
)
pm20020maAlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm20020maAlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm20020maAlmLineLaserTempLowWarningPortn = _Pm20020maAlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 7),
    _Pm20020maAlmLineLaserTempLowWarningPortn_Type()
)
pm20020maAlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm20020maAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm20020maAlmLineLaserTempHighWarningPortn = _Pm20020maAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 8),
    _Pm20020maAlmLineLaserTempHighWarningPortn_Type()
)
pm20020maAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm20020maAlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm20020maAlmLineLaserTempHighAlarmPortn = _Pm20020maAlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 9),
    _Pm20020maAlmLineLaserTempHighAlarmPortn_Type()
)
pm20020maAlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm20020maAlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm20020maAlmLineTxPowerLowAlarmPortn = _Pm20020maAlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 10),
    _Pm20020maAlmLineTxPowerLowAlarmPortn_Type()
)
pm20020maAlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm20020maAlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm20020maAlmLineTxPowerLowWarningPortn = _Pm20020maAlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 11),
    _Pm20020maAlmLineTxPowerLowWarningPortn_Type()
)
pm20020maAlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm20020maAlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm20020maAlmLineTxPowerHighWarningPortn = _Pm20020maAlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 12),
    _Pm20020maAlmLineTxPowerHighWarningPortn_Type()
)
pm20020maAlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm20020maAlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm20020maAlmLineTxPowerHighAlarmPortn = _Pm20020maAlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 13),
    _Pm20020maAlmLineTxPowerHighAlarmPortn_Type()
)
pm20020maAlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm20020maAlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm20020maAlmLineBiasLowAlarmPortn = _Pm20020maAlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 14),
    _Pm20020maAlmLineBiasLowAlarmPortn_Type()
)
pm20020maAlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineBiasLowAlarmPortn.setStatus("current")
_Pm20020maAlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineBiasLowWarningPortn_Object = MibTableColumn
pm20020maAlmLineBiasLowWarningPortn = _Pm20020maAlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 15),
    _Pm20020maAlmLineBiasLowWarningPortn_Type()
)
pm20020maAlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineBiasLowWarningPortn.setStatus("current")
_Pm20020maAlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineBiasHighWarningPortn_Object = MibTableColumn
pm20020maAlmLineBiasHighWarningPortn = _Pm20020maAlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 16),
    _Pm20020maAlmLineBiasHighWarningPortn_Type()
)
pm20020maAlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineBiasHighWarningPortn.setStatus("current")
_Pm20020maAlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm20020maAlmLineBiasHighAlarmPortn = _Pm20020maAlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 184, 1, 17),
    _Pm20020maAlmLineBiasHighAlarmPortn_Type()
)
pm20020maAlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineBiasHighAlarmPortn.setStatus("current")
_Pm20020maAlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm20020maAlmlineNetworkLaneAlarmWarning2Table = _Pm20020maAlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188)
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm20020maAlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm20020maAlmlineNetworkLaneAlarmWarning2Entry = _Pm20020maAlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1)
)
pm20020maAlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm20020maAlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm20020maAlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm20020maAlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm20020maAlmlineNetworkLaneAlarmWarning2Index = _Pm20020maAlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 1),
    _Pm20020maAlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm20020maAlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm20020maAlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm20020maAlmTxModulatorBiasLowAlarmPortn = _Pm20020maAlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 2),
    _Pm20020maAlmTxModulatorBiasLowAlarmPortn_Type()
)
pm20020maAlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm20020maAlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm20020maAlmTxModulatorBiasLowWarningPortn = _Pm20020maAlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 3),
    _Pm20020maAlmTxModulatorBiasLowWarningPortn_Type()
)
pm20020maAlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm20020maAlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm20020maAlmTxModulatorBiasHighWarningPortn = _Pm20020maAlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 4),
    _Pm20020maAlmTxModulatorBiasHighWarningPortn_Type()
)
pm20020maAlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm20020maAlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm20020maAlmTxModulatorBiasHighAlarmPortn = _Pm20020maAlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 5),
    _Pm20020maAlmTxModulatorBiasHighAlarmPortn_Type()
)
pm20020maAlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm20020maAlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm20020maAlmRxLaserTempLowAlarmPortn = _Pm20020maAlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 6),
    _Pm20020maAlmRxLaserTempLowAlarmPortn_Type()
)
pm20020maAlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm20020maAlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm20020maAlmRxLaserTempLowWarningPortn = _Pm20020maAlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 7),
    _Pm20020maAlmRxLaserTempLowWarningPortn_Type()
)
pm20020maAlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm20020maAlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm20020maAlmRxLaserTempHighWarningPortn = _Pm20020maAlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 8),
    _Pm20020maAlmRxLaserTempHighWarningPortn_Type()
)
pm20020maAlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm20020maAlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm20020maAlmRxLaserTempHighAlarmPortn = _Pm20020maAlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 9),
    _Pm20020maAlmRxLaserTempHighAlarmPortn_Type()
)
pm20020maAlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm20020maAlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm20020maAlmRxLaserOutputLowAlarmPortn = _Pm20020maAlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 10),
    _Pm20020maAlmRxLaserOutputLowAlarmPortn_Type()
)
pm20020maAlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm20020maAlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm20020maAlmRxLaserOutputLowWarningPortn = _Pm20020maAlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 11),
    _Pm20020maAlmRxLaserOutputLowWarningPortn_Type()
)
pm20020maAlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm20020maAlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm20020maAlmRxLaserOutputHighWarningPortn = _Pm20020maAlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 12),
    _Pm20020maAlmRxLaserOutputHighWarningPortn_Type()
)
pm20020maAlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm20020maAlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm20020maAlmRxLaserOutputHighAlarmPortn = _Pm20020maAlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 13),
    _Pm20020maAlmRxLaserOutputHighAlarmPortn_Type()
)
pm20020maAlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm20020maAlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm20020maAlmRxLaserBiasLowAlarmPortn = _Pm20020maAlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 14),
    _Pm20020maAlmRxLaserBiasLowAlarmPortn_Type()
)
pm20020maAlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm20020maAlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm20020maAlmRxLaserBiasLowWarningPortn = _Pm20020maAlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 15),
    _Pm20020maAlmRxLaserBiasLowWarningPortn_Type()
)
pm20020maAlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm20020maAlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm20020maAlmRxLaserBiasHighWarningPortn = _Pm20020maAlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 16),
    _Pm20020maAlmRxLaserBiasHighWarningPortn_Type()
)
pm20020maAlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm20020maAlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm20020maAlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm20020maAlmRxLaserBiasHighAlarmPortn = _Pm20020maAlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 1, 188, 1, 17),
    _Pm20020maAlmRxLaserBiasHighAlarmPortn_Type()
)
pm20020maAlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm20020maAlmLineUrg_ObjectIdentity = ObjectIdentity
pm20020maAlmLineUrg = _Pm20020maAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2)
)
_Pm20020maAlmlineNetworkLaneFaultTable_Object = MibTable
pm20020maAlmlineNetworkLaneFaultTable = _Pm20020maAlmlineNetworkLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192)
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneFaultTable.setStatus("current")
_Pm20020maAlmlineNetworkLaneFaultEntry_Object = MibTableRow
pm20020maAlmlineNetworkLaneFaultEntry = _Pm20020maAlmlineNetworkLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1)
)
pm20020maAlmlineNetworkLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmlineNetworkLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneFaultEntry.setStatus("current")


class _Pm20020maAlmlineNetworkLaneFaultIndex_Type(Integer32):
    """Custom type pm20020maAlmlineNetworkLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmlineNetworkLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20020maAlmlineNetworkLaneFaultIndex_Object = MibTableColumn
pm20020maAlmlineNetworkLaneFaultIndex = _Pm20020maAlmlineNetworkLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 1),
    _Pm20020maAlmlineNetworkLaneFaultIndex_Type()
)
pm20020maAlmlineNetworkLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneFaultIndex.setStatus("current")
_Pm20020maAlmLineLaneRxTecFaultPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneRxTecFaultPortn_Object = MibTableColumn
pm20020maAlmLineLaneRxTecFaultPortn = _Pm20020maAlmLineLaneRxTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 3),
    _Pm20020maAlmLineLaneRxTecFaultPortn_Type()
)
pm20020maAlmLineLaneRxTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneRxTecFaultPortn.setStatus("current")
_Pm20020maAlmLineLaneRxFifoErrorPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneRxFifoErrorPortn_Object = MibTableColumn
pm20020maAlmLineLaneRxFifoErrorPortn = _Pm20020maAlmLineLaneRxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 4),
    _Pm20020maAlmLineLaneRxFifoErrorPortn_Type()
)
pm20020maAlmLineLaneRxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneRxFifoErrorPortn.setStatus("current")
_Pm20020maAlmLineLaneRxLolPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneRxLolPortn_Object = MibTableColumn
pm20020maAlmLineLaneRxLolPortn = _Pm20020maAlmLineLaneRxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 5),
    _Pm20020maAlmLineLaneRxLolPortn_Type()
)
pm20020maAlmLineLaneRxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneRxLolPortn.setStatus("current")
_Pm20020maAlmLineLaneRxLosPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneRxLosPortn_Object = MibTableColumn
pm20020maAlmLineLaneRxLosPortn = _Pm20020maAlmLineLaneRxLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 6),
    _Pm20020maAlmLineLaneRxLosPortn_Type()
)
pm20020maAlmLineLaneRxLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneRxLosPortn.setStatus("current")
_Pm20020maAlmLineLaneTxLolPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneTxLolPortn_Object = MibTableColumn
pm20020maAlmLineLaneTxLolPortn = _Pm20020maAlmLineLaneTxLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 8),
    _Pm20020maAlmLineLaneTxLolPortn_Type()
)
pm20020maAlmLineLaneTxLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneTxLolPortn.setStatus("current")
_Pm20020maAlmLineLaneTxLosfPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneTxLosfPortn_Object = MibTableColumn
pm20020maAlmLineLaneTxLosfPortn = _Pm20020maAlmLineLaneTxLosfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 9),
    _Pm20020maAlmLineLaneTxLosfPortn_Type()
)
pm20020maAlmLineLaneTxLosfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneTxLosfPortn.setStatus("current")
_Pm20020maAlmLineLaneApdPowerSupplyPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneApdPowerSupplyPortn_Object = MibTableColumn
pm20020maAlmLineLaneApdPowerSupplyPortn = _Pm20020maAlmLineLaneApdPowerSupplyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 15),
    _Pm20020maAlmLineLaneApdPowerSupplyPortn_Type()
)
pm20020maAlmLineLaneApdPowerSupplyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneApdPowerSupplyPortn.setStatus("current")
_Pm20020maAlmLineLaneWavelengthUnlockedPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneWavelengthUnlockedPortn_Object = MibTableColumn
pm20020maAlmLineLaneWavelengthUnlockedPortn = _Pm20020maAlmLineLaneWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 16),
    _Pm20020maAlmLineLaneWavelengthUnlockedPortn_Type()
)
pm20020maAlmLineLaneWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneWavelengthUnlockedPortn.setStatus("current")
_Pm20020maAlmLineLaneTecFaultPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneTecFaultPortn_Object = MibTableColumn
pm20020maAlmLineLaneTecFaultPortn = _Pm20020maAlmLineLaneTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 192, 1, 17),
    _Pm20020maAlmLineLaneTecFaultPortn_Type()
)
pm20020maAlmLineLaneTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneTecFaultPortn.setStatus("current")
_Pm20020maAlmlineHostLaneFaultTable_Object = MibTable
pm20020maAlmlineHostLaneFaultTable = _Pm20020maAlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196)
)
if mibBuilder.loadTexts:
    pm20020maAlmlineHostLaneFaultTable.setStatus("current")
_Pm20020maAlmlineHostLaneFaultEntry_Object = MibTableRow
pm20020maAlmlineHostLaneFaultEntry = _Pm20020maAlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1)
)
pm20020maAlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmlineHostLaneFaultEntry.setStatus("current")


class _Pm20020maAlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm20020maAlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm20020maAlmlineHostLaneFaultIndex_Object = MibTableColumn
pm20020maAlmlineHostLaneFaultIndex = _Pm20020maAlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 1),
    _Pm20020maAlmlineHostLaneFaultIndex_Type()
)
pm20020maAlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmlineHostLaneFaultIndex.setStatus("current")
_Pm20020maAlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm20020maAlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm20020maAlmLineInputLossOfSignalPortn = _Pm20020maAlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 2),
    _Pm20020maAlmLineInputLossOfSignalPortn_Type()
)
pm20020maAlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineInputLossOfSignalPortn.setStatus("current")
_Pm20020maAlmLineLossOfFramePortn_Type = EkiOnOff
_Pm20020maAlmLineLossOfFramePortn_Object = MibTableColumn
pm20020maAlmLineLossOfFramePortn = _Pm20020maAlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 3),
    _Pm20020maAlmLineLossOfFramePortn_Type()
)
pm20020maAlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLossOfFramePortn.setStatus("current")
_Pm20020maAlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm20020maAlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm20020maAlmLineSmBdiInsertedPortn = _Pm20020maAlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 4),
    _Pm20020maAlmLineSmBdiInsertedPortn_Type()
)
pm20020maAlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineSmBdiInsertedPortn.setStatus("current")
_Pm20020maAlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm20020maAlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm20020maAlmLineSmBdiDetectedPortn = _Pm20020maAlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 5),
    _Pm20020maAlmLineSmBdiDetectedPortn_Type()
)
pm20020maAlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineSmBdiDetectedPortn.setStatus("current")
_Pm20020maAlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm20020maAlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm20020maAlmLineSmIaeInsertedPortn = _Pm20020maAlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 6),
    _Pm20020maAlmLineSmIaeInsertedPortn_Type()
)
pm20020maAlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineSmIaeInsertedPortn.setStatus("current")
_Pm20020maAlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm20020maAlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm20020maAlmLineSmIaeDetectedPortn = _Pm20020maAlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 7),
    _Pm20020maAlmLineSmIaeDetectedPortn_Type()
)
pm20020maAlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineSmIaeDetectedPortn.setStatus("current")
_Pm20020maAlmLineTxHostLolPortn_Type = EkiOnOff
_Pm20020maAlmLineTxHostLolPortn_Object = MibTableColumn
pm20020maAlmLineTxHostLolPortn = _Pm20020maAlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 10),
    _Pm20020maAlmLineTxHostLolPortn_Type()
)
pm20020maAlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxHostLolPortn.setStatus("current")
_Pm20020maAlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm20020maAlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm20020maAlmLineLaneTxFifoErrorPortn = _Pm20020maAlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 196, 1, 11),
    _Pm20020maAlmLineLaneTxFifoErrorPortn_Type()
)
pm20020maAlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm20020maAlmlineNetworkLaneRxOtnTable_Object = MibTable
pm20020maAlmlineNetworkLaneRxOtnTable = _Pm20020maAlmlineNetworkLaneRxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200)
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneRxOtnTable.setStatus("current")
_Pm20020maAlmlineNetworkLaneRxOtnEntry_Object = MibTableRow
pm20020maAlmlineNetworkLaneRxOtnEntry = _Pm20020maAlmlineNetworkLaneRxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1)
)
pm20020maAlmlineNetworkLaneRxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmlineNetworkLaneRxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneRxOtnEntry.setStatus("current")


class _Pm20020maAlmlineNetworkLaneRxOtnIndex_Type(Integer32):
    """Custom type pm20020maAlmlineNetworkLaneRxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmlineNetworkLaneRxOtnIndex_Type.__name__ = "Integer32"
_Pm20020maAlmlineNetworkLaneRxOtnIndex_Object = MibTableColumn
pm20020maAlmlineNetworkLaneRxOtnIndex = _Pm20020maAlmlineNetworkLaneRxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 1),
    _Pm20020maAlmlineNetworkLaneRxOtnIndex_Type()
)
pm20020maAlmlineNetworkLaneRxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmlineNetworkLaneRxOtnIndex.setStatus("current")
_Pm20020maAlmLineRxOtnOduAisPortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnOduAisPortn_Object = MibTableColumn
pm20020maAlmLineRxOtnOduAisPortn = _Pm20020maAlmLineRxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 10),
    _Pm20020maAlmLineRxOtnOduAisPortn_Type()
)
pm20020maAlmLineRxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnOduAisPortn.setStatus("current")
_Pm20020maAlmLineRxOtnOtuAisPortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnOtuAisPortn_Object = MibTableColumn
pm20020maAlmLineRxOtnOtuAisPortn = _Pm20020maAlmLineRxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 11),
    _Pm20020maAlmLineRxOtnOtuAisPortn_Type()
)
pm20020maAlmLineRxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnOtuAisPortn.setStatus("current")
_Pm20020maAlmLineRxSmBdiPortn_Type = EkiOnOff
_Pm20020maAlmLineRxSmBdiPortn_Object = MibTableColumn
pm20020maAlmLineRxSmBdiPortn = _Pm20020maAlmLineRxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 12),
    _Pm20020maAlmLineRxSmBdiPortn_Type()
)
pm20020maAlmLineRxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxSmBdiPortn.setStatus("current")
_Pm20020maAlmLineRxOtnIaePortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnIaePortn_Object = MibTableColumn
pm20020maAlmLineRxOtnIaePortn = _Pm20020maAlmLineRxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 13),
    _Pm20020maAlmLineRxOtnIaePortn_Type()
)
pm20020maAlmLineRxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnIaePortn.setStatus("current")
_Pm20020maAlmLineRxOtnOomPortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnOomPortn_Object = MibTableColumn
pm20020maAlmLineRxOtnOomPortn = _Pm20020maAlmLineRxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 14),
    _Pm20020maAlmLineRxOtnOomPortn_Type()
)
pm20020maAlmLineRxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnOomPortn.setStatus("current")
_Pm20020maAlmLineRxOtnLomPortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnLomPortn_Object = MibTableColumn
pm20020maAlmLineRxOtnLomPortn = _Pm20020maAlmLineRxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 15),
    _Pm20020maAlmLineRxOtnLomPortn_Type()
)
pm20020maAlmLineRxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnLomPortn.setStatus("current")
_Pm20020maAlmLineRxOtnOofPortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnOofPortn_Object = MibTableColumn
pm20020maAlmLineRxOtnOofPortn = _Pm20020maAlmLineRxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 16),
    _Pm20020maAlmLineRxOtnOofPortn_Type()
)
pm20020maAlmLineRxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnOofPortn.setStatus("current")
_Pm20020maAlmLineRxOtnLofPortn_Type = EkiOnOff
_Pm20020maAlmLineRxOtnLofPortn_Object = MibTableColumn
pm20020maAlmLineRxOtnLofPortn = _Pm20020maAlmLineRxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 200, 1, 17),
    _Pm20020maAlmLineRxOtnLofPortn_Type()
)
pm20020maAlmLineRxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineRxOtnLofPortn.setStatus("current")
_Pm20020maAlmlineHostLaneTxOtnTable_Object = MibTable
pm20020maAlmlineHostLaneTxOtnTable = _Pm20020maAlmlineHostLaneTxOtnTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204)
)
if mibBuilder.loadTexts:
    pm20020maAlmlineHostLaneTxOtnTable.setStatus("current")
_Pm20020maAlmlineHostLaneTxOtnEntry_Object = MibTableRow
pm20020maAlmlineHostLaneTxOtnEntry = _Pm20020maAlmlineHostLaneTxOtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1)
)
pm20020maAlmlineHostLaneTxOtnEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmlineHostLaneTxOtnIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmlineHostLaneTxOtnEntry.setStatus("current")


class _Pm20020maAlmlineHostLaneTxOtnIndex_Type(Integer32):
    """Custom type pm20020maAlmlineHostLaneTxOtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmlineHostLaneTxOtnIndex_Type.__name__ = "Integer32"
_Pm20020maAlmlineHostLaneTxOtnIndex_Object = MibTableColumn
pm20020maAlmlineHostLaneTxOtnIndex = _Pm20020maAlmlineHostLaneTxOtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 1),
    _Pm20020maAlmlineHostLaneTxOtnIndex_Type()
)
pm20020maAlmlineHostLaneTxOtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmlineHostLaneTxOtnIndex.setStatus("current")
_Pm20020maAlmLineTxOtnOduAisPortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnOduAisPortn_Object = MibTableColumn
pm20020maAlmLineTxOtnOduAisPortn = _Pm20020maAlmLineTxOtnOduAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 10),
    _Pm20020maAlmLineTxOtnOduAisPortn_Type()
)
pm20020maAlmLineTxOtnOduAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnOduAisPortn.setStatus("current")
_Pm20020maAlmLineTxOtnOtuAisPortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnOtuAisPortn_Object = MibTableColumn
pm20020maAlmLineTxOtnOtuAisPortn = _Pm20020maAlmLineTxOtnOtuAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 11),
    _Pm20020maAlmLineTxOtnOtuAisPortn_Type()
)
pm20020maAlmLineTxOtnOtuAisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnOtuAisPortn.setStatus("current")
_Pm20020maAlmLineTxSmBdiPortn_Type = EkiOnOff
_Pm20020maAlmLineTxSmBdiPortn_Object = MibTableColumn
pm20020maAlmLineTxSmBdiPortn = _Pm20020maAlmLineTxSmBdiPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 12),
    _Pm20020maAlmLineTxSmBdiPortn_Type()
)
pm20020maAlmLineTxSmBdiPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxSmBdiPortn.setStatus("current")
_Pm20020maAlmLineTxOtnIaePortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnIaePortn_Object = MibTableColumn
pm20020maAlmLineTxOtnIaePortn = _Pm20020maAlmLineTxOtnIaePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 13),
    _Pm20020maAlmLineTxOtnIaePortn_Type()
)
pm20020maAlmLineTxOtnIaePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnIaePortn.setStatus("current")
_Pm20020maAlmLineTxOtnOomPortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnOomPortn_Object = MibTableColumn
pm20020maAlmLineTxOtnOomPortn = _Pm20020maAlmLineTxOtnOomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 14),
    _Pm20020maAlmLineTxOtnOomPortn_Type()
)
pm20020maAlmLineTxOtnOomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnOomPortn.setStatus("current")
_Pm20020maAlmLineTxOtnLomPortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnLomPortn_Object = MibTableColumn
pm20020maAlmLineTxOtnLomPortn = _Pm20020maAlmLineTxOtnLomPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 15),
    _Pm20020maAlmLineTxOtnLomPortn_Type()
)
pm20020maAlmLineTxOtnLomPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnLomPortn.setStatus("current")
_Pm20020maAlmLineTxOtnOofPortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnOofPortn_Object = MibTableColumn
pm20020maAlmLineTxOtnOofPortn = _Pm20020maAlmLineTxOtnOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 16),
    _Pm20020maAlmLineTxOtnOofPortn_Type()
)
pm20020maAlmLineTxOtnOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnOofPortn.setStatus("current")
_Pm20020maAlmLineTxOtnLofPortn_Type = EkiOnOff
_Pm20020maAlmLineTxOtnLofPortn_Object = MibTableColumn
pm20020maAlmLineTxOtnLofPortn = _Pm20020maAlmLineTxOtnLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 2, 204, 1, 17),
    _Pm20020maAlmLineTxOtnLofPortn_Type()
)
pm20020maAlmLineTxOtnLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineTxOtnLofPortn.setStatus("current")
_Pm20020maAlmLineCrit_ObjectIdentity = ObjectIdentity
pm20020maAlmLineCrit = _Pm20020maAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3)
)
_Pm20020maAlmsynthAlmLineTable_Object = MibTable
pm20020maAlmsynthAlmLineTable = _Pm20020maAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pm20020maAlmsynthAlmLineTable.setStatus("current")
_Pm20020maAlmsynthAlmLineEntry_Object = MibTableRow
pm20020maAlmsynthAlmLineEntry = _Pm20020maAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1)
)
pm20020maAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm20020maAlmsynthAlmLineEntry.setStatus("current")


class _Pm20020maAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm20020maAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm20020maAlmsynthAlmLineIndex_Object = MibTableColumn
pm20020maAlmsynthAlmLineIndex = _Pm20020maAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 1),
    _Pm20020maAlmsynthAlmLineIndex_Type()
)
pm20020maAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmsynthAlmLineIndex.setStatus("current")
_Pm20020maAlmXfpAbsentPortn_Type = EkiOnOff
_Pm20020maAlmXfpAbsentPortn_Object = MibTableColumn
pm20020maAlmXfpAbsentPortn = _Pm20020maAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 2),
    _Pm20020maAlmXfpAbsentPortn_Type()
)
pm20020maAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmXfpAbsentPortn.setStatus("current")
_Pm20020maAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm20020maAlmXfpInitNotComplPortn_Object = MibTableColumn
pm20020maAlmXfpInitNotComplPortn = _Pm20020maAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 3),
    _Pm20020maAlmXfpInitNotComplPortn_Type()
)
pm20020maAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmXfpInitNotComplPortn.setStatus("current")
_Pm20020maAlmLineHwFailPortn_Type = EkiOnOff
_Pm20020maAlmLineHwFailPortn_Object = MibTableColumn
pm20020maAlmLineHwFailPortn = _Pm20020maAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 5),
    _Pm20020maAlmLineHwFailPortn_Type()
)
pm20020maAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineHwFailPortn.setStatus("current")
_Pm20020maAlmXfpTxOffPortn_Type = EkiOnOff
_Pm20020maAlmXfpTxOffPortn_Object = MibTableColumn
pm20020maAlmXfpTxOffPortn = _Pm20020maAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 6),
    _Pm20020maAlmXfpTxOffPortn_Type()
)
pm20020maAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmXfpTxOffPortn.setStatus("current")
_Pm20020maAlmLineLocalOosPortn_Type = EkiOnOff
_Pm20020maAlmLineLocalOosPortn_Object = MibTableColumn
pm20020maAlmLineLocalOosPortn = _Pm20020maAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 7),
    _Pm20020maAlmLineLocalOosPortn_Type()
)
pm20020maAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineLocalOosPortn.setStatus("current")
_Pm20020maAlmUpRdiInsPortn_Type = EkiOnOff
_Pm20020maAlmUpRdiInsPortn_Object = MibTableColumn
pm20020maAlmUpRdiInsPortn = _Pm20020maAlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 9),
    _Pm20020maAlmUpRdiInsPortn_Type()
)
pm20020maAlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmUpRdiInsPortn.setStatus("current")
_Pm20020maAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm20020maAlmLineDdmWarningPortn_Object = MibTableColumn
pm20020maAlmLineDdmWarningPortn = _Pm20020maAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 10),
    _Pm20020maAlmLineDdmWarningPortn_Type()
)
pm20020maAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineDdmWarningPortn.setStatus("current")
_Pm20020maAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm20020maAlmLineDdmAlmPortn_Object = MibTableColumn
pm20020maAlmLineDdmAlmPortn = _Pm20020maAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 11),
    _Pm20020maAlmLineDdmAlmPortn_Type()
)
pm20020maAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineDdmAlmPortn.setStatus("current")
_Pm20020maAlmLineFailPortn_Type = EkiOnOff
_Pm20020maAlmLineFailPortn_Object = MibTableColumn
pm20020maAlmLineFailPortn = _Pm20020maAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 13),
    _Pm20020maAlmLineFailPortn_Type()
)
pm20020maAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineFailPortn.setStatus("current")
_Pm20020maAlmLineActivePortn_Type = EkiOnOff
_Pm20020maAlmLineActivePortn_Object = MibTableColumn
pm20020maAlmLineActivePortn = _Pm20020maAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 2, 3, 3, 40, 1, 17),
    _Pm20020maAlmLineActivePortn_Type()
)
pm20020maAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maAlmLineActivePortn.setStatus("current")
_Pm20020mameasures_ObjectIdentity = ObjectIdentity
pm20020mameasures = _Pm20020mameasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3)
)
_Pm20020maMesrOther_ObjectIdentity = ObjectIdentity
pm20020maMesrOther = _Pm20020maMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1)
)
_Pm20020maMesrsynth0_Type = EkiMeasureType
_Pm20020maMesrsynth0_Object = MibScalar
pm20020maMesrsynth0 = _Pm20020maMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 0),
    _Pm20020maMesrsynth0_Type()
)
pm20020maMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrsynth0.setStatus("deprecated")
_Pm20020maMesrsynth1_Type = EkiMeasureType
_Pm20020maMesrsynth1_Object = MibScalar
pm20020maMesrsynth1 = _Pm20020maMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 1),
    _Pm20020maMesrsynth1_Type()
)
pm20020maMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrsynth1.setStatus("deprecated")


class _Pm20020maMesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm20020maMesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm20020maMesrpmIntervalNumber_Object = MibScalar
pm20020maMesrpmIntervalNumber = _Pm20020maMesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 7),
    _Pm20020maMesrpmIntervalNumber_Type()
)
pm20020maMesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrpmIntervalNumber.setStatus("current")


class _Pm20020maMesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm20020maMesrlineNetTxLaserOutputPwrAverage = _Pm20020maMesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 196),
    _Pm20020maMesrlineNetTxLaserOutputPwrAverage_Type()
)
pm20020maMesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm20020maMesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxLaserTempAverage_Object = MibScalar
pm20020maMesrlineNetTxLaserTempAverage = _Pm20020maMesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 197),
    _Pm20020maMesrlineNetTxLaserTempAverage_Type()
)
pm20020maMesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm20020maMesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm20020maMesrlineNetTxBiasCurrentAverage = _Pm20020maMesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 198),
    _Pm20020maMesrlineNetTxBiasCurrentAverage_Type()
)
pm20020maMesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm20020maMesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetRxInputPwrAverage_Object = MibScalar
pm20020maMesrlineNetRxInputPwrAverage = _Pm20020maMesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 199),
    _Pm20020maMesrlineNetRxInputPwrAverage_Type()
)
pm20020maMesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm20020maMesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineResidualChromaticDispAverage_Object = MibScalar
pm20020maMesrlineResidualChromaticDispAverage = _Pm20020maMesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 200),
    _Pm20020maMesrlineResidualChromaticDispAverage_Type()
)
pm20020maMesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm20020maMesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineDiffGroupDelayAverage_Object = MibScalar
pm20020maMesrlineDiffGroupDelayAverage = _Pm20020maMesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 201),
    _Pm20020maMesrlineDiffGroupDelayAverage_Type()
)
pm20020maMesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm20020maMesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineQFactorAverage_Object = MibScalar
pm20020maMesrlineQFactorAverage = _Pm20020maMesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 202),
    _Pm20020maMesrlineQFactorAverage_Type()
)
pm20020maMesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorAverage.setStatus("current")


class _Pm20020maMesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm20020maMesrlineCarrierFreqOffsetAverage = _Pm20020maMesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 203),
    _Pm20020maMesrlineCarrierFreqOffsetAverage_Type()
)
pm20020maMesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm20020maMesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm20020maMesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineOsnrAverage_Object = MibScalar
pm20020maMesrlineOsnrAverage = _Pm20020maMesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 204),
    _Pm20020maMesrlineOsnrAverage_Type()
)
pm20020maMesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrAverage.setStatus("current")


class _Pm20020maMesrclientNetTxTempMin_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetTxTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxTempMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetTxTempMin_Object = MibScalar
pm20020maMesrclientNetTxTempMin = _Pm20020maMesrclientNetTxTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 208),
    _Pm20020maMesrclientNetTxTempMin_Type()
)
pm20020maMesrclientNetTxTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxTempMin.setStatus("current")


class _Pm20020maMesrclientNetTxBiasMin_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetTxBiasMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxBiasMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetTxBiasMin_Object = MibScalar
pm20020maMesrclientNetTxBiasMin = _Pm20020maMesrclientNetTxBiasMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 209),
    _Pm20020maMesrclientNetTxBiasMin_Type()
)
pm20020maMesrclientNetTxBiasMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxBiasMin.setStatus("current")


class _Pm20020maMesrclientNetTxPwrMin_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetTxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxPwrMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetTxPwrMin_Object = MibScalar
pm20020maMesrclientNetTxPwrMin = _Pm20020maMesrclientNetTxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 210),
    _Pm20020maMesrclientNetTxPwrMin_Type()
)
pm20020maMesrclientNetTxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxPwrMin.setStatus("current")


class _Pm20020maMesrclientNetRxPwrMin_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetRxPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetRxPwrMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetRxPwrMin_Object = MibScalar
pm20020maMesrclientNetRxPwrMin = _Pm20020maMesrclientNetRxPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 211),
    _Pm20020maMesrclientNetRxPwrMin_Type()
)
pm20020maMesrclientNetRxPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetRxPwrMin.setStatus("current")


class _Pm20020maMesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm20020maMesrlineNetTxLaserOutputPwrMin = _Pm20020maMesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 212),
    _Pm20020maMesrlineNetTxLaserOutputPwrMin_Type()
)
pm20020maMesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm20020maMesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxLaserTempMin_Object = MibScalar
pm20020maMesrlineNetTxLaserTempMin = _Pm20020maMesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 213),
    _Pm20020maMesrlineNetTxLaserTempMin_Type()
)
pm20020maMesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempMin.setStatus("current")


class _Pm20020maMesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxBiasCurrentMin_Object = MibScalar
pm20020maMesrlineNetTxBiasCurrentMin = _Pm20020maMesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 214),
    _Pm20020maMesrlineNetTxBiasCurrentMin_Type()
)
pm20020maMesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm20020maMesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetRxInputPwrMin_Object = MibScalar
pm20020maMesrlineNetRxInputPwrMin = _Pm20020maMesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 215),
    _Pm20020maMesrlineNetRxInputPwrMin_Type()
)
pm20020maMesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrMin.setStatus("current")


class _Pm20020maMesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineResidualChromaticDispMin_Object = MibScalar
pm20020maMesrlineResidualChromaticDispMin = _Pm20020maMesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 216),
    _Pm20020maMesrlineResidualChromaticDispMin_Type()
)
pm20020maMesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispMin.setStatus("current")


class _Pm20020maMesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineDiffGroupDelayMin_Object = MibScalar
pm20020maMesrlineDiffGroupDelayMin = _Pm20020maMesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 217),
    _Pm20020maMesrlineDiffGroupDelayMin_Type()
)
pm20020maMesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayMin.setStatus("current")


class _Pm20020maMesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineQFactorMin_Object = MibScalar
pm20020maMesrlineQFactorMin = _Pm20020maMesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 218),
    _Pm20020maMesrlineQFactorMin_Type()
)
pm20020maMesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorMin.setStatus("current")


class _Pm20020maMesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineCarrierFreqOffsetMin_Object = MibScalar
pm20020maMesrlineCarrierFreqOffsetMin = _Pm20020maMesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 219),
    _Pm20020maMesrlineCarrierFreqOffsetMin_Type()
)
pm20020maMesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm20020maMesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm20020maMesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineOsnrMin_Object = MibScalar
pm20020maMesrlineOsnrMin = _Pm20020maMesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 220),
    _Pm20020maMesrlineOsnrMin_Type()
)
pm20020maMesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrMin.setStatus("current")


class _Pm20020maMesrclientNetTxTempMax_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetTxTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxTempMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetTxTempMax_Object = MibScalar
pm20020maMesrclientNetTxTempMax = _Pm20020maMesrclientNetTxTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 224),
    _Pm20020maMesrclientNetTxTempMax_Type()
)
pm20020maMesrclientNetTxTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxTempMax.setStatus("current")


class _Pm20020maMesrclientNetTxBiasMax_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetTxBiasMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxBiasMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetTxBiasMax_Object = MibScalar
pm20020maMesrclientNetTxBiasMax = _Pm20020maMesrclientNetTxBiasMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 225),
    _Pm20020maMesrclientNetTxBiasMax_Type()
)
pm20020maMesrclientNetTxBiasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxBiasMax.setStatus("current")


class _Pm20020maMesrclientNetTxPwrMax_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetTxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxPwrMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetTxPwrMax_Object = MibScalar
pm20020maMesrclientNetTxPwrMax = _Pm20020maMesrclientNetTxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 226),
    _Pm20020maMesrclientNetTxPwrMax_Type()
)
pm20020maMesrclientNetTxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxPwrMax.setStatus("current")


class _Pm20020maMesrclientNetRxPwrMax_Type(Unsigned32):
    """Custom type pm20020maMesrclientNetRxPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetRxPwrMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientNetRxPwrMax_Object = MibScalar
pm20020maMesrclientNetRxPwrMax = _Pm20020maMesrclientNetRxPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 227),
    _Pm20020maMesrclientNetRxPwrMax_Type()
)
pm20020maMesrclientNetRxPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetRxPwrMax.setStatus("current")


class _Pm20020maMesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm20020maMesrlineNetTxLaserOutputPwrMax = _Pm20020maMesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 228),
    _Pm20020maMesrlineNetTxLaserOutputPwrMax_Type()
)
pm20020maMesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm20020maMesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxLaserTempMax_Object = MibScalar
pm20020maMesrlineNetTxLaserTempMax = _Pm20020maMesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 229),
    _Pm20020maMesrlineNetTxLaserTempMax_Type()
)
pm20020maMesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempMax.setStatus("current")


class _Pm20020maMesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetTxBiasCurrentMax_Object = MibScalar
pm20020maMesrlineNetTxBiasCurrentMax = _Pm20020maMesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 230),
    _Pm20020maMesrlineNetTxBiasCurrentMax_Type()
)
pm20020maMesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm20020maMesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineNetRxInputPwrMax_Object = MibScalar
pm20020maMesrlineNetRxInputPwrMax = _Pm20020maMesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 231),
    _Pm20020maMesrlineNetRxInputPwrMax_Type()
)
pm20020maMesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrMax.setStatus("current")


class _Pm20020maMesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineResidualChromaticDispMax_Object = MibScalar
pm20020maMesrlineResidualChromaticDispMax = _Pm20020maMesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 232),
    _Pm20020maMesrlineResidualChromaticDispMax_Type()
)
pm20020maMesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispMax.setStatus("current")


class _Pm20020maMesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineDiffGroupDelayMax_Object = MibScalar
pm20020maMesrlineDiffGroupDelayMax = _Pm20020maMesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 233),
    _Pm20020maMesrlineDiffGroupDelayMax_Type()
)
pm20020maMesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayMax.setStatus("current")


class _Pm20020maMesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineQFactorMax_Object = MibScalar
pm20020maMesrlineQFactorMax = _Pm20020maMesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 234),
    _Pm20020maMesrlineQFactorMax_Type()
)
pm20020maMesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorMax.setStatus("current")


class _Pm20020maMesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineCarrierFreqOffsetMax_Object = MibScalar
pm20020maMesrlineCarrierFreqOffsetMax = _Pm20020maMesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 235),
    _Pm20020maMesrlineCarrierFreqOffsetMax_Type()
)
pm20020maMesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm20020maMesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm20020maMesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineOsnrMax_Object = MibScalar
pm20020maMesrlineOsnrMax = _Pm20020maMesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 1, 236),
    _Pm20020maMesrlineOsnrMax_Type()
)
pm20020maMesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrMax.setStatus("current")
_Pm20020maMesrClient_ObjectIdentity = ObjectIdentity
pm20020maMesrClient = _Pm20020maMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2)
)


class _Pm20020maMesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm20020maMesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientCfpTemp_Object = MibScalar
pm20020maMesrclientCfpTemp = _Pm20020maMesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 8),
    _Pm20020maMesrclientCfpTemp_Type()
)
pm20020maMesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientCfpTemp.setStatus("current")


class _Pm20020maMesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm20020maMesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientCfp3v3Voltage_Object = MibScalar
pm20020maMesrclientCfp3v3Voltage = _Pm20020maMesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 9),
    _Pm20020maMesrclientCfp3v3Voltage_Type()
)
pm20020maMesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientCfp3v3Voltage.setStatus("current")


class _Pm20020maMesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm20020maMesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm20020maMesrclientSoaBiasCurrent_Object = MibScalar
pm20020maMesrclientSoaBiasCurrent = _Pm20020maMesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 10),
    _Pm20020maMesrclientSoaBiasCurrent_Type()
)
pm20020maMesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientSoaBiasCurrent.setStatus("current")
_Pm20020maMesrclientNetTxTempTable_Object = MibTable
pm20020maMesrclientNetTxTempTable = _Pm20020maMesrclientNetTxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxTempTable.setStatus("current")
_Pm20020maMesrclientNetTxTempEntry_Object = MibTableRow
pm20020maMesrclientNetTxTempEntry = _Pm20020maMesrclientNetTxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 16, 1)
)
pm20020maMesrclientNetTxTempEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrclientNetTxTempIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxTempEntry.setStatus("current")


class _Pm20020maMesrclientNetTxTempIndex_Type(Integer32):
    """Custom type pm20020maMesrclientNetTxTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrclientNetTxTempIndex_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetTxTempIndex_Object = MibTableColumn
pm20020maMesrclientNetTxTempIndex = _Pm20020maMesrclientNetTxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 16, 1, 1),
    _Pm20020maMesrclientNetTxTempIndex_Type()
)
pm20020maMesrclientNetTxTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxTempIndex.setStatus("current")


class _Pm20020maMesrclientNetTxTempPortn_Type(Integer32):
    """Custom type pm20020maMesrclientNetTxTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxTempPortn_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetTxTempPortn_Object = MibTableColumn
pm20020maMesrclientNetTxTempPortn = _Pm20020maMesrclientNetTxTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 16, 1, 2),
    _Pm20020maMesrclientNetTxTempPortn_Type()
)
pm20020maMesrclientNetTxTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxTempPortn.setStatus("current")
_Pm20020maMesrclientNetTxBiasTable_Object = MibTable
pm20020maMesrclientNetTxBiasTable = _Pm20020maMesrclientNetTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxBiasTable.setStatus("current")
_Pm20020maMesrclientNetTxBiasEntry_Object = MibTableRow
pm20020maMesrclientNetTxBiasEntry = _Pm20020maMesrclientNetTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 48, 1)
)
pm20020maMesrclientNetTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrclientNetTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxBiasEntry.setStatus("current")


class _Pm20020maMesrclientNetTxBiasIndex_Type(Integer32):
    """Custom type pm20020maMesrclientNetTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrclientNetTxBiasIndex_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetTxBiasIndex_Object = MibTableColumn
pm20020maMesrclientNetTxBiasIndex = _Pm20020maMesrclientNetTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 48, 1, 1),
    _Pm20020maMesrclientNetTxBiasIndex_Type()
)
pm20020maMesrclientNetTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxBiasIndex.setStatus("current")


class _Pm20020maMesrclientNetTxBiasPortn_Type(Integer32):
    """Custom type pm20020maMesrclientNetTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxBiasPortn_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetTxBiasPortn_Object = MibTableColumn
pm20020maMesrclientNetTxBiasPortn = _Pm20020maMesrclientNetTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 48, 1, 2),
    _Pm20020maMesrclientNetTxBiasPortn_Type()
)
pm20020maMesrclientNetTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxBiasPortn.setStatus("current")
_Pm20020maMesrclientNetTxPwrTable_Object = MibTable
pm20020maMesrclientNetTxPwrTable = _Pm20020maMesrclientNetTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxPwrTable.setStatus("current")
_Pm20020maMesrclientNetTxPwrEntry_Object = MibTableRow
pm20020maMesrclientNetTxPwrEntry = _Pm20020maMesrclientNetTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 80, 1)
)
pm20020maMesrclientNetTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrclientNetTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxPwrEntry.setStatus("current")


class _Pm20020maMesrclientNetTxPwrIndex_Type(Integer32):
    """Custom type pm20020maMesrclientNetTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrclientNetTxPwrIndex_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetTxPwrIndex_Object = MibTableColumn
pm20020maMesrclientNetTxPwrIndex = _Pm20020maMesrclientNetTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 80, 1, 1),
    _Pm20020maMesrclientNetTxPwrIndex_Type()
)
pm20020maMesrclientNetTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxPwrIndex.setStatus("current")


class _Pm20020maMesrclientNetTxPwrPortn_Type(Integer32):
    """Custom type pm20020maMesrclientNetTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetTxPwrPortn_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetTxPwrPortn_Object = MibTableColumn
pm20020maMesrclientNetTxPwrPortn = _Pm20020maMesrclientNetTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 80, 1, 2),
    _Pm20020maMesrclientNetTxPwrPortn_Type()
)
pm20020maMesrclientNetTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetTxPwrPortn.setStatus("current")
_Pm20020maMesrclientNetRxPwrTable_Object = MibTable
pm20020maMesrclientNetRxPwrTable = _Pm20020maMesrclientNetRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetRxPwrTable.setStatus("current")
_Pm20020maMesrclientNetRxPwrEntry_Object = MibTableRow
pm20020maMesrclientNetRxPwrEntry = _Pm20020maMesrclientNetRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 112, 1)
)
pm20020maMesrclientNetRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrclientNetRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrclientNetRxPwrEntry.setStatus("current")


class _Pm20020maMesrclientNetRxPwrIndex_Type(Integer32):
    """Custom type pm20020maMesrclientNetRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrclientNetRxPwrIndex_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetRxPwrIndex_Object = MibTableColumn
pm20020maMesrclientNetRxPwrIndex = _Pm20020maMesrclientNetRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 112, 1, 1),
    _Pm20020maMesrclientNetRxPwrIndex_Type()
)
pm20020maMesrclientNetRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetRxPwrIndex.setStatus("current")


class _Pm20020maMesrclientNetRxPwrPortn_Type(Integer32):
    """Custom type pm20020maMesrclientNetRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrclientNetRxPwrPortn_Type.__name__ = "Integer32"
_Pm20020maMesrclientNetRxPwrPortn_Object = MibTableColumn
pm20020maMesrclientNetRxPwrPortn = _Pm20020maMesrclientNetRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 2, 112, 1, 2),
    _Pm20020maMesrclientNetRxPwrPortn_Type()
)
pm20020maMesrclientNetRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrclientNetRxPwrPortn.setStatus("current")
_Pm20020maMesrLine_ObjectIdentity = ObjectIdentity
pm20020maMesrLine = _Pm20020maMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3)
)


class _Pm20020maMesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm20020maMesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineMsaTemp_Object = MibScalar
pm20020maMesrlineMsaTemp = _Pm20020maMesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 12),
    _Pm20020maMesrlineMsaTemp_Type()
)
pm20020maMesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineMsaTemp.setStatus("current")


class _Pm20020maMesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm20020maMesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineMsa3v3Voltage_Object = MibScalar
pm20020maMesrlineMsa3v3Voltage = _Pm20020maMesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 13),
    _Pm20020maMesrlineMsa3v3Voltage_Type()
)
pm20020maMesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineMsa3v3Voltage.setStatus("current")


class _Pm20020maMesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm20020maMesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm20020maMesrlineSoaBiasCurrent_Object = MibScalar
pm20020maMesrlineSoaBiasCurrent = _Pm20020maMesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 14),
    _Pm20020maMesrlineSoaBiasCurrent_Type()
)
pm20020maMesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineSoaBiasCurrent.setStatus("current")
_Pm20020maMesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm20020maMesrlineNetTxLaserOutputPwrTable = _Pm20020maMesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm20020maMesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm20020maMesrlineNetTxLaserOutputPwrEntry = _Pm20020maMesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 144, 1)
)
pm20020maMesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm20020maMesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm20020maMesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm20020maMesrlineNetTxLaserOutputPwrIndex = _Pm20020maMesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 144, 1, 1),
    _Pm20020maMesrlineNetTxLaserOutputPwrIndex_Type()
)
pm20020maMesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm20020maMesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm20020maMesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm20020maMesrlineNetTxLaserOutputPwrPortn = _Pm20020maMesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 144, 1, 2),
    _Pm20020maMesrlineNetTxLaserOutputPwrPortn_Type()
)
pm20020maMesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm20020maMesrlineNetTxLaserTempTable_Object = MibTable
pm20020maMesrlineNetTxLaserTempTable = _Pm20020maMesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempTable.setStatus("current")
_Pm20020maMesrlineNetTxLaserTempEntry_Object = MibTableRow
pm20020maMesrlineNetTxLaserTempEntry = _Pm20020maMesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 148, 1)
)
pm20020maMesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm20020maMesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm20020maMesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm20020maMesrlineNetTxLaserTempIndex = _Pm20020maMesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 148, 1, 1),
    _Pm20020maMesrlineNetTxLaserTempIndex_Type()
)
pm20020maMesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm20020maMesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm20020maMesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm20020maMesrlineNetTxLaserTempPortn = _Pm20020maMesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 148, 1, 2),
    _Pm20020maMesrlineNetTxLaserTempPortn_Type()
)
pm20020maMesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxLaserTempPortn.setStatus("current")
_Pm20020maMesrlineNetTxBiasCurrentTable_Object = MibTable
pm20020maMesrlineNetTxBiasCurrentTable = _Pm20020maMesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm20020maMesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm20020maMesrlineNetTxBiasCurrentEntry = _Pm20020maMesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 152, 1)
)
pm20020maMesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm20020maMesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm20020maMesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm20020maMesrlineNetTxBiasCurrentIndex = _Pm20020maMesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 152, 1, 1),
    _Pm20020maMesrlineNetTxBiasCurrentIndex_Type()
)
pm20020maMesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm20020maMesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm20020maMesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm20020maMesrlineNetTxBiasCurrentPortn = _Pm20020maMesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 152, 1, 2),
    _Pm20020maMesrlineNetTxBiasCurrentPortn_Type()
)
pm20020maMesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm20020maMesrlineNetRxInputPwrTable_Object = MibTable
pm20020maMesrlineNetRxInputPwrTable = _Pm20020maMesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrTable.setStatus("current")
_Pm20020maMesrlineNetRxInputPwrEntry_Object = MibTableRow
pm20020maMesrlineNetRxInputPwrEntry = _Pm20020maMesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 156, 1)
)
pm20020maMesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm20020maMesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm20020maMesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm20020maMesrlineNetRxInputPwrIndex = _Pm20020maMesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 156, 1, 1),
    _Pm20020maMesrlineNetRxInputPwrIndex_Type()
)
pm20020maMesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm20020maMesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm20020maMesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm20020maMesrlineNetRxInputPwrPortn = _Pm20020maMesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 156, 1, 2),
    _Pm20020maMesrlineNetRxInputPwrPortn_Type()
)
pm20020maMesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineNetRxInputPwrPortn.setStatus("current")
_Pm20020maMesrlineResidualChromaticDispTable_Object = MibTable
pm20020maMesrlineResidualChromaticDispTable = _Pm20020maMesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispTable.setStatus("current")
_Pm20020maMesrlineResidualChromaticDispEntry_Object = MibTableRow
pm20020maMesrlineResidualChromaticDispEntry = _Pm20020maMesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 160, 1)
)
pm20020maMesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm20020maMesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm20020maMesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm20020maMesrlineResidualChromaticDispIndex = _Pm20020maMesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 160, 1, 1),
    _Pm20020maMesrlineResidualChromaticDispIndex_Type()
)
pm20020maMesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm20020maMesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm20020maMesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm20020maMesrlineResidualChromaticDispPortn = _Pm20020maMesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 160, 1, 2),
    _Pm20020maMesrlineResidualChromaticDispPortn_Type()
)
pm20020maMesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineResidualChromaticDispPortn.setStatus("current")
_Pm20020maMesrlineDiffGroupDelayTable_Object = MibTable
pm20020maMesrlineDiffGroupDelayTable = _Pm20020maMesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayTable.setStatus("current")
_Pm20020maMesrlineDiffGroupDelayEntry_Object = MibTableRow
pm20020maMesrlineDiffGroupDelayEntry = _Pm20020maMesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 164, 1)
)
pm20020maMesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm20020maMesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm20020maMesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm20020maMesrlineDiffGroupDelayIndex = _Pm20020maMesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 164, 1, 1),
    _Pm20020maMesrlineDiffGroupDelayIndex_Type()
)
pm20020maMesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm20020maMesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm20020maMesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm20020maMesrlineDiffGroupDelayPortn = _Pm20020maMesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 164, 1, 2),
    _Pm20020maMesrlineDiffGroupDelayPortn_Type()
)
pm20020maMesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineDiffGroupDelayPortn.setStatus("current")
_Pm20020maMesrlineQFactorTable_Object = MibTable
pm20020maMesrlineQFactorTable = _Pm20020maMesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 168)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorTable.setStatus("current")
_Pm20020maMesrlineQFactorEntry_Object = MibTableRow
pm20020maMesrlineQFactorEntry = _Pm20020maMesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 168, 1)
)
pm20020maMesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorEntry.setStatus("current")


class _Pm20020maMesrlineQFactorIndex_Type(Integer32):
    """Custom type pm20020maMesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineQFactorIndex_Object = MibTableColumn
pm20020maMesrlineQFactorIndex = _Pm20020maMesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 168, 1, 1),
    _Pm20020maMesrlineQFactorIndex_Type()
)
pm20020maMesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorIndex.setStatus("current")


class _Pm20020maMesrlineQFactorPortn_Type(Integer32):
    """Custom type pm20020maMesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineQFactorPortn_Object = MibTableColumn
pm20020maMesrlineQFactorPortn = _Pm20020maMesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 168, 1, 2),
    _Pm20020maMesrlineQFactorPortn_Type()
)
pm20020maMesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineQFactorPortn.setStatus("current")
_Pm20020maMesrlineCarrierFreqOffsetTable_Object = MibTable
pm20020maMesrlineCarrierFreqOffsetTable = _Pm20020maMesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 172)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm20020maMesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm20020maMesrlineCarrierFreqOffsetEntry = _Pm20020maMesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 172, 1)
)
pm20020maMesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm20020maMesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm20020maMesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm20020maMesrlineCarrierFreqOffsetIndex = _Pm20020maMesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 172, 1, 1),
    _Pm20020maMesrlineCarrierFreqOffsetIndex_Type()
)
pm20020maMesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm20020maMesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm20020maMesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm20020maMesrlineCarrierFreqOffsetPortn = _Pm20020maMesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 172, 1, 2),
    _Pm20020maMesrlineCarrierFreqOffsetPortn_Type()
)
pm20020maMesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm20020maMesrlineOsnrTable_Object = MibTable
pm20020maMesrlineOsnrTable = _Pm20020maMesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 176)
)
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrTable.setStatus("current")
_Pm20020maMesrlineOsnrEntry_Object = MibTableRow
pm20020maMesrlineOsnrEntry = _Pm20020maMesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 176, 1)
)
pm20020maMesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrEntry.setStatus("current")


class _Pm20020maMesrlineOsnrIndex_Type(Integer32):
    """Custom type pm20020maMesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm20020maMesrlineOsnrIndex_Object = MibTableColumn
pm20020maMesrlineOsnrIndex = _Pm20020maMesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 176, 1, 1),
    _Pm20020maMesrlineOsnrIndex_Type()
)
pm20020maMesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrIndex.setStatus("current")


class _Pm20020maMesrlineOsnrPortn_Type(Integer32):
    """Custom type pm20020maMesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm20020maMesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm20020maMesrlineOsnrPortn_Object = MibTableColumn
pm20020maMesrlineOsnrPortn = _Pm20020maMesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 3, 3, 176, 1, 2),
    _Pm20020maMesrlineOsnrPortn_Type()
)
pm20020maMesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMesrlineOsnrPortn.setStatus("current")
_Pm20020macounters_ObjectIdentity = ObjectIdentity
pm20020macounters = _Pm20020macounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4)
)
_Pm20020maCntOther_ObjectIdentity = ObjectIdentity
pm20020maCntOther = _Pm20020maCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 1)
)
_Pm20020maCntClient_ObjectIdentity = ObjectIdentity
pm20020maCntClient = _Pm20020maCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2)
)
_Pm20020maCntclientInputErrorCounterTable_Object = MibTable
pm20020maCntclientInputErrorCounterTable = _Pm20020maCntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 112)
)
if mibBuilder.loadTexts:
    pm20020maCntclientInputErrorCounterTable.setStatus("current")
_Pm20020maCntclientInputErrorCounterEntry_Object = MibTableRow
pm20020maCntclientInputErrorCounterEntry = _Pm20020maCntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 112, 1)
)
pm20020maCntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntclientInputErrorCounterEntry.setStatus("current")


class _Pm20020maCntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm20020maCntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntclientInputErrorCounterIndex_Object = MibTableColumn
pm20020maCntclientInputErrorCounterIndex = _Pm20020maCntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 112, 1, 1),
    _Pm20020maCntclientInputErrorCounterIndex_Type()
)
pm20020maCntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientInputErrorCounterIndex.setStatus("current")
_Pm20020maCntclientInputErrorCounterValuePortn_Type = Counter32
_Pm20020maCntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm20020maCntclientInputErrorCounterValuePortn = _Pm20020maCntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 112, 1, 2),
    _Pm20020maCntclientInputErrorCounterValuePortn_Type()
)
pm20020maCntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientInputErrorCounterValuePortn.setStatus("current")
_Pm20020maCntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm20020maCntclientInputErrorCounterErrorPortn = _Pm20020maCntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 112, 1, 3),
    _Pm20020maCntclientInputErrorCounterErrorPortn_Type()
)
pm20020maCntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm20020maCntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm20020maCntclientInputErrorCounterOverloadPortn = _Pm20020maCntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 112, 1, 4),
    _Pm20020maCntclientInputErrorCounterOverloadPortn_Type()
)
pm20020maCntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm20020maCntclientCbipCounterTable_Object = MibTable
pm20020maCntclientCbipCounterTable = _Pm20020maCntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 144)
)
if mibBuilder.loadTexts:
    pm20020maCntclientCbipCounterTable.setStatus("current")
_Pm20020maCntclientCbipCounterEntry_Object = MibTableRow
pm20020maCntclientCbipCounterEntry = _Pm20020maCntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 144, 1)
)
pm20020maCntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntclientCbipCounterEntry.setStatus("current")


class _Pm20020maCntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm20020maCntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntclientCbipCounterIndex_Object = MibTableColumn
pm20020maCntclientCbipCounterIndex = _Pm20020maCntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 144, 1, 1),
    _Pm20020maCntclientCbipCounterIndex_Type()
)
pm20020maCntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientCbipCounterIndex.setStatus("current")
_Pm20020maCntclientCbipCounterValuePortn_Type = Counter32
_Pm20020maCntclientCbipCounterValuePortn_Object = MibTableColumn
pm20020maCntclientCbipCounterValuePortn = _Pm20020maCntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 144, 1, 2),
    _Pm20020maCntclientCbipCounterValuePortn_Type()
)
pm20020maCntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientCbipCounterValuePortn.setStatus("current")
_Pm20020maCntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntclientCbipCounterErrorPortn_Object = MibTableColumn
pm20020maCntclientCbipCounterErrorPortn = _Pm20020maCntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 144, 1, 3),
    _Pm20020maCntclientCbipCounterErrorPortn_Type()
)
pm20020maCntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientCbipCounterErrorPortn.setStatus("current")
_Pm20020maCntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm20020maCntclientCbipCounterOverloadPortn = _Pm20020maCntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 2, 144, 1, 4),
    _Pm20020maCntclientCbipCounterOverloadPortn_Type()
)
pm20020maCntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntclientCbipCounterOverloadPortn.setStatus("current")
_Pm20020maCntLine_ObjectIdentity = ObjectIdentity
pm20020maCntLine = _Pm20020maCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3)
)
_Pm20020maCntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm20020maCntlocalLineSmBip8ErrorCounterTable = _Pm20020maCntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm20020maCntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm20020maCntlocalLineSmBip8ErrorCounterEntry = _Pm20020maCntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 192, 1)
)
pm20020maCntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm20020maCntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm20020maCntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm20020maCntlocalLineSmBip8ErrorCounterIndex = _Pm20020maCntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 192, 1, 1),
    _Pm20020maCntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm20020maCntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm20020maCntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm20020maCntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm20020maCntlocalLineSmBip8ErrorCounterValuePortn = _Pm20020maCntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 192, 1, 2),
    _Pm20020maCntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm20020maCntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn = _Pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 192, 1, 3),
    _Pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 192, 1, 4),
    _Pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm20020maCntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm20020maCntlocalLineFecCorrectedErrorsCounterTable = _Pm20020maCntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm20020maCntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm20020maCntlocalLineFecCorrectedErrorsCounterEntry = _Pm20020maCntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 193, 1)
)
pm20020maCntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm20020maCntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm20020maCntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm20020maCntlocalLineFecCorrectedErrorsCounterIndex = _Pm20020maCntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 193, 1, 1),
    _Pm20020maCntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm20020maCntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 193, 1, 2),
    _Pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 193, 1, 3),
    _Pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 193, 1, 4),
    _Pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm20020maCntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm20020maCntremoteLineSmBip8ErrorCounterTable = _Pm20020maCntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm20020maCntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm20020maCntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm20020maCntremoteLineSmBip8ErrorCounterEntry = _Pm20020maCntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 194, 1)
)
pm20020maCntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm20020maCntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm20020maCntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm20020maCntremoteLineSmBip8ErrorCounterIndex = _Pm20020maCntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 194, 1, 1),
    _Pm20020maCntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm20020maCntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm20020maCntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm20020maCntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm20020maCntremoteLineSmBip8ErrorCounterValuePortn = _Pm20020maCntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 194, 1, 2),
    _Pm20020maCntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm20020maCntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn = _Pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 194, 1, 3),
    _Pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 194, 1, 4),
    _Pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm20020maCntlineDfrmTimCntTable_Object = MibTable
pm20020maCntlineDfrmTimCntTable = _Pm20020maCntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm20020maCntlineDfrmTimCntTable.setStatus("current")
_Pm20020maCntlineDfrmTimCntEntry_Object = MibTableRow
pm20020maCntlineDfrmTimCntEntry = _Pm20020maCntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 195, 1)
)
pm20020maCntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlineDfrmTimCntEntry.setStatus("current")


class _Pm20020maCntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm20020maCntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm20020maCntlineDfrmTimCntIndex_Object = MibTableColumn
pm20020maCntlineDfrmTimCntIndex = _Pm20020maCntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 195, 1, 1),
    _Pm20020maCntlineDfrmTimCntIndex_Type()
)
pm20020maCntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlineDfrmTimCntIndex.setStatus("current")
_Pm20020maCntlineDfrmTimCntValuePortn_Type = Counter64
_Pm20020maCntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm20020maCntlineDfrmTimCntValuePortn = _Pm20020maCntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 195, 1, 2),
    _Pm20020maCntlineDfrmTimCntValuePortn_Type()
)
pm20020maCntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlineDfrmTimCntValuePortn.setStatus("current")
_Pm20020maCntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm20020maCntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm20020maCntlineDfrmTimCntErrorPortn = _Pm20020maCntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 195, 1, 3),
    _Pm20020maCntlineDfrmTimCntErrorPortn_Type()
)
pm20020maCntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm20020maCntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm20020maCntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm20020maCntlineDfrmTimCntOverloadPortn = _Pm20020maCntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 195, 1, 4),
    _Pm20020maCntlineDfrmTimCntOverloadPortn_Type()
)
pm20020maCntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterTable_Object = MibTable
pm20020maCntlocalLineTrscvPreSdFecErrorCounterTable = _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecErrorCounterTable.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry_Object = MibTableRow
pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry = _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 196, 1)
)
pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry.setStatus("current")


class _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex = _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 196, 1, 1),
    _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex_Type()
)
pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type = Counter64
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn = _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 196, 1, 2),
    _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type()
)
pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn = _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 196, 1, 3),
    _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type()
)
pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn = _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 196, 1, 4),
    _Pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type()
)
pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object = MibTable
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable = _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object = MibTableRow
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry = _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 197, 1)
)
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setStatus("current")


class _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex = _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 197, 1, 1),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type = Counter64
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn = _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 197, 1, 2),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn = _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 197, 1, 3),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn = _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 197, 1, 4),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterTable_Object = MibTable
pm20020maCntlocalLineTrscvPreSdFecBitCounterTable = _Pm20020maCntlocalLineTrscvPreSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 198)
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecBitCounterTable.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry_Object = MibTableRow
pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry = _Pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 198, 1)
)
pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry.setStatus("current")


class _Pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex = _Pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 198, 1, 1),
    _Pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex_Type()
)
pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Type = Counter64
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn = _Pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 198, 1, 2),
    _Pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn_Type()
)
pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn = _Pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 198, 1, 3),
    _Pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type()
)
pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn = _Pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 198, 1, 4),
    _Pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type()
)
pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object = MibTable
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterTable = _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 199)
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterTable.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object = MibTableRow
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry = _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 199, 1)
)
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setStatus("current")


class _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex = _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 199, 1, 1),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type = Counter64
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn = _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 199, 1, 2),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn = _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 199, 1, 3),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setStatus("current")
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn = _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 4, 3, 199, 1, 4),
    _Pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type()
)
pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setStatus("current")
_Pm20020macontrolsWrite_ObjectIdentity = ObjectIdentity
pm20020macontrolsWrite = _Pm20020macontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6)
)
_Pm20020maCtrlOther_ObjectIdentity = ObjectIdentity
pm20020maCtrlOther = _Pm20020maCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1)
)
_Pm20020maCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm20020maCtrlconfMgnt1 = _Pm20020maCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 1)
)
_Pm20020maCtrlConf1Load1_Type = EkiOnOff
_Pm20020maCtrlConf1Load1_Object = MibScalar
pm20020maCtrlConf1Load1 = _Pm20020maCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 1, 1),
    _Pm20020maCtrlConf1Load1_Type()
)
pm20020maCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlConf1Load1.setStatus("current")
_Pm20020maCtrlConf2Load1_Type = EkiOnOff
_Pm20020maCtrlConf2Load1_Object = MibScalar
pm20020maCtrlConf2Load1 = _Pm20020maCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 1, 2),
    _Pm20020maCtrlConf2Load1_Type()
)
pm20020maCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlConf2Load1.setStatus("current")
_Pm20020maCtrlConf2Flash1_Type = EkiOnOff
_Pm20020maCtrlConf2Flash1_Object = MibScalar
pm20020maCtrlConf2Flash1 = _Pm20020maCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 1, 10),
    _Pm20020maCtrlConf2Flash1_Type()
)
pm20020maCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlConf2Flash1.setStatus("current")
_Pm20020maCtrlConf2Clear1_Type = EkiOnOff
_Pm20020maCtrlConf2Clear1_Object = MibScalar
pm20020maCtrlConf2Clear1 = _Pm20020maCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 1, 14),
    _Pm20020maCtrlConf2Clear1_Type()
)
pm20020maCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlConf2Clear1.setStatus("current")
_Pm20020maCtrlsynth4_ObjectIdentity = ObjectIdentity
pm20020maCtrlsynth4 = _Pm20020maCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 4)
)
_Pm20020maCtrlCorrelatOn_Type = EkiOnOff
_Pm20020maCtrlCorrelatOn_Object = MibScalar
pm20020maCtrlCorrelatOn = _Pm20020maCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 4, 1),
    _Pm20020maCtrlCorrelatOn_Type()
)
pm20020maCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlCorrelatOn.setStatus("current")
_Pm20020maCtrlCorrelatOff_Type = EkiOnOff
_Pm20020maCtrlCorrelatOff_Object = MibScalar
pm20020maCtrlCorrelatOff = _Pm20020maCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 4, 2),
    _Pm20020maCtrlCorrelatOff_Type()
)
pm20020maCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlCorrelatOff.setStatus("current")
_Pm20020maCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm20020maCtrlswMgnt = _Pm20020maCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 5)
)
_Pm20020maCtrlColdReset_Type = EkiOnOff
_Pm20020maCtrlColdReset_Object = MibScalar
pm20020maCtrlColdReset = _Pm20020maCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 5, 2),
    _Pm20020maCtrlColdReset_Type()
)
pm20020maCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlColdReset.setStatus("current")
_Pm20020maCtrlWarmReset_Type = EkiOnOff
_Pm20020maCtrlWarmReset_Object = MibScalar
pm20020maCtrlWarmReset = _Pm20020maCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 5, 3),
    _Pm20020maCtrlWarmReset_Type()
)
pm20020maCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlWarmReset.setStatus("current")
_Pm20020maCtrlLoadSwBank1_Type = EkiOnOff
_Pm20020maCtrlLoadSwBank1_Object = MibScalar
pm20020maCtrlLoadSwBank1 = _Pm20020maCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 5, 5),
    _Pm20020maCtrlLoadSwBank1_Type()
)
pm20020maCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLoadSwBank1.setStatus("current")
_Pm20020maCtrlLoadSwBank2_Type = EkiOnOff
_Pm20020maCtrlLoadSwBank2_Object = MibScalar
pm20020maCtrlLoadSwBank2 = _Pm20020maCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 5, 6),
    _Pm20020maCtrlLoadSwBank2_Type()
)
pm20020maCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLoadSwBank2.setStatus("current")
_Pm20020maCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm20020maCtrlgwMgnt = _Pm20020maCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 6)
)
_Pm20020maCtrlCurrentGwReset_Type = EkiOnOff
_Pm20020maCtrlCurrentGwReset_Object = MibScalar
pm20020maCtrlCurrentGwReset = _Pm20020maCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 6, 1),
    _Pm20020maCtrlCurrentGwReset_Type()
)
pm20020maCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlCurrentGwReset.setStatus("current")
_Pm20020maCtrlLoadGwBank1_Type = EkiOnOff
_Pm20020maCtrlLoadGwBank1_Object = MibScalar
pm20020maCtrlLoadGwBank1 = _Pm20020maCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 6, 5),
    _Pm20020maCtrlLoadGwBank1_Type()
)
pm20020maCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLoadGwBank1.setStatus("current")
_Pm20020maCtrlLoadGwBank2_Type = EkiOnOff
_Pm20020maCtrlLoadGwBank2_Object = MibScalar
pm20020maCtrlLoadGwBank2 = _Pm20020maCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 6, 6),
    _Pm20020maCtrlLoadGwBank2_Type()
)
pm20020maCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLoadGwBank2.setStatus("current")
_Pm20020maCtrlLoadGwBank3_Type = EkiOnOff
_Pm20020maCtrlLoadGwBank3_Object = MibScalar
pm20020maCtrlLoadGwBank3 = _Pm20020maCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 6, 7),
    _Pm20020maCtrlLoadGwBank3_Type()
)
pm20020maCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLoadGwBank3.setStatus("current")
_Pm20020maCtrlLoadGwBank4_Type = EkiOnOff
_Pm20020maCtrlLoadGwBank4_Object = MibScalar
pm20020maCtrlLoadGwBank4 = _Pm20020maCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 6, 8),
    _Pm20020maCtrlLoadGwBank4_Type()
)
pm20020maCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLoadGwBank4.setStatus("current")
_Pm20020maCtrlledTest_ObjectIdentity = ObjectIdentity
pm20020maCtrlledTest = _Pm20020maCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 192)
)
_Pm20020maCtrlGreenLed_Type = EkiOnOff
_Pm20020maCtrlGreenLed_Object = MibScalar
pm20020maCtrlGreenLed = _Pm20020maCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 192, 1),
    _Pm20020maCtrlGreenLed_Type()
)
pm20020maCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlGreenLed.setStatus("current")
_Pm20020maCtrlRedLed_Type = EkiOnOff
_Pm20020maCtrlRedLed_Object = MibScalar
pm20020maCtrlRedLed = _Pm20020maCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 192, 2),
    _Pm20020maCtrlRedLed_Type()
)
pm20020maCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlRedLed.setStatus("current")
_Pm20020maCtrlLedOff_Type = EkiOnOff
_Pm20020maCtrlLedOff_Object = MibScalar
pm20020maCtrlLedOff = _Pm20020maCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 192, 3),
    _Pm20020maCtrlLedOff_Type()
)
pm20020maCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlLedOff.setStatus("current")
_Pm20020maCtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm20020maCtrlinitSwitchMarvell = _Pm20020maCtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 201)
)
_Pm20020maCtrlInitSwitchMarvell_Type = EkiOnOff
_Pm20020maCtrlInitSwitchMarvell_Object = MibScalar
pm20020maCtrlInitSwitchMarvell = _Pm20020maCtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 201, 1),
    _Pm20020maCtrlInitSwitchMarvell_Type()
)
pm20020maCtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlInitSwitchMarvell.setStatus("current")
_Pm20020maCtrlresetCount_ObjectIdentity = ObjectIdentity
pm20020maCtrlresetCount = _Pm20020maCtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 259)
)
_Pm20020maCtrlResetcount_Type = EkiOnOff
_Pm20020maCtrlResetcount_Object = MibScalar
pm20020maCtrlResetcount = _Pm20020maCtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 259, 1),
    _Pm20020maCtrlResetcount_Type()
)
pm20020maCtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlResetcount.setStatus("current")
_Pm20020maCtrlresetRmon_ObjectIdentity = ObjectIdentity
pm20020maCtrlresetRmon = _Pm20020maCtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 260)
)
_Pm20020maCtrlResetrmon_Type = EkiOnOff
_Pm20020maCtrlResetrmon_Object = MibScalar
pm20020maCtrlResetrmon = _Pm20020maCtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 260, 1),
    _Pm20020maCtrlResetrmon_Type()
)
pm20020maCtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlResetrmon.setStatus("current")
_Pm20020maCtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm20020maCtrlresetMeasurements = _Pm20020maCtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 261)
)
_Pm20020maCtrlResetmeasurements_Type = EkiOnOff
_Pm20020maCtrlResetmeasurements_Object = MibScalar
pm20020maCtrlResetmeasurements = _Pm20020maCtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 1, 261, 1),
    _Pm20020maCtrlResetmeasurements_Type()
)
pm20020maCtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlResetmeasurements.setStatus("current")
_Pm20020maCtrlClient_ObjectIdentity = ObjectIdentity
pm20020maCtrlClient = _Pm20020maCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2)
)
_Pm20020maCtrlaccessLoopTable_Object = MibTable
pm20020maCtrlaccessLoopTable = _Pm20020maCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm20020maCtrlaccessLoopTable.setStatus("current")
_Pm20020maCtrlaccessLoopEntry_Object = MibTableRow
pm20020maCtrlaccessLoopEntry = _Pm20020maCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 16, 1)
)
pm20020maCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlaccessLoopEntry.setStatus("current")


class _Pm20020maCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm20020maCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlaccessLoopIndex_Object = MibTableColumn
pm20020maCtrlaccessLoopIndex = _Pm20020maCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 16, 1, 1),
    _Pm20020maCtrlaccessLoopIndex_Type()
)
pm20020maCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlaccessLoopIndex.setStatus("current")
_Pm20020maCtrlaccessLoopPortn_Type = EkiState
_Pm20020maCtrlaccessLoopPortn_Object = MibTableColumn
pm20020maCtrlaccessLoopPortn = _Pm20020maCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 16, 1, 2),
    _Pm20020maCtrlaccessLoopPortn_Type()
)
pm20020maCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlaccessLoopPortn.setStatus("current")
_Pm20020maCtrlclientLoopToLineTable_Object = MibTable
pm20020maCtrlclientLoopToLineTable = _Pm20020maCtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm20020maCtrlclientLoopToLineTable.setStatus("current")
_Pm20020maCtrlclientLoopToLineEntry_Object = MibTableRow
pm20020maCtrlclientLoopToLineEntry = _Pm20020maCtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 17, 1)
)
pm20020maCtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlclientLoopToLineEntry.setStatus("current")


class _Pm20020maCtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm20020maCtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlclientLoopToLineIndex_Object = MibTableColumn
pm20020maCtrlclientLoopToLineIndex = _Pm20020maCtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 17, 1, 1),
    _Pm20020maCtrlclientLoopToLineIndex_Type()
)
pm20020maCtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlclientLoopToLineIndex.setStatus("current")
_Pm20020maCtrlclientLoopToLinePortn_Type = EkiState
_Pm20020maCtrlclientLoopToLinePortn_Object = MibTableColumn
pm20020maCtrlclientLoopToLinePortn = _Pm20020maCtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 17, 1, 2),
    _Pm20020maCtrlclientLoopToLinePortn_Type()
)
pm20020maCtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlclientLoopToLinePortn.setStatus("current")
_Pm20020maCtrlcsfUpInsTable_Object = MibTable
pm20020maCtrlcsfUpInsTable = _Pm20020maCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm20020maCtrlcsfUpInsTable.setStatus("current")
_Pm20020maCtrlcsfUpInsEntry_Object = MibTableRow
pm20020maCtrlcsfUpInsEntry = _Pm20020maCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 21, 1)
)
pm20020maCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlcsfUpInsEntry.setStatus("current")


class _Pm20020maCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm20020maCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlcsfUpInsIndex_Object = MibTableColumn
pm20020maCtrlcsfUpInsIndex = _Pm20020maCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 21, 1, 1),
    _Pm20020maCtrlcsfUpInsIndex_Type()
)
pm20020maCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlcsfUpInsIndex.setStatus("current")
_Pm20020maCtrlcsfUpInsPortn_Type = EkiState
_Pm20020maCtrlcsfUpInsPortn_Object = MibTableColumn
pm20020maCtrlcsfUpInsPortn = _Pm20020maCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 21, 1, 2),
    _Pm20020maCtrlcsfUpInsPortn_Type()
)
pm20020maCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlcsfUpInsPortn.setStatus("current")
_Pm20020maCtrlcaisDwInsTable_Object = MibTable
pm20020maCtrlcaisDwInsTable = _Pm20020maCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm20020maCtrlcaisDwInsTable.setStatus("current")
_Pm20020maCtrlcaisDwInsEntry_Object = MibTableRow
pm20020maCtrlcaisDwInsEntry = _Pm20020maCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 22, 1)
)
pm20020maCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlcaisDwInsEntry.setStatus("current")


class _Pm20020maCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm20020maCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlcaisDwInsIndex_Object = MibTableColumn
pm20020maCtrlcaisDwInsIndex = _Pm20020maCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 22, 1, 1),
    _Pm20020maCtrlcaisDwInsIndex_Type()
)
pm20020maCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlcaisDwInsIndex.setStatus("current")
_Pm20020maCtrlcaisDwInsPortn_Type = EkiState
_Pm20020maCtrlcaisDwInsPortn_Object = MibTableColumn
pm20020maCtrlcaisDwInsPortn = _Pm20020maCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 22, 1, 2),
    _Pm20020maCtrlcaisDwInsPortn_Type()
)
pm20020maCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlcaisDwInsPortn.setStatus("current")
_Pm20020maCtrlclientResetAllCountTable_Object = MibTable
pm20020maCtrlclientResetAllCountTable = _Pm20020maCtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm20020maCtrlclientResetAllCountTable.setStatus("current")
_Pm20020maCtrlclientResetAllCountEntry_Object = MibTableRow
pm20020maCtrlclientResetAllCountEntry = _Pm20020maCtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 262, 1)
)
pm20020maCtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlclientResetAllCountEntry.setStatus("current")


class _Pm20020maCtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm20020maCtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlclientResetAllCountIndex_Object = MibTableColumn
pm20020maCtrlclientResetAllCountIndex = _Pm20020maCtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 262, 1, 1),
    _Pm20020maCtrlclientResetAllCountIndex_Type()
)
pm20020maCtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlclientResetAllCountIndex.setStatus("current")
_Pm20020maCtrlclientResetAllCountsPortn_Type = EkiState
_Pm20020maCtrlclientResetAllCountsPortn_Object = MibTableColumn
pm20020maCtrlclientResetAllCountsPortn = _Pm20020maCtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 2, 262, 1, 2),
    _Pm20020maCtrlclientResetAllCountsPortn_Type()
)
pm20020maCtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlclientResetAllCountsPortn.setStatus("current")
_Pm20020maCtrlLine_ObjectIdentity = ObjectIdentity
pm20020maCtrlLine = _Pm20020maCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3)
)
_Pm20020maCtrlcommAccessLoopTable_Object = MibTable
pm20020maCtrlcommAccessLoopTable = _Pm20020maCtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm20020maCtrlcommAccessLoopTable.setStatus("current")
_Pm20020maCtrlcommAccessLoopEntry_Object = MibTableRow
pm20020maCtrlcommAccessLoopEntry = _Pm20020maCtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 64, 1)
)
pm20020maCtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlcommAccessLoopEntry.setStatus("current")


class _Pm20020maCtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm20020maCtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlcommAccessLoopIndex_Object = MibTableColumn
pm20020maCtrlcommAccessLoopIndex = _Pm20020maCtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 64, 1, 1),
    _Pm20020maCtrlcommAccessLoopIndex_Type()
)
pm20020maCtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlcommAccessLoopIndex.setStatus("current")
_Pm20020maCtrlcommAccessLoopPortn_Type = EkiState
_Pm20020maCtrlcommAccessLoopPortn_Object = MibTableColumn
pm20020maCtrlcommAccessLoopPortn = _Pm20020maCtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 64, 1, 2),
    _Pm20020maCtrlcommAccessLoopPortn_Type()
)
pm20020maCtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlcommAccessLoopPortn.setStatus("current")
_Pm20020maCtrllineLoopTable_Object = MibTable
pm20020maCtrllineLoopTable = _Pm20020maCtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm20020maCtrllineLoopTable.setStatus("current")
_Pm20020maCtrllineLoopEntry_Object = MibTableRow
pm20020maCtrllineLoopEntry = _Pm20020maCtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 66, 1)
)
pm20020maCtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrllineLoopEntry.setStatus("current")


class _Pm20020maCtrllineLoopIndex_Type(Integer32):
    """Custom type pm20020maCtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm20020maCtrllineLoopIndex_Object = MibTableColumn
pm20020maCtrllineLoopIndex = _Pm20020maCtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 66, 1, 1),
    _Pm20020maCtrllineLoopIndex_Type()
)
pm20020maCtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrllineLoopIndex.setStatus("current")
_Pm20020maCtrllineLoopPortn_Type = EkiState
_Pm20020maCtrllineLoopPortn_Object = MibTableColumn
pm20020maCtrllineLoopPortn = _Pm20020maCtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 66, 1, 2),
    _Pm20020maCtrllineLoopPortn_Type()
)
pm20020maCtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrllineLoopPortn.setStatus("current")
_Pm20020maCtrlfecDisableTable_Object = MibTable
pm20020maCtrlfecDisableTable = _Pm20020maCtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm20020maCtrlfecDisableTable.setStatus("current")
_Pm20020maCtrlfecDisableEntry_Object = MibTableRow
pm20020maCtrlfecDisableEntry = _Pm20020maCtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 69, 1)
)
pm20020maCtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlfecDisableEntry.setStatus("current")


class _Pm20020maCtrlfecDisableIndex_Type(Integer32):
    """Custom type pm20020maCtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlfecDisableIndex_Object = MibTableColumn
pm20020maCtrlfecDisableIndex = _Pm20020maCtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 69, 1, 1),
    _Pm20020maCtrlfecDisableIndex_Type()
)
pm20020maCtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlfecDisableIndex.setStatus("current")
_Pm20020maCtrlfecDisablePortn_Type = EkiState
_Pm20020maCtrlfecDisablePortn_Object = MibTableColumn
pm20020maCtrlfecDisablePortn = _Pm20020maCtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 69, 1, 2),
    _Pm20020maCtrlfecDisablePortn_Type()
)
pm20020maCtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlfecDisablePortn.setStatus("current")
_Pm20020maCtrlmsaLineLoopTable_Object = MibTable
pm20020maCtrlmsaLineLoopTable = _Pm20020maCtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaLineLoopTable.setStatus("current")
_Pm20020maCtrlmsaLineLoopEntry_Object = MibTableRow
pm20020maCtrlmsaLineLoopEntry = _Pm20020maCtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 209, 1)
)
pm20020maCtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaLineLoopEntry.setStatus("current")


class _Pm20020maCtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm20020maCtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlmsaLineLoopIndex_Object = MibTableColumn
pm20020maCtrlmsaLineLoopIndex = _Pm20020maCtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 209, 1, 1),
    _Pm20020maCtrlmsaLineLoopIndex_Type()
)
pm20020maCtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaLineLoopIndex.setStatus("current")
_Pm20020maCtrlmsaLineLoopPortn_Type = EkiState
_Pm20020maCtrlmsaLineLoopPortn_Object = MibTableColumn
pm20020maCtrlmsaLineLoopPortn = _Pm20020maCtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 209, 1, 2),
    _Pm20020maCtrlmsaLineLoopPortn_Type()
)
pm20020maCtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaLineLoopPortn.setStatus("current")
_Pm20020maCtrlmsaTxResetTable_Object = MibTable
pm20020maCtrlmsaTxResetTable = _Pm20020maCtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaTxResetTable.setStatus("current")
_Pm20020maCtrlmsaTxResetEntry_Object = MibTableRow
pm20020maCtrlmsaTxResetEntry = _Pm20020maCtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 210, 1)
)
pm20020maCtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaTxResetEntry.setStatus("current")


class _Pm20020maCtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm20020maCtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlmsaTxResetIndex_Object = MibTableColumn
pm20020maCtrlmsaTxResetIndex = _Pm20020maCtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 210, 1, 1),
    _Pm20020maCtrlmsaTxResetIndex_Type()
)
pm20020maCtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaTxResetIndex.setStatus("current")
_Pm20020maCtrlmsaTxResetPortn_Type = EkiState
_Pm20020maCtrlmsaTxResetPortn_Object = MibTableColumn
pm20020maCtrlmsaTxResetPortn = _Pm20020maCtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 210, 1, 2),
    _Pm20020maCtrlmsaTxResetPortn_Type()
)
pm20020maCtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaTxResetPortn.setStatus("current")
_Pm20020maCtrlmsaRxResetTable_Object = MibTable
pm20020maCtrlmsaRxResetTable = _Pm20020maCtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaRxResetTable.setStatus("current")
_Pm20020maCtrlmsaRxResetEntry_Object = MibTableRow
pm20020maCtrlmsaRxResetEntry = _Pm20020maCtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 211, 1)
)
pm20020maCtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaRxResetEntry.setStatus("current")


class _Pm20020maCtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm20020maCtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlmsaRxResetIndex_Object = MibTableColumn
pm20020maCtrlmsaRxResetIndex = _Pm20020maCtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 211, 1, 1),
    _Pm20020maCtrlmsaRxResetIndex_Type()
)
pm20020maCtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaRxResetIndex.setStatus("current")
_Pm20020maCtrlmsaRxResetPortn_Type = EkiState
_Pm20020maCtrlmsaRxResetPortn_Object = MibTableColumn
pm20020maCtrlmsaRxResetPortn = _Pm20020maCtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 211, 1, 2),
    _Pm20020maCtrlmsaRxResetPortn_Type()
)
pm20020maCtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaRxResetPortn.setStatus("current")
_Pm20020maCtrlmsaShutdownTable_Object = MibTable
pm20020maCtrlmsaShutdownTable = _Pm20020maCtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaShutdownTable.setStatus("current")
_Pm20020maCtrlmsaShutdownEntry_Object = MibTableRow
pm20020maCtrlmsaShutdownEntry = _Pm20020maCtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 212, 1)
)
pm20020maCtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrlmsaShutdownEntry.setStatus("current")


class _Pm20020maCtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm20020maCtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm20020maCtrlmsaShutdownIndex_Object = MibTableColumn
pm20020maCtrlmsaShutdownIndex = _Pm20020maCtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 212, 1, 1),
    _Pm20020maCtrlmsaShutdownIndex_Type()
)
pm20020maCtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaShutdownIndex.setStatus("current")
_Pm20020maCtrlmsaShutdownPortn_Type = EkiState
_Pm20020maCtrlmsaShutdownPortn_Object = MibTableColumn
pm20020maCtrlmsaShutdownPortn = _Pm20020maCtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 212, 1, 2),
    _Pm20020maCtrlmsaShutdownPortn_Type()
)
pm20020maCtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrlmsaShutdownPortn.setStatus("current")
_Pm20020maCtrllineResetAllCountTable_Object = MibTable
pm20020maCtrllineResetAllCountTable = _Pm20020maCtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm20020maCtrllineResetAllCountTable.setStatus("current")
_Pm20020maCtrllineResetAllCountEntry_Object = MibTableRow
pm20020maCtrllineResetAllCountEntry = _Pm20020maCtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 263, 1)
)
pm20020maCtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCtrllineResetAllCountEntry.setStatus("current")


class _Pm20020maCtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm20020maCtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm20020maCtrllineResetAllCountIndex_Object = MibTableColumn
pm20020maCtrllineResetAllCountIndex = _Pm20020maCtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 263, 1, 1),
    _Pm20020maCtrllineResetAllCountIndex_Type()
)
pm20020maCtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCtrllineResetAllCountIndex.setStatus("current")
_Pm20020maCtrllineResetAllCountsPortn_Type = EkiState
_Pm20020maCtrllineResetAllCountsPortn_Object = MibTableColumn
pm20020maCtrllineResetAllCountsPortn = _Pm20020maCtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 6, 3, 263, 1, 2),
    _Pm20020maCtrllineResetAllCountsPortn_Type()
)
pm20020maCtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCtrllineResetAllCountsPortn.setStatus("current")
_Pm20020mari_ObjectIdentity = ObjectIdentity
pm20020mari = _Pm20020mari_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7)
)
_Pm20020mariTable_ObjectIdentity = ObjectIdentity
pm20020mariTable = _Pm20020mariTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1)
)
_Pm20020maRinvSfpTable_Object = MibTable
pm20020maRinvSfpTable = _Pm20020maRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm20020maRinvSfpTable.setStatus("current")
_Pm20020maRinvSfpEntry_Object = MibTableRow
pm20020maRinvSfpEntry = _Pm20020maRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 1, 1)
)
pm20020maRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm20020maRinvSfpEntry.setStatus("current")


class _Pm20020maRinvSfpIndex_Type(Integer32):
    """Custom type pm20020maRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm20020maRinvSfpIndex_Type.__name__ = "Integer32"
_Pm20020maRinvSfpIndex_Object = MibTableColumn
pm20020maRinvSfpIndex = _Pm20020maRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 1, 1, 1),
    _Pm20020maRinvSfpIndex_Type()
)
pm20020maRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvSfpIndex.setStatus("current")
_Pm20020maRinvsfp_Type = DisplayString
_Pm20020maRinvsfp_Object = MibTableColumn
pm20020maRinvsfp = _Pm20020maRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 1, 1, 2),
    _Pm20020maRinvsfp_Type()
)
pm20020maRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvsfp.setStatus("current")
_Pm20020maRinvLineTable_Object = MibTable
pm20020maRinvLineTable = _Pm20020maRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm20020maRinvLineTable.setStatus("current")
_Pm20020maRinvLineEntry_Object = MibTableRow
pm20020maRinvLineEntry = _Pm20020maRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 2, 1)
)
pm20020maRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm20020maRinvLineEntry.setStatus("current")


class _Pm20020maRinvLineIndex_Type(Integer32):
    """Custom type pm20020maRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm20020maRinvLineIndex_Type.__name__ = "Integer32"
_Pm20020maRinvLineIndex_Object = MibTableColumn
pm20020maRinvLineIndex = _Pm20020maRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 2, 1, 1),
    _Pm20020maRinvLineIndex_Type()
)
pm20020maRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvLineIndex.setStatus("current")
_Pm20020maRinvxfpLine_Type = DisplayString
_Pm20020maRinvxfpLine_Object = MibTableColumn
pm20020maRinvxfpLine = _Pm20020maRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 1, 2, 1, 2),
    _Pm20020maRinvxfpLine_Type()
)
pm20020maRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvxfpLine.setStatus("current")
_Pm20020maRinvReloadInventory_Type = EkiOnOff
_Pm20020maRinvReloadInventory_Object = MibScalar
pm20020maRinvReloadInventory = _Pm20020maRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 2),
    _Pm20020maRinvReloadInventory_Type()
)
pm20020maRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maRinvReloadInventory.setStatus("current")
_Pm20020maRinvHwPlatform_Type = DisplayString
_Pm20020maRinvHwPlatform_Object = MibScalar
pm20020maRinvHwPlatform = _Pm20020maRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 3),
    _Pm20020maRinvHwPlatform_Type()
)
pm20020maRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvHwPlatform.setStatus("current")
_Pm20020maRinvModulePlatform_Type = DisplayString
_Pm20020maRinvModulePlatform_Object = MibScalar
pm20020maRinvModulePlatform = _Pm20020maRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 4),
    _Pm20020maRinvModulePlatform_Type()
)
pm20020maRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvModulePlatform.setStatus("current")
_Pm20020maRinvSwPlatform_Type = DisplayString
_Pm20020maRinvSwPlatform_Object = MibScalar
pm20020maRinvSwPlatform = _Pm20020maRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 5),
    _Pm20020maRinvSwPlatform_Type()
)
pm20020maRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvSwPlatform.setStatus("current")
_Pm20020maRinvGwPlatform_Type = DisplayString
_Pm20020maRinvGwPlatform_Object = MibScalar
pm20020maRinvGwPlatform = _Pm20020maRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 7, 6),
    _Pm20020maRinvGwPlatform_Type()
)
pm20020maRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maRinvGwPlatform.setStatus("current")
_Pm20020madownload_ObjectIdentity = ObjectIdentity
pm20020madownload = _Pm20020madownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8)
)
_Pm20020maDwlOther_ObjectIdentity = ObjectIdentity
pm20020maDwlOther = _Pm20020maDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1)
)
_Pm20020maDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm20020maDwlrestartProcess = _Pm20020maDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 0)
)
_Pm20020maDwlWarmRestartProcessed_Type = EkiOnOff
_Pm20020maDwlWarmRestartProcessed_Object = MibScalar
pm20020maDwlWarmRestartProcessed = _Pm20020maDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 0, 1),
    _Pm20020maDwlWarmRestartProcessed_Type()
)
pm20020maDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlWarmRestartProcessed.setStatus("current")
_Pm20020maDwlColdRestartProcessed_Type = EkiOnOff
_Pm20020maDwlColdRestartProcessed_Object = MibScalar
pm20020maDwlColdRestartProcessed = _Pm20020maDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 0, 2),
    _Pm20020maDwlColdRestartProcessed_Type()
)
pm20020maDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlColdRestartProcessed.setStatus("current")
_Pm20020maDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm20020maDwlswBanksUsed = _Pm20020maDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 1)
)
_Pm20020maDwlSwBank1Used_Type = EkiOnOff
_Pm20020maDwlSwBank1Used_Object = MibScalar
pm20020maDwlSwBank1Used = _Pm20020maDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 1, 1),
    _Pm20020maDwlSwBank1Used_Type()
)
pm20020maDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlSwBank1Used.setStatus("current")
_Pm20020maDwlSwBank2Used_Type = EkiOnOff
_Pm20020maDwlSwBank2Used_Object = MibScalar
pm20020maDwlSwBank2Used = _Pm20020maDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 1, 2),
    _Pm20020maDwlSwBank2Used_Type()
)
pm20020maDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlSwBank2Used.setStatus("current")
_Pm20020maDwlSwBank1Notempty_Type = EkiOnOff
_Pm20020maDwlSwBank1Notempty_Object = MibScalar
pm20020maDwlSwBank1Notempty = _Pm20020maDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 1, 5),
    _Pm20020maDwlSwBank1Notempty_Type()
)
pm20020maDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlSwBank1Notempty.setStatus("current")
_Pm20020maDwlSwBank2Notempty_Type = EkiOnOff
_Pm20020maDwlSwBank2Notempty_Object = MibScalar
pm20020maDwlSwBank2Notempty = _Pm20020maDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 1, 6),
    _Pm20020maDwlSwBank2Notempty_Type()
)
pm20020maDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlSwBank2Notempty.setStatus("current")
_Pm20020maDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm20020maDwlgwBanksUsed = _Pm20020maDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2)
)
_Pm20020maDwlGwBank1Used_Type = EkiOnOff
_Pm20020maDwlGwBank1Used_Object = MibScalar
pm20020maDwlGwBank1Used = _Pm20020maDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 1),
    _Pm20020maDwlGwBank1Used_Type()
)
pm20020maDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank1Used.setStatus("current")
_Pm20020maDwlGwBank2Used_Type = EkiOnOff
_Pm20020maDwlGwBank2Used_Object = MibScalar
pm20020maDwlGwBank2Used = _Pm20020maDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 2),
    _Pm20020maDwlGwBank2Used_Type()
)
pm20020maDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank2Used.setStatus("current")
_Pm20020maDwlGwBank3Used_Type = EkiOnOff
_Pm20020maDwlGwBank3Used_Object = MibScalar
pm20020maDwlGwBank3Used = _Pm20020maDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 3),
    _Pm20020maDwlGwBank3Used_Type()
)
pm20020maDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank3Used.setStatus("current")
_Pm20020maDwlGwBank4Used_Type = EkiOnOff
_Pm20020maDwlGwBank4Used_Object = MibScalar
pm20020maDwlGwBank4Used = _Pm20020maDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 4),
    _Pm20020maDwlGwBank4Used_Type()
)
pm20020maDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank4Used.setStatus("current")
_Pm20020maDwlGwBank1Notempty_Type = EkiOnOff
_Pm20020maDwlGwBank1Notempty_Object = MibScalar
pm20020maDwlGwBank1Notempty = _Pm20020maDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 5),
    _Pm20020maDwlGwBank1Notempty_Type()
)
pm20020maDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank1Notempty.setStatus("current")
_Pm20020maDwlGwBank2Notempty_Type = EkiOnOff
_Pm20020maDwlGwBank2Notempty_Object = MibScalar
pm20020maDwlGwBank2Notempty = _Pm20020maDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 6),
    _Pm20020maDwlGwBank2Notempty_Type()
)
pm20020maDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank2Notempty.setStatus("current")
_Pm20020maDwlGwBank3Notempty_Type = EkiOnOff
_Pm20020maDwlGwBank3Notempty_Object = MibScalar
pm20020maDwlGwBank3Notempty = _Pm20020maDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 7),
    _Pm20020maDwlGwBank3Notempty_Type()
)
pm20020maDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank3Notempty.setStatus("current")
_Pm20020maDwlGwBank4Notempty_Type = EkiOnOff
_Pm20020maDwlGwBank4Notempty_Object = MibScalar
pm20020maDwlGwBank4Notempty = _Pm20020maDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 1, 2, 8),
    _Pm20020maDwlGwBank4Notempty_Type()
)
pm20020maDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maDwlGwBank4Notempty.setStatus("current")
_Pm20020maDwlClient_ObjectIdentity = ObjectIdentity
pm20020maDwlClient = _Pm20020maDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 2)
)
_Pm20020maDwlLine_ObjectIdentity = ObjectIdentity
pm20020maDwlLine = _Pm20020maDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 8, 3)
)
_Pm20020maConfig_ObjectIdentity = ObjectIdentity
pm20020maConfig = _Pm20020maConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9)
)
_Pm20020maCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm20020maCfgAccessCAisCsf = _Pm20020maCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 1)
)
_Pm20020maCfgClientcaiscsfTable_Object = MibTable
pm20020maCfgClientcaiscsfTable = _Pm20020maCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm20020maCfgClientcaiscsfTable.setStatus("current")
_Pm20020maCfgClientcaiscsfEntry_Object = MibTableRow
pm20020maCfgClientcaiscsfEntry = _Pm20020maCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 1, 1, 1)
)
pm20020maCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgClientcaiscsfEntry.setStatus("current")


class _Pm20020maCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm20020maCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm20020maCfgClientcaiscsfIndex_Object = MibTableColumn
pm20020maCfgClientcaiscsfIndex = _Pm20020maCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 1, 1, 1, 1),
    _Pm20020maCfgClientcaiscsfIndex_Type()
)
pm20020maCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgClientcaiscsfIndex.setStatus("current")


class _Pm20020maCfgReservePortn_Type(Unsigned32):
    """Custom type pm20020maCfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgReservePortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgReservePortn_Object = MibTableColumn
pm20020maCfgReservePortn = _Pm20020maCfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 1, 1, 1, 3),
    _Pm20020maCfgReservePortn_Type()
)
pm20020maCfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgReservePortn.setStatus("current")
_Pm20020maCfgStartup_ObjectIdentity = ObjectIdentity
pm20020maCfgStartup = _Pm20020maCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2)
)
_Pm20020maCfgClientStartupTable_Object = MibTable
pm20020maCfgClientStartupTable = _Pm20020maCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm20020maCfgClientStartupTable.setStatus("current")
_Pm20020maCfgClientStartupEntry_Object = MibTableRow
pm20020maCfgClientStartupEntry = _Pm20020maCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 1, 1)
)
pm20020maCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgClientStartupEntry.setStatus("current")


class _Pm20020maCfgClientStartupIndex_Type(Integer32):
    """Custom type pm20020maCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm20020maCfgClientStartupIndex_Object = MibTableColumn
pm20020maCfgClientStartupIndex = _Pm20020maCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 1, 1, 1),
    _Pm20020maCfgClientStartupIndex_Type()
)
pm20020maCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgClientStartupIndex.setStatus("current")


class _Pm20020maCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm20020maCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgSystConfPortPortn_Object = MibTableColumn
pm20020maCfgSystConfPortPortn = _Pm20020maCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 1, 1, 3),
    _Pm20020maCfgSystConfPortPortn_Type()
)
pm20020maCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgSystConfPortPortn.setStatus("current")


class _Pm20020maCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm20020maCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgNetConfPortPortn_Object = MibTableColumn
pm20020maCfgNetConfPortPortn = _Pm20020maCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 1, 1, 4),
    _Pm20020maCfgNetConfPortPortn_Type()
)
pm20020maCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgNetConfPortPortn.setStatus("current")


class _Pm20020maCfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm20020maCfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgOptionsPortPortn_Object = MibTableColumn
pm20020maCfgOptionsPortPortn = _Pm20020maCfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 1, 1, 14),
    _Pm20020maCfgOptionsPortPortn_Type()
)
pm20020maCfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgOptionsPortPortn.setStatus("current")
_Pm20020maCfgLineStartupTable_Object = MibTable
pm20020maCfgLineStartupTable = _Pm20020maCfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm20020maCfgLineStartupTable.setStatus("current")
_Pm20020maCfgLineStartupEntry_Object = MibTableRow
pm20020maCfgLineStartupEntry = _Pm20020maCfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 2, 1)
)
pm20020maCfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgLineStartupEntry.setStatus("current")


class _Pm20020maCfgLineStartupIndex_Type(Integer32):
    """Custom type pm20020maCfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm20020maCfgLineStartupIndex_Object = MibTableColumn
pm20020maCfgLineStartupIndex = _Pm20020maCfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 2, 1, 1),
    _Pm20020maCfgLineStartupIndex_Type()
)
pm20020maCfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgLineStartupIndex.setStatus("current")


class _Pm20020maCfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm20020maCfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgSystConfLinePortn_Object = MibTableColumn
pm20020maCfgSystConfLinePortn = _Pm20020maCfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 2, 1, 3),
    _Pm20020maCfgSystConfLinePortn_Type()
)
pm20020maCfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgSystConfLinePortn.setStatus("current")


class _Pm20020maCfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm20020maCfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgOptionsLinePortn_Object = MibTableColumn
pm20020maCfgOptionsLinePortn = _Pm20020maCfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 2, 1, 14),
    _Pm20020maCfgOptionsLinePortn_Type()
)
pm20020maCfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgOptionsLinePortn.setStatus("current")
_Pm20020maCfgXfpTable_Object = MibTable
pm20020maCfgXfpTable = _Pm20020maCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm20020maCfgXfpTable.setStatus("current")
_Pm20020maCfgXfpEntry_Object = MibTableRow
pm20020maCfgXfpEntry = _Pm20020maCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 3, 1)
)
pm20020maCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgXfpEntry.setStatus("current")


class _Pm20020maCfgXfpIndex_Type(Integer32):
    """Custom type pm20020maCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgXfpIndex_Type.__name__ = "Integer32"
_Pm20020maCfgXfpIndex_Object = MibTableColumn
pm20020maCfgXfpIndex = _Pm20020maCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 3, 1, 1),
    _Pm20020maCfgXfpIndex_Type()
)
pm20020maCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgXfpIndex.setStatus("current")


class _Pm20020maCfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm20020maCfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgSystConfMsaLinePortn_Object = MibTableColumn
pm20020maCfgSystConfMsaLinePortn = _Pm20020maCfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 2, 3, 1, 3),
    _Pm20020maCfgSystConfMsaLinePortn_Type()
)
pm20020maCfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgSystConfMsaLinePortn.setStatus("current")
_Pm20020maCfgLabels_ObjectIdentity = ObjectIdentity
pm20020maCfgLabels = _Pm20020maCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3)
)
_Pm20020maCfgLabelclientTable_Object = MibTable
pm20020maCfgLabelclientTable = _Pm20020maCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm20020maCfgLabelclientTable.setStatus("current")
_Pm20020maCfgLabelclientEntry_Object = MibTableRow
pm20020maCfgLabelclientEntry = _Pm20020maCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 1, 1)
)
pm20020maCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgLabelclientEntry.setStatus("current")


class _Pm20020maCfgLabelclientIndex_Type(Integer32):
    """Custom type pm20020maCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm20020maCfgLabelclientIndex_Object = MibTableColumn
pm20020maCfgLabelclientIndex = _Pm20020maCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 1, 1, 1),
    _Pm20020maCfgLabelclientIndex_Type()
)
pm20020maCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgLabelclientIndex.setStatus("current")


class _Pm20020maCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm20020maCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm20020maCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm20020maCfgLabelclientPortn_Object = MibTableColumn
pm20020maCfgLabelclientPortn = _Pm20020maCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 1, 1, 3),
    _Pm20020maCfgLabelclientPortn_Type()
)
pm20020maCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgLabelclientPortn.setStatus("current")
_Pm20020maCfgLabellineTable_Object = MibTable
pm20020maCfgLabellineTable = _Pm20020maCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm20020maCfgLabellineTable.setStatus("current")
_Pm20020maCfgLabellineEntry_Object = MibTableRow
pm20020maCfgLabellineEntry = _Pm20020maCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 2, 1)
)
pm20020maCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgLabellineEntry.setStatus("current")


class _Pm20020maCfgLabellineIndex_Type(Integer32):
    """Custom type pm20020maCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm20020maCfgLabellineIndex_Object = MibTableColumn
pm20020maCfgLabellineIndex = _Pm20020maCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 2, 1, 1),
    _Pm20020maCfgLabellineIndex_Type()
)
pm20020maCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgLabellineIndex.setStatus("current")


class _Pm20020maCfgLabellinePortn_Type(DisplayString):
    """Custom type pm20020maCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm20020maCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm20020maCfgLabellinePortn_Object = MibTableColumn
pm20020maCfgLabellinePortn = _Pm20020maCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 3, 2, 1, 3),
    _Pm20020maCfgLabellinePortn_Type()
)
pm20020maCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgLabellinePortn.setStatus("current")
_Pm20020maCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm20020maCfgStartuptlh = _Pm20020maCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4)
)
_Pm20020maCfgOtxtlhTable_Object = MibTable
pm20020maCfgOtxtlhTable = _Pm20020maCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm20020maCfgOtxtlhTable.setStatus("current")
_Pm20020maCfgOtxtlhEntry_Object = MibTableRow
pm20020maCfgOtxtlhEntry = _Pm20020maCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1)
)
pm20020maCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgOtxtlhEntry.setStatus("current")


class _Pm20020maCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm20020maCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm20020maCfgOtxtlhIndex_Object = MibTableColumn
pm20020maCfgOtxtlhIndex = _Pm20020maCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1, 1),
    _Pm20020maCfgOtxtlhIndex_Type()
)
pm20020maCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgOtxtlhIndex.setStatus("current")


class _Pm20020maCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm20020maCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgLinePwrLaserPortn_Object = MibTableColumn
pm20020maCfgLinePwrLaserPortn = _Pm20020maCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1, 6),
    _Pm20020maCfgLinePwrLaserPortn_Type()
)
pm20020maCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgLinePwrLaserPortn.setStatus("current")


class _Pm20020maCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm20020maCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgLineFCurrentPortn_Object = MibTableColumn
pm20020maCfgLineFCurrentPortn = _Pm20020maCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1, 7),
    _Pm20020maCfgLineFCurrentPortn_Type()
)
pm20020maCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgLineFCurrentPortn.setStatus("current")


class _Pm20020maCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm20020maCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgLineGridCurrentPortn_Object = MibTableColumn
pm20020maCfgLineGridCurrentPortn = _Pm20020maCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1, 8),
    _Pm20020maCfgLineGridCurrentPortn_Type()
)
pm20020maCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgLineGridCurrentPortn.setStatus("current")


class _Pm20020maCfgFPortn_Type(Unsigned32):
    """Custom type pm20020maCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgFPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgFPortn_Object = MibTableColumn
pm20020maCfgFPortn = _Pm20020maCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1, 9),
    _Pm20020maCfgFPortn_Type()
)
pm20020maCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgFPortn.setStatus("current")


class _Pm20020maCfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm20020maCfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgRxLineFCurrentPortn_Object = MibTableColumn
pm20020maCfgRxLineFCurrentPortn = _Pm20020maCfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 4, 1, 1, 10),
    _Pm20020maCfgRxLineFCurrentPortn_Type()
)
pm20020maCfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgRxLineFCurrentPortn.setStatus("current")
_Pm20020maCfgOther_ObjectIdentity = ObjectIdentity
pm20020maCfgOther = _Pm20020maCfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 5)
)
_Pm20020matablemoduleOther_ObjectIdentity = ObjectIdentity
pm20020matablemoduleOther = _Pm20020matablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 5, 1)
)


class _Pm20020maCfgmode_Type(Unsigned32):
    """Custom type pm20020maCfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgmode_Type.__name__ = "Unsigned32"
_Pm20020maCfgmode_Object = MibScalar
pm20020maCfgmode = _Pm20020maCfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 5, 1, 2),
    _Pm20020maCfgmode_Type()
)
pm20020maCfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgmode.setStatus("current")


class _Pm20020maCfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm20020maCfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm20020maCfgfanLowSpeedThreshold_Object = MibScalar
pm20020maCfgfanLowSpeedThreshold = _Pm20020maCfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 5, 1, 3),
    _Pm20020maCfgfanLowSpeedThreshold_Type()
)
pm20020maCfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgfanLowSpeedThreshold.setStatus("current")


class _Pm20020maCfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm20020maCfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm20020maCfgfanHighSpeedThreshold_Object = MibScalar
pm20020maCfgfanHighSpeedThreshold = _Pm20020maCfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 5, 1, 4),
    _Pm20020maCfgfanHighSpeedThreshold_Type()
)
pm20020maCfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgfanHighSpeedThreshold.setStatus("current")
_Pm20020maCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm20020maCfgStartuptablefive = _Pm20020maCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6)
)
_Pm20020maCfgOtxtlhcapabilitiesTable_Object = MibTable
pm20020maCfgOtxtlhcapabilitiesTable = _Pm20020maCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm20020maCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm20020maCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm20020maCfgOtxtlhcapabilitiesEntry = _Pm20020maCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1)
)
pm20020maCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm20020maCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm20020maCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm20020maCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm20020maCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm20020maCfgOtxtlhcapabilitiesIndex = _Pm20020maCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1, 1),
    _Pm20020maCfgOtxtlhcapabilitiesIndex_Type()
)
pm20020maCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm20020maCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm20020maCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgComponentTypePortn_Object = MibTableColumn
pm20020maCfgComponentTypePortn = _Pm20020maCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1, 3),
    _Pm20020maCfgComponentTypePortn_Type()
)
pm20020maCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgComponentTypePortn.setStatus("current")


class _Pm20020maCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm20020maCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgMiscellaneousPortn_Object = MibTableColumn
pm20020maCfgMiscellaneousPortn = _Pm20020maCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1, 4),
    _Pm20020maCfgMiscellaneousPortn_Type()
)
pm20020maCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgMiscellaneousPortn.setStatus("current")


class _Pm20020maCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm20020maCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgFirstChannelPortn_Object = MibTableColumn
pm20020maCfgFirstChannelPortn = _Pm20020maCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1, 5),
    _Pm20020maCfgFirstChannelPortn_Type()
)
pm20020maCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgFirstChannelPortn.setStatus("current")


class _Pm20020maCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm20020maCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgLastChannelPortn_Object = MibTableColumn
pm20020maCfgLastChannelPortn = _Pm20020maCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1, 6),
    _Pm20020maCfgLastChannelPortn_Type()
)
pm20020maCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgLastChannelPortn.setStatus("current")


class _Pm20020maCfgGridPortn_Type(Unsigned32):
    """Custom type pm20020maCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm20020maCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm20020maCfgGridPortn_Object = MibTableColumn
pm20020maCfgGridPortn = _Pm20020maCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 6, 1, 1, 7),
    _Pm20020maCfgGridPortn_Type()
)
pm20020maCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maCfgGridPortn.setStatus("current")
_Pm20020maCfgWriteConfiguration_Type = EkiOnOff
_Pm20020maCfgWriteConfiguration_Object = MibScalar
pm20020maCfgWriteConfiguration = _Pm20020maCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 9, 257),
    _Pm20020maCfgWriteConfiguration_Type()
)
pm20020maCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maCfgWriteConfiguration.setStatus("current")
_Pm20020matraps_ObjectIdentity = ObjectIdentity
pm20020matraps = _Pm20020matraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10)
)


class _Pm20020matrapPortNumber_Type(Integer32):
    """Custom type pm20020matrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm20020matrapPortNumber_Type.__name__ = "Integer32"
_Pm20020matrapPortNumber_Object = MibScalar
pm20020matrapPortNumber = _Pm20020matrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 2),
    _Pm20020matrapPortNumber_Type()
)
pm20020matrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020matrapPortNumber.setStatus("current")


class _Pm20020matrapLineNumber_Type(Integer32):
    """Custom type pm20020matrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm20020matrapLineNumber_Type.__name__ = "Integer32"
_Pm20020matrapLineNumber_Object = MibScalar
pm20020matrapLineNumber = _Pm20020matrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 3),
    _Pm20020matrapLineNumber_Type()
)
pm20020matrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020matrapLineNumber.setStatus("current")


class _Pm20020matrapBoardNumber_Type(Integer32):
    """Custom type pm20020matrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm20020matrapBoardNumber_Type.__name__ = "Integer32"
_Pm20020matrapBoardNumber_Object = MibScalar
pm20020matrapBoardNumber = _Pm20020matrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 4),
    _Pm20020matrapBoardNumber_Type()
)
pm20020matrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020matrapBoardNumber.setStatus("current")
_Pm20020maMonitoring_ObjectIdentity = ObjectIdentity
pm20020maMonitoring = _Pm20020maMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11)
)
_Pm20020maMonOther_ObjectIdentity = ObjectIdentity
pm20020maMonOther = _Pm20020maMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 1)
)
_Pm20020maMonRmon_ObjectIdentity = ObjectIdentity
pm20020maMonRmon = _Pm20020maMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 1, 3)
)
_Pm20020maMonClient_ObjectIdentity = ObjectIdentity
pm20020maMonClient = _Pm20020maMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2)
)
_Pm20020maMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm20020maMonClientRmonCounter = _Pm20020maMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4)
)
_Pm20020maMonupRmonBytesCounterClientInputTable_Object = MibTable
pm20020maMonupRmonBytesCounterClientInputTable = _Pm20020maMonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonBytesCounterClientInputEntry = _Pm20020maMonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 16, 1)
)
pm20020maMonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonBytesCounterClientInputIndex = _Pm20020maMonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 16, 1, 1),
    _Pm20020maMonupRmonBytesCounterClientInputIndex_Type()
)
pm20020maMonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonBytesCounterClientInputValuePortn = _Pm20020maMonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 16, 1, 2),
    _Pm20020maMonupRmonBytesCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonBytesCounterClientInputErrorPortn = _Pm20020maMonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 16, 1, 3),
    _Pm20020maMonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonBytesCounterClientInputOverloadPortn = _Pm20020maMonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 16, 1, 4),
    _Pm20020maMonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm20020maMonupRmonCrcErrorsCounterClientInputTable = _Pm20020maMonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonCrcErrorsCounterClientInputEntry = _Pm20020maMonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 48, 1)
)
pm20020maMonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonCrcErrorsCounterClientInputIndex = _Pm20020maMonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 48, 1, 1),
    _Pm20020maMonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm20020maMonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn = _Pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 48, 1, 2),
    _Pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 48, 1, 3),
    _Pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 48, 1, 4),
    _Pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonPacketsCounterClientInputTable_Object = MibTable
pm20020maMonupRmonPacketsCounterClientInputTable = _Pm20020maMonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonPacketsCounterClientInputEntry = _Pm20020maMonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 80, 1)
)
pm20020maMonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonPacketsCounterClientInputIndex = _Pm20020maMonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 80, 1, 1),
    _Pm20020maMonupRmonPacketsCounterClientInputIndex_Type()
)
pm20020maMonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonPacketsCounterClientInputValuePortn = _Pm20020maMonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 80, 1, 2),
    _Pm20020maMonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonPacketsCounterClientInputErrorPortn = _Pm20020maMonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 80, 1, 3),
    _Pm20020maMonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonPacketsCounterClientInputOverloadPortn = _Pm20020maMonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 80, 1, 4),
    _Pm20020maMonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm20020maMonupRmonBroadcastCounterClientInputTable = _Pm20020maMonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 112)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonBroadcastCounterClientInputEntry = _Pm20020maMonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 112, 1)
)
pm20020maMonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonBroadcastCounterClientInputIndex = _Pm20020maMonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 112, 1, 1),
    _Pm20020maMonupRmonBroadcastCounterClientInputIndex_Type()
)
pm20020maMonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonBroadcastCounterClientInputValuePortn = _Pm20020maMonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 112, 1, 2),
    _Pm20020maMonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonBroadcastCounterClientInputErrorPortn = _Pm20020maMonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 112, 1, 3),
    _Pm20020maMonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn = _Pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 112, 1, 4),
    _Pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonMulticastCounterClientInputTable_Object = MibTable
pm20020maMonupRmonMulticastCounterClientInputTable = _Pm20020maMonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 144)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonMulticastCounterClientInputEntry = _Pm20020maMonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 144, 1)
)
pm20020maMonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonMulticastCounterClientInputIndex = _Pm20020maMonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 144, 1, 1),
    _Pm20020maMonupRmonMulticastCounterClientInputIndex_Type()
)
pm20020maMonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonMulticastCounterClientInputValuePortn = _Pm20020maMonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 144, 1, 2),
    _Pm20020maMonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonMulticastCounterClientInputErrorPortn = _Pm20020maMonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 144, 1, 3),
    _Pm20020maMonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonMulticastCounterClientInputOverloadPortn = _Pm20020maMonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 144, 1, 4),
    _Pm20020maMonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm20020maMonupRmonPauseFrameCounterClientInputTable = _Pm20020maMonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonPauseFrameCounterClientInputEntry = _Pm20020maMonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 176, 1)
)
pm20020maMonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonPauseFrameCounterClientInputIndex = _Pm20020maMonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 176, 1, 1),
    _Pm20020maMonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm20020maMonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonPauseFrameCounterClientInputValuePortn = _Pm20020maMonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 176, 1, 2),
    _Pm20020maMonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn = _Pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 176, 1, 3),
    _Pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 176, 1, 4),
    _Pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonUnicastCounterClientInputTable_Object = MibTable
pm20020maMonupRmonUnicastCounterClientInputTable = _Pm20020maMonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 304)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonUnicastCounterClientInputEntry = _Pm20020maMonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 304, 1)
)
pm20020maMonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonUnicastCounterClientInputIndex = _Pm20020maMonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 304, 1, 1),
    _Pm20020maMonupRmonUnicastCounterClientInputIndex_Type()
)
pm20020maMonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonUnicastCounterClientInputValuePortn = _Pm20020maMonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 304, 1, 2),
    _Pm20020maMonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonUnicastCounterClientInputErrorPortn = _Pm20020maMonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 304, 1, 3),
    _Pm20020maMonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonUnicastCounterClientInputOverloadPortn = _Pm20020maMonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 304, 1, 4),
    _Pm20020maMonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm20020maMonupRmonNonunicastCounterClientInputTable = _Pm20020maMonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 336)
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm20020maMonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm20020maMonupRmonNonunicastCounterClientInputEntry = _Pm20020maMonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 336, 1)
)
pm20020maMonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm20020maMonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm20020maMonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm20020maMonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm20020maMonupRmonNonunicastCounterClientInputIndex = _Pm20020maMonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 336, 1, 1),
    _Pm20020maMonupRmonNonunicastCounterClientInputIndex_Type()
)
pm20020maMonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm20020maMonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm20020maMonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm20020maMonupRmonNonunicastCounterClientInputValuePortn = _Pm20020maMonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 336, 1, 2),
    _Pm20020maMonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm20020maMonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm20020maMonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm20020maMonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm20020maMonupRmonNonunicastCounterClientInputErrorPortn = _Pm20020maMonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 336, 1, 3),
    _Pm20020maMonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm20020maMonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn = _Pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 336, 1, 4),
    _Pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonBytesCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonBytesCounterClientOutputTable = _Pm20020maMondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 400)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonBytesCounterClientOutputEntry = _Pm20020maMondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 400, 1)
)
pm20020maMondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonBytesCounterClientOutputIndex = _Pm20020maMondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 400, 1, 1),
    _Pm20020maMondownRmonBytesCounterClientOutputIndex_Type()
)
pm20020maMondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonBytesCounterClientOutputValuePortn = _Pm20020maMondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 400, 1, 2),
    _Pm20020maMondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonBytesCounterClientOutputErrorPortn = _Pm20020maMondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 400, 1, 3),
    _Pm20020maMondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonBytesCounterClientOutputOverloadPortn = _Pm20020maMondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 400, 1, 4),
    _Pm20020maMondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonCrcErrorsCounterClientOutputTable = _Pm20020maMondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 432)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonCrcErrorsCounterClientOutputEntry = _Pm20020maMondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 432, 1)
)
pm20020maMondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonCrcErrorsCounterClientOutputIndex = _Pm20020maMondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 432, 1, 1),
    _Pm20020maMondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm20020maMondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 432, 1, 2),
    _Pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 432, 1, 3),
    _Pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 432, 1, 4),
    _Pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonPacketsCounterClientOutputTable = _Pm20020maMondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 464)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonPacketsCounterClientOutputEntry = _Pm20020maMondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 464, 1)
)
pm20020maMondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonPacketsCounterClientOutputIndex = _Pm20020maMondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 464, 1, 1),
    _Pm20020maMondownRmonPacketsCounterClientOutputIndex_Type()
)
pm20020maMondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonPacketsCounterClientOutputValuePortn = _Pm20020maMondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 464, 1, 2),
    _Pm20020maMondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonPacketsCounterClientOutputErrorPortn = _Pm20020maMondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 464, 1, 3),
    _Pm20020maMondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn = _Pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 464, 1, 4),
    _Pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonBroadcastCounterClientOutputTable = _Pm20020maMondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 496)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonBroadcastCounterClientOutputEntry = _Pm20020maMondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 496, 1)
)
pm20020maMondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonBroadcastCounterClientOutputIndex = _Pm20020maMondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 496, 1, 1),
    _Pm20020maMondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm20020maMondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonBroadcastCounterClientOutputValuePortn = _Pm20020maMondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 496, 1, 2),
    _Pm20020maMondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn = _Pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 496, 1, 3),
    _Pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 496, 1, 4),
    _Pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonMulticastCounterClientOutputTable = _Pm20020maMondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 528)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonMulticastCounterClientOutputEntry = _Pm20020maMondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 528, 1)
)
pm20020maMondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonMulticastCounterClientOutputIndex = _Pm20020maMondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 528, 1, 1),
    _Pm20020maMondownRmonMulticastCounterClientOutputIndex_Type()
)
pm20020maMondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonMulticastCounterClientOutputValuePortn = _Pm20020maMondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 528, 1, 2),
    _Pm20020maMondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonMulticastCounterClientOutputErrorPortn = _Pm20020maMondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 528, 1, 3),
    _Pm20020maMondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn = _Pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 528, 1, 4),
    _Pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonPauseFrameCounterClientOutputTable = _Pm20020maMondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 560)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonPauseFrameCounterClientOutputEntry = _Pm20020maMondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 560, 1)
)
pm20020maMondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonPauseFrameCounterClientOutputIndex = _Pm20020maMondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 560, 1, 1),
    _Pm20020maMondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm20020maMondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn = _Pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 560, 1, 2),
    _Pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 560, 1, 3),
    _Pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 560, 1, 4),
    _Pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonUnicastCounterClientOutputTable = _Pm20020maMondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 688)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonUnicastCounterClientOutputEntry = _Pm20020maMondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 688, 1)
)
pm20020maMondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonUnicastCounterClientOutputIndex = _Pm20020maMondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 688, 1, 1),
    _Pm20020maMondownRmonUnicastCounterClientOutputIndex_Type()
)
pm20020maMondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonUnicastCounterClientOutputValuePortn = _Pm20020maMondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 688, 1, 2),
    _Pm20020maMondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonUnicastCounterClientOutputErrorPortn = _Pm20020maMondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 688, 1, 3),
    _Pm20020maMondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn = _Pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 688, 1, 4),
    _Pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm20020maMondownRmonNonunicastCounterClientOutputTable = _Pm20020maMondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 720)
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm20020maMondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm20020maMondownRmonNonunicastCounterClientOutputEntry = _Pm20020maMondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 720, 1)
)
pm20020maMondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maMondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm20020maMondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm20020maMondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm20020maMondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maMondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm20020maMondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm20020maMondownRmonNonunicastCounterClientOutputIndex = _Pm20020maMondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 720, 1, 1),
    _Pm20020maMondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm20020maMondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm20020maMondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm20020maMondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm20020maMondownRmonNonunicastCounterClientOutputValuePortn = _Pm20020maMondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 720, 1, 2),
    _Pm20020maMondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm20020maMondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn = _Pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 720, 1, 3),
    _Pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 2, 4, 720, 1, 4),
    _Pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm20020maMonPerfOther_ObjectIdentity = ObjectIdentity
pm20020maMonPerfOther = _Pm20020maMonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5)
)
_Pm20020maMonPerfSync_ObjectIdentity = ObjectIdentity
pm20020maMonPerfSync = _Pm20020maMonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 1)
)
_Pm20020maPerfEnable_Type = EkiOnOff
_Pm20020maPerfEnable_Object = MibScalar
pm20020maPerfEnable = _Pm20020maPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 1, 257),
    _Pm20020maPerfEnable_Type()
)
pm20020maPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerfEnable.setStatus("current")
_Pm20020maPerf15minSync_Type = EkiOnOff
_Pm20020maPerf15minSync_Object = MibScalar
pm20020maPerf15minSync = _Pm20020maPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 1, 259),
    _Pm20020maPerf15minSync_Type()
)
pm20020maPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerf15minSync.setStatus("current")
_Pm20020maPerf24hSync_Type = EkiOnOff
_Pm20020maPerf24hSync_Object = MibScalar
pm20020maPerf24hSync = _Pm20020maPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 1, 260),
    _Pm20020maPerf24hSync_Type()
)
pm20020maPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerf24hSync.setStatus("current")
_Pm20020maMonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm20020maMonPerfTimeStamp = _Pm20020maMonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2)
)
_Pm20020maPerf15MinShort_Type = EkiOnOff
_Pm20020maPerf15MinShort_Object = MibScalar
pm20020maPerf15MinShort = _Pm20020maPerf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2, 1),
    _Pm20020maPerf15MinShort_Type()
)
pm20020maPerf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerf15MinShort.setStatus("current")
_Pm20020maPerf15MinLong_Type = EkiOnOff
_Pm20020maPerf15MinLong_Object = MibScalar
pm20020maPerf15MinLong = _Pm20020maPerf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2, 2),
    _Pm20020maPerf15MinLong_Type()
)
pm20020maPerf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerf15MinLong.setStatus("current")
_Pm20020maPerf24HoursShort_Type = Counter32
_Pm20020maPerf24HoursShort_Object = MibScalar
pm20020maPerf24HoursShort = _Pm20020maPerf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2, 5),
    _Pm20020maPerf24HoursShort_Type()
)
pm20020maPerf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerf24HoursShort.setStatus("current")
_Pm20020maPerf24HoursLong_Type = Counter32
_Pm20020maPerf24HoursLong_Object = MibScalar
pm20020maPerf24HoursLong = _Pm20020maPerf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2, 6),
    _Pm20020maPerf24HoursLong_Type()
)
pm20020maPerf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerf24HoursLong.setStatus("current")
_Pm20020maPerfCurrent15MinElapsedTime_Type = Counter32
_Pm20020maPerfCurrent15MinElapsedTime_Object = MibScalar
pm20020maPerfCurrent15MinElapsedTime = _Pm20020maPerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2, 7),
    _Pm20020maPerfCurrent15MinElapsedTime_Type()
)
pm20020maPerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerfCurrent15MinElapsedTime.setStatus("current")
_Pm20020maPerfCurrent24HoursElapsedTime_Type = Counter32
_Pm20020maPerfCurrent24HoursElapsedTime_Object = MibScalar
pm20020maPerfCurrent24HoursElapsedTime = _Pm20020maPerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 5, 2, 8),
    _Pm20020maPerfCurrent24HoursElapsedTime_Type()
)
pm20020maPerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm20020maPerfCurrent24HoursElapsedTime.setStatus("current")
_Pm20020maMonPerfClient_ObjectIdentity = ObjectIdentity
pm20020maMonPerfClient = _Pm20020maMonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6)
)
_Pm20020maPerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm20020maPerfTelecomInputClientCurrent15StatTable = _Pm20020maPerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm20020maPerfTelecomInputClientCurrent15StatEntry = _Pm20020maPerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1)
)
pm20020maPerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm20020maPerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatIndex = _Pm20020maPerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 1),
    _Pm20020maPerfTelecomInputClientCurrent15StatIndex_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn = _Pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 2),
    _Pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn = _Pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 3),
    _Pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn = _Pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 4),
    _Pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn = _Pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 5),
    _Pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn = _Pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 6),
    _Pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn = _Pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 7),
    _Pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 8),
    _Pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 9),
    _Pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn = _Pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 10),
    _Pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn = _Pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 16, 1, 11),
    _Pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomInputClientPast15StatHistoryPort1Table = _Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1)
)
pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index = _Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 1),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 2),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 3),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 4),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 5),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 6),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 7),
    _Pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 8),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 9),
    _Pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 10),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 48, 1, 11),
    _Pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm20020maPerfTelecomInputClientCurrent24StatTable = _Pm20020maPerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm20020maPerfTelecomInputClientCurrent24StatEntry = _Pm20020maPerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1)
)
pm20020maPerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm20020maPerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatIndex = _Pm20020maPerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 1),
    _Pm20020maPerfTelecomInputClientCurrent24StatIndex_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn = _Pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 2),
    _Pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn = _Pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 3),
    _Pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn = _Pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 4),
    _Pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn = _Pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 5),
    _Pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn = _Pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 6),
    _Pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn = _Pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 7),
    _Pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 8),
    _Pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 9),
    _Pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn = _Pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 10),
    _Pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn = _Pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 80, 1, 11),
    _Pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomInputClientPast24StatHistoryPort1Table = _Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1)
)
pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index = _Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 1),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 2),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 3),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 4),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 5),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 6),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 7),
    _Pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 8),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 9),
    _Pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 10),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 112, 1, 11),
    _Pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm20020maPerfTelecomOutputClientCurrent15StatTable = _Pm20020maPerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm20020maPerfTelecomOutputClientCurrent15StatEntry = _Pm20020maPerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1)
)
pm20020maPerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm20020maPerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatIndex = _Pm20020maPerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 1),
    _Pm20020maPerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 2),
    _Pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 3),
    _Pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 4),
    _Pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 5),
    _Pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 6),
    _Pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 7),
    _Pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 8),
    _Pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 9),
    _Pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 10),
    _Pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 144, 1, 11),
    _Pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1)
)
pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 1),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 2),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 3),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 4),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 5),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 6),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 7),
    _Pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 8),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 9),
    _Pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 10),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 176, 1, 11),
    _Pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm20020maPerfTelecomOutputClientCurrent24StatTable = _Pm20020maPerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm20020maPerfTelecomOutputClientCurrent24StatEntry = _Pm20020maPerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1)
)
pm20020maPerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm20020maPerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatIndex = _Pm20020maPerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 1),
    _Pm20020maPerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 2),
    _Pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 3),
    _Pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 4),
    _Pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 5),
    _Pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 6),
    _Pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 7),
    _Pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 8),
    _Pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 9),
    _Pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 10),
    _Pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 208, 1, 11),
    _Pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1)
)
pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 1),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 2),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 3),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 4),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 5),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 6),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 7),
    _Pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 8),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 9),
    _Pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 10),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 240, 1, 11),
    _Pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm20020maPerfDatacomClientCurrent15StatTable_Object = MibTable
pm20020maPerfDatacomClientCurrent15StatTable = _Pm20020maPerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848)
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm20020maPerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm20020maPerfDatacomClientCurrent15StatEntry = _Pm20020maPerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1)
)
pm20020maPerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm20020maPerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm20020maPerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm20020maPerfDatacomClientCurrent15StatIndex = _Pm20020maPerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 1),
    _Pm20020maPerfDatacomClientCurrent15StatIndex_Type()
)
pm20020maPerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn = _Pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 4),
    _Pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatInCrcCountPortn = _Pm20020maperfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 5),
    _Pm20020maperfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn = _Pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 6),
    _Pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatInPacketCountPortn = _Pm20020maperfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 7),
    _Pm20020maperfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn = _Pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 28),
    _Pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn = _Pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 29),
    _Pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn = _Pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 30),
    _Pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn = _Pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 848, 1, 31),
    _Pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm20020maPerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm20020maPerfDatacomClientPast15StatHistoryPort1Table = _Pm20020maPerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880)
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfDatacomClientPast15StatHistoryPort1Entry = _Pm20020maPerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1)
)
pm20020maPerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfDatacomClientPast15StatHistoryPort1Index = _Pm20020maPerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 1),
    _Pm20020maPerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm20020maPerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm20020maperfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatInCrcCountInvPort1 = _Pm20020maperfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 4),
    _Pm20020maperfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pm20020maperfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatInCrcCountPort1 = _Pm20020maperfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 5),
    _Pm20020maperfdatacomclientPast15StatInCrcCountPort1_Type()
)
pm20020maperfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatInPacketCountInvPort1 = _Pm20020maperfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 6),
    _Pm20020maperfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
pm20020maperfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatInPacketCountPort1 = _Pm20020maperfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 7),
    _Pm20020maperfdatacomclientPast15StatInPacketCountPort1_Type()
)
pm20020maperfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1 = _Pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 28),
    _Pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatOutCrcCountPort1 = _Pm20020maperfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 29),
    _Pm20020maperfdatacomclientPast15StatOutCrcCountPort1_Type()
)
pm20020maperfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1 = _Pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 30),
    _Pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast15StatOutPacketCountPort1 = _Pm20020maperfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 880, 1, 31),
    _Pm20020maperfdatacomclientPast15StatOutPacketCountPort1_Type()
)
pm20020maperfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm20020maPerfDatacomClientCurrent24StatTable_Object = MibTable
pm20020maPerfDatacomClientCurrent24StatTable = _Pm20020maPerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912)
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm20020maPerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm20020maPerfDatacomClientCurrent24StatEntry = _Pm20020maPerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1)
)
pm20020maPerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm20020maPerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm20020maPerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm20020maPerfDatacomClientCurrent24StatIndex = _Pm20020maPerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 1),
    _Pm20020maPerfDatacomClientCurrent24StatIndex_Type()
)
pm20020maPerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn = _Pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 4),
    _Pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatInCrcCountPortn = _Pm20020maperfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 5),
    _Pm20020maperfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn = _Pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 6),
    _Pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatInPacketCountPortn = _Pm20020maperfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 7),
    _Pm20020maperfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn = _Pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 28),
    _Pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn = _Pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 29),
    _Pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn = _Pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 30),
    _Pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn = _Pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 912, 1, 31),
    _Pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm20020maPerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm20020maPerfDatacomClientPast24StatHistoryPort1Table = _Pm20020maPerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944)
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfDatacomClientPast24StatHistoryPort1Entry = _Pm20020maPerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1)
)
pm20020maPerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfDatacomClientPast24StatHistoryPort1Index = _Pm20020maPerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 1),
    _Pm20020maPerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm20020maPerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm20020maperfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatInCrcCountInvPort1 = _Pm20020maperfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 4),
    _Pm20020maperfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pm20020maperfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatInCrcCountPort1 = _Pm20020maperfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 5),
    _Pm20020maperfdatacomclientPast24StatInCrcCountPort1_Type()
)
pm20020maperfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatInPacketCountInvPort1 = _Pm20020maperfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 6),
    _Pm20020maperfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
pm20020maperfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatInPacketCountPort1 = _Pm20020maperfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 7),
    _Pm20020maperfdatacomclientPast24StatInPacketCountPort1_Type()
)
pm20020maperfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1 = _Pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 28),
    _Pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatOutCrcCountPort1 = _Pm20020maperfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 29),
    _Pm20020maperfdatacomclientPast24StatOutCrcCountPort1_Type()
)
pm20020maperfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1 = _Pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 30),
    _Pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Pm20020maperfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Pm20020maperfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
pm20020maperfdatacomclientPast24StatOutPacketCountPort1 = _Pm20020maperfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 6, 944, 1, 31),
    _Pm20020maperfdatacomclientPast24StatOutPacketCountPort1_Type()
)
pm20020maperfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maperfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm20020maMonPerfLine_ObjectIdentity = ObjectIdentity
pm20020maMonPerfLine = _Pm20020maMonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7)
)
_Pm20020maPerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm20020maPerfTelecomLinePostFecCurrent15StatTable = _Pm20020maPerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm20020maPerfTelecomLinePostFecCurrent15StatEntry = _Pm20020maPerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1)
)
pm20020maPerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm20020maPerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatIndex = _Pm20020maPerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 1),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 2),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 3),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 4),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 5),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 6),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 7),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 8),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 9),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 10),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 336, 1, 11),
    _Pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1)
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 1),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 2),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 3),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 4),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 5),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 6),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 7),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 8),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 9),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 10),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 337, 1, 11),
    _Pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm20020maPerfTelecomLinePostFecCurrent24StatTable = _Pm20020maPerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm20020maPerfTelecomLinePostFecCurrent24StatEntry = _Pm20020maPerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1)
)
pm20020maPerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm20020maPerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatIndex = _Pm20020maPerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 1),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 2),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 3),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 4),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 5),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 6),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 7),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 8),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 9),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 10),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 338, 1, 11),
    _Pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1)
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 1),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 2),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 3),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 4),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 5),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 6),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 7),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 8),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 9),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 10),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 339, 1, 11),
    _Pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm20020maPerfTelecomBerLinePreFecCurrent15StatTable = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1)
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 1),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 2),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 3),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 4),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 5),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 6),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 352, 1, 7),
    _Pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1)
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 1),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 2),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 3),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 4),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 5),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 6),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 353, 1, 7),
    _Pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm20020maPerfTelecomBerLinePreFecCurrent24StatTable = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1)
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 1),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 2),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 3),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 4),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 5),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 6),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 354, 1, 7),
    _Pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355)
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1)
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm20020ma-MIB", "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 1),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 2),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 3),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 4),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 5),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 6),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 69, 11, 7, 355, 1, 7),
    _Pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm20020maLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 30)
)
pm20020maLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapLineNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm20020maLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 31)
)
pm20020maLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapLineNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm20020maLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 32)
)
pm20020maLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapLineNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm20020maLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 33)
)
pm20020maLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapLineNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm20020maLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 34)
)
pm20020maLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineFailPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineHwFailPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapLineNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maLineTrapCritGoesOn.setStatus(
        "current"
    )

pm20020maLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 35)
)
pm20020maLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineFailPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020maAlmLineHwFailPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapLineNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maLineTrapCritGoesOff.setStatus(
        "current"
    )

pm20020maClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 40)
)
pm20020maClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapPortNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm20020maClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 41)
)
pm20020maClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapPortNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm20020maClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 42)
)
pm20020maClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapPortNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm20020maClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 43)
)
pm20020maClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapPortNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm20020maClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 44)
)
pm20020maClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmFailAccPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020maAlmHwFailAccPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapPortNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maClientTrapCritGoesOn.setStatus(
        "current"
    )

pm20020maClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 45)
)
pm20020maClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmFailAccPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020maAlmHwFailAccPortn"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapPortNumber"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maClientTrapCritGoesOff.setStatus(
        "current"
    )

pm20020maPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 50)
)
pm20020maPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmDefFuseB"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020maAlmDefFuseA"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm20020maPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 69, 10, 51)
)
pm20020maPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm20020ma-MIB", "pm20020maAlmDefFuseB"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020maAlmDefFuseA"),
        ("EKINOPS-Pm20020ma-MIB", "pm20020matrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm20020maPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm20020ma-MIB",
    **{"Pm20020maMultiRate": Pm20020maMultiRate,
       "Pm20020maOtxMode": Pm20020maOtxMode,
       "Pm20020maOtxGrid": Pm20020maOtxGrid,
       "Pm20020maAdjustValue": Pm20020maAdjustValue,
       "Pm20020maClientProtocol": Pm20020maClientProtocol,
       "Pm20020maProtocolMode": Pm20020maProtocolMode,
       "Pm20020maOtxChannel": Pm20020maOtxChannel,
       "Pm20020maOrxChannel": Pm20020maOrxChannel,
       "Pm20020maDccMode": Pm20020maDccMode,
       "Pm20020maModuleMode": Pm20020maModuleMode,
       "modulePm20020ma": modulePm20020ma,
       "pm20020maalarms": pm20020maalarms,
       "pm20020maAlmOther": pm20020maAlmOther,
       "pm20020maAlmOtherNurg": pm20020maAlmOtherNurg,
       "pm20020maAlmsynthAlm2": pm20020maAlmsynthAlm2,
       "pm20020maAlmConfTableSave": pm20020maAlmConfTableSave,
       "pm20020maAlmInvUpload": pm20020maAlmInvUpload,
       "pm20020maAlmConfTableLoad": pm20020maAlmConfTableLoad,
       "pm20020maAlmCorrelatOff": pm20020maAlmCorrelatOff,
       "pm20020maAlmMaintenanceOn": pm20020maAlmMaintenanceOn,
       "pm20020maAlmOtherUrg": pm20020maAlmOtherUrg,
       "pm20020maAlmmodFanFail": pm20020maAlmmodFanFail,
       "pm20020maAlmFanFail": pm20020maAlmFanFail,
       "pm20020maAlmFanHighSpeed": pm20020maAlmFanHighSpeed,
       "pm20020maAlmOtherCrit": pm20020maAlmOtherCrit,
       "pm20020maAlmsynthAlm0": pm20020maAlmsynthAlm0,
       "pm20020maAlmFailFan": pm20020maAlmFailFan,
       "pm20020maAlmModGlobFail": pm20020maAlmModGlobFail,
       "pm20020maAlmDefFuseA": pm20020maAlmDefFuseA,
       "pm20020maAlmDefFuseB": pm20020maAlmDefFuseB,
       "pm20020maAlmclientModuleState": pm20020maAlmclientModuleState,
       "pm20020maAlmCfpInitialize": pm20020maAlmCfpInitialize,
       "pm20020maAlmCfpLowPower": pm20020maAlmCfpLowPower,
       "pm20020maAlmCfpHighPowerUp": pm20020maAlmCfpHighPowerUp,
       "pm20020maAlmCfpTxOff": pm20020maAlmCfpTxOff,
       "pm20020maAlmCfpTxTurnOn": pm20020maAlmCfpTxTurnOn,
       "pm20020maAlmCfpReady": pm20020maAlmCfpReady,
       "pm20020maAlmCfpFault": pm20020maAlmCfpFault,
       "pm20020maAlmCfpTxTurnOff": pm20020maAlmCfpTxTurnOff,
       "pm20020maAlmCfpHighPowerDown": pm20020maAlmCfpHighPowerDown,
       "pm20020maAlmclientModuleGeneralStatus": pm20020maAlmclientModuleGeneralStatus,
       "pm20020maAlmCfpOutOfAlignment": pm20020maAlmCfpOutOfAlignment,
       "pm20020maAlmCfpRxNetworkLol": pm20020maAlmCfpRxNetworkLol,
       "pm20020maAlmCfpRxLos": pm20020maAlmCfpRxLos,
       "pm20020maAlmCfpTxHostLol": pm20020maAlmCfpTxHostLol,
       "pm20020maAlmCfpTxLosf": pm20020maAlmCfpTxLosf,
       "pm20020maAlmCfpTxCmuLol": pm20020maAlmCfpTxCmuLol,
       "pm20020maAlmCfpTxJitterPllLol": pm20020maAlmCfpTxJitterPllLol,
       "pm20020maAlmCfpLossOfRefclk": pm20020maAlmCfpLossOfRefclk,
       "pm20020maAlmCfpHwInterlock": pm20020maAlmCfpHwInterlock,
       "pm20020maAlmclientGlobalAlarmSummary": pm20020maAlmclientGlobalAlarmSummary,
       "pm20020maAlmCfpSoftGlobAlarmTest": pm20020maAlmCfpSoftGlobAlarmTest,
       "pm20020maAlmCfpNetworkLaneAlarmWarning2": pm20020maAlmCfpNetworkLaneAlarmWarning2,
       "pm20020maAlmCfpModuleState": pm20020maAlmCfpModuleState,
       "pm20020maAlmCfpModuleGeneralStatus": pm20020maAlmCfpModuleGeneralStatus,
       "pm20020maAlmCfpModuleFault": pm20020maAlmCfpModuleFault,
       "pm20020maAlmCfpModuleAlarmWarning1": pm20020maAlmCfpModuleAlarmWarning1,
       "pm20020maAlmCfpModuleAlarmWarning2": pm20020maAlmCfpModuleAlarmWarning2,
       "pm20020maAlmCfpNetworkLaneAlarmWarning1": pm20020maAlmCfpNetworkLaneAlarmWarning1,
       "pm20020maAlmCfpNetworkLaneFaultStatus": pm20020maAlmCfpNetworkLaneFaultStatus,
       "pm20020maAlmCfpHostLaneFaultStatus": pm20020maAlmCfpHostLaneFaultStatus,
       "pm20020maAlmCfpGlobAlarmAssertion": pm20020maAlmCfpGlobAlarmAssertion,
       "pm20020maAlmmsaModuleState": pm20020maAlmmsaModuleState,
       "pm20020maAlmMsaInitialize": pm20020maAlmMsaInitialize,
       "pm20020maAlmMsaLowPower": pm20020maAlmMsaLowPower,
       "pm20020maAlmMsaHighPowerUp": pm20020maAlmMsaHighPowerUp,
       "pm20020maAlmMsaTxOff": pm20020maAlmMsaTxOff,
       "pm20020maAlmMsaTxTurnOn": pm20020maAlmMsaTxTurnOn,
       "pm20020maAlmMsaReady": pm20020maAlmMsaReady,
       "pm20020maAlmMsaFault": pm20020maAlmMsaFault,
       "pm20020maAlmMsaTxTurnOff": pm20020maAlmMsaTxTurnOff,
       "pm20020maAlmMsaHighPowerDown": pm20020maAlmMsaHighPowerDown,
       "pm20020maAlmmsaModuleGeneralStatus": pm20020maAlmmsaModuleGeneralStatus,
       "pm20020maAlmMsaOutOfAlignment": pm20020maAlmMsaOutOfAlignment,
       "pm20020maAlmMsaRxNetworkLol": pm20020maAlmMsaRxNetworkLol,
       "pm20020maAlmMsaRxLos": pm20020maAlmMsaRxLos,
       "pm20020maAlmMsaTxHostLol": pm20020maAlmMsaTxHostLol,
       "pm20020maAlmMsaTxLosf": pm20020maAlmMsaTxLosf,
       "pm20020maAlmMsaTxCmuLol": pm20020maAlmMsaTxCmuLol,
       "pm20020maAlmMsaTxJitterPllLol": pm20020maAlmMsaTxJitterPllLol,
       "pm20020maAlmMsaLossOfRefclk": pm20020maAlmMsaLossOfRefclk,
       "pm20020maAlmMsaHwInterlock": pm20020maAlmMsaHwInterlock,
       "pm20020maAlmmsaGlobalAlarmSummary": pm20020maAlmmsaGlobalAlarmSummary,
       "pm20020maAlmMsaSoftGlobAlarmTest": pm20020maAlmMsaSoftGlobAlarmTest,
       "pm20020maAlmMsaNetworkHostAlarmStatus": pm20020maAlmMsaNetworkHostAlarmStatus,
       "pm20020maAlmMsaNetworkLaneAlarmWarning2": pm20020maAlmMsaNetworkLaneAlarmWarning2,
       "pm20020maAlmMsaModuleState": pm20020maAlmMsaModuleState,
       "pm20020maAlmMsaModuleGeneralStatus": pm20020maAlmMsaModuleGeneralStatus,
       "pm20020maAlmModuleFault": pm20020maAlmModuleFault,
       "pm20020maAlmMsaModuleAlarmWarning1": pm20020maAlmMsaModuleAlarmWarning1,
       "pm20020maAlmMsaModuleAlarmWarning2": pm20020maAlmMsaModuleAlarmWarning2,
       "pm20020maAlmMsaNetworkLaneAlarmWarning1": pm20020maAlmMsaNetworkLaneAlarmWarning1,
       "pm20020maAlmMsaNetworkLaneFaultStatus": pm20020maAlmMsaNetworkLaneFaultStatus,
       "pm20020maAlmMsaHostLaneFaultStatus": pm20020maAlmMsaHostLaneFaultStatus,
       "pm20020maAlmMsaGlobAlarmAssertion": pm20020maAlmMsaGlobAlarmAssertion,
       "pm20020maAlmmsaNetworkTxAlignment": pm20020maAlmmsaNetworkTxAlignment,
       "pm20020maAlmNetTxTimingFault": pm20020maAlmNetTxTimingFault,
       "pm20020maAlmNetTxReferenceClockFault": pm20020maAlmNetTxReferenceClockFault,
       "pm20020maAlmNetTxCmuLockFault": pm20020maAlmNetTxCmuLockFault,
       "pm20020maAlmNetTxOutOfAlignment": pm20020maAlmNetTxOutOfAlignment,
       "pm20020maAlmNetTxLossOfAlignment": pm20020maAlmNetTxLossOfAlignment,
       "pm20020maAlmmsaNetworkRxAlignment": pm20020maAlmmsaNetworkRxAlignment,
       "pm20020maAlmNetRxTimingFault": pm20020maAlmNetRxTimingFault,
       "pm20020maAlmNetRxOutOfAlignment": pm20020maAlmNetRxOutOfAlignment,
       "pm20020maAlmNetRxLossOfAlignment": pm20020maAlmNetRxLossOfAlignment,
       "pm20020maAlmNetRxModemLockFault": pm20020maAlmNetRxModemLockFault,
       "pm20020maAlmNetRxModemSyncDetectFault": pm20020maAlmNetRxModemSyncDetectFault,
       "pm20020maAlmmsaNetworkHostNetworkAlarmSummary": pm20020maAlmmsaNetworkHostNetworkAlarmSummary,
       "pm20020maAlmNetworkTxAlignment": pm20020maAlmNetworkTxAlignment,
       "pm20020maAlmNetworkRxAlignment": pm20020maAlmNetworkRxAlignment,
       "pm20020maAlmNetworkRxOtn": pm20020maAlmNetworkRxOtn,
       "pm20020maAlmHostRxAlignment": pm20020maAlmHostRxAlignment,
       "pm20020maAlmHostTxAlignment": pm20020maAlmHostTxAlignment,
       "pm20020maAlmHostTxOtnStatus": pm20020maAlmHostTxOtnStatus,
       "pm20020maAlmmsaHostTxAlignment": pm20020maAlmmsaHostTxAlignment,
       "pm20020maAlmHostTxDeskewLockFault": pm20020maAlmHostTxDeskewLockFault,
       "pm20020maAlmHostTxOutOfAlignment": pm20020maAlmHostTxOutOfAlignment,
       "pm20020maAlmHostTxLossOfAlignment": pm20020maAlmHostTxLossOfAlignment,
       "pm20020maAlmHostTxCdrLockFault": pm20020maAlmHostTxCdrLockFault,
       "pm20020maAlmmsaHostRxAlignment": pm20020maAlmmsaHostRxAlignment,
       "pm20020maAlmHostRxCmuLockFault": pm20020maAlmHostRxCmuLockFault,
       "pm20020maAlmHostRxOutOfAlignment": pm20020maAlmHostRxOutOfAlignment,
       "pm20020maAlmHostRxLossOfAlignment": pm20020maAlmHostRxLossOfAlignment,
       "pm20020maAlmClient": pm20020maAlmClient,
       "pm20020maAlmClientNurg": pm20020maAlmClientNurg,
       "pm20020maAlmclientNetworkLaneAlarmWarningTable": pm20020maAlmclientNetworkLaneAlarmWarningTable,
       "pm20020maAlmclientNetworkLaneAlarmWarningEntry": pm20020maAlmclientNetworkLaneAlarmWarningEntry,
       "pm20020maAlmclientNetworkLaneAlarmWarningIndex": pm20020maAlmclientNetworkLaneAlarmWarningIndex,
       "pm20020maAlmClientRxPowerLowAlarmPortn": pm20020maAlmClientRxPowerLowAlarmPortn,
       "pm20020maAlmClientRxPowerLowWarningPortn": pm20020maAlmClientRxPowerLowWarningPortn,
       "pm20020maAlmClientRxPowerHighWarningPortn": pm20020maAlmClientRxPowerHighWarningPortn,
       "pm20020maAlmClientRxPowerHighAlarmPortn": pm20020maAlmClientRxPowerHighAlarmPortn,
       "pm20020maAlmLaserTempLowAlarmPortn": pm20020maAlmLaserTempLowAlarmPortn,
       "pm20020maAlmClientLaserTempLowWarningPortn": pm20020maAlmClientLaserTempLowWarningPortn,
       "pm20020maAlmClientLaserTempHighWarningPortn": pm20020maAlmClientLaserTempHighWarningPortn,
       "pm20020maAlmClientLaserTempHighAlarmPortn": pm20020maAlmClientLaserTempHighAlarmPortn,
       "pm20020maAlmClientTxPowerLowAlarmPortn": pm20020maAlmClientTxPowerLowAlarmPortn,
       "pm20020maAlmClientTxPowerLowWarningPortn": pm20020maAlmClientTxPowerLowWarningPortn,
       "pm20020maAlmClientTxPowerHighWarningPortn": pm20020maAlmClientTxPowerHighWarningPortn,
       "pm20020maAlmClientTxPowerHighAlarmPortn": pm20020maAlmClientTxPowerHighAlarmPortn,
       "pm20020maAlmClientBiasLowAlarmPortn": pm20020maAlmClientBiasLowAlarmPortn,
       "pm20020maAlmClientBiasLowWarningPortn": pm20020maAlmClientBiasLowWarningPortn,
       "pm20020maAlmClientBiasHighWarningPortn": pm20020maAlmClientBiasHighWarningPortn,
       "pm20020maAlmClientBiasHighAlarmPortn": pm20020maAlmClientBiasHighAlarmPortn,
       "pm20020maAlmclientSfpWarnDdmTable": pm20020maAlmclientSfpWarnDdmTable,
       "pm20020maAlmclientSfpWarnDdmEntry": pm20020maAlmclientSfpWarnDdmEntry,
       "pm20020maAlmclientSfpWarnDdmIndex": pm20020maAlmclientSfpWarnDdmIndex,
       "pm20020maAlmTxPwLowWngPortn": pm20020maAlmTxPwLowWngPortn,
       "pm20020maAlmTxPwrHighWngPortn": pm20020maAlmTxPwrHighWngPortn,
       "pm20020maAlmTxBiasLowWngPortn": pm20020maAlmTxBiasLowWngPortn,
       "pm20020maAlmTxBiasHighWngPortn": pm20020maAlmTxBiasHighWngPortn,
       "pm20020maAlmVccLowWngPortn": pm20020maAlmVccLowWngPortn,
       "pm20020maAlmVccHighWngPortn": pm20020maAlmVccHighWngPortn,
       "pm20020maAlmTempLowWngPortn": pm20020maAlmTempLowWngPortn,
       "pm20020maAlmTempHighWngPortn": pm20020maAlmTempHighWngPortn,
       "pm20020maAlmRxPwrLowWngPortn": pm20020maAlmRxPwrLowWngPortn,
       "pm20020maAlmRxPwrHighWngPortn": pm20020maAlmRxPwrHighWngPortn,
       "pm20020maAlmClientUrg": pm20020maAlmClientUrg,
       "pm20020maAlmclientNetworkLaneFaultTable": pm20020maAlmclientNetworkLaneFaultTable,
       "pm20020maAlmclientNetworkLaneFaultEntry": pm20020maAlmclientNetworkLaneFaultEntry,
       "pm20020maAlmclientNetworkLaneFaultIndex": pm20020maAlmclientNetworkLaneFaultIndex,
       "pm20020maAlmClientLaneRxFifoErrorPortn": pm20020maAlmClientLaneRxFifoErrorPortn,
       "pm20020maAlmClientLaneRxLolPortn": pm20020maAlmClientLaneRxLolPortn,
       "pm20020maAlmClientLaneRxLosPortn": pm20020maAlmClientLaneRxLosPortn,
       "pm20020maAlmClientLaneTxLolPortn": pm20020maAlmClientLaneTxLolPortn,
       "pm20020maAlmClientLaneTxLosfPortn": pm20020maAlmClientLaneTxLosfPortn,
       "pm20020maAlmClientLaneApdPowerSupplyPortn": pm20020maAlmClientLaneApdPowerSupplyPortn,
       "pm20020maAlmClientLaneWavelengthUnlockedPortn": pm20020maAlmClientLaneWavelengthUnlockedPortn,
       "pm20020maAlmClientLaneTecFaultPortn": pm20020maAlmClientLaneTecFaultPortn,
       "pm20020maAlmclientHostLaneFaultTable": pm20020maAlmclientHostLaneFaultTable,
       "pm20020maAlmclientHostLaneFaultEntry": pm20020maAlmclientHostLaneFaultEntry,
       "pm20020maAlmclientHostLaneFaultIndex": pm20020maAlmclientHostLaneFaultIndex,
       "pm20020maAlmClientLossOfSyncPortn": pm20020maAlmClientLossOfSyncPortn,
       "pm20020maAlmClientInputLossOfSigPortn": pm20020maAlmClientInputLossOfSigPortn,
       "pm20020maAlmClientLanesMarkerUnlockPortn": pm20020maAlmClientLanesMarkerUnlockPortn,
       "pm20020maAlmClientLanes6466UnlockPortn": pm20020maAlmClientLanes6466UnlockPortn,
       "pm20020maAlmClientLanesNotAlignedPortn": pm20020maAlmClientLanesNotAlignedPortn,
       "pm20020maAlmClientCsfDetectedPortn": pm20020maAlmClientCsfDetectedPortn,
       "pm20020maAlmClientTxHostLolPortn": pm20020maAlmClientTxHostLolPortn,
       "pm20020maAlmClientLaneTxFifoErrorPortn": pm20020maAlmClientLaneTxFifoErrorPortn,
       "pm20020maAlmclientSfpAlmDdmTable": pm20020maAlmclientSfpAlmDdmTable,
       "pm20020maAlmclientSfpAlmDdmEntry": pm20020maAlmclientSfpAlmDdmEntry,
       "pm20020maAlmclientSfpAlmDdmIndex": pm20020maAlmclientSfpAlmDdmIndex,
       "pm20020maAlmTxPwrLowAlaPortn": pm20020maAlmTxPwrLowAlaPortn,
       "pm20020maAlmTxPwrHighAlaPortn": pm20020maAlmTxPwrHighAlaPortn,
       "pm20020maAlmTxBiasLowAlaPortn": pm20020maAlmTxBiasLowAlaPortn,
       "pm20020maAlmTxBiasHighAlaPortn": pm20020maAlmTxBiasHighAlaPortn,
       "pm20020maAlmVccLowAlaPortn": pm20020maAlmVccLowAlaPortn,
       "pm20020maAlmVccHighAlaPortn": pm20020maAlmVccHighAlaPortn,
       "pm20020maAlmTempLowAlaPortn": pm20020maAlmTempLowAlaPortn,
       "pm20020maAlmTempHighAlaPortn": pm20020maAlmTempHighAlaPortn,
       "pm20020maAlmRxPwrLowAlaPortn": pm20020maAlmRxPwrLowAlaPortn,
       "pm20020maAlmRxPwrHighAlaPortn": pm20020maAlmRxPwrHighAlaPortn,
       "pm20020maAlmClientCrit": pm20020maAlmClientCrit,
       "pm20020maAlmsynthAlmPortTable": pm20020maAlmsynthAlmPortTable,
       "pm20020maAlmsynthAlmPortEntry": pm20020maAlmsynthAlmPortEntry,
       "pm20020maAlmsynthAlmPortIndex": pm20020maAlmsynthAlmPortIndex,
       "pm20020maAlmSfpAbsentPortn": pm20020maAlmSfpAbsentPortn,
       "pm20020maAlmDdmAbsentPortn": pm20020maAlmDdmAbsentPortn,
       "pm20020maAlmHwFailAccPortn": pm20020maAlmHwFailAccPortn,
       "pm20020maAlmDwLsdPortn": pm20020maAlmDwLsdPortn,
       "pm20020maAlmClientLocalOosPortn": pm20020maAlmClientLocalOosPortn,
       "pm20020maAlmClientRemoteOosPortn": pm20020maAlmClientRemoteOosPortn,
       "pm20020maAlmDwCaisPortn": pm20020maAlmDwCaisPortn,
       "pm20020maAlmSfpDdmWarningPortn": pm20020maAlmSfpDdmWarningPortn,
       "pm20020maAlmSfpDdmAlmPortn": pm20020maAlmSfpDdmAlmPortn,
       "pm20020maAlmFailAccPortn": pm20020maAlmFailAccPortn,
       "pm20020maAlmUpCsfPortn": pm20020maAlmUpCsfPortn,
       "pm20020maAlmLine": pm20020maAlmLine,
       "pm20020maAlmLineNurg": pm20020maAlmLineNurg,
       "pm20020maAlmlineNetworkLaneAlarmWarning1Table": pm20020maAlmlineNetworkLaneAlarmWarning1Table,
       "pm20020maAlmlineNetworkLaneAlarmWarning1Entry": pm20020maAlmlineNetworkLaneAlarmWarning1Entry,
       "pm20020maAlmlineNetworkLaneAlarmWarning1Index": pm20020maAlmlineNetworkLaneAlarmWarning1Index,
       "pm20020maAlmLineRxPowerLowAlarmPortn": pm20020maAlmLineRxPowerLowAlarmPortn,
       "pm20020maAlmLineRxPowerLowWarningPortn": pm20020maAlmLineRxPowerLowWarningPortn,
       "pm20020maAlmLineRxPowerHighWarningPortn": pm20020maAlmLineRxPowerHighWarningPortn,
       "pm20020maAlmLineRxPowerHighAlarmPortn": pm20020maAlmLineRxPowerHighAlarmPortn,
       "pm20020maAlmLineLaserTempLowAlarmPortn": pm20020maAlmLineLaserTempLowAlarmPortn,
       "pm20020maAlmLineLaserTempLowWarningPortn": pm20020maAlmLineLaserTempLowWarningPortn,
       "pm20020maAlmLineLaserTempHighWarningPortn": pm20020maAlmLineLaserTempHighWarningPortn,
       "pm20020maAlmLineLaserTempHighAlarmPortn": pm20020maAlmLineLaserTempHighAlarmPortn,
       "pm20020maAlmLineTxPowerLowAlarmPortn": pm20020maAlmLineTxPowerLowAlarmPortn,
       "pm20020maAlmLineTxPowerLowWarningPortn": pm20020maAlmLineTxPowerLowWarningPortn,
       "pm20020maAlmLineTxPowerHighWarningPortn": pm20020maAlmLineTxPowerHighWarningPortn,
       "pm20020maAlmLineTxPowerHighAlarmPortn": pm20020maAlmLineTxPowerHighAlarmPortn,
       "pm20020maAlmLineBiasLowAlarmPortn": pm20020maAlmLineBiasLowAlarmPortn,
       "pm20020maAlmLineBiasLowWarningPortn": pm20020maAlmLineBiasLowWarningPortn,
       "pm20020maAlmLineBiasHighWarningPortn": pm20020maAlmLineBiasHighWarningPortn,
       "pm20020maAlmLineBiasHighAlarmPortn": pm20020maAlmLineBiasHighAlarmPortn,
       "pm20020maAlmlineNetworkLaneAlarmWarning2Table": pm20020maAlmlineNetworkLaneAlarmWarning2Table,
       "pm20020maAlmlineNetworkLaneAlarmWarning2Entry": pm20020maAlmlineNetworkLaneAlarmWarning2Entry,
       "pm20020maAlmlineNetworkLaneAlarmWarning2Index": pm20020maAlmlineNetworkLaneAlarmWarning2Index,
       "pm20020maAlmTxModulatorBiasLowAlarmPortn": pm20020maAlmTxModulatorBiasLowAlarmPortn,
       "pm20020maAlmTxModulatorBiasLowWarningPortn": pm20020maAlmTxModulatorBiasLowWarningPortn,
       "pm20020maAlmTxModulatorBiasHighWarningPortn": pm20020maAlmTxModulatorBiasHighWarningPortn,
       "pm20020maAlmTxModulatorBiasHighAlarmPortn": pm20020maAlmTxModulatorBiasHighAlarmPortn,
       "pm20020maAlmRxLaserTempLowAlarmPortn": pm20020maAlmRxLaserTempLowAlarmPortn,
       "pm20020maAlmRxLaserTempLowWarningPortn": pm20020maAlmRxLaserTempLowWarningPortn,
       "pm20020maAlmRxLaserTempHighWarningPortn": pm20020maAlmRxLaserTempHighWarningPortn,
       "pm20020maAlmRxLaserTempHighAlarmPortn": pm20020maAlmRxLaserTempHighAlarmPortn,
       "pm20020maAlmRxLaserOutputLowAlarmPortn": pm20020maAlmRxLaserOutputLowAlarmPortn,
       "pm20020maAlmRxLaserOutputLowWarningPortn": pm20020maAlmRxLaserOutputLowWarningPortn,
       "pm20020maAlmRxLaserOutputHighWarningPortn": pm20020maAlmRxLaserOutputHighWarningPortn,
       "pm20020maAlmRxLaserOutputHighAlarmPortn": pm20020maAlmRxLaserOutputHighAlarmPortn,
       "pm20020maAlmRxLaserBiasLowAlarmPortn": pm20020maAlmRxLaserBiasLowAlarmPortn,
       "pm20020maAlmRxLaserBiasLowWarningPortn": pm20020maAlmRxLaserBiasLowWarningPortn,
       "pm20020maAlmRxLaserBiasHighWarningPortn": pm20020maAlmRxLaserBiasHighWarningPortn,
       "pm20020maAlmRxLaserBiasHighAlarmPortn": pm20020maAlmRxLaserBiasHighAlarmPortn,
       "pm20020maAlmLineUrg": pm20020maAlmLineUrg,
       "pm20020maAlmlineNetworkLaneFaultTable": pm20020maAlmlineNetworkLaneFaultTable,
       "pm20020maAlmlineNetworkLaneFaultEntry": pm20020maAlmlineNetworkLaneFaultEntry,
       "pm20020maAlmlineNetworkLaneFaultIndex": pm20020maAlmlineNetworkLaneFaultIndex,
       "pm20020maAlmLineLaneRxTecFaultPortn": pm20020maAlmLineLaneRxTecFaultPortn,
       "pm20020maAlmLineLaneRxFifoErrorPortn": pm20020maAlmLineLaneRxFifoErrorPortn,
       "pm20020maAlmLineLaneRxLolPortn": pm20020maAlmLineLaneRxLolPortn,
       "pm20020maAlmLineLaneRxLosPortn": pm20020maAlmLineLaneRxLosPortn,
       "pm20020maAlmLineLaneTxLolPortn": pm20020maAlmLineLaneTxLolPortn,
       "pm20020maAlmLineLaneTxLosfPortn": pm20020maAlmLineLaneTxLosfPortn,
       "pm20020maAlmLineLaneApdPowerSupplyPortn": pm20020maAlmLineLaneApdPowerSupplyPortn,
       "pm20020maAlmLineLaneWavelengthUnlockedPortn": pm20020maAlmLineLaneWavelengthUnlockedPortn,
       "pm20020maAlmLineLaneTecFaultPortn": pm20020maAlmLineLaneTecFaultPortn,
       "pm20020maAlmlineHostLaneFaultTable": pm20020maAlmlineHostLaneFaultTable,
       "pm20020maAlmlineHostLaneFaultEntry": pm20020maAlmlineHostLaneFaultEntry,
       "pm20020maAlmlineHostLaneFaultIndex": pm20020maAlmlineHostLaneFaultIndex,
       "pm20020maAlmLineInputLossOfSignalPortn": pm20020maAlmLineInputLossOfSignalPortn,
       "pm20020maAlmLineLossOfFramePortn": pm20020maAlmLineLossOfFramePortn,
       "pm20020maAlmLineSmBdiInsertedPortn": pm20020maAlmLineSmBdiInsertedPortn,
       "pm20020maAlmLineSmBdiDetectedPortn": pm20020maAlmLineSmBdiDetectedPortn,
       "pm20020maAlmLineSmIaeInsertedPortn": pm20020maAlmLineSmIaeInsertedPortn,
       "pm20020maAlmLineSmIaeDetectedPortn": pm20020maAlmLineSmIaeDetectedPortn,
       "pm20020maAlmLineTxHostLolPortn": pm20020maAlmLineTxHostLolPortn,
       "pm20020maAlmLineLaneTxFifoErrorPortn": pm20020maAlmLineLaneTxFifoErrorPortn,
       "pm20020maAlmlineNetworkLaneRxOtnTable": pm20020maAlmlineNetworkLaneRxOtnTable,
       "pm20020maAlmlineNetworkLaneRxOtnEntry": pm20020maAlmlineNetworkLaneRxOtnEntry,
       "pm20020maAlmlineNetworkLaneRxOtnIndex": pm20020maAlmlineNetworkLaneRxOtnIndex,
       "pm20020maAlmLineRxOtnOduAisPortn": pm20020maAlmLineRxOtnOduAisPortn,
       "pm20020maAlmLineRxOtnOtuAisPortn": pm20020maAlmLineRxOtnOtuAisPortn,
       "pm20020maAlmLineRxSmBdiPortn": pm20020maAlmLineRxSmBdiPortn,
       "pm20020maAlmLineRxOtnIaePortn": pm20020maAlmLineRxOtnIaePortn,
       "pm20020maAlmLineRxOtnOomPortn": pm20020maAlmLineRxOtnOomPortn,
       "pm20020maAlmLineRxOtnLomPortn": pm20020maAlmLineRxOtnLomPortn,
       "pm20020maAlmLineRxOtnOofPortn": pm20020maAlmLineRxOtnOofPortn,
       "pm20020maAlmLineRxOtnLofPortn": pm20020maAlmLineRxOtnLofPortn,
       "pm20020maAlmlineHostLaneTxOtnTable": pm20020maAlmlineHostLaneTxOtnTable,
       "pm20020maAlmlineHostLaneTxOtnEntry": pm20020maAlmlineHostLaneTxOtnEntry,
       "pm20020maAlmlineHostLaneTxOtnIndex": pm20020maAlmlineHostLaneTxOtnIndex,
       "pm20020maAlmLineTxOtnOduAisPortn": pm20020maAlmLineTxOtnOduAisPortn,
       "pm20020maAlmLineTxOtnOtuAisPortn": pm20020maAlmLineTxOtnOtuAisPortn,
       "pm20020maAlmLineTxSmBdiPortn": pm20020maAlmLineTxSmBdiPortn,
       "pm20020maAlmLineTxOtnIaePortn": pm20020maAlmLineTxOtnIaePortn,
       "pm20020maAlmLineTxOtnOomPortn": pm20020maAlmLineTxOtnOomPortn,
       "pm20020maAlmLineTxOtnLomPortn": pm20020maAlmLineTxOtnLomPortn,
       "pm20020maAlmLineTxOtnOofPortn": pm20020maAlmLineTxOtnOofPortn,
       "pm20020maAlmLineTxOtnLofPortn": pm20020maAlmLineTxOtnLofPortn,
       "pm20020maAlmLineCrit": pm20020maAlmLineCrit,
       "pm20020maAlmsynthAlmLineTable": pm20020maAlmsynthAlmLineTable,
       "pm20020maAlmsynthAlmLineEntry": pm20020maAlmsynthAlmLineEntry,
       "pm20020maAlmsynthAlmLineIndex": pm20020maAlmsynthAlmLineIndex,
       "pm20020maAlmXfpAbsentPortn": pm20020maAlmXfpAbsentPortn,
       "pm20020maAlmXfpInitNotComplPortn": pm20020maAlmXfpInitNotComplPortn,
       "pm20020maAlmLineHwFailPortn": pm20020maAlmLineHwFailPortn,
       "pm20020maAlmXfpTxOffPortn": pm20020maAlmXfpTxOffPortn,
       "pm20020maAlmLineLocalOosPortn": pm20020maAlmLineLocalOosPortn,
       "pm20020maAlmUpRdiInsPortn": pm20020maAlmUpRdiInsPortn,
       "pm20020maAlmLineDdmWarningPortn": pm20020maAlmLineDdmWarningPortn,
       "pm20020maAlmLineDdmAlmPortn": pm20020maAlmLineDdmAlmPortn,
       "pm20020maAlmLineFailPortn": pm20020maAlmLineFailPortn,
       "pm20020maAlmLineActivePortn": pm20020maAlmLineActivePortn,
       "pm20020mameasures": pm20020mameasures,
       "pm20020maMesrOther": pm20020maMesrOther,
       "pm20020maMesrsynth0": pm20020maMesrsynth0,
       "pm20020maMesrsynth1": pm20020maMesrsynth1,
       "pm20020maMesrpmIntervalNumber": pm20020maMesrpmIntervalNumber,
       "pm20020maMesrlineNetTxLaserOutputPwrAverage": pm20020maMesrlineNetTxLaserOutputPwrAverage,
       "pm20020maMesrlineNetTxLaserTempAverage": pm20020maMesrlineNetTxLaserTempAverage,
       "pm20020maMesrlineNetTxBiasCurrentAverage": pm20020maMesrlineNetTxBiasCurrentAverage,
       "pm20020maMesrlineNetRxInputPwrAverage": pm20020maMesrlineNetRxInputPwrAverage,
       "pm20020maMesrlineResidualChromaticDispAverage": pm20020maMesrlineResidualChromaticDispAverage,
       "pm20020maMesrlineDiffGroupDelayAverage": pm20020maMesrlineDiffGroupDelayAverage,
       "pm20020maMesrlineQFactorAverage": pm20020maMesrlineQFactorAverage,
       "pm20020maMesrlineCarrierFreqOffsetAverage": pm20020maMesrlineCarrierFreqOffsetAverage,
       "pm20020maMesrlineOsnrAverage": pm20020maMesrlineOsnrAverage,
       "pm20020maMesrclientNetTxTempMin": pm20020maMesrclientNetTxTempMin,
       "pm20020maMesrclientNetTxBiasMin": pm20020maMesrclientNetTxBiasMin,
       "pm20020maMesrclientNetTxPwrMin": pm20020maMesrclientNetTxPwrMin,
       "pm20020maMesrclientNetRxPwrMin": pm20020maMesrclientNetRxPwrMin,
       "pm20020maMesrlineNetTxLaserOutputPwrMin": pm20020maMesrlineNetTxLaserOutputPwrMin,
       "pm20020maMesrlineNetTxLaserTempMin": pm20020maMesrlineNetTxLaserTempMin,
       "pm20020maMesrlineNetTxBiasCurrentMin": pm20020maMesrlineNetTxBiasCurrentMin,
       "pm20020maMesrlineNetRxInputPwrMin": pm20020maMesrlineNetRxInputPwrMin,
       "pm20020maMesrlineResidualChromaticDispMin": pm20020maMesrlineResidualChromaticDispMin,
       "pm20020maMesrlineDiffGroupDelayMin": pm20020maMesrlineDiffGroupDelayMin,
       "pm20020maMesrlineQFactorMin": pm20020maMesrlineQFactorMin,
       "pm20020maMesrlineCarrierFreqOffsetMin": pm20020maMesrlineCarrierFreqOffsetMin,
       "pm20020maMesrlineOsnrMin": pm20020maMesrlineOsnrMin,
       "pm20020maMesrclientNetTxTempMax": pm20020maMesrclientNetTxTempMax,
       "pm20020maMesrclientNetTxBiasMax": pm20020maMesrclientNetTxBiasMax,
       "pm20020maMesrclientNetTxPwrMax": pm20020maMesrclientNetTxPwrMax,
       "pm20020maMesrclientNetRxPwrMax": pm20020maMesrclientNetRxPwrMax,
       "pm20020maMesrlineNetTxLaserOutputPwrMax": pm20020maMesrlineNetTxLaserOutputPwrMax,
       "pm20020maMesrlineNetTxLaserTempMax": pm20020maMesrlineNetTxLaserTempMax,
       "pm20020maMesrlineNetTxBiasCurrentMax": pm20020maMesrlineNetTxBiasCurrentMax,
       "pm20020maMesrlineNetRxInputPwrMax": pm20020maMesrlineNetRxInputPwrMax,
       "pm20020maMesrlineResidualChromaticDispMax": pm20020maMesrlineResidualChromaticDispMax,
       "pm20020maMesrlineDiffGroupDelayMax": pm20020maMesrlineDiffGroupDelayMax,
       "pm20020maMesrlineQFactorMax": pm20020maMesrlineQFactorMax,
       "pm20020maMesrlineCarrierFreqOffsetMax": pm20020maMesrlineCarrierFreqOffsetMax,
       "pm20020maMesrlineOsnrMax": pm20020maMesrlineOsnrMax,
       "pm20020maMesrClient": pm20020maMesrClient,
       "pm20020maMesrclientCfpTemp": pm20020maMesrclientCfpTemp,
       "pm20020maMesrclientCfp3v3Voltage": pm20020maMesrclientCfp3v3Voltage,
       "pm20020maMesrclientSoaBiasCurrent": pm20020maMesrclientSoaBiasCurrent,
       "pm20020maMesrclientNetTxTempTable": pm20020maMesrclientNetTxTempTable,
       "pm20020maMesrclientNetTxTempEntry": pm20020maMesrclientNetTxTempEntry,
       "pm20020maMesrclientNetTxTempIndex": pm20020maMesrclientNetTxTempIndex,
       "pm20020maMesrclientNetTxTempPortn": pm20020maMesrclientNetTxTempPortn,
       "pm20020maMesrclientNetTxBiasTable": pm20020maMesrclientNetTxBiasTable,
       "pm20020maMesrclientNetTxBiasEntry": pm20020maMesrclientNetTxBiasEntry,
       "pm20020maMesrclientNetTxBiasIndex": pm20020maMesrclientNetTxBiasIndex,
       "pm20020maMesrclientNetTxBiasPortn": pm20020maMesrclientNetTxBiasPortn,
       "pm20020maMesrclientNetTxPwrTable": pm20020maMesrclientNetTxPwrTable,
       "pm20020maMesrclientNetTxPwrEntry": pm20020maMesrclientNetTxPwrEntry,
       "pm20020maMesrclientNetTxPwrIndex": pm20020maMesrclientNetTxPwrIndex,
       "pm20020maMesrclientNetTxPwrPortn": pm20020maMesrclientNetTxPwrPortn,
       "pm20020maMesrclientNetRxPwrTable": pm20020maMesrclientNetRxPwrTable,
       "pm20020maMesrclientNetRxPwrEntry": pm20020maMesrclientNetRxPwrEntry,
       "pm20020maMesrclientNetRxPwrIndex": pm20020maMesrclientNetRxPwrIndex,
       "pm20020maMesrclientNetRxPwrPortn": pm20020maMesrclientNetRxPwrPortn,
       "pm20020maMesrLine": pm20020maMesrLine,
       "pm20020maMesrlineMsaTemp": pm20020maMesrlineMsaTemp,
       "pm20020maMesrlineMsa3v3Voltage": pm20020maMesrlineMsa3v3Voltage,
       "pm20020maMesrlineSoaBiasCurrent": pm20020maMesrlineSoaBiasCurrent,
       "pm20020maMesrlineNetTxLaserOutputPwrTable": pm20020maMesrlineNetTxLaserOutputPwrTable,
       "pm20020maMesrlineNetTxLaserOutputPwrEntry": pm20020maMesrlineNetTxLaserOutputPwrEntry,
       "pm20020maMesrlineNetTxLaserOutputPwrIndex": pm20020maMesrlineNetTxLaserOutputPwrIndex,
       "pm20020maMesrlineNetTxLaserOutputPwrPortn": pm20020maMesrlineNetTxLaserOutputPwrPortn,
       "pm20020maMesrlineNetTxLaserTempTable": pm20020maMesrlineNetTxLaserTempTable,
       "pm20020maMesrlineNetTxLaserTempEntry": pm20020maMesrlineNetTxLaserTempEntry,
       "pm20020maMesrlineNetTxLaserTempIndex": pm20020maMesrlineNetTxLaserTempIndex,
       "pm20020maMesrlineNetTxLaserTempPortn": pm20020maMesrlineNetTxLaserTempPortn,
       "pm20020maMesrlineNetTxBiasCurrentTable": pm20020maMesrlineNetTxBiasCurrentTable,
       "pm20020maMesrlineNetTxBiasCurrentEntry": pm20020maMesrlineNetTxBiasCurrentEntry,
       "pm20020maMesrlineNetTxBiasCurrentIndex": pm20020maMesrlineNetTxBiasCurrentIndex,
       "pm20020maMesrlineNetTxBiasCurrentPortn": pm20020maMesrlineNetTxBiasCurrentPortn,
       "pm20020maMesrlineNetRxInputPwrTable": pm20020maMesrlineNetRxInputPwrTable,
       "pm20020maMesrlineNetRxInputPwrEntry": pm20020maMesrlineNetRxInputPwrEntry,
       "pm20020maMesrlineNetRxInputPwrIndex": pm20020maMesrlineNetRxInputPwrIndex,
       "pm20020maMesrlineNetRxInputPwrPortn": pm20020maMesrlineNetRxInputPwrPortn,
       "pm20020maMesrlineResidualChromaticDispTable": pm20020maMesrlineResidualChromaticDispTable,
       "pm20020maMesrlineResidualChromaticDispEntry": pm20020maMesrlineResidualChromaticDispEntry,
       "pm20020maMesrlineResidualChromaticDispIndex": pm20020maMesrlineResidualChromaticDispIndex,
       "pm20020maMesrlineResidualChromaticDispPortn": pm20020maMesrlineResidualChromaticDispPortn,
       "pm20020maMesrlineDiffGroupDelayTable": pm20020maMesrlineDiffGroupDelayTable,
       "pm20020maMesrlineDiffGroupDelayEntry": pm20020maMesrlineDiffGroupDelayEntry,
       "pm20020maMesrlineDiffGroupDelayIndex": pm20020maMesrlineDiffGroupDelayIndex,
       "pm20020maMesrlineDiffGroupDelayPortn": pm20020maMesrlineDiffGroupDelayPortn,
       "pm20020maMesrlineQFactorTable": pm20020maMesrlineQFactorTable,
       "pm20020maMesrlineQFactorEntry": pm20020maMesrlineQFactorEntry,
       "pm20020maMesrlineQFactorIndex": pm20020maMesrlineQFactorIndex,
       "pm20020maMesrlineQFactorPortn": pm20020maMesrlineQFactorPortn,
       "pm20020maMesrlineCarrierFreqOffsetTable": pm20020maMesrlineCarrierFreqOffsetTable,
       "pm20020maMesrlineCarrierFreqOffsetEntry": pm20020maMesrlineCarrierFreqOffsetEntry,
       "pm20020maMesrlineCarrierFreqOffsetIndex": pm20020maMesrlineCarrierFreqOffsetIndex,
       "pm20020maMesrlineCarrierFreqOffsetPortn": pm20020maMesrlineCarrierFreqOffsetPortn,
       "pm20020maMesrlineOsnrTable": pm20020maMesrlineOsnrTable,
       "pm20020maMesrlineOsnrEntry": pm20020maMesrlineOsnrEntry,
       "pm20020maMesrlineOsnrIndex": pm20020maMesrlineOsnrIndex,
       "pm20020maMesrlineOsnrPortn": pm20020maMesrlineOsnrPortn,
       "pm20020macounters": pm20020macounters,
       "pm20020maCntOther": pm20020maCntOther,
       "pm20020maCntClient": pm20020maCntClient,
       "pm20020maCntclientInputErrorCounterTable": pm20020maCntclientInputErrorCounterTable,
       "pm20020maCntclientInputErrorCounterEntry": pm20020maCntclientInputErrorCounterEntry,
       "pm20020maCntclientInputErrorCounterIndex": pm20020maCntclientInputErrorCounterIndex,
       "pm20020maCntclientInputErrorCounterValuePortn": pm20020maCntclientInputErrorCounterValuePortn,
       "pm20020maCntclientInputErrorCounterErrorPortn": pm20020maCntclientInputErrorCounterErrorPortn,
       "pm20020maCntclientInputErrorCounterOverloadPortn": pm20020maCntclientInputErrorCounterOverloadPortn,
       "pm20020maCntclientCbipCounterTable": pm20020maCntclientCbipCounterTable,
       "pm20020maCntclientCbipCounterEntry": pm20020maCntclientCbipCounterEntry,
       "pm20020maCntclientCbipCounterIndex": pm20020maCntclientCbipCounterIndex,
       "pm20020maCntclientCbipCounterValuePortn": pm20020maCntclientCbipCounterValuePortn,
       "pm20020maCntclientCbipCounterErrorPortn": pm20020maCntclientCbipCounterErrorPortn,
       "pm20020maCntclientCbipCounterOverloadPortn": pm20020maCntclientCbipCounterOverloadPortn,
       "pm20020maCntLine": pm20020maCntLine,
       "pm20020maCntlocalLineSmBip8ErrorCounterTable": pm20020maCntlocalLineSmBip8ErrorCounterTable,
       "pm20020maCntlocalLineSmBip8ErrorCounterEntry": pm20020maCntlocalLineSmBip8ErrorCounterEntry,
       "pm20020maCntlocalLineSmBip8ErrorCounterIndex": pm20020maCntlocalLineSmBip8ErrorCounterIndex,
       "pm20020maCntlocalLineSmBip8ErrorCounterValuePortn": pm20020maCntlocalLineSmBip8ErrorCounterValuePortn,
       "pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn": pm20020maCntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn": pm20020maCntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm20020maCntlocalLineFecCorrectedErrorsCounterTable": pm20020maCntlocalLineFecCorrectedErrorsCounterTable,
       "pm20020maCntlocalLineFecCorrectedErrorsCounterEntry": pm20020maCntlocalLineFecCorrectedErrorsCounterEntry,
       "pm20020maCntlocalLineFecCorrectedErrorsCounterIndex": pm20020maCntlocalLineFecCorrectedErrorsCounterIndex,
       "pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn": pm20020maCntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn": pm20020maCntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm20020maCntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm20020maCntremoteLineSmBip8ErrorCounterTable": pm20020maCntremoteLineSmBip8ErrorCounterTable,
       "pm20020maCntremoteLineSmBip8ErrorCounterEntry": pm20020maCntremoteLineSmBip8ErrorCounterEntry,
       "pm20020maCntremoteLineSmBip8ErrorCounterIndex": pm20020maCntremoteLineSmBip8ErrorCounterIndex,
       "pm20020maCntremoteLineSmBip8ErrorCounterValuePortn": pm20020maCntremoteLineSmBip8ErrorCounterValuePortn,
       "pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn": pm20020maCntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn": pm20020maCntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm20020maCntlineDfrmTimCntTable": pm20020maCntlineDfrmTimCntTable,
       "pm20020maCntlineDfrmTimCntEntry": pm20020maCntlineDfrmTimCntEntry,
       "pm20020maCntlineDfrmTimCntIndex": pm20020maCntlineDfrmTimCntIndex,
       "pm20020maCntlineDfrmTimCntValuePortn": pm20020maCntlineDfrmTimCntValuePortn,
       "pm20020maCntlineDfrmTimCntErrorPortn": pm20020maCntlineDfrmTimCntErrorPortn,
       "pm20020maCntlineDfrmTimCntOverloadPortn": pm20020maCntlineDfrmTimCntOverloadPortn,
       "pm20020maCntlocalLineTrscvPreSdFecErrorCounterTable": pm20020maCntlocalLineTrscvPreSdFecErrorCounterTable,
       "pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry": pm20020maCntlocalLineTrscvPreSdFecErrorCounterEntry,
       "pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex": pm20020maCntlocalLineTrscvPreSdFecErrorCounterIndex,
       "pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn": pm20020maCntlocalLineTrscvPreSdFecErrorCounterValuePortn,
       "pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn": pm20020maCntlocalLineTrscvPreSdFecErrorCounterErrorPortn,
       "pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn": pm20020maCntlocalLineTrscvPreSdFecErrorCounterOverloadPortn,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable": pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterTable,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry": pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterEntry,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex": pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterIndex,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn": pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn": pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn": pm20020maCntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn,
       "pm20020maCntlocalLineTrscvPreSdFecBitCounterTable": pm20020maCntlocalLineTrscvPreSdFecBitCounterTable,
       "pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry": pm20020maCntlocalLineTrscvPreSdFecBitCounterEntry,
       "pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex": pm20020maCntlocalLineTrscvPreSdFecBitCounterIndex,
       "pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn": pm20020maCntlocalLineTrscvPreSdFecBitCounterValuePortn,
       "pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn": pm20020maCntlocalLineTrscvPreSdFecBitCounterErrorPortn,
       "pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn": pm20020maCntlocalLineTrscvPreSdFecBitCounterOverloadPortn,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterTable": pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterTable,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry": pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterEntry,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex": pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterIndex,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn": pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn": pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn,
       "pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn": pm20020maCntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn,
       "pm20020macontrolsWrite": pm20020macontrolsWrite,
       "pm20020maCtrlOther": pm20020maCtrlOther,
       "pm20020maCtrlconfMgnt1": pm20020maCtrlconfMgnt1,
       "pm20020maCtrlConf1Load1": pm20020maCtrlConf1Load1,
       "pm20020maCtrlConf2Load1": pm20020maCtrlConf2Load1,
       "pm20020maCtrlConf2Flash1": pm20020maCtrlConf2Flash1,
       "pm20020maCtrlConf2Clear1": pm20020maCtrlConf2Clear1,
       "pm20020maCtrlsynth4": pm20020maCtrlsynth4,
       "pm20020maCtrlCorrelatOn": pm20020maCtrlCorrelatOn,
       "pm20020maCtrlCorrelatOff": pm20020maCtrlCorrelatOff,
       "pm20020maCtrlswMgnt": pm20020maCtrlswMgnt,
       "pm20020maCtrlColdReset": pm20020maCtrlColdReset,
       "pm20020maCtrlWarmReset": pm20020maCtrlWarmReset,
       "pm20020maCtrlLoadSwBank1": pm20020maCtrlLoadSwBank1,
       "pm20020maCtrlLoadSwBank2": pm20020maCtrlLoadSwBank2,
       "pm20020maCtrlgwMgnt": pm20020maCtrlgwMgnt,
       "pm20020maCtrlCurrentGwReset": pm20020maCtrlCurrentGwReset,
       "pm20020maCtrlLoadGwBank1": pm20020maCtrlLoadGwBank1,
       "pm20020maCtrlLoadGwBank2": pm20020maCtrlLoadGwBank2,
       "pm20020maCtrlLoadGwBank3": pm20020maCtrlLoadGwBank3,
       "pm20020maCtrlLoadGwBank4": pm20020maCtrlLoadGwBank4,
       "pm20020maCtrlledTest": pm20020maCtrlledTest,
       "pm20020maCtrlGreenLed": pm20020maCtrlGreenLed,
       "pm20020maCtrlRedLed": pm20020maCtrlRedLed,
       "pm20020maCtrlLedOff": pm20020maCtrlLedOff,
       "pm20020maCtrlinitSwitchMarvell": pm20020maCtrlinitSwitchMarvell,
       "pm20020maCtrlInitSwitchMarvell": pm20020maCtrlInitSwitchMarvell,
       "pm20020maCtrlresetCount": pm20020maCtrlresetCount,
       "pm20020maCtrlResetcount": pm20020maCtrlResetcount,
       "pm20020maCtrlresetRmon": pm20020maCtrlresetRmon,
       "pm20020maCtrlResetrmon": pm20020maCtrlResetrmon,
       "pm20020maCtrlresetMeasurements": pm20020maCtrlresetMeasurements,
       "pm20020maCtrlResetmeasurements": pm20020maCtrlResetmeasurements,
       "pm20020maCtrlClient": pm20020maCtrlClient,
       "pm20020maCtrlaccessLoopTable": pm20020maCtrlaccessLoopTable,
       "pm20020maCtrlaccessLoopEntry": pm20020maCtrlaccessLoopEntry,
       "pm20020maCtrlaccessLoopIndex": pm20020maCtrlaccessLoopIndex,
       "pm20020maCtrlaccessLoopPortn": pm20020maCtrlaccessLoopPortn,
       "pm20020maCtrlclientLoopToLineTable": pm20020maCtrlclientLoopToLineTable,
       "pm20020maCtrlclientLoopToLineEntry": pm20020maCtrlclientLoopToLineEntry,
       "pm20020maCtrlclientLoopToLineIndex": pm20020maCtrlclientLoopToLineIndex,
       "pm20020maCtrlclientLoopToLinePortn": pm20020maCtrlclientLoopToLinePortn,
       "pm20020maCtrlcsfUpInsTable": pm20020maCtrlcsfUpInsTable,
       "pm20020maCtrlcsfUpInsEntry": pm20020maCtrlcsfUpInsEntry,
       "pm20020maCtrlcsfUpInsIndex": pm20020maCtrlcsfUpInsIndex,
       "pm20020maCtrlcsfUpInsPortn": pm20020maCtrlcsfUpInsPortn,
       "pm20020maCtrlcaisDwInsTable": pm20020maCtrlcaisDwInsTable,
       "pm20020maCtrlcaisDwInsEntry": pm20020maCtrlcaisDwInsEntry,
       "pm20020maCtrlcaisDwInsIndex": pm20020maCtrlcaisDwInsIndex,
       "pm20020maCtrlcaisDwInsPortn": pm20020maCtrlcaisDwInsPortn,
       "pm20020maCtrlclientResetAllCountTable": pm20020maCtrlclientResetAllCountTable,
       "pm20020maCtrlclientResetAllCountEntry": pm20020maCtrlclientResetAllCountEntry,
       "pm20020maCtrlclientResetAllCountIndex": pm20020maCtrlclientResetAllCountIndex,
       "pm20020maCtrlclientResetAllCountsPortn": pm20020maCtrlclientResetAllCountsPortn,
       "pm20020maCtrlLine": pm20020maCtrlLine,
       "pm20020maCtrlcommAccessLoopTable": pm20020maCtrlcommAccessLoopTable,
       "pm20020maCtrlcommAccessLoopEntry": pm20020maCtrlcommAccessLoopEntry,
       "pm20020maCtrlcommAccessLoopIndex": pm20020maCtrlcommAccessLoopIndex,
       "pm20020maCtrlcommAccessLoopPortn": pm20020maCtrlcommAccessLoopPortn,
       "pm20020maCtrllineLoopTable": pm20020maCtrllineLoopTable,
       "pm20020maCtrllineLoopEntry": pm20020maCtrllineLoopEntry,
       "pm20020maCtrllineLoopIndex": pm20020maCtrllineLoopIndex,
       "pm20020maCtrllineLoopPortn": pm20020maCtrllineLoopPortn,
       "pm20020maCtrlfecDisableTable": pm20020maCtrlfecDisableTable,
       "pm20020maCtrlfecDisableEntry": pm20020maCtrlfecDisableEntry,
       "pm20020maCtrlfecDisableIndex": pm20020maCtrlfecDisableIndex,
       "pm20020maCtrlfecDisablePortn": pm20020maCtrlfecDisablePortn,
       "pm20020maCtrlmsaLineLoopTable": pm20020maCtrlmsaLineLoopTable,
       "pm20020maCtrlmsaLineLoopEntry": pm20020maCtrlmsaLineLoopEntry,
       "pm20020maCtrlmsaLineLoopIndex": pm20020maCtrlmsaLineLoopIndex,
       "pm20020maCtrlmsaLineLoopPortn": pm20020maCtrlmsaLineLoopPortn,
       "pm20020maCtrlmsaTxResetTable": pm20020maCtrlmsaTxResetTable,
       "pm20020maCtrlmsaTxResetEntry": pm20020maCtrlmsaTxResetEntry,
       "pm20020maCtrlmsaTxResetIndex": pm20020maCtrlmsaTxResetIndex,
       "pm20020maCtrlmsaTxResetPortn": pm20020maCtrlmsaTxResetPortn,
       "pm20020maCtrlmsaRxResetTable": pm20020maCtrlmsaRxResetTable,
       "pm20020maCtrlmsaRxResetEntry": pm20020maCtrlmsaRxResetEntry,
       "pm20020maCtrlmsaRxResetIndex": pm20020maCtrlmsaRxResetIndex,
       "pm20020maCtrlmsaRxResetPortn": pm20020maCtrlmsaRxResetPortn,
       "pm20020maCtrlmsaShutdownTable": pm20020maCtrlmsaShutdownTable,
       "pm20020maCtrlmsaShutdownEntry": pm20020maCtrlmsaShutdownEntry,
       "pm20020maCtrlmsaShutdownIndex": pm20020maCtrlmsaShutdownIndex,
       "pm20020maCtrlmsaShutdownPortn": pm20020maCtrlmsaShutdownPortn,
       "pm20020maCtrllineResetAllCountTable": pm20020maCtrllineResetAllCountTable,
       "pm20020maCtrllineResetAllCountEntry": pm20020maCtrllineResetAllCountEntry,
       "pm20020maCtrllineResetAllCountIndex": pm20020maCtrllineResetAllCountIndex,
       "pm20020maCtrllineResetAllCountsPortn": pm20020maCtrllineResetAllCountsPortn,
       "pm20020mari": pm20020mari,
       "pm20020mariTable": pm20020mariTable,
       "pm20020maRinvSfpTable": pm20020maRinvSfpTable,
       "pm20020maRinvSfpEntry": pm20020maRinvSfpEntry,
       "pm20020maRinvSfpIndex": pm20020maRinvSfpIndex,
       "pm20020maRinvsfp": pm20020maRinvsfp,
       "pm20020maRinvLineTable": pm20020maRinvLineTable,
       "pm20020maRinvLineEntry": pm20020maRinvLineEntry,
       "pm20020maRinvLineIndex": pm20020maRinvLineIndex,
       "pm20020maRinvxfpLine": pm20020maRinvxfpLine,
       "pm20020maRinvReloadInventory": pm20020maRinvReloadInventory,
       "pm20020maRinvHwPlatform": pm20020maRinvHwPlatform,
       "pm20020maRinvModulePlatform": pm20020maRinvModulePlatform,
       "pm20020maRinvSwPlatform": pm20020maRinvSwPlatform,
       "pm20020maRinvGwPlatform": pm20020maRinvGwPlatform,
       "pm20020madownload": pm20020madownload,
       "pm20020maDwlOther": pm20020maDwlOther,
       "pm20020maDwlrestartProcess": pm20020maDwlrestartProcess,
       "pm20020maDwlWarmRestartProcessed": pm20020maDwlWarmRestartProcessed,
       "pm20020maDwlColdRestartProcessed": pm20020maDwlColdRestartProcessed,
       "pm20020maDwlswBanksUsed": pm20020maDwlswBanksUsed,
       "pm20020maDwlSwBank1Used": pm20020maDwlSwBank1Used,
       "pm20020maDwlSwBank2Used": pm20020maDwlSwBank2Used,
       "pm20020maDwlSwBank1Notempty": pm20020maDwlSwBank1Notempty,
       "pm20020maDwlSwBank2Notempty": pm20020maDwlSwBank2Notempty,
       "pm20020maDwlgwBanksUsed": pm20020maDwlgwBanksUsed,
       "pm20020maDwlGwBank1Used": pm20020maDwlGwBank1Used,
       "pm20020maDwlGwBank2Used": pm20020maDwlGwBank2Used,
       "pm20020maDwlGwBank3Used": pm20020maDwlGwBank3Used,
       "pm20020maDwlGwBank4Used": pm20020maDwlGwBank4Used,
       "pm20020maDwlGwBank1Notempty": pm20020maDwlGwBank1Notempty,
       "pm20020maDwlGwBank2Notempty": pm20020maDwlGwBank2Notempty,
       "pm20020maDwlGwBank3Notempty": pm20020maDwlGwBank3Notempty,
       "pm20020maDwlGwBank4Notempty": pm20020maDwlGwBank4Notempty,
       "pm20020maDwlClient": pm20020maDwlClient,
       "pm20020maDwlLine": pm20020maDwlLine,
       "pm20020maConfig": pm20020maConfig,
       "pm20020maCfgAccessCAisCsf": pm20020maCfgAccessCAisCsf,
       "pm20020maCfgClientcaiscsfTable": pm20020maCfgClientcaiscsfTable,
       "pm20020maCfgClientcaiscsfEntry": pm20020maCfgClientcaiscsfEntry,
       "pm20020maCfgClientcaiscsfIndex": pm20020maCfgClientcaiscsfIndex,
       "pm20020maCfgReservePortn": pm20020maCfgReservePortn,
       "pm20020maCfgStartup": pm20020maCfgStartup,
       "pm20020maCfgClientStartupTable": pm20020maCfgClientStartupTable,
       "pm20020maCfgClientStartupEntry": pm20020maCfgClientStartupEntry,
       "pm20020maCfgClientStartupIndex": pm20020maCfgClientStartupIndex,
       "pm20020maCfgSystConfPortPortn": pm20020maCfgSystConfPortPortn,
       "pm20020maCfgNetConfPortPortn": pm20020maCfgNetConfPortPortn,
       "pm20020maCfgOptionsPortPortn": pm20020maCfgOptionsPortPortn,
       "pm20020maCfgLineStartupTable": pm20020maCfgLineStartupTable,
       "pm20020maCfgLineStartupEntry": pm20020maCfgLineStartupEntry,
       "pm20020maCfgLineStartupIndex": pm20020maCfgLineStartupIndex,
       "pm20020maCfgSystConfLinePortn": pm20020maCfgSystConfLinePortn,
       "pm20020maCfgOptionsLinePortn": pm20020maCfgOptionsLinePortn,
       "pm20020maCfgXfpTable": pm20020maCfgXfpTable,
       "pm20020maCfgXfpEntry": pm20020maCfgXfpEntry,
       "pm20020maCfgXfpIndex": pm20020maCfgXfpIndex,
       "pm20020maCfgSystConfMsaLinePortn": pm20020maCfgSystConfMsaLinePortn,
       "pm20020maCfgLabels": pm20020maCfgLabels,
       "pm20020maCfgLabelclientTable": pm20020maCfgLabelclientTable,
       "pm20020maCfgLabelclientEntry": pm20020maCfgLabelclientEntry,
       "pm20020maCfgLabelclientIndex": pm20020maCfgLabelclientIndex,
       "pm20020maCfgLabelclientPortn": pm20020maCfgLabelclientPortn,
       "pm20020maCfgLabellineTable": pm20020maCfgLabellineTable,
       "pm20020maCfgLabellineEntry": pm20020maCfgLabellineEntry,
       "pm20020maCfgLabellineIndex": pm20020maCfgLabellineIndex,
       "pm20020maCfgLabellinePortn": pm20020maCfgLabellinePortn,
       "pm20020maCfgStartuptlh": pm20020maCfgStartuptlh,
       "pm20020maCfgOtxtlhTable": pm20020maCfgOtxtlhTable,
       "pm20020maCfgOtxtlhEntry": pm20020maCfgOtxtlhEntry,
       "pm20020maCfgOtxtlhIndex": pm20020maCfgOtxtlhIndex,
       "pm20020maCfgLinePwrLaserPortn": pm20020maCfgLinePwrLaserPortn,
       "pm20020maCfgLineFCurrentPortn": pm20020maCfgLineFCurrentPortn,
       "pm20020maCfgLineGridCurrentPortn": pm20020maCfgLineGridCurrentPortn,
       "pm20020maCfgFPortn": pm20020maCfgFPortn,
       "pm20020maCfgRxLineFCurrentPortn": pm20020maCfgRxLineFCurrentPortn,
       "pm20020maCfgOther": pm20020maCfgOther,
       "pm20020matablemoduleOther": pm20020matablemoduleOther,
       "pm20020maCfgmode": pm20020maCfgmode,
       "pm20020maCfgfanLowSpeedThreshold": pm20020maCfgfanLowSpeedThreshold,
       "pm20020maCfgfanHighSpeedThreshold": pm20020maCfgfanHighSpeedThreshold,
       "pm20020maCfgStartuptablefive": pm20020maCfgStartuptablefive,
       "pm20020maCfgOtxtlhcapabilitiesTable": pm20020maCfgOtxtlhcapabilitiesTable,
       "pm20020maCfgOtxtlhcapabilitiesEntry": pm20020maCfgOtxtlhcapabilitiesEntry,
       "pm20020maCfgOtxtlhcapabilitiesIndex": pm20020maCfgOtxtlhcapabilitiesIndex,
       "pm20020maCfgComponentTypePortn": pm20020maCfgComponentTypePortn,
       "pm20020maCfgMiscellaneousPortn": pm20020maCfgMiscellaneousPortn,
       "pm20020maCfgFirstChannelPortn": pm20020maCfgFirstChannelPortn,
       "pm20020maCfgLastChannelPortn": pm20020maCfgLastChannelPortn,
       "pm20020maCfgGridPortn": pm20020maCfgGridPortn,
       "pm20020maCfgWriteConfiguration": pm20020maCfgWriteConfiguration,
       "pm20020matraps": pm20020matraps,
       "pm20020matrapPortNumber": pm20020matrapPortNumber,
       "pm20020matrapLineNumber": pm20020matrapLineNumber,
       "pm20020matrapBoardNumber": pm20020matrapBoardNumber,
       "pm20020maLineTrapNotUrgentGoesOn": pm20020maLineTrapNotUrgentGoesOn,
       "pm20020maLineTrapNotUrgentGoesOff": pm20020maLineTrapNotUrgentGoesOff,
       "pm20020maLineTrapUrgentGoesOn": pm20020maLineTrapUrgentGoesOn,
       "pm20020maLineTrapUrgentGoesOff": pm20020maLineTrapUrgentGoesOff,
       "pm20020maLineTrapCritGoesOn": pm20020maLineTrapCritGoesOn,
       "pm20020maLineTrapCritGoesOff": pm20020maLineTrapCritGoesOff,
       "pm20020maClientTrapNotUrgentGoesOn": pm20020maClientTrapNotUrgentGoesOn,
       "pm20020maClientTrapNotUrgentGoesOff": pm20020maClientTrapNotUrgentGoesOff,
       "pm20020maClientTrapUrgentGoesOn": pm20020maClientTrapUrgentGoesOn,
       "pm20020maClientTrapUrgentGoesOff": pm20020maClientTrapUrgentGoesOff,
       "pm20020maClientTrapCritGoesOn": pm20020maClientTrapCritGoesOn,
       "pm20020maClientTrapCritGoesOff": pm20020maClientTrapCritGoesOff,
       "pm20020maPowerTrapUrgentGoesOn": pm20020maPowerTrapUrgentGoesOn,
       "pm20020maPowerTrapUrgentGoesOff": pm20020maPowerTrapUrgentGoesOff,
       "pm20020maMonitoring": pm20020maMonitoring,
       "pm20020maMonOther": pm20020maMonOther,
       "pm20020maMonRmon": pm20020maMonRmon,
       "pm20020maMonClient": pm20020maMonClient,
       "pm20020maMonClientRmonCounter": pm20020maMonClientRmonCounter,
       "pm20020maMonupRmonBytesCounterClientInputTable": pm20020maMonupRmonBytesCounterClientInputTable,
       "pm20020maMonupRmonBytesCounterClientInputEntry": pm20020maMonupRmonBytesCounterClientInputEntry,
       "pm20020maMonupRmonBytesCounterClientInputIndex": pm20020maMonupRmonBytesCounterClientInputIndex,
       "pm20020maMonupRmonBytesCounterClientInputValuePortn": pm20020maMonupRmonBytesCounterClientInputValuePortn,
       "pm20020maMonupRmonBytesCounterClientInputErrorPortn": pm20020maMonupRmonBytesCounterClientInputErrorPortn,
       "pm20020maMonupRmonBytesCounterClientInputOverloadPortn": pm20020maMonupRmonBytesCounterClientInputOverloadPortn,
       "pm20020maMonupRmonCrcErrorsCounterClientInputTable": pm20020maMonupRmonCrcErrorsCounterClientInputTable,
       "pm20020maMonupRmonCrcErrorsCounterClientInputEntry": pm20020maMonupRmonCrcErrorsCounterClientInputEntry,
       "pm20020maMonupRmonCrcErrorsCounterClientInputIndex": pm20020maMonupRmonCrcErrorsCounterClientInputIndex,
       "pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn": pm20020maMonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn": pm20020maMonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn": pm20020maMonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm20020maMonupRmonPacketsCounterClientInputTable": pm20020maMonupRmonPacketsCounterClientInputTable,
       "pm20020maMonupRmonPacketsCounterClientInputEntry": pm20020maMonupRmonPacketsCounterClientInputEntry,
       "pm20020maMonupRmonPacketsCounterClientInputIndex": pm20020maMonupRmonPacketsCounterClientInputIndex,
       "pm20020maMonupRmonPacketsCounterClientInputValuePortn": pm20020maMonupRmonPacketsCounterClientInputValuePortn,
       "pm20020maMonupRmonPacketsCounterClientInputErrorPortn": pm20020maMonupRmonPacketsCounterClientInputErrorPortn,
       "pm20020maMonupRmonPacketsCounterClientInputOverloadPortn": pm20020maMonupRmonPacketsCounterClientInputOverloadPortn,
       "pm20020maMonupRmonBroadcastCounterClientInputTable": pm20020maMonupRmonBroadcastCounterClientInputTable,
       "pm20020maMonupRmonBroadcastCounterClientInputEntry": pm20020maMonupRmonBroadcastCounterClientInputEntry,
       "pm20020maMonupRmonBroadcastCounterClientInputIndex": pm20020maMonupRmonBroadcastCounterClientInputIndex,
       "pm20020maMonupRmonBroadcastCounterClientInputValuePortn": pm20020maMonupRmonBroadcastCounterClientInputValuePortn,
       "pm20020maMonupRmonBroadcastCounterClientInputErrorPortn": pm20020maMonupRmonBroadcastCounterClientInputErrorPortn,
       "pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn": pm20020maMonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm20020maMonupRmonMulticastCounterClientInputTable": pm20020maMonupRmonMulticastCounterClientInputTable,
       "pm20020maMonupRmonMulticastCounterClientInputEntry": pm20020maMonupRmonMulticastCounterClientInputEntry,
       "pm20020maMonupRmonMulticastCounterClientInputIndex": pm20020maMonupRmonMulticastCounterClientInputIndex,
       "pm20020maMonupRmonMulticastCounterClientInputValuePortn": pm20020maMonupRmonMulticastCounterClientInputValuePortn,
       "pm20020maMonupRmonMulticastCounterClientInputErrorPortn": pm20020maMonupRmonMulticastCounterClientInputErrorPortn,
       "pm20020maMonupRmonMulticastCounterClientInputOverloadPortn": pm20020maMonupRmonMulticastCounterClientInputOverloadPortn,
       "pm20020maMonupRmonPauseFrameCounterClientInputTable": pm20020maMonupRmonPauseFrameCounterClientInputTable,
       "pm20020maMonupRmonPauseFrameCounterClientInputEntry": pm20020maMonupRmonPauseFrameCounterClientInputEntry,
       "pm20020maMonupRmonPauseFrameCounterClientInputIndex": pm20020maMonupRmonPauseFrameCounterClientInputIndex,
       "pm20020maMonupRmonPauseFrameCounterClientInputValuePortn": pm20020maMonupRmonPauseFrameCounterClientInputValuePortn,
       "pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn": pm20020maMonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn": pm20020maMonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm20020maMonupRmonUnicastCounterClientInputTable": pm20020maMonupRmonUnicastCounterClientInputTable,
       "pm20020maMonupRmonUnicastCounterClientInputEntry": pm20020maMonupRmonUnicastCounterClientInputEntry,
       "pm20020maMonupRmonUnicastCounterClientInputIndex": pm20020maMonupRmonUnicastCounterClientInputIndex,
       "pm20020maMonupRmonUnicastCounterClientInputValuePortn": pm20020maMonupRmonUnicastCounterClientInputValuePortn,
       "pm20020maMonupRmonUnicastCounterClientInputErrorPortn": pm20020maMonupRmonUnicastCounterClientInputErrorPortn,
       "pm20020maMonupRmonUnicastCounterClientInputOverloadPortn": pm20020maMonupRmonUnicastCounterClientInputOverloadPortn,
       "pm20020maMonupRmonNonunicastCounterClientInputTable": pm20020maMonupRmonNonunicastCounterClientInputTable,
       "pm20020maMonupRmonNonunicastCounterClientInputEntry": pm20020maMonupRmonNonunicastCounterClientInputEntry,
       "pm20020maMonupRmonNonunicastCounterClientInputIndex": pm20020maMonupRmonNonunicastCounterClientInputIndex,
       "pm20020maMonupRmonNonunicastCounterClientInputValuePortn": pm20020maMonupRmonNonunicastCounterClientInputValuePortn,
       "pm20020maMonupRmonNonunicastCounterClientInputErrorPortn": pm20020maMonupRmonNonunicastCounterClientInputErrorPortn,
       "pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn": pm20020maMonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm20020maMondownRmonBytesCounterClientOutputTable": pm20020maMondownRmonBytesCounterClientOutputTable,
       "pm20020maMondownRmonBytesCounterClientOutputEntry": pm20020maMondownRmonBytesCounterClientOutputEntry,
       "pm20020maMondownRmonBytesCounterClientOutputIndex": pm20020maMondownRmonBytesCounterClientOutputIndex,
       "pm20020maMondownRmonBytesCounterClientOutputValuePortn": pm20020maMondownRmonBytesCounterClientOutputValuePortn,
       "pm20020maMondownRmonBytesCounterClientOutputErrorPortn": pm20020maMondownRmonBytesCounterClientOutputErrorPortn,
       "pm20020maMondownRmonBytesCounterClientOutputOverloadPortn": pm20020maMondownRmonBytesCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonCrcErrorsCounterClientOutputTable": pm20020maMondownRmonCrcErrorsCounterClientOutputTable,
       "pm20020maMondownRmonCrcErrorsCounterClientOutputEntry": pm20020maMondownRmonCrcErrorsCounterClientOutputEntry,
       "pm20020maMondownRmonCrcErrorsCounterClientOutputIndex": pm20020maMondownRmonCrcErrorsCounterClientOutputIndex,
       "pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn": pm20020maMondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn": pm20020maMondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm20020maMondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonPacketsCounterClientOutputTable": pm20020maMondownRmonPacketsCounterClientOutputTable,
       "pm20020maMondownRmonPacketsCounterClientOutputEntry": pm20020maMondownRmonPacketsCounterClientOutputEntry,
       "pm20020maMondownRmonPacketsCounterClientOutputIndex": pm20020maMondownRmonPacketsCounterClientOutputIndex,
       "pm20020maMondownRmonPacketsCounterClientOutputValuePortn": pm20020maMondownRmonPacketsCounterClientOutputValuePortn,
       "pm20020maMondownRmonPacketsCounterClientOutputErrorPortn": pm20020maMondownRmonPacketsCounterClientOutputErrorPortn,
       "pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn": pm20020maMondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonBroadcastCounterClientOutputTable": pm20020maMondownRmonBroadcastCounterClientOutputTable,
       "pm20020maMondownRmonBroadcastCounterClientOutputEntry": pm20020maMondownRmonBroadcastCounterClientOutputEntry,
       "pm20020maMondownRmonBroadcastCounterClientOutputIndex": pm20020maMondownRmonBroadcastCounterClientOutputIndex,
       "pm20020maMondownRmonBroadcastCounterClientOutputValuePortn": pm20020maMondownRmonBroadcastCounterClientOutputValuePortn,
       "pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn": pm20020maMondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn": pm20020maMondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonMulticastCounterClientOutputTable": pm20020maMondownRmonMulticastCounterClientOutputTable,
       "pm20020maMondownRmonMulticastCounterClientOutputEntry": pm20020maMondownRmonMulticastCounterClientOutputEntry,
       "pm20020maMondownRmonMulticastCounterClientOutputIndex": pm20020maMondownRmonMulticastCounterClientOutputIndex,
       "pm20020maMondownRmonMulticastCounterClientOutputValuePortn": pm20020maMondownRmonMulticastCounterClientOutputValuePortn,
       "pm20020maMondownRmonMulticastCounterClientOutputErrorPortn": pm20020maMondownRmonMulticastCounterClientOutputErrorPortn,
       "pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn": pm20020maMondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonPauseFrameCounterClientOutputTable": pm20020maMondownRmonPauseFrameCounterClientOutputTable,
       "pm20020maMondownRmonPauseFrameCounterClientOutputEntry": pm20020maMondownRmonPauseFrameCounterClientOutputEntry,
       "pm20020maMondownRmonPauseFrameCounterClientOutputIndex": pm20020maMondownRmonPauseFrameCounterClientOutputIndex,
       "pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn": pm20020maMondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn": pm20020maMondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn": pm20020maMondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonUnicastCounterClientOutputTable": pm20020maMondownRmonUnicastCounterClientOutputTable,
       "pm20020maMondownRmonUnicastCounterClientOutputEntry": pm20020maMondownRmonUnicastCounterClientOutputEntry,
       "pm20020maMondownRmonUnicastCounterClientOutputIndex": pm20020maMondownRmonUnicastCounterClientOutputIndex,
       "pm20020maMondownRmonUnicastCounterClientOutputValuePortn": pm20020maMondownRmonUnicastCounterClientOutputValuePortn,
       "pm20020maMondownRmonUnicastCounterClientOutputErrorPortn": pm20020maMondownRmonUnicastCounterClientOutputErrorPortn,
       "pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn": pm20020maMondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm20020maMondownRmonNonunicastCounterClientOutputTable": pm20020maMondownRmonNonunicastCounterClientOutputTable,
       "pm20020maMondownRmonNonunicastCounterClientOutputEntry": pm20020maMondownRmonNonunicastCounterClientOutputEntry,
       "pm20020maMondownRmonNonunicastCounterClientOutputIndex": pm20020maMondownRmonNonunicastCounterClientOutputIndex,
       "pm20020maMondownRmonNonunicastCounterClientOutputValuePortn": pm20020maMondownRmonNonunicastCounterClientOutputValuePortn,
       "pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn": pm20020maMondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn": pm20020maMondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm20020maMonPerfOther": pm20020maMonPerfOther,
       "pm20020maMonPerfSync": pm20020maMonPerfSync,
       "pm20020maPerfEnable": pm20020maPerfEnable,
       "pm20020maPerf15minSync": pm20020maPerf15minSync,
       "pm20020maPerf24hSync": pm20020maPerf24hSync,
       "pm20020maMonPerfTimeStamp": pm20020maMonPerfTimeStamp,
       "pm20020maPerf15MinShort": pm20020maPerf15MinShort,
       "pm20020maPerf15MinLong": pm20020maPerf15MinLong,
       "pm20020maPerf24HoursShort": pm20020maPerf24HoursShort,
       "pm20020maPerf24HoursLong": pm20020maPerf24HoursLong,
       "pm20020maPerfCurrent15MinElapsedTime": pm20020maPerfCurrent15MinElapsedTime,
       "pm20020maPerfCurrent24HoursElapsedTime": pm20020maPerfCurrent24HoursElapsedTime,
       "pm20020maMonPerfClient": pm20020maMonPerfClient,
       "pm20020maPerfTelecomInputClientCurrent15StatTable": pm20020maPerfTelecomInputClientCurrent15StatTable,
       "pm20020maPerfTelecomInputClientCurrent15StatEntry": pm20020maPerfTelecomInputClientCurrent15StatEntry,
       "pm20020maPerfTelecomInputClientCurrent15StatIndex": pm20020maPerfTelecomInputClientCurrent15StatIndex,
       "pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn": pm20020maPerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn": pm20020maPerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn": pm20020maPerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn": pm20020maPerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn": pm20020maPerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn": pm20020maPerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn": pm20020maPerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn": pm20020maPerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn": pm20020maPerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn": pm20020maPerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm20020maPerfTelecomInputClientPast15StatHistoryPort1Table": pm20020maPerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry": pm20020maPerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index": pm20020maPerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1": pm20020maPerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1": pm20020maPerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1": pm20020maPerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1": pm20020maPerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1": pm20020maPerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1": pm20020maPerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm20020maPerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1": pm20020maPerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1": pm20020maPerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1": pm20020maPerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm20020maPerfTelecomInputClientCurrent24StatTable": pm20020maPerfTelecomInputClientCurrent24StatTable,
       "pm20020maPerfTelecomInputClientCurrent24StatEntry": pm20020maPerfTelecomInputClientCurrent24StatEntry,
       "pm20020maPerfTelecomInputClientCurrent24StatIndex": pm20020maPerfTelecomInputClientCurrent24StatIndex,
       "pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn": pm20020maPerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn": pm20020maPerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn": pm20020maPerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn": pm20020maPerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn": pm20020maPerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn": pm20020maPerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn": pm20020maPerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn": pm20020maPerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn": pm20020maPerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn": pm20020maPerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm20020maPerfTelecomInputClientPast24StatHistoryPort1Table": pm20020maPerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry": pm20020maPerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index": pm20020maPerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1": pm20020maPerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1": pm20020maPerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1": pm20020maPerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1": pm20020maPerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1": pm20020maPerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1": pm20020maPerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm20020maPerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1": pm20020maPerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1": pm20020maPerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1": pm20020maPerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm20020maPerfTelecomOutputClientCurrent15StatTable": pm20020maPerfTelecomOutputClientCurrent15StatTable,
       "pm20020maPerfTelecomOutputClientCurrent15StatEntry": pm20020maPerfTelecomOutputClientCurrent15StatEntry,
       "pm20020maPerfTelecomOutputClientCurrent15StatIndex": pm20020maPerfTelecomOutputClientCurrent15StatIndex,
       "pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn": pm20020maPerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn": pm20020maPerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn": pm20020maPerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn": pm20020maPerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn": pm20020maPerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn": pm20020maPerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn": pm20020maPerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn": pm20020maPerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn": pm20020maPerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn": pm20020maPerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Table": pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry": pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index": pm20020maPerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm20020maPerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm20020maPerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm20020maPerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm20020maPerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm20020maPerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1": pm20020maPerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm20020maPerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm20020maPerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm20020maPerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm20020maPerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm20020maPerfTelecomOutputClientCurrent24StatTable": pm20020maPerfTelecomOutputClientCurrent24StatTable,
       "pm20020maPerfTelecomOutputClientCurrent24StatEntry": pm20020maPerfTelecomOutputClientCurrent24StatEntry,
       "pm20020maPerfTelecomOutputClientCurrent24StatIndex": pm20020maPerfTelecomOutputClientCurrent24StatIndex,
       "pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn": pm20020maPerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn": pm20020maPerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn": pm20020maPerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn": pm20020maPerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn": pm20020maPerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn": pm20020maPerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn": pm20020maPerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn": pm20020maPerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn": pm20020maPerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn": pm20020maPerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Table": pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry": pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index": pm20020maPerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm20020maPerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm20020maPerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm20020maPerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm20020maPerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm20020maPerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1": pm20020maPerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm20020maPerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm20020maPerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm20020maPerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm20020maPerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm20020maPerfDatacomClientCurrent15StatTable": pm20020maPerfDatacomClientCurrent15StatTable,
       "pm20020maPerfDatacomClientCurrent15StatEntry": pm20020maPerfDatacomClientCurrent15StatEntry,
       "pm20020maPerfDatacomClientCurrent15StatIndex": pm20020maPerfDatacomClientCurrent15StatIndex,
       "pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn": pm20020maperfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pm20020maperfdatacomclientCurrent15StatInCrcCountPortn": pm20020maperfdatacomclientCurrent15StatInCrcCountPortn,
       "pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn": pm20020maperfdatacomclientCurrent15StatInPacketCountInvPortn,
       "pm20020maperfdatacomclientCurrent15StatInPacketCountPortn": pm20020maperfdatacomclientCurrent15StatInPacketCountPortn,
       "pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn": pm20020maperfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn": pm20020maperfdatacomclientCurrent15StatOutCrcCountPortn,
       "pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn": pm20020maperfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn": pm20020maperfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm20020maPerfDatacomClientPast15StatHistoryPort1Table": pm20020maPerfDatacomClientPast15StatHistoryPort1Table,
       "pm20020maPerfDatacomClientPast15StatHistoryPort1Entry": pm20020maPerfDatacomClientPast15StatHistoryPort1Entry,
       "pm20020maPerfDatacomClientPast15StatHistoryPort1Index": pm20020maPerfDatacomClientPast15StatHistoryPort1Index,
       "pm20020maperfdatacomclientPast15StatInCrcCountInvPort1": pm20020maperfdatacomclientPast15StatInCrcCountInvPort1,
       "pm20020maperfdatacomclientPast15StatInCrcCountPort1": pm20020maperfdatacomclientPast15StatInCrcCountPort1,
       "pm20020maperfdatacomclientPast15StatInPacketCountInvPort1": pm20020maperfdatacomclientPast15StatInPacketCountInvPort1,
       "pm20020maperfdatacomclientPast15StatInPacketCountPort1": pm20020maperfdatacomclientPast15StatInPacketCountPort1,
       "pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1": pm20020maperfdatacomclientPast15StatOutCrcCountInvPort1,
       "pm20020maperfdatacomclientPast15StatOutCrcCountPort1": pm20020maperfdatacomclientPast15StatOutCrcCountPort1,
       "pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1": pm20020maperfdatacomclientPast15StatOutPacketCountInvPort1,
       "pm20020maperfdatacomclientPast15StatOutPacketCountPort1": pm20020maperfdatacomclientPast15StatOutPacketCountPort1,
       "pm20020maPerfDatacomClientCurrent24StatTable": pm20020maPerfDatacomClientCurrent24StatTable,
       "pm20020maPerfDatacomClientCurrent24StatEntry": pm20020maPerfDatacomClientCurrent24StatEntry,
       "pm20020maPerfDatacomClientCurrent24StatIndex": pm20020maPerfDatacomClientCurrent24StatIndex,
       "pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn": pm20020maperfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pm20020maperfdatacomclientCurrent24StatInCrcCountPortn": pm20020maperfdatacomclientCurrent24StatInCrcCountPortn,
       "pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn": pm20020maperfdatacomclientCurrent24StatInPacketCountInvPortn,
       "pm20020maperfdatacomclientCurrent24StatInPacketCountPortn": pm20020maperfdatacomclientCurrent24StatInPacketCountPortn,
       "pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn": pm20020maperfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn": pm20020maperfdatacomclientCurrent24StatOutCrcCountPortn,
       "pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn": pm20020maperfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn": pm20020maperfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm20020maPerfDatacomClientPast24StatHistoryPort1Table": pm20020maPerfDatacomClientPast24StatHistoryPort1Table,
       "pm20020maPerfDatacomClientPast24StatHistoryPort1Entry": pm20020maPerfDatacomClientPast24StatHistoryPort1Entry,
       "pm20020maPerfDatacomClientPast24StatHistoryPort1Index": pm20020maPerfDatacomClientPast24StatHistoryPort1Index,
       "pm20020maperfdatacomclientPast24StatInCrcCountInvPort1": pm20020maperfdatacomclientPast24StatInCrcCountInvPort1,
       "pm20020maperfdatacomclientPast24StatInCrcCountPort1": pm20020maperfdatacomclientPast24StatInCrcCountPort1,
       "pm20020maperfdatacomclientPast24StatInPacketCountInvPort1": pm20020maperfdatacomclientPast24StatInPacketCountInvPort1,
       "pm20020maperfdatacomclientPast24StatInPacketCountPort1": pm20020maperfdatacomclientPast24StatInPacketCountPort1,
       "pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1": pm20020maperfdatacomclientPast24StatOutCrcCountInvPort1,
       "pm20020maperfdatacomclientPast24StatOutCrcCountPort1": pm20020maperfdatacomclientPast24StatOutCrcCountPort1,
       "pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1": pm20020maperfdatacomclientPast24StatOutPacketCountInvPort1,
       "pm20020maperfdatacomclientPast24StatOutPacketCountPort1": pm20020maperfdatacomclientPast24StatOutPacketCountPort1,
       "pm20020maMonPerfLine": pm20020maMonPerfLine,
       "pm20020maPerfTelecomLinePostFecCurrent15StatTable": pm20020maPerfTelecomLinePostFecCurrent15StatTable,
       "pm20020maPerfTelecomLinePostFecCurrent15StatEntry": pm20020maPerfTelecomLinePostFecCurrent15StatEntry,
       "pm20020maPerfTelecomLinePostFecCurrent15StatIndex": pm20020maPerfTelecomLinePostFecCurrent15StatIndex,
       "pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn": pm20020maPerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn": pm20020maPerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn": pm20020maPerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn": pm20020maPerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn": pm20020maPerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn": pm20020maPerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm20020maPerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm20020maPerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn": pm20020maPerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn": pm20020maPerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Table": pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index": pm20020maPerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm20020maPerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm20020maPerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm20020maPerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm20020maPerfTelecomLinePostFecCurrent24StatTable": pm20020maPerfTelecomLinePostFecCurrent24StatTable,
       "pm20020maPerfTelecomLinePostFecCurrent24StatEntry": pm20020maPerfTelecomLinePostFecCurrent24StatEntry,
       "pm20020maPerfTelecomLinePostFecCurrent24StatIndex": pm20020maPerfTelecomLinePostFecCurrent24StatIndex,
       "pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn": pm20020maPerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn": pm20020maPerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn": pm20020maPerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn": pm20020maPerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn": pm20020maPerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn": pm20020maPerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm20020maPerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm20020maPerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn": pm20020maPerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn": pm20020maPerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Table": pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index": pm20020maPerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm20020maPerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm20020maPerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm20020maPerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatTable": pm20020maPerfTelecomBerLinePreFecCurrent15StatTable,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry": pm20020maPerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex": pm20020maPerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm20020maPerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm20020maPerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm20020maPerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm20020maPerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm20020maPerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm20020maPerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatTable": pm20020maPerfTelecomBerLinePreFecCurrent24StatTable,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry": pm20020maPerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex": pm20020maPerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm20020maPerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm20020maPerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm20020maPerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm20020maPerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm20020maPerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm20020maPerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
