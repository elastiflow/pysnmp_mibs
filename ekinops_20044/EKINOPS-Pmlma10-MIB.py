# SNMP MIB module (EKINOPS-Pmlma10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pmlma10-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
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

modulePmlma10 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68)
)
if mibBuilder.loadTexts:
    modulePmlma10.setRevisions(
        ("2014-10-09 00:00",
         "2015-01-27 00:00",
         "2015-10-21 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmlma10MultiRate(TextualConvention, Integer32):
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



class Pmlma10OtxMode(TextualConvention, Integer32):
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



class Pmlma10OtxGrid(TextualConvention, Integer32):
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



class Pmlma10AdjustValue(TextualConvention, Integer32):
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



class Pmlma10ClientProtocol(TextualConvention, Integer32):
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



class Pmlma10ProtocolMode(TextualConvention, Integer32):
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



class Pmlma10OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pmlma10OrxChannel(TextualConvention, Integer32):
    status = "current"


class Pmlma10ClientIgnoreTimer(TextualConvention, Integer32):
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



class Pmlma10DccMode(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_Pmlma10alarms_ObjectIdentity = ObjectIdentity
pmlma10alarms = _Pmlma10alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2)
)
_Pmlma10AlmOther_ObjectIdentity = ObjectIdentity
pmlma10AlmOther = _Pmlma10AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1)
)
_Pmlma10AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmlma10AlmOtherNurg = _Pmlma10AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 1)
)
_Pmlma10AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmlma10AlmsynthAlm2 = _Pmlma10AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 1, 2)
)
_Pmlma10AlmConfTableSave_Type = EkiOnOff
_Pmlma10AlmConfTableSave_Object = MibScalar
pmlma10AlmConfTableSave = _Pmlma10AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 1, 2, 1),
    _Pmlma10AlmConfTableSave_Type()
)
pmlma10AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmConfTableSave.setStatus("current")
_Pmlma10AlmInvUpload_Type = EkiOnOff
_Pmlma10AlmInvUpload_Object = MibScalar
pmlma10AlmInvUpload = _Pmlma10AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 1, 2, 2),
    _Pmlma10AlmInvUpload_Type()
)
pmlma10AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmInvUpload.setStatus("current")
_Pmlma10AlmConfTableLoad_Type = EkiOnOff
_Pmlma10AlmConfTableLoad_Object = MibScalar
pmlma10AlmConfTableLoad = _Pmlma10AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 1, 2, 3),
    _Pmlma10AlmConfTableLoad_Type()
)
pmlma10AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmConfTableLoad.setStatus("current")
_Pmlma10AlmCorrelatOff_Type = EkiOnOff
_Pmlma10AlmCorrelatOff_Object = MibScalar
pmlma10AlmCorrelatOff = _Pmlma10AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 1, 2, 4),
    _Pmlma10AlmCorrelatOff_Type()
)
pmlma10AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmCorrelatOff.setStatus("current")
_Pmlma10AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmlma10AlmOtherUrg = _Pmlma10AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 2)
)
_Pmlma10AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmlma10AlmOtherCrit = _Pmlma10AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 3)
)
_Pmlma10AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmlma10AlmsynthAlm0 = _Pmlma10AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 3, 0)
)
_Pmlma10AlmModGlobFail_Type = EkiOnOff
_Pmlma10AlmModGlobFail_Object = MibScalar
pmlma10AlmModGlobFail = _Pmlma10AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 3, 0, 9),
    _Pmlma10AlmModGlobFail_Type()
)
pmlma10AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmModGlobFail.setStatus("current")
_Pmlma10AlmDefFuseA_Type = EkiOnOff
_Pmlma10AlmDefFuseA_Object = MibScalar
pmlma10AlmDefFuseA = _Pmlma10AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 3, 0, 15),
    _Pmlma10AlmDefFuseA_Type()
)
pmlma10AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmDefFuseA.setStatus("current")
_Pmlma10AlmDefFuseB_Type = EkiOnOff
_Pmlma10AlmDefFuseB_Object = MibScalar
pmlma10AlmDefFuseB = _Pmlma10AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 1, 3, 0, 16),
    _Pmlma10AlmDefFuseB_Type()
)
pmlma10AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmDefFuseB.setStatus("current")
_Pmlma10AlmClient_ObjectIdentity = ObjectIdentity
pmlma10AlmClient = _Pmlma10AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2)
)
_Pmlma10AlmClientNurg_ObjectIdentity = ObjectIdentity
pmlma10AlmClientNurg = _Pmlma10AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1)
)
_Pmlma10AlmclientSfpWarnDdmTable_Object = MibTable
pmlma10AlmclientSfpWarnDdmTable = _Pmlma10AlmclientSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232)
)
if mibBuilder.loadTexts:
    pmlma10AlmclientSfpWarnDdmTable.setStatus("current")
_Pmlma10AlmclientSfpWarnDdmEntry_Object = MibTableRow
pmlma10AlmclientSfpWarnDdmEntry = _Pmlma10AlmclientSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1)
)
pmlma10AlmclientSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmclientSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pmlma10AlmclientSfpWarnDdmEntry.setStatus("current")


class _Pmlma10AlmclientSfpWarnDdmIndex_Type(Integer32):
    """Custom type pmlma10AlmclientSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmclientSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pmlma10AlmclientSfpWarnDdmIndex_Object = MibTableColumn
pmlma10AlmclientSfpWarnDdmIndex = _Pmlma10AlmclientSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 1),
    _Pmlma10AlmclientSfpWarnDdmIndex_Type()
)
pmlma10AlmclientSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmclientSfpWarnDdmIndex.setStatus("current")
_Pmlma10AlmClientTxPwLowWngPortn_Type = EkiOnOff
_Pmlma10AlmClientTxPwLowWngPortn_Object = MibTableColumn
pmlma10AlmClientTxPwLowWngPortn = _Pmlma10AlmClientTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 2),
    _Pmlma10AlmClientTxPwLowWngPortn_Type()
)
pmlma10AlmClientTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxPwLowWngPortn.setStatus("current")
_Pmlma10AlmClientTxPwrHighWngPortn_Type = EkiOnOff
_Pmlma10AlmClientTxPwrHighWngPortn_Object = MibTableColumn
pmlma10AlmClientTxPwrHighWngPortn = _Pmlma10AlmClientTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 3),
    _Pmlma10AlmClientTxPwrHighWngPortn_Type()
)
pmlma10AlmClientTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxPwrHighWngPortn.setStatus("current")
_Pmlma10AlmClientTxBiasLowWngPortn_Type = EkiOnOff
_Pmlma10AlmClientTxBiasLowWngPortn_Object = MibTableColumn
pmlma10AlmClientTxBiasLowWngPortn = _Pmlma10AlmClientTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 4),
    _Pmlma10AlmClientTxBiasLowWngPortn_Type()
)
pmlma10AlmClientTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxBiasLowWngPortn.setStatus("current")
_Pmlma10AlmClientTxBiasHighWngPortn_Type = EkiOnOff
_Pmlma10AlmClientTxBiasHighWngPortn_Object = MibTableColumn
pmlma10AlmClientTxBiasHighWngPortn = _Pmlma10AlmClientTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 5),
    _Pmlma10AlmClientTxBiasHighWngPortn_Type()
)
pmlma10AlmClientTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxBiasHighWngPortn.setStatus("current")
_Pmlma10AlmClientVccLowWngPortn_Type = EkiOnOff
_Pmlma10AlmClientVccLowWngPortn_Object = MibTableColumn
pmlma10AlmClientVccLowWngPortn = _Pmlma10AlmClientVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 6),
    _Pmlma10AlmClientVccLowWngPortn_Type()
)
pmlma10AlmClientVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientVccLowWngPortn.setStatus("current")
_Pmlma10AlmClientVccHighWngPortn_Type = EkiOnOff
_Pmlma10AlmClientVccHighWngPortn_Object = MibTableColumn
pmlma10AlmClientVccHighWngPortn = _Pmlma10AlmClientVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 7),
    _Pmlma10AlmClientVccHighWngPortn_Type()
)
pmlma10AlmClientVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientVccHighWngPortn.setStatus("current")
_Pmlma10AlmClientTempLowWngPortn_Type = EkiOnOff
_Pmlma10AlmClientTempLowWngPortn_Object = MibTableColumn
pmlma10AlmClientTempLowWngPortn = _Pmlma10AlmClientTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 8),
    _Pmlma10AlmClientTempLowWngPortn_Type()
)
pmlma10AlmClientTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTempLowWngPortn.setStatus("current")
_Pmlma10AlmClientTempHighWngPortn_Type = EkiOnOff
_Pmlma10AlmClientTempHighWngPortn_Object = MibTableColumn
pmlma10AlmClientTempHighWngPortn = _Pmlma10AlmClientTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 9),
    _Pmlma10AlmClientTempHighWngPortn_Type()
)
pmlma10AlmClientTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTempHighWngPortn.setStatus("current")
_Pmlma10AlmClientRxPwrLowWngPortn_Type = EkiOnOff
_Pmlma10AlmClientRxPwrLowWngPortn_Object = MibTableColumn
pmlma10AlmClientRxPwrLowWngPortn = _Pmlma10AlmClientRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 16),
    _Pmlma10AlmClientRxPwrLowWngPortn_Type()
)
pmlma10AlmClientRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientRxPwrLowWngPortn.setStatus("current")
_Pmlma10AlmClientRxPwrHighWngPortn_Type = EkiOnOff
_Pmlma10AlmClientRxPwrHighWngPortn_Object = MibTableColumn
pmlma10AlmClientRxPwrHighWngPortn = _Pmlma10AlmClientRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 1, 232, 1, 17),
    _Pmlma10AlmClientRxPwrHighWngPortn_Type()
)
pmlma10AlmClientRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientRxPwrHighWngPortn.setStatus("current")
_Pmlma10AlmClientUrg_ObjectIdentity = ObjectIdentity
pmlma10AlmClientUrg = _Pmlma10AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2)
)
_Pmlma10AlmclientHostLaneFaultTable_Object = MibTable
pmlma10AlmclientHostLaneFaultTable = _Pmlma10AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88)
)
if mibBuilder.loadTexts:
    pmlma10AlmclientHostLaneFaultTable.setStatus("current")
_Pmlma10AlmclientHostLaneFaultEntry_Object = MibTableRow
pmlma10AlmclientHostLaneFaultEntry = _Pmlma10AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88, 1)
)
pmlma10AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pmlma10AlmclientHostLaneFaultEntry.setStatus("current")


class _Pmlma10AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pmlma10AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pmlma10AlmclientHostLaneFaultIndex_Object = MibTableColumn
pmlma10AlmclientHostLaneFaultIndex = _Pmlma10AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88, 1, 1),
    _Pmlma10AlmclientHostLaneFaultIndex_Type()
)
pmlma10AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmclientHostLaneFaultIndex.setStatus("current")
_Pmlma10AlmClientLossOfSyncPortn_Type = EkiOnOff
_Pmlma10AlmClientLossOfSyncPortn_Object = MibTableColumn
pmlma10AlmClientLossOfSyncPortn = _Pmlma10AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88, 1, 2),
    _Pmlma10AlmClientLossOfSyncPortn_Type()
)
pmlma10AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientLossOfSyncPortn.setStatus("current")
_Pmlma10AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pmlma10AlmClientInputLossOfSigPortn_Object = MibTableColumn
pmlma10AlmClientInputLossOfSigPortn = _Pmlma10AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88, 1, 3),
    _Pmlma10AlmClientInputLossOfSigPortn_Type()
)
pmlma10AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientInputLossOfSigPortn.setStatus("current")
_Pmlma10AlmClientCsfDetectedPortn_Type = EkiOnOff
_Pmlma10AlmClientCsfDetectedPortn_Object = MibTableColumn
pmlma10AlmClientCsfDetectedPortn = _Pmlma10AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88, 1, 7),
    _Pmlma10AlmClientCsfDetectedPortn_Type()
)
pmlma10AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientCsfDetectedPortn.setStatus("current")
_Pmlma10AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pmlma10AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pmlma10AlmClientLaneTxFifoErrorPortn = _Pmlma10AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 88, 1, 11),
    _Pmlma10AlmClientLaneTxFifoErrorPortn_Type()
)
pmlma10AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pmlma10AlmclientSfpAlmDdmTable_Object = MibTable
pmlma10AlmclientSfpAlmDdmTable = _Pmlma10AlmclientSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216)
)
if mibBuilder.loadTexts:
    pmlma10AlmclientSfpAlmDdmTable.setStatus("current")
_Pmlma10AlmclientSfpAlmDdmEntry_Object = MibTableRow
pmlma10AlmclientSfpAlmDdmEntry = _Pmlma10AlmclientSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1)
)
pmlma10AlmclientSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmclientSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pmlma10AlmclientSfpAlmDdmEntry.setStatus("current")


class _Pmlma10AlmclientSfpAlmDdmIndex_Type(Integer32):
    """Custom type pmlma10AlmclientSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmclientSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pmlma10AlmclientSfpAlmDdmIndex_Object = MibTableColumn
pmlma10AlmclientSfpAlmDdmIndex = _Pmlma10AlmclientSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 1),
    _Pmlma10AlmclientSfpAlmDdmIndex_Type()
)
pmlma10AlmclientSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmclientSfpAlmDdmIndex.setStatus("current")
_Pmlma10AlmClientTxPwrLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientTxPwrLowAlaPortn_Object = MibTableColumn
pmlma10AlmClientTxPwrLowAlaPortn = _Pmlma10AlmClientTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 2),
    _Pmlma10AlmClientTxPwrLowAlaPortn_Type()
)
pmlma10AlmClientTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxPwrLowAlaPortn.setStatus("current")
_Pmlma10AlmClientTxPwrHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientTxPwrHighAlaPortn_Object = MibTableColumn
pmlma10AlmClientTxPwrHighAlaPortn = _Pmlma10AlmClientTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 3),
    _Pmlma10AlmClientTxPwrHighAlaPortn_Type()
)
pmlma10AlmClientTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxPwrHighAlaPortn.setStatus("current")
_Pmlma10AlmClientTxBiasLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientTxBiasLowAlaPortn_Object = MibTableColumn
pmlma10AlmClientTxBiasLowAlaPortn = _Pmlma10AlmClientTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 4),
    _Pmlma10AlmClientTxBiasLowAlaPortn_Type()
)
pmlma10AlmClientTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxBiasLowAlaPortn.setStatus("current")
_Pmlma10AlmClientTxBiasHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientTxBiasHighAlaPortn_Object = MibTableColumn
pmlma10AlmClientTxBiasHighAlaPortn = _Pmlma10AlmClientTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 5),
    _Pmlma10AlmClientTxBiasHighAlaPortn_Type()
)
pmlma10AlmClientTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTxBiasHighAlaPortn.setStatus("current")
_Pmlma10AlmClientVccLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientVccLowAlaPortn_Object = MibTableColumn
pmlma10AlmClientVccLowAlaPortn = _Pmlma10AlmClientVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 6),
    _Pmlma10AlmClientVccLowAlaPortn_Type()
)
pmlma10AlmClientVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientVccLowAlaPortn.setStatus("current")
_Pmlma10AlmClientVccHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientVccHighAlaPortn_Object = MibTableColumn
pmlma10AlmClientVccHighAlaPortn = _Pmlma10AlmClientVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 7),
    _Pmlma10AlmClientVccHighAlaPortn_Type()
)
pmlma10AlmClientVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientVccHighAlaPortn.setStatus("current")
_Pmlma10AlmClientTempLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientTempLowAlaPortn_Object = MibTableColumn
pmlma10AlmClientTempLowAlaPortn = _Pmlma10AlmClientTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 8),
    _Pmlma10AlmClientTempLowAlaPortn_Type()
)
pmlma10AlmClientTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTempLowAlaPortn.setStatus("current")
_Pmlma10AlmClientTempHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientTempHighAlaPortn_Object = MibTableColumn
pmlma10AlmClientTempHighAlaPortn = _Pmlma10AlmClientTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 9),
    _Pmlma10AlmClientTempHighAlaPortn_Type()
)
pmlma10AlmClientTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientTempHighAlaPortn.setStatus("current")
_Pmlma10AlmClientRxPwrLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientRxPwrLowAlaPortn_Object = MibTableColumn
pmlma10AlmClientRxPwrLowAlaPortn = _Pmlma10AlmClientRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 16),
    _Pmlma10AlmClientRxPwrLowAlaPortn_Type()
)
pmlma10AlmClientRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientRxPwrLowAlaPortn.setStatus("current")
_Pmlma10AlmClientRxPwrHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmClientRxPwrHighAlaPortn_Object = MibTableColumn
pmlma10AlmClientRxPwrHighAlaPortn = _Pmlma10AlmClientRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 2, 216, 1, 17),
    _Pmlma10AlmClientRxPwrHighAlaPortn_Type()
)
pmlma10AlmClientRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientRxPwrHighAlaPortn.setStatus("current")
_Pmlma10AlmClientCrit_ObjectIdentity = ObjectIdentity
pmlma10AlmClientCrit = _Pmlma10AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3)
)
_Pmlma10AlmsynthAlmPortTable_Object = MibTable
pmlma10AlmsynthAlmPortTable = _Pmlma10AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmlma10AlmsynthAlmPortTable.setStatus("current")
_Pmlma10AlmsynthAlmPortEntry_Object = MibTableRow
pmlma10AlmsynthAlmPortEntry = _Pmlma10AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1)
)
pmlma10AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmlma10AlmsynthAlmPortEntry.setStatus("current")


class _Pmlma10AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmlma10AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmlma10AlmsynthAlmPortIndex_Object = MibTableColumn
pmlma10AlmsynthAlmPortIndex = _Pmlma10AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 1),
    _Pmlma10AlmsynthAlmPortIndex_Type()
)
pmlma10AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmsynthAlmPortIndex.setStatus("current")
_Pmlma10AlmSfpAbsentPortn_Type = EkiOnOff
_Pmlma10AlmSfpAbsentPortn_Object = MibTableColumn
pmlma10AlmSfpAbsentPortn = _Pmlma10AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 2),
    _Pmlma10AlmSfpAbsentPortn_Type()
)
pmlma10AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmSfpAbsentPortn.setStatus("current")
_Pmlma10AlmDdmAbsentPortn_Type = EkiOnOff
_Pmlma10AlmDdmAbsentPortn_Object = MibTableColumn
pmlma10AlmDdmAbsentPortn = _Pmlma10AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 3),
    _Pmlma10AlmDdmAbsentPortn_Type()
)
pmlma10AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmDdmAbsentPortn.setStatus("current")
_Pmlma10AlmHwFailAccPortn_Type = EkiOnOff
_Pmlma10AlmHwFailAccPortn_Object = MibTableColumn
pmlma10AlmHwFailAccPortn = _Pmlma10AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 5),
    _Pmlma10AlmHwFailAccPortn_Type()
)
pmlma10AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmHwFailAccPortn.setStatus("current")
_Pmlma10AlmDwLsdPortn_Type = EkiOnOff
_Pmlma10AlmDwLsdPortn_Object = MibTableColumn
pmlma10AlmDwLsdPortn = _Pmlma10AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 6),
    _Pmlma10AlmDwLsdPortn_Type()
)
pmlma10AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmDwLsdPortn.setStatus("current")
_Pmlma10AlmClientLocalOosPortn_Type = EkiOnOff
_Pmlma10AlmClientLocalOosPortn_Object = MibTableColumn
pmlma10AlmClientLocalOosPortn = _Pmlma10AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 7),
    _Pmlma10AlmClientLocalOosPortn_Type()
)
pmlma10AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientLocalOosPortn.setStatus("current")
_Pmlma10AlmClientRemoteOosPortn_Type = EkiOnOff
_Pmlma10AlmClientRemoteOosPortn_Object = MibTableColumn
pmlma10AlmClientRemoteOosPortn = _Pmlma10AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 8),
    _Pmlma10AlmClientRemoteOosPortn_Type()
)
pmlma10AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmClientRemoteOosPortn.setStatus("current")
_Pmlma10AlmDwCaisPortn_Type = EkiOnOff
_Pmlma10AlmDwCaisPortn_Object = MibTableColumn
pmlma10AlmDwCaisPortn = _Pmlma10AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 9),
    _Pmlma10AlmDwCaisPortn_Type()
)
pmlma10AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmDwCaisPortn.setStatus("current")
_Pmlma10AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pmlma10AlmSfpDdmWarningPortn_Object = MibTableColumn
pmlma10AlmSfpDdmWarningPortn = _Pmlma10AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 10),
    _Pmlma10AlmSfpDdmWarningPortn_Type()
)
pmlma10AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmSfpDdmWarningPortn.setStatus("current")
_Pmlma10AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pmlma10AlmSfpDdmAlmPortn_Object = MibTableColumn
pmlma10AlmSfpDdmAlmPortn = _Pmlma10AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 11),
    _Pmlma10AlmSfpDdmAlmPortn_Type()
)
pmlma10AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmSfpDdmAlmPortn.setStatus("current")
_Pmlma10AlmFailAccPortn_Type = EkiOnOff
_Pmlma10AlmFailAccPortn_Object = MibTableColumn
pmlma10AlmFailAccPortn = _Pmlma10AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 13),
    _Pmlma10AlmFailAccPortn_Type()
)
pmlma10AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmFailAccPortn.setStatus("current")
_Pmlma10AlmUpCsfPortn_Type = EkiOnOff
_Pmlma10AlmUpCsfPortn_Object = MibTableColumn
pmlma10AlmUpCsfPortn = _Pmlma10AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 2, 3, 8, 1, 17),
    _Pmlma10AlmUpCsfPortn_Type()
)
pmlma10AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmUpCsfPortn.setStatus("current")
_Pmlma10AlmLine_ObjectIdentity = ObjectIdentity
pmlma10AlmLine = _Pmlma10AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3)
)
_Pmlma10AlmLineNurg_ObjectIdentity = ObjectIdentity
pmlma10AlmLineNurg = _Pmlma10AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 1)
)
_Pmlma10AlmLineUrg_ObjectIdentity = ObjectIdentity
pmlma10AlmLineUrg = _Pmlma10AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2)
)
_Pmlma10AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pmlma10AlmlineNetworkLaneAlarmWarning1Table = _Pmlma10AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104)
)
if mibBuilder.loadTexts:
    pmlma10AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pmlma10AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pmlma10AlmlineNetworkLaneAlarmWarning1Entry = _Pmlma10AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1)
)
pmlma10AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pmlma10AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pmlma10AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pmlma10AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pmlma10AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pmlma10AlmlineNetworkLaneAlarmWarning1Index = _Pmlma10AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 1),
    _Pmlma10AlmlineNetworkLaneAlarmWarning1Index_Type()
)
pmlma10AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pmlma10AlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pmlma10AlmLineTxPwrLowAlaPortn = _Pmlma10AlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 2),
    _Pmlma10AlmLineTxPwrLowAlaPortn_Type()
)
pmlma10AlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxPwrLowAlaPortn.setStatus("current")
_Pmlma10AlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pmlma10AlmLineTxPwrHighAlaPortn = _Pmlma10AlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 3),
    _Pmlma10AlmLineTxPwrHighAlaPortn_Type()
)
pmlma10AlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxPwrHighAlaPortn.setStatus("current")
_Pmlma10AlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pmlma10AlmLineTxBiasLowAlaPortn = _Pmlma10AlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 4),
    _Pmlma10AlmLineTxBiasLowAlaPortn_Type()
)
pmlma10AlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxBiasLowAlaPortn.setStatus("current")
_Pmlma10AlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pmlma10AlmLineTxBiasHighAlaPortn = _Pmlma10AlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 5),
    _Pmlma10AlmLineTxBiasHighAlaPortn_Type()
)
pmlma10AlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxBiasHighAlaPortn.setStatus("current")
_Pmlma10AlmLineVccLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineVccLowAlaPortn_Object = MibTableColumn
pmlma10AlmLineVccLowAlaPortn = _Pmlma10AlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 6),
    _Pmlma10AlmLineVccLowAlaPortn_Type()
)
pmlma10AlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineVccLowAlaPortn.setStatus("current")
_Pmlma10AlmLineVccHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineVccHighAlaPortn_Object = MibTableColumn
pmlma10AlmLineVccHighAlaPortn = _Pmlma10AlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 7),
    _Pmlma10AlmLineVccHighAlaPortn_Type()
)
pmlma10AlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineVccHighAlaPortn.setStatus("current")
_Pmlma10AlmLineTempLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineTempLowAlaPortn_Object = MibTableColumn
pmlma10AlmLineTempLowAlaPortn = _Pmlma10AlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 8),
    _Pmlma10AlmLineTempLowAlaPortn_Type()
)
pmlma10AlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTempLowAlaPortn.setStatus("current")
_Pmlma10AlmLineTempHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineTempHighAlaPortn_Object = MibTableColumn
pmlma10AlmLineTempHighAlaPortn = _Pmlma10AlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 9),
    _Pmlma10AlmLineTempHighAlaPortn_Type()
)
pmlma10AlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTempHighAlaPortn.setStatus("current")
_Pmlma10AlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pmlma10AlmLineRxPwrLowAlaPortn = _Pmlma10AlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 16),
    _Pmlma10AlmLineRxPwrLowAlaPortn_Type()
)
pmlma10AlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineRxPwrLowAlaPortn.setStatus("current")
_Pmlma10AlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pmlma10AlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pmlma10AlmLineRxPwrHighAlaPortn = _Pmlma10AlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 104, 1, 17),
    _Pmlma10AlmLineRxPwrHighAlaPortn_Type()
)
pmlma10AlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineRxPwrHighAlaPortn.setStatus("current")
_Pmlma10AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pmlma10AlmlineNetworkLaneAlarmWarning2Table = _Pmlma10AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120)
)
if mibBuilder.loadTexts:
    pmlma10AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pmlma10AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pmlma10AlmlineNetworkLaneAlarmWarning2Entry = _Pmlma10AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1)
)
pmlma10AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pmlma10AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pmlma10AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pmlma10AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pmlma10AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pmlma10AlmlineNetworkLaneAlarmWarning2Index = _Pmlma10AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 1),
    _Pmlma10AlmlineNetworkLaneAlarmWarning2Index_Type()
)
pmlma10AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pmlma10AlmLineTxPwLowWngPortn_Type = EkiOnOff
_Pmlma10AlmLineTxPwLowWngPortn_Object = MibTableColumn
pmlma10AlmLineTxPwLowWngPortn = _Pmlma10AlmLineTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 2),
    _Pmlma10AlmLineTxPwLowWngPortn_Type()
)
pmlma10AlmLineTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxPwLowWngPortn.setStatus("current")
_Pmlma10AlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pmlma10AlmLineTxPwrHighWngPortn_Object = MibTableColumn
pmlma10AlmLineTxPwrHighWngPortn = _Pmlma10AlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 3),
    _Pmlma10AlmLineTxPwrHighWngPortn_Type()
)
pmlma10AlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxPwrHighWngPortn.setStatus("current")
_Pmlma10AlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pmlma10AlmLineTxBiasLowWngPortn_Object = MibTableColumn
pmlma10AlmLineTxBiasLowWngPortn = _Pmlma10AlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 4),
    _Pmlma10AlmLineTxBiasLowWngPortn_Type()
)
pmlma10AlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxBiasLowWngPortn.setStatus("current")
_Pmlma10AlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pmlma10AlmLineTxBiasHighWngPortn_Object = MibTableColumn
pmlma10AlmLineTxBiasHighWngPortn = _Pmlma10AlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 5),
    _Pmlma10AlmLineTxBiasHighWngPortn_Type()
)
pmlma10AlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxBiasHighWngPortn.setStatus("current")
_Pmlma10AlmLineVccLowWngPortn_Type = EkiOnOff
_Pmlma10AlmLineVccLowWngPortn_Object = MibTableColumn
pmlma10AlmLineVccLowWngPortn = _Pmlma10AlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 6),
    _Pmlma10AlmLineVccLowWngPortn_Type()
)
pmlma10AlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineVccLowWngPortn.setStatus("current")
_Pmlma10AlmLineVccHighWngPortn_Type = EkiOnOff
_Pmlma10AlmLineVccHighWngPortn_Object = MibTableColumn
pmlma10AlmLineVccHighWngPortn = _Pmlma10AlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 7),
    _Pmlma10AlmLineVccHighWngPortn_Type()
)
pmlma10AlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineVccHighWngPortn.setStatus("current")
_Pmlma10AlmLineTempLowWngPortn_Type = EkiOnOff
_Pmlma10AlmLineTempLowWngPortn_Object = MibTableColumn
pmlma10AlmLineTempLowWngPortn = _Pmlma10AlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 8),
    _Pmlma10AlmLineTempLowWngPortn_Type()
)
pmlma10AlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTempLowWngPortn.setStatus("current")
_Pmlma10AlmLineTempHighWngPortn_Type = EkiOnOff
_Pmlma10AlmLineTempHighWngPortn_Object = MibTableColumn
pmlma10AlmLineTempHighWngPortn = _Pmlma10AlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 9),
    _Pmlma10AlmLineTempHighWngPortn_Type()
)
pmlma10AlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTempHighWngPortn.setStatus("current")
_Pmlma10AlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pmlma10AlmLineRxPwrLowWngPortn_Object = MibTableColumn
pmlma10AlmLineRxPwrLowWngPortn = _Pmlma10AlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 16),
    _Pmlma10AlmLineRxPwrLowWngPortn_Type()
)
pmlma10AlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineRxPwrLowWngPortn.setStatus("current")
_Pmlma10AlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pmlma10AlmLineRxPwrHighWngPortn_Object = MibTableColumn
pmlma10AlmLineRxPwrHighWngPortn = _Pmlma10AlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 120, 1, 17),
    _Pmlma10AlmLineRxPwrHighWngPortn_Type()
)
pmlma10AlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineRxPwrHighWngPortn.setStatus("current")
_Pmlma10AlmlineHostLaneFaultTable_Object = MibTable
pmlma10AlmlineHostLaneFaultTable = _Pmlma10AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152)
)
if mibBuilder.loadTexts:
    pmlma10AlmlineHostLaneFaultTable.setStatus("current")
_Pmlma10AlmlineHostLaneFaultEntry_Object = MibTableRow
pmlma10AlmlineHostLaneFaultEntry = _Pmlma10AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152, 1)
)
pmlma10AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pmlma10AlmlineHostLaneFaultEntry.setStatus("current")


class _Pmlma10AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pmlma10AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pmlma10AlmlineHostLaneFaultIndex_Object = MibTableColumn
pmlma10AlmlineHostLaneFaultIndex = _Pmlma10AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152, 1, 1),
    _Pmlma10AlmlineHostLaneFaultIndex_Type()
)
pmlma10AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmlineHostLaneFaultIndex.setStatus("current")
_Pmlma10AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pmlma10AlmLineInputLossOfSignalPortn_Object = MibTableColumn
pmlma10AlmLineInputLossOfSignalPortn = _Pmlma10AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152, 1, 2),
    _Pmlma10AlmLineInputLossOfSignalPortn_Type()
)
pmlma10AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineInputLossOfSignalPortn.setStatus("current")
_Pmlma10AlmLineLossOfFramePortn_Type = EkiOnOff
_Pmlma10AlmLineLossOfFramePortn_Object = MibTableColumn
pmlma10AlmLineLossOfFramePortn = _Pmlma10AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152, 1, 3),
    _Pmlma10AlmLineLossOfFramePortn_Type()
)
pmlma10AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineLossOfFramePortn.setStatus("current")
_Pmlma10AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pmlma10AlmLineSmBdiInsertedPortn_Object = MibTableColumn
pmlma10AlmLineSmBdiInsertedPortn = _Pmlma10AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152, 1, 4),
    _Pmlma10AlmLineSmBdiInsertedPortn_Type()
)
pmlma10AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineSmBdiInsertedPortn.setStatus("current")
_Pmlma10AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pmlma10AlmLineSmBdiDetectedPortn_Object = MibTableColumn
pmlma10AlmLineSmBdiDetectedPortn = _Pmlma10AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 2, 152, 1, 5),
    _Pmlma10AlmLineSmBdiDetectedPortn_Type()
)
pmlma10AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineSmBdiDetectedPortn.setStatus("current")
_Pmlma10AlmLineCrit_ObjectIdentity = ObjectIdentity
pmlma10AlmLineCrit = _Pmlma10AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3)
)
_Pmlma10AlmsynthAlmLineTable_Object = MibTable
pmlma10AlmsynthAlmLineTable = _Pmlma10AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pmlma10AlmsynthAlmLineTable.setStatus("current")
_Pmlma10AlmsynthAlmLineEntry_Object = MibTableRow
pmlma10AlmsynthAlmLineEntry = _Pmlma10AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1)
)
pmlma10AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pmlma10AlmsynthAlmLineEntry.setStatus("current")


class _Pmlma10AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pmlma10AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pmlma10AlmsynthAlmLineIndex_Object = MibTableColumn
pmlma10AlmsynthAlmLineIndex = _Pmlma10AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 1),
    _Pmlma10AlmsynthAlmLineIndex_Type()
)
pmlma10AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmsynthAlmLineIndex.setStatus("current")
_Pmlma10AlmLineSfpAbsentPortn_Type = EkiOnOff
_Pmlma10AlmLineSfpAbsentPortn_Object = MibTableColumn
pmlma10AlmLineSfpAbsentPortn = _Pmlma10AlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 2),
    _Pmlma10AlmLineSfpAbsentPortn_Type()
)
pmlma10AlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineSfpAbsentPortn.setStatus("current")
_Pmlma10AlmLineDdmAbsentPortn_Type = EkiOnOff
_Pmlma10AlmLineDdmAbsentPortn_Object = MibTableColumn
pmlma10AlmLineDdmAbsentPortn = _Pmlma10AlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 3),
    _Pmlma10AlmLineDdmAbsentPortn_Type()
)
pmlma10AlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineDdmAbsentPortn.setStatus("current")
_Pmlma10AlmLineHwFailPortn_Type = EkiOnOff
_Pmlma10AlmLineHwFailPortn_Object = MibTableColumn
pmlma10AlmLineHwFailPortn = _Pmlma10AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 5),
    _Pmlma10AlmLineHwFailPortn_Type()
)
pmlma10AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineHwFailPortn.setStatus("current")
_Pmlma10AlmLineTxOffPortn_Type = EkiOnOff
_Pmlma10AlmLineTxOffPortn_Object = MibTableColumn
pmlma10AlmLineTxOffPortn = _Pmlma10AlmLineTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 6),
    _Pmlma10AlmLineTxOffPortn_Type()
)
pmlma10AlmLineTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineTxOffPortn.setStatus("current")
_Pmlma10AlmLineLocalOosPortn_Type = EkiOnOff
_Pmlma10AlmLineLocalOosPortn_Object = MibTableColumn
pmlma10AlmLineLocalOosPortn = _Pmlma10AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 7),
    _Pmlma10AlmLineLocalOosPortn_Type()
)
pmlma10AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineLocalOosPortn.setStatus("current")
_Pmlma10AlmUpRdiInsPortn_Type = EkiOnOff
_Pmlma10AlmUpRdiInsPortn_Object = MibTableColumn
pmlma10AlmUpRdiInsPortn = _Pmlma10AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 9),
    _Pmlma10AlmUpRdiInsPortn_Type()
)
pmlma10AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmUpRdiInsPortn.setStatus("current")
_Pmlma10AlmLineDdmWarningPortn_Type = EkiOnOff
_Pmlma10AlmLineDdmWarningPortn_Object = MibTableColumn
pmlma10AlmLineDdmWarningPortn = _Pmlma10AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 10),
    _Pmlma10AlmLineDdmWarningPortn_Type()
)
pmlma10AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineDdmWarningPortn.setStatus("current")
_Pmlma10AlmLineDdmAlmPortn_Type = EkiOnOff
_Pmlma10AlmLineDdmAlmPortn_Object = MibTableColumn
pmlma10AlmLineDdmAlmPortn = _Pmlma10AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 11),
    _Pmlma10AlmLineDdmAlmPortn_Type()
)
pmlma10AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineDdmAlmPortn.setStatus("current")
_Pmlma10AlmLineFailPortn_Type = EkiOnOff
_Pmlma10AlmLineFailPortn_Object = MibTableColumn
pmlma10AlmLineFailPortn = _Pmlma10AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 2, 3, 3, 24, 1, 13),
    _Pmlma10AlmLineFailPortn_Type()
)
pmlma10AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10AlmLineFailPortn.setStatus("current")
_Pmlma10measures_ObjectIdentity = ObjectIdentity
pmlma10measures = _Pmlma10measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3)
)
_Pmlma10MesrOther_ObjectIdentity = ObjectIdentity
pmlma10MesrOther = _Pmlma10MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 1)
)
_Pmlma10MesrClient_ObjectIdentity = ObjectIdentity
pmlma10MesrClient = _Pmlma10MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2)
)
_Pmlma10MesrclientTempTable_Object = MibTable
pmlma10MesrclientTempTable = _Pmlma10MesrclientTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmlma10MesrclientTempTable.setStatus("current")
_Pmlma10MesrclientTempEntry_Object = MibTableRow
pmlma10MesrclientTempEntry = _Pmlma10MesrclientTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 16, 1)
)
pmlma10MesrclientTempEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrclientTempIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrclientTempEntry.setStatus("current")


class _Pmlma10MesrclientTempIndex_Type(Integer32):
    """Custom type pmlma10MesrclientTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrclientTempIndex_Type.__name__ = "Integer32"
_Pmlma10MesrclientTempIndex_Object = MibTableColumn
pmlma10MesrclientTempIndex = _Pmlma10MesrclientTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 16, 1, 1),
    _Pmlma10MesrclientTempIndex_Type()
)
pmlma10MesrclientTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientTempIndex.setStatus("current")


class _Pmlma10MesrclientTempPortn_Type(Integer32):
    """Custom type pmlma10MesrclientTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrclientTempPortn_Type.__name__ = "Integer32"
_Pmlma10MesrclientTempPortn_Object = MibTableColumn
pmlma10MesrclientTempPortn = _Pmlma10MesrclientTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 16, 1, 2),
    _Pmlma10MesrclientTempPortn_Type()
)
pmlma10MesrclientTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientTempPortn.setStatus("current")
_Pmlma10MesrclientTxBiasTable_Object = MibTable
pmlma10MesrclientTxBiasTable = _Pmlma10MesrclientTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmlma10MesrclientTxBiasTable.setStatus("current")
_Pmlma10MesrclientTxBiasEntry_Object = MibTableRow
pmlma10MesrclientTxBiasEntry = _Pmlma10MesrclientTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 32, 1)
)
pmlma10MesrclientTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrclientTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrclientTxBiasEntry.setStatus("current")


class _Pmlma10MesrclientTxBiasIndex_Type(Integer32):
    """Custom type pmlma10MesrclientTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrclientTxBiasIndex_Type.__name__ = "Integer32"
_Pmlma10MesrclientTxBiasIndex_Object = MibTableColumn
pmlma10MesrclientTxBiasIndex = _Pmlma10MesrclientTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 32, 1, 1),
    _Pmlma10MesrclientTxBiasIndex_Type()
)
pmlma10MesrclientTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientTxBiasIndex.setStatus("current")


class _Pmlma10MesrclientTxBiasPortn_Type(Integer32):
    """Custom type pmlma10MesrclientTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrclientTxBiasPortn_Type.__name__ = "Integer32"
_Pmlma10MesrclientTxBiasPortn_Object = MibTableColumn
pmlma10MesrclientTxBiasPortn = _Pmlma10MesrclientTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 32, 1, 2),
    _Pmlma10MesrclientTxBiasPortn_Type()
)
pmlma10MesrclientTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientTxBiasPortn.setStatus("current")
_Pmlma10MesrclientTxPwrTable_Object = MibTable
pmlma10MesrclientTxPwrTable = _Pmlma10MesrclientTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmlma10MesrclientTxPwrTable.setStatus("current")
_Pmlma10MesrclientTxPwrEntry_Object = MibTableRow
pmlma10MesrclientTxPwrEntry = _Pmlma10MesrclientTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 48, 1)
)
pmlma10MesrclientTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrclientTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrclientTxPwrEntry.setStatus("current")


class _Pmlma10MesrclientTxPwrIndex_Type(Integer32):
    """Custom type pmlma10MesrclientTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrclientTxPwrIndex_Type.__name__ = "Integer32"
_Pmlma10MesrclientTxPwrIndex_Object = MibTableColumn
pmlma10MesrclientTxPwrIndex = _Pmlma10MesrclientTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 48, 1, 1),
    _Pmlma10MesrclientTxPwrIndex_Type()
)
pmlma10MesrclientTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientTxPwrIndex.setStatus("current")


class _Pmlma10MesrclientTxPwrPortn_Type(Integer32):
    """Custom type pmlma10MesrclientTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrclientTxPwrPortn_Type.__name__ = "Integer32"
_Pmlma10MesrclientTxPwrPortn_Object = MibTableColumn
pmlma10MesrclientTxPwrPortn = _Pmlma10MesrclientTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 48, 1, 2),
    _Pmlma10MesrclientTxPwrPortn_Type()
)
pmlma10MesrclientTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientTxPwrPortn.setStatus("current")
_Pmlma10MesrclientRxPwrTable_Object = MibTable
pmlma10MesrclientRxPwrTable = _Pmlma10MesrclientRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 64)
)
if mibBuilder.loadTexts:
    pmlma10MesrclientRxPwrTable.setStatus("current")
_Pmlma10MesrclientRxPwrEntry_Object = MibTableRow
pmlma10MesrclientRxPwrEntry = _Pmlma10MesrclientRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 64, 1)
)
pmlma10MesrclientRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrclientRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrclientRxPwrEntry.setStatus("current")


class _Pmlma10MesrclientRxPwrIndex_Type(Integer32):
    """Custom type pmlma10MesrclientRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrclientRxPwrIndex_Type.__name__ = "Integer32"
_Pmlma10MesrclientRxPwrIndex_Object = MibTableColumn
pmlma10MesrclientRxPwrIndex = _Pmlma10MesrclientRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 64, 1, 1),
    _Pmlma10MesrclientRxPwrIndex_Type()
)
pmlma10MesrclientRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientRxPwrIndex.setStatus("current")


class _Pmlma10MesrclientRxPwrPortn_Type(Integer32):
    """Custom type pmlma10MesrclientRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrclientRxPwrPortn_Type.__name__ = "Integer32"
_Pmlma10MesrclientRxPwrPortn_Object = MibTableColumn
pmlma10MesrclientRxPwrPortn = _Pmlma10MesrclientRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 2, 64, 1, 2),
    _Pmlma10MesrclientRxPwrPortn_Type()
)
pmlma10MesrclientRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrclientRxPwrPortn.setStatus("current")
_Pmlma10MesrLine_ObjectIdentity = ObjectIdentity
pmlma10MesrLine = _Pmlma10MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3)
)
_Pmlma10MesrlineTxPwrTable_Object = MibTable
pmlma10MesrlineTxPwrTable = _Pmlma10MesrlineTxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 80)
)
if mibBuilder.loadTexts:
    pmlma10MesrlineTxPwrTable.setStatus("current")
_Pmlma10MesrlineTxPwrEntry_Object = MibTableRow
pmlma10MesrlineTxPwrEntry = _Pmlma10MesrlineTxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 80, 1)
)
pmlma10MesrlineTxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrlineTxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrlineTxPwrEntry.setStatus("current")


class _Pmlma10MesrlineTxPwrIndex_Type(Integer32):
    """Custom type pmlma10MesrlineTxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrlineTxPwrIndex_Type.__name__ = "Integer32"
_Pmlma10MesrlineTxPwrIndex_Object = MibTableColumn
pmlma10MesrlineTxPwrIndex = _Pmlma10MesrlineTxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 80, 1, 1),
    _Pmlma10MesrlineTxPwrIndex_Type()
)
pmlma10MesrlineTxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineTxPwrIndex.setStatus("current")


class _Pmlma10MesrlineTxPwrPortn_Type(Integer32):
    """Custom type pmlma10MesrlineTxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrlineTxPwrPortn_Type.__name__ = "Integer32"
_Pmlma10MesrlineTxPwrPortn_Object = MibTableColumn
pmlma10MesrlineTxPwrPortn = _Pmlma10MesrlineTxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 80, 1, 2),
    _Pmlma10MesrlineTxPwrPortn_Type()
)
pmlma10MesrlineTxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineTxPwrPortn.setStatus("current")
_Pmlma10MesrlineTempTable_Object = MibTable
pmlma10MesrlineTempTable = _Pmlma10MesrlineTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 96)
)
if mibBuilder.loadTexts:
    pmlma10MesrlineTempTable.setStatus("current")
_Pmlma10MesrlineTempEntry_Object = MibTableRow
pmlma10MesrlineTempEntry = _Pmlma10MesrlineTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 96, 1)
)
pmlma10MesrlineTempEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrlineTempIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrlineTempEntry.setStatus("current")


class _Pmlma10MesrlineTempIndex_Type(Integer32):
    """Custom type pmlma10MesrlineTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrlineTempIndex_Type.__name__ = "Integer32"
_Pmlma10MesrlineTempIndex_Object = MibTableColumn
pmlma10MesrlineTempIndex = _Pmlma10MesrlineTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 96, 1, 1),
    _Pmlma10MesrlineTempIndex_Type()
)
pmlma10MesrlineTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineTempIndex.setStatus("current")


class _Pmlma10MesrlineTempPortn_Type(Integer32):
    """Custom type pmlma10MesrlineTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrlineTempPortn_Type.__name__ = "Integer32"
_Pmlma10MesrlineTempPortn_Object = MibTableColumn
pmlma10MesrlineTempPortn = _Pmlma10MesrlineTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 96, 1, 2),
    _Pmlma10MesrlineTempPortn_Type()
)
pmlma10MesrlineTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineTempPortn.setStatus("current")
_Pmlma10MesrlineTxBiasTable_Object = MibTable
pmlma10MesrlineTxBiasTable = _Pmlma10MesrlineTxBiasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 112)
)
if mibBuilder.loadTexts:
    pmlma10MesrlineTxBiasTable.setStatus("current")
_Pmlma10MesrlineTxBiasEntry_Object = MibTableRow
pmlma10MesrlineTxBiasEntry = _Pmlma10MesrlineTxBiasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 112, 1)
)
pmlma10MesrlineTxBiasEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrlineTxBiasIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrlineTxBiasEntry.setStatus("current")


class _Pmlma10MesrlineTxBiasIndex_Type(Integer32):
    """Custom type pmlma10MesrlineTxBiasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrlineTxBiasIndex_Type.__name__ = "Integer32"
_Pmlma10MesrlineTxBiasIndex_Object = MibTableColumn
pmlma10MesrlineTxBiasIndex = _Pmlma10MesrlineTxBiasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 112, 1, 1),
    _Pmlma10MesrlineTxBiasIndex_Type()
)
pmlma10MesrlineTxBiasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineTxBiasIndex.setStatus("current")


class _Pmlma10MesrlineTxBiasPortn_Type(Integer32):
    """Custom type pmlma10MesrlineTxBiasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrlineTxBiasPortn_Type.__name__ = "Integer32"
_Pmlma10MesrlineTxBiasPortn_Object = MibTableColumn
pmlma10MesrlineTxBiasPortn = _Pmlma10MesrlineTxBiasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 112, 1, 2),
    _Pmlma10MesrlineTxBiasPortn_Type()
)
pmlma10MesrlineTxBiasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineTxBiasPortn.setStatus("current")
_Pmlma10MesrlineRxPwrTable_Object = MibTable
pmlma10MesrlineRxPwrTable = _Pmlma10MesrlineRxPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pmlma10MesrlineRxPwrTable.setStatus("current")
_Pmlma10MesrlineRxPwrEntry_Object = MibTableRow
pmlma10MesrlineRxPwrEntry = _Pmlma10MesrlineRxPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 128, 1)
)
pmlma10MesrlineRxPwrEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MesrlineRxPwrIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MesrlineRxPwrEntry.setStatus("current")


class _Pmlma10MesrlineRxPwrIndex_Type(Integer32):
    """Custom type pmlma10MesrlineRxPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MesrlineRxPwrIndex_Type.__name__ = "Integer32"
_Pmlma10MesrlineRxPwrIndex_Object = MibTableColumn
pmlma10MesrlineRxPwrIndex = _Pmlma10MesrlineRxPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 128, 1, 1),
    _Pmlma10MesrlineRxPwrIndex_Type()
)
pmlma10MesrlineRxPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineRxPwrIndex.setStatus("current")


class _Pmlma10MesrlineRxPwrPortn_Type(Integer32):
    """Custom type pmlma10MesrlineRxPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmlma10MesrlineRxPwrPortn_Type.__name__ = "Integer32"
_Pmlma10MesrlineRxPwrPortn_Object = MibTableColumn
pmlma10MesrlineRxPwrPortn = _Pmlma10MesrlineRxPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 3, 3, 128, 1, 2),
    _Pmlma10MesrlineRxPwrPortn_Type()
)
pmlma10MesrlineRxPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MesrlineRxPwrPortn.setStatus("current")
_Pmlma10counters_ObjectIdentity = ObjectIdentity
pmlma10counters = _Pmlma10counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4)
)
_Pmlma10CntOther_ObjectIdentity = ObjectIdentity
pmlma10CntOther = _Pmlma10CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 1)
)
_Pmlma10CntClient_ObjectIdentity = ObjectIdentity
pmlma10CntClient = _Pmlma10CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2)
)
_Pmlma10CntclientCbipCounterTable_Object = MibTable
pmlma10CntclientCbipCounterTable = _Pmlma10CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2, 96)
)
if mibBuilder.loadTexts:
    pmlma10CntclientCbipCounterTable.setStatus("current")
_Pmlma10CntclientCbipCounterEntry_Object = MibTableRow
pmlma10CntclientCbipCounterEntry = _Pmlma10CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2, 96, 1)
)
pmlma10CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CntclientCbipCounterEntry.setStatus("current")


class _Pmlma10CntclientCbipCounterIndex_Type(Integer32):
    """Custom type pmlma10CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pmlma10CntclientCbipCounterIndex_Object = MibTableColumn
pmlma10CntclientCbipCounterIndex = _Pmlma10CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2, 96, 1, 1),
    _Pmlma10CntclientCbipCounterIndex_Type()
)
pmlma10CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntclientCbipCounterIndex.setStatus("current")
_Pmlma10CntclientCbipCounterValuePortn_Type = Counter32
_Pmlma10CntclientCbipCounterValuePortn_Object = MibTableColumn
pmlma10CntclientCbipCounterValuePortn = _Pmlma10CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2, 96, 1, 2),
    _Pmlma10CntclientCbipCounterValuePortn_Type()
)
pmlma10CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntclientCbipCounterValuePortn.setStatus("current")
_Pmlma10CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pmlma10CntclientCbipCounterErrorPortn_Object = MibTableColumn
pmlma10CntclientCbipCounterErrorPortn = _Pmlma10CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2, 96, 1, 3),
    _Pmlma10CntclientCbipCounterErrorPortn_Type()
)
pmlma10CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntclientCbipCounterErrorPortn.setStatus("current")
_Pmlma10CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pmlma10CntclientCbipCounterOverloadPortn_Object = MibTableColumn
pmlma10CntclientCbipCounterOverloadPortn = _Pmlma10CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 2, 96, 1, 4),
    _Pmlma10CntclientCbipCounterOverloadPortn_Type()
)
pmlma10CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntclientCbipCounterOverloadPortn.setStatus("current")
_Pmlma10CntLine_ObjectIdentity = ObjectIdentity
pmlma10CntLine = _Pmlma10CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3)
)
_Pmlma10CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pmlma10CntlocalLineSmBip8ErrorCounterTable = _Pmlma10CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pmlma10CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pmlma10CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pmlma10CntlocalLineSmBip8ErrorCounterEntry = _Pmlma10CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 192, 1)
)
pmlma10CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pmlma10CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pmlma10CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pmlma10CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pmlma10CntlocalLineSmBip8ErrorCounterIndex = _Pmlma10CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 192, 1, 1),
    _Pmlma10CntlocalLineSmBip8ErrorCounterIndex_Type()
)
pmlma10CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pmlma10CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter32
_Pmlma10CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pmlma10CntlocalLineSmBip8ErrorCounterValuePortn = _Pmlma10CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 192, 1, 2),
    _Pmlma10CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pmlma10CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn = _Pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 192, 1, 3),
    _Pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn = _Pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 192, 1, 4),
    _Pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pmlma10CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pmlma10CntlocalLineFecCorrectedErrorsCounterTable = _Pmlma10CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 200)
)
if mibBuilder.loadTexts:
    pmlma10CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pmlma10CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pmlma10CntlocalLineFecCorrectedErrorsCounterEntry = _Pmlma10CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 200, 1)
)
pmlma10CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pmlma10CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pmlma10CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pmlma10CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pmlma10CntlocalLineFecCorrectedErrorsCounterIndex = _Pmlma10CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 200, 1, 1),
    _Pmlma10CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pmlma10CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter32
_Pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn = _Pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 200, 1, 2),
    _Pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 200, 1, 3),
    _Pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 200, 1, 4),
    _Pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pmlma10CntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pmlma10CntremoteLineSmBip8ErrorCounterTable = _Pmlma10CntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 208)
)
if mibBuilder.loadTexts:
    pmlma10CntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pmlma10CntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pmlma10CntremoteLineSmBip8ErrorCounterEntry = _Pmlma10CntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 208, 1)
)
pmlma10CntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pmlma10CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pmlma10CntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pmlma10CntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pmlma10CntremoteLineSmBip8ErrorCounterIndex = _Pmlma10CntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 208, 1, 1),
    _Pmlma10CntremoteLineSmBip8ErrorCounterIndex_Type()
)
pmlma10CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pmlma10CntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter32
_Pmlma10CntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pmlma10CntremoteLineSmBip8ErrorCounterValuePortn = _Pmlma10CntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 208, 1, 2),
    _Pmlma10CntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pmlma10CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn = _Pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 208, 1, 3),
    _Pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn = _Pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 208, 1, 4),
    _Pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pmlma10CntlineDfrmTimCntTable_Object = MibTable
pmlma10CntlineDfrmTimCntTable = _Pmlma10CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 216)
)
if mibBuilder.loadTexts:
    pmlma10CntlineDfrmTimCntTable.setStatus("current")
_Pmlma10CntlineDfrmTimCntEntry_Object = MibTableRow
pmlma10CntlineDfrmTimCntEntry = _Pmlma10CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 216, 1)
)
pmlma10CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CntlineDfrmTimCntEntry.setStatus("current")


class _Pmlma10CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pmlma10CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pmlma10CntlineDfrmTimCntIndex_Object = MibTableColumn
pmlma10CntlineDfrmTimCntIndex = _Pmlma10CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 216, 1, 1),
    _Pmlma10CntlineDfrmTimCntIndex_Type()
)
pmlma10CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlineDfrmTimCntIndex.setStatus("current")
_Pmlma10CntlineDfrmTimCntValuePortn_Type = Counter32
_Pmlma10CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pmlma10CntlineDfrmTimCntValuePortn = _Pmlma10CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 216, 1, 2),
    _Pmlma10CntlineDfrmTimCntValuePortn_Type()
)
pmlma10CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlineDfrmTimCntValuePortn.setStatus("current")
_Pmlma10CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pmlma10CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pmlma10CntlineDfrmTimCntErrorPortn = _Pmlma10CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 216, 1, 3),
    _Pmlma10CntlineDfrmTimCntErrorPortn_Type()
)
pmlma10CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pmlma10CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pmlma10CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pmlma10CntlineDfrmTimCntOverloadPortn = _Pmlma10CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 3, 216, 1, 4),
    _Pmlma10CntlineDfrmTimCntOverloadPortn_Type()
)
pmlma10CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pmlma10CntCountersReset_Type = EkiOnOff
_Pmlma10CntCountersReset_Object = MibScalar
pmlma10CntCountersReset = _Pmlma10CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 259),
    _Pmlma10CntCountersReset_Type()
)
pmlma10CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CntCountersReset.setStatus("current")
_Pmlma10CntCountersStop_Type = EkiOnOff
_Pmlma10CntCountersStop_Object = MibScalar
pmlma10CntCountersStop = _Pmlma10CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 4, 260),
    _Pmlma10CntCountersStop_Type()
)
pmlma10CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CntCountersStop.setStatus("current")
_Pmlma10controlsWrite_ObjectIdentity = ObjectIdentity
pmlma10controlsWrite = _Pmlma10controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6)
)
_Pmlma10CtrlOther_ObjectIdentity = ObjectIdentity
pmlma10CtrlOther = _Pmlma10CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1)
)
_Pmlma10CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmlma10CtrlconfMgnt1 = _Pmlma10CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 1)
)
_Pmlma10CtrlConf1Load1_Type = EkiOnOff
_Pmlma10CtrlConf1Load1_Object = MibScalar
pmlma10CtrlConf1Load1 = _Pmlma10CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 1, 1),
    _Pmlma10CtrlConf1Load1_Type()
)
pmlma10CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlConf1Load1.setStatus("current")
_Pmlma10CtrlConf2Load1_Type = EkiOnOff
_Pmlma10CtrlConf2Load1_Object = MibScalar
pmlma10CtrlConf2Load1 = _Pmlma10CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 1, 2),
    _Pmlma10CtrlConf2Load1_Type()
)
pmlma10CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlConf2Load1.setStatus("current")
_Pmlma10CtrlConf2Flash1_Type = EkiOnOff
_Pmlma10CtrlConf2Flash1_Object = MibScalar
pmlma10CtrlConf2Flash1 = _Pmlma10CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 1, 10),
    _Pmlma10CtrlConf2Flash1_Type()
)
pmlma10CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlConf2Flash1.setStatus("current")
_Pmlma10CtrlConf2Clear1_Type = EkiOnOff
_Pmlma10CtrlConf2Clear1_Object = MibScalar
pmlma10CtrlConf2Clear1 = _Pmlma10CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 1, 14),
    _Pmlma10CtrlConf2Clear1_Type()
)
pmlma10CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlConf2Clear1.setStatus("current")
_Pmlma10Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmlma10Ctrlsynth4 = _Pmlma10Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 4)
)
_Pmlma10CtrlCorrelatOn_Type = EkiOnOff
_Pmlma10CtrlCorrelatOn_Object = MibScalar
pmlma10CtrlCorrelatOn = _Pmlma10CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 4, 1),
    _Pmlma10CtrlCorrelatOn_Type()
)
pmlma10CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlCorrelatOn.setStatus("current")
_Pmlma10CtrlCorrelatOff_Type = EkiOnOff
_Pmlma10CtrlCorrelatOff_Object = MibScalar
pmlma10CtrlCorrelatOff = _Pmlma10CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 4, 2),
    _Pmlma10CtrlCorrelatOff_Type()
)
pmlma10CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlCorrelatOff.setStatus("current")
_Pmlma10CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmlma10CtrlswMgnt = _Pmlma10CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 5)
)
_Pmlma10CtrlColdReset_Type = EkiOnOff
_Pmlma10CtrlColdReset_Object = MibScalar
pmlma10CtrlColdReset = _Pmlma10CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 5, 2),
    _Pmlma10CtrlColdReset_Type()
)
pmlma10CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlColdReset.setStatus("current")
_Pmlma10CtrlWarmReset_Type = EkiOnOff
_Pmlma10CtrlWarmReset_Object = MibScalar
pmlma10CtrlWarmReset = _Pmlma10CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 5, 3),
    _Pmlma10CtrlWarmReset_Type()
)
pmlma10CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlWarmReset.setStatus("current")
_Pmlma10CtrlLoadSwBank1_Type = EkiOnOff
_Pmlma10CtrlLoadSwBank1_Object = MibScalar
pmlma10CtrlLoadSwBank1 = _Pmlma10CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 5, 5),
    _Pmlma10CtrlLoadSwBank1_Type()
)
pmlma10CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLoadSwBank1.setStatus("current")
_Pmlma10CtrlLoadSwBank2_Type = EkiOnOff
_Pmlma10CtrlLoadSwBank2_Object = MibScalar
pmlma10CtrlLoadSwBank2 = _Pmlma10CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 5, 6),
    _Pmlma10CtrlLoadSwBank2_Type()
)
pmlma10CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLoadSwBank2.setStatus("current")
_Pmlma10CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmlma10CtrlgwMgnt = _Pmlma10CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 6)
)
_Pmlma10CtrlCurrentGwReset_Type = EkiOnOff
_Pmlma10CtrlCurrentGwReset_Object = MibScalar
pmlma10CtrlCurrentGwReset = _Pmlma10CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 6, 1),
    _Pmlma10CtrlCurrentGwReset_Type()
)
pmlma10CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlCurrentGwReset.setStatus("current")
_Pmlma10CtrlLoadGwBank1_Type = EkiOnOff
_Pmlma10CtrlLoadGwBank1_Object = MibScalar
pmlma10CtrlLoadGwBank1 = _Pmlma10CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 6, 5),
    _Pmlma10CtrlLoadGwBank1_Type()
)
pmlma10CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLoadGwBank1.setStatus("current")
_Pmlma10CtrlLoadGwBank2_Type = EkiOnOff
_Pmlma10CtrlLoadGwBank2_Object = MibScalar
pmlma10CtrlLoadGwBank2 = _Pmlma10CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 6, 6),
    _Pmlma10CtrlLoadGwBank2_Type()
)
pmlma10CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLoadGwBank2.setStatus("current")
_Pmlma10CtrlLoadGwBank3_Type = EkiOnOff
_Pmlma10CtrlLoadGwBank3_Object = MibScalar
pmlma10CtrlLoadGwBank3 = _Pmlma10CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 6, 7),
    _Pmlma10CtrlLoadGwBank3_Type()
)
pmlma10CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLoadGwBank3.setStatus("current")
_Pmlma10CtrlLoadGwBank4_Type = EkiOnOff
_Pmlma10CtrlLoadGwBank4_Object = MibScalar
pmlma10CtrlLoadGwBank4 = _Pmlma10CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 6, 8),
    _Pmlma10CtrlLoadGwBank4_Type()
)
pmlma10CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLoadGwBank4.setStatus("current")
_Pmlma10CtrlledTest_ObjectIdentity = ObjectIdentity
pmlma10CtrlledTest = _Pmlma10CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 192)
)
_Pmlma10CtrlGreenLed_Type = EkiOnOff
_Pmlma10CtrlGreenLed_Object = MibScalar
pmlma10CtrlGreenLed = _Pmlma10CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 192, 1),
    _Pmlma10CtrlGreenLed_Type()
)
pmlma10CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlGreenLed.setStatus("current")
_Pmlma10CtrlRedLed_Type = EkiOnOff
_Pmlma10CtrlRedLed_Object = MibScalar
pmlma10CtrlRedLed = _Pmlma10CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 192, 2),
    _Pmlma10CtrlRedLed_Type()
)
pmlma10CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlRedLed.setStatus("current")
_Pmlma10CtrlLedOff_Type = EkiOnOff
_Pmlma10CtrlLedOff_Object = MibScalar
pmlma10CtrlLedOff = _Pmlma10CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 1, 192, 3),
    _Pmlma10CtrlLedOff_Type()
)
pmlma10CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlLedOff.setStatus("current")
_Pmlma10CtrlClient_ObjectIdentity = ObjectIdentity
pmlma10CtrlClient = _Pmlma10CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2)
)
_Pmlma10CtrlaccessLoopTable_Object = MibTable
pmlma10CtrlaccessLoopTable = _Pmlma10CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmlma10CtrlaccessLoopTable.setStatus("current")
_Pmlma10CtrlaccessLoopEntry_Object = MibTableRow
pmlma10CtrlaccessLoopEntry = _Pmlma10CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 16, 1)
)
pmlma10CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrlaccessLoopEntry.setStatus("current")


class _Pmlma10CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pmlma10CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pmlma10CtrlaccessLoopIndex_Object = MibTableColumn
pmlma10CtrlaccessLoopIndex = _Pmlma10CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 16, 1, 1),
    _Pmlma10CtrlaccessLoopIndex_Type()
)
pmlma10CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrlaccessLoopIndex.setStatus("current")
_Pmlma10CtrlaccessLoopPortn_Type = EkiState
_Pmlma10CtrlaccessLoopPortn_Object = MibTableColumn
pmlma10CtrlaccessLoopPortn = _Pmlma10CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 16, 1, 2),
    _Pmlma10CtrlaccessLoopPortn_Type()
)
pmlma10CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlaccessLoopPortn.setStatus("current")
_Pmlma10CtrlclientLoopToLineTable_Object = MibTable
pmlma10CtrlclientLoopToLineTable = _Pmlma10CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pmlma10CtrlclientLoopToLineTable.setStatus("current")
_Pmlma10CtrlclientLoopToLineEntry_Object = MibTableRow
pmlma10CtrlclientLoopToLineEntry = _Pmlma10CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 17, 1)
)
pmlma10CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrlclientLoopToLineEntry.setStatus("current")


class _Pmlma10CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pmlma10CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pmlma10CtrlclientLoopToLineIndex_Object = MibTableColumn
pmlma10CtrlclientLoopToLineIndex = _Pmlma10CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 17, 1, 1),
    _Pmlma10CtrlclientLoopToLineIndex_Type()
)
pmlma10CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrlclientLoopToLineIndex.setStatus("current")
_Pmlma10CtrlclientLoopToLinePortn_Type = EkiState
_Pmlma10CtrlclientLoopToLinePortn_Object = MibTableColumn
pmlma10CtrlclientLoopToLinePortn = _Pmlma10CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 17, 1, 2),
    _Pmlma10CtrlclientLoopToLinePortn_Type()
)
pmlma10CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlclientLoopToLinePortn.setStatus("current")
_Pmlma10CtrlcsfUpInsTable_Object = MibTable
pmlma10CtrlcsfUpInsTable = _Pmlma10CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pmlma10CtrlcsfUpInsTable.setStatus("current")
_Pmlma10CtrlcsfUpInsEntry_Object = MibTableRow
pmlma10CtrlcsfUpInsEntry = _Pmlma10CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 21, 1)
)
pmlma10CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrlcsfUpInsEntry.setStatus("current")


class _Pmlma10CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pmlma10CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pmlma10CtrlcsfUpInsIndex_Object = MibTableColumn
pmlma10CtrlcsfUpInsIndex = _Pmlma10CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 21, 1, 1),
    _Pmlma10CtrlcsfUpInsIndex_Type()
)
pmlma10CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrlcsfUpInsIndex.setStatus("current")
_Pmlma10CtrlcsfUpInsPortn_Type = EkiState
_Pmlma10CtrlcsfUpInsPortn_Object = MibTableColumn
pmlma10CtrlcsfUpInsPortn = _Pmlma10CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 21, 1, 2),
    _Pmlma10CtrlcsfUpInsPortn_Type()
)
pmlma10CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlcsfUpInsPortn.setStatus("current")
_Pmlma10CtrlcaisDwInsTable_Object = MibTable
pmlma10CtrlcaisDwInsTable = _Pmlma10CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pmlma10CtrlcaisDwInsTable.setStatus("current")
_Pmlma10CtrlcaisDwInsEntry_Object = MibTableRow
pmlma10CtrlcaisDwInsEntry = _Pmlma10CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 22, 1)
)
pmlma10CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrlcaisDwInsEntry.setStatus("current")


class _Pmlma10CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pmlma10CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pmlma10CtrlcaisDwInsIndex_Object = MibTableColumn
pmlma10CtrlcaisDwInsIndex = _Pmlma10CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 22, 1, 1),
    _Pmlma10CtrlcaisDwInsIndex_Type()
)
pmlma10CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrlcaisDwInsIndex.setStatus("current")
_Pmlma10CtrlcaisDwInsPortn_Type = EkiState
_Pmlma10CtrlcaisDwInsPortn_Object = MibTableColumn
pmlma10CtrlcaisDwInsPortn = _Pmlma10CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 2, 22, 1, 2),
    _Pmlma10CtrlcaisDwInsPortn_Type()
)
pmlma10CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlcaisDwInsPortn.setStatus("current")
_Pmlma10CtrlLine_ObjectIdentity = ObjectIdentity
pmlma10CtrlLine = _Pmlma10CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3)
)
_Pmlma10CtrlcommAccessLoopTable_Object = MibTable
pmlma10CtrlcommAccessLoopTable = _Pmlma10CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pmlma10CtrlcommAccessLoopTable.setStatus("current")
_Pmlma10CtrlcommAccessLoopEntry_Object = MibTableRow
pmlma10CtrlcommAccessLoopEntry = _Pmlma10CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 64, 1)
)
pmlma10CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrlcommAccessLoopEntry.setStatus("current")


class _Pmlma10CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pmlma10CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pmlma10CtrlcommAccessLoopIndex_Object = MibTableColumn
pmlma10CtrlcommAccessLoopIndex = _Pmlma10CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 64, 1, 1),
    _Pmlma10CtrlcommAccessLoopIndex_Type()
)
pmlma10CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrlcommAccessLoopIndex.setStatus("current")
_Pmlma10CtrlcommAccessLoopPortn_Type = EkiState
_Pmlma10CtrlcommAccessLoopPortn_Object = MibTableColumn
pmlma10CtrlcommAccessLoopPortn = _Pmlma10CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 64, 1, 2),
    _Pmlma10CtrlcommAccessLoopPortn_Type()
)
pmlma10CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlcommAccessLoopPortn.setStatus("current")
_Pmlma10CtrllineLoopTable_Object = MibTable
pmlma10CtrllineLoopTable = _Pmlma10CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pmlma10CtrllineLoopTable.setStatus("current")
_Pmlma10CtrllineLoopEntry_Object = MibTableRow
pmlma10CtrllineLoopEntry = _Pmlma10CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 66, 1)
)
pmlma10CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrllineLoopEntry.setStatus("current")


class _Pmlma10CtrllineLoopIndex_Type(Integer32):
    """Custom type pmlma10CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pmlma10CtrllineLoopIndex_Object = MibTableColumn
pmlma10CtrllineLoopIndex = _Pmlma10CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 66, 1, 1),
    _Pmlma10CtrllineLoopIndex_Type()
)
pmlma10CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrllineLoopIndex.setStatus("current")
_Pmlma10CtrllineLoopPortn_Type = EkiState
_Pmlma10CtrllineLoopPortn_Object = MibTableColumn
pmlma10CtrllineLoopPortn = _Pmlma10CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 66, 1, 2),
    _Pmlma10CtrllineLoopPortn_Type()
)
pmlma10CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrllineLoopPortn.setStatus("current")
_Pmlma10CtrlfecDisableTable_Object = MibTable
pmlma10CtrlfecDisableTable = _Pmlma10CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pmlma10CtrlfecDisableTable.setStatus("current")
_Pmlma10CtrlfecDisableEntry_Object = MibTableRow
pmlma10CtrlfecDisableEntry = _Pmlma10CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 69, 1)
)
pmlma10CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CtrlfecDisableEntry.setStatus("current")


class _Pmlma10CtrlfecDisableIndex_Type(Integer32):
    """Custom type pmlma10CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pmlma10CtrlfecDisableIndex_Object = MibTableColumn
pmlma10CtrlfecDisableIndex = _Pmlma10CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 69, 1, 1),
    _Pmlma10CtrlfecDisableIndex_Type()
)
pmlma10CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CtrlfecDisableIndex.setStatus("current")
_Pmlma10CtrlfecDisablePortn_Type = EkiState
_Pmlma10CtrlfecDisablePortn_Object = MibTableColumn
pmlma10CtrlfecDisablePortn = _Pmlma10CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 6, 3, 69, 1, 2),
    _Pmlma10CtrlfecDisablePortn_Type()
)
pmlma10CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CtrlfecDisablePortn.setStatus("current")
_Pmlma10ri_ObjectIdentity = ObjectIdentity
pmlma10ri = _Pmlma10ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7)
)
_Pmlma10riTable_ObjectIdentity = ObjectIdentity
pmlma10riTable = _Pmlma10riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1)
)
_Pmlma10RinvSfpTable_Object = MibTable
pmlma10RinvSfpTable = _Pmlma10RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmlma10RinvSfpTable.setStatus("current")
_Pmlma10RinvSfpEntry_Object = MibTableRow
pmlma10RinvSfpEntry = _Pmlma10RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 1, 1)
)
pmlma10RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pmlma10RinvSfpEntry.setStatus("current")


class _Pmlma10RinvSfpIndex_Type(Integer32):
    """Custom type pmlma10RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmlma10RinvSfpIndex_Type.__name__ = "Integer32"
_Pmlma10RinvSfpIndex_Object = MibTableColumn
pmlma10RinvSfpIndex = _Pmlma10RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 1, 1, 1),
    _Pmlma10RinvSfpIndex_Type()
)
pmlma10RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvSfpIndex.setStatus("current")
_Pmlma10Rinvsfp_Type = DisplayString
_Pmlma10Rinvsfp_Object = MibTableColumn
pmlma10Rinvsfp = _Pmlma10Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 1, 1, 2),
    _Pmlma10Rinvsfp_Type()
)
pmlma10Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10Rinvsfp.setStatus("current")
_Pmlma10RinvLineTable_Object = MibTable
pmlma10RinvLineTable = _Pmlma10RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmlma10RinvLineTable.setStatus("current")
_Pmlma10RinvLineEntry_Object = MibTableRow
pmlma10RinvLineEntry = _Pmlma10RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 2, 1)
)
pmlma10RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmlma10RinvLineEntry.setStatus("current")


class _Pmlma10RinvLineIndex_Type(Integer32):
    """Custom type pmlma10RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmlma10RinvLineIndex_Type.__name__ = "Integer32"
_Pmlma10RinvLineIndex_Object = MibTableColumn
pmlma10RinvLineIndex = _Pmlma10RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 2, 1, 1),
    _Pmlma10RinvLineIndex_Type()
)
pmlma10RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvLineIndex.setStatus("current")
_Pmlma10RinvxfpLine_Type = DisplayString
_Pmlma10RinvxfpLine_Object = MibTableColumn
pmlma10RinvxfpLine = _Pmlma10RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 1, 2, 1, 2),
    _Pmlma10RinvxfpLine_Type()
)
pmlma10RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvxfpLine.setStatus("current")
_Pmlma10RinvReloadInventory_Type = EkiOnOff
_Pmlma10RinvReloadInventory_Object = MibScalar
pmlma10RinvReloadInventory = _Pmlma10RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 2),
    _Pmlma10RinvReloadInventory_Type()
)
pmlma10RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10RinvReloadInventory.setStatus("current")
_Pmlma10RinvHwPlatform_Type = DisplayString
_Pmlma10RinvHwPlatform_Object = MibScalar
pmlma10RinvHwPlatform = _Pmlma10RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 3),
    _Pmlma10RinvHwPlatform_Type()
)
pmlma10RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvHwPlatform.setStatus("current")
_Pmlma10RinvModulePlatform_Type = DisplayString
_Pmlma10RinvModulePlatform_Object = MibScalar
pmlma10RinvModulePlatform = _Pmlma10RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 4),
    _Pmlma10RinvModulePlatform_Type()
)
pmlma10RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvModulePlatform.setStatus("current")
_Pmlma10RinvSwPlatform_Type = DisplayString
_Pmlma10RinvSwPlatform_Object = MibScalar
pmlma10RinvSwPlatform = _Pmlma10RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 5),
    _Pmlma10RinvSwPlatform_Type()
)
pmlma10RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvSwPlatform.setStatus("current")
_Pmlma10RinvGwPlatform_Type = DisplayString
_Pmlma10RinvGwPlatform_Object = MibScalar
pmlma10RinvGwPlatform = _Pmlma10RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 7, 6),
    _Pmlma10RinvGwPlatform_Type()
)
pmlma10RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10RinvGwPlatform.setStatus("current")
_Pmlma10download_ObjectIdentity = ObjectIdentity
pmlma10download = _Pmlma10download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8)
)
_Pmlma10DwlOther_ObjectIdentity = ObjectIdentity
pmlma10DwlOther = _Pmlma10DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1)
)
_Pmlma10DwlrestartProcess_ObjectIdentity = ObjectIdentity
pmlma10DwlrestartProcess = _Pmlma10DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 0)
)
_Pmlma10DwlWarmRestartProcessed_Type = EkiOnOff
_Pmlma10DwlWarmRestartProcessed_Object = MibScalar
pmlma10DwlWarmRestartProcessed = _Pmlma10DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 0, 1),
    _Pmlma10DwlWarmRestartProcessed_Type()
)
pmlma10DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlWarmRestartProcessed.setStatus("current")
_Pmlma10DwlColdRestartProcessed_Type = EkiOnOff
_Pmlma10DwlColdRestartProcessed_Object = MibScalar
pmlma10DwlColdRestartProcessed = _Pmlma10DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 0, 2),
    _Pmlma10DwlColdRestartProcessed_Type()
)
pmlma10DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlColdRestartProcessed.setStatus("current")
_Pmlma10DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmlma10DwlswBanksUsed = _Pmlma10DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 1)
)
_Pmlma10DwlSwBank1Used_Type = EkiOnOff
_Pmlma10DwlSwBank1Used_Object = MibScalar
pmlma10DwlSwBank1Used = _Pmlma10DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 1, 1),
    _Pmlma10DwlSwBank1Used_Type()
)
pmlma10DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlSwBank1Used.setStatus("current")
_Pmlma10DwlSwBank2Used_Type = EkiOnOff
_Pmlma10DwlSwBank2Used_Object = MibScalar
pmlma10DwlSwBank2Used = _Pmlma10DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 1, 2),
    _Pmlma10DwlSwBank2Used_Type()
)
pmlma10DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlSwBank2Used.setStatus("current")
_Pmlma10DwlSwBank1Notempty_Type = EkiOnOff
_Pmlma10DwlSwBank1Notempty_Object = MibScalar
pmlma10DwlSwBank1Notempty = _Pmlma10DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 1, 5),
    _Pmlma10DwlSwBank1Notempty_Type()
)
pmlma10DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlSwBank1Notempty.setStatus("current")
_Pmlma10DwlSwBank2Notempty_Type = EkiOnOff
_Pmlma10DwlSwBank2Notempty_Object = MibScalar
pmlma10DwlSwBank2Notempty = _Pmlma10DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 1, 6),
    _Pmlma10DwlSwBank2Notempty_Type()
)
pmlma10DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlSwBank2Notempty.setStatus("current")
_Pmlma10DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmlma10DwlgwBanksUsed = _Pmlma10DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2)
)
_Pmlma10DwlGwBank1Used_Type = EkiOnOff
_Pmlma10DwlGwBank1Used_Object = MibScalar
pmlma10DwlGwBank1Used = _Pmlma10DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 1),
    _Pmlma10DwlGwBank1Used_Type()
)
pmlma10DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank1Used.setStatus("current")
_Pmlma10DwlGwBank2Used_Type = EkiOnOff
_Pmlma10DwlGwBank2Used_Object = MibScalar
pmlma10DwlGwBank2Used = _Pmlma10DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 2),
    _Pmlma10DwlGwBank2Used_Type()
)
pmlma10DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank2Used.setStatus("current")
_Pmlma10DwlGwBank3Used_Type = EkiOnOff
_Pmlma10DwlGwBank3Used_Object = MibScalar
pmlma10DwlGwBank3Used = _Pmlma10DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 3),
    _Pmlma10DwlGwBank3Used_Type()
)
pmlma10DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank3Used.setStatus("current")
_Pmlma10DwlGwBank4Used_Type = EkiOnOff
_Pmlma10DwlGwBank4Used_Object = MibScalar
pmlma10DwlGwBank4Used = _Pmlma10DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 4),
    _Pmlma10DwlGwBank4Used_Type()
)
pmlma10DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank4Used.setStatus("current")
_Pmlma10DwlGwBank1Notempty_Type = EkiOnOff
_Pmlma10DwlGwBank1Notempty_Object = MibScalar
pmlma10DwlGwBank1Notempty = _Pmlma10DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 5),
    _Pmlma10DwlGwBank1Notempty_Type()
)
pmlma10DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank1Notempty.setStatus("current")
_Pmlma10DwlGwBank2Notempty_Type = EkiOnOff
_Pmlma10DwlGwBank2Notempty_Object = MibScalar
pmlma10DwlGwBank2Notempty = _Pmlma10DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 6),
    _Pmlma10DwlGwBank2Notempty_Type()
)
pmlma10DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank2Notempty.setStatus("current")
_Pmlma10DwlGwBank3Notempty_Type = EkiOnOff
_Pmlma10DwlGwBank3Notempty_Object = MibScalar
pmlma10DwlGwBank3Notempty = _Pmlma10DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 7),
    _Pmlma10DwlGwBank3Notempty_Type()
)
pmlma10DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank3Notempty.setStatus("current")
_Pmlma10DwlGwBank4Notempty_Type = EkiOnOff
_Pmlma10DwlGwBank4Notempty_Object = MibScalar
pmlma10DwlGwBank4Notempty = _Pmlma10DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 1, 2, 8),
    _Pmlma10DwlGwBank4Notempty_Type()
)
pmlma10DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10DwlGwBank4Notempty.setStatus("current")
_Pmlma10DwlClient_ObjectIdentity = ObjectIdentity
pmlma10DwlClient = _Pmlma10DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 2)
)
_Pmlma10DwlLine_ObjectIdentity = ObjectIdentity
pmlma10DwlLine = _Pmlma10DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 8, 3)
)
_Pmlma10Config_ObjectIdentity = ObjectIdentity
pmlma10Config = _Pmlma10Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9)
)
_Pmlma10CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pmlma10CfgAccessCAisCsf = _Pmlma10CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 1)
)
_Pmlma10CfgClientcaiscsfTable_Object = MibTable
pmlma10CfgClientcaiscsfTable = _Pmlma10CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pmlma10CfgClientcaiscsfTable.setStatus("current")
_Pmlma10CfgClientcaiscsfEntry_Object = MibTableRow
pmlma10CfgClientcaiscsfEntry = _Pmlma10CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 1, 1, 1)
)
pmlma10CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgClientcaiscsfEntry.setStatus("current")


class _Pmlma10CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pmlma10CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pmlma10CfgClientcaiscsfIndex_Object = MibTableColumn
pmlma10CfgClientcaiscsfIndex = _Pmlma10CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 1, 1, 1, 1),
    _Pmlma10CfgClientcaiscsfIndex_Type()
)
pmlma10CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgClientcaiscsfIndex.setStatus("current")


class _Pmlma10CfgReservePortn_Type(Unsigned32):
    """Custom type pmlma10CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgReservePortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgReservePortn_Object = MibTableColumn
pmlma10CfgReservePortn = _Pmlma10CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 1, 1, 1, 3),
    _Pmlma10CfgReservePortn_Type()
)
pmlma10CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgReservePortn.setStatus("current")
_Pmlma10CfgStartup_ObjectIdentity = ObjectIdentity
pmlma10CfgStartup = _Pmlma10CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2)
)
_Pmlma10CfgClientStartupTable_Object = MibTable
pmlma10CfgClientStartupTable = _Pmlma10CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmlma10CfgClientStartupTable.setStatus("current")
_Pmlma10CfgClientStartupEntry_Object = MibTableRow
pmlma10CfgClientStartupEntry = _Pmlma10CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 1, 1)
)
pmlma10CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgClientStartupEntry.setStatus("current")


class _Pmlma10CfgClientStartupIndex_Type(Integer32):
    """Custom type pmlma10CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pmlma10CfgClientStartupIndex_Object = MibTableColumn
pmlma10CfgClientStartupIndex = _Pmlma10CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 1, 1, 1),
    _Pmlma10CfgClientStartupIndex_Type()
)
pmlma10CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgClientStartupIndex.setStatus("current")


class _Pmlma10CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pmlma10CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgSystConfPortPortn_Object = MibTableColumn
pmlma10CfgSystConfPortPortn = _Pmlma10CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 1, 1, 3),
    _Pmlma10CfgSystConfPortPortn_Type()
)
pmlma10CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgSystConfPortPortn.setStatus("current")


class _Pmlma10CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pmlma10CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgNetConfPortPortn_Object = MibTableColumn
pmlma10CfgNetConfPortPortn = _Pmlma10CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 1, 1, 4),
    _Pmlma10CfgNetConfPortPortn_Type()
)
pmlma10CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgNetConfPortPortn.setStatus("current")


class _Pmlma10CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pmlma10CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgOptionsPortPortn_Object = MibTableColumn
pmlma10CfgOptionsPortPortn = _Pmlma10CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 1, 1, 14),
    _Pmlma10CfgOptionsPortPortn_Type()
)
pmlma10CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgOptionsPortPortn.setStatus("current")
_Pmlma10CfgLinexr1StartupTable_Object = MibTable
pmlma10CfgLinexr1StartupTable = _Pmlma10CfgLinexr1StartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pmlma10CfgLinexr1StartupTable.setStatus("current")
_Pmlma10CfgLinexr1StartupEntry_Object = MibTableRow
pmlma10CfgLinexr1StartupEntry = _Pmlma10CfgLinexr1StartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 2, 1)
)
pmlma10CfgLinexr1StartupEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgLinexr1StartupIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgLinexr1StartupEntry.setStatus("current")


class _Pmlma10CfgLinexr1StartupIndex_Type(Integer32):
    """Custom type pmlma10CfgLinexr1StartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgLinexr1StartupIndex_Type.__name__ = "Integer32"
_Pmlma10CfgLinexr1StartupIndex_Object = MibTableColumn
pmlma10CfgLinexr1StartupIndex = _Pmlma10CfgLinexr1StartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 2, 1, 1),
    _Pmlma10CfgLinexr1StartupIndex_Type()
)
pmlma10CfgLinexr1StartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgLinexr1StartupIndex.setStatus("current")


class _Pmlma10CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pmlma10CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgSystConfLinePortn_Object = MibTableColumn
pmlma10CfgSystConfLinePortn = _Pmlma10CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 2, 1, 3),
    _Pmlma10CfgSystConfLinePortn_Type()
)
pmlma10CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgSystConfLinePortn.setStatus("current")


class _Pmlma10CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pmlma10CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgOptionsLinePortn_Object = MibTableColumn
pmlma10CfgOptionsLinePortn = _Pmlma10CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 2, 1, 14),
    _Pmlma10CfgOptionsLinePortn_Type()
)
pmlma10CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgOptionsLinePortn.setStatus("current")
_Pmlma10CfgEmptyTable_Object = MibTable
pmlma10CfgEmptyTable = _Pmlma10CfgEmptyTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pmlma10CfgEmptyTable.setStatus("current")
_Pmlma10CfgEmptyEntry_Object = MibTableRow
pmlma10CfgEmptyEntry = _Pmlma10CfgEmptyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 3, 1)
)
pmlma10CfgEmptyEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgEmptyIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgEmptyEntry.setStatus("current")


class _Pmlma10CfgEmptyIndex_Type(Integer32):
    """Custom type pmlma10CfgEmptyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgEmptyIndex_Type.__name__ = "Integer32"
_Pmlma10CfgEmptyIndex_Object = MibTableColumn
pmlma10CfgEmptyIndex = _Pmlma10CfgEmptyIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 3, 1, 1),
    _Pmlma10CfgEmptyIndex_Type()
)
pmlma10CfgEmptyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgEmptyIndex.setStatus("current")


class _Pmlma10CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pmlma10CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgSystConfMsaLinePortn_Object = MibTableColumn
pmlma10CfgSystConfMsaLinePortn = _Pmlma10CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 2, 3, 1, 3),
    _Pmlma10CfgSystConfMsaLinePortn_Type()
)
pmlma10CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgSystConfMsaLinePortn.setStatus("current")
_Pmlma10CfgLabels_ObjectIdentity = ObjectIdentity
pmlma10CfgLabels = _Pmlma10CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3)
)
_Pmlma10CfgLabelclientTable_Object = MibTable
pmlma10CfgLabelclientTable = _Pmlma10CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmlma10CfgLabelclientTable.setStatus("current")
_Pmlma10CfgLabelclientEntry_Object = MibTableRow
pmlma10CfgLabelclientEntry = _Pmlma10CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 1, 1)
)
pmlma10CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgLabelclientEntry.setStatus("current")


class _Pmlma10CfgLabelclientIndex_Type(Integer32):
    """Custom type pmlma10CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmlma10CfgLabelclientIndex_Object = MibTableColumn
pmlma10CfgLabelclientIndex = _Pmlma10CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 1, 1, 1),
    _Pmlma10CfgLabelclientIndex_Type()
)
pmlma10CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgLabelclientIndex.setStatus("current")


class _Pmlma10CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmlma10CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmlma10CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmlma10CfgLabelclientPortn_Object = MibTableColumn
pmlma10CfgLabelclientPortn = _Pmlma10CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 1, 1, 3),
    _Pmlma10CfgLabelclientPortn_Type()
)
pmlma10CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgLabelclientPortn.setStatus("current")
_Pmlma10CfgLabellineTable_Object = MibTable
pmlma10CfgLabellineTable = _Pmlma10CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmlma10CfgLabellineTable.setStatus("current")
_Pmlma10CfgLabellineEntry_Object = MibTableRow
pmlma10CfgLabellineEntry = _Pmlma10CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 2, 1)
)
pmlma10CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgLabellineEntry.setStatus("current")


class _Pmlma10CfgLabellineIndex_Type(Integer32):
    """Custom type pmlma10CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmlma10CfgLabellineIndex_Object = MibTableColumn
pmlma10CfgLabellineIndex = _Pmlma10CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 2, 1, 1),
    _Pmlma10CfgLabellineIndex_Type()
)
pmlma10CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgLabellineIndex.setStatus("current")


class _Pmlma10CfgLabellinePortn_Type(DisplayString):
    """Custom type pmlma10CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmlma10CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmlma10CfgLabellinePortn_Object = MibTableColumn
pmlma10CfgLabellinePortn = _Pmlma10CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 3, 2, 1, 3),
    _Pmlma10CfgLabellinePortn_Type()
)
pmlma10CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgLabellinePortn.setStatus("current")
_Pmlma10CfgStartuptlh_ObjectIdentity = ObjectIdentity
pmlma10CfgStartuptlh = _Pmlma10CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4)
)
_Pmlma10CfgOtxtlhTable_Object = MibTable
pmlma10CfgOtxtlhTable = _Pmlma10CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pmlma10CfgOtxtlhTable.setStatus("current")
_Pmlma10CfgOtxtlhEntry_Object = MibTableRow
pmlma10CfgOtxtlhEntry = _Pmlma10CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1)
)
pmlma10CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgOtxtlhEntry.setStatus("current")


class _Pmlma10CfgOtxtlhIndex_Type(Integer32):
    """Custom type pmlma10CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pmlma10CfgOtxtlhIndex_Object = MibTableColumn
pmlma10CfgOtxtlhIndex = _Pmlma10CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1, 1),
    _Pmlma10CfgOtxtlhIndex_Type()
)
pmlma10CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgOtxtlhIndex.setStatus("current")


class _Pmlma10CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pmlma10CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgLinePwrLaserPortn_Object = MibTableColumn
pmlma10CfgLinePwrLaserPortn = _Pmlma10CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1, 6),
    _Pmlma10CfgLinePwrLaserPortn_Type()
)
pmlma10CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgLinePwrLaserPortn.setStatus("current")


class _Pmlma10CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmlma10CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgLineFCurrentPortn_Object = MibTableColumn
pmlma10CfgLineFCurrentPortn = _Pmlma10CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1, 7),
    _Pmlma10CfgLineFCurrentPortn_Type()
)
pmlma10CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgLineFCurrentPortn.setStatus("current")


class _Pmlma10CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pmlma10CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgLineGridCurrentPortn_Object = MibTableColumn
pmlma10CfgLineGridCurrentPortn = _Pmlma10CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1, 8),
    _Pmlma10CfgLineGridCurrentPortn_Type()
)
pmlma10CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgLineGridCurrentPortn.setStatus("current")


class _Pmlma10CfgFPortn_Type(Unsigned32):
    """Custom type pmlma10CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgFPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgFPortn_Object = MibTableColumn
pmlma10CfgFPortn = _Pmlma10CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1, 9),
    _Pmlma10CfgFPortn_Type()
)
pmlma10CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgFPortn.setStatus("current")


class _Pmlma10CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmlma10CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgRxLineFCurrentPortn_Object = MibTableColumn
pmlma10CfgRxLineFCurrentPortn = _Pmlma10CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 4, 1, 1, 10),
    _Pmlma10CfgRxLineFCurrentPortn_Type()
)
pmlma10CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgRxLineFCurrentPortn.setStatus("current")
_Pmlma10CfgOther_ObjectIdentity = ObjectIdentity
pmlma10CfgOther = _Pmlma10CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 5)
)
_Pmlma10tablemoduleOther_ObjectIdentity = ObjectIdentity
pmlma10tablemoduleOther = _Pmlma10tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 5, 1)
)


class _Pmlma10Cfgmode_Type(Unsigned32):
    """Custom type pmlma10Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10Cfgmode_Type.__name__ = "Unsigned32"
_Pmlma10Cfgmode_Object = MibScalar
pmlma10Cfgmode = _Pmlma10Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 5, 1, 2),
    _Pmlma10Cfgmode_Type()
)
pmlma10Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10Cfgmode.setStatus("current")
_Pmlma10CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pmlma10CfgStartuptablefive = _Pmlma10CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6)
)
_Pmlma10CfgOtxtlhcapabilitiesTable_Object = MibTable
pmlma10CfgOtxtlhcapabilitiesTable = _Pmlma10CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pmlma10CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pmlma10CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pmlma10CfgOtxtlhcapabilitiesEntry = _Pmlma10CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1)
)
pmlma10CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pmlma10CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pmlma10CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pmlma10CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pmlma10CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pmlma10CfgOtxtlhcapabilitiesIndex = _Pmlma10CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1, 1),
    _Pmlma10CfgOtxtlhcapabilitiesIndex_Type()
)
pmlma10CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pmlma10CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pmlma10CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgComponentTypePortn_Object = MibTableColumn
pmlma10CfgComponentTypePortn = _Pmlma10CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1, 3),
    _Pmlma10CfgComponentTypePortn_Type()
)
pmlma10CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgComponentTypePortn.setStatus("current")


class _Pmlma10CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pmlma10CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgMiscellaneousPortn_Object = MibTableColumn
pmlma10CfgMiscellaneousPortn = _Pmlma10CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1, 4),
    _Pmlma10CfgMiscellaneousPortn_Type()
)
pmlma10CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgMiscellaneousPortn.setStatus("current")


class _Pmlma10CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pmlma10CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgFirstChannelPortn_Object = MibTableColumn
pmlma10CfgFirstChannelPortn = _Pmlma10CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1, 5),
    _Pmlma10CfgFirstChannelPortn_Type()
)
pmlma10CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgFirstChannelPortn.setStatus("current")


class _Pmlma10CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pmlma10CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgLastChannelPortn_Object = MibTableColumn
pmlma10CfgLastChannelPortn = _Pmlma10CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1, 6),
    _Pmlma10CfgLastChannelPortn_Type()
)
pmlma10CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgLastChannelPortn.setStatus("current")


class _Pmlma10CfgGridPortn_Type(Unsigned32):
    """Custom type pmlma10CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmlma10CfgGridPortn_Type.__name__ = "Unsigned32"
_Pmlma10CfgGridPortn_Object = MibTableColumn
pmlma10CfgGridPortn = _Pmlma10CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 6, 1, 1, 7),
    _Pmlma10CfgGridPortn_Type()
)
pmlma10CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10CfgGridPortn.setStatus("current")
_Pmlma10CfgWriteConfiguration_Type = EkiOnOff
_Pmlma10CfgWriteConfiguration_Object = MibScalar
pmlma10CfgWriteConfiguration = _Pmlma10CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 9, 257),
    _Pmlma10CfgWriteConfiguration_Type()
)
pmlma10CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10CfgWriteConfiguration.setStatus("current")
_Pmlma10traps_ObjectIdentity = ObjectIdentity
pmlma10traps = _Pmlma10traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10)
)


class _Pmlma10trapPortNumber_Type(Integer32):
    """Custom type pmlma10trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmlma10trapPortNumber_Type.__name__ = "Integer32"
_Pmlma10trapPortNumber_Object = MibScalar
pmlma10trapPortNumber = _Pmlma10trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 2),
    _Pmlma10trapPortNumber_Type()
)
pmlma10trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10trapPortNumber.setStatus("current")


class _Pmlma10trapLineNumber_Type(Integer32):
    """Custom type pmlma10trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmlma10trapLineNumber_Type.__name__ = "Integer32"
_Pmlma10trapLineNumber_Object = MibScalar
pmlma10trapLineNumber = _Pmlma10trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 3),
    _Pmlma10trapLineNumber_Type()
)
pmlma10trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10trapLineNumber.setStatus("current")


class _Pmlma10trapBoardNumber_Type(Integer32):
    """Custom type pmlma10trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmlma10trapBoardNumber_Type.__name__ = "Integer32"
_Pmlma10trapBoardNumber_Object = MibScalar
pmlma10trapBoardNumber = _Pmlma10trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 4),
    _Pmlma10trapBoardNumber_Type()
)
pmlma10trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10trapBoardNumber.setStatus("current")
_Pmlma10Monitoring_ObjectIdentity = ObjectIdentity
pmlma10Monitoring = _Pmlma10Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11)
)
_Pmlma10MonOther_ObjectIdentity = ObjectIdentity
pmlma10MonOther = _Pmlma10MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 1)
)
_Pmlma10MonRmon_ObjectIdentity = ObjectIdentity
pmlma10MonRmon = _Pmlma10MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 1, 3)
)
_Pmlma10MonCountersReset_Type = EkiOnOff
_Pmlma10MonCountersReset_Object = MibScalar
pmlma10MonCountersReset = _Pmlma10MonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 1, 3, 359),
    _Pmlma10MonCountersReset_Type()
)
pmlma10MonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10MonCountersReset.setStatus("current")
_Pmlma10MonCountersStop_Type = EkiOnOff
_Pmlma10MonCountersStop_Object = MibScalar
pmlma10MonCountersStop = _Pmlma10MonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 1, 3, 360),
    _Pmlma10MonCountersStop_Type()
)
pmlma10MonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmlma10MonCountersStop.setStatus("current")
_Pmlma10MonClient_ObjectIdentity = ObjectIdentity
pmlma10MonClient = _Pmlma10MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2)
)
_Pmlma10MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pmlma10MonClientRmonCounter = _Pmlma10MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4)
)
_Pmlma10MonupRmonBytesCounterClientInputTable_Object = MibTable
pmlma10MonupRmonBytesCounterClientInputTable = _Pmlma10MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonBytesCounterClientInputTable.setStatus("current")
_Pmlma10MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pmlma10MonupRmonBytesCounterClientInputEntry = _Pmlma10MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 16, 1)
)
pmlma10MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pmlma10MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pmlma10MonupRmonBytesCounterClientInputIndex = _Pmlma10MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 16, 1, 1),
    _Pmlma10MonupRmonBytesCounterClientInputIndex_Type()
)
pmlma10MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pmlma10MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pmlma10MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MonupRmonBytesCounterClientInputValuePortn = _Pmlma10MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 16, 1, 2),
    _Pmlma10MonupRmonBytesCounterClientInputValuePortn_Type()
)
pmlma10MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pmlma10MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MonupRmonBytesCounterClientInputErrorPortn = _Pmlma10MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 16, 1, 3),
    _Pmlma10MonupRmonBytesCounterClientInputErrorPortn_Type()
)
pmlma10MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MonupRmonBytesCounterClientInputOverloadPortn = _Pmlma10MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 16, 1, 4),
    _Pmlma10MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pmlma10MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pmlma10MonupRmonCrcErrorsCounterClientInputTable = _Pmlma10MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pmlma10MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pmlma10MonupRmonCrcErrorsCounterClientInputEntry = _Pmlma10MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 32, 1)
)
pmlma10MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pmlma10MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pmlma10MonupRmonCrcErrorsCounterClientInputIndex = _Pmlma10MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 32, 1, 1),
    _Pmlma10MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pmlma10MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn = _Pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 32, 1, 2),
    _Pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn = _Pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 32, 1, 3),
    _Pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 32, 1, 4),
    _Pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MonupRmonPacketsCounterClientInputTable_Object = MibTable
pmlma10MonupRmonPacketsCounterClientInputTable = _Pmlma10MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pmlma10MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pmlma10MonupRmonPacketsCounterClientInputEntry = _Pmlma10MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 48, 1)
)
pmlma10MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pmlma10MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pmlma10MonupRmonPacketsCounterClientInputIndex = _Pmlma10MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 48, 1, 1),
    _Pmlma10MonupRmonPacketsCounterClientInputIndex_Type()
)
pmlma10MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pmlma10MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pmlma10MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MonupRmonPacketsCounterClientInputValuePortn = _Pmlma10MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 48, 1, 2),
    _Pmlma10MonupRmonPacketsCounterClientInputValuePortn_Type()
)
pmlma10MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pmlma10MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MonupRmonPacketsCounterClientInputErrorPortn = _Pmlma10MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 48, 1, 3),
    _Pmlma10MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pmlma10MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MonupRmonPacketsCounterClientInputOverloadPortn = _Pmlma10MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 48, 1, 4),
    _Pmlma10MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pmlma10MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MonupRmonBroadcastCounterClientInputTable_Object = MibTable
pmlma10MonupRmonBroadcastCounterClientInputTable = _Pmlma10MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 64)
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pmlma10MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pmlma10MonupRmonBroadcastCounterClientInputEntry = _Pmlma10MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 64, 1)
)
pmlma10MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pmlma10MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pmlma10MonupRmonBroadcastCounterClientInputIndex = _Pmlma10MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 64, 1, 1),
    _Pmlma10MonupRmonBroadcastCounterClientInputIndex_Type()
)
pmlma10MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pmlma10MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pmlma10MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MonupRmonBroadcastCounterClientInputValuePortn = _Pmlma10MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 64, 1, 2),
    _Pmlma10MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pmlma10MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pmlma10MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MonupRmonBroadcastCounterClientInputErrorPortn = _Pmlma10MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 64, 1, 3),
    _Pmlma10MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pmlma10MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn = _Pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 64, 1, 4),
    _Pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MonupRmonMulticastCounterClientInputTable_Object = MibTable
pmlma10MonupRmonMulticastCounterClientInputTable = _Pmlma10MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pmlma10MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pmlma10MonupRmonMulticastCounterClientInputEntry = _Pmlma10MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 80, 1)
)
pmlma10MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pmlma10MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pmlma10MonupRmonMulticastCounterClientInputIndex = _Pmlma10MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 80, 1, 1),
    _Pmlma10MonupRmonMulticastCounterClientInputIndex_Type()
)
pmlma10MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pmlma10MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pmlma10MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MonupRmonMulticastCounterClientInputValuePortn = _Pmlma10MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 80, 1, 2),
    _Pmlma10MonupRmonMulticastCounterClientInputValuePortn_Type()
)
pmlma10MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pmlma10MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MonupRmonMulticastCounterClientInputErrorPortn = _Pmlma10MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 80, 1, 3),
    _Pmlma10MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pmlma10MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MonupRmonMulticastCounterClientInputOverloadPortn = _Pmlma10MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 80, 1, 4),
    _Pmlma10MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pmlma10MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pmlma10MonupRmonPauseFrameCounterClientInputTable = _Pmlma10MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 96)
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pmlma10MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pmlma10MonupRmonPauseFrameCounterClientInputEntry = _Pmlma10MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 96, 1)
)
pmlma10MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pmlma10MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pmlma10MonupRmonPauseFrameCounterClientInputIndex = _Pmlma10MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 96, 1, 1),
    _Pmlma10MonupRmonPauseFrameCounterClientInputIndex_Type()
)
pmlma10MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pmlma10MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pmlma10MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MonupRmonPauseFrameCounterClientInputValuePortn = _Pmlma10MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 96, 1, 2),
    _Pmlma10MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pmlma10MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn = _Pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 96, 1, 3),
    _Pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn = _Pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 96, 1, 4),
    _Pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MondwRmonCrcErrorsCounterClientInputTable_Object = MibTable
pmlma10MondwRmonCrcErrorsCounterClientInputTable = _Pmlma10MondwRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 224)
)
if mibBuilder.loadTexts:
    pmlma10MondwRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pmlma10MondwRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pmlma10MondwRmonCrcErrorsCounterClientInputEntry = _Pmlma10MondwRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 224, 1)
)
pmlma10MondwRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MondwRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MondwRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pmlma10MondwRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MondwRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MondwRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MondwRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pmlma10MondwRmonCrcErrorsCounterClientInputIndex = _Pmlma10MondwRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 224, 1, 1),
    _Pmlma10MondwRmonCrcErrorsCounterClientInputIndex_Type()
)
pmlma10MondwRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn = _Pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 224, 1, 2),
    _Pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn = _Pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 224, 1, 3),
    _Pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn = _Pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 224, 1, 4),
    _Pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pmlma10MondwRmonPacketsCounterClientInputTable_Object = MibTable
pmlma10MondwRmonPacketsCounterClientInputTable = _Pmlma10MondwRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 240)
)
if mibBuilder.loadTexts:
    pmlma10MondwRmonPacketsCounterClientInputTable.setStatus("current")
_Pmlma10MondwRmonPacketsCounterClientInputEntry_Object = MibTableRow
pmlma10MondwRmonPacketsCounterClientInputEntry = _Pmlma10MondwRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 240, 1)
)
pmlma10MondwRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pmlma10-MIB", "pmlma10MondwRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pmlma10MondwRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pmlma10MondwRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pmlma10MondwRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmlma10MondwRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pmlma10MondwRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pmlma10MondwRmonPacketsCounterClientInputIndex = _Pmlma10MondwRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 240, 1, 1),
    _Pmlma10MondwRmonPacketsCounterClientInputIndex_Type()
)
pmlma10MondwRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonPacketsCounterClientInputIndex.setStatus("current")
_Pmlma10MondwRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pmlma10MondwRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pmlma10MondwRmonPacketsCounterClientInputValuePortn = _Pmlma10MondwRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 240, 1, 2),
    _Pmlma10MondwRmonPacketsCounterClientInputValuePortn_Type()
)
pmlma10MondwRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pmlma10MondwRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pmlma10MondwRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pmlma10MondwRmonPacketsCounterClientInputErrorPortn = _Pmlma10MondwRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 240, 1, 3),
    _Pmlma10MondwRmonPacketsCounterClientInputErrorPortn_Type()
)
pmlma10MondwRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pmlma10MondwRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pmlma10MondwRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pmlma10MondwRmonPacketsCounterClientInputOverloadPortn = _Pmlma10MondwRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 68, 11, 2, 4, 240, 1, 4),
    _Pmlma10MondwRmonPacketsCounterClientInputOverloadPortn_Type()
)
pmlma10MondwRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmlma10MondwRmonPacketsCounterClientInputOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pmlma10LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 30)
)
pmlma10LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineDdmWarningPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapLineNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmlma10LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 31)
)
pmlma10LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineDdmWarningPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapLineNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmlma10LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 32)
)
pmlma10LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineDdmAlmPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapLineNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmlma10LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 33)
)
pmlma10LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineDdmAlmPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapLineNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmlma10LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 34)
)
pmlma10LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineFailPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineHwFailPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapLineNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10LineTrapCritGoesOn.setStatus(
        "current"
    )

pmlma10LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 35)
)
pmlma10LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineFailPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10AlmLineHwFailPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapLineNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10LineTrapCritGoesOff.setStatus(
        "current"
    )

pmlma10ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 40)
)
pmlma10ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapPortNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmlma10ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 41)
)
pmlma10ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapPortNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmlma10ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 42)
)
pmlma10ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapPortNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmlma10ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 43)
)
pmlma10ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapPortNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmlma10ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 44)
)
pmlma10ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmFailAccPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10AlmHwFailAccPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapPortNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10ClientTrapCritGoesOn.setStatus(
        "current"
    )

pmlma10ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 45)
)
pmlma10ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmFailAccPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10AlmHwFailAccPortn"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapPortNumber"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10ClientTrapCritGoesOff.setStatus(
        "current"
    )

pmlma10PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 50)
)
pmlma10PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmDefFuseB"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10AlmDefFuseA"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmlma10PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 68, 10, 51)
)
pmlma10PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pmlma10-MIB", "pmlma10AlmDefFuseB"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10AlmDefFuseA"),
        ("EKINOPS-Pmlma10-MIB", "pmlma10trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmlma10PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pmlma10-MIB",
    **{"Pmlma10MultiRate": Pmlma10MultiRate,
       "Pmlma10OtxMode": Pmlma10OtxMode,
       "Pmlma10OtxGrid": Pmlma10OtxGrid,
       "Pmlma10AdjustValue": Pmlma10AdjustValue,
       "Pmlma10ClientProtocol": Pmlma10ClientProtocol,
       "Pmlma10ProtocolMode": Pmlma10ProtocolMode,
       "Pmlma10OtxChannel": Pmlma10OtxChannel,
       "Pmlma10OrxChannel": Pmlma10OrxChannel,
       "Pmlma10ClientIgnoreTimer": Pmlma10ClientIgnoreTimer,
       "Pmlma10DccMode": Pmlma10DccMode,
       "modulePmlma10": modulePmlma10,
       "pmlma10alarms": pmlma10alarms,
       "pmlma10AlmOther": pmlma10AlmOther,
       "pmlma10AlmOtherNurg": pmlma10AlmOtherNurg,
       "pmlma10AlmsynthAlm2": pmlma10AlmsynthAlm2,
       "pmlma10AlmConfTableSave": pmlma10AlmConfTableSave,
       "pmlma10AlmInvUpload": pmlma10AlmInvUpload,
       "pmlma10AlmConfTableLoad": pmlma10AlmConfTableLoad,
       "pmlma10AlmCorrelatOff": pmlma10AlmCorrelatOff,
       "pmlma10AlmOtherUrg": pmlma10AlmOtherUrg,
       "pmlma10AlmOtherCrit": pmlma10AlmOtherCrit,
       "pmlma10AlmsynthAlm0": pmlma10AlmsynthAlm0,
       "pmlma10AlmModGlobFail": pmlma10AlmModGlobFail,
       "pmlma10AlmDefFuseA": pmlma10AlmDefFuseA,
       "pmlma10AlmDefFuseB": pmlma10AlmDefFuseB,
       "pmlma10AlmClient": pmlma10AlmClient,
       "pmlma10AlmClientNurg": pmlma10AlmClientNurg,
       "pmlma10AlmclientSfpWarnDdmTable": pmlma10AlmclientSfpWarnDdmTable,
       "pmlma10AlmclientSfpWarnDdmEntry": pmlma10AlmclientSfpWarnDdmEntry,
       "pmlma10AlmclientSfpWarnDdmIndex": pmlma10AlmclientSfpWarnDdmIndex,
       "pmlma10AlmClientTxPwLowWngPortn": pmlma10AlmClientTxPwLowWngPortn,
       "pmlma10AlmClientTxPwrHighWngPortn": pmlma10AlmClientTxPwrHighWngPortn,
       "pmlma10AlmClientTxBiasLowWngPortn": pmlma10AlmClientTxBiasLowWngPortn,
       "pmlma10AlmClientTxBiasHighWngPortn": pmlma10AlmClientTxBiasHighWngPortn,
       "pmlma10AlmClientVccLowWngPortn": pmlma10AlmClientVccLowWngPortn,
       "pmlma10AlmClientVccHighWngPortn": pmlma10AlmClientVccHighWngPortn,
       "pmlma10AlmClientTempLowWngPortn": pmlma10AlmClientTempLowWngPortn,
       "pmlma10AlmClientTempHighWngPortn": pmlma10AlmClientTempHighWngPortn,
       "pmlma10AlmClientRxPwrLowWngPortn": pmlma10AlmClientRxPwrLowWngPortn,
       "pmlma10AlmClientRxPwrHighWngPortn": pmlma10AlmClientRxPwrHighWngPortn,
       "pmlma10AlmClientUrg": pmlma10AlmClientUrg,
       "pmlma10AlmclientHostLaneFaultTable": pmlma10AlmclientHostLaneFaultTable,
       "pmlma10AlmclientHostLaneFaultEntry": pmlma10AlmclientHostLaneFaultEntry,
       "pmlma10AlmclientHostLaneFaultIndex": pmlma10AlmclientHostLaneFaultIndex,
       "pmlma10AlmClientLossOfSyncPortn": pmlma10AlmClientLossOfSyncPortn,
       "pmlma10AlmClientInputLossOfSigPortn": pmlma10AlmClientInputLossOfSigPortn,
       "pmlma10AlmClientCsfDetectedPortn": pmlma10AlmClientCsfDetectedPortn,
       "pmlma10AlmClientLaneTxFifoErrorPortn": pmlma10AlmClientLaneTxFifoErrorPortn,
       "pmlma10AlmclientSfpAlmDdmTable": pmlma10AlmclientSfpAlmDdmTable,
       "pmlma10AlmclientSfpAlmDdmEntry": pmlma10AlmclientSfpAlmDdmEntry,
       "pmlma10AlmclientSfpAlmDdmIndex": pmlma10AlmclientSfpAlmDdmIndex,
       "pmlma10AlmClientTxPwrLowAlaPortn": pmlma10AlmClientTxPwrLowAlaPortn,
       "pmlma10AlmClientTxPwrHighAlaPortn": pmlma10AlmClientTxPwrHighAlaPortn,
       "pmlma10AlmClientTxBiasLowAlaPortn": pmlma10AlmClientTxBiasLowAlaPortn,
       "pmlma10AlmClientTxBiasHighAlaPortn": pmlma10AlmClientTxBiasHighAlaPortn,
       "pmlma10AlmClientVccLowAlaPortn": pmlma10AlmClientVccLowAlaPortn,
       "pmlma10AlmClientVccHighAlaPortn": pmlma10AlmClientVccHighAlaPortn,
       "pmlma10AlmClientTempLowAlaPortn": pmlma10AlmClientTempLowAlaPortn,
       "pmlma10AlmClientTempHighAlaPortn": pmlma10AlmClientTempHighAlaPortn,
       "pmlma10AlmClientRxPwrLowAlaPortn": pmlma10AlmClientRxPwrLowAlaPortn,
       "pmlma10AlmClientRxPwrHighAlaPortn": pmlma10AlmClientRxPwrHighAlaPortn,
       "pmlma10AlmClientCrit": pmlma10AlmClientCrit,
       "pmlma10AlmsynthAlmPortTable": pmlma10AlmsynthAlmPortTable,
       "pmlma10AlmsynthAlmPortEntry": pmlma10AlmsynthAlmPortEntry,
       "pmlma10AlmsynthAlmPortIndex": pmlma10AlmsynthAlmPortIndex,
       "pmlma10AlmSfpAbsentPortn": pmlma10AlmSfpAbsentPortn,
       "pmlma10AlmDdmAbsentPortn": pmlma10AlmDdmAbsentPortn,
       "pmlma10AlmHwFailAccPortn": pmlma10AlmHwFailAccPortn,
       "pmlma10AlmDwLsdPortn": pmlma10AlmDwLsdPortn,
       "pmlma10AlmClientLocalOosPortn": pmlma10AlmClientLocalOosPortn,
       "pmlma10AlmClientRemoteOosPortn": pmlma10AlmClientRemoteOosPortn,
       "pmlma10AlmDwCaisPortn": pmlma10AlmDwCaisPortn,
       "pmlma10AlmSfpDdmWarningPortn": pmlma10AlmSfpDdmWarningPortn,
       "pmlma10AlmSfpDdmAlmPortn": pmlma10AlmSfpDdmAlmPortn,
       "pmlma10AlmFailAccPortn": pmlma10AlmFailAccPortn,
       "pmlma10AlmUpCsfPortn": pmlma10AlmUpCsfPortn,
       "pmlma10AlmLine": pmlma10AlmLine,
       "pmlma10AlmLineNurg": pmlma10AlmLineNurg,
       "pmlma10AlmLineUrg": pmlma10AlmLineUrg,
       "pmlma10AlmlineNetworkLaneAlarmWarning1Table": pmlma10AlmlineNetworkLaneAlarmWarning1Table,
       "pmlma10AlmlineNetworkLaneAlarmWarning1Entry": pmlma10AlmlineNetworkLaneAlarmWarning1Entry,
       "pmlma10AlmlineNetworkLaneAlarmWarning1Index": pmlma10AlmlineNetworkLaneAlarmWarning1Index,
       "pmlma10AlmLineTxPwrLowAlaPortn": pmlma10AlmLineTxPwrLowAlaPortn,
       "pmlma10AlmLineTxPwrHighAlaPortn": pmlma10AlmLineTxPwrHighAlaPortn,
       "pmlma10AlmLineTxBiasLowAlaPortn": pmlma10AlmLineTxBiasLowAlaPortn,
       "pmlma10AlmLineTxBiasHighAlaPortn": pmlma10AlmLineTxBiasHighAlaPortn,
       "pmlma10AlmLineVccLowAlaPortn": pmlma10AlmLineVccLowAlaPortn,
       "pmlma10AlmLineVccHighAlaPortn": pmlma10AlmLineVccHighAlaPortn,
       "pmlma10AlmLineTempLowAlaPortn": pmlma10AlmLineTempLowAlaPortn,
       "pmlma10AlmLineTempHighAlaPortn": pmlma10AlmLineTempHighAlaPortn,
       "pmlma10AlmLineRxPwrLowAlaPortn": pmlma10AlmLineRxPwrLowAlaPortn,
       "pmlma10AlmLineRxPwrHighAlaPortn": pmlma10AlmLineRxPwrHighAlaPortn,
       "pmlma10AlmlineNetworkLaneAlarmWarning2Table": pmlma10AlmlineNetworkLaneAlarmWarning2Table,
       "pmlma10AlmlineNetworkLaneAlarmWarning2Entry": pmlma10AlmlineNetworkLaneAlarmWarning2Entry,
       "pmlma10AlmlineNetworkLaneAlarmWarning2Index": pmlma10AlmlineNetworkLaneAlarmWarning2Index,
       "pmlma10AlmLineTxPwLowWngPortn": pmlma10AlmLineTxPwLowWngPortn,
       "pmlma10AlmLineTxPwrHighWngPortn": pmlma10AlmLineTxPwrHighWngPortn,
       "pmlma10AlmLineTxBiasLowWngPortn": pmlma10AlmLineTxBiasLowWngPortn,
       "pmlma10AlmLineTxBiasHighWngPortn": pmlma10AlmLineTxBiasHighWngPortn,
       "pmlma10AlmLineVccLowWngPortn": pmlma10AlmLineVccLowWngPortn,
       "pmlma10AlmLineVccHighWngPortn": pmlma10AlmLineVccHighWngPortn,
       "pmlma10AlmLineTempLowWngPortn": pmlma10AlmLineTempLowWngPortn,
       "pmlma10AlmLineTempHighWngPortn": pmlma10AlmLineTempHighWngPortn,
       "pmlma10AlmLineRxPwrLowWngPortn": pmlma10AlmLineRxPwrLowWngPortn,
       "pmlma10AlmLineRxPwrHighWngPortn": pmlma10AlmLineRxPwrHighWngPortn,
       "pmlma10AlmlineHostLaneFaultTable": pmlma10AlmlineHostLaneFaultTable,
       "pmlma10AlmlineHostLaneFaultEntry": pmlma10AlmlineHostLaneFaultEntry,
       "pmlma10AlmlineHostLaneFaultIndex": pmlma10AlmlineHostLaneFaultIndex,
       "pmlma10AlmLineInputLossOfSignalPortn": pmlma10AlmLineInputLossOfSignalPortn,
       "pmlma10AlmLineLossOfFramePortn": pmlma10AlmLineLossOfFramePortn,
       "pmlma10AlmLineSmBdiInsertedPortn": pmlma10AlmLineSmBdiInsertedPortn,
       "pmlma10AlmLineSmBdiDetectedPortn": pmlma10AlmLineSmBdiDetectedPortn,
       "pmlma10AlmLineCrit": pmlma10AlmLineCrit,
       "pmlma10AlmsynthAlmLineTable": pmlma10AlmsynthAlmLineTable,
       "pmlma10AlmsynthAlmLineEntry": pmlma10AlmsynthAlmLineEntry,
       "pmlma10AlmsynthAlmLineIndex": pmlma10AlmsynthAlmLineIndex,
       "pmlma10AlmLineSfpAbsentPortn": pmlma10AlmLineSfpAbsentPortn,
       "pmlma10AlmLineDdmAbsentPortn": pmlma10AlmLineDdmAbsentPortn,
       "pmlma10AlmLineHwFailPortn": pmlma10AlmLineHwFailPortn,
       "pmlma10AlmLineTxOffPortn": pmlma10AlmLineTxOffPortn,
       "pmlma10AlmLineLocalOosPortn": pmlma10AlmLineLocalOosPortn,
       "pmlma10AlmUpRdiInsPortn": pmlma10AlmUpRdiInsPortn,
       "pmlma10AlmLineDdmWarningPortn": pmlma10AlmLineDdmWarningPortn,
       "pmlma10AlmLineDdmAlmPortn": pmlma10AlmLineDdmAlmPortn,
       "pmlma10AlmLineFailPortn": pmlma10AlmLineFailPortn,
       "pmlma10measures": pmlma10measures,
       "pmlma10MesrOther": pmlma10MesrOther,
       "pmlma10MesrClient": pmlma10MesrClient,
       "pmlma10MesrclientTempTable": pmlma10MesrclientTempTable,
       "pmlma10MesrclientTempEntry": pmlma10MesrclientTempEntry,
       "pmlma10MesrclientTempIndex": pmlma10MesrclientTempIndex,
       "pmlma10MesrclientTempPortn": pmlma10MesrclientTempPortn,
       "pmlma10MesrclientTxBiasTable": pmlma10MesrclientTxBiasTable,
       "pmlma10MesrclientTxBiasEntry": pmlma10MesrclientTxBiasEntry,
       "pmlma10MesrclientTxBiasIndex": pmlma10MesrclientTxBiasIndex,
       "pmlma10MesrclientTxBiasPortn": pmlma10MesrclientTxBiasPortn,
       "pmlma10MesrclientTxPwrTable": pmlma10MesrclientTxPwrTable,
       "pmlma10MesrclientTxPwrEntry": pmlma10MesrclientTxPwrEntry,
       "pmlma10MesrclientTxPwrIndex": pmlma10MesrclientTxPwrIndex,
       "pmlma10MesrclientTxPwrPortn": pmlma10MesrclientTxPwrPortn,
       "pmlma10MesrclientRxPwrTable": pmlma10MesrclientRxPwrTable,
       "pmlma10MesrclientRxPwrEntry": pmlma10MesrclientRxPwrEntry,
       "pmlma10MesrclientRxPwrIndex": pmlma10MesrclientRxPwrIndex,
       "pmlma10MesrclientRxPwrPortn": pmlma10MesrclientRxPwrPortn,
       "pmlma10MesrLine": pmlma10MesrLine,
       "pmlma10MesrlineTxPwrTable": pmlma10MesrlineTxPwrTable,
       "pmlma10MesrlineTxPwrEntry": pmlma10MesrlineTxPwrEntry,
       "pmlma10MesrlineTxPwrIndex": pmlma10MesrlineTxPwrIndex,
       "pmlma10MesrlineTxPwrPortn": pmlma10MesrlineTxPwrPortn,
       "pmlma10MesrlineTempTable": pmlma10MesrlineTempTable,
       "pmlma10MesrlineTempEntry": pmlma10MesrlineTempEntry,
       "pmlma10MesrlineTempIndex": pmlma10MesrlineTempIndex,
       "pmlma10MesrlineTempPortn": pmlma10MesrlineTempPortn,
       "pmlma10MesrlineTxBiasTable": pmlma10MesrlineTxBiasTable,
       "pmlma10MesrlineTxBiasEntry": pmlma10MesrlineTxBiasEntry,
       "pmlma10MesrlineTxBiasIndex": pmlma10MesrlineTxBiasIndex,
       "pmlma10MesrlineTxBiasPortn": pmlma10MesrlineTxBiasPortn,
       "pmlma10MesrlineRxPwrTable": pmlma10MesrlineRxPwrTable,
       "pmlma10MesrlineRxPwrEntry": pmlma10MesrlineRxPwrEntry,
       "pmlma10MesrlineRxPwrIndex": pmlma10MesrlineRxPwrIndex,
       "pmlma10MesrlineRxPwrPortn": pmlma10MesrlineRxPwrPortn,
       "pmlma10counters": pmlma10counters,
       "pmlma10CntOther": pmlma10CntOther,
       "pmlma10CntClient": pmlma10CntClient,
       "pmlma10CntclientCbipCounterTable": pmlma10CntclientCbipCounterTable,
       "pmlma10CntclientCbipCounterEntry": pmlma10CntclientCbipCounterEntry,
       "pmlma10CntclientCbipCounterIndex": pmlma10CntclientCbipCounterIndex,
       "pmlma10CntclientCbipCounterValuePortn": pmlma10CntclientCbipCounterValuePortn,
       "pmlma10CntclientCbipCounterErrorPortn": pmlma10CntclientCbipCounterErrorPortn,
       "pmlma10CntclientCbipCounterOverloadPortn": pmlma10CntclientCbipCounterOverloadPortn,
       "pmlma10CntLine": pmlma10CntLine,
       "pmlma10CntlocalLineSmBip8ErrorCounterTable": pmlma10CntlocalLineSmBip8ErrorCounterTable,
       "pmlma10CntlocalLineSmBip8ErrorCounterEntry": pmlma10CntlocalLineSmBip8ErrorCounterEntry,
       "pmlma10CntlocalLineSmBip8ErrorCounterIndex": pmlma10CntlocalLineSmBip8ErrorCounterIndex,
       "pmlma10CntlocalLineSmBip8ErrorCounterValuePortn": pmlma10CntlocalLineSmBip8ErrorCounterValuePortn,
       "pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn": pmlma10CntlocalLineSmBip8ErrorCounterErrorPortn,
       "pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn": pmlma10CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pmlma10CntlocalLineFecCorrectedErrorsCounterTable": pmlma10CntlocalLineFecCorrectedErrorsCounterTable,
       "pmlma10CntlocalLineFecCorrectedErrorsCounterEntry": pmlma10CntlocalLineFecCorrectedErrorsCounterEntry,
       "pmlma10CntlocalLineFecCorrectedErrorsCounterIndex": pmlma10CntlocalLineFecCorrectedErrorsCounterIndex,
       "pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn": pmlma10CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn": pmlma10CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn": pmlma10CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pmlma10CntremoteLineSmBip8ErrorCounterTable": pmlma10CntremoteLineSmBip8ErrorCounterTable,
       "pmlma10CntremoteLineSmBip8ErrorCounterEntry": pmlma10CntremoteLineSmBip8ErrorCounterEntry,
       "pmlma10CntremoteLineSmBip8ErrorCounterIndex": pmlma10CntremoteLineSmBip8ErrorCounterIndex,
       "pmlma10CntremoteLineSmBip8ErrorCounterValuePortn": pmlma10CntremoteLineSmBip8ErrorCounterValuePortn,
       "pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn": pmlma10CntremoteLineSmBip8ErrorCounterErrorPortn,
       "pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn": pmlma10CntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pmlma10CntlineDfrmTimCntTable": pmlma10CntlineDfrmTimCntTable,
       "pmlma10CntlineDfrmTimCntEntry": pmlma10CntlineDfrmTimCntEntry,
       "pmlma10CntlineDfrmTimCntIndex": pmlma10CntlineDfrmTimCntIndex,
       "pmlma10CntlineDfrmTimCntValuePortn": pmlma10CntlineDfrmTimCntValuePortn,
       "pmlma10CntlineDfrmTimCntErrorPortn": pmlma10CntlineDfrmTimCntErrorPortn,
       "pmlma10CntlineDfrmTimCntOverloadPortn": pmlma10CntlineDfrmTimCntOverloadPortn,
       "pmlma10CntCountersReset": pmlma10CntCountersReset,
       "pmlma10CntCountersStop": pmlma10CntCountersStop,
       "pmlma10controlsWrite": pmlma10controlsWrite,
       "pmlma10CtrlOther": pmlma10CtrlOther,
       "pmlma10CtrlconfMgnt1": pmlma10CtrlconfMgnt1,
       "pmlma10CtrlConf1Load1": pmlma10CtrlConf1Load1,
       "pmlma10CtrlConf2Load1": pmlma10CtrlConf2Load1,
       "pmlma10CtrlConf2Flash1": pmlma10CtrlConf2Flash1,
       "pmlma10CtrlConf2Clear1": pmlma10CtrlConf2Clear1,
       "pmlma10Ctrlsynth4": pmlma10Ctrlsynth4,
       "pmlma10CtrlCorrelatOn": pmlma10CtrlCorrelatOn,
       "pmlma10CtrlCorrelatOff": pmlma10CtrlCorrelatOff,
       "pmlma10CtrlswMgnt": pmlma10CtrlswMgnt,
       "pmlma10CtrlColdReset": pmlma10CtrlColdReset,
       "pmlma10CtrlWarmReset": pmlma10CtrlWarmReset,
       "pmlma10CtrlLoadSwBank1": pmlma10CtrlLoadSwBank1,
       "pmlma10CtrlLoadSwBank2": pmlma10CtrlLoadSwBank2,
       "pmlma10CtrlgwMgnt": pmlma10CtrlgwMgnt,
       "pmlma10CtrlCurrentGwReset": pmlma10CtrlCurrentGwReset,
       "pmlma10CtrlLoadGwBank1": pmlma10CtrlLoadGwBank1,
       "pmlma10CtrlLoadGwBank2": pmlma10CtrlLoadGwBank2,
       "pmlma10CtrlLoadGwBank3": pmlma10CtrlLoadGwBank3,
       "pmlma10CtrlLoadGwBank4": pmlma10CtrlLoadGwBank4,
       "pmlma10CtrlledTest": pmlma10CtrlledTest,
       "pmlma10CtrlGreenLed": pmlma10CtrlGreenLed,
       "pmlma10CtrlRedLed": pmlma10CtrlRedLed,
       "pmlma10CtrlLedOff": pmlma10CtrlLedOff,
       "pmlma10CtrlClient": pmlma10CtrlClient,
       "pmlma10CtrlaccessLoopTable": pmlma10CtrlaccessLoopTable,
       "pmlma10CtrlaccessLoopEntry": pmlma10CtrlaccessLoopEntry,
       "pmlma10CtrlaccessLoopIndex": pmlma10CtrlaccessLoopIndex,
       "pmlma10CtrlaccessLoopPortn": pmlma10CtrlaccessLoopPortn,
       "pmlma10CtrlclientLoopToLineTable": pmlma10CtrlclientLoopToLineTable,
       "pmlma10CtrlclientLoopToLineEntry": pmlma10CtrlclientLoopToLineEntry,
       "pmlma10CtrlclientLoopToLineIndex": pmlma10CtrlclientLoopToLineIndex,
       "pmlma10CtrlclientLoopToLinePortn": pmlma10CtrlclientLoopToLinePortn,
       "pmlma10CtrlcsfUpInsTable": pmlma10CtrlcsfUpInsTable,
       "pmlma10CtrlcsfUpInsEntry": pmlma10CtrlcsfUpInsEntry,
       "pmlma10CtrlcsfUpInsIndex": pmlma10CtrlcsfUpInsIndex,
       "pmlma10CtrlcsfUpInsPortn": pmlma10CtrlcsfUpInsPortn,
       "pmlma10CtrlcaisDwInsTable": pmlma10CtrlcaisDwInsTable,
       "pmlma10CtrlcaisDwInsEntry": pmlma10CtrlcaisDwInsEntry,
       "pmlma10CtrlcaisDwInsIndex": pmlma10CtrlcaisDwInsIndex,
       "pmlma10CtrlcaisDwInsPortn": pmlma10CtrlcaisDwInsPortn,
       "pmlma10CtrlLine": pmlma10CtrlLine,
       "pmlma10CtrlcommAccessLoopTable": pmlma10CtrlcommAccessLoopTable,
       "pmlma10CtrlcommAccessLoopEntry": pmlma10CtrlcommAccessLoopEntry,
       "pmlma10CtrlcommAccessLoopIndex": pmlma10CtrlcommAccessLoopIndex,
       "pmlma10CtrlcommAccessLoopPortn": pmlma10CtrlcommAccessLoopPortn,
       "pmlma10CtrllineLoopTable": pmlma10CtrllineLoopTable,
       "pmlma10CtrllineLoopEntry": pmlma10CtrllineLoopEntry,
       "pmlma10CtrllineLoopIndex": pmlma10CtrllineLoopIndex,
       "pmlma10CtrllineLoopPortn": pmlma10CtrllineLoopPortn,
       "pmlma10CtrlfecDisableTable": pmlma10CtrlfecDisableTable,
       "pmlma10CtrlfecDisableEntry": pmlma10CtrlfecDisableEntry,
       "pmlma10CtrlfecDisableIndex": pmlma10CtrlfecDisableIndex,
       "pmlma10CtrlfecDisablePortn": pmlma10CtrlfecDisablePortn,
       "pmlma10ri": pmlma10ri,
       "pmlma10riTable": pmlma10riTable,
       "pmlma10RinvSfpTable": pmlma10RinvSfpTable,
       "pmlma10RinvSfpEntry": pmlma10RinvSfpEntry,
       "pmlma10RinvSfpIndex": pmlma10RinvSfpIndex,
       "pmlma10Rinvsfp": pmlma10Rinvsfp,
       "pmlma10RinvLineTable": pmlma10RinvLineTable,
       "pmlma10RinvLineEntry": pmlma10RinvLineEntry,
       "pmlma10RinvLineIndex": pmlma10RinvLineIndex,
       "pmlma10RinvxfpLine": pmlma10RinvxfpLine,
       "pmlma10RinvReloadInventory": pmlma10RinvReloadInventory,
       "pmlma10RinvHwPlatform": pmlma10RinvHwPlatform,
       "pmlma10RinvModulePlatform": pmlma10RinvModulePlatform,
       "pmlma10RinvSwPlatform": pmlma10RinvSwPlatform,
       "pmlma10RinvGwPlatform": pmlma10RinvGwPlatform,
       "pmlma10download": pmlma10download,
       "pmlma10DwlOther": pmlma10DwlOther,
       "pmlma10DwlrestartProcess": pmlma10DwlrestartProcess,
       "pmlma10DwlWarmRestartProcessed": pmlma10DwlWarmRestartProcessed,
       "pmlma10DwlColdRestartProcessed": pmlma10DwlColdRestartProcessed,
       "pmlma10DwlswBanksUsed": pmlma10DwlswBanksUsed,
       "pmlma10DwlSwBank1Used": pmlma10DwlSwBank1Used,
       "pmlma10DwlSwBank2Used": pmlma10DwlSwBank2Used,
       "pmlma10DwlSwBank1Notempty": pmlma10DwlSwBank1Notempty,
       "pmlma10DwlSwBank2Notempty": pmlma10DwlSwBank2Notempty,
       "pmlma10DwlgwBanksUsed": pmlma10DwlgwBanksUsed,
       "pmlma10DwlGwBank1Used": pmlma10DwlGwBank1Used,
       "pmlma10DwlGwBank2Used": pmlma10DwlGwBank2Used,
       "pmlma10DwlGwBank3Used": pmlma10DwlGwBank3Used,
       "pmlma10DwlGwBank4Used": pmlma10DwlGwBank4Used,
       "pmlma10DwlGwBank1Notempty": pmlma10DwlGwBank1Notempty,
       "pmlma10DwlGwBank2Notempty": pmlma10DwlGwBank2Notempty,
       "pmlma10DwlGwBank3Notempty": pmlma10DwlGwBank3Notempty,
       "pmlma10DwlGwBank4Notempty": pmlma10DwlGwBank4Notempty,
       "pmlma10DwlClient": pmlma10DwlClient,
       "pmlma10DwlLine": pmlma10DwlLine,
       "pmlma10Config": pmlma10Config,
       "pmlma10CfgAccessCAisCsf": pmlma10CfgAccessCAisCsf,
       "pmlma10CfgClientcaiscsfTable": pmlma10CfgClientcaiscsfTable,
       "pmlma10CfgClientcaiscsfEntry": pmlma10CfgClientcaiscsfEntry,
       "pmlma10CfgClientcaiscsfIndex": pmlma10CfgClientcaiscsfIndex,
       "pmlma10CfgReservePortn": pmlma10CfgReservePortn,
       "pmlma10CfgStartup": pmlma10CfgStartup,
       "pmlma10CfgClientStartupTable": pmlma10CfgClientStartupTable,
       "pmlma10CfgClientStartupEntry": pmlma10CfgClientStartupEntry,
       "pmlma10CfgClientStartupIndex": pmlma10CfgClientStartupIndex,
       "pmlma10CfgSystConfPortPortn": pmlma10CfgSystConfPortPortn,
       "pmlma10CfgNetConfPortPortn": pmlma10CfgNetConfPortPortn,
       "pmlma10CfgOptionsPortPortn": pmlma10CfgOptionsPortPortn,
       "pmlma10CfgLinexr1StartupTable": pmlma10CfgLinexr1StartupTable,
       "pmlma10CfgLinexr1StartupEntry": pmlma10CfgLinexr1StartupEntry,
       "pmlma10CfgLinexr1StartupIndex": pmlma10CfgLinexr1StartupIndex,
       "pmlma10CfgSystConfLinePortn": pmlma10CfgSystConfLinePortn,
       "pmlma10CfgOptionsLinePortn": pmlma10CfgOptionsLinePortn,
       "pmlma10CfgEmptyTable": pmlma10CfgEmptyTable,
       "pmlma10CfgEmptyEntry": pmlma10CfgEmptyEntry,
       "pmlma10CfgEmptyIndex": pmlma10CfgEmptyIndex,
       "pmlma10CfgSystConfMsaLinePortn": pmlma10CfgSystConfMsaLinePortn,
       "pmlma10CfgLabels": pmlma10CfgLabels,
       "pmlma10CfgLabelclientTable": pmlma10CfgLabelclientTable,
       "pmlma10CfgLabelclientEntry": pmlma10CfgLabelclientEntry,
       "pmlma10CfgLabelclientIndex": pmlma10CfgLabelclientIndex,
       "pmlma10CfgLabelclientPortn": pmlma10CfgLabelclientPortn,
       "pmlma10CfgLabellineTable": pmlma10CfgLabellineTable,
       "pmlma10CfgLabellineEntry": pmlma10CfgLabellineEntry,
       "pmlma10CfgLabellineIndex": pmlma10CfgLabellineIndex,
       "pmlma10CfgLabellinePortn": pmlma10CfgLabellinePortn,
       "pmlma10CfgStartuptlh": pmlma10CfgStartuptlh,
       "pmlma10CfgOtxtlhTable": pmlma10CfgOtxtlhTable,
       "pmlma10CfgOtxtlhEntry": pmlma10CfgOtxtlhEntry,
       "pmlma10CfgOtxtlhIndex": pmlma10CfgOtxtlhIndex,
       "pmlma10CfgLinePwrLaserPortn": pmlma10CfgLinePwrLaserPortn,
       "pmlma10CfgLineFCurrentPortn": pmlma10CfgLineFCurrentPortn,
       "pmlma10CfgLineGridCurrentPortn": pmlma10CfgLineGridCurrentPortn,
       "pmlma10CfgFPortn": pmlma10CfgFPortn,
       "pmlma10CfgRxLineFCurrentPortn": pmlma10CfgRxLineFCurrentPortn,
       "pmlma10CfgOther": pmlma10CfgOther,
       "pmlma10tablemoduleOther": pmlma10tablemoduleOther,
       "pmlma10Cfgmode": pmlma10Cfgmode,
       "pmlma10CfgStartuptablefive": pmlma10CfgStartuptablefive,
       "pmlma10CfgOtxtlhcapabilitiesTable": pmlma10CfgOtxtlhcapabilitiesTable,
       "pmlma10CfgOtxtlhcapabilitiesEntry": pmlma10CfgOtxtlhcapabilitiesEntry,
       "pmlma10CfgOtxtlhcapabilitiesIndex": pmlma10CfgOtxtlhcapabilitiesIndex,
       "pmlma10CfgComponentTypePortn": pmlma10CfgComponentTypePortn,
       "pmlma10CfgMiscellaneousPortn": pmlma10CfgMiscellaneousPortn,
       "pmlma10CfgFirstChannelPortn": pmlma10CfgFirstChannelPortn,
       "pmlma10CfgLastChannelPortn": pmlma10CfgLastChannelPortn,
       "pmlma10CfgGridPortn": pmlma10CfgGridPortn,
       "pmlma10CfgWriteConfiguration": pmlma10CfgWriteConfiguration,
       "pmlma10traps": pmlma10traps,
       "pmlma10trapPortNumber": pmlma10trapPortNumber,
       "pmlma10trapLineNumber": pmlma10trapLineNumber,
       "pmlma10trapBoardNumber": pmlma10trapBoardNumber,
       "pmlma10LineTrapNotUrgentGoesOn": pmlma10LineTrapNotUrgentGoesOn,
       "pmlma10LineTrapNotUrgentGoesOff": pmlma10LineTrapNotUrgentGoesOff,
       "pmlma10LineTrapUrgentGoesOn": pmlma10LineTrapUrgentGoesOn,
       "pmlma10LineTrapUrgentGoesOff": pmlma10LineTrapUrgentGoesOff,
       "pmlma10LineTrapCritGoesOn": pmlma10LineTrapCritGoesOn,
       "pmlma10LineTrapCritGoesOff": pmlma10LineTrapCritGoesOff,
       "pmlma10ClientTrapNotUrgentGoesOn": pmlma10ClientTrapNotUrgentGoesOn,
       "pmlma10ClientTrapNotUrgentGoesOff": pmlma10ClientTrapNotUrgentGoesOff,
       "pmlma10ClientTrapUrgentGoesOn": pmlma10ClientTrapUrgentGoesOn,
       "pmlma10ClientTrapUrgentGoesOff": pmlma10ClientTrapUrgentGoesOff,
       "pmlma10ClientTrapCritGoesOn": pmlma10ClientTrapCritGoesOn,
       "pmlma10ClientTrapCritGoesOff": pmlma10ClientTrapCritGoesOff,
       "pmlma10PowerTrapUrgentGoesOn": pmlma10PowerTrapUrgentGoesOn,
       "pmlma10PowerTrapUrgentGoesOff": pmlma10PowerTrapUrgentGoesOff,
       "pmlma10Monitoring": pmlma10Monitoring,
       "pmlma10MonOther": pmlma10MonOther,
       "pmlma10MonRmon": pmlma10MonRmon,
       "pmlma10MonCountersReset": pmlma10MonCountersReset,
       "pmlma10MonCountersStop": pmlma10MonCountersStop,
       "pmlma10MonClient": pmlma10MonClient,
       "pmlma10MonClientRmonCounter": pmlma10MonClientRmonCounter,
       "pmlma10MonupRmonBytesCounterClientInputTable": pmlma10MonupRmonBytesCounterClientInputTable,
       "pmlma10MonupRmonBytesCounterClientInputEntry": pmlma10MonupRmonBytesCounterClientInputEntry,
       "pmlma10MonupRmonBytesCounterClientInputIndex": pmlma10MonupRmonBytesCounterClientInputIndex,
       "pmlma10MonupRmonBytesCounterClientInputValuePortn": pmlma10MonupRmonBytesCounterClientInputValuePortn,
       "pmlma10MonupRmonBytesCounterClientInputErrorPortn": pmlma10MonupRmonBytesCounterClientInputErrorPortn,
       "pmlma10MonupRmonBytesCounterClientInputOverloadPortn": pmlma10MonupRmonBytesCounterClientInputOverloadPortn,
       "pmlma10MonupRmonCrcErrorsCounterClientInputTable": pmlma10MonupRmonCrcErrorsCounterClientInputTable,
       "pmlma10MonupRmonCrcErrorsCounterClientInputEntry": pmlma10MonupRmonCrcErrorsCounterClientInputEntry,
       "pmlma10MonupRmonCrcErrorsCounterClientInputIndex": pmlma10MonupRmonCrcErrorsCounterClientInputIndex,
       "pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn": pmlma10MonupRmonCrcErrorsCounterClientInputValuePortn,
       "pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn": pmlma10MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn": pmlma10MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pmlma10MonupRmonPacketsCounterClientInputTable": pmlma10MonupRmonPacketsCounterClientInputTable,
       "pmlma10MonupRmonPacketsCounterClientInputEntry": pmlma10MonupRmonPacketsCounterClientInputEntry,
       "pmlma10MonupRmonPacketsCounterClientInputIndex": pmlma10MonupRmonPacketsCounterClientInputIndex,
       "pmlma10MonupRmonPacketsCounterClientInputValuePortn": pmlma10MonupRmonPacketsCounterClientInputValuePortn,
       "pmlma10MonupRmonPacketsCounterClientInputErrorPortn": pmlma10MonupRmonPacketsCounterClientInputErrorPortn,
       "pmlma10MonupRmonPacketsCounterClientInputOverloadPortn": pmlma10MonupRmonPacketsCounterClientInputOverloadPortn,
       "pmlma10MonupRmonBroadcastCounterClientInputTable": pmlma10MonupRmonBroadcastCounterClientInputTable,
       "pmlma10MonupRmonBroadcastCounterClientInputEntry": pmlma10MonupRmonBroadcastCounterClientInputEntry,
       "pmlma10MonupRmonBroadcastCounterClientInputIndex": pmlma10MonupRmonBroadcastCounterClientInputIndex,
       "pmlma10MonupRmonBroadcastCounterClientInputValuePortn": pmlma10MonupRmonBroadcastCounterClientInputValuePortn,
       "pmlma10MonupRmonBroadcastCounterClientInputErrorPortn": pmlma10MonupRmonBroadcastCounterClientInputErrorPortn,
       "pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn": pmlma10MonupRmonBroadcastCounterClientInputOverloadPortn,
       "pmlma10MonupRmonMulticastCounterClientInputTable": pmlma10MonupRmonMulticastCounterClientInputTable,
       "pmlma10MonupRmonMulticastCounterClientInputEntry": pmlma10MonupRmonMulticastCounterClientInputEntry,
       "pmlma10MonupRmonMulticastCounterClientInputIndex": pmlma10MonupRmonMulticastCounterClientInputIndex,
       "pmlma10MonupRmonMulticastCounterClientInputValuePortn": pmlma10MonupRmonMulticastCounterClientInputValuePortn,
       "pmlma10MonupRmonMulticastCounterClientInputErrorPortn": pmlma10MonupRmonMulticastCounterClientInputErrorPortn,
       "pmlma10MonupRmonMulticastCounterClientInputOverloadPortn": pmlma10MonupRmonMulticastCounterClientInputOverloadPortn,
       "pmlma10MonupRmonPauseFrameCounterClientInputTable": pmlma10MonupRmonPauseFrameCounterClientInputTable,
       "pmlma10MonupRmonPauseFrameCounterClientInputEntry": pmlma10MonupRmonPauseFrameCounterClientInputEntry,
       "pmlma10MonupRmonPauseFrameCounterClientInputIndex": pmlma10MonupRmonPauseFrameCounterClientInputIndex,
       "pmlma10MonupRmonPauseFrameCounterClientInputValuePortn": pmlma10MonupRmonPauseFrameCounterClientInputValuePortn,
       "pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn": pmlma10MonupRmonPauseFrameCounterClientInputErrorPortn,
       "pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn": pmlma10MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pmlma10MondwRmonCrcErrorsCounterClientInputTable": pmlma10MondwRmonCrcErrorsCounterClientInputTable,
       "pmlma10MondwRmonCrcErrorsCounterClientInputEntry": pmlma10MondwRmonCrcErrorsCounterClientInputEntry,
       "pmlma10MondwRmonCrcErrorsCounterClientInputIndex": pmlma10MondwRmonCrcErrorsCounterClientInputIndex,
       "pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn": pmlma10MondwRmonCrcErrorsCounterClientInputValuePortn,
       "pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn": pmlma10MondwRmonCrcErrorsCounterClientInputErrorPortn,
       "pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn": pmlma10MondwRmonCrcErrorsCounterClientInputOverloadPortn,
       "pmlma10MondwRmonPacketsCounterClientInputTable": pmlma10MondwRmonPacketsCounterClientInputTable,
       "pmlma10MondwRmonPacketsCounterClientInputEntry": pmlma10MondwRmonPacketsCounterClientInputEntry,
       "pmlma10MondwRmonPacketsCounterClientInputIndex": pmlma10MondwRmonPacketsCounterClientInputIndex,
       "pmlma10MondwRmonPacketsCounterClientInputValuePortn": pmlma10MondwRmonPacketsCounterClientInputValuePortn,
       "pmlma10MondwRmonPacketsCounterClientInputErrorPortn": pmlma10MondwRmonPacketsCounterClientInputErrorPortn,
       "pmlma10MondwRmonPacketsCounterClientInputOverloadPortn": pmlma10MondwRmonPacketsCounterClientInputOverloadPortn}
)
