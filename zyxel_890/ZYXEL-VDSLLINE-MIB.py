# SNMP MIB module (ZYXEL-VDSLLINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-VDSLLINE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:33:26 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(vesSeriesCommon,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "vesSeriesCommon")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccessSwitchVdslLineMib_ObjectIdentity = ObjectIdentity
accessSwitchVdslLineMib = _AccessSwitchVdslLineMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1)
)
_AccessSwitchVdslLineMibObjects_ObjectIdentity = ObjectIdentity
accessSwitchVdslLineMibObjects = _AccessSwitchVdslLineMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1)
)
_AccessSwitchVdslLineTable_Object = MibTable
accessSwitchVdslLineTable = _AccessSwitchVdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    accessSwitchVdslLineTable.setStatus("mandatory")
_AccessSwitchVdslLineEntry_Object = MibTableRow
accessSwitchVdslLineEntry = _AccessSwitchVdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 1, 1)
)
accessSwitchVdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslLineEntry.setStatus("mandatory")


class _AccessSwitchVdslLineCoding_Type(Integer32):
    """Custom type accessSwitchVdslLineCoding based on Integer32"""
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
        *(("other", 1),
          ("dmt", 2),
          ("cap", 3),
          ("qam", 4))
    )


_AccessSwitchVdslLineCoding_Type.__name__ = "Integer32"
_AccessSwitchVdslLineCoding_Object = MibTableColumn
accessSwitchVdslLineCoding = _AccessSwitchVdslLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 1, 1, 1),
    _AccessSwitchVdslLineCoding_Type()
)
accessSwitchVdslLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslLineCoding.setStatus("mandatory")
_AccessSwitchVdslLineDiscCount_Type = Counter32
_AccessSwitchVdslLineDiscCount_Object = MibTableColumn
accessSwitchVdslLineDiscCount = _AccessSwitchVdslLineDiscCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 1, 1, 2),
    _AccessSwitchVdslLineDiscCount_Type()
)
accessSwitchVdslLineDiscCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslLineDiscCount.setStatus("mandatory")


class _AccessSwitchVdslLineConfProfile_Type(DisplayString):
    """Custom type accessSwitchVdslLineConfProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AccessSwitchVdslLineConfProfile_Type.__name__ = "DisplayString"
_AccessSwitchVdslLineConfProfile_Object = MibTableColumn
accessSwitchVdslLineConfProfile = _AccessSwitchVdslLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 1, 1, 3),
    _AccessSwitchVdslLineConfProfile_Type()
)
accessSwitchVdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchVdslLineConfProfile.setStatus("mandatory")
_AccessSwitchVdslVtuoPhysTable_Object = MibTable
accessSwitchVdslVtuoPhysTable = _AccessSwitchVdslVtuoPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPhysTable.setStatus("mandatory")
_AccessSwitchVdslVtuoPhysEntry_Object = MibTableRow
accessSwitchVdslVtuoPhysEntry = _AccessSwitchVdslVtuoPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1)
)
accessSwitchVdslVtuoPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPhysEntry.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrSnrMgn_Type = Integer32
_AccessSwitchVdslVtuoCurrSnrMgn_Object = MibTableColumn
accessSwitchVdslVtuoCurrSnrMgn = _AccessSwitchVdslVtuoCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 1),
    _AccessSwitchVdslVtuoCurrSnrMgn_Type()
)
accessSwitchVdslVtuoCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrMse_Type = Integer32
_AccessSwitchVdslVtuoCurrMse_Object = MibTableColumn
accessSwitchVdslVtuoCurrMse = _AccessSwitchVdslVtuoCurrMse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 2),
    _AccessSwitchVdslVtuoCurrMse_Type()
)
accessSwitchVdslVtuoCurrMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrMse.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrPsd_Type = Integer32
_AccessSwitchVdslVtuoCurrPsd_Object = MibTableColumn
accessSwitchVdslVtuoCurrPsd = _AccessSwitchVdslVtuoCurrPsd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 3),
    _AccessSwitchVdslVtuoCurrPsd_Type()
)
accessSwitchVdslVtuoCurrPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrPsd.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrRsErr_Type = Counter32
_AccessSwitchVdslVtuoCurrRsErr_Object = MibTableColumn
accessSwitchVdslVtuoCurrRsErr = _AccessSwitchVdslVtuoCurrRsErr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 4),
    _AccessSwitchVdslVtuoCurrRsErr_Type()
)
accessSwitchVdslVtuoCurrRsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrRsErr.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrAtn_Type = Gauge32
_AccessSwitchVdslVtuoCurrAtn_Object = MibTableColumn
accessSwitchVdslVtuoCurrAtn = _AccessSwitchVdslVtuoCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 5),
    _AccessSwitchVdslVtuoCurrAtn_Type()
)
accessSwitchVdslVtuoCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrAtn.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrOutputPwr_Type = Integer32
_AccessSwitchVdslVtuoCurrOutputPwr_Object = MibTableColumn
accessSwitchVdslVtuoCurrOutputPwr = _AccessSwitchVdslVtuoCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 6),
    _AccessSwitchVdslVtuoCurrOutputPwr_Type()
)
accessSwitchVdslVtuoCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrOutputPwr.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrRate_Type = Integer32
_AccessSwitchVdslVtuoCurrRate_Object = MibTableColumn
accessSwitchVdslVtuoCurrRate = _AccessSwitchVdslVtuoCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 7),
    _AccessSwitchVdslVtuoCurrRate_Type()
)
accessSwitchVdslVtuoCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrRate.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrAttainableRate_Type = Gauge32
_AccessSwitchVdslVtuoCurrAttainableRate_Object = MibTableColumn
accessSwitchVdslVtuoCurrAttainableRate = _AccessSwitchVdslVtuoCurrAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 8),
    _AccessSwitchVdslVtuoCurrAttainableRate_Type()
)
accessSwitchVdslVtuoCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrAttainableRate.setStatus("mandatory")
_AccessSwitchVdslVtuoCurrStatus_Type = Integer32
_AccessSwitchVdslVtuoCurrStatus_Object = MibTableColumn
accessSwitchVdslVtuoCurrStatus = _AccessSwitchVdslVtuoCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 2, 1, 9),
    _AccessSwitchVdslVtuoCurrStatus_Type()
)
accessSwitchVdslVtuoCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoCurrStatus.setStatus("mandatory")
_AccessSwitchVdslVturPhysTable_Object = MibTable
accessSwitchVdslVturPhysTable = _AccessSwitchVdslVturPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturPhysTable.setStatus("mandatory")
_AccessSwitchVdslVturPhysEntry_Object = MibTableRow
accessSwitchVdslVturPhysEntry = _AccessSwitchVdslVturPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1)
)
accessSwitchVdslVturPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturPhysEntry.setStatus("mandatory")
_AccessSwitchVdslVturCurrSnrMgn_Type = Integer32
_AccessSwitchVdslVturCurrSnrMgn_Object = MibTableColumn
accessSwitchVdslVturCurrSnrMgn = _AccessSwitchVdslVturCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 1),
    _AccessSwitchVdslVturCurrSnrMgn_Type()
)
accessSwitchVdslVturCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVturCurrMse_Type = Integer32
_AccessSwitchVdslVturCurrMse_Object = MibTableColumn
accessSwitchVdslVturCurrMse = _AccessSwitchVdslVturCurrMse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 2),
    _AccessSwitchVdslVturCurrMse_Type()
)
accessSwitchVdslVturCurrMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrMse.setStatus("mandatory")
_AccessSwitchVdslVturCurrPsd_Type = Integer32
_AccessSwitchVdslVturCurrPsd_Object = MibTableColumn
accessSwitchVdslVturCurrPsd = _AccessSwitchVdslVturCurrPsd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 3),
    _AccessSwitchVdslVturCurrPsd_Type()
)
accessSwitchVdslVturCurrPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrPsd.setStatus("mandatory")
_AccessSwitchVdslVturCurrRsErr_Type = Counter32
_AccessSwitchVdslVturCurrRsErr_Object = MibTableColumn
accessSwitchVdslVturCurrRsErr = _AccessSwitchVdslVturCurrRsErr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 4),
    _AccessSwitchVdslVturCurrRsErr_Type()
)
accessSwitchVdslVturCurrRsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrRsErr.setStatus("mandatory")
_AccessSwitchVdslVturCurrAtn_Type = Gauge32
_AccessSwitchVdslVturCurrAtn_Object = MibTableColumn
accessSwitchVdslVturCurrAtn = _AccessSwitchVdslVturCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 5),
    _AccessSwitchVdslVturCurrAtn_Type()
)
accessSwitchVdslVturCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrAtn.setStatus("mandatory")
_AccessSwitchVdslVturCurrOutputPwr_Type = Integer32
_AccessSwitchVdslVturCurrOutputPwr_Object = MibTableColumn
accessSwitchVdslVturCurrOutputPwr = _AccessSwitchVdslVturCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 6),
    _AccessSwitchVdslVturCurrOutputPwr_Type()
)
accessSwitchVdslVturCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrOutputPwr.setStatus("mandatory")
_AccessSwitchVdslVturCurrRate_Type = Integer32
_AccessSwitchVdslVturCurrRate_Object = MibTableColumn
accessSwitchVdslVturCurrRate = _AccessSwitchVdslVturCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 7),
    _AccessSwitchVdslVturCurrRate_Type()
)
accessSwitchVdslVturCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrRate.setStatus("mandatory")
_AccessSwitchVdslVturCurrAttainableRate_Type = Gauge32
_AccessSwitchVdslVturCurrAttainableRate_Object = MibTableColumn
accessSwitchVdslVturCurrAttainableRate = _AccessSwitchVdslVturCurrAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 8),
    _AccessSwitchVdslVturCurrAttainableRate_Type()
)
accessSwitchVdslVturCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrAttainableRate.setStatus("mandatory")
_AccessSwitchVdslVturCurrStatus_Type = Integer32
_AccessSwitchVdslVturCurrStatus_Object = MibTableColumn
accessSwitchVdslVturCurrStatus = _AccessSwitchVdslVturCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 3, 1, 9),
    _AccessSwitchVdslVturCurrStatus_Type()
)
accessSwitchVdslVturCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturCurrStatus.setStatus("mandatory")
_AccessSwitchVdslVtuoInventoryTable_Object = MibTable
accessSwitchVdslVtuoInventoryTable = _AccessSwitchVdslVtuoInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoInventoryTable.setStatus("mandatory")
_AccessSwitchVdslVtuoInventoryEntry_Object = MibTableRow
accessSwitchVdslVtuoInventoryEntry = _AccessSwitchVdslVtuoInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 4, 1)
)
accessSwitchVdslVtuoInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoInventoryEntry.setStatus("mandatory")
_AccessSwitchVdslVtuoInvSerialNumber_Type = DisplayString
_AccessSwitchVdslVtuoInvSerialNumber_Object = MibTableColumn
accessSwitchVdslVtuoInvSerialNumber = _AccessSwitchVdslVtuoInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 4, 1, 1),
    _AccessSwitchVdslVtuoInvSerialNumber_Type()
)
accessSwitchVdslVtuoInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoInvSerialNumber.setStatus("mandatory")
_AccessSwitchVdslVtuoInvVendorID_Type = DisplayString
_AccessSwitchVdslVtuoInvVendorID_Object = MibTableColumn
accessSwitchVdslVtuoInvVendorID = _AccessSwitchVdslVtuoInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 4, 1, 2),
    _AccessSwitchVdslVtuoInvVendorID_Type()
)
accessSwitchVdslVtuoInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoInvVendorID.setStatus("mandatory")
_AccessSwitchVdslVtuoInvVersionNumber_Type = DisplayString
_AccessSwitchVdslVtuoInvVersionNumber_Object = MibTableColumn
accessSwitchVdslVtuoInvVersionNumber = _AccessSwitchVdslVtuoInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 4, 1, 3),
    _AccessSwitchVdslVtuoInvVersionNumber_Type()
)
accessSwitchVdslVtuoInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoInvVersionNumber.setStatus("mandatory")
_AccessSwitchVdslVturInventoryTable_Object = MibTable
accessSwitchVdslVturInventoryTable = _AccessSwitchVdslVturInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturInventoryTable.setStatus("mandatory")
_AccessSwitchVdslVturInventoryEntry_Object = MibTableRow
accessSwitchVdslVturInventoryEntry = _AccessSwitchVdslVturInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 5, 1)
)
accessSwitchVdslVturInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturInventoryEntry.setStatus("mandatory")
_AccessSwitchVdslVturInvSerialNumber_Type = DisplayString
_AccessSwitchVdslVturInvSerialNumber_Object = MibTableColumn
accessSwitchVdslVturInvSerialNumber = _AccessSwitchVdslVturInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 5, 1, 1),
    _AccessSwitchVdslVturInvSerialNumber_Type()
)
accessSwitchVdslVturInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturInvSerialNumber.setStatus("mandatory")
_AccessSwitchVdslVturInvVendorID_Type = DisplayString
_AccessSwitchVdslVturInvVendorID_Object = MibTableColumn
accessSwitchVdslVturInvVendorID = _AccessSwitchVdslVturInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 5, 1, 2),
    _AccessSwitchVdslVturInvVendorID_Type()
)
accessSwitchVdslVturInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturInvVendorID.setStatus("mandatory")
_AccessSwitchVdslVturInvVersionNumber_Type = DisplayString
_AccessSwitchVdslVturInvVersionNumber_Object = MibTableColumn
accessSwitchVdslVturInvVersionNumber = _AccessSwitchVdslVturInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 5, 1, 3),
    _AccessSwitchVdslVturInvVersionNumber_Type()
)
accessSwitchVdslVturInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturInvVersionNumber.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfDataTable_Object = MibTable
accessSwitchVdslVtuoPerfDataTable = _AccessSwitchVdslVtuoPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfDataTable.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfDataEntry_Object = MibTableRow
accessSwitchVdslVtuoPerfDataEntry = _AccessSwitchVdslVtuoPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1)
)
accessSwitchVdslVtuoPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfDataEntry.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfLofs_Type = Counter32
_AccessSwitchVdslVtuoPerfLofs_Object = MibTableColumn
accessSwitchVdslVtuoPerfLofs = _AccessSwitchVdslVtuoPerfLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 1),
    _AccessSwitchVdslVtuoPerfLofs_Type()
)
accessSwitchVdslVtuoPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfLofs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfLoss_Type = Counter32
_AccessSwitchVdslVtuoPerfLoss_Object = MibTableColumn
accessSwitchVdslVtuoPerfLoss = _AccessSwitchVdslVtuoPerfLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 2),
    _AccessSwitchVdslVtuoPerfLoss_Type()
)
accessSwitchVdslVtuoPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfLoss.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfLols_Type = Counter32
_AccessSwitchVdslVtuoPerfLols_Object = MibTableColumn
accessSwitchVdslVtuoPerfLols = _AccessSwitchVdslVtuoPerfLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 3),
    _AccessSwitchVdslVtuoPerfLols_Type()
)
accessSwitchVdslVtuoPerfLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfLols.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfLprs_Type = Counter32
_AccessSwitchVdslVtuoPerfLprs_Object = MibTableColumn
accessSwitchVdslVtuoPerfLprs = _AccessSwitchVdslVtuoPerfLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 4),
    _AccessSwitchVdslVtuoPerfLprs_Type()
)
accessSwitchVdslVtuoPerfLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfLprs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfESs_Type = Counter32
_AccessSwitchVdslVtuoPerfESs_Object = MibTableColumn
accessSwitchVdslVtuoPerfESs = _AccessSwitchVdslVtuoPerfESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 5),
    _AccessSwitchVdslVtuoPerfESs_Type()
)
accessSwitchVdslVtuoPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfESs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfInits_Type = Counter32
_AccessSwitchVdslVtuoPerfInits_Object = MibTableColumn
accessSwitchVdslVtuoPerfInits = _AccessSwitchVdslVtuoPerfInits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 6),
    _AccessSwitchVdslVtuoPerfInits_Type()
)
accessSwitchVdslVtuoPerfInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfInits.setStatus("mandatory")


class _AccessSwitchVdslVtuoPerfValidIntervals_Type(Integer32):
    """Custom type accessSwitchVdslVtuoPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AccessSwitchVdslVtuoPerfValidIntervals_Type.__name__ = "Integer32"
_AccessSwitchVdslVtuoPerfValidIntervals_Object = MibTableColumn
accessSwitchVdslVtuoPerfValidIntervals = _AccessSwitchVdslVtuoPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 7),
    _AccessSwitchVdslVtuoPerfValidIntervals_Type()
)
accessSwitchVdslVtuoPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfValidIntervals.setStatus("mandatory")


class _AccessSwitchVdslVtuoPerfInvalidIntervals_Type(Integer32):
    """Custom type accessSwitchVdslVtuoPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AccessSwitchVdslVtuoPerfInvalidIntervals_Type.__name__ = "Integer32"
_AccessSwitchVdslVtuoPerfInvalidIntervals_Object = MibTableColumn
accessSwitchVdslVtuoPerfInvalidIntervals = _AccessSwitchVdslVtuoPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 8),
    _AccessSwitchVdslVtuoPerfInvalidIntervals_Type()
)
accessSwitchVdslVtuoPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfInvalidIntervals.setStatus("mandatory")


class _AccessSwitchVdslVtuoPerfCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type accessSwitchVdslVtuoPerfCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AccessSwitchVdslVtuoPerfCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_AccessSwitchVdslVtuoPerfCurr15MinTimeElapsed_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinTimeElapsed = _AccessSwitchVdslVtuoPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 9),
    _AccessSwitchVdslVtuoPerfCurr15MinTimeElapsed_Type()
)
accessSwitchVdslVtuoPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinTimeElapsed.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr15MinLofs_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr15MinLofs_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinLofs = _AccessSwitchVdslVtuoPerfCurr15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 10),
    _AccessSwitchVdslVtuoPerfCurr15MinLofs_Type()
)
accessSwitchVdslVtuoPerfCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinLofs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr15MinLoss_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr15MinLoss_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinLoss = _AccessSwitchVdslVtuoPerfCurr15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 11),
    _AccessSwitchVdslVtuoPerfCurr15MinLoss_Type()
)
accessSwitchVdslVtuoPerfCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinLoss.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr15MinLols_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr15MinLols_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinLols = _AccessSwitchVdslVtuoPerfCurr15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 12),
    _AccessSwitchVdslVtuoPerfCurr15MinLols_Type()
)
accessSwitchVdslVtuoPerfCurr15MinLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinLols.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr15MinLprs_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr15MinLprs_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinLprs = _AccessSwitchVdslVtuoPerfCurr15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 13),
    _AccessSwitchVdslVtuoPerfCurr15MinLprs_Type()
)
accessSwitchVdslVtuoPerfCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinLprs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr15MinESs_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr15MinESs_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinESs = _AccessSwitchVdslVtuoPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 14),
    _AccessSwitchVdslVtuoPerfCurr15MinESs_Type()
)
accessSwitchVdslVtuoPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinESs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr15MinInits_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr15MinInits_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr15MinInits = _AccessSwitchVdslVtuoPerfCurr15MinInits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 15),
    _AccessSwitchVdslVtuoPerfCurr15MinInits_Type()
)
accessSwitchVdslVtuoPerfCurr15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr15MinInits.setStatus("mandatory")


class _AccessSwitchVdslVtuoPerfCurr1DayTimeElapsed_Type(Gauge32):
    """Custom type accessSwitchVdslVtuoPerfCurr1DayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AccessSwitchVdslVtuoPerfCurr1DayTimeElapsed_Type.__name__ = "Gauge32"
_AccessSwitchVdslVtuoPerfCurr1DayTimeElapsed_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayTimeElapsed = _AccessSwitchVdslVtuoPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 16),
    _AccessSwitchVdslVtuoPerfCurr1DayTimeElapsed_Type()
)
accessSwitchVdslVtuoPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayTimeElapsed.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr1DayLofs_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr1DayLofs_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayLofs = _AccessSwitchVdslVtuoPerfCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 17),
    _AccessSwitchVdslVtuoPerfCurr1DayLofs_Type()
)
accessSwitchVdslVtuoPerfCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayLofs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr1DayLoss_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr1DayLoss_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayLoss = _AccessSwitchVdslVtuoPerfCurr1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 18),
    _AccessSwitchVdslVtuoPerfCurr1DayLoss_Type()
)
accessSwitchVdslVtuoPerfCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayLoss.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr1DayLols_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr1DayLols_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayLols = _AccessSwitchVdslVtuoPerfCurr1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 19),
    _AccessSwitchVdslVtuoPerfCurr1DayLols_Type()
)
accessSwitchVdslVtuoPerfCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayLols.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr1DayLprs_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr1DayLprs_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayLprs = _AccessSwitchVdslVtuoPerfCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 20),
    _AccessSwitchVdslVtuoPerfCurr1DayLprs_Type()
)
accessSwitchVdslVtuoPerfCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayLprs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr1DayESs_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr1DayESs_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayESs = _AccessSwitchVdslVtuoPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 21),
    _AccessSwitchVdslVtuoPerfCurr1DayESs_Type()
)
accessSwitchVdslVtuoPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayESs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfCurr1DayInits_Type = Counter32
_AccessSwitchVdslVtuoPerfCurr1DayInits_Object = MibTableColumn
accessSwitchVdslVtuoPerfCurr1DayInits = _AccessSwitchVdslVtuoPerfCurr1DayInits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 22),
    _AccessSwitchVdslVtuoPerfCurr1DayInits_Type()
)
accessSwitchVdslVtuoPerfCurr1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfCurr1DayInits.setStatus("mandatory")


class _AccessSwitchVdslVtuoPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type accessSwitchVdslVtuoPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AccessSwitchVdslVtuoPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_AccessSwitchVdslVtuoPerfPrev1DayMoniSecs_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayMoniSecs = _AccessSwitchVdslVtuoPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 23),
    _AccessSwitchVdslVtuoPerfPrev1DayMoniSecs_Type()
)
accessSwitchVdslVtuoPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayMoniSecs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfPrev1DayLofs_Type = Counter32
_AccessSwitchVdslVtuoPerfPrev1DayLofs_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayLofs = _AccessSwitchVdslVtuoPerfPrev1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 24),
    _AccessSwitchVdslVtuoPerfPrev1DayLofs_Type()
)
accessSwitchVdslVtuoPerfPrev1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayLofs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfPrev1DayLoss_Type = Counter32
_AccessSwitchVdslVtuoPerfPrev1DayLoss_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayLoss = _AccessSwitchVdslVtuoPerfPrev1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 25),
    _AccessSwitchVdslVtuoPerfPrev1DayLoss_Type()
)
accessSwitchVdslVtuoPerfPrev1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayLoss.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfPrev1DayLols_Type = Counter32
_AccessSwitchVdslVtuoPerfPrev1DayLols_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayLols = _AccessSwitchVdslVtuoPerfPrev1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 26),
    _AccessSwitchVdslVtuoPerfPrev1DayLols_Type()
)
accessSwitchVdslVtuoPerfPrev1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayLols.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfPrev1DayLprs_Type = Counter32
_AccessSwitchVdslVtuoPerfPrev1DayLprs_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayLprs = _AccessSwitchVdslVtuoPerfPrev1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 27),
    _AccessSwitchVdslVtuoPerfPrev1DayLprs_Type()
)
accessSwitchVdslVtuoPerfPrev1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayLprs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfPrev1DayESs_Type = Counter32
_AccessSwitchVdslVtuoPerfPrev1DayESs_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayESs = _AccessSwitchVdslVtuoPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 28),
    _AccessSwitchVdslVtuoPerfPrev1DayESs_Type()
)
accessSwitchVdslVtuoPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayESs.setStatus("mandatory")
_AccessSwitchVdslVtuoPerfPrev1DayInits_Type = Counter32
_AccessSwitchVdslVtuoPerfPrev1DayInits_Object = MibTableColumn
accessSwitchVdslVtuoPerfPrev1DayInits = _AccessSwitchVdslVtuoPerfPrev1DayInits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 6, 1, 29),
    _AccessSwitchVdslVtuoPerfPrev1DayInits_Type()
)
accessSwitchVdslVtuoPerfPrev1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoPerfPrev1DayInits.setStatus("mandatory")
_AccessSwitchVdslVturPerfDataTable_Object = MibTable
accessSwitchVdslVturPerfDataTable = _AccessSwitchVdslVturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfDataTable.setStatus("mandatory")
_AccessSwitchVdslVturPerfDataEntry_Object = MibTableRow
accessSwitchVdslVturPerfDataEntry = _AccessSwitchVdslVturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1)
)
accessSwitchVdslVturPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfDataEntry.setStatus("mandatory")
_AccessSwitchVdslVturPerfLofs_Type = Counter32
_AccessSwitchVdslVturPerfLofs_Object = MibTableColumn
accessSwitchVdslVturPerfLofs = _AccessSwitchVdslVturPerfLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 1),
    _AccessSwitchVdslVturPerfLofs_Type()
)
accessSwitchVdslVturPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfLofs.setStatus("mandatory")
_AccessSwitchVdslVturPerfLoss_Type = Counter32
_AccessSwitchVdslVturPerfLoss_Object = MibTableColumn
accessSwitchVdslVturPerfLoss = _AccessSwitchVdslVturPerfLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 2),
    _AccessSwitchVdslVturPerfLoss_Type()
)
accessSwitchVdslVturPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfLoss.setStatus("mandatory")
_AccessSwitchVdslVturPerfLprs_Type = Counter32
_AccessSwitchVdslVturPerfLprs_Object = MibTableColumn
accessSwitchVdslVturPerfLprs = _AccessSwitchVdslVturPerfLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 3),
    _AccessSwitchVdslVturPerfLprs_Type()
)
accessSwitchVdslVturPerfLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfLprs.setStatus("mandatory")
_AccessSwitchVdslVturPerfESs_Type = Counter32
_AccessSwitchVdslVturPerfESs_Object = MibTableColumn
accessSwitchVdslVturPerfESs = _AccessSwitchVdslVturPerfESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 4),
    _AccessSwitchVdslVturPerfESs_Type()
)
accessSwitchVdslVturPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfESs.setStatus("mandatory")


class _AccessSwitchVdslVturPerfValidIntervals_Type(Integer32):
    """Custom type accessSwitchVdslVturPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AccessSwitchVdslVturPerfValidIntervals_Type.__name__ = "Integer32"
_AccessSwitchVdslVturPerfValidIntervals_Object = MibTableColumn
accessSwitchVdslVturPerfValidIntervals = _AccessSwitchVdslVturPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 5),
    _AccessSwitchVdslVturPerfValidIntervals_Type()
)
accessSwitchVdslVturPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfValidIntervals.setStatus("mandatory")


class _AccessSwitchVdslVturPerfInvalidIntervals_Type(Integer32):
    """Custom type accessSwitchVdslVturPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AccessSwitchVdslVturPerfInvalidIntervals_Type.__name__ = "Integer32"
_AccessSwitchVdslVturPerfInvalidIntervals_Object = MibTableColumn
accessSwitchVdslVturPerfInvalidIntervals = _AccessSwitchVdslVturPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 6),
    _AccessSwitchVdslVturPerfInvalidIntervals_Type()
)
accessSwitchVdslVturPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfInvalidIntervals.setStatus("mandatory")


class _AccessSwitchVdslVturPerfCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type accessSwitchVdslVturPerfCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AccessSwitchVdslVturPerfCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_AccessSwitchVdslVturPerfCurr15MinTimeElapsed_Object = MibTableColumn
accessSwitchVdslVturPerfCurr15MinTimeElapsed = _AccessSwitchVdslVturPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 7),
    _AccessSwitchVdslVturPerfCurr15MinTimeElapsed_Type()
)
accessSwitchVdslVturPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr15MinTimeElapsed.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr15MinLofs_Type = Counter32
_AccessSwitchVdslVturPerfCurr15MinLofs_Object = MibTableColumn
accessSwitchVdslVturPerfCurr15MinLofs = _AccessSwitchVdslVturPerfCurr15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 8),
    _AccessSwitchVdslVturPerfCurr15MinLofs_Type()
)
accessSwitchVdslVturPerfCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr15MinLofs.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr15MinLoss_Type = Counter32
_AccessSwitchVdslVturPerfCurr15MinLoss_Object = MibTableColumn
accessSwitchVdslVturPerfCurr15MinLoss = _AccessSwitchVdslVturPerfCurr15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 9),
    _AccessSwitchVdslVturPerfCurr15MinLoss_Type()
)
accessSwitchVdslVturPerfCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr15MinLoss.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr15MinLprs_Type = Counter32
_AccessSwitchVdslVturPerfCurr15MinLprs_Object = MibTableColumn
accessSwitchVdslVturPerfCurr15MinLprs = _AccessSwitchVdslVturPerfCurr15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 10),
    _AccessSwitchVdslVturPerfCurr15MinLprs_Type()
)
accessSwitchVdslVturPerfCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr15MinLprs.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr15MinESs_Type = Counter32
_AccessSwitchVdslVturPerfCurr15MinESs_Object = MibTableColumn
accessSwitchVdslVturPerfCurr15MinESs = _AccessSwitchVdslVturPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 11),
    _AccessSwitchVdslVturPerfCurr15MinESs_Type()
)
accessSwitchVdslVturPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr15MinESs.setStatus("mandatory")


class _AccessSwitchVdslVturPerfCurr1DayTimeElapsed_Type(Gauge32):
    """Custom type accessSwitchVdslVturPerfCurr1DayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AccessSwitchVdslVturPerfCurr1DayTimeElapsed_Type.__name__ = "Gauge32"
_AccessSwitchVdslVturPerfCurr1DayTimeElapsed_Object = MibTableColumn
accessSwitchVdslVturPerfCurr1DayTimeElapsed = _AccessSwitchVdslVturPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 12),
    _AccessSwitchVdslVturPerfCurr1DayTimeElapsed_Type()
)
accessSwitchVdslVturPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr1DayTimeElapsed.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr1DayLofs_Type = Counter32
_AccessSwitchVdslVturPerfCurr1DayLofs_Object = MibTableColumn
accessSwitchVdslVturPerfCurr1DayLofs = _AccessSwitchVdslVturPerfCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 13),
    _AccessSwitchVdslVturPerfCurr1DayLofs_Type()
)
accessSwitchVdslVturPerfCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr1DayLofs.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr1DayLoss_Type = Counter32
_AccessSwitchVdslVturPerfCurr1DayLoss_Object = MibTableColumn
accessSwitchVdslVturPerfCurr1DayLoss = _AccessSwitchVdslVturPerfCurr1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 14),
    _AccessSwitchVdslVturPerfCurr1DayLoss_Type()
)
accessSwitchVdslVturPerfCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr1DayLoss.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr1DayLprs_Type = Counter32
_AccessSwitchVdslVturPerfCurr1DayLprs_Object = MibTableColumn
accessSwitchVdslVturPerfCurr1DayLprs = _AccessSwitchVdslVturPerfCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 15),
    _AccessSwitchVdslVturPerfCurr1DayLprs_Type()
)
accessSwitchVdslVturPerfCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr1DayLprs.setStatus("mandatory")
_AccessSwitchVdslVturPerfCurr1DayESs_Type = Counter32
_AccessSwitchVdslVturPerfCurr1DayESs_Object = MibTableColumn
accessSwitchVdslVturPerfCurr1DayESs = _AccessSwitchVdslVturPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 16),
    _AccessSwitchVdslVturPerfCurr1DayESs_Type()
)
accessSwitchVdslVturPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfCurr1DayESs.setStatus("mandatory")


class _AccessSwitchVdslVturPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type accessSwitchVdslVturPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AccessSwitchVdslVturPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_AccessSwitchVdslVturPerfPrev1DayMoniSecs_Object = MibTableColumn
accessSwitchVdslVturPerfPrev1DayMoniSecs = _AccessSwitchVdslVturPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 17),
    _AccessSwitchVdslVturPerfPrev1DayMoniSecs_Type()
)
accessSwitchVdslVturPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfPrev1DayMoniSecs.setStatus("mandatory")
_AccessSwitchVdslVturPerfPrev1DayLofs_Type = Counter32
_AccessSwitchVdslVturPerfPrev1DayLofs_Object = MibTableColumn
accessSwitchVdslVturPerfPrev1DayLofs = _AccessSwitchVdslVturPerfPrev1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 18),
    _AccessSwitchVdslVturPerfPrev1DayLofs_Type()
)
accessSwitchVdslVturPerfPrev1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfPrev1DayLofs.setStatus("mandatory")
_AccessSwitchVdslVturPerfPrev1DayLoss_Type = Counter32
_AccessSwitchVdslVturPerfPrev1DayLoss_Object = MibTableColumn
accessSwitchVdslVturPerfPrev1DayLoss = _AccessSwitchVdslVturPerfPrev1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 19),
    _AccessSwitchVdslVturPerfPrev1DayLoss_Type()
)
accessSwitchVdslVturPerfPrev1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfPrev1DayLoss.setStatus("mandatory")
_AccessSwitchVdslVturPerfPrev1DayLprs_Type = Counter32
_AccessSwitchVdslVturPerfPrev1DayLprs_Object = MibTableColumn
accessSwitchVdslVturPerfPrev1DayLprs = _AccessSwitchVdslVturPerfPrev1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 20),
    _AccessSwitchVdslVturPerfPrev1DayLprs_Type()
)
accessSwitchVdslVturPerfPrev1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfPrev1DayLprs.setStatus("mandatory")
_AccessSwitchVdslVturPerfPrev1DayESs_Type = Counter32
_AccessSwitchVdslVturPerfPrev1DayESs_Object = MibTableColumn
accessSwitchVdslVturPerfPrev1DayESs = _AccessSwitchVdslVturPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 7, 1, 21),
    _AccessSwitchVdslVturPerfPrev1DayESs_Type()
)
accessSwitchVdslVturPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturPerfPrev1DayESs.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalTable_Object = MibTable
accessSwitchVdslVtuoIntervalTable = _AccessSwitchVdslVtuoIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalTable.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalEntry_Object = MibTableRow
accessSwitchVdslVtuoIntervalEntry = _AccessSwitchVdslVtuoIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1)
)
accessSwitchVdslVtuoIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VDSLLINE-MIB", "accessSwitchVdslVtuoIntervalNumber"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalEntry.setStatus("mandatory")


class _AccessSwitchVdslVtuoIntervalNumber_Type(Integer32):
    """Custom type accessSwitchVdslVtuoIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AccessSwitchVdslVtuoIntervalNumber_Type.__name__ = "Integer32"
_AccessSwitchVdslVtuoIntervalNumber_Object = MibTableColumn
accessSwitchVdslVtuoIntervalNumber = _AccessSwitchVdslVtuoIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 1),
    _AccessSwitchVdslVtuoIntervalNumber_Type()
)
accessSwitchVdslVtuoIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalNumber.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalLofs_Type = Counter32
_AccessSwitchVdslVtuoIntervalLofs_Object = MibTableColumn
accessSwitchVdslVtuoIntervalLofs = _AccessSwitchVdslVtuoIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 2),
    _AccessSwitchVdslVtuoIntervalLofs_Type()
)
accessSwitchVdslVtuoIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalLofs.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalLoss_Type = Counter32
_AccessSwitchVdslVtuoIntervalLoss_Object = MibTableColumn
accessSwitchVdslVtuoIntervalLoss = _AccessSwitchVdslVtuoIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 3),
    _AccessSwitchVdslVtuoIntervalLoss_Type()
)
accessSwitchVdslVtuoIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalLoss.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalLols_Type = Counter32
_AccessSwitchVdslVtuoIntervalLols_Object = MibTableColumn
accessSwitchVdslVtuoIntervalLols = _AccessSwitchVdslVtuoIntervalLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 4),
    _AccessSwitchVdslVtuoIntervalLols_Type()
)
accessSwitchVdslVtuoIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalLols.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalLprs_Type = Counter32
_AccessSwitchVdslVtuoIntervalLprs_Object = MibTableColumn
accessSwitchVdslVtuoIntervalLprs = _AccessSwitchVdslVtuoIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 5),
    _AccessSwitchVdslVtuoIntervalLprs_Type()
)
accessSwitchVdslVtuoIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalLprs.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalESs_Type = Counter32
_AccessSwitchVdslVtuoIntervalESs_Object = MibTableColumn
accessSwitchVdslVtuoIntervalESs = _AccessSwitchVdslVtuoIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 6),
    _AccessSwitchVdslVtuoIntervalESs_Type()
)
accessSwitchVdslVtuoIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalESs.setStatus("mandatory")
_AccessSwitchVdslVtuoIntervalInits_Type = Counter32
_AccessSwitchVdslVtuoIntervalInits_Object = MibTableColumn
accessSwitchVdslVtuoIntervalInits = _AccessSwitchVdslVtuoIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 7),
    _AccessSwitchVdslVtuoIntervalInits_Type()
)
accessSwitchVdslVtuoIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalInits.setStatus("mandatory")


class _AccessSwitchVdslVtuoIntervalValidData_Type(Integer32):
    """Custom type accessSwitchVdslVtuoIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AccessSwitchVdslVtuoIntervalValidData_Type.__name__ = "Integer32"
_AccessSwitchVdslVtuoIntervalValidData_Object = MibTableColumn
accessSwitchVdslVtuoIntervalValidData = _AccessSwitchVdslVtuoIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 8, 1, 8),
    _AccessSwitchVdslVtuoIntervalValidData_Type()
)
accessSwitchVdslVtuoIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoIntervalValidData.setStatus("mandatory")
_AccessSwitchVdslVturIntervalTable_Object = MibTable
accessSwitchVdslVturIntervalTable = _AccessSwitchVdslVturIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalTable.setStatus("mandatory")
_AccessSwitchVdslVturIntervalEntry_Object = MibTableRow
accessSwitchVdslVturIntervalEntry = _AccessSwitchVdslVturIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1)
)
accessSwitchVdslVturIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-VDSLLINE-MIB", "accessSwitchVdslVturIntervalNumber"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalEntry.setStatus("mandatory")


class _AccessSwitchVdslVturIntervalNumber_Type(Integer32):
    """Custom type accessSwitchVdslVturIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AccessSwitchVdslVturIntervalNumber_Type.__name__ = "Integer32"
_AccessSwitchVdslVturIntervalNumber_Object = MibTableColumn
accessSwitchVdslVturIntervalNumber = _AccessSwitchVdslVturIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1, 1),
    _AccessSwitchVdslVturIntervalNumber_Type()
)
accessSwitchVdslVturIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalNumber.setStatus("mandatory")
_AccessSwitchVdslVturIntervalLofs_Type = Counter32
_AccessSwitchVdslVturIntervalLofs_Object = MibTableColumn
accessSwitchVdslVturIntervalLofs = _AccessSwitchVdslVturIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1, 2),
    _AccessSwitchVdslVturIntervalLofs_Type()
)
accessSwitchVdslVturIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalLofs.setStatus("mandatory")
_AccessSwitchVdslVturIntervalLoss_Type = Counter32
_AccessSwitchVdslVturIntervalLoss_Object = MibTableColumn
accessSwitchVdslVturIntervalLoss = _AccessSwitchVdslVturIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1, 3),
    _AccessSwitchVdslVturIntervalLoss_Type()
)
accessSwitchVdslVturIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalLoss.setStatus("mandatory")
_AccessSwitchVdslVturIntervalLprs_Type = Counter32
_AccessSwitchVdslVturIntervalLprs_Object = MibTableColumn
accessSwitchVdslVturIntervalLprs = _AccessSwitchVdslVturIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1, 4),
    _AccessSwitchVdslVturIntervalLprs_Type()
)
accessSwitchVdslVturIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalLprs.setStatus("mandatory")
_AccessSwitchVdslVturIntervalESs_Type = Counter32
_AccessSwitchVdslVturIntervalESs_Object = MibTableColumn
accessSwitchVdslVturIntervalESs = _AccessSwitchVdslVturIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1, 5),
    _AccessSwitchVdslVturIntervalESs_Type()
)
accessSwitchVdslVturIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalESs.setStatus("mandatory")


class _AccessSwitchVdslVturIntervalValidData_Type(Integer32):
    """Custom type accessSwitchVdslVturIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AccessSwitchVdslVturIntervalValidData_Type.__name__ = "Integer32"
_AccessSwitchVdslVturIntervalValidData_Object = MibTableColumn
accessSwitchVdslVturIntervalValidData = _AccessSwitchVdslVturIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 9, 1, 6),
    _AccessSwitchVdslVturIntervalValidData_Type()
)
accessSwitchVdslVturIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturIntervalValidData.setStatus("mandatory")
_AccessSwitchVdslLineConfProfileTable_Object = MibTable
accessSwitchVdslLineConfProfileTable = _AccessSwitchVdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    accessSwitchVdslLineConfProfileTable.setStatus("mandatory")
_AccessSwitchVdslLineConfProfileEntry_Object = MibTableRow
accessSwitchVdslLineConfProfileEntry = _AccessSwitchVdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1)
)
accessSwitchVdslLineConfProfileEntry.setIndexNames(
    (1, "ZYXEL-VDSLLINE-MIB", "accessSwitchVdslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslLineConfProfileEntry.setStatus("mandatory")


class _AccessSwitchVdslLineConfProfileName_Type(DisplayString):
    """Custom type accessSwitchVdslLineConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AccessSwitchVdslLineConfProfileName_Type.__name__ = "DisplayString"
_AccessSwitchVdslLineConfProfileName_Object = MibTableColumn
accessSwitchVdslLineConfProfileName = _AccessSwitchVdslLineConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 1),
    _AccessSwitchVdslLineConfProfileName_Type()
)
accessSwitchVdslLineConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessSwitchVdslLineConfProfileName.setStatus("mandatory")


class _AccessSwitchVdslLineConfMode_Type(Integer32):
    """Custom type accessSwitchVdslLineConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenBase-S", 0),
          ("ansi", 1),
          ("etsi", 2))
    )


_AccessSwitchVdslLineConfMode_Type.__name__ = "Integer32"
_AccessSwitchVdslLineConfMode_Object = MibTableColumn
accessSwitchVdslLineConfMode = _AccessSwitchVdslLineConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 2),
    _AccessSwitchVdslLineConfMode_Type()
)
accessSwitchVdslLineConfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslLineConfMode.setStatus("mandatory")
_AccessSwitchVdslVtuoConfRate_Type = Integer32
_AccessSwitchVdslVtuoConfRate_Object = MibTableColumn
accessSwitchVdslVtuoConfRate = _AccessSwitchVdslVtuoConfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 3),
    _AccessSwitchVdslVtuoConfRate_Type()
)
accessSwitchVdslVtuoConfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoConfRate.setStatus("mandatory")
_AccessSwitchVdslVtuoConfTargetSnrMgn_Type = Integer32
_AccessSwitchVdslVtuoConfTargetSnrMgn_Object = MibTableColumn
accessSwitchVdslVtuoConfTargetSnrMgn = _AccessSwitchVdslVtuoConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 4),
    _AccessSwitchVdslVtuoConfTargetSnrMgn_Type()
)
accessSwitchVdslVtuoConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoConfTargetSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVtuoConfMaxSnrMgn_Type = Integer32
_AccessSwitchVdslVtuoConfMaxSnrMgn_Object = MibTableColumn
accessSwitchVdslVtuoConfMaxSnrMgn = _AccessSwitchVdslVtuoConfMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 5),
    _AccessSwitchVdslVtuoConfMaxSnrMgn_Type()
)
accessSwitchVdslVtuoConfMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoConfMaxSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVtuoConfMinSnrMgn_Type = Integer32
_AccessSwitchVdslVtuoConfMinSnrMgn_Object = MibTableColumn
accessSwitchVdslVtuoConfMinSnrMgn = _AccessSwitchVdslVtuoConfMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 6),
    _AccessSwitchVdslVtuoConfMinSnrMgn_Type()
)
accessSwitchVdslVtuoConfMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoConfMinSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVturConfRate_Type = Integer32
_AccessSwitchVdslVturConfRate_Object = MibTableColumn
accessSwitchVdslVturConfRate = _AccessSwitchVdslVturConfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 7),
    _AccessSwitchVdslVturConfRate_Type()
)
accessSwitchVdslVturConfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVturConfRate.setStatus("mandatory")
_AccessSwitchVdslVturConfTargetSnrMgn_Type = Integer32
_AccessSwitchVdslVturConfTargetSnrMgn_Object = MibTableColumn
accessSwitchVdslVturConfTargetSnrMgn = _AccessSwitchVdslVturConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 8),
    _AccessSwitchVdslVturConfTargetSnrMgn_Type()
)
accessSwitchVdslVturConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVturConfTargetSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVturConfMaxSnrMgn_Type = Integer32
_AccessSwitchVdslVturConfMaxSnrMgn_Object = MibTableColumn
accessSwitchVdslVturConfMaxSnrMgn = _AccessSwitchVdslVturConfMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 9),
    _AccessSwitchVdslVturConfMaxSnrMgn_Type()
)
accessSwitchVdslVturConfMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVturConfMaxSnrMgn.setStatus("mandatory")
_AccessSwitchVdslVturConfMinSnrMgn_Type = Integer32
_AccessSwitchVdslVturConfMinSnrMgn_Object = MibTableColumn
accessSwitchVdslVturConfMinSnrMgn = _AccessSwitchVdslVturConfMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 10),
    _AccessSwitchVdslVturConfMinSnrMgn_Type()
)
accessSwitchVdslVturConfMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslVturConfMinSnrMgn.setStatus("mandatory")
_AccessSwitchVdslLineConfProfileRowStatus_Type = RowStatus
_AccessSwitchVdslLineConfProfileRowStatus_Object = MibTableColumn
accessSwitchVdslLineConfProfileRowStatus = _AccessSwitchVdslLineConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 10, 1, 11),
    _AccessSwitchVdslLineConfProfileRowStatus_Type()
)
accessSwitchVdslLineConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessSwitchVdslLineConfProfileRowStatus.setStatus("mandatory")
_VesMaxNumOfProfiles_Type = Integer32
_VesMaxNumOfProfiles_Object = MibScalar
vesMaxNumOfProfiles = _VesMaxNumOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 1, 11),
    _VesMaxNumOfProfiles_Type()
)
vesMaxNumOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vesMaxNumOfProfiles.setStatus("mandatory")
_AccessSwitchVdslLCSMib_ObjectIdentity = ObjectIdentity
accessSwitchVdslLCSMib = _AccessSwitchVdslLCSMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2)
)
_AccessSwitchVdslLCSMibObjects_ObjectIdentity = ObjectIdentity
accessSwitchVdslLCSMibObjects = _AccessSwitchVdslLCSMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 1)
)
_AccessSwitchVdslLCSQam_ObjectIdentity = ObjectIdentity
accessSwitchVdslLCSQam = _AccessSwitchVdslLCSQam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2)
)
_AccessSwitchVdslVtuoQamTable_Object = MibTable
accessSwitchVdslVtuoQamTable = _AccessSwitchVdslVtuoQamTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoQamTable.setStatus("mandatory")
_AccessSwitchVdslVtuoQamEntry_Object = MibTableRow
accessSwitchVdslVtuoQamEntry = _AccessSwitchVdslVtuoQamEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 1, 1)
)
accessSwitchVdslVtuoQamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoQamEntry.setStatus("mandatory")
_AccessSwitchVdslVtuoQamConstellation_Type = Integer32
_AccessSwitchVdslVtuoQamConstellation_Object = MibTableColumn
accessSwitchVdslVtuoQamConstellation = _AccessSwitchVdslVtuoQamConstellation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 1, 1, 1),
    _AccessSwitchVdslVtuoQamConstellation_Type()
)
accessSwitchVdslVtuoQamConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoQamConstellation.setStatus("mandatory")
_AccessSwitchVdslVtuoQamInterpolation_Type = Integer32
_AccessSwitchVdslVtuoQamInterpolation_Object = MibTableColumn
accessSwitchVdslVtuoQamInterpolation = _AccessSwitchVdslVtuoQamInterpolation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 1, 1, 2),
    _AccessSwitchVdslVtuoQamInterpolation_Type()
)
accessSwitchVdslVtuoQamInterpolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoQamInterpolation.setStatus("mandatory")
_AccessSwitchVdslVtuoQamFc_Type = Integer32
_AccessSwitchVdslVtuoQamFc_Object = MibTableColumn
accessSwitchVdslVtuoQamFc = _AccessSwitchVdslVtuoQamFc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 1, 1, 3),
    _AccessSwitchVdslVtuoQamFc_Type()
)
accessSwitchVdslVtuoQamFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVtuoQamFc.setStatus("mandatory")
_AccessSwitchVdslVturQamTable_Object = MibTable
accessSwitchVdslVturQamTable = _AccessSwitchVdslVturQamTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturQamTable.setStatus("mandatory")
_AccessSwitchVdslVturQamEntry_Object = MibTableRow
accessSwitchVdslVturQamEntry = _AccessSwitchVdslVturQamEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 2, 1)
)
accessSwitchVdslVturQamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVdslVturQamEntry.setStatus("mandatory")
_AccessSwitchVdslVturQamConstellation_Type = Integer32
_AccessSwitchVdslVturQamConstellation_Object = MibTableColumn
accessSwitchVdslVturQamConstellation = _AccessSwitchVdslVturQamConstellation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 2, 1, 1),
    _AccessSwitchVdslVturQamConstellation_Type()
)
accessSwitchVdslVturQamConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturQamConstellation.setStatus("mandatory")
_AccessSwitchVdslVturQamInterpolation_Type = Integer32
_AccessSwitchVdslVturQamInterpolation_Object = MibTableColumn
accessSwitchVdslVturQamInterpolation = _AccessSwitchVdslVturQamInterpolation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 2, 1, 2),
    _AccessSwitchVdslVturQamInterpolation_Type()
)
accessSwitchVdslVturQamInterpolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturQamInterpolation.setStatus("mandatory")
_AccessSwitchVdslVturQamFc_Type = Integer32
_AccessSwitchVdslVturQamFc_Object = MibTableColumn
accessSwitchVdslVturQamFc = _AccessSwitchVdslVturQamFc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 1, 1, 2, 2, 2, 1, 3),
    _AccessSwitchVdslVturQamFc_Type()
)
accessSwitchVdslVturQamFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVdslVturQamFc.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VDSLLINE-MIB",
    **{"accessSwitchVdslLineMib": accessSwitchVdslLineMib,
       "accessSwitchVdslLineMibObjects": accessSwitchVdslLineMibObjects,
       "accessSwitchVdslLineTable": accessSwitchVdslLineTable,
       "accessSwitchVdslLineEntry": accessSwitchVdslLineEntry,
       "accessSwitchVdslLineCoding": accessSwitchVdslLineCoding,
       "accessSwitchVdslLineDiscCount": accessSwitchVdslLineDiscCount,
       "accessSwitchVdslLineConfProfile": accessSwitchVdslLineConfProfile,
       "accessSwitchVdslVtuoPhysTable": accessSwitchVdslVtuoPhysTable,
       "accessSwitchVdslVtuoPhysEntry": accessSwitchVdslVtuoPhysEntry,
       "accessSwitchVdslVtuoCurrSnrMgn": accessSwitchVdslVtuoCurrSnrMgn,
       "accessSwitchVdslVtuoCurrMse": accessSwitchVdslVtuoCurrMse,
       "accessSwitchVdslVtuoCurrPsd": accessSwitchVdslVtuoCurrPsd,
       "accessSwitchVdslVtuoCurrRsErr": accessSwitchVdslVtuoCurrRsErr,
       "accessSwitchVdslVtuoCurrAtn": accessSwitchVdslVtuoCurrAtn,
       "accessSwitchVdslVtuoCurrOutputPwr": accessSwitchVdslVtuoCurrOutputPwr,
       "accessSwitchVdslVtuoCurrRate": accessSwitchVdslVtuoCurrRate,
       "accessSwitchVdslVtuoCurrAttainableRate": accessSwitchVdslVtuoCurrAttainableRate,
       "accessSwitchVdslVtuoCurrStatus": accessSwitchVdslVtuoCurrStatus,
       "accessSwitchVdslVturPhysTable": accessSwitchVdslVturPhysTable,
       "accessSwitchVdslVturPhysEntry": accessSwitchVdslVturPhysEntry,
       "accessSwitchVdslVturCurrSnrMgn": accessSwitchVdslVturCurrSnrMgn,
       "accessSwitchVdslVturCurrMse": accessSwitchVdslVturCurrMse,
       "accessSwitchVdslVturCurrPsd": accessSwitchVdslVturCurrPsd,
       "accessSwitchVdslVturCurrRsErr": accessSwitchVdslVturCurrRsErr,
       "accessSwitchVdslVturCurrAtn": accessSwitchVdslVturCurrAtn,
       "accessSwitchVdslVturCurrOutputPwr": accessSwitchVdslVturCurrOutputPwr,
       "accessSwitchVdslVturCurrRate": accessSwitchVdslVturCurrRate,
       "accessSwitchVdslVturCurrAttainableRate": accessSwitchVdslVturCurrAttainableRate,
       "accessSwitchVdslVturCurrStatus": accessSwitchVdslVturCurrStatus,
       "accessSwitchVdslVtuoInventoryTable": accessSwitchVdslVtuoInventoryTable,
       "accessSwitchVdslVtuoInventoryEntry": accessSwitchVdslVtuoInventoryEntry,
       "accessSwitchVdslVtuoInvSerialNumber": accessSwitchVdslVtuoInvSerialNumber,
       "accessSwitchVdslVtuoInvVendorID": accessSwitchVdslVtuoInvVendorID,
       "accessSwitchVdslVtuoInvVersionNumber": accessSwitchVdslVtuoInvVersionNumber,
       "accessSwitchVdslVturInventoryTable": accessSwitchVdslVturInventoryTable,
       "accessSwitchVdslVturInventoryEntry": accessSwitchVdslVturInventoryEntry,
       "accessSwitchVdslVturInvSerialNumber": accessSwitchVdslVturInvSerialNumber,
       "accessSwitchVdslVturInvVendorID": accessSwitchVdslVturInvVendorID,
       "accessSwitchVdslVturInvVersionNumber": accessSwitchVdslVturInvVersionNumber,
       "accessSwitchVdslVtuoPerfDataTable": accessSwitchVdslVtuoPerfDataTable,
       "accessSwitchVdslVtuoPerfDataEntry": accessSwitchVdslVtuoPerfDataEntry,
       "accessSwitchVdslVtuoPerfLofs": accessSwitchVdslVtuoPerfLofs,
       "accessSwitchVdslVtuoPerfLoss": accessSwitchVdslVtuoPerfLoss,
       "accessSwitchVdslVtuoPerfLols": accessSwitchVdslVtuoPerfLols,
       "accessSwitchVdslVtuoPerfLprs": accessSwitchVdslVtuoPerfLprs,
       "accessSwitchVdslVtuoPerfESs": accessSwitchVdslVtuoPerfESs,
       "accessSwitchVdslVtuoPerfInits": accessSwitchVdslVtuoPerfInits,
       "accessSwitchVdslVtuoPerfValidIntervals": accessSwitchVdslVtuoPerfValidIntervals,
       "accessSwitchVdslVtuoPerfInvalidIntervals": accessSwitchVdslVtuoPerfInvalidIntervals,
       "accessSwitchVdslVtuoPerfCurr15MinTimeElapsed": accessSwitchVdslVtuoPerfCurr15MinTimeElapsed,
       "accessSwitchVdslVtuoPerfCurr15MinLofs": accessSwitchVdslVtuoPerfCurr15MinLofs,
       "accessSwitchVdslVtuoPerfCurr15MinLoss": accessSwitchVdslVtuoPerfCurr15MinLoss,
       "accessSwitchVdslVtuoPerfCurr15MinLols": accessSwitchVdslVtuoPerfCurr15MinLols,
       "accessSwitchVdslVtuoPerfCurr15MinLprs": accessSwitchVdslVtuoPerfCurr15MinLprs,
       "accessSwitchVdslVtuoPerfCurr15MinESs": accessSwitchVdslVtuoPerfCurr15MinESs,
       "accessSwitchVdslVtuoPerfCurr15MinInits": accessSwitchVdslVtuoPerfCurr15MinInits,
       "accessSwitchVdslVtuoPerfCurr1DayTimeElapsed": accessSwitchVdslVtuoPerfCurr1DayTimeElapsed,
       "accessSwitchVdslVtuoPerfCurr1DayLofs": accessSwitchVdslVtuoPerfCurr1DayLofs,
       "accessSwitchVdslVtuoPerfCurr1DayLoss": accessSwitchVdslVtuoPerfCurr1DayLoss,
       "accessSwitchVdslVtuoPerfCurr1DayLols": accessSwitchVdslVtuoPerfCurr1DayLols,
       "accessSwitchVdslVtuoPerfCurr1DayLprs": accessSwitchVdslVtuoPerfCurr1DayLprs,
       "accessSwitchVdslVtuoPerfCurr1DayESs": accessSwitchVdslVtuoPerfCurr1DayESs,
       "accessSwitchVdslVtuoPerfCurr1DayInits": accessSwitchVdslVtuoPerfCurr1DayInits,
       "accessSwitchVdslVtuoPerfPrev1DayMoniSecs": accessSwitchVdslVtuoPerfPrev1DayMoniSecs,
       "accessSwitchVdslVtuoPerfPrev1DayLofs": accessSwitchVdslVtuoPerfPrev1DayLofs,
       "accessSwitchVdslVtuoPerfPrev1DayLoss": accessSwitchVdslVtuoPerfPrev1DayLoss,
       "accessSwitchVdslVtuoPerfPrev1DayLols": accessSwitchVdslVtuoPerfPrev1DayLols,
       "accessSwitchVdslVtuoPerfPrev1DayLprs": accessSwitchVdslVtuoPerfPrev1DayLprs,
       "accessSwitchVdslVtuoPerfPrev1DayESs": accessSwitchVdslVtuoPerfPrev1DayESs,
       "accessSwitchVdslVtuoPerfPrev1DayInits": accessSwitchVdslVtuoPerfPrev1DayInits,
       "accessSwitchVdslVturPerfDataTable": accessSwitchVdslVturPerfDataTable,
       "accessSwitchVdslVturPerfDataEntry": accessSwitchVdslVturPerfDataEntry,
       "accessSwitchVdslVturPerfLofs": accessSwitchVdslVturPerfLofs,
       "accessSwitchVdslVturPerfLoss": accessSwitchVdslVturPerfLoss,
       "accessSwitchVdslVturPerfLprs": accessSwitchVdslVturPerfLprs,
       "accessSwitchVdslVturPerfESs": accessSwitchVdslVturPerfESs,
       "accessSwitchVdslVturPerfValidIntervals": accessSwitchVdslVturPerfValidIntervals,
       "accessSwitchVdslVturPerfInvalidIntervals": accessSwitchVdslVturPerfInvalidIntervals,
       "accessSwitchVdslVturPerfCurr15MinTimeElapsed": accessSwitchVdslVturPerfCurr15MinTimeElapsed,
       "accessSwitchVdslVturPerfCurr15MinLofs": accessSwitchVdslVturPerfCurr15MinLofs,
       "accessSwitchVdslVturPerfCurr15MinLoss": accessSwitchVdslVturPerfCurr15MinLoss,
       "accessSwitchVdslVturPerfCurr15MinLprs": accessSwitchVdslVturPerfCurr15MinLprs,
       "accessSwitchVdslVturPerfCurr15MinESs": accessSwitchVdslVturPerfCurr15MinESs,
       "accessSwitchVdslVturPerfCurr1DayTimeElapsed": accessSwitchVdslVturPerfCurr1DayTimeElapsed,
       "accessSwitchVdslVturPerfCurr1DayLofs": accessSwitchVdslVturPerfCurr1DayLofs,
       "accessSwitchVdslVturPerfCurr1DayLoss": accessSwitchVdslVturPerfCurr1DayLoss,
       "accessSwitchVdslVturPerfCurr1DayLprs": accessSwitchVdslVturPerfCurr1DayLprs,
       "accessSwitchVdslVturPerfCurr1DayESs": accessSwitchVdslVturPerfCurr1DayESs,
       "accessSwitchVdslVturPerfPrev1DayMoniSecs": accessSwitchVdslVturPerfPrev1DayMoniSecs,
       "accessSwitchVdslVturPerfPrev1DayLofs": accessSwitchVdslVturPerfPrev1DayLofs,
       "accessSwitchVdslVturPerfPrev1DayLoss": accessSwitchVdslVturPerfPrev1DayLoss,
       "accessSwitchVdslVturPerfPrev1DayLprs": accessSwitchVdslVturPerfPrev1DayLprs,
       "accessSwitchVdslVturPerfPrev1DayESs": accessSwitchVdslVturPerfPrev1DayESs,
       "accessSwitchVdslVtuoIntervalTable": accessSwitchVdslVtuoIntervalTable,
       "accessSwitchVdslVtuoIntervalEntry": accessSwitchVdslVtuoIntervalEntry,
       "accessSwitchVdslVtuoIntervalNumber": accessSwitchVdslVtuoIntervalNumber,
       "accessSwitchVdslVtuoIntervalLofs": accessSwitchVdslVtuoIntervalLofs,
       "accessSwitchVdslVtuoIntervalLoss": accessSwitchVdslVtuoIntervalLoss,
       "accessSwitchVdslVtuoIntervalLols": accessSwitchVdslVtuoIntervalLols,
       "accessSwitchVdslVtuoIntervalLprs": accessSwitchVdslVtuoIntervalLprs,
       "accessSwitchVdslVtuoIntervalESs": accessSwitchVdslVtuoIntervalESs,
       "accessSwitchVdslVtuoIntervalInits": accessSwitchVdslVtuoIntervalInits,
       "accessSwitchVdslVtuoIntervalValidData": accessSwitchVdslVtuoIntervalValidData,
       "accessSwitchVdslVturIntervalTable": accessSwitchVdslVturIntervalTable,
       "accessSwitchVdslVturIntervalEntry": accessSwitchVdslVturIntervalEntry,
       "accessSwitchVdslVturIntervalNumber": accessSwitchVdslVturIntervalNumber,
       "accessSwitchVdslVturIntervalLofs": accessSwitchVdslVturIntervalLofs,
       "accessSwitchVdslVturIntervalLoss": accessSwitchVdslVturIntervalLoss,
       "accessSwitchVdslVturIntervalLprs": accessSwitchVdslVturIntervalLprs,
       "accessSwitchVdslVturIntervalESs": accessSwitchVdslVturIntervalESs,
       "accessSwitchVdslVturIntervalValidData": accessSwitchVdslVturIntervalValidData,
       "accessSwitchVdslLineConfProfileTable": accessSwitchVdslLineConfProfileTable,
       "accessSwitchVdslLineConfProfileEntry": accessSwitchVdslLineConfProfileEntry,
       "accessSwitchVdslLineConfProfileName": accessSwitchVdslLineConfProfileName,
       "accessSwitchVdslLineConfMode": accessSwitchVdslLineConfMode,
       "accessSwitchVdslVtuoConfRate": accessSwitchVdslVtuoConfRate,
       "accessSwitchVdslVtuoConfTargetSnrMgn": accessSwitchVdslVtuoConfTargetSnrMgn,
       "accessSwitchVdslVtuoConfMaxSnrMgn": accessSwitchVdslVtuoConfMaxSnrMgn,
       "accessSwitchVdslVtuoConfMinSnrMgn": accessSwitchVdslVtuoConfMinSnrMgn,
       "accessSwitchVdslVturConfRate": accessSwitchVdslVturConfRate,
       "accessSwitchVdslVturConfTargetSnrMgn": accessSwitchVdslVturConfTargetSnrMgn,
       "accessSwitchVdslVturConfMaxSnrMgn": accessSwitchVdslVturConfMaxSnrMgn,
       "accessSwitchVdslVturConfMinSnrMgn": accessSwitchVdslVturConfMinSnrMgn,
       "accessSwitchVdslLineConfProfileRowStatus": accessSwitchVdslLineConfProfileRowStatus,
       "vesMaxNumOfProfiles": vesMaxNumOfProfiles,
       "accessSwitchVdslLCSMib": accessSwitchVdslLCSMib,
       "accessSwitchVdslLCSMibObjects": accessSwitchVdslLCSMibObjects,
       "accessSwitchVdslLCSQam": accessSwitchVdslLCSQam,
       "accessSwitchVdslVtuoQamTable": accessSwitchVdslVtuoQamTable,
       "accessSwitchVdslVtuoQamEntry": accessSwitchVdslVtuoQamEntry,
       "accessSwitchVdslVtuoQamConstellation": accessSwitchVdslVtuoQamConstellation,
       "accessSwitchVdslVtuoQamInterpolation": accessSwitchVdslVtuoQamInterpolation,
       "accessSwitchVdslVtuoQamFc": accessSwitchVdslVtuoQamFc,
       "accessSwitchVdslVturQamTable": accessSwitchVdslVturQamTable,
       "accessSwitchVdslVturQamEntry": accessSwitchVdslVturQamEntry,
       "accessSwitchVdslVturQamConstellation": accessSwitchVdslVturQamConstellation,
       "accessSwitchVdslVturQamInterpolation": accessSwitchVdslVturQamInterpolation,
       "accessSwitchVdslVturQamFc": accessSwitchVdslVturQamFc}
)
