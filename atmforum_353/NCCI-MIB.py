# SNMP MIB module (NCCI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/NCCI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:06:53 2025
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

(atmVclEntry,
 atmVplEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclEntry",
    "atmVplEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

atmfNcciMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1)
)
if mibBuilder.loadTexts:
    atmfNcciMIB.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmNcciType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("aesaBased", 1),
          ("bisup", 2))
    )



class AtmNcci(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(9, 9),
        ValueSizeConstraint(28, 28),
    )



class AtmNcciRoot(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfSignalling_ObjectIdentity = ObjectIdentity
atmfSignalling = _AtmfSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9)
)
_AtmfNcci_ObjectIdentity = ObjectIdentity
atmfNcci = _AtmfNcci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1)
)
_NcciMIBObjects_ObjectIdentity = ObjectIdentity
ncciMIBObjects = _NcciMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1)
)
_NcciIfTable_Object = MibTable
ncciIfTable = _NcciIfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ncciIfTable.setStatus("current")
_NcciIfEntry_Object = MibTableRow
ncciIfEntry = _NcciIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1)
)
ncciIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NCCI-MIB", "ncciIfDirection"),
)
if mibBuilder.loadTexts:
    ncciIfEntry.setStatus("current")


class _NcciIfDirection_Type(Integer32):
    """Custom type ncciIfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_NcciIfDirection_Type.__name__ = "Integer32"
_NcciIfDirection_Object = MibTableColumn
ncciIfDirection = _NcciIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 1),
    _NcciIfDirection_Type()
)
ncciIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ncciIfDirection.setStatus("current")


class _NcciIfAction_Type(Integer32):
    """Custom type ncciIfAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discardNcci", 1),
          ("assignNcci", 2),
          ("forwardNcci", 3))
    )


_NcciIfAction_Type.__name__ = "Integer32"
_NcciIfAction_Object = MibTableColumn
ncciIfAction = _NcciIfAction_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 2),
    _NcciIfAction_Type()
)
ncciIfAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfAction.setStatus("current")


class _NcciIfSave_Type(Bits):
    """Custom type ncciIfSave based on Bits"""
    namedValues = NamedValues(
        *(("localNcci", 0),
          ("remoteNcci", 1))
    )

_NcciIfSave_Type.__name__ = "Bits"
_NcciIfSave_Object = MibTableColumn
ncciIfSave = _NcciIfSave_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 3),
    _NcciIfSave_Type()
)
ncciIfSave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfSave.setStatus("current")


class _NcciIfinConnect_Type(TruthValue):
    """Custom type ncciIfinConnect based on TruthValue"""
    defaultValue = 1


_NcciIfinConnect_Type.__name__ = "TruthValue"
_NcciIfinConnect_Object = MibTableColumn
ncciIfinConnect = _NcciIfinConnect_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 4),
    _NcciIfinConnect_Type()
)
ncciIfinConnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfinConnect.setStatus("current")


class _NcciIfType_Type(AtmNcciType):
    """Custom type ncciIfType based on AtmNcciType"""
    defaultValue = 0


_NcciIfType_Type.__name__ = "AtmNcciType"
_NcciIfType_Object = MibTableColumn
ncciIfType = _NcciIfType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 5),
    _NcciIfType_Type()
)
ncciIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfType.setStatus("current")
_NcciIfRoot_Type = AtmNcciRoot
_NcciIfRoot_Object = MibTableColumn
ncciIfRoot = _NcciIfRoot_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 6),
    _NcciIfRoot_Type()
)
ncciIfRoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfRoot.setStatus("current")


class _NcciIfCastType_Type(Integer32):
    """Custom type ncciIfCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 1),
          ("p2mp", 2),
          ("p2pANDp2mp", 3))
    )


_NcciIfCastType_Type.__name__ = "Integer32"
_NcciIfCastType_Object = MibTableColumn
ncciIfCastType = _NcciIfCastType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 7),
    _NcciIfCastType_Type()
)
ncciIfCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfCastType.setStatus("current")


class _NcciIfVpType_Type(Integer32):
    """Custom type ncciIfVpType based on Integer32"""
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
        *(("none", 1),
          ("svp", 2),
          ("spvpInitiator", 3),
          ("svpANDspvpInitiator", 4))
    )


_NcciIfVpType_Type.__name__ = "Integer32"
_NcciIfVpType_Object = MibTableColumn
ncciIfVpType = _NcciIfVpType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 8),
    _NcciIfVpType_Type()
)
ncciIfVpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfVpType.setStatus("current")


class _NcciIfVcType_Type(Integer32):
    """Custom type ncciIfVcType based on Integer32"""
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
        *(("none", 1),
          ("svc", 2),
          ("spvcInitiator", 3),
          ("svcANDspvcInitiator", 4))
    )


_NcciIfVcType_Type.__name__ = "Integer32"
_NcciIfVcType_Object = MibTableColumn
ncciIfVcType = _NcciIfVcType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 9),
    _NcciIfVcType_Type()
)
ncciIfVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfVcType.setStatus("current")
_NcciIfRowStatus_Type = RowStatus
_NcciIfRowStatus_Object = MibTableColumn
ncciIfRowStatus = _NcciIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 1, 1, 10),
    _NcciIfRowStatus_Type()
)
ncciIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ncciIfRowStatus.setStatus("current")
_NcciVpTable_Object = MibTable
ncciVpTable = _NcciVpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ncciVpTable.setStatus("current")
_NcciVpEntry_Object = MibTableRow
ncciVpEntry = _NcciVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ncciVpEntry.setStatus("current")
_NcciVpLocalType_Type = AtmNcciType
_NcciVpLocalType_Object = MibTableColumn
ncciVpLocalType = _NcciVpLocalType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 2, 1, 1),
    _NcciVpLocalType_Type()
)
ncciVpLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVpLocalType.setStatus("current")
_NcciVpLocalValue_Type = AtmNcci
_NcciVpLocalValue_Object = MibTableColumn
ncciVpLocalValue = _NcciVpLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 2, 1, 2),
    _NcciVpLocalValue_Type()
)
ncciVpLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVpLocalValue.setStatus("current")
_NcciVpRemoteType_Type = AtmNcciType
_NcciVpRemoteType_Object = MibTableColumn
ncciVpRemoteType = _NcciVpRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 2, 1, 3),
    _NcciVpRemoteType_Type()
)
ncciVpRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVpRemoteType.setStatus("current")
_NcciVpRemoteValue_Type = AtmNcci
_NcciVpRemoteValue_Object = MibTableColumn
ncciVpRemoteValue = _NcciVpRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 2, 1, 4),
    _NcciVpRemoteValue_Type()
)
ncciVpRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVpRemoteValue.setStatus("current")
_NcciVcTable_Object = MibTable
ncciVcTable = _NcciVcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ncciVcTable.setStatus("current")
_NcciVcEntry_Object = MibTableRow
ncciVcEntry = _NcciVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ncciVcEntry.setStatus("current")
_NcciVcLocalType_Type = AtmNcciType
_NcciVcLocalType_Object = MibTableColumn
ncciVcLocalType = _NcciVcLocalType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 3, 1, 1),
    _NcciVcLocalType_Type()
)
ncciVcLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVcLocalType.setStatus("current")
_NcciVcLocalValue_Type = AtmNcci
_NcciVcLocalValue_Object = MibTableColumn
ncciVcLocalValue = _NcciVcLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 3, 1, 2),
    _NcciVcLocalValue_Type()
)
ncciVcLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVcLocalValue.setStatus("current")
_NcciVcRemoteType_Type = AtmNcciType
_NcciVcRemoteType_Object = MibTableColumn
ncciVcRemoteType = _NcciVcRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 3, 1, 3),
    _NcciVcRemoteType_Type()
)
ncciVcRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVcRemoteType.setStatus("current")
_NcciVcRemoteValue_Type = AtmNcci
_NcciVcRemoteValue_Object = MibTableColumn
ncciVcRemoteValue = _NcciVcRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 1, 3, 1, 4),
    _NcciVcRemoteValue_Type()
)
ncciVcRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncciVcRemoteValue.setStatus("current")
_NcciMIBConformance_ObjectIdentity = ObjectIdentity
ncciMIBConformance = _NcciMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2)
)
_NcciMIBCompliances_ObjectIdentity = ObjectIdentity
ncciMIBCompliances = _NcciMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 1)
)
_NcciMIBGroups_ObjectIdentity = ObjectIdentity
ncciMIBGroups = _NcciMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 2)
)
atmVplEntry.registerAugmentions(
    ("NCCI-MIB",
     "ncciVpEntry")
)
ncciVpEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("NCCI-MIB",
     "ncciVcEntry")
)
ncciVcEntry.setIndexNames(*atmVclEntry.getIndexNames())

# Managed Objects groups

ncciIfMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 2, 1)
)
ncciIfMinGroup.setObjects(
      *(("NCCI-MIB", "ncciIfAction"),
        ("NCCI-MIB", "ncciIfSave"),
        ("NCCI-MIB", "ncciIfinConnect"),
        ("NCCI-MIB", "ncciIfType"),
        ("NCCI-MIB", "ncciIfRoot"),
        ("NCCI-MIB", "ncciIfCastType"),
        ("NCCI-MIB", "ncciIfVcType"),
        ("NCCI-MIB", "ncciIfRowStatus"))
)
if mibBuilder.loadTexts:
    ncciIfMinGroup.setStatus("current")

ncciVcMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 2, 2)
)
ncciVcMinGroup.setObjects(
      *(("NCCI-MIB", "ncciVcLocalType"),
        ("NCCI-MIB", "ncciVcLocalValue"),
        ("NCCI-MIB", "ncciVcRemoteType"),
        ("NCCI-MIB", "ncciVcRemoteValue"))
)
if mibBuilder.loadTexts:
    ncciVcMinGroup.setStatus("current")

ncciIfVpOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 2, 3)
)
ncciIfVpOptionalGroup.setObjects(
    ("NCCI-MIB", "ncciIfVpType")
)
if mibBuilder.loadTexts:
    ncciIfVpOptionalGroup.setStatus("current")

ncciVpOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 2, 4)
)
ncciVpOptionalGroup.setObjects(
      *(("NCCI-MIB", "ncciVpLocalType"),
        ("NCCI-MIB", "ncciVpLocalValue"),
        ("NCCI-MIB", "ncciVpRemoteType"),
        ("NCCI-MIB", "ncciVpRemoteValue"))
)
if mibBuilder.loadTexts:
    ncciVpOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ncciMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 9, 1, 1, 2, 1, 1)
)
ncciMIBCompliance.setObjects(
      *(("NCCI-MIB", "ncciIfMinGroup"),
        ("NCCI-MIB", "ncciVcMinGroup"))
)
if mibBuilder.loadTexts:
    ncciMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NCCI-MIB",
    **{"AtmNcciType": AtmNcciType,
       "AtmNcci": AtmNcci,
       "AtmNcciRoot": AtmNcciRoot,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfSignalling": atmfSignalling,
       "atmfNcci": atmfNcci,
       "atmfNcciMIB": atmfNcciMIB,
       "ncciMIBObjects": ncciMIBObjects,
       "ncciIfTable": ncciIfTable,
       "ncciIfEntry": ncciIfEntry,
       "ncciIfDirection": ncciIfDirection,
       "ncciIfAction": ncciIfAction,
       "ncciIfSave": ncciIfSave,
       "ncciIfinConnect": ncciIfinConnect,
       "ncciIfType": ncciIfType,
       "ncciIfRoot": ncciIfRoot,
       "ncciIfCastType": ncciIfCastType,
       "ncciIfVpType": ncciIfVpType,
       "ncciIfVcType": ncciIfVcType,
       "ncciIfRowStatus": ncciIfRowStatus,
       "ncciVpTable": ncciVpTable,
       "ncciVpEntry": ncciVpEntry,
       "ncciVpLocalType": ncciVpLocalType,
       "ncciVpLocalValue": ncciVpLocalValue,
       "ncciVpRemoteType": ncciVpRemoteType,
       "ncciVpRemoteValue": ncciVpRemoteValue,
       "ncciVcTable": ncciVcTable,
       "ncciVcEntry": ncciVcEntry,
       "ncciVcLocalType": ncciVcLocalType,
       "ncciVcLocalValue": ncciVcLocalValue,
       "ncciVcRemoteType": ncciVcRemoteType,
       "ncciVcRemoteValue": ncciVcRemoteValue,
       "ncciMIBConformance": ncciMIBConformance,
       "ncciMIBCompliances": ncciMIBCompliances,
       "ncciMIBCompliance": ncciMIBCompliance,
       "ncciMIBGroups": ncciMIBGroups,
       "ncciIfMinGroup": ncciIfMinGroup,
       "ncciVcMinGroup": ncciVcMinGroup,
       "ncciIfVpOptionalGroup": ncciIfVpOptionalGroup,
       "ncciVpOptionalGroup": ncciVpOptionalGroup}
)
