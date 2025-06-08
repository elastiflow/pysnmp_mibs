# SNMP MIB module (VAR-TSSPLICER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/steelwedge_48000/VAR-TSSPLICER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:10:58 2025
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
 RowStatus,
 TDomain,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TDomain",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(VarErrorStatus,) = mibBuilder.importSymbols(
    "VAR-ERROR-MIB",
    "VarErrorStatus")

(VarBoolGroupState,
 varProducts) = mibBuilder.importSymbols(
    "VAR-GLOBAL-MIB",
    "VarBoolGroupState",
    "varProducts")


# MODULE-IDENTITY

varTSSplicerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2)
)
if mibBuilder.loadTexts:
    varTSSplicerMib.setRevisions(
        ("2016-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VarAllBypasses_Type = VarBoolGroupState
_VarAllBypasses_Object = MibScalar
varAllBypasses = _VarAllBypasses_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 1),
    _VarAllBypasses_Type()
)
varAllBypasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varAllBypasses.setStatus("current")
_VarHwTractsTable_Object = MibTable
varHwTractsTable = _VarHwTractsTable_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3)
)
if mibBuilder.loadTexts:
    varHwTractsTable.setStatus("current")
_VarHwTractEntry_Object = MibTableRow
varHwTractEntry = _VarHwTractEntry_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3, 1)
)
varHwTractEntry.setIndexNames(
    (0, "VAR-TSSPLICER-MIB", "varHwTractIndex"),
)
if mibBuilder.loadTexts:
    varHwTractEntry.setStatus("current")
_VarHwTractIndex_Type = Unsigned32
_VarHwTractIndex_Object = MibTableColumn
varHwTractIndex = _VarHwTractIndex_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3, 1, 1),
    _VarHwTractIndex_Type()
)
varHwTractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varHwTractIndex.setStatus("current")
_VarHwTractTitle_Type = DisplayString
_VarHwTractTitle_Object = MibTableColumn
varHwTractTitle = _VarHwTractTitle_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3, 1, 2),
    _VarHwTractTitle_Type()
)
varHwTractTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varHwTractTitle.setStatus("current")
_VarHwTractInBitrate_Type = Integer32
_VarHwTractInBitrate_Object = MibTableColumn
varHwTractInBitrate = _VarHwTractInBitrate_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3, 1, 3),
    _VarHwTractInBitrate_Type()
)
varHwTractInBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varHwTractInBitrate.setStatus("current")
_VarHwTractOutBitrate_Type = Integer32
_VarHwTractOutBitrate_Object = MibTableColumn
varHwTractOutBitrate = _VarHwTractOutBitrate_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3, 1, 4),
    _VarHwTractOutBitrate_Type()
)
varHwTractOutBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varHwTractOutBitrate.setStatus("current")
_VarHwTractBypass_Type = VarBoolGroupState
_VarHwTractBypass_Object = MibTableColumn
varHwTractBypass = _VarHwTractBypass_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 3, 1, 5),
    _VarHwTractBypass_Type()
)
varHwTractBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varHwTractBypass.setStatus("current")
_VarMainCfgURL_Type = OctetString
_VarMainCfgURL_Object = MibScalar
varMainCfgURL = _VarMainCfgURL_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 4),
    _VarMainCfgURL_Type()
)
varMainCfgURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varMainCfgURL.setStatus("current")
_VarMainCfgReloadPeriod_Type = Unsigned32
_VarMainCfgReloadPeriod_Object = MibScalar
varMainCfgReloadPeriod = _VarMainCfgReloadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 5),
    _VarMainCfgReloadPeriod_Type()
)
varMainCfgReloadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varMainCfgReloadPeriod.setStatus("current")
_VarSplicerID_Type = OctetString
_VarSplicerID_Object = MibScalar
varSplicerID = _VarSplicerID_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 6),
    _VarSplicerID_Type()
)
varSplicerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varSplicerID.setStatus("current")
_VarZoneID_Type = OctetString
_VarZoneID_Object = MibScalar
varZoneID = _VarZoneID_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 7),
    _VarZoneID_Type()
)
varZoneID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varZoneID.setStatus("current")
_VarTransferSpeedLimit_Type = Unsigned32
_VarTransferSpeedLimit_Object = MibScalar
varTransferSpeedLimit = _VarTransferSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 8),
    _VarTransferSpeedLimit_Type()
)
varTransferSpeedLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    varTransferSpeedLimit.setStatus("current")
_VarAllMediaPresent_Type = TruthValue
_VarAllMediaPresent_Object = MibScalar
varAllMediaPresent = _VarAllMediaPresent_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 9),
    _VarAllMediaPresent_Type()
)
varAllMediaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varAllMediaPresent.setStatus("current")
_VarAllSchedulesPresent_Type = TruthValue
_VarAllSchedulesPresent_Object = MibScalar
varAllSchedulesPresent = _VarAllSchedulesPresent_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 10),
    _VarAllSchedulesPresent_Type()
)
varAllSchedulesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varAllSchedulesPresent.setStatus("current")
_VarMainCfgDownloadStatus_Type = VarErrorStatus
_VarMainCfgDownloadStatus_Object = MibScalar
varMainCfgDownloadStatus = _VarMainCfgDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 48000, 1, 2, 11),
    _VarMainCfgDownloadStatus_Type()
)
varMainCfgDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varMainCfgDownloadStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VAR-TSSPLICER-MIB",
    **{"varTSSplicerMib": varTSSplicerMib,
       "varAllBypasses": varAllBypasses,
       "varHwTractsTable": varHwTractsTable,
       "varHwTractEntry": varHwTractEntry,
       "varHwTractIndex": varHwTractIndex,
       "varHwTractTitle": varHwTractTitle,
       "varHwTractInBitrate": varHwTractInBitrate,
       "varHwTractOutBitrate": varHwTractOutBitrate,
       "varHwTractBypass": varHwTractBypass,
       "varMainCfgURL": varMainCfgURL,
       "varMainCfgReloadPeriod": varMainCfgReloadPeriod,
       "varSplicerID": varSplicerID,
       "varZoneID": varZoneID,
       "varTransferSpeedLimit": varTransferSpeedLimit,
       "varAllMediaPresent": varAllMediaPresent,
       "varAllSchedulesPresent": varAllSchedulesPresent,
       "varMainCfgDownloadStatus": varMainCfgDownloadStatus}
)
