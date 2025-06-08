# SNMP MIB module (INS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/INS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_InsAgents_ObjectIdentity = ObjectIdentity
insAgents = _InsAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200)
)
_Ins_ObjectIdentity = ObjectIdentity
ins = _Ins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1)
)
_InsSystemGroup_ObjectIdentity = ObjectIdentity
insSystemGroup = _InsSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1)
)


class _InsSysReset_Type(Integer32):
    """Custom type insSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("software-reset", 1),
          ("factory-reset", 2))
    )


_InsSysReset_Type.__name__ = "Integer32"
_InsSysReset_Object = MibScalar
insSysReset = _InsSysReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 1),
    _InsSysReset_Type()
)
insSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insSysReset.setStatus("mandatory")


class _InsAdminStatus_Type(Integer32):
    """Custom type insAdminStatus based on Integer32"""
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
        *(("on-line", 1),
          ("off-line", 2),
          ("unknown", 3))
    )


_InsAdminStatus_Type.__name__ = "Integer32"
_InsAdminStatus_Object = MibScalar
insAdminStatus = _InsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 2),
    _InsAdminStatus_Type()
)
insAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insAdminStatus.setStatus("mandatory")


class _InsOperStatus_Type(Integer32):
    """Custom type insOperStatus based on Integer32"""
    defaultValue = 4

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
        *(("on-line", 1),
          ("off-line", 2),
          ("failure", 3),
          ("unknown", 4))
    )


_InsOperStatus_Type.__name__ = "Integer32"
_InsOperStatus_Object = MibScalar
insOperStatus = _InsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 3),
    _InsOperStatus_Type()
)
insOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insOperStatus.setStatus("mandatory")


class _InsAlarmStatus_Type(Integer32):
    """Custom type insAlarmStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor-alarm", 2),
          ("major-alarm", 3))
    )


_InsAlarmStatus_Type.__name__ = "Integer32"
_InsAlarmStatus_Object = MibScalar
insAlarmStatus = _InsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 4),
    _InsAlarmStatus_Type()
)
insAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insAlarmStatus.setStatus("mandatory")
_InsRelease_Type = DisplayString
_InsRelease_Object = MibScalar
insRelease = _InsRelease_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 5),
    _InsRelease_Type()
)
insRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insRelease.setStatus("mandatory")
_InsVersion_Type = DisplayString
_InsVersion_Object = MibScalar
insVersion = _InsVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 6),
    _InsVersion_Type()
)
insVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insVersion.setStatus("mandatory")


class _InsSysType_Type(Integer32):
    """Custom type insSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("das", 1),
          ("dasd", 2))
    )


_InsSysType_Type.__name__ = "Integer32"
_InsSysType_Object = MibScalar
insSysType = _InsSysType_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 7),
    _InsSysType_Type()
)
insSysType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insSysType.setStatus("mandatory")


class _InsPrevOperStatus_Type(Integer32):
    """Custom type insPrevOperStatus based on Integer32"""
    defaultValue = 4

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
        *(("on-line", 1),
          ("off-line", 2),
          ("failure", 3),
          ("unknown", 4))
    )


_InsPrevOperStatus_Type.__name__ = "Integer32"
_InsPrevOperStatus_Object = MibScalar
insPrevOperStatus = _InsPrevOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 8),
    _InsPrevOperStatus_Type()
)
insPrevOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insPrevOperStatus.setStatus("mandatory")


class _InsUpdtStatus_Type(Integer32):
    """Custom type insUpdtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_InsUpdtStatus_Type.__name__ = "Integer32"
_InsUpdtStatus_Object = MibScalar
insUpdtStatus = _InsUpdtStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 9),
    _InsUpdtStatus_Type()
)
insUpdtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insUpdtStatus.setStatus("mandatory")


class _InsPeerStatus_Type(Integer32):
    """Custom type insPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2),
          ("unknown", 3))
    )


_InsPeerStatus_Type.__name__ = "Integer32"
_InsPeerStatus_Object = MibScalar
insPeerStatus = _InsPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 10),
    _InsPeerStatus_Type()
)
insPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insPeerStatus.setStatus("mandatory")


class _InsBurstUpdt_Type(Integer32):
    """Custom type insBurstUpdt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_InsBurstUpdt_Type.__name__ = "Integer32"
_InsBurstUpdt_Object = MibScalar
insBurstUpdt = _InsBurstUpdt_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 11),
    _InsBurstUpdt_Type()
)
insBurstUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insBurstUpdt.setStatus("mandatory")


class _InsAdaxStatus_Type(Integer32):
    """Custom type insAdaxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("failed", 2))
    )


_InsAdaxStatus_Type.__name__ = "Integer32"
_InsAdaxStatus_Object = MibScalar
insAdaxStatus = _InsAdaxStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 12),
    _InsAdaxStatus_Type()
)
insAdaxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insAdaxStatus.setStatus("mandatory")


class _InsDatabaseStatus_Type(Integer32):
    """Custom type insDatabaseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("failed", 2))
    )


_InsDatabaseStatus_Type.__name__ = "Integer32"
_InsDatabaseStatus_Object = MibScalar
insDatabaseStatus = _InsDatabaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 13),
    _InsDatabaseStatus_Type()
)
insDatabaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insDatabaseStatus.setStatus("mandatory")


class _InsDiskStatus_Type(Integer32):
    """Custom type insDiskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("failed", 2))
    )


_InsDiskStatus_Type.__name__ = "Integer32"
_InsDiskStatus_Object = MibScalar
insDiskStatus = _InsDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 14),
    _InsDiskStatus_Type()
)
insDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insDiskStatus.setStatus("mandatory")


class _InsGenericStatus_Type(Integer32):
    """Custom type insGenericStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("failed", 2))
    )


_InsGenericStatus_Type.__name__ = "Integer32"
_InsGenericStatus_Object = MibScalar
insGenericStatus = _InsGenericStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 15),
    _InsGenericStatus_Type()
)
insGenericStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insGenericStatus.setStatus("mandatory")


class _InsSpecificStatus_Type(Integer32):
    """Custom type insSpecificStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("failed", 2))
    )


_InsSpecificStatus_Type.__name__ = "Integer32"
_InsSpecificStatus_Object = MibScalar
insSpecificStatus = _InsSpecificStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 16),
    _InsSpecificStatus_Type()
)
insSpecificStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insSpecificStatus.setStatus("mandatory")
_InsRedInsTable_Object = MibTable
insRedInsTable = _InsRedInsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17)
)
if mibBuilder.loadTexts:
    insRedInsTable.setStatus("mandatory")
_InsRedInsEntry_Object = MibTableRow
insRedInsEntry = _InsRedInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1)
)
insRedInsEntry.setIndexNames(
    (0, "INS-MIB", "sysNum"),
)
if mibBuilder.loadTexts:
    insRedInsEntry.setStatus("mandatory")


class _SysNum_Type(Integer32):
    """Custom type sysNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SysNum_Type.__name__ = "Integer32"
_SysNum_Object = MibTableColumn
sysNum = _SysNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1, 1),
    _SysNum_Type()
)
sysNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNum.setStatus("mandatory")


class _RedName_Type(DisplayString):
    """Custom type redName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RedName_Type.__name__ = "DisplayString"
_RedName_Object = MibTableColumn
redName = _RedName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1, 2),
    _RedName_Type()
)
redName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redName.setStatus("mandatory")
_RedPeerIpAddress_Type = IpAddress
_RedPeerIpAddress_Object = MibTableColumn
redPeerIpAddress = _RedPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1, 3),
    _RedPeerIpAddress_Type()
)
redPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redPeerIpAddress.setStatus("mandatory")
_RedOwnFrIpAddress_Type = IpAddress
_RedOwnFrIpAddress_Object = MibTableColumn
redOwnFrIpAddress = _RedOwnFrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1, 4),
    _RedOwnFrIpAddress_Type()
)
redOwnFrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redOwnFrIpAddress.setStatus("mandatory")
_RedPeerFrIpAddress_Type = IpAddress
_RedPeerFrIpAddress_Object = MibTableColumn
redPeerFrIpAddress = _RedPeerFrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1, 5),
    _RedPeerFrIpAddress_Type()
)
redPeerFrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redPeerFrIpAddress.setStatus("mandatory")


class _RedRedInsRowStatus_Type(Integer32):
    """Custom type redRedInsRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-wait", 5),
          ("destroy", 6))
    )


_RedRedInsRowStatus_Type.__name__ = "Integer32"
_RedRedInsRowStatus_Object = MibTableColumn
redRedInsRowStatus = _RedRedInsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 1, 17, 1, 6),
    _RedRedInsRowStatus_Type()
)
redRedInsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redRedInsRowStatus.setStatus("mandatory")
_InsServerGroup_ObjectIdentity = ObjectIdentity
insServerGroup = _InsServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2)
)
_InsServerTable_Object = MibTable
insServerTable = _InsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1)
)
if mibBuilder.loadTexts:
    insServerTable.setStatus("mandatory")
_InsServerEntry_Object = MibTableRow
insServerEntry = _InsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1)
)
insServerEntry.setIndexNames(
    (0, "INS-MIB", "insServerPreference"),
)
if mibBuilder.loadTexts:
    insServerEntry.setStatus("mandatory")


class _InsServerPreference_Type(Integer32):
    """Custom type insServerPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_InsServerPreference_Type.__name__ = "Integer32"
_InsServerPreference_Object = MibTableColumn
insServerPreference = _InsServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 1),
    _InsServerPreference_Type()
)
insServerPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insServerPreference.setStatus("mandatory")
_InsServerIpAddr_Type = IpAddress
_InsServerIpAddr_Object = MibTableColumn
insServerIpAddr = _InsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 2),
    _InsServerIpAddr_Type()
)
insServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insServerIpAddr.setStatus("mandatory")


class _InsServerName_Type(DisplayString):
    """Custom type insServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InsServerName_Type.__name__ = "DisplayString"
_InsServerName_Object = MibTableColumn
insServerName = _InsServerName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 3),
    _InsServerName_Type()
)
insServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insServerName.setStatus("mandatory")


class _InsServerAdminStatus_Type(Integer32):
    """Custom type insServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_InsServerAdminStatus_Type.__name__ = "Integer32"
_InsServerAdminStatus_Object = MibTableColumn
insServerAdminStatus = _InsServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 4),
    _InsServerAdminStatus_Type()
)
insServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insServerAdminStatus.setStatus("mandatory")
_InsStbyServerIpAddr_Type = IpAddress
_InsStbyServerIpAddr_Object = MibTableColumn
insStbyServerIpAddr = _InsStbyServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 5),
    _InsStbyServerIpAddr_Type()
)
insStbyServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insStbyServerIpAddr.setStatus("mandatory")


class _InsStbyServerName_Type(DisplayString):
    """Custom type insStbyServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InsStbyServerName_Type.__name__ = "DisplayString"
_InsStbyServerName_Object = MibTableColumn
insStbyServerName = _InsStbyServerName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 6),
    _InsStbyServerName_Type()
)
insStbyServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insStbyServerName.setStatus("mandatory")


class _InsServerRowStatus_Type(Integer32):
    """Custom type insServerRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-wait", 5),
          ("destroy", 6))
    )


_InsServerRowStatus_Type.__name__ = "Integer32"
_InsServerRowStatus_Object = MibTableColumn
insServerRowStatus = _InsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 1, 1, 7),
    _InsServerRowStatus_Type()
)
insServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insServerRowStatus.setStatus("mandatory")


class _InsdLocalNode_Type(DisplayString):
    """Custom type insdLocalNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InsdLocalNode_Type.__name__ = "DisplayString"
_InsdLocalNode_Object = MibScalar
insdLocalNode = _InsdLocalNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 2),
    _InsdLocalNode_Type()
)
insdLocalNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdLocalNode.setStatus("mandatory")


class _InsdLocalShelf_Type(DisplayString):
    """Custom type insdLocalShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InsdLocalShelf_Type.__name__ = "DisplayString"
_InsdLocalShelf_Object = MibScalar
insdLocalShelf = _InsdLocalShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 3),
    _InsdLocalShelf_Type()
)
insdLocalShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdLocalShelf.setStatus("mandatory")


class _InsdLocalSlot_Type(Integer32):
    """Custom type insdLocalSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsdLocalSlot_Type.__name__ = "Integer32"
_InsdLocalSlot_Object = MibScalar
insdLocalSlot = _InsdLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 4),
    _InsdLocalSlot_Type()
)
insdLocalSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdLocalSlot.setStatus("mandatory")


class _InsdLocalLine_Type(Integer32):
    """Custom type insdLocalLine based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1023),
    )


_InsdLocalLine_Type.__name__ = "Integer32"
_InsdLocalLine_Object = MibScalar
insdLocalLine = _InsdLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 5),
    _InsdLocalLine_Type()
)
insdLocalLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdLocalLine.setStatus("mandatory")


class _InsdLocalPort_Type(Integer32):
    """Custom type insdLocalPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsdLocalPort_Type.__name__ = "Integer32"
_InsdLocalPort_Object = MibScalar
insdLocalPort = _InsdLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 6),
    _InsdLocalPort_Type()
)
insdLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdLocalPort.setStatus("mandatory")


class _InsdLocalDlci_Type(Integer32):
    """Custom type insdLocalDlci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsdLocalDlci_Type.__name__ = "Integer32"
_InsdLocalDlci_Object = MibScalar
insdLocalDlci = _InsdLocalDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 7),
    _InsdLocalDlci_Type()
)
insdLocalDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdLocalDlci.setStatus("mandatory")


class _InsdRemoteNode_Type(DisplayString):
    """Custom type insdRemoteNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InsdRemoteNode_Type.__name__ = "DisplayString"
_InsdRemoteNode_Object = MibScalar
insdRemoteNode = _InsdRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 8),
    _InsdRemoteNode_Type()
)
insdRemoteNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdRemoteNode.setStatus("mandatory")


class _InsdRemoteShelf_Type(DisplayString):
    """Custom type insdRemoteShelf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InsdRemoteShelf_Type.__name__ = "DisplayString"
_InsdRemoteShelf_Object = MibScalar
insdRemoteShelf = _InsdRemoteShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 9),
    _InsdRemoteShelf_Type()
)
insdRemoteShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdRemoteShelf.setStatus("mandatory")


class _InsdRemoteSlot_Type(Integer32):
    """Custom type insdRemoteSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsdRemoteSlot_Type.__name__ = "Integer32"
_InsdRemoteSlot_Object = MibScalar
insdRemoteSlot = _InsdRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 10),
    _InsdRemoteSlot_Type()
)
insdRemoteSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdRemoteSlot.setStatus("mandatory")


class _InsdRemoteLine_Type(Integer32):
    """Custom type insdRemoteLine based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1023),
    )


_InsdRemoteLine_Type.__name__ = "Integer32"
_InsdRemoteLine_Object = MibScalar
insdRemoteLine = _InsdRemoteLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 11),
    _InsdRemoteLine_Type()
)
insdRemoteLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdRemoteLine.setStatus("mandatory")


class _InsdRemotePort_Type(Integer32):
    """Custom type insdRemotePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsdRemotePort_Type.__name__ = "Integer32"
_InsdRemotePort_Object = MibScalar
insdRemotePort = _InsdRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 12),
    _InsdRemotePort_Type()
)
insdRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdRemotePort.setStatus("mandatory")


class _InsdRemoteDlci_Type(Integer32):
    """Custom type insdRemoteDlci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsdRemoteDlci_Type.__name__ = "Integer32"
_InsdRemoteDlci_Object = MibScalar
insdRemoteDlci = _InsdRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 13),
    _InsdRemoteDlci_Type()
)
insdRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdRemoteDlci.setStatus("mandatory")


class _InsdConnAni_Type(DisplayString):
    """Custom type insdConnAni based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InsdConnAni_Type.__name__ = "DisplayString"
_InsdConnAni_Object = MibScalar
insdConnAni = _InsdConnAni_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 14),
    _InsdConnAni_Type()
)
insdConnAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdConnAni.setStatus("mandatory")


class _InsdConnStatus_Type(Integer32):
    """Custom type insdConnStatus based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("invalid-ins-station", 1),
          ("invalid-calling-number", 2),
          ("no-ANI-end-point", 3),
          ("no-conn-for-ANI", 4),
          ("repair-pending-for-ANI", 5),
          ("conn-translation-fail", 6),
          ("conn-record-fail", 7),
          ("no-assoc", 8),
          ("create-conn-fail", 9))
    )


_InsdConnStatus_Type.__name__ = "Integer32"
_InsdConnStatus_Object = MibScalar
insdConnStatus = _InsdConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 15),
    _InsdConnStatus_Type()
)
insdConnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdConnStatus.setStatus("mandatory")


class _InsdPortStatus_Type(Integer32):
    """Custom type insdPortStatus based on Integer32"""
    defaultValue = 5

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
        *(("down-port-fail", 1),
          ("delete-port-fail", 2),
          ("add-port-fail", 3),
          ("up-port-fail", 4),
          ("set-port-fail", 5))
    )


_InsdPortStatus_Type.__name__ = "Integer32"
_InsdPortStatus_Object = MibScalar
insdPortStatus = _InsdPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 2, 16),
    _InsdPortStatus_Type()
)
insdPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insdPortStatus.setStatus("mandatory")
_InsDialupConfigGroup_ObjectIdentity = ObjectIdentity
insDialupConfigGroup = _InsDialupConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3)
)


class _InsDialupCdrFileBackupInterval_Type(Integer32):
    """Custom type insDialupCdrFileBackupInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_InsDialupCdrFileBackupInterval_Type.__name__ = "Integer32"
_InsDialupCdrFileBackupInterval_Object = MibScalar
insDialupCdrFileBackupInterval = _InsDialupCdrFileBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 1),
    _InsDialupCdrFileBackupInterval_Type()
)
insDialupCdrFileBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupCdrFileBackupInterval.setStatus("mandatory")


class _InsDialupCdrFileBackupCount_Type(Integer32):
    """Custom type insDialupCdrFileBackupCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_InsDialupCdrFileBackupCount_Type.__name__ = "Integer32"
_InsDialupCdrFileBackupCount_Object = MibScalar
insDialupCdrFileBackupCount = _InsDialupCdrFileBackupCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 2),
    _InsDialupCdrFileBackupCount_Type()
)
insDialupCdrFileBackupCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupCdrFileBackupCount.setStatus("mandatory")
_InsDialupSwitchTable_Object = MibTable
insDialupSwitchTable = _InsDialupSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 3)
)
if mibBuilder.loadTexts:
    insDialupSwitchTable.setStatus("mandatory")
_InsDialupSwitchEntry_Object = MibTableRow
insDialupSwitchEntry = _InsDialupSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 3, 1)
)
insDialupSwitchEntry.setIndexNames(
    (0, "INS-MIB", "insDialupSwitchDlci"),
)
if mibBuilder.loadTexts:
    insDialupSwitchEntry.setStatus("mandatory")


class _InsDialupSwitchDlci_Type(Integer32):
    """Custom type insDialupSwitchDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsDialupSwitchDlci_Type.__name__ = "Integer32"
_InsDialupSwitchDlci_Object = MibTableColumn
insDialupSwitchDlci = _InsDialupSwitchDlci_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 3, 1, 1),
    _InsDialupSwitchDlci_Type()
)
insDialupSwitchDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupSwitchDlci.setStatus("mandatory")


class _InsDialupSwitchType_Type(Integer32):
    """Custom type insDialupSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("att-4ess", 1),
          ("att-5ess", 2),
          ("nt-dms100", 3),
          ("nt-dms250", 4),
          ("ntt", 5),
          ("etsi", 6),
          ("austel", 7),
          ("dasi", 8))
    )


_InsDialupSwitchType_Type.__name__ = "Integer32"
_InsDialupSwitchType_Object = MibTableColumn
insDialupSwitchType = _InsDialupSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 3, 1, 2),
    _InsDialupSwitchType_Type()
)
insDialupSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupSwitchType.setStatus("mandatory")


class _InsDialupSwitchInterface_Type(Integer32):
    """Custom type insDialupSwitchInterface based on Integer32"""
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
        *(("t1", 1),
          ("e1", 2),
          ("v35", 3),
          ("x21", 4))
    )


_InsDialupSwitchInterface_Type.__name__ = "Integer32"
_InsDialupSwitchInterface_Object = MibTableColumn
insDialupSwitchInterface = _InsDialupSwitchInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 3, 1, 3),
    _InsDialupSwitchInterface_Type()
)
insDialupSwitchInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupSwitchInterface.setStatus("mandatory")


class _InsDialupSwitchRowStatus_Type(Integer32):
    """Custom type insDialupSwitchRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-wait", 5),
          ("destroy", 6))
    )


_InsDialupSwitchRowStatus_Type.__name__ = "Integer32"
_InsDialupSwitchRowStatus_Object = MibTableColumn
insDialupSwitchRowStatus = _InsDialupSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 3, 1, 4),
    _InsDialupSwitchRowStatus_Type()
)
insDialupSwitchRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupSwitchRowStatus.setStatus("mandatory")
_InsDialupCallTraceNumber_Type = DisplayString
_InsDialupCallTraceNumber_Object = MibScalar
insDialupCallTraceNumber = _InsDialupCallTraceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 3, 4),
    _InsDialupCallTraceNumber_Type()
)
insDialupCallTraceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insDialupCallTraceNumber.setStatus("mandatory")
_InsEventGroup_ObjectIdentity = ObjectIdentity
insEventGroup = _InsEventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4)
)
_InsEventLatestIndex_Type = Integer32
_InsEventLatestIndex_Object = MibScalar
insEventLatestIndex = _InsEventLatestIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 1),
    _InsEventLatestIndex_Type()
)
insEventLatestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventLatestIndex.setStatus("mandatory")
_InsEventTable_Object = MibTable
insEventTable = _InsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2)
)
if mibBuilder.loadTexts:
    insEventTable.setStatus("mandatory")
_InsEventEntry_Object = MibTableRow
insEventEntry = _InsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1)
)
insEventEntry.setIndexNames(
    (0, "INS-MIB", "insEventIndex"),
)
if mibBuilder.loadTexts:
    insEventEntry.setStatus("mandatory")


class _InsEventIndex_Type(Integer32):
    """Custom type insEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InsEventIndex_Type.__name__ = "Integer32"
_InsEventIndex_Object = MibTableColumn
insEventIndex = _InsEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 1),
    _InsEventIndex_Type()
)
insEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    insEventIndex.setStatus("mandatory")


class _InsEventClass_Type(Integer32):
    """Custom type insEventClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("information", 1),
          ("alarm", 2))
    )


_InsEventClass_Type.__name__ = "Integer32"
_InsEventClass_Object = MibTableColumn
insEventClass = _InsEventClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 2),
    _InsEventClass_Type()
)
insEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventClass.setStatus("mandatory")


class _InsEventType_Type(Integer32):
    """Custom type insEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ipx-communication-failure", 1),
          ("ins-server-communication-failure", 2),
          ("isdn-switch-communication-failure", 3),
          ("disk-threshold-reached", 4),
          ("nms-communication-failure", 5),
          ("cold-start", 6),
          ("software-reset", 7),
          ("factory-reset", 8),
          ("ins-online", 9),
          ("ins-offline", 10),
          ("ins-failure", 11),
          ("received-insAdminStatus-down", 12),
          ("received-insAdminStatus-up", 13),
          ("cdr-file-expired", 14),
          ("interprocess-communication-failure", 15),
          ("received-interrupt-to-terminate-process", 16),
          ("memory-allocation-failure", 17),
          ("cannot-open-cdr-file", 18),
          ("cannot-rename-cdr-file", 19))
    )


_InsEventType_Type.__name__ = "Integer32"
_InsEventType_Object = MibTableColumn
insEventType = _InsEventType_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 3),
    _InsEventType_Type()
)
insEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventType.setStatus("mandatory")
_InsEventInstance_Type = DisplayString
_InsEventInstance_Object = MibTableColumn
insEventInstance = _InsEventInstance_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 4),
    _InsEventInstance_Type()
)
insEventInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventInstance.setStatus("mandatory")
_InsEventTimeStamp_Type = TimeTicks
_InsEventTimeStamp_Object = MibTableColumn
insEventTimeStamp = _InsEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 5),
    _InsEventTimeStamp_Type()
)
insEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventTimeStamp.setStatus("mandatory")


class _InsEventSeverity_Type(Integer32):
    """Custom type insEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor-alarm", 2),
          ("major-alarm", 3))
    )


_InsEventSeverity_Type.__name__ = "Integer32"
_InsEventSeverity_Object = MibTableColumn
insEventSeverity = _InsEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 6),
    _InsEventSeverity_Type()
)
insEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventSeverity.setStatus("mandatory")


class _InsEventDescription_Type(DisplayString):
    """Custom type insEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InsEventDescription_Type.__name__ = "DisplayString"
_InsEventDescription_Object = MibTableColumn
insEventDescription = _InsEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 7),
    _InsEventDescription_Type()
)
insEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insEventDescription.setStatus("mandatory")


class _InsEventRowStatus_Type(Integer32):
    """Custom type insEventRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-wait", 5),
          ("destroy", 6))
    )


_InsEventRowStatus_Type.__name__ = "Integer32"
_InsEventRowStatus_Object = MibTableColumn
insEventRowStatus = _InsEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 2, 1, 8),
    _InsEventRowStatus_Type()
)
insEventRowStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    insEventRowStatus.setStatus("mandatory")


class _InsPRIFailCause_Type(Integer32):
    """Custom type insPRIFailCause based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-down-reset", 1),
          ("process-error", 2))
    )


_InsPRIFailCause_Type.__name__ = "Integer32"
_InsPRIFailCause_Object = MibScalar
insPRIFailCause = _InsPRIFailCause_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 3),
    _InsPRIFailCause_Type()
)
insPRIFailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insPRIFailCause.setStatus("mandatory")


class _InsCallFailureCause_Type(Integer32):
    """Custom type insCallFailureCause based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_InsCallFailureCause_Type.__name__ = "Integer32"
_InsCallFailureCause_Object = MibScalar
insCallFailureCause = _InsCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 4),
    _InsCallFailureCause_Type()
)
insCallFailureCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insCallFailureCause.setStatus("mandatory")


class _InsProtocolErrorCause_Type(Integer32):
    """Custom type insProtocolErrorCause based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_InsProtocolErrorCause_Type.__name__ = "Integer32"
_InsProtocolErrorCause_Object = MibScalar
insProtocolErrorCause = _InsProtocolErrorCause_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 5),
    _InsProtocolErrorCause_Type()
)
insProtocolErrorCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insProtocolErrorCause.setStatus("mandatory")


class _InsProtocolMessage_Type(Integer32):
    """Custom type insProtocolMessage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 117),
    )


_InsProtocolMessage_Type.__name__ = "Integer32"
_InsProtocolMessage_Object = MibScalar
insProtocolMessage = _InsProtocolMessage_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 6),
    _InsProtocolMessage_Type()
)
insProtocolMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insProtocolMessage.setStatus("mandatory")


class _InsCallOperation_Type(Integer32):
    """Custom type insCallOperation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("setup", 1),
          ("disconnect", 2))
    )


_InsCallOperation_Type.__name__ = "Integer32"
_InsCallOperation_Object = MibScalar
insCallOperation = _InsCallOperation_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 7),
    _InsCallOperation_Type()
)
insCallOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insCallOperation.setStatus("mandatory")


class _InsCallingNumber_Type(DisplayString):
    """Custom type insCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InsCallingNumber_Type.__name__ = "DisplayString"
_InsCallingNumber_Object = MibScalar
insCallingNumber = _InsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 8),
    _InsCallingNumber_Type()
)
insCallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insCallingNumber.setStatus("mandatory")


class _InsCalledNumber_Type(DisplayString):
    """Custom type insCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InsCalledNumber_Type.__name__ = "DisplayString"
_InsCalledNumber_Object = MibScalar
insCalledNumber = _InsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 9),
    _InsCalledNumber_Type()
)
insCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insCalledNumber.setStatus("mandatory")


class _InsBearerChannel_Type(Integer32):
    """Custom type insBearerChannel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_InsBearerChannel_Type.__name__ = "Integer32"
_InsBearerChannel_Object = MibScalar
insBearerChannel = _InsBearerChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 4, 10),
    _InsBearerChannel_Type()
)
insBearerChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    insBearerChannel.setStatus("mandatory")
_NmsGroup_ObjectIdentity = ObjectIdentity
nmsGroup = _NmsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5)
)
_NmsTable_Object = MibTable
nmsTable = _NmsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1)
)
if mibBuilder.loadTexts:
    nmsTable.setStatus("mandatory")
_NmsEntry_Object = MibTableRow
nmsEntry = _NmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1, 1)
)
nmsEntry.setIndexNames(
    (0, "INS-MIB", "nmsPreference"),
)
if mibBuilder.loadTexts:
    nmsEntry.setStatus("mandatory")


class _NmsPreference_Type(Integer32):
    """Custom type nmsPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NmsPreference_Type.__name__ = "Integer32"
_NmsPreference_Object = MibTableColumn
nmsPreference = _NmsPreference_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1, 1, 1),
    _NmsPreference_Type()
)
nmsPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsPreference.setStatus("mandatory")
_NmsIpAddr_Type = IpAddress
_NmsIpAddr_Object = MibTableColumn
nmsIpAddr = _NmsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1, 1, 2),
    _NmsIpAddr_Type()
)
nmsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIpAddr.setStatus("mandatory")


class _NmsName_Type(DisplayString):
    """Custom type nmsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsName_Type.__name__ = "DisplayString"
_NmsName_Object = MibTableColumn
nmsName = _NmsName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1, 1, 3),
    _NmsName_Type()
)
nmsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsName.setStatus("mandatory")


class _NmsDbName_Type(DisplayString):
    """Custom type nmsDbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsDbName_Type.__name__ = "DisplayString"
_NmsDbName_Object = MibTableColumn
nmsDbName = _NmsDbName_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1, 1, 4),
    _NmsDbName_Type()
)
nmsDbName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsDbName.setStatus("mandatory")


class _NmsRowStatus_Type(Integer32):
    """Custom type nmsRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create-and-wait", 5),
          ("destroy", 6))
    )


_NmsRowStatus_Type.__name__ = "Integer32"
_NmsRowStatus_Object = MibTableColumn
nmsRowStatus = _NmsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 200, 1, 5, 1, 1, 5),
    _NmsRowStatus_Type()
)
nmsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INS-MIB",
    **{"stratacom": stratacom,
       "insAgents": insAgents,
       "ins": ins,
       "insSystemGroup": insSystemGroup,
       "insSysReset": insSysReset,
       "insAdminStatus": insAdminStatus,
       "insOperStatus": insOperStatus,
       "insAlarmStatus": insAlarmStatus,
       "insRelease": insRelease,
       "insVersion": insVersion,
       "insSysType": insSysType,
       "insPrevOperStatus": insPrevOperStatus,
       "insUpdtStatus": insUpdtStatus,
       "insPeerStatus": insPeerStatus,
       "insBurstUpdt": insBurstUpdt,
       "insAdaxStatus": insAdaxStatus,
       "insDatabaseStatus": insDatabaseStatus,
       "insDiskStatus": insDiskStatus,
       "insGenericStatus": insGenericStatus,
       "insSpecificStatus": insSpecificStatus,
       "insRedInsTable": insRedInsTable,
       "insRedInsEntry": insRedInsEntry,
       "sysNum": sysNum,
       "redName": redName,
       "redPeerIpAddress": redPeerIpAddress,
       "redOwnFrIpAddress": redOwnFrIpAddress,
       "redPeerFrIpAddress": redPeerFrIpAddress,
       "redRedInsRowStatus": redRedInsRowStatus,
       "insServerGroup": insServerGroup,
       "insServerTable": insServerTable,
       "insServerEntry": insServerEntry,
       "insServerPreference": insServerPreference,
       "insServerIpAddr": insServerIpAddr,
       "insServerName": insServerName,
       "insServerAdminStatus": insServerAdminStatus,
       "insStbyServerIpAddr": insStbyServerIpAddr,
       "insStbyServerName": insStbyServerName,
       "insServerRowStatus": insServerRowStatus,
       "insdLocalNode": insdLocalNode,
       "insdLocalShelf": insdLocalShelf,
       "insdLocalSlot": insdLocalSlot,
       "insdLocalLine": insdLocalLine,
       "insdLocalPort": insdLocalPort,
       "insdLocalDlci": insdLocalDlci,
       "insdRemoteNode": insdRemoteNode,
       "insdRemoteShelf": insdRemoteShelf,
       "insdRemoteSlot": insdRemoteSlot,
       "insdRemoteLine": insdRemoteLine,
       "insdRemotePort": insdRemotePort,
       "insdRemoteDlci": insdRemoteDlci,
       "insdConnAni": insdConnAni,
       "insdConnStatus": insdConnStatus,
       "insdPortStatus": insdPortStatus,
       "insDialupConfigGroup": insDialupConfigGroup,
       "insDialupCdrFileBackupInterval": insDialupCdrFileBackupInterval,
       "insDialupCdrFileBackupCount": insDialupCdrFileBackupCount,
       "insDialupSwitchTable": insDialupSwitchTable,
       "insDialupSwitchEntry": insDialupSwitchEntry,
       "insDialupSwitchDlci": insDialupSwitchDlci,
       "insDialupSwitchType": insDialupSwitchType,
       "insDialupSwitchInterface": insDialupSwitchInterface,
       "insDialupSwitchRowStatus": insDialupSwitchRowStatus,
       "insDialupCallTraceNumber": insDialupCallTraceNumber,
       "insEventGroup": insEventGroup,
       "insEventLatestIndex": insEventLatestIndex,
       "insEventTable": insEventTable,
       "insEventEntry": insEventEntry,
       "insEventIndex": insEventIndex,
       "insEventClass": insEventClass,
       "insEventType": insEventType,
       "insEventInstance": insEventInstance,
       "insEventTimeStamp": insEventTimeStamp,
       "insEventSeverity": insEventSeverity,
       "insEventDescription": insEventDescription,
       "insEventRowStatus": insEventRowStatus,
       "insPRIFailCause": insPRIFailCause,
       "insCallFailureCause": insCallFailureCause,
       "insProtocolErrorCause": insProtocolErrorCause,
       "insProtocolMessage": insProtocolMessage,
       "insCallOperation": insCallOperation,
       "insCallingNumber": insCallingNumber,
       "insCalledNumber": insCalledNumber,
       "insBearerChannel": insBearerChannel,
       "nmsGroup": nmsGroup,
       "nmsTable": nmsTable,
       "nmsEntry": nmsEntry,
       "nmsPreference": nmsPreference,
       "nmsIpAddr": nmsIpAddr,
       "nmsName": nmsName,
       "nmsDbName": nmsDbName,
       "nmsRowStatus": nmsRowStatus}
)
