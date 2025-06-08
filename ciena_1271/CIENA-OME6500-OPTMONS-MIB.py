# SNMP MIB module (CIENA-OME6500-OPTMONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-OME6500-OPTMONS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:47 2025
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

(cienaGenericMIBs,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaGenericMIBs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaOme6500OptmonsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7)
)
if mibBuilder.loadTexts:
    cienaOme6500OptmonsMIB.setRevisions(
        ("2017-12-13 00:00",
         "2018-04-23 00:00",
         "2018-06-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaOme6500OptmonsTable_Object = MibTable
cienaOme6500OptmonsTable = _CienaOme6500OptmonsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1)
)
if mibBuilder.loadTexts:
    cienaOme6500OptmonsTable.setStatus("current")
_CienaOme6500OptmonsEntry_Object = MibTableRow
cienaOme6500OptmonsEntry = _CienaOme6500OptmonsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1)
)
cienaOme6500OptmonsEntry.setIndexNames(
    (0, "CIENA-OME6500-OPTMONS-MIB", "cienaOme6500OptmonsIfIndex"),
)
if mibBuilder.loadTexts:
    cienaOme6500OptmonsEntry.setStatus("current")
_CienaOme6500OptmonsIfIndex_Type = InterfaceIndex
_CienaOme6500OptmonsIfIndex_Object = MibTableColumn
cienaOme6500OptmonsIfIndex = _CienaOme6500OptmonsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 1),
    _CienaOme6500OptmonsIfIndex_Type()
)
cienaOme6500OptmonsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsIfIndex.setStatus("current")
_CienaOme6500OptmonsIfDescr_Type = DisplayString
_CienaOme6500OptmonsIfDescr_Object = MibTableColumn
cienaOme6500OptmonsIfDescr = _CienaOme6500OptmonsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 2),
    _CienaOme6500OptmonsIfDescr_Type()
)
cienaOme6500OptmonsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsIfDescr.setStatus("current")
_CienaOme6500OptmonsSst_Type = DisplayString
_CienaOme6500OptmonsSst_Object = MibTableColumn
cienaOme6500OptmonsSst = _CienaOme6500OptmonsSst_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 3),
    _CienaOme6500OptmonsSst_Type()
)
cienaOme6500OptmonsSst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsSst.setStatus("current")


class _CienaOme6500OptmonsPst_Type(Integer32):
    """Custom type cienaOme6500OptmonsPst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("is", 0),
          ("oosMa", 1),
          ("isAnr", 2),
          ("oosAu", 3),
          ("oosAuma", 4),
          ("oosMaanr", 5))
    )


_CienaOme6500OptmonsPst_Type.__name__ = "Integer32"
_CienaOme6500OptmonsPst_Object = MibTableColumn
cienaOme6500OptmonsPst = _CienaOme6500OptmonsPst_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 4),
    _CienaOme6500OptmonsPst_Type()
)
cienaOme6500OptmonsPst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsPst.setStatus("current")
_CienaOme6500OptmonsAinsTimeLeft_Type = DisplayString
_CienaOme6500OptmonsAinsTimeLeft_Object = MibTableColumn
cienaOme6500OptmonsAinsTimeLeft = _CienaOme6500OptmonsAinsTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 5),
    _CienaOme6500OptmonsAinsTimeLeft_Type()
)
cienaOme6500OptmonsAinsTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsAinsTimeLeft.setStatus("current")
_CienaOme6500OptmonsLosThres_Type = DisplayString
_CienaOme6500OptmonsLosThres_Object = MibTableColumn
cienaOme6500OptmonsLosThres = _CienaOme6500OptmonsLosThres_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 6),
    _CienaOme6500OptmonsLosThres_Type()
)
cienaOme6500OptmonsLosThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsLosThres.setStatus("current")
_CienaOme6500OptmonsPortLabel_Type = DisplayString
_CienaOme6500OptmonsPortLabel_Object = MibTableColumn
cienaOme6500OptmonsPortLabel = _CienaOme6500OptmonsPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 7),
    _CienaOme6500OptmonsPortLabel_Type()
)
cienaOme6500OptmonsPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsPortLabel.setStatus("current")
_CienaOme6500OptmonsAlsoDisabled_Type = DisplayString
_CienaOme6500OptmonsAlsoDisabled_Object = MibTableColumn
cienaOme6500OptmonsAlsoDisabled = _CienaOme6500OptmonsAlsoDisabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 8),
    _CienaOme6500OptmonsAlsoDisabled_Type()
)
cienaOme6500OptmonsAlsoDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsAlsoDisabled.setStatus("current")
_CienaOme6500OptmonsProtNswSwStatus_Type = DisplayString
_CienaOme6500OptmonsProtNswSwStatus_Object = MibTableColumn
cienaOme6500OptmonsProtNswSwStatus = _CienaOme6500OptmonsProtNswSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 9),
    _CienaOme6500OptmonsProtNswSwStatus_Type()
)
cienaOme6500OptmonsProtNswSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtNswSwStatus.setStatus("current")
_CienaOme6500OptmonsProtNswSwEnd_Type = DisplayString
_CienaOme6500OptmonsProtNswSwEnd_Object = MibTableColumn
cienaOme6500OptmonsProtNswSwEnd = _CienaOme6500OptmonsProtNswSwEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 10),
    _CienaOme6500OptmonsProtNswSwEnd_Type()
)
cienaOme6500OptmonsProtNswSwEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtNswSwEnd.setStatus("current")
_CienaOme6500OptmonsProtNswSwReason_Type = DisplayString
_CienaOme6500OptmonsProtNswSwReason_Object = MibTableColumn
cienaOme6500OptmonsProtNswSwReason = _CienaOme6500OptmonsProtNswSwReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 1, 1, 11),
    _CienaOme6500OptmonsProtNswSwReason_Type()
)
cienaOme6500OptmonsProtNswSwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtNswSwReason.setStatus("current")
_CienaOme6500OptmonsProtGroupTable_Object = MibTable
cienaOme6500OptmonsProtGroupTable = _CienaOme6500OptmonsProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2)
)
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupTable.setStatus("current")
_CienaOme6500OptmonsProtGroupEntry_Object = MibTableRow
cienaOme6500OptmonsProtGroupEntry = _CienaOme6500OptmonsProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1)
)
cienaOme6500OptmonsProtGroupEntry.setIndexNames(
    (0, "CIENA-OME6500-OPTMONS-MIB", "cienaOme6500OptmonsProtGroupWrkgIfIndex"),
    (0, "CIENA-OME6500-OPTMONS-MIB", "cienaOme6500OptmonsProtGroupProtIfIndex"),
)
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupEntry.setStatus("current")
_CienaOme6500OptmonsProtGroupWrkgIfIndex_Type = InterfaceIndex
_CienaOme6500OptmonsProtGroupWrkgIfIndex_Object = MibTableColumn
cienaOme6500OptmonsProtGroupWrkgIfIndex = _CienaOme6500OptmonsProtGroupWrkgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 1),
    _CienaOme6500OptmonsProtGroupWrkgIfIndex_Type()
)
cienaOme6500OptmonsProtGroupWrkgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupWrkgIfIndex.setStatus("current")
_CienaOme6500OptmonsProtGroupWrkgIfDescr_Type = DisplayString
_CienaOme6500OptmonsProtGroupWrkgIfDescr_Object = MibTableColumn
cienaOme6500OptmonsProtGroupWrkgIfDescr = _CienaOme6500OptmonsProtGroupWrkgIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 2),
    _CienaOme6500OptmonsProtGroupWrkgIfDescr_Type()
)
cienaOme6500OptmonsProtGroupWrkgIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupWrkgIfDescr.setStatus("current")
_CienaOme6500OptmonsProtGroupWrkgSst_Type = DisplayString
_CienaOme6500OptmonsProtGroupWrkgSst_Object = MibTableColumn
cienaOme6500OptmonsProtGroupWrkgSst = _CienaOme6500OptmonsProtGroupWrkgSst_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 3),
    _CienaOme6500OptmonsProtGroupWrkgSst_Type()
)
cienaOme6500OptmonsProtGroupWrkgSst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupWrkgSst.setStatus("current")
_CienaOme6500OptmonsProtGroupProtIfIndex_Type = InterfaceIndex
_CienaOme6500OptmonsProtGroupProtIfIndex_Object = MibTableColumn
cienaOme6500OptmonsProtGroupProtIfIndex = _CienaOme6500OptmonsProtGroupProtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 4),
    _CienaOme6500OptmonsProtGroupProtIfIndex_Type()
)
cienaOme6500OptmonsProtGroupProtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupProtIfIndex.setStatus("current")
_CienaOme6500OptmonsProtGroupProtIfDescr_Type = DisplayString
_CienaOme6500OptmonsProtGroupProtIfDescr_Object = MibTableColumn
cienaOme6500OptmonsProtGroupProtIfDescr = _CienaOme6500OptmonsProtGroupProtIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 5),
    _CienaOme6500OptmonsProtGroupProtIfDescr_Type()
)
cienaOme6500OptmonsProtGroupProtIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupProtIfDescr.setStatus("current")
_CienaOme6500OptmonsProtGroupProtSst_Type = DisplayString
_CienaOme6500OptmonsProtGroupProtSst_Object = MibTableColumn
cienaOme6500OptmonsProtGroupProtSst = _CienaOme6500OptmonsProtGroupProtSst_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 6),
    _CienaOme6500OptmonsProtGroupProtSst_Type()
)
cienaOme6500OptmonsProtGroupProtSst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupProtSst.setStatus("current")
_CienaOme6500OptmonsProtGroupProtScheme_Type = DisplayString
_CienaOme6500OptmonsProtGroupProtScheme_Object = MibTableColumn
cienaOme6500OptmonsProtGroupProtScheme = _CienaOme6500OptmonsProtGroupProtScheme_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 7),
    _CienaOme6500OptmonsProtGroupProtScheme_Type()
)
cienaOme6500OptmonsProtGroupProtScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupProtScheme.setStatus("current")
_CienaOme6500OptmonsProtGroupWaitToRestore_Type = DisplayString
_CienaOme6500OptmonsProtGroupWaitToRestore_Object = MibTableColumn
cienaOme6500OptmonsProtGroupWaitToRestore = _CienaOme6500OptmonsProtGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 8),
    _CienaOme6500OptmonsProtGroupWaitToRestore_Type()
)
cienaOme6500OptmonsProtGroupWaitToRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupWaitToRestore.setStatus("current")
_CienaOme6500OptmonsProtGroupDetectGuardTime_Type = DisplayString
_CienaOme6500OptmonsProtGroupDetectGuardTime_Object = MibTableColumn
cienaOme6500OptmonsProtGroupDetectGuardTime = _CienaOme6500OptmonsProtGroupDetectGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 9),
    _CienaOme6500OptmonsProtGroupDetectGuardTime_Type()
)
cienaOme6500OptmonsProtGroupDetectGuardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupDetectGuardTime.setStatus("current")
_CienaOme6500OptmonsProtGroupRevertive_Type = DisplayString
_CienaOme6500OptmonsProtGroupRevertive_Object = MibTableColumn
cienaOme6500OptmonsProtGroupRevertive = _CienaOme6500OptmonsProtGroupRevertive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 10),
    _CienaOme6500OptmonsProtGroupRevertive_Type()
)
cienaOme6500OptmonsProtGroupRevertive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupRevertive.setStatus("current")
_CienaOme6500OptmonsProtGroupRemStandard_Type = DisplayString
_CienaOme6500OptmonsProtGroupRemStandard_Object = MibTableColumn
cienaOme6500OptmonsProtGroupRemStandard = _CienaOme6500OptmonsProtGroupRemStandard_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 11),
    _CienaOme6500OptmonsProtGroupRemStandard_Type()
)
cienaOme6500OptmonsProtGroupRemStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupRemStandard.setStatus("current")


class _CienaOme6500OptmonsProtGroupLossPwr_Type(Integer32):
    """Custom type cienaOme6500OptmonsProtGroupLossPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("n", 0),
          ("y", 1))
    )


_CienaOme6500OptmonsProtGroupLossPwr_Type.__name__ = "Integer32"
_CienaOme6500OptmonsProtGroupLossPwr_Object = MibTableColumn
cienaOme6500OptmonsProtGroupLossPwr = _CienaOme6500OptmonsProtGroupLossPwr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 12),
    _CienaOme6500OptmonsProtGroupLossPwr_Type()
)
cienaOme6500OptmonsProtGroupLossPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupLossPwr.setStatus("current")


class _CienaOme6500OptmonsProtGroupTtops_Type(Integer32):
    """Custom type cienaOme6500OptmonsProtGroupTtops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("n", 0),
          ("y", 1))
    )


_CienaOme6500OptmonsProtGroupTtops_Type.__name__ = "Integer32"
_CienaOme6500OptmonsProtGroupTtops_Object = MibTableColumn
cienaOme6500OptmonsProtGroupTtops = _CienaOme6500OptmonsProtGroupTtops_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 13),
    _CienaOme6500OptmonsProtGroupTtops_Type()
)
cienaOme6500OptmonsProtGroupTtops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupTtops.setStatus("current")


class _CienaOme6500OptmonsProtGroupPsDirn_Type(Integer32):
    """Custom type cienaOme6500OptmonsProtGroupPsDirn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uni", 0),
          ("bi", 1))
    )


_CienaOme6500OptmonsProtGroupPsDirn_Type.__name__ = "Integer32"
_CienaOme6500OptmonsProtGroupPsDirn_Object = MibTableColumn
cienaOme6500OptmonsProtGroupPsDirn = _CienaOme6500OptmonsProtGroupPsDirn_Object(
    (1, 3, 6, 1, 4, 1, 1271, 29, 7, 2, 1, 14),
    _CienaOme6500OptmonsProtGroupPsDirn_Type()
)
cienaOme6500OptmonsProtGroupPsDirn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaOme6500OptmonsProtGroupPsDirn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-OME6500-OPTMONS-MIB",
    **{"cienaOme6500OptmonsMIB": cienaOme6500OptmonsMIB,
       "cienaOme6500OptmonsTable": cienaOme6500OptmonsTable,
       "cienaOme6500OptmonsEntry": cienaOme6500OptmonsEntry,
       "cienaOme6500OptmonsIfIndex": cienaOme6500OptmonsIfIndex,
       "cienaOme6500OptmonsIfDescr": cienaOme6500OptmonsIfDescr,
       "cienaOme6500OptmonsSst": cienaOme6500OptmonsSst,
       "cienaOme6500OptmonsPst": cienaOme6500OptmonsPst,
       "cienaOme6500OptmonsAinsTimeLeft": cienaOme6500OptmonsAinsTimeLeft,
       "cienaOme6500OptmonsLosThres": cienaOme6500OptmonsLosThres,
       "cienaOme6500OptmonsPortLabel": cienaOme6500OptmonsPortLabel,
       "cienaOme6500OptmonsAlsoDisabled": cienaOme6500OptmonsAlsoDisabled,
       "cienaOme6500OptmonsProtNswSwStatus": cienaOme6500OptmonsProtNswSwStatus,
       "cienaOme6500OptmonsProtNswSwEnd": cienaOme6500OptmonsProtNswSwEnd,
       "cienaOme6500OptmonsProtNswSwReason": cienaOme6500OptmonsProtNswSwReason,
       "cienaOme6500OptmonsProtGroupTable": cienaOme6500OptmonsProtGroupTable,
       "cienaOme6500OptmonsProtGroupEntry": cienaOme6500OptmonsProtGroupEntry,
       "cienaOme6500OptmonsProtGroupWrkgIfIndex": cienaOme6500OptmonsProtGroupWrkgIfIndex,
       "cienaOme6500OptmonsProtGroupWrkgIfDescr": cienaOme6500OptmonsProtGroupWrkgIfDescr,
       "cienaOme6500OptmonsProtGroupWrkgSst": cienaOme6500OptmonsProtGroupWrkgSst,
       "cienaOme6500OptmonsProtGroupProtIfIndex": cienaOme6500OptmonsProtGroupProtIfIndex,
       "cienaOme6500OptmonsProtGroupProtIfDescr": cienaOme6500OptmonsProtGroupProtIfDescr,
       "cienaOme6500OptmonsProtGroupProtSst": cienaOme6500OptmonsProtGroupProtSst,
       "cienaOme6500OptmonsProtGroupProtScheme": cienaOme6500OptmonsProtGroupProtScheme,
       "cienaOme6500OptmonsProtGroupWaitToRestore": cienaOme6500OptmonsProtGroupWaitToRestore,
       "cienaOme6500OptmonsProtGroupDetectGuardTime": cienaOme6500OptmonsProtGroupDetectGuardTime,
       "cienaOme6500OptmonsProtGroupRevertive": cienaOme6500OptmonsProtGroupRevertive,
       "cienaOme6500OptmonsProtGroupRemStandard": cienaOme6500OptmonsProtGroupRemStandard,
       "cienaOme6500OptmonsProtGroupLossPwr": cienaOme6500OptmonsProtGroupLossPwr,
       "cienaOme6500OptmonsProtGroupTtops": cienaOme6500OptmonsProtGroupTtops,
       "cienaOme6500OptmonsProtGroupPsDirn": cienaOme6500OptmonsProtGroupPsDirn}
)
