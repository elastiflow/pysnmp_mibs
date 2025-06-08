# SNMP MIB module (EION-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/eion_34226/EION-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:58:48 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34226)
)
if mibBuilder.loadTexts:
    eionMIB.setRevisions(
        ("2013-07-31 00:00",
         "2013-03-31 00:00",
         "1970-01-01 00:00",
         "2011-10-31 00:00",
         "2010-12-31 00:00",
         "2009-05-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EionStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EionCmn_ObjectIdentity = ObjectIdentity
eionCmn = _EionCmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1)
)
_EionCmnNotifications_ObjectIdentity = ObjectIdentity
eionCmnNotifications = _EionCmnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 0)
)
_EionCmnObjects_ObjectIdentity = ObjectIdentity
eionCmnObjects = _EionCmnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1)
)
_EionCmnMacACLLastChange_Type = TimeTicks
_EionCmnMacACLLastChange_Object = MibScalar
eionCmnMacACLLastChange = _EionCmnMacACLLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 1),
    _EionCmnMacACLLastChange_Type()
)
eionCmnMacACLLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMacACLLastChange.setStatus("current")
_EionCmnMacACLNumRows_Type = Unsigned32
_EionCmnMacACLNumRows_Object = MibScalar
eionCmnMacACLNumRows = _EionCmnMacACLNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 2),
    _EionCmnMacACLNumRows_Type()
)
eionCmnMacACLNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMacACLNumRows.setStatus("current")
_EionCmnMacACLTable_Object = MibTable
eionCmnMacACLTable = _EionCmnMacACLTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eionCmnMacACLTable.setStatus("current")
_EionCmnMacACLEntry_Object = MibTableRow
eionCmnMacACLEntry = _EionCmnMacACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 3, 1)
)
eionCmnMacACLEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnMacACLIndex"),
)
if mibBuilder.loadTexts:
    eionCmnMacACLEntry.setStatus("current")
_EionCmnMacACLIndex_Type = Unsigned32
_EionCmnMacACLIndex_Object = MibTableColumn
eionCmnMacACLIndex = _EionCmnMacACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 3, 1, 1),
    _EionCmnMacACLIndex_Type()
)
eionCmnMacACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnMacACLIndex.setStatus("current")


class _EionCmnMacACLAddr_Type(DisplayString):
    """Custom type eionCmnMacACLAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_EionCmnMacACLAddr_Type.__name__ = "DisplayString"
_EionCmnMacACLAddr_Object = MibTableColumn
eionCmnMacACLAddr = _EionCmnMacACLAddr_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 3, 1, 2),
    _EionCmnMacACLAddr_Type()
)
eionCmnMacACLAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnMacACLAddr.setStatus("current")


class _EionCmnMacACLName_Type(DisplayString):
    """Custom type eionCmnMacACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EionCmnMacACLName_Type.__name__ = "DisplayString"
_EionCmnMacACLName_Object = MibTableColumn
eionCmnMacACLName = _EionCmnMacACLName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 3, 1, 3),
    _EionCmnMacACLName_Type()
)
eionCmnMacACLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnMacACLName.setStatus("current")


class _EionCmnMacACLRowStatus_Type(Integer32):
    """Custom type eionCmnMacACLRowStatus based on Integer32"""
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
        *(("create", 1),
          ("destroy", 2),
          ("add", 3),
          ("delete", 4),
          ("active", 5))
    )


_EionCmnMacACLRowStatus_Type.__name__ = "Integer32"
_EionCmnMacACLRowStatus_Object = MibTableColumn
eionCmnMacACLRowStatus = _EionCmnMacACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 3, 1, 4),
    _EionCmnMacACLRowStatus_Type()
)
eionCmnMacACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnMacACLRowStatus.setStatus("current")
_EionCmnBrdgLastChange_Type = TimeTicks
_EionCmnBrdgLastChange_Object = MibScalar
eionCmnBrdgLastChange = _EionCmnBrdgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 4),
    _EionCmnBrdgLastChange_Type()
)
eionCmnBrdgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgLastChange.setStatus("current")
_EionCmnBrdgNumRows_Type = Unsigned32
_EionCmnBrdgNumRows_Object = MibScalar
eionCmnBrdgNumRows = _EionCmnBrdgNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 5),
    _EionCmnBrdgNumRows_Type()
)
eionCmnBrdgNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgNumRows.setStatus("current")
_EionCmnBrdgTable_Object = MibTable
eionCmnBrdgTable = _EionCmnBrdgTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eionCmnBrdgTable.setStatus("current")
_EionCmnBrdgEntry_Object = MibTableRow
eionCmnBrdgEntry = _EionCmnBrdgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1)
)
eionCmnBrdgEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnBrdgIndex"),
)
if mibBuilder.loadTexts:
    eionCmnBrdgEntry.setStatus("current")
_EionCmnBrdgIndex_Type = Unsigned32
_EionCmnBrdgIndex_Object = MibTableColumn
eionCmnBrdgIndex = _EionCmnBrdgIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 1),
    _EionCmnBrdgIndex_Type()
)
eionCmnBrdgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnBrdgIndex.setStatus("current")


class _EionCmnBrdgName_Type(DisplayString):
    """Custom type eionCmnBrdgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EionCmnBrdgName_Type.__name__ = "DisplayString"
_EionCmnBrdgName_Object = MibTableColumn
eionCmnBrdgName = _EionCmnBrdgName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 2),
    _EionCmnBrdgName_Type()
)
eionCmnBrdgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgName.setStatus("current")


class _EionCmnBrdgAssPortName_Type(DisplayString):
    """Custom type eionCmnBrdgAssPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 272),
    )


_EionCmnBrdgAssPortName_Type.__name__ = "DisplayString"
_EionCmnBrdgAssPortName_Object = MibTableColumn
eionCmnBrdgAssPortName = _EionCmnBrdgAssPortName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 3),
    _EionCmnBrdgAssPortName_Type()
)
eionCmnBrdgAssPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgAssPortName.setStatus("current")


class _EionCmnBrdgId_Type(DisplayString):
    """Custom type eionCmnBrdgId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_EionCmnBrdgId_Type.__name__ = "DisplayString"
_EionCmnBrdgId_Object = MibTableColumn
eionCmnBrdgId = _EionCmnBrdgId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 4),
    _EionCmnBrdgId_Type()
)
eionCmnBrdgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgId.setStatus("current")
_EionCmnBrdgSTP_Type = TruthValue
_EionCmnBrdgSTP_Object = MibTableColumn
eionCmnBrdgSTP = _EionCmnBrdgSTP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 5),
    _EionCmnBrdgSTP_Type()
)
eionCmnBrdgSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgSTP.setStatus("current")
_EionCmnBrdgMTU_Type = Unsigned32
_EionCmnBrdgMTU_Object = MibTableColumn
eionCmnBrdgMTU = _EionCmnBrdgMTU_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 6),
    _EionCmnBrdgMTU_Type()
)
eionCmnBrdgMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnBrdgMTU.setStatus("current")
_EionCmnBrdgAging_Type = Unsigned32
_EionCmnBrdgAging_Object = MibTableColumn
eionCmnBrdgAging = _EionCmnBrdgAging_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 7),
    _EionCmnBrdgAging_Type()
)
eionCmnBrdgAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnBrdgAging.setStatus("current")
_EionCmnBrdgMulticast_Type = EionStatus
_EionCmnBrdgMulticast_Object = MibTableColumn
eionCmnBrdgMulticast = _EionCmnBrdgMulticast_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 6, 1, 8),
    _EionCmnBrdgMulticast_Type()
)
eionCmnBrdgMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnBrdgMulticast.setStatus("current")
_EionCmnBrdgFDBLastChange_Type = TimeTicks
_EionCmnBrdgFDBLastChange_Object = MibScalar
eionCmnBrdgFDBLastChange = _EionCmnBrdgFDBLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 7),
    _EionCmnBrdgFDBLastChange_Type()
)
eionCmnBrdgFDBLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgFDBLastChange.setStatus("current")
_EionCmnBrdgFDBNumRows_Type = Unsigned32
_EionCmnBrdgFDBNumRows_Object = MibScalar
eionCmnBrdgFDBNumRows = _EionCmnBrdgFDBNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 8),
    _EionCmnBrdgFDBNumRows_Type()
)
eionCmnBrdgFDBNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgFDBNumRows.setStatus("current")
_EionCmnBrdgFDBTable_Object = MibTable
eionCmnBrdgFDBTable = _EionCmnBrdgFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 9)
)
if mibBuilder.loadTexts:
    eionCmnBrdgFDBTable.setStatus("current")
_EionCmnBrdgFDBEntry_Object = MibTableRow
eionCmnBrdgFDBEntry = _EionCmnBrdgFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 9, 1)
)
eionCmnBrdgFDBEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnBrdgFDBIndex"),
)
if mibBuilder.loadTexts:
    eionCmnBrdgFDBEntry.setStatus("current")
_EionCmnBrdgFDBIndex_Type = Unsigned32
_EionCmnBrdgFDBIndex_Object = MibTableColumn
eionCmnBrdgFDBIndex = _EionCmnBrdgFDBIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 9, 1, 1),
    _EionCmnBrdgFDBIndex_Type()
)
eionCmnBrdgFDBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnBrdgFDBIndex.setStatus("current")


class _EionCmnBrdgFDBName_Type(DisplayString):
    """Custom type eionCmnBrdgFDBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EionCmnBrdgFDBName_Type.__name__ = "DisplayString"
_EionCmnBrdgFDBName_Object = MibTableColumn
eionCmnBrdgFDBName = _EionCmnBrdgFDBName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 9, 1, 2),
    _EionCmnBrdgFDBName_Type()
)
eionCmnBrdgFDBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgFDBName.setStatus("current")


class _EionCmnBrdgFDBMACId_Type(DisplayString):
    """Custom type eionCmnBrdgFDBMACId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EionCmnBrdgFDBMACId_Type.__name__ = "DisplayString"
_EionCmnBrdgFDBMACId_Object = MibTableColumn
eionCmnBrdgFDBMACId = _EionCmnBrdgFDBMACId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 9, 1, 3),
    _EionCmnBrdgFDBMACId_Type()
)
eionCmnBrdgFDBMACId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgFDBMACId.setStatus("current")
_EionCmnBrdgFDBIsLocal_Type = TruthValue
_EionCmnBrdgFDBIsLocal_Object = MibTableColumn
eionCmnBrdgFDBIsLocal = _EionCmnBrdgFDBIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 9, 1, 4),
    _EionCmnBrdgFDBIsLocal_Type()
)
eionCmnBrdgFDBIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnBrdgFDBIsLocal.setStatus("current")
_EionCmnDataVlanLastChange_Type = TimeTicks
_EionCmnDataVlanLastChange_Object = MibScalar
eionCmnDataVlanLastChange = _EionCmnDataVlanLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 10),
    _EionCmnDataVlanLastChange_Type()
)
eionCmnDataVlanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnDataVlanLastChange.setStatus("current")
_EionCmnDataVlanNumRows_Type = Unsigned32
_EionCmnDataVlanNumRows_Object = MibScalar
eionCmnDataVlanNumRows = _EionCmnDataVlanNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 11),
    _EionCmnDataVlanNumRows_Type()
)
eionCmnDataVlanNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnDataVlanNumRows.setStatus("current")
_EionCmnDataVlanTable_Object = MibTable
eionCmnDataVlanTable = _EionCmnDataVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 12)
)
if mibBuilder.loadTexts:
    eionCmnDataVlanTable.setStatus("current")
_EionCmnDataVlanEntry_Object = MibTableRow
eionCmnDataVlanEntry = _EionCmnDataVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 12, 1)
)
eionCmnDataVlanEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnDataVlanIndex"),
)
if mibBuilder.loadTexts:
    eionCmnDataVlanEntry.setStatus("current")
_EionCmnDataVlanIndex_Type = Unsigned32
_EionCmnDataVlanIndex_Object = MibTableColumn
eionCmnDataVlanIndex = _EionCmnDataVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 12, 1, 1),
    _EionCmnDataVlanIndex_Type()
)
eionCmnDataVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnDataVlanIndex.setStatus("current")
_EionCmnDataVlanId_Type = Unsigned32
_EionCmnDataVlanId_Object = MibTableColumn
eionCmnDataVlanId = _EionCmnDataVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 12, 1, 2),
    _EionCmnDataVlanId_Type()
)
eionCmnDataVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDataVlanId.setStatus("current")
_EionCmnDataVlanStatus_Type = EionStatus
_EionCmnDataVlanStatus_Object = MibTableColumn
eionCmnDataVlanStatus = _EionCmnDataVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 12, 1, 3),
    _EionCmnDataVlanStatus_Type()
)
eionCmnDataVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDataVlanStatus.setStatus("current")
_EionCmnMacVsNameLastChange_Type = TimeTicks
_EionCmnMacVsNameLastChange_Object = MibScalar
eionCmnMacVsNameLastChange = _EionCmnMacVsNameLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 13),
    _EionCmnMacVsNameLastChange_Type()
)
eionCmnMacVsNameLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMacVsNameLastChange.setStatus("current")
_EionCmnMacVsNameNumRows_Type = Unsigned32
_EionCmnMacVsNameNumRows_Object = MibScalar
eionCmnMacVsNameNumRows = _EionCmnMacVsNameNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 14),
    _EionCmnMacVsNameNumRows_Type()
)
eionCmnMacVsNameNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMacVsNameNumRows.setStatus("current")
_EionCmnMacVsNameTable_Object = MibTable
eionCmnMacVsNameTable = _EionCmnMacVsNameTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 15)
)
if mibBuilder.loadTexts:
    eionCmnMacVsNameTable.setStatus("current")
_EionCmnMacVsNameEntry_Object = MibTableRow
eionCmnMacVsNameEntry = _EionCmnMacVsNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 15, 1)
)
eionCmnMacVsNameEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnMacVsNameMacAddr"),
)
if mibBuilder.loadTexts:
    eionCmnMacVsNameEntry.setStatus("current")


class _EionCmnMacVsNameMacAddr_Type(DisplayString):
    """Custom type eionCmnMacVsNameMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_EionCmnMacVsNameMacAddr_Type.__name__ = "DisplayString"
_EionCmnMacVsNameMacAddr_Object = MibTableColumn
eionCmnMacVsNameMacAddr = _EionCmnMacVsNameMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 15, 1, 1),
    _EionCmnMacVsNameMacAddr_Type()
)
eionCmnMacVsNameMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnMacVsNameMacAddr.setStatus("current")


class _EionCmnMacVsNameName_Type(DisplayString):
    """Custom type eionCmnMacVsNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EionCmnMacVsNameName_Type.__name__ = "DisplayString"
_EionCmnMacVsNameName_Object = MibTableColumn
eionCmnMacVsNameName = _EionCmnMacVsNameName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 15, 1, 2),
    _EionCmnMacVsNameName_Type()
)
eionCmnMacVsNameName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnMacVsNameName.setStatus("current")
_EionCmnMacVsNameRowStatus_Type = RowStatus
_EionCmnMacVsNameRowStatus_Object = MibTableColumn
eionCmnMacVsNameRowStatus = _EionCmnMacVsNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 15, 1, 3),
    _EionCmnMacVsNameRowStatus_Type()
)
eionCmnMacVsNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnMacVsNameRowStatus.setStatus("current")
_EionCmnMgmtIPLastChange_Type = TimeTicks
_EionCmnMgmtIPLastChange_Object = MibScalar
eionCmnMgmtIPLastChange = _EionCmnMgmtIPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 16),
    _EionCmnMgmtIPLastChange_Type()
)
eionCmnMgmtIPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMgmtIPLastChange.setStatus("current")
_EionCmnMgmtIPNumRows_Type = Unsigned32
_EionCmnMgmtIPNumRows_Object = MibScalar
eionCmnMgmtIPNumRows = _EionCmnMgmtIPNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 17),
    _EionCmnMgmtIPNumRows_Type()
)
eionCmnMgmtIPNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMgmtIPNumRows.setStatus("current")
_EionCmnMgmtIPTable_Object = MibTable
eionCmnMgmtIPTable = _EionCmnMgmtIPTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 18)
)
if mibBuilder.loadTexts:
    eionCmnMgmtIPTable.setStatus("current")
_EionCmnMgmtIPEntry_Object = MibTableRow
eionCmnMgmtIPEntry = _EionCmnMgmtIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 18, 1)
)
eionCmnMgmtIPEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnBrdgIndex"),
)
if mibBuilder.loadTexts:
    eionCmnMgmtIPEntry.setStatus("current")
_EionCmnMgmtIP_Type = IpAddress
_EionCmnMgmtIP_Object = MibTableColumn
eionCmnMgmtIP = _EionCmnMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 18, 1, 1),
    _EionCmnMgmtIP_Type()
)
eionCmnMgmtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnMgmtIP.setStatus("current")
_EionCmnMgmtMask_Type = IpAddress
_EionCmnMgmtMask_Object = MibTableColumn
eionCmnMgmtMask = _EionCmnMgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 18, 1, 2),
    _EionCmnMgmtMask_Type()
)
eionCmnMgmtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnMgmtMask.setStatus("current")
_EionCmnMgmtVLANLastChange_Type = TimeTicks
_EionCmnMgmtVLANLastChange_Object = MibScalar
eionCmnMgmtVLANLastChange = _EionCmnMgmtVLANLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 19),
    _EionCmnMgmtVLANLastChange_Type()
)
eionCmnMgmtVLANLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMgmtVLANLastChange.setStatus("current")
_EionCmnMgmtVLANNumRows_Type = Unsigned32
_EionCmnMgmtVLANNumRows_Object = MibScalar
eionCmnMgmtVLANNumRows = _EionCmnMgmtVLANNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 20),
    _EionCmnMgmtVLANNumRows_Type()
)
eionCmnMgmtVLANNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnMgmtVLANNumRows.setStatus("current")
_EionCmnMgmtVLANTable_Object = MibTable
eionCmnMgmtVLANTable = _EionCmnMgmtVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 21)
)
if mibBuilder.loadTexts:
    eionCmnMgmtVLANTable.setStatus("current")
_EionCmnMgmtVLANEntry_Object = MibTableRow
eionCmnMgmtVLANEntry = _EionCmnMgmtVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 21, 1)
)
eionCmnMgmtVLANEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnMgmtVLANIndex"),
)
if mibBuilder.loadTexts:
    eionCmnMgmtVLANEntry.setStatus("current")
_EionCmnMgmtVLANIndex_Type = Unsigned32
_EionCmnMgmtVLANIndex_Object = MibTableColumn
eionCmnMgmtVLANIndex = _EionCmnMgmtVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 21, 1, 1),
    _EionCmnMgmtVLANIndex_Type()
)
eionCmnMgmtVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnMgmtVLANIndex.setStatus("current")
_EionCmnMgmtVLANID_Type = Unsigned32
_EionCmnMgmtVLANID_Object = MibTableColumn
eionCmnMgmtVLANID = _EionCmnMgmtVLANID_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 21, 1, 2),
    _EionCmnMgmtVLANID_Type()
)
eionCmnMgmtVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnMgmtVLANID.setStatus("current")
_EionCmnMgmtVLANStatus_Type = EionStatus
_EionCmnMgmtVLANStatus_Object = MibTableColumn
eionCmnMgmtVLANStatus = _EionCmnMgmtVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 21, 1, 3),
    _EionCmnMgmtVLANStatus_Type()
)
eionCmnMgmtVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnMgmtVLANStatus.setStatus("current")
_EionCmnDHCPLastChange_Type = TimeTicks
_EionCmnDHCPLastChange_Object = MibScalar
eionCmnDHCPLastChange = _EionCmnDHCPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 22),
    _EionCmnDHCPLastChange_Type()
)
eionCmnDHCPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnDHCPLastChange.setStatus("current")
_EionCmnDHCPNumRows_Type = Unsigned32
_EionCmnDHCPNumRows_Object = MibScalar
eionCmnDHCPNumRows = _EionCmnDHCPNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 23),
    _EionCmnDHCPNumRows_Type()
)
eionCmnDHCPNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnDHCPNumRows.setStatus("current")
_EionCmnDHCPTable_Object = MibTable
eionCmnDHCPTable = _EionCmnDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24)
)
if mibBuilder.loadTexts:
    eionCmnDHCPTable.setStatus("current")
_EionCmnDHCPEntry_Object = MibTableRow
eionCmnDHCPEntry = _EionCmnDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1)
)
eionCmnDHCPEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnDHCPIndex"),
)
if mibBuilder.loadTexts:
    eionCmnDHCPEntry.setStatus("current")
_EionCmnDHCPIndex_Type = Unsigned32
_EionCmnDHCPIndex_Object = MibTableColumn
eionCmnDHCPIndex = _EionCmnDHCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 1),
    _EionCmnDHCPIndex_Type()
)
eionCmnDHCPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnDHCPIndex.setStatus("current")


class _EionCmnDHCPInterfaceName_Type(DisplayString):
    """Custom type eionCmnDHCPInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EionCmnDHCPInterfaceName_Type.__name__ = "DisplayString"
_EionCmnDHCPInterfaceName_Object = MibTableColumn
eionCmnDHCPInterfaceName = _EionCmnDHCPInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 2),
    _EionCmnDHCPInterfaceName_Type()
)
eionCmnDHCPInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnDHCPInterfaceName.setStatus("current")
_EionCmnDHCPServerStatus_Type = EionStatus
_EionCmnDHCPServerStatus_Object = MibTableColumn
eionCmnDHCPServerStatus = _EionCmnDHCPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 3),
    _EionCmnDHCPServerStatus_Type()
)
eionCmnDHCPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPServerStatus.setStatus("current")
_EionCmnDHCPClientStatus_Type = EionStatus
_EionCmnDHCPClientStatus_Object = MibTableColumn
eionCmnDHCPClientStatus = _EionCmnDHCPClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 4),
    _EionCmnDHCPClientStatus_Type()
)
eionCmnDHCPClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPClientStatus.setStatus("current")
_EionCmnDHCPRouterIP_Type = IpAddress
_EionCmnDHCPRouterIP_Object = MibTableColumn
eionCmnDHCPRouterIP = _EionCmnDHCPRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 5),
    _EionCmnDHCPRouterIP_Type()
)
eionCmnDHCPRouterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPRouterIP.setStatus("current")
_EionCmnDHCPSubnetMask_Type = IpAddress
_EionCmnDHCPSubnetMask_Object = MibTableColumn
eionCmnDHCPSubnetMask = _EionCmnDHCPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 6),
    _EionCmnDHCPSubnetMask_Type()
)
eionCmnDHCPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPSubnetMask.setStatus("current")
_EionCmnDHCPStartIP_Type = IpAddress
_EionCmnDHCPStartIP_Object = MibTableColumn
eionCmnDHCPStartIP = _EionCmnDHCPStartIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 7),
    _EionCmnDHCPStartIP_Type()
)
eionCmnDHCPStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPStartIP.setStatus("current")
_EionCmnDHCPEndIP_Type = IpAddress
_EionCmnDHCPEndIP_Object = MibTableColumn
eionCmnDHCPEndIP = _EionCmnDHCPEndIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 8),
    _EionCmnDHCPEndIP_Type()
)
eionCmnDHCPEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPEndIP.setStatus("current")
_EionCmnDHCPDNSServerIP_Type = IpAddress
_EionCmnDHCPDNSServerIP_Object = MibTableColumn
eionCmnDHCPDNSServerIP = _EionCmnDHCPDNSServerIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 9),
    _EionCmnDHCPDNSServerIP_Type()
)
eionCmnDHCPDNSServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPDNSServerIP.setStatus("current")


class _EionCmnDHCPDomainName_Type(DisplayString):
    """Custom type eionCmnDHCPDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_EionCmnDHCPDomainName_Type.__name__ = "DisplayString"
_EionCmnDHCPDomainName_Object = MibTableColumn
eionCmnDHCPDomainName = _EionCmnDHCPDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 10),
    _EionCmnDHCPDomainName_Type()
)
eionCmnDHCPDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPDomainName.setStatus("current")
_EionCmnDHCPLeaseTime_Type = Unsigned32
_EionCmnDHCPLeaseTime_Object = MibTableColumn
eionCmnDHCPLeaseTime = _EionCmnDHCPLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 11),
    _EionCmnDHCPLeaseTime_Type()
)
eionCmnDHCPLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPLeaseTime.setStatus("current")
_EionCmnDHCPMinLeaseTime_Type = Unsigned32
_EionCmnDHCPMinLeaseTime_Object = MibTableColumn
eionCmnDHCPMinLeaseTime = _EionCmnDHCPMinLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 12),
    _EionCmnDHCPMinLeaseTime_Type()
)
eionCmnDHCPMinLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPMinLeaseTime.setStatus("current")
_EionCmnDHCPMaxNumLease_Type = Unsigned32
_EionCmnDHCPMaxNumLease_Object = MibTableColumn
eionCmnDHCPMaxNumLease = _EionCmnDHCPMaxNumLease_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 24, 1, 13),
    _EionCmnDHCPMaxNumLease_Type()
)
eionCmnDHCPMaxNumLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnDHCPMaxNumLease.setStatus("current")
_EionCmnSNMPLastChange_Type = TimeTicks
_EionCmnSNMPLastChange_Object = MibScalar
eionCmnSNMPLastChange = _EionCmnSNMPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 25),
    _EionCmnSNMPLastChange_Type()
)
eionCmnSNMPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSNMPLastChange.setStatus("current")
_EionCmnSNMPNumRows_Type = Unsigned32
_EionCmnSNMPNumRows_Object = MibScalar
eionCmnSNMPNumRows = _EionCmnSNMPNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 26),
    _EionCmnSNMPNumRows_Type()
)
eionCmnSNMPNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSNMPNumRows.setStatus("current")
_EionCmnSNMPTable_Object = MibTable
eionCmnSNMPTable = _EionCmnSNMPTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27)
)
if mibBuilder.loadTexts:
    eionCmnSNMPTable.setStatus("current")
_EionCmnSNMPEntry_Object = MibTableRow
eionCmnSNMPEntry = _EionCmnSNMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1)
)
eionCmnSNMPEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnSNMPIndex"),
)
if mibBuilder.loadTexts:
    eionCmnSNMPEntry.setStatus("current")
_EionCmnSNMPIndex_Type = Unsigned32
_EionCmnSNMPIndex_Object = MibTableColumn
eionCmnSNMPIndex = _EionCmnSNMPIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 1),
    _EionCmnSNMPIndex_Type()
)
eionCmnSNMPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnSNMPIndex.setStatus("current")
_EionCmnSNMPStatus_Type = EionStatus
_EionCmnSNMPStatus_Object = MibTableColumn
eionCmnSNMPStatus = _EionCmnSNMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 2),
    _EionCmnSNMPStatus_Type()
)
eionCmnSNMPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSNMPStatus.setStatus("current")


class _EionCmnSNMPLocation_Type(DisplayString):
    """Custom type eionCmnSNMPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EionCmnSNMPLocation_Type.__name__ = "DisplayString"
_EionCmnSNMPLocation_Object = MibTableColumn
eionCmnSNMPLocation = _EionCmnSNMPLocation_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 3),
    _EionCmnSNMPLocation_Type()
)
eionCmnSNMPLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPLocation.setStatus("current")


class _EionCmnSNMPRoCommunityName_Type(DisplayString):
    """Custom type eionCmnSNMPRoCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EionCmnSNMPRoCommunityName_Type.__name__ = "DisplayString"
_EionCmnSNMPRoCommunityName_Object = MibTableColumn
eionCmnSNMPRoCommunityName = _EionCmnSNMPRoCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 4),
    _EionCmnSNMPRoCommunityName_Type()
)
eionCmnSNMPRoCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPRoCommunityName.setStatus("current")


class _EionCmnSNMPRwCommunityName_Type(DisplayString):
    """Custom type eionCmnSNMPRwCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EionCmnSNMPRwCommunityName_Type.__name__ = "DisplayString"
_EionCmnSNMPRwCommunityName_Object = MibTableColumn
eionCmnSNMPRwCommunityName = _EionCmnSNMPRwCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 5),
    _EionCmnSNMPRwCommunityName_Type()
)
eionCmnSNMPRwCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPRwCommunityName.setStatus("current")


class _EionCmnSNMPContact_Type(DisplayString):
    """Custom type eionCmnSNMPContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EionCmnSNMPContact_Type.__name__ = "DisplayString"
_EionCmnSNMPContact_Object = MibTableColumn
eionCmnSNMPContact = _EionCmnSNMPContact_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 6),
    _EionCmnSNMPContact_Type()
)
eionCmnSNMPContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPContact.setStatus("current")
_EionCmnSNMPManagerIP_Type = IpAddress
_EionCmnSNMPManagerIP_Object = MibTableColumn
eionCmnSNMPManagerIP = _EionCmnSNMPManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 7),
    _EionCmnSNMPManagerIP_Type()
)
eionCmnSNMPManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPManagerIP.setStatus("current")
_EionCmnSNMPRSSIThres_Type = Integer32
_EionCmnSNMPRSSIThres_Object = MibTableColumn
eionCmnSNMPRSSIThres = _EionCmnSNMPRSSIThres_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 8),
    _EionCmnSNMPRSSIThres_Type()
)
eionCmnSNMPRSSIThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPRSSIThres.setStatus("current")
_EionCmnSNMPSendPktErrRateThres_Type = Unsigned32
_EionCmnSNMPSendPktErrRateThres_Object = MibTableColumn
eionCmnSNMPSendPktErrRateThres = _EionCmnSNMPSendPktErrRateThres_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 9),
    _EionCmnSNMPSendPktErrRateThres_Type()
)
eionCmnSNMPSendPktErrRateThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPSendPktErrRateThres.setStatus("current")
_EionCmnSNMPRcvPktErrRateThres_Type = Unsigned32
_EionCmnSNMPRcvPktErrRateThres_Object = MibTableColumn
eionCmnSNMPRcvPktErrRateThres = _EionCmnSNMPRcvPktErrRateThres_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 27, 1, 10),
    _EionCmnSNMPRcvPktErrRateThres_Type()
)
eionCmnSNMPRcvPktErrRateThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSNMPRcvPktErrRateThres.setStatus("current")
_EionCmnSyslogLastChange_Type = TimeTicks
_EionCmnSyslogLastChange_Object = MibScalar
eionCmnSyslogLastChange = _EionCmnSyslogLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 28),
    _EionCmnSyslogLastChange_Type()
)
eionCmnSyslogLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSyslogLastChange.setStatus("current")
_EionCmnSyslogNumRows_Type = Unsigned32
_EionCmnSyslogNumRows_Object = MibScalar
eionCmnSyslogNumRows = _EionCmnSyslogNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 29),
    _EionCmnSyslogNumRows_Type()
)
eionCmnSyslogNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSyslogNumRows.setStatus("current")
_EionCmnSyslogTable_Object = MibTable
eionCmnSyslogTable = _EionCmnSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 30)
)
if mibBuilder.loadTexts:
    eionCmnSyslogTable.setStatus("current")
_EionCmnSyslogEntry_Object = MibTableRow
eionCmnSyslogEntry = _EionCmnSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 30, 1)
)
eionCmnSyslogEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnSyslogIndex"),
)
if mibBuilder.loadTexts:
    eionCmnSyslogEntry.setStatus("current")
_EionCmnSyslogIndex_Type = Unsigned32
_EionCmnSyslogIndex_Object = MibTableColumn
eionCmnSyslogIndex = _EionCmnSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 30, 1, 1),
    _EionCmnSyslogIndex_Type()
)
eionCmnSyslogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnSyslogIndex.setStatus("current")
_EionCmnSyslogStatus_Type = EionStatus
_EionCmnSyslogStatus_Object = MibTableColumn
eionCmnSyslogStatus = _EionCmnSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 30, 1, 2),
    _EionCmnSyslogStatus_Type()
)
eionCmnSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSyslogStatus.setStatus("current")
_EionCmnSysDateLastChange_Type = TimeTicks
_EionCmnSysDateLastChange_Object = MibScalar
eionCmnSysDateLastChange = _EionCmnSysDateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 31),
    _EionCmnSysDateLastChange_Type()
)
eionCmnSysDateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSysDateLastChange.setStatus("current")
_EionCmnSysDateNumRows_Type = Unsigned32
_EionCmnSysDateNumRows_Object = MibScalar
eionCmnSysDateNumRows = _EionCmnSysDateNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 32),
    _EionCmnSysDateNumRows_Type()
)
eionCmnSysDateNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSysDateNumRows.setStatus("current")
_EionCmnSysDateTimeTable_Object = MibTable
eionCmnSysDateTimeTable = _EionCmnSysDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 33)
)
if mibBuilder.loadTexts:
    eionCmnSysDateTimeTable.setStatus("current")
_EionCmnSysDateTimeEntry_Object = MibTableRow
eionCmnSysDateTimeEntry = _EionCmnSysDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 33, 1)
)
eionCmnSysDateTimeEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnSysDateTimeIndex"),
)
if mibBuilder.loadTexts:
    eionCmnSysDateTimeEntry.setStatus("current")
_EionCmnSysDateTimeIndex_Type = Unsigned32
_EionCmnSysDateTimeIndex_Object = MibTableColumn
eionCmnSysDateTimeIndex = _EionCmnSysDateTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 33, 1, 1),
    _EionCmnSysDateTimeIndex_Type()
)
eionCmnSysDateTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnSysDateTimeIndex.setStatus("current")


class _EionCmnSysDate_Type(DisplayString):
    """Custom type eionCmnSysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EionCmnSysDate_Type.__name__ = "DisplayString"
_EionCmnSysDate_Object = MibTableColumn
eionCmnSysDate = _EionCmnSysDate_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 33, 1, 2),
    _EionCmnSysDate_Type()
)
eionCmnSysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSysDate.setStatus("current")


class _EionCmnSysTime_Type(DisplayString):
    """Custom type eionCmnSysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EionCmnSysTime_Type.__name__ = "DisplayString"
_EionCmnSysTime_Object = MibTableColumn
eionCmnSysTime = _EionCmnSysTime_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 33, 1, 3),
    _EionCmnSysTime_Type()
)
eionCmnSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSysTime.setStatus("current")
_EionCmnUploadLastChange_Type = TimeTicks
_EionCmnUploadLastChange_Object = MibScalar
eionCmnUploadLastChange = _EionCmnUploadLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 34),
    _EionCmnUploadLastChange_Type()
)
eionCmnUploadLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnUploadLastChange.setStatus("current")
_EionCmnUploadNumRows_Type = Unsigned32
_EionCmnUploadNumRows_Object = MibScalar
eionCmnUploadNumRows = _EionCmnUploadNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 35),
    _EionCmnUploadNumRows_Type()
)
eionCmnUploadNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnUploadNumRows.setStatus("current")
_EionCmnUploadTable_Object = MibTable
eionCmnUploadTable = _EionCmnUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36)
)
if mibBuilder.loadTexts:
    eionCmnUploadTable.setStatus("current")
_EionCmnUploadEntry_Object = MibTableRow
eionCmnUploadEntry = _EionCmnUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1)
)
eionCmnUploadEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnUploadIndex"),
)
if mibBuilder.loadTexts:
    eionCmnUploadEntry.setStatus("current")
_EionCmnUploadIndex_Type = Unsigned32
_EionCmnUploadIndex_Object = MibTableColumn
eionCmnUploadIndex = _EionCmnUploadIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1, 1),
    _EionCmnUploadIndex_Type()
)
eionCmnUploadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnUploadIndex.setStatus("current")
_EionCmnUploadIP_Type = IpAddress
_EionCmnUploadIP_Object = MibTableColumn
eionCmnUploadIP = _EionCmnUploadIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1, 2),
    _EionCmnUploadIP_Type()
)
eionCmnUploadIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnUploadIP.setStatus("current")


class _EionCmnUploadRowStatus_Type(Integer32):
    """Custom type eionCmnUploadRowStatus based on Integer32"""
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
        *(("saveConfigToLocalPC", 1),
          ("uploadConfig", 2),
          ("uploadFirmWare", 3),
          ("uploadLicence", 4),
          ("inProgress", 5))
    )


_EionCmnUploadRowStatus_Type.__name__ = "Integer32"
_EionCmnUploadRowStatus_Object = MibTableColumn
eionCmnUploadRowStatus = _EionCmnUploadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1, 3),
    _EionCmnUploadRowStatus_Type()
)
eionCmnUploadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnUploadRowStatus.setStatus("current")


class _EionCmnUploadUserName_Type(DisplayString):
    """Custom type eionCmnUploadUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EionCmnUploadUserName_Type.__name__ = "DisplayString"
_EionCmnUploadUserName_Object = MibTableColumn
eionCmnUploadUserName = _EionCmnUploadUserName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1, 4),
    _EionCmnUploadUserName_Type()
)
eionCmnUploadUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnUploadUserName.setStatus("current")


class _EionCmnUploadPassword_Type(DisplayString):
    """Custom type eionCmnUploadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EionCmnUploadPassword_Type.__name__ = "DisplayString"
_EionCmnUploadPassword_Object = MibTableColumn
eionCmnUploadPassword = _EionCmnUploadPassword_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1, 5),
    _EionCmnUploadPassword_Type()
)
eionCmnUploadPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnUploadPassword.setStatus("current")


class _EionCmnUploadFilePath_Type(DisplayString):
    """Custom type eionCmnUploadFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EionCmnUploadFilePath_Type.__name__ = "DisplayString"
_EionCmnUploadFilePath_Object = MibTableColumn
eionCmnUploadFilePath = _EionCmnUploadFilePath_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 36, 1, 6),
    _EionCmnUploadFilePath_Type()
)
eionCmnUploadFilePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eionCmnUploadFilePath.setStatus("current")
_EionCmnWatchDogLastChange_Type = TimeTicks
_EionCmnWatchDogLastChange_Object = MibScalar
eionCmnWatchDogLastChange = _EionCmnWatchDogLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 37),
    _EionCmnWatchDogLastChange_Type()
)
eionCmnWatchDogLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnWatchDogLastChange.setStatus("current")
_EionCmnWatchDogNumRows_Type = Unsigned32
_EionCmnWatchDogNumRows_Object = MibScalar
eionCmnWatchDogNumRows = _EionCmnWatchDogNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 38),
    _EionCmnWatchDogNumRows_Type()
)
eionCmnWatchDogNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnWatchDogNumRows.setStatus("current")
_EionCmnWatchDogTable_Object = MibTable
eionCmnWatchDogTable = _EionCmnWatchDogTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 39)
)
if mibBuilder.loadTexts:
    eionCmnWatchDogTable.setStatus("current")
_EionCmnWatchDogEntry_Object = MibTableRow
eionCmnWatchDogEntry = _EionCmnWatchDogEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 39, 1)
)
eionCmnWatchDogEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnWatchDogIndex"),
)
if mibBuilder.loadTexts:
    eionCmnWatchDogEntry.setStatus("current")
_EionCmnWatchDogIndex_Type = Unsigned32
_EionCmnWatchDogIndex_Object = MibTableColumn
eionCmnWatchDogIndex = _EionCmnWatchDogIndex_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 39, 1, 1),
    _EionCmnWatchDogIndex_Type()
)
eionCmnWatchDogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnWatchDogIndex.setStatus("current")
_EionCmnWatchDogStatus_Type = EionStatus
_EionCmnWatchDogStatus_Object = MibTableColumn
eionCmnWatchDogStatus = _EionCmnWatchDogStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 39, 1, 2),
    _EionCmnWatchDogStatus_Type()
)
eionCmnWatchDogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnWatchDogStatus.setStatus("current")
_EionCmnWatchDogExpTime_Type = Unsigned32
_EionCmnWatchDogExpTime_Object = MibTableColumn
eionCmnWatchDogExpTime = _EionCmnWatchDogExpTime_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 39, 1, 3),
    _EionCmnWatchDogExpTime_Type()
)
eionCmnWatchDogExpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnWatchDogExpTime.setStatus("current")
_EionCmnFrmWareRollBckLastChange_Type = TimeTicks
_EionCmnFrmWareRollBckLastChange_Object = MibScalar
eionCmnFrmWareRollBckLastChange = _EionCmnFrmWareRollBckLastChange_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 40),
    _EionCmnFrmWareRollBckLastChange_Type()
)
eionCmnFrmWareRollBckLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnFrmWareRollBckLastChange.setStatus("current")
_EionCmnFrmWareRollBckNumRows_Type = Unsigned32
_EionCmnFrmWareRollBckNumRows_Object = MibScalar
eionCmnFrmWareRollBckNumRows = _EionCmnFrmWareRollBckNumRows_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 41),
    _EionCmnFrmWareRollBckNumRows_Type()
)
eionCmnFrmWareRollBckNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnFrmWareRollBckNumRows.setStatus("current")
_EionCmnFrmWareRollBckTable_Object = MibTable
eionCmnFrmWareRollBckTable = _EionCmnFrmWareRollBckTable_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 42)
)
if mibBuilder.loadTexts:
    eionCmnFrmWareRollBckTable.setStatus("current")
_EionCmnFrmWareRollBckEntry_Object = MibTableRow
eionCmnFrmWareRollBckEntry = _EionCmnFrmWareRollBckEntry_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 42, 1)
)
eionCmnFrmWareRollBckEntry.setIndexNames(
    (0, "EION-SYSTEM-MIB", "eionCmnRollBackStatus"),
)
if mibBuilder.loadTexts:
    eionCmnFrmWareRollBckEntry.setStatus("current")


class _EionCmnRollBackStatus_Type(Integer32):
    """Custom type eionCmnRollBackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_EionCmnRollBackStatus_Type.__name__ = "Integer32"
_EionCmnRollBackStatus_Object = MibTableColumn
eionCmnRollBackStatus = _EionCmnRollBackStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 42, 1, 1),
    _EionCmnRollBackStatus_Type()
)
eionCmnRollBackStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eionCmnRollBackStatus.setStatus("current")


class _EionCmnRollBackFirmWareVer_Type(DisplayString):
    """Custom type eionCmnRollBackFirmWareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EionCmnRollBackFirmWareVer_Type.__name__ = "DisplayString"
_EionCmnRollBackFirmWareVer_Object = MibTableColumn
eionCmnRollBackFirmWareVer = _EionCmnRollBackFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 42, 1, 2),
    _EionCmnRollBackFirmWareVer_Type()
)
eionCmnRollBackFirmWareVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnRollBackFirmWareVer.setStatus("current")


class _EionCmnRollBackAction_Type(Integer32):
    """Custom type eionCmnRollBackAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("set", 1),
          ("commit", 2))
    )


_EionCmnRollBackAction_Type.__name__ = "Integer32"
_EionCmnRollBackAction_Object = MibTableColumn
eionCmnRollBackAction = _EionCmnRollBackAction_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 1, 42, 1, 3),
    _EionCmnRollBackAction_Type()
)
eionCmnRollBackAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnRollBackAction.setStatus("current")
_EionCmnConformance_ObjectIdentity = ObjectIdentity
eionCmnConformance = _EionCmnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2)
)
_EionCmnCompliances_ObjectIdentity = ObjectIdentity
eionCmnCompliances = _EionCmnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 1)
)
_EionCmnGroups_ObjectIdentity = ObjectIdentity
eionCmnGroups = _EionCmnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2)
)
_EionCmnAntennaAlignStatus_Type = EionStatus
_EionCmnAntennaAlignStatus_Object = MibScalar
eionCmnAntennaAlignStatus = _EionCmnAntennaAlignStatus_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 3),
    _EionCmnAntennaAlignStatus_Type()
)
eionCmnAntennaAlignStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnAntennaAlignStatus.setStatus("current")
_EionCmnGatewayIP_Type = IpAddress
_EionCmnGatewayIP_Object = MibScalar
eionCmnGatewayIP = _EionCmnGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 4),
    _EionCmnGatewayIP_Type()
)
eionCmnGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnGatewayIP.setStatus("current")


class _EionCmnHostName_Type(DisplayString):
    """Custom type eionCmnHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EionCmnHostName_Type.__name__ = "DisplayString"
_EionCmnHostName_Object = MibScalar
eionCmnHostName = _EionCmnHostName_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 5),
    _EionCmnHostName_Type()
)
eionCmnHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnHostName.setStatus("current")


class _EionCmnSaveConfig_Type(Integer32):
    """Custom type eionCmnSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("default", 2))
    )


_EionCmnSaveConfig_Type.__name__ = "Integer32"
_EionCmnSaveConfig_Object = MibScalar
eionCmnSaveConfig = _EionCmnSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 6),
    _EionCmnSaveConfig_Type()
)
eionCmnSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnSaveConfig.setStatus("current")


class _EionCmnReboot_Type(Integer32):
    """Custom type eionCmnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("run", 0),
          ("reboot", 1),
          ("rebootsave", 2))
    )


_EionCmnReboot_Type.__name__ = "Integer32"
_EionCmnReboot_Object = MibScalar
eionCmnReboot = _EionCmnReboot_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 7),
    _EionCmnReboot_Type()
)
eionCmnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnReboot.setStatus("current")


class _EionCmnApplyConfig_Type(Unsigned32):
    """Custom type eionCmnApplyConfig based on Unsigned32"""
    defaultValue = 0


_EionCmnApplyConfig_Type.__name__ = "Unsigned32"
_EionCmnApplyConfig_Object = MibScalar
eionCmnApplyConfig = _EionCmnApplyConfig_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 8),
    _EionCmnApplyConfig_Type()
)
eionCmnApplyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eionCmnApplyConfig.setStatus("current")


class _EionCmnSerialNumber_Type(DisplayString):
    """Custom type eionCmnSerialNumber based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_EionCmnSerialNumber_Type.__name__ = "DisplayString"
_EionCmnSerialNumber_Object = MibScalar
eionCmnSerialNumber = _EionCmnSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34226, 1, 9),
    _EionCmnSerialNumber_Type()
)
eionCmnSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eionCmnSerialNumber.setStatus("current")
_EionCmnAgentOIDs_ObjectIdentity = ObjectIdentity
eionCmnAgentOIDs = _EionCmnAgentOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 10)
)
_LibraPlus_ObjectIdentity = ObjectIdentity
libraPlus = _LibraPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 10, 1)
)
_LibraMax_ObjectIdentity = ObjectIdentity
libraMax = _LibraMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 10, 2)
)
_Vip_ObjectIdentity = ObjectIdentity
vip = _Vip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 10, 3)
)
_StarPlus_ObjectIdentity = ObjectIdentity
starPlus = _StarPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 10, 4)
)
_StarMax_ObjectIdentity = ObjectIdentity
starMax = _StarMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34226, 1, 10, 5)
)

# Managed Objects groups

eionCmnMacACLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 1)
)
eionCmnMacACLGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnMacACLLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnMacACLNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnMacACLAddr"),
        ("EION-SYSTEM-MIB", "eionCmnMacACLName"),
        ("EION-SYSTEM-MIB", "eionCmnMacACLRowStatus"))
)
if mibBuilder.loadTexts:
    eionCmnMacACLGroup.setStatus("current")

eionCmnBrdgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 2)
)
eionCmnBrdgGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnBrdgLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgName"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgAssPortName"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgId"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgSTP"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgMTU"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgAging"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgMulticast"))
)
if mibBuilder.loadTexts:
    eionCmnBrdgGroup.setStatus("current")

eionCmnBrdgFDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 3)
)
eionCmnBrdgFDBGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnBrdgFDBLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgFDBNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgFDBName"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgFDBMACId"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgFDBIsLocal"))
)
if mibBuilder.loadTexts:
    eionCmnBrdgFDBGroup.setStatus("current")

eionCmnDataVLANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 4)
)
eionCmnDataVLANGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnDataVlanLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnDataVlanNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnDataVlanId"),
        ("EION-SYSTEM-MIB", "eionCmnDataVlanStatus"))
)
if mibBuilder.loadTexts:
    eionCmnDataVLANGroup.setStatus("current")

eionCmnMacVsNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 5)
)
eionCmnMacVsNameGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnMacVsNameLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnMacVsNameNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnMacVsNameRowStatus"),
        ("EION-SYSTEM-MIB", "eionCmnMacVsNameName"))
)
if mibBuilder.loadTexts:
    eionCmnMacVsNameGroup.setStatus("current")

eionCmnMgmtIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 6)
)
eionCmnMgmtIPGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnMgmtIPLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtIPNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtIP"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtMask"))
)
if mibBuilder.loadTexts:
    eionCmnMgmtIPGroup.setStatus("current")

eionCmnMgmtVLANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 7)
)
eionCmnMgmtVLANGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnMgmtVLANLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtVLANNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtVLANID"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtVLANStatus"))
)
if mibBuilder.loadTexts:
    eionCmnMgmtVLANGroup.setStatus("current")

eionCmnDHCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 8)
)
eionCmnDHCPGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnDHCPLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPInterfaceName"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPServerStatus"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPClientStatus"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPRouterIP"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPSubnetMask"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPStartIP"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPEndIP"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPDNSServerIP"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPDomainName"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPLeaseTime"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPMinLeaseTime"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPMaxNumLease"))
)
if mibBuilder.loadTexts:
    eionCmnDHCPGroup.setStatus("current")

eionCmnSNMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 9)
)
eionCmnSNMPGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnSNMPLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPStatus"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPLocation"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPRoCommunityName"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPRwCommunityName"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPContact"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPManagerIP"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPRSSIThres"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPSendPktErrRateThres"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPRcvPktErrRateThres"))
)
if mibBuilder.loadTexts:
    eionCmnSNMPGroup.setStatus("current")

eionCmnSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 10)
)
eionCmnSyslogGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnSyslogLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnSyslogNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnSyslogStatus"))
)
if mibBuilder.loadTexts:
    eionCmnSyslogGroup.setStatus("current")

eionCmnSysDateTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 11)
)
eionCmnSysDateTimeGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnSysDateLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnSysDateNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnSysDate"),
        ("EION-SYSTEM-MIB", "eionCmnSysTime"))
)
if mibBuilder.loadTexts:
    eionCmnSysDateTimeGroup.setStatus("current")

eionCmnUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 12)
)
eionCmnUploadGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnUploadLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnUploadNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnUploadIP"),
        ("EION-SYSTEM-MIB", "eionCmnUploadRowStatus"),
        ("EION-SYSTEM-MIB", "eionCmnUploadUserName"),
        ("EION-SYSTEM-MIB", "eionCmnUploadPassword"),
        ("EION-SYSTEM-MIB", "eionCmnUploadFilePath"))
)
if mibBuilder.loadTexts:
    eionCmnUploadGroup.setStatus("current")

eionCmnWatchDogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 13)
)
eionCmnWatchDogGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnWatchDogLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnWatchDogNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnWatchDogStatus"),
        ("EION-SYSTEM-MIB", "eionCmnWatchDogExpTime"))
)
if mibBuilder.loadTexts:
    eionCmnWatchDogGroup.setStatus("current")

eionCmnFrmWareRollBckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 14)
)
eionCmnFrmWareRollBckGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnFrmWareRollBckLastChange"),
        ("EION-SYSTEM-MIB", "eionCmnFrmWareRollBckNumRows"),
        ("EION-SYSTEM-MIB", "eionCmnRollBackFirmWareVer"),
        ("EION-SYSTEM-MIB", "eionCmnRollBackAction"))
)
if mibBuilder.loadTexts:
    eionCmnFrmWareRollBckGroup.setStatus("current")

eionCmnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 2, 15)
)
eionCmnGroup.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnAntennaAlignStatus"),
        ("EION-SYSTEM-MIB", "eionCmnGatewayIP"),
        ("EION-SYSTEM-MIB", "eionCmnHostName"),
        ("EION-SYSTEM-MIB", "eionCmnSaveConfig"),
        ("EION-SYSTEM-MIB", "eionCmnReboot"),
        ("EION-SYSTEM-MIB", "eionCmnApplyConfig"),
        ("EION-SYSTEM-MIB", "eionCmnSerialNumber"))
)
if mibBuilder.loadTexts:
    eionCmnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

eionCmnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34226, 1, 2, 1, 1)
)
eionCmnCompliance.setObjects(
      *(("EION-SYSTEM-MIB", "eionCmnMacACLGroup"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgGroup"),
        ("EION-SYSTEM-MIB", "eionCmnBrdgFDBGroup"),
        ("EION-SYSTEM-MIB", "eionCmnDataVLANGroup"),
        ("EION-SYSTEM-MIB", "eionCmnMacVsNameGroup"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtIPGroup"),
        ("EION-SYSTEM-MIB", "eionCmnMgmtVLANGroup"),
        ("EION-SYSTEM-MIB", "eionCmnDHCPGroup"),
        ("EION-SYSTEM-MIB", "eionCmnSNMPGroup"),
        ("EION-SYSTEM-MIB", "eionCmnSyslogGroup"),
        ("EION-SYSTEM-MIB", "eionCmnSysDateTimeGroup"),
        ("EION-SYSTEM-MIB", "eionCmnUploadGroup"),
        ("EION-SYSTEM-MIB", "eionCmnWatchDogGroup"),
        ("EION-SYSTEM-MIB", "eionCmnFrmWareRollBckGroup"),
        ("EION-SYSTEM-MIB", "eionCmnGroup"))
)
if mibBuilder.loadTexts:
    eionCmnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EION-SYSTEM-MIB",
    **{"EionStatus": EionStatus,
       "eionMIB": eionMIB,
       "eionCmn": eionCmn,
       "eionCmnNotifications": eionCmnNotifications,
       "eionCmnObjects": eionCmnObjects,
       "eionCmnMacACLLastChange": eionCmnMacACLLastChange,
       "eionCmnMacACLNumRows": eionCmnMacACLNumRows,
       "eionCmnMacACLTable": eionCmnMacACLTable,
       "eionCmnMacACLEntry": eionCmnMacACLEntry,
       "eionCmnMacACLIndex": eionCmnMacACLIndex,
       "eionCmnMacACLAddr": eionCmnMacACLAddr,
       "eionCmnMacACLName": eionCmnMacACLName,
       "eionCmnMacACLRowStatus": eionCmnMacACLRowStatus,
       "eionCmnBrdgLastChange": eionCmnBrdgLastChange,
       "eionCmnBrdgNumRows": eionCmnBrdgNumRows,
       "eionCmnBrdgTable": eionCmnBrdgTable,
       "eionCmnBrdgEntry": eionCmnBrdgEntry,
       "eionCmnBrdgIndex": eionCmnBrdgIndex,
       "eionCmnBrdgName": eionCmnBrdgName,
       "eionCmnBrdgAssPortName": eionCmnBrdgAssPortName,
       "eionCmnBrdgId": eionCmnBrdgId,
       "eionCmnBrdgSTP": eionCmnBrdgSTP,
       "eionCmnBrdgMTU": eionCmnBrdgMTU,
       "eionCmnBrdgAging": eionCmnBrdgAging,
       "eionCmnBrdgMulticast": eionCmnBrdgMulticast,
       "eionCmnBrdgFDBLastChange": eionCmnBrdgFDBLastChange,
       "eionCmnBrdgFDBNumRows": eionCmnBrdgFDBNumRows,
       "eionCmnBrdgFDBTable": eionCmnBrdgFDBTable,
       "eionCmnBrdgFDBEntry": eionCmnBrdgFDBEntry,
       "eionCmnBrdgFDBIndex": eionCmnBrdgFDBIndex,
       "eionCmnBrdgFDBName": eionCmnBrdgFDBName,
       "eionCmnBrdgFDBMACId": eionCmnBrdgFDBMACId,
       "eionCmnBrdgFDBIsLocal": eionCmnBrdgFDBIsLocal,
       "eionCmnDataVlanLastChange": eionCmnDataVlanLastChange,
       "eionCmnDataVlanNumRows": eionCmnDataVlanNumRows,
       "eionCmnDataVlanTable": eionCmnDataVlanTable,
       "eionCmnDataVlanEntry": eionCmnDataVlanEntry,
       "eionCmnDataVlanIndex": eionCmnDataVlanIndex,
       "eionCmnDataVlanId": eionCmnDataVlanId,
       "eionCmnDataVlanStatus": eionCmnDataVlanStatus,
       "eionCmnMacVsNameLastChange": eionCmnMacVsNameLastChange,
       "eionCmnMacVsNameNumRows": eionCmnMacVsNameNumRows,
       "eionCmnMacVsNameTable": eionCmnMacVsNameTable,
       "eionCmnMacVsNameEntry": eionCmnMacVsNameEntry,
       "eionCmnMacVsNameMacAddr": eionCmnMacVsNameMacAddr,
       "eionCmnMacVsNameName": eionCmnMacVsNameName,
       "eionCmnMacVsNameRowStatus": eionCmnMacVsNameRowStatus,
       "eionCmnMgmtIPLastChange": eionCmnMgmtIPLastChange,
       "eionCmnMgmtIPNumRows": eionCmnMgmtIPNumRows,
       "eionCmnMgmtIPTable": eionCmnMgmtIPTable,
       "eionCmnMgmtIPEntry": eionCmnMgmtIPEntry,
       "eionCmnMgmtIP": eionCmnMgmtIP,
       "eionCmnMgmtMask": eionCmnMgmtMask,
       "eionCmnMgmtVLANLastChange": eionCmnMgmtVLANLastChange,
       "eionCmnMgmtVLANNumRows": eionCmnMgmtVLANNumRows,
       "eionCmnMgmtVLANTable": eionCmnMgmtVLANTable,
       "eionCmnMgmtVLANEntry": eionCmnMgmtVLANEntry,
       "eionCmnMgmtVLANIndex": eionCmnMgmtVLANIndex,
       "eionCmnMgmtVLANID": eionCmnMgmtVLANID,
       "eionCmnMgmtVLANStatus": eionCmnMgmtVLANStatus,
       "eionCmnDHCPLastChange": eionCmnDHCPLastChange,
       "eionCmnDHCPNumRows": eionCmnDHCPNumRows,
       "eionCmnDHCPTable": eionCmnDHCPTable,
       "eionCmnDHCPEntry": eionCmnDHCPEntry,
       "eionCmnDHCPIndex": eionCmnDHCPIndex,
       "eionCmnDHCPInterfaceName": eionCmnDHCPInterfaceName,
       "eionCmnDHCPServerStatus": eionCmnDHCPServerStatus,
       "eionCmnDHCPClientStatus": eionCmnDHCPClientStatus,
       "eionCmnDHCPRouterIP": eionCmnDHCPRouterIP,
       "eionCmnDHCPSubnetMask": eionCmnDHCPSubnetMask,
       "eionCmnDHCPStartIP": eionCmnDHCPStartIP,
       "eionCmnDHCPEndIP": eionCmnDHCPEndIP,
       "eionCmnDHCPDNSServerIP": eionCmnDHCPDNSServerIP,
       "eionCmnDHCPDomainName": eionCmnDHCPDomainName,
       "eionCmnDHCPLeaseTime": eionCmnDHCPLeaseTime,
       "eionCmnDHCPMinLeaseTime": eionCmnDHCPMinLeaseTime,
       "eionCmnDHCPMaxNumLease": eionCmnDHCPMaxNumLease,
       "eionCmnSNMPLastChange": eionCmnSNMPLastChange,
       "eionCmnSNMPNumRows": eionCmnSNMPNumRows,
       "eionCmnSNMPTable": eionCmnSNMPTable,
       "eionCmnSNMPEntry": eionCmnSNMPEntry,
       "eionCmnSNMPIndex": eionCmnSNMPIndex,
       "eionCmnSNMPStatus": eionCmnSNMPStatus,
       "eionCmnSNMPLocation": eionCmnSNMPLocation,
       "eionCmnSNMPRoCommunityName": eionCmnSNMPRoCommunityName,
       "eionCmnSNMPRwCommunityName": eionCmnSNMPRwCommunityName,
       "eionCmnSNMPContact": eionCmnSNMPContact,
       "eionCmnSNMPManagerIP": eionCmnSNMPManagerIP,
       "eionCmnSNMPRSSIThres": eionCmnSNMPRSSIThres,
       "eionCmnSNMPSendPktErrRateThres": eionCmnSNMPSendPktErrRateThres,
       "eionCmnSNMPRcvPktErrRateThres": eionCmnSNMPRcvPktErrRateThres,
       "eionCmnSyslogLastChange": eionCmnSyslogLastChange,
       "eionCmnSyslogNumRows": eionCmnSyslogNumRows,
       "eionCmnSyslogTable": eionCmnSyslogTable,
       "eionCmnSyslogEntry": eionCmnSyslogEntry,
       "eionCmnSyslogIndex": eionCmnSyslogIndex,
       "eionCmnSyslogStatus": eionCmnSyslogStatus,
       "eionCmnSysDateLastChange": eionCmnSysDateLastChange,
       "eionCmnSysDateNumRows": eionCmnSysDateNumRows,
       "eionCmnSysDateTimeTable": eionCmnSysDateTimeTable,
       "eionCmnSysDateTimeEntry": eionCmnSysDateTimeEntry,
       "eionCmnSysDateTimeIndex": eionCmnSysDateTimeIndex,
       "eionCmnSysDate": eionCmnSysDate,
       "eionCmnSysTime": eionCmnSysTime,
       "eionCmnUploadLastChange": eionCmnUploadLastChange,
       "eionCmnUploadNumRows": eionCmnUploadNumRows,
       "eionCmnUploadTable": eionCmnUploadTable,
       "eionCmnUploadEntry": eionCmnUploadEntry,
       "eionCmnUploadIndex": eionCmnUploadIndex,
       "eionCmnUploadIP": eionCmnUploadIP,
       "eionCmnUploadRowStatus": eionCmnUploadRowStatus,
       "eionCmnUploadUserName": eionCmnUploadUserName,
       "eionCmnUploadPassword": eionCmnUploadPassword,
       "eionCmnUploadFilePath": eionCmnUploadFilePath,
       "eionCmnWatchDogLastChange": eionCmnWatchDogLastChange,
       "eionCmnWatchDogNumRows": eionCmnWatchDogNumRows,
       "eionCmnWatchDogTable": eionCmnWatchDogTable,
       "eionCmnWatchDogEntry": eionCmnWatchDogEntry,
       "eionCmnWatchDogIndex": eionCmnWatchDogIndex,
       "eionCmnWatchDogStatus": eionCmnWatchDogStatus,
       "eionCmnWatchDogExpTime": eionCmnWatchDogExpTime,
       "eionCmnFrmWareRollBckLastChange": eionCmnFrmWareRollBckLastChange,
       "eionCmnFrmWareRollBckNumRows": eionCmnFrmWareRollBckNumRows,
       "eionCmnFrmWareRollBckTable": eionCmnFrmWareRollBckTable,
       "eionCmnFrmWareRollBckEntry": eionCmnFrmWareRollBckEntry,
       "eionCmnRollBackStatus": eionCmnRollBackStatus,
       "eionCmnRollBackFirmWareVer": eionCmnRollBackFirmWareVer,
       "eionCmnRollBackAction": eionCmnRollBackAction,
       "eionCmnConformance": eionCmnConformance,
       "eionCmnCompliances": eionCmnCompliances,
       "eionCmnCompliance": eionCmnCompliance,
       "eionCmnGroups": eionCmnGroups,
       "eionCmnMacACLGroup": eionCmnMacACLGroup,
       "eionCmnBrdgGroup": eionCmnBrdgGroup,
       "eionCmnBrdgFDBGroup": eionCmnBrdgFDBGroup,
       "eionCmnDataVLANGroup": eionCmnDataVLANGroup,
       "eionCmnMacVsNameGroup": eionCmnMacVsNameGroup,
       "eionCmnMgmtIPGroup": eionCmnMgmtIPGroup,
       "eionCmnMgmtVLANGroup": eionCmnMgmtVLANGroup,
       "eionCmnDHCPGroup": eionCmnDHCPGroup,
       "eionCmnSNMPGroup": eionCmnSNMPGroup,
       "eionCmnSyslogGroup": eionCmnSyslogGroup,
       "eionCmnSysDateTimeGroup": eionCmnSysDateTimeGroup,
       "eionCmnUploadGroup": eionCmnUploadGroup,
       "eionCmnWatchDogGroup": eionCmnWatchDogGroup,
       "eionCmnFrmWareRollBckGroup": eionCmnFrmWareRollBckGroup,
       "eionCmnGroup": eionCmnGroup,
       "eionCmnAntennaAlignStatus": eionCmnAntennaAlignStatus,
       "eionCmnGatewayIP": eionCmnGatewayIP,
       "eionCmnHostName": eionCmnHostName,
       "eionCmnSaveConfig": eionCmnSaveConfig,
       "eionCmnReboot": eionCmnReboot,
       "eionCmnApplyConfig": eionCmnApplyConfig,
       "eionCmnSerialNumber": eionCmnSerialNumber,
       "eionCmnAgentOIDs": eionCmnAgentOIDs,
       "libraPlus": libraPlus,
       "libraMax": libraMax,
       "vip": vip,
       "starPlus": starPlus,
       "starMax": starMax}
)
