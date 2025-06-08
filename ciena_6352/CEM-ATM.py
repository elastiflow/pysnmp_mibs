# SNMP MIB module (CEM-ATM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-ATM.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(atmTrafficDescrParamEntry,
 atmVcCrossConnectAdminStatus,
 atmVcCrossConnectEntry,
 atmVcCrossConnectH2LLastChange,
 atmVcCrossConnectH2LOperStatus,
 atmVcCrossConnectHighIfIndex,
 atmVcCrossConnectHighVci,
 atmVcCrossConnectHighVpi,
 atmVcCrossConnectIndex,
 atmVcCrossConnectL2HLastChange,
 atmVcCrossConnectL2HOperStatus,
 atmVcCrossConnectLowIfIndex,
 atmVcCrossConnectLowVci,
 atmVcCrossConnectLowVpi,
 atmVcCrossConnectRowStatus,
 atmVclEntry,
 atmVpCrossConnectEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry",
    "atmVcCrossConnectAdminStatus",
    "atmVcCrossConnectEntry",
    "atmVcCrossConnectH2LLastChange",
    "atmVcCrossConnectH2LOperStatus",
    "atmVcCrossConnectHighIfIndex",
    "atmVcCrossConnectHighVci",
    "atmVcCrossConnectHighVpi",
    "atmVcCrossConnectIndex",
    "atmVcCrossConnectL2HLastChange",
    "atmVcCrossConnectL2HOperStatus",
    "atmVcCrossConnectLowIfIndex",
    "atmVcCrossConnectLowVci",
    "atmVcCrossConnectLowVpi",
    "atmVcCrossConnectRowStatus",
    "atmVclEntry",
    "atmVpCrossConnectEntry")

(atmVclStatEntry,) = mibBuilder.importSymbols(
    "ATM2-MIB",
    "atmVclStatEntry")

(CnTopologyServiceType,) = mibBuilder.importSymbols(
    "CEM-CENTRALIZED-MANAGEMENT-MIB",
    "CnTopologyServiceType")

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4)
)
if mibBuilder.loadTexts:
    cnAtmMIB.setRevisions(
        ("2003-02-07 14:59",
         "2002-02-19 12:48",
         "2001-11-16 12:28",
         "2002-02-19 12:48")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnAtmLaunchLoopbackControlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAtmLaunchLoopbackSegment", 1),
          ("cnAtmLaunchLoopbackEndToEnd", 2))
    )



class CnAtmLaunchLoopbackStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cnAtmLoopbackUntested", 1),
          ("cnAtmLoopbackTestPassed", 2),
          ("cnAtmLoopbackTestFailed", 3),
          ("cnAtmLoopbackTestInProgress", 4),
          ("cnAtmLoopbackTestMaxSimultaneous", 5),
          ("cnAtmLoopbackTestInvalidParameters", 6))
    )



class CnAtmPvcUpstreamPolicingControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CnAtmObjects_ObjectIdentity = ObjectIdentity
cnAtmObjects = _CnAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1)
)
_CnAtmTrafficDescriptorTypes_ObjectIdentity = ObjectIdentity
cnAtmTrafficDescriptorTypes = _CnAtmTrafficDescriptorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1)
)
_CnAtmNoClpNoScrMcr_ObjectIdentity = ObjectIdentity
cnAtmNoClpNoScrMcr = _CnAtmNoClpNoScrMcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnAtmNoClpNoScrMcr.setStatus("deprecated")
_CnAtmNoClpTaggingNoScrMcr_ObjectIdentity = ObjectIdentity
cnAtmNoClpTaggingNoScrMcr = _CnAtmNoClpTaggingNoScrMcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnAtmNoClpTaggingNoScrMcr.setStatus("deprecated")
_CnAtmNoClpNoScrMdcrCdvt_ObjectIdentity = ObjectIdentity
cnAtmNoClpNoScrMdcrCdvt = _CnAtmNoClpNoScrMdcrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnAtmNoClpNoScrMdcrCdvt.setStatus("current")
_CnAtmNoClpTaggingNoScrMdcrCdvt_ObjectIdentity = ObjectIdentity
cnAtmNoClpTaggingNoScrMdcrCdvt = _CnAtmNoClpTaggingNoScrMdcrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cnAtmNoClpTaggingNoScrMdcrCdvt.setStatus("current")
_CnAtmClpNoScrMcrCdvt_ObjectIdentity = ObjectIdentity
cnAtmClpNoScrMcrCdvt = _CnAtmClpNoScrMcrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cnAtmClpNoScrMcrCdvt.setStatus("current")
_CnAtmClpTaggingNoScrMcrCdvt_ObjectIdentity = ObjectIdentity
cnAtmClpTaggingNoScrMcrCdvt = _CnAtmClpTaggingNoScrMcrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cnAtmClpTaggingNoScrMcrCdvt.setStatus("current")
_CnAtmInterfaceConfTable_Object = MibTable
cnAtmInterfaceConfTable = _CnAtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cnAtmInterfaceConfTable.setStatus("current")
_CnAtmInterfaceConfEntry_Object = MibTableRow
cnAtmInterfaceConfEntry = _CnAtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1)
)
cnAtmInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnAtmInterfaceConfEntry.setStatus("current")


class _CnAtmInterfaceMaxConfigVpiBits_Type(Integer32):
    """Custom type cnAtmInterfaceMaxConfigVpiBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CnAtmInterfaceMaxConfigVpiBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxConfigVpiBits_Object = MibTableColumn
cnAtmInterfaceMaxConfigVpiBits = _CnAtmInterfaceMaxConfigVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 1),
    _CnAtmInterfaceMaxConfigVpiBits_Type()
)
cnAtmInterfaceMaxConfigVpiBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxConfigVpiBits.setStatus("current")


class _CnAtmInterfaceMaxActualVpiBits_Type(Integer32):
    """Custom type cnAtmInterfaceMaxActualVpiBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CnAtmInterfaceMaxActualVpiBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxActualVpiBits_Object = MibTableColumn
cnAtmInterfaceMaxActualVpiBits = _CnAtmInterfaceMaxActualVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 2),
    _CnAtmInterfaceMaxActualVpiBits_Type()
)
cnAtmInterfaceMaxActualVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxActualVpiBits.setStatus("current")


class _CnAtmInterfaceMinConfigVpiBits_Type(Integer32):
    """Custom type cnAtmInterfaceMinConfigVpiBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CnAtmInterfaceMinConfigVpiBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMinConfigVpiBits_Object = MibTableColumn
cnAtmInterfaceMinConfigVpiBits = _CnAtmInterfaceMinConfigVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 3),
    _CnAtmInterfaceMinConfigVpiBits_Type()
)
cnAtmInterfaceMinConfigVpiBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMinConfigVpiBits.setStatus("current")


class _CnAtmInterfaceMinActualVpiBits_Type(Integer32):
    """Custom type cnAtmInterfaceMinActualVpiBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_CnAtmInterfaceMinActualVpiBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMinActualVpiBits_Object = MibTableColumn
cnAtmInterfaceMinActualVpiBits = _CnAtmInterfaceMinActualVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 4),
    _CnAtmInterfaceMinActualVpiBits_Type()
)
cnAtmInterfaceMinActualVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMinActualVpiBits.setStatus("current")


class _CnAtmInterfaceMaxConfigVciBits_Type(Integer32):
    """Custom type cnAtmInterfaceMaxConfigVciBits based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 16),
    )


_CnAtmInterfaceMaxConfigVciBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxConfigVciBits_Object = MibTableColumn
cnAtmInterfaceMaxConfigVciBits = _CnAtmInterfaceMaxConfigVciBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 5),
    _CnAtmInterfaceMaxConfigVciBits_Type()
)
cnAtmInterfaceMaxConfigVciBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxConfigVciBits.setStatus("current")


class _CnAtmInterfaceMaxActualVciBits_Type(Integer32):
    """Custom type cnAtmInterfaceMaxActualVciBits based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 16),
    )


_CnAtmInterfaceMaxActualVciBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxActualVciBits_Object = MibTableColumn
cnAtmInterfaceMaxActualVciBits = _CnAtmInterfaceMaxActualVciBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 6),
    _CnAtmInterfaceMaxActualVciBits_Type()
)
cnAtmInterfaceMaxActualVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxActualVciBits.setStatus("current")


class _CnAtmInterfaceMinConfigVciBits_Type(Integer32):
    """Custom type cnAtmInterfaceMinConfigVciBits based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 16),
    )


_CnAtmInterfaceMinConfigVciBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMinConfigVciBits_Object = MibTableColumn
cnAtmInterfaceMinConfigVciBits = _CnAtmInterfaceMinConfigVciBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 7),
    _CnAtmInterfaceMinConfigVciBits_Type()
)
cnAtmInterfaceMinConfigVciBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMinConfigVciBits.setStatus("current")


class _CnAtmInterfaceMinActualVciBits_Type(Integer32):
    """Custom type cnAtmInterfaceMinActualVciBits based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 16),
    )


_CnAtmInterfaceMinActualVciBits_Type.__name__ = "Integer32"
_CnAtmInterfaceMinActualVciBits_Object = MibTableColumn
cnAtmInterfaceMinActualVciBits = _CnAtmInterfaceMinActualVciBits_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 8),
    _CnAtmInterfaceMinActualVciBits_Type()
)
cnAtmInterfaceMinActualVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMinActualVciBits.setStatus("current")


class _CnAtmInterfaceMaxConfigVpc_Type(Integer32):
    """Custom type cnAtmInterfaceMaxConfigVpc based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CnAtmInterfaceMaxConfigVpc_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxConfigVpc_Object = MibTableColumn
cnAtmInterfaceMaxConfigVpc = _CnAtmInterfaceMaxConfigVpc_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 9),
    _CnAtmInterfaceMaxConfigVpc_Type()
)
cnAtmInterfaceMaxConfigVpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxConfigVpc.setStatus("current")


class _CnAtmInterfaceMaxActualVpc_Type(Integer32):
    """Custom type cnAtmInterfaceMaxActualVpc based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CnAtmInterfaceMaxActualVpc_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxActualVpc_Object = MibTableColumn
cnAtmInterfaceMaxActualVpc = _CnAtmInterfaceMaxActualVpc_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 10),
    _CnAtmInterfaceMaxActualVpc_Type()
)
cnAtmInterfaceMaxActualVpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxActualVpc.setStatus("current")


class _CnAtmInterfaceMaxConfigVcc_Type(Integer32):
    """Custom type cnAtmInterfaceMaxConfigVcc based on Integer32"""
    defaultValue = 268435456

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435456),
    )


_CnAtmInterfaceMaxConfigVcc_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxConfigVcc_Object = MibTableColumn
cnAtmInterfaceMaxConfigVcc = _CnAtmInterfaceMaxConfigVcc_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 11),
    _CnAtmInterfaceMaxConfigVcc_Type()
)
cnAtmInterfaceMaxConfigVcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxConfigVcc.setStatus("current")


class _CnAtmInterfaceMaxActualVcc_Type(Integer32):
    """Custom type cnAtmInterfaceMaxActualVcc based on Integer32"""
    defaultValue = 268435456

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435456),
    )


_CnAtmInterfaceMaxActualVcc_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxActualVcc_Object = MibTableColumn
cnAtmInterfaceMaxActualVcc = _CnAtmInterfaceMaxActualVcc_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 12),
    _CnAtmInterfaceMaxActualVcc_Type()
)
cnAtmInterfaceMaxActualVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxActualVcc.setStatus("current")


class _CnAtmInterfaceServiceCatSupported_Type(Integer32):
    """Custom type cnAtmInterfaceServiceCatSupported based on Integer32"""
    defaultValue = 19


_CnAtmInterfaceServiceCatSupported_Type.__name__ = "Integer32"
_CnAtmInterfaceServiceCatSupported_Object = MibTableColumn
cnAtmInterfaceServiceCatSupported = _CnAtmInterfaceServiceCatSupported_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 13),
    _CnAtmInterfaceServiceCatSupported_Type()
)
cnAtmInterfaceServiceCatSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceServiceCatSupported.setStatus("current")


class _CnAtmInterfaceCbrBf_Type(Integer32):
    """Custom type cnAtmInterfaceCbrBf based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmInterfaceCbrBf_Type.__name__ = "Integer32"
_CnAtmInterfaceCbrBf_Object = MibTableColumn
cnAtmInterfaceCbrBf = _CnAtmInterfaceCbrBf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 14),
    _CnAtmInterfaceCbrBf_Type()
)
cnAtmInterfaceCbrBf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceCbrBf.setStatus("current")


class _CnAtmInterfaceRtVbrBf_Type(Integer32):
    """Custom type cnAtmInterfaceRtVbrBf based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmInterfaceRtVbrBf_Type.__name__ = "Integer32"
_CnAtmInterfaceRtVbrBf_Object = MibTableColumn
cnAtmInterfaceRtVbrBf = _CnAtmInterfaceRtVbrBf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 15),
    _CnAtmInterfaceRtVbrBf_Type()
)
cnAtmInterfaceRtVbrBf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceRtVbrBf.setStatus("current")


class _CnAtmInterfaceNrtVbrBf_Type(Integer32):
    """Custom type cnAtmInterfaceNrtVbrBf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmInterfaceNrtVbrBf_Type.__name__ = "Integer32"
_CnAtmInterfaceNrtVbrBf_Object = MibTableColumn
cnAtmInterfaceNrtVbrBf = _CnAtmInterfaceNrtVbrBf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 16),
    _CnAtmInterfaceNrtVbrBf_Type()
)
cnAtmInterfaceNrtVbrBf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceNrtVbrBf.setStatus("current")


class _CnAtmInterfaceUbrBf_Type(Integer32):
    """Custom type cnAtmInterfaceUbrBf based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmInterfaceUbrBf_Type.__name__ = "Integer32"
_CnAtmInterfaceUbrBf_Object = MibTableColumn
cnAtmInterfaceUbrBf = _CnAtmInterfaceUbrBf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 17),
    _CnAtmInterfaceUbrBf_Type()
)
cnAtmInterfaceUbrBf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceUbrBf.setStatus("current")


class _CnAtmInterfaceUbrPlusBf_Type(Integer32):
    """Custom type cnAtmInterfaceUbrPlusBf based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmInterfaceUbrPlusBf_Type.__name__ = "Integer32"
_CnAtmInterfaceUbrPlusBf_Object = MibTableColumn
cnAtmInterfaceUbrPlusBf = _CnAtmInterfaceUbrPlusBf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 18),
    _CnAtmInterfaceUbrPlusBf_Type()
)
cnAtmInterfaceUbrPlusBf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceUbrPlusBf.setStatus("deprecated")


class _CnAtmInterfaceMaxConfigRxBandwidth_Type(Integer32):
    """Custom type cnAtmInterfaceMaxConfigRxBandwidth based on Integer32"""
    defaultValue = 2147483647


_CnAtmInterfaceMaxConfigRxBandwidth_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxConfigRxBandwidth_Object = MibTableColumn
cnAtmInterfaceMaxConfigRxBandwidth = _CnAtmInterfaceMaxConfigRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 19),
    _CnAtmInterfaceMaxConfigRxBandwidth_Type()
)
cnAtmInterfaceMaxConfigRxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxConfigRxBandwidth.setStatus("current")


class _CnAtmInterfaceGfrBf_Type(Integer32):
    """Custom type cnAtmInterfaceGfrBf based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmInterfaceGfrBf_Type.__name__ = "Integer32"
_CnAtmInterfaceGfrBf_Object = MibTableColumn
cnAtmInterfaceGfrBf = _CnAtmInterfaceGfrBf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 20),
    _CnAtmInterfaceGfrBf_Type()
)
cnAtmInterfaceGfrBf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceGfrBf.setStatus("current")


class _CnAtmInterfaceMaxConfigTxBandwidth_Type(Integer32):
    """Custom type cnAtmInterfaceMaxConfigTxBandwidth based on Integer32"""
    defaultValue = 2147483647


_CnAtmInterfaceMaxConfigTxBandwidth_Type.__name__ = "Integer32"
_CnAtmInterfaceMaxConfigTxBandwidth_Object = MibTableColumn
cnAtmInterfaceMaxConfigTxBandwidth = _CnAtmInterfaceMaxConfigTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 21),
    _CnAtmInterfaceMaxConfigTxBandwidth_Type()
)
cnAtmInterfaceMaxConfigTxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxConfigTxBandwidth.setStatus("current")
_CnAtmInterfaceMaxActualRxBandwidth_Type = Unsigned32
_CnAtmInterfaceMaxActualRxBandwidth_Object = MibTableColumn
cnAtmInterfaceMaxActualRxBandwidth = _CnAtmInterfaceMaxActualRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 22),
    _CnAtmInterfaceMaxActualRxBandwidth_Type()
)
cnAtmInterfaceMaxActualRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxActualRxBandwidth.setStatus("current")


class _CnAtmInterfaceMaxActualTxBandwidth_Type(Unsigned32):
    """Custom type cnAtmInterfaceMaxActualTxBandwidth based on Unsigned32"""
    defaultValue = 2147483647


_CnAtmInterfaceMaxActualTxBandwidth_Type.__name__ = "Unsigned32"
_CnAtmInterfaceMaxActualTxBandwidth_Object = MibTableColumn
cnAtmInterfaceMaxActualTxBandwidth = _CnAtmInterfaceMaxActualTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 23),
    _CnAtmInterfaceMaxActualTxBandwidth_Type()
)
cnAtmInterfaceMaxActualTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceMaxActualTxBandwidth.setStatus("current")
_CnAtmInterfaceAvailableRxBandwidth_Type = Integer32
_CnAtmInterfaceAvailableRxBandwidth_Object = MibTableColumn
cnAtmInterfaceAvailableRxBandwidth = _CnAtmInterfaceAvailableRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 24),
    _CnAtmInterfaceAvailableRxBandwidth_Type()
)
cnAtmInterfaceAvailableRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceAvailableRxBandwidth.setStatus("current")
_CnAtmInterfaceAvailableTxBandwidth_Type = Integer32
_CnAtmInterfaceAvailableTxBandwidth_Object = MibTableColumn
cnAtmInterfaceAvailableTxBandwidth = _CnAtmInterfaceAvailableTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 25),
    _CnAtmInterfaceAvailableTxBandwidth_Type()
)
cnAtmInterfaceAvailableTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmInterfaceAvailableTxBandwidth.setStatus("current")


class _CnAtmInterfaceCellScrambling_Type(Integer32):
    """Custom type cnAtmInterfaceCellScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CnAtmInterfaceCellScrambling_Type.__name__ = "Integer32"
_CnAtmInterfaceCellScrambling_Object = MibTableColumn
cnAtmInterfaceCellScrambling = _CnAtmInterfaceCellScrambling_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 26),
    _CnAtmInterfaceCellScrambling_Type()
)
cnAtmInterfaceCellScrambling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceCellScrambling.setStatus("current")


class _CnAtmInterfaceIntervalStats_Type(Integer32):
    """Custom type cnAtmInterfaceIntervalStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CnAtmInterfaceIntervalStats_Type.__name__ = "Integer32"
_CnAtmInterfaceIntervalStats_Object = MibTableColumn
cnAtmInterfaceIntervalStats = _CnAtmInterfaceIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 27),
    _CnAtmInterfaceIntervalStats_Type()
)
cnAtmInterfaceIntervalStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceIntervalStats.setStatus("current")
_CnAtmInterfaceRowStatus_Type = RowStatus
_CnAtmInterfaceRowStatus_Object = MibTableColumn
cnAtmInterfaceRowStatus = _CnAtmInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 28),
    _CnAtmInterfaceRowStatus_Type()
)
cnAtmInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfaceRowStatus.setStatus("current")
_CnAtmInterfacePvcUpstreamPolicing_Type = CnAtmPvcUpstreamPolicingControl
_CnAtmInterfacePvcUpstreamPolicing_Object = MibTableColumn
cnAtmInterfacePvcUpstreamPolicing = _CnAtmInterfacePvcUpstreamPolicing_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 2, 1, 29),
    _CnAtmInterfacePvcUpstreamPolicing_Type()
)
cnAtmInterfacePvcUpstreamPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmInterfacePvcUpstreamPolicing.setStatus("current")
_CnAtmNode_ObjectIdentity = ObjectIdentity
cnAtmNode = _CnAtmNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3)
)


class _CnAtmNodeQos1Clr0_Type(Integer32):
    """Custom type cnAtmNodeQos1Clr0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos1Clr0_Type.__name__ = "Integer32"
_CnAtmNodeQos1Clr0_Object = MibScalar
cnAtmNodeQos1Clr0 = _CnAtmNodeQos1Clr0_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 1),
    _CnAtmNodeQos1Clr0_Type()
)
cnAtmNodeQos1Clr0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos1Clr0.setStatus("current")


class _CnAtmNodeQos2Clr0_Type(Integer32):
    """Custom type cnAtmNodeQos2Clr0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos2Clr0_Type.__name__ = "Integer32"
_CnAtmNodeQos2Clr0_Object = MibScalar
cnAtmNodeQos2Clr0 = _CnAtmNodeQos2Clr0_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 2),
    _CnAtmNodeQos2Clr0_Type()
)
cnAtmNodeQos2Clr0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos2Clr0.setStatus("current")


class _CnAtmNodeQos3Clr0_Type(Integer32):
    """Custom type cnAtmNodeQos3Clr0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos3Clr0_Type.__name__ = "Integer32"
_CnAtmNodeQos3Clr0_Object = MibScalar
cnAtmNodeQos3Clr0 = _CnAtmNodeQos3Clr0_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 3),
    _CnAtmNodeQos3Clr0_Type()
)
cnAtmNodeQos3Clr0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos3Clr0.setStatus("deprecated")


class _CnAtmNodeQos4Clr0_Type(Integer32):
    """Custom type cnAtmNodeQos4Clr0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos4Clr0_Type.__name__ = "Integer32"
_CnAtmNodeQos4Clr0_Object = MibScalar
cnAtmNodeQos4Clr0 = _CnAtmNodeQos4Clr0_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 4),
    _CnAtmNodeQos4Clr0_Type()
)
cnAtmNodeQos4Clr0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos4Clr0.setStatus("deprecated")


class _CnAtmNodeQos1Clr1_Type(Integer32):
    """Custom type cnAtmNodeQos1Clr1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos1Clr1_Type.__name__ = "Integer32"
_CnAtmNodeQos1Clr1_Object = MibScalar
cnAtmNodeQos1Clr1 = _CnAtmNodeQos1Clr1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 5),
    _CnAtmNodeQos1Clr1_Type()
)
cnAtmNodeQos1Clr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos1Clr1.setStatus("current")


class _CnAtmNodeQos2Clr1_Type(Integer32):
    """Custom type cnAtmNodeQos2Clr1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos2Clr1_Type.__name__ = "Integer32"
_CnAtmNodeQos2Clr1_Object = MibScalar
cnAtmNodeQos2Clr1 = _CnAtmNodeQos2Clr1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 6),
    _CnAtmNodeQos2Clr1_Type()
)
cnAtmNodeQos2Clr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos2Clr1.setStatus("current")


class _CnAtmNodeQos3Clr1_Type(Integer32):
    """Custom type cnAtmNodeQos3Clr1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos3Clr1_Type.__name__ = "Integer32"
_CnAtmNodeQos3Clr1_Object = MibScalar
cnAtmNodeQos3Clr1 = _CnAtmNodeQos3Clr1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 7),
    _CnAtmNodeQos3Clr1_Type()
)
cnAtmNodeQos3Clr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos3Clr1.setStatus("current")


class _CnAtmNodeQos4Clr1_Type(Integer32):
    """Custom type cnAtmNodeQos4Clr1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmNodeQos4Clr1_Type.__name__ = "Integer32"
_CnAtmNodeQos4Clr1_Object = MibScalar
cnAtmNodeQos4Clr1 = _CnAtmNodeQos4Clr1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 8),
    _CnAtmNodeQos4Clr1_Type()
)
cnAtmNodeQos4Clr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos4Clr1.setStatus("current")


class _CnAtmNodeQos1Cdv_Type(Integer32):
    """Custom type cnAtmNodeQos1Cdv based on Integer32"""
    defaultValue = 750


_CnAtmNodeQos1Cdv_Type.__name__ = "Integer32"
_CnAtmNodeQos1Cdv_Object = MibScalar
cnAtmNodeQos1Cdv = _CnAtmNodeQos1Cdv_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 9),
    _CnAtmNodeQos1Cdv_Type()
)
cnAtmNodeQos1Cdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos1Cdv.setStatus("current")


class _CnAtmNodeQos2Cdv_Type(Integer32):
    """Custom type cnAtmNodeQos2Cdv based on Integer32"""
    defaultValue = 750


_CnAtmNodeQos2Cdv_Type.__name__ = "Integer32"
_CnAtmNodeQos2Cdv_Object = MibScalar
cnAtmNodeQos2Cdv = _CnAtmNodeQos2Cdv_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 10),
    _CnAtmNodeQos2Cdv_Type()
)
cnAtmNodeQos2Cdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos2Cdv.setStatus("current")


class _CnAtmNodeQos3Cdv_Type(Integer32):
    """Custom type cnAtmNodeQos3Cdv based on Integer32"""
    defaultValue = 750


_CnAtmNodeQos3Cdv_Type.__name__ = "Integer32"
_CnAtmNodeQos3Cdv_Object = MibScalar
cnAtmNodeQos3Cdv = _CnAtmNodeQos3Cdv_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 11),
    _CnAtmNodeQos3Cdv_Type()
)
cnAtmNodeQos3Cdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos3Cdv.setStatus("current")


class _CnAtmNodeQos4Cdv_Type(Integer32):
    """Custom type cnAtmNodeQos4Cdv based on Integer32"""
    defaultValue = 750


_CnAtmNodeQos4Cdv_Type.__name__ = "Integer32"
_CnAtmNodeQos4Cdv_Object = MibScalar
cnAtmNodeQos4Cdv = _CnAtmNodeQos4Cdv_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 12),
    _CnAtmNodeQos4Cdv_Type()
)
cnAtmNodeQos4Cdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos4Cdv.setStatus("current")


class _CnAtmNodeQos1MaxCtd_Type(Integer32):
    """Custom type cnAtmNodeQos1MaxCtd based on Integer32"""
    defaultValue = 10


_CnAtmNodeQos1MaxCtd_Type.__name__ = "Integer32"
_CnAtmNodeQos1MaxCtd_Object = MibScalar
cnAtmNodeQos1MaxCtd = _CnAtmNodeQos1MaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 13),
    _CnAtmNodeQos1MaxCtd_Type()
)
cnAtmNodeQos1MaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos1MaxCtd.setStatus("current")


class _CnAtmNodeQos2MaxCtd_Type(Integer32):
    """Custom type cnAtmNodeQos2MaxCtd based on Integer32"""
    defaultValue = 10


_CnAtmNodeQos2MaxCtd_Type.__name__ = "Integer32"
_CnAtmNodeQos2MaxCtd_Object = MibScalar
cnAtmNodeQos2MaxCtd = _CnAtmNodeQos2MaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 3, 14),
    _CnAtmNodeQos2MaxCtd_Type()
)
cnAtmNodeQos2MaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmNodeQos2MaxCtd.setStatus("current")


class _CnDefaultAtmTrafficDescrParamIndex_Type(Integer32):
    """Custom type cnDefaultAtmTrafficDescrParamIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnDefaultAtmTrafficDescrParamIndex_Type.__name__ = "Integer32"
_CnDefaultAtmTrafficDescrParamIndex_Object = MibScalar
cnDefaultAtmTrafficDescrParamIndex = _CnDefaultAtmTrafficDescrParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 4),
    _CnDefaultAtmTrafficDescrParamIndex_Type()
)
cnDefaultAtmTrafficDescrParamIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDefaultAtmTrafficDescrParamIndex.setStatus("current")
_CnAtmEndPointTable_Object = MibTable
cnAtmEndPointTable = _CnAtmEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7)
)
if mibBuilder.loadTexts:
    cnAtmEndPointTable.setStatus("current")
_CnAtmEndPointEntry_Object = MibTableRow
cnAtmEndPointEntry = _CnAtmEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cnAtmEndPointEntry.setStatus("current")


class _CnAtmF5EPType_Type(Integer32):
    """Custom type cnAtmF5EPType based on Integer32"""
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
        *(("cnAtmF5None", 0),
          ("cnAtmF5EndToEnd", 1),
          ("cnAtmF5Segment", 2))
    )


_CnAtmF5EPType_Type.__name__ = "Integer32"
_CnAtmF5EPType_Object = MibTableColumn
cnAtmF5EPType = _CnAtmF5EPType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1, 1),
    _CnAtmF5EPType_Type()
)
cnAtmF5EPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmF5EPType.setStatus("current")


class _CnAtmF5EPConnectionState_Type(Integer32):
    """Custom type cnAtmF5EPConnectionState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAtmF5Ok", 1),
          ("cnAtmF5Ais", 2))
    )


_CnAtmF5EPConnectionState_Type.__name__ = "Integer32"
_CnAtmF5EPConnectionState_Object = MibTableColumn
cnAtmF5EPConnectionState = _CnAtmF5EPConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1, 2),
    _CnAtmF5EPConnectionState_Type()
)
cnAtmF5EPConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmF5EPConnectionState.setStatus("current")


class _CnAtmF5EPContinuityCheck_Type(Integer32):
    """Custom type cnAtmF5EPContinuityCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAtmF5CCDisabled", 1),
          ("cnAtmF5CCEnabled", 2))
    )


_CnAtmF5EPContinuityCheck_Type.__name__ = "Integer32"
_CnAtmF5EPContinuityCheck_Object = MibTableColumn
cnAtmF5EPContinuityCheck = _CnAtmF5EPContinuityCheck_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1, 3),
    _CnAtmF5EPContinuityCheck_Type()
)
cnAtmF5EPContinuityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmF5EPContinuityCheck.setStatus("current")


class _CnAtmF5EPLaunchLoopback_Type(Integer32):
    """Custom type cnAtmF5EPLaunchLoopback based on Integer32"""
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
        *(("cnAtmF5NoLoopback", 0),
          ("cnAtmF5LaunchLoopbackEndToEnd", 1),
          ("cnAtmF5LaunchLoopbackSegment", 2))
    )


_CnAtmF5EPLaunchLoopback_Type.__name__ = "Integer32"
_CnAtmF5EPLaunchLoopback_Object = MibTableColumn
cnAtmF5EPLaunchLoopback = _CnAtmF5EPLaunchLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1, 4),
    _CnAtmF5EPLaunchLoopback_Type()
)
cnAtmF5EPLaunchLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmF5EPLaunchLoopback.setStatus("current")


class _CnAtmF5EPTraps_Type(Integer32):
    """Custom type cnAtmF5EPTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAtmF5TrapsDisabled", 1),
          ("cnAtmF5TrapsEnabled", 2))
    )


_CnAtmF5EPTraps_Type.__name__ = "Integer32"
_CnAtmF5EPTraps_Object = MibTableColumn
cnAtmF5EPTraps = _CnAtmF5EPTraps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1, 5),
    _CnAtmF5EPTraps_Type()
)
cnAtmF5EPTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAtmF5EPTraps.setStatus("current")


class _CnAtmEPType_Type(Integer32):
    """Custom type cnAtmEPType based on Integer32"""
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
        *(("cnAtmEPTypeUnknown", 1),
          ("cnAtmEPTypeATM", 2),
          ("cnAtmEPTypeVoice", 3),
          ("cnAtmEPTypeManagement", 4))
    )


_CnAtmEPType_Type.__name__ = "Integer32"
_CnAtmEPType_Object = MibTableColumn
cnAtmEPType = _CnAtmEPType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 7, 1, 6),
    _CnAtmEPType_Type()
)
cnAtmEPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmEPType.setStatus("current")
_CnAtmSysStats_ObjectIdentity = ObjectIdentity
cnAtmSysStats = _CnAtmSysStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 8)
)
_CnAtmUpstreamCgtnDcrdClp0_Type = Counter32
_CnAtmUpstreamCgtnDcrdClp0_Object = MibScalar
cnAtmUpstreamCgtnDcrdClp0 = _CnAtmUpstreamCgtnDcrdClp0_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 8, 1),
    _CnAtmUpstreamCgtnDcrdClp0_Type()
)
cnAtmUpstreamCgtnDcrdClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmUpstreamCgtnDcrdClp0.setStatus("current")
_CnAtmUpstreamCgtnDcrdClp1_Type = Counter32
_CnAtmUpstreamCgtnDcrdClp1_Object = MibScalar
cnAtmUpstreamCgtnDcrdClp1 = _CnAtmUpstreamCgtnDcrdClp1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 8, 2),
    _CnAtmUpstreamCgtnDcrdClp1_Type()
)
cnAtmUpstreamCgtnDcrdClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmUpstreamCgtnDcrdClp1.setStatus("current")
_CnAtmDownstreamCgtnDcrdClp0_Type = Counter32
_CnAtmDownstreamCgtnDcrdClp0_Object = MibScalar
cnAtmDownstreamCgtnDcrdClp0 = _CnAtmDownstreamCgtnDcrdClp0_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 8, 3),
    _CnAtmDownstreamCgtnDcrdClp0_Type()
)
cnAtmDownstreamCgtnDcrdClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmDownstreamCgtnDcrdClp0.setStatus("current")
_CnAtmDownstreamCgtnDcrdClp1_Type = Counter32
_CnAtmDownstreamCgtnDcrdClp1_Object = MibScalar
cnAtmDownstreamCgtnDcrdClp1 = _CnAtmDownstreamCgtnDcrdClp1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 8, 4),
    _CnAtmDownstreamCgtnDcrdClp1_Type()
)
cnAtmDownstreamCgtnDcrdClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmDownstreamCgtnDcrdClp1.setStatus("current")
_CnAtmInterfaceStatsTable_Object = MibTable
cnAtmInterfaceStatsTable = _CnAtmInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9)
)
if mibBuilder.loadTexts:
    cnAtmInterfaceStatsTable.setStatus("current")
_CnAtmInterfaceStatsEntry_Object = MibTableRow
cnAtmInterfaceStatsEntry = _CnAtmInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1)
)
cnAtmInterfaceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnAtmInterfaceStatsEntry.setStatus("current")
_CnAtmIntfInCells_Type = Counter32
_CnAtmIntfInCells_Object = MibTableColumn
cnAtmIntfInCells = _CnAtmIntfInCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 1),
    _CnAtmIntfInCells_Type()
)
cnAtmIntfInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfInCells.setStatus("current")
_CnAtmIntfOutCells_Type = Counter32
_CnAtmIntfOutCells_Object = MibTableColumn
cnAtmIntfOutCells = _CnAtmIntfOutCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 2),
    _CnAtmIntfOutCells_Type()
)
cnAtmIntfOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfOutCells.setStatus("current")
_CnAtmIntfInErrors_Type = Counter32
_CnAtmIntfInErrors_Object = MibTableColumn
cnAtmIntfInErrors = _CnAtmIntfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 3),
    _CnAtmIntfInErrors_Type()
)
cnAtmIntfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfInErrors.setStatus("current")
_CnAtmIntfInUnknownProtos_Type = Counter32
_CnAtmIntfInUnknownProtos_Object = MibTableColumn
cnAtmIntfInUnknownProtos = _CnAtmIntfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 4),
    _CnAtmIntfInUnknownProtos_Type()
)
cnAtmIntfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfInUnknownProtos.setStatus("current")
_CnAtmIntfInDiscards_Type = Counter32
_CnAtmIntfInDiscards_Object = MibTableColumn
cnAtmIntfInDiscards = _CnAtmIntfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 5),
    _CnAtmIntfInDiscards_Type()
)
cnAtmIntfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfInDiscards.setStatus("current")
_CnAtmIntfOutDiscards_Type = Counter32
_CnAtmIntfOutDiscards_Object = MibTableColumn
cnAtmIntfOutDiscards = _CnAtmIntfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 6),
    _CnAtmIntfOutDiscards_Type()
)
cnAtmIntfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfOutDiscards.setStatus("current")
_CnAtmIntfLastUnknownVpi_Type = Integer32
_CnAtmIntfLastUnknownVpi_Object = MibTableColumn
cnAtmIntfLastUnknownVpi = _CnAtmIntfLastUnknownVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 7),
    _CnAtmIntfLastUnknownVpi_Type()
)
cnAtmIntfLastUnknownVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfLastUnknownVpi.setStatus("current")
_CnAtmIntfLastUnknownVci_Type = Integer32
_CnAtmIntfLastUnknownVci_Object = MibTableColumn
cnAtmIntfLastUnknownVci = _CnAtmIntfLastUnknownVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 9, 1, 8),
    _CnAtmIntfLastUnknownVci_Type()
)
cnAtmIntfLastUnknownVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfLastUnknownVci.setStatus("current")
_CnAtmVclStatTable_Object = MibTable
cnAtmVclStatTable = _CnAtmVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 10)
)
if mibBuilder.loadTexts:
    cnAtmVclStatTable.setStatus("current")
_CnAtmVclStatEntry_Object = MibTableRow
cnAtmVclStatEntry = _CnAtmVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cnAtmVclStatEntry.setStatus("current")
_CnAtmVclTotalCongDiscards_Type = Counter32
_CnAtmVclTotalCongDiscards_Object = MibTableColumn
cnAtmVclTotalCongDiscards = _CnAtmVclTotalCongDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 10, 1, 1),
    _CnAtmVclTotalCongDiscards_Type()
)
cnAtmVclTotalCongDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmVclTotalCongDiscards.setStatus("current")
_CnAtmVclClp0CongDiscards_Type = Counter32
_CnAtmVclClp0CongDiscards_Object = MibTableColumn
cnAtmVclClp0CongDiscards = _CnAtmVclClp0CongDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 10, 1, 2),
    _CnAtmVclClp0CongDiscards_Type()
)
cnAtmVclClp0CongDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmVclClp0CongDiscards.setStatus("current")
_CnAtmInterfaceIntervalStatsTable_Object = MibTable
cnAtmInterfaceIntervalStatsTable = _CnAtmInterfaceIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11)
)
if mibBuilder.loadTexts:
    cnAtmInterfaceIntervalStatsTable.setStatus("current")
_CnAtmInterfaceIntervalStatsEntry_Object = MibTableRow
cnAtmInterfaceIntervalStatsEntry = _CnAtmInterfaceIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1)
)
cnAtmInterfaceIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CEM-ATM", "cnAtmIntfIntervalNumber"),
)
if mibBuilder.loadTexts:
    cnAtmInterfaceIntervalStatsEntry.setStatus("current")


class _CnAtmIntfIntervalNumber_Type(Integer32):
    """Custom type cnAtmIntfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CnAtmIntfIntervalNumber_Type.__name__ = "Integer32"
_CnAtmIntfIntervalNumber_Object = MibTableColumn
cnAtmIntfIntervalNumber = _CnAtmIntfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 1),
    _CnAtmIntfIntervalNumber_Type()
)
cnAtmIntfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalNumber.setStatus("current")
_CnAtmIntfIntervalInCells_Type = Counter32
_CnAtmIntfIntervalInCells_Object = MibTableColumn
cnAtmIntfIntervalInCells = _CnAtmIntfIntervalInCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 2),
    _CnAtmIntfIntervalInCells_Type()
)
cnAtmIntfIntervalInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalInCells.setStatus("current")
_CnAtmIntfIntervalOutCells_Type = Counter32
_CnAtmIntfIntervalOutCells_Object = MibTableColumn
cnAtmIntfIntervalOutCells = _CnAtmIntfIntervalOutCells_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 3),
    _CnAtmIntfIntervalOutCells_Type()
)
cnAtmIntfIntervalOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalOutCells.setStatus("current")
_CnAtmIntfIntervalInErrors_Type = Counter32
_CnAtmIntfIntervalInErrors_Object = MibTableColumn
cnAtmIntfIntervalInErrors = _CnAtmIntfIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 4),
    _CnAtmIntfIntervalInErrors_Type()
)
cnAtmIntfIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalInErrors.setStatus("current")
_CnAtmIntfIntervalInUnknownProtos_Type = Counter32
_CnAtmIntfIntervalInUnknownProtos_Object = MibTableColumn
cnAtmIntfIntervalInUnknownProtos = _CnAtmIntfIntervalInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 5),
    _CnAtmIntfIntervalInUnknownProtos_Type()
)
cnAtmIntfIntervalInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalInUnknownProtos.setStatus("current")
_CnAtmIntfIntervalInDiscards_Type = Counter32
_CnAtmIntfIntervalInDiscards_Object = MibTableColumn
cnAtmIntfIntervalInDiscards = _CnAtmIntfIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 6),
    _CnAtmIntfIntervalInDiscards_Type()
)
cnAtmIntfIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalInDiscards.setStatus("current")
_CnAtmIntfIntervalOutDiscards_Type = Counter32
_CnAtmIntfIntervalOutDiscards_Object = MibTableColumn
cnAtmIntfIntervalOutDiscards = _CnAtmIntfIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 7),
    _CnAtmIntfIntervalOutDiscards_Type()
)
cnAtmIntfIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalOutDiscards.setStatus("current")
_CnAtmIntfIntervalValidData_Type = TruthValue
_CnAtmIntfIntervalValidData_Object = MibTableColumn
cnAtmIntfIntervalValidData = _CnAtmIntfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 11, 1, 8),
    _CnAtmIntfIntervalValidData_Type()
)
cnAtmIntfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmIntfIntervalValidData.setStatus("current")
_CnAtmVcCrossConnectTable_Object = MibTable
cnAtmVcCrossConnectTable = _CnAtmVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 12)
)
if mibBuilder.loadTexts:
    cnAtmVcCrossConnectTable.setStatus("current")
_CnAtmVcCrossConnectEntry_Object = MibTableRow
cnAtmVcCrossConnectEntry = _CnAtmVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cnAtmVcCrossConnectEntry.setStatus("current")
_CnAtmPvcUpstreamPolicing_Type = CnAtmPvcUpstreamPolicingControl
_CnAtmPvcUpstreamPolicing_Object = MibTableColumn
cnAtmPvcUpstreamPolicing = _CnAtmPvcUpstreamPolicing_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 12, 1, 1),
    _CnAtmPvcUpstreamPolicing_Type()
)
cnAtmPvcUpstreamPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmPvcUpstreamPolicing.setStatus("current")


class _CnAtmDSPvcTag_Type(OctetString):
    """Custom type cnAtmDSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAtmDSPvcTag_Type.__name__ = "OctetString"
_CnAtmDSPvcTag_Object = MibTableColumn
cnAtmDSPvcTag = _CnAtmDSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 12, 1, 2),
    _CnAtmDSPvcTag_Type()
)
cnAtmDSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmDSPvcTag.setStatus("current")


class _CnAtmUSPvcTag_Type(OctetString):
    """Custom type cnAtmUSPvcTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAtmUSPvcTag_Type.__name__ = "OctetString"
_CnAtmUSPvcTag_Object = MibTableColumn
cnAtmUSPvcTag = _CnAtmUSPvcTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 12, 1, 3),
    _CnAtmUSPvcTag_Type()
)
cnAtmUSPvcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmUSPvcTag.setStatus("current")


class _CnAtmPvcServiceType_Type(CnTopologyServiceType):
    """Custom type cnAtmPvcServiceType based on CnTopologyServiceType"""
    defaultValue = 1


_CnAtmPvcServiceType_Type.__name__ = "CnTopologyServiceType"
_CnAtmPvcServiceType_Object = MibTableColumn
cnAtmPvcServiceType = _CnAtmPvcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 12, 1, 4),
    _CnAtmPvcServiceType_Type()
)
cnAtmPvcServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmPvcServiceType.setStatus("current")
_CnAtmTDScopeTable_Object = MibTable
cnAtmTDScopeTable = _CnAtmTDScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 13)
)
if mibBuilder.loadTexts:
    cnAtmTDScopeTable.setStatus("current")
_CnAtmTDScopeEntry_Object = MibTableRow
cnAtmTDScopeEntry = _CnAtmTDScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cnAtmTDScopeEntry.setStatus("current")


class _CnAtmTDScope_Type(Integer32):
    """Custom type cnAtmTDScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("global", 2),
          ("internal", 3))
    )


_CnAtmTDScope_Type.__name__ = "Integer32"
_CnAtmTDScope_Object = MibTableColumn
cnAtmTDScope = _CnAtmTDScope_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 13, 1, 1),
    _CnAtmTDScope_Type()
)
cnAtmTDScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmTDScope.setStatus("current")


class _CnAtmTrafficDescrGlobalParamIndexNext_Type(Integer32):
    """Custom type cnAtmTrafficDescrGlobalParamIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnAtmTrafficDescrGlobalParamIndexNext_Type.__name__ = "Integer32"
_CnAtmTrafficDescrGlobalParamIndexNext_Object = MibScalar
cnAtmTrafficDescrGlobalParamIndexNext = _CnAtmTrafficDescrGlobalParamIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 14),
    _CnAtmTrafficDescrGlobalParamIndexNext_Type()
)
cnAtmTrafficDescrGlobalParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmTrafficDescrGlobalParamIndexNext.setStatus("current")
_CnAtmTDDistListTable_Object = MibTable
cnAtmTDDistListTable = _CnAtmTDDistListTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 15)
)
if mibBuilder.loadTexts:
    cnAtmTDDistListTable.setStatus("current")
_CnAtmTDDistListEntry_Object = MibTableRow
cnAtmTDDistListEntry = _CnAtmTDDistListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cnAtmTDDistListEntry.setStatus("current")


class _CnAtmTDDistListIndex_Type(Integer32):
    """Custom type cnAtmTDDistListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAtmTDDistListIndex_Type.__name__ = "Integer32"
_CnAtmTDDistListIndex_Object = MibTableColumn
cnAtmTDDistListIndex = _CnAtmTDDistListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 15, 1, 1),
    _CnAtmTDDistListIndex_Type()
)
cnAtmTDDistListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmTDDistListIndex.setStatus("current")
_CnAtmVpCrossConnectTable_Object = MibTable
cnAtmVpCrossConnectTable = _CnAtmVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 16)
)
if mibBuilder.loadTexts:
    cnAtmVpCrossConnectTable.setStatus("current")
_CnAtmVpCrossConnectEntry_Object = MibTableRow
cnAtmVpCrossConnectEntry = _CnAtmVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cnAtmVpCrossConnectEntry.setStatus("current")


class _CnAtmPvpServiceType_Type(CnTopologyServiceType):
    """Custom type cnAtmPvpServiceType based on CnTopologyServiceType"""
    defaultValue = 1


_CnAtmPvpServiceType_Type.__name__ = "CnTopologyServiceType"
_CnAtmPvpServiceType_Object = MibTableColumn
cnAtmPvpServiceType = _CnAtmPvpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 16, 1, 1),
    _CnAtmPvpServiceType_Type()
)
cnAtmPvpServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAtmPvpServiceType.setStatus("current")


class _CnAtmDSPvpTag_Type(OctetString):
    """Custom type cnAtmDSPvpTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAtmDSPvpTag_Type.__name__ = "OctetString"
_CnAtmDSPvpTag_Object = MibTableColumn
cnAtmDSPvpTag = _CnAtmDSPvpTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 16, 1, 2),
    _CnAtmDSPvpTag_Type()
)
cnAtmDSPvpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmDSPvpTag.setStatus("current")


class _CnAtmUSPvpTag_Type(OctetString):
    """Custom type cnAtmUSPvpTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAtmUSPvpTag_Type.__name__ = "OctetString"
_CnAtmUSPvpTag_Object = MibTableColumn
cnAtmUSPvpTag = _CnAtmUSPvpTag_Object(
    (1, 3, 6, 1, 4, 1, 6352, 4, 1, 16, 1, 3),
    _CnAtmUSPvpTag_Type()
)
cnAtmUSPvpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAtmUSPvpTag.setStatus("current")
_CnAtmNotifications_ObjectIdentity = ObjectIdentity
cnAtmNotifications = _CnAtmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 2)
)
_CnAtmModuleConformance_ObjectIdentity = ObjectIdentity
cnAtmModuleConformance = _CnAtmModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3)
)
_CnAtmGroups_ObjectIdentity = ObjectIdentity
cnAtmGroups = _CnAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3, 1)
)
atmVclEntry.registerAugmentions(
    ("CEM-ATM",
     "cnAtmEndPointEntry")
)
cnAtmEndPointEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVclStatEntry.registerAugmentions(
    ("CEM-ATM",
     "cnAtmVclStatEntry")
)
cnAtmVclStatEntry.setIndexNames(*atmVclStatEntry.getIndexNames())
atmVcCrossConnectEntry.registerAugmentions(
    ("CEM-ATM",
     "cnAtmVcCrossConnectEntry")
)
cnAtmVcCrossConnectEntry.setIndexNames(*atmVcCrossConnectEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions(
    ("CEM-ATM",
     "cnAtmTDScopeEntry")
)
cnAtmTDScopeEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions(
    ("CEM-ATM",
     "cnAtmTDDistListEntry")
)
cnAtmTDDistListEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
atmVpCrossConnectEntry.registerAugmentions(
    ("CEM-ATM",
     "cnAtmVpCrossConnectEntry")
)
cnAtmVpCrossConnectEntry.setIndexNames(*atmVpCrossConnectEntry.getIndexNames())

# Managed Objects groups

cnx510ATMObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3, 1, 1)
)
cnx510ATMObjectGroup.setObjects(
      *(("CEM-ATM", "cnAtmInterfaceMaxConfigVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMinConfigVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMinActualVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMinConfigVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMinActualVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVpc"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVpc"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVcc"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVcc"),
        ("CEM-ATM", "cnAtmInterfaceServiceCatSupported"),
        ("CEM-ATM", "cnAtmInterfaceCbrBf"),
        ("CEM-ATM", "cnAtmInterfaceRtVbrBf"),
        ("CEM-ATM", "cnAtmInterfaceNrtVbrBf"),
        ("CEM-ATM", "cnAtmInterfaceUbrBf"),
        ("CEM-ATM", "cnAtmInterfaceUbrPlusBf"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualRxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceAvailableTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceCellScrambling"),
        ("CEM-ATM", "cnAtmInterfaceRowStatus"),
        ("CEM-ATM", "cnAtmNodeQos1Clr0"),
        ("CEM-ATM", "cnAtmNodeQos2Clr0"),
        ("CEM-ATM", "cnAtmNodeQos3Clr0"),
        ("CEM-ATM", "cnAtmNodeQos4Clr0"),
        ("CEM-ATM", "cnAtmNodeQos1Clr1"),
        ("CEM-ATM", "cnAtmNodeQos2Clr1"),
        ("CEM-ATM", "cnAtmNodeQos3Clr1"),
        ("CEM-ATM", "cnAtmNodeQos4Clr1"),
        ("CEM-ATM", "cnAtmNodeQos1Cdv"),
        ("CEM-ATM", "cnAtmNodeQos2Cdv"),
        ("CEM-ATM", "cnAtmNodeQos3Cdv"),
        ("CEM-ATM", "cnAtmNodeQos4Cdv"),
        ("CEM-ATM", "cnAtmNodeQos1MaxCtd"),
        ("CEM-ATM", "cnAtmNodeQos2MaxCtd"),
        ("CEM-ATM", "cnDefaultAtmTrafficDescrParamIndex"))
)
if mibBuilder.loadTexts:
    cnx510ATMObjectGroup.setStatus("deprecated")

cnx511ATMObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3, 1, 2)
)
cnx511ATMObjectGroup.setObjects(
      *(("CEM-ATM", "cnAtmInterfaceMaxConfigVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMinConfigVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMinActualVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMinConfigVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMinActualVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVpc"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVpc"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVcc"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVcc"),
        ("CEM-ATM", "cnAtmInterfaceServiceCatSupported"),
        ("CEM-ATM", "cnAtmInterfaceCbrBf"),
        ("CEM-ATM", "cnAtmInterfaceRtVbrBf"),
        ("CEM-ATM", "cnAtmInterfaceNrtVbrBf"),
        ("CEM-ATM", "cnAtmInterfaceUbrBf"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualRxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceAvailableRxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceAvailableTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceCellScrambling"),
        ("CEM-ATM", "cnAtmInterfaceRowStatus"),
        ("CEM-ATM", "cnAtmNodeQos1Clr0"),
        ("CEM-ATM", "cnAtmNodeQos2Clr0"),
        ("CEM-ATM", "cnAtmNodeQos1Clr1"),
        ("CEM-ATM", "cnAtmNodeQos2Clr1"),
        ("CEM-ATM", "cnAtmNodeQos3Clr1"),
        ("CEM-ATM", "cnAtmNodeQos4Clr1"),
        ("CEM-ATM", "cnAtmNodeQos1Cdv"),
        ("CEM-ATM", "cnAtmNodeQos2Cdv"),
        ("CEM-ATM", "cnAtmNodeQos3Cdv"),
        ("CEM-ATM", "cnAtmNodeQos4Cdv"),
        ("CEM-ATM", "cnAtmNodeQos1MaxCtd"),
        ("CEM-ATM", "cnAtmNodeQos2MaxCtd"),
        ("CEM-ATM", "cnDefaultAtmTrafficDescrParamIndex"),
        ("CEM-ATM", "cnAtmF5EPType"),
        ("CEM-ATM", "cnAtmF5EPConnectionState"),
        ("CEM-ATM", "cnAtmF5EPContinuityCheck"),
        ("CEM-ATM", "cnAtmF5EPLaunchLoopback"),
        ("CEM-ATM", "cnAtmDownstreamCgtnDcrdClp1"),
        ("CEM-ATM", "cnAtmDownstreamCgtnDcrdClp0"),
        ("CEM-ATM", "cnAtmUpstreamCgtnDcrdClp1"),
        ("CEM-ATM", "cnAtmUpstreamCgtnDcrdClp0"),
        ("CEM-ATM", "cnAtmInterfaceGfrBf"),
        ("CEM-ATM", "cnAtmF5EPTraps"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigRxBandwidth"))
)
if mibBuilder.loadTexts:
    cnx511ATMObjectGroup.setStatus("current")

cn1KATMObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3, 1, 3)
)
cn1KATMObjectGroup.setObjects(
      *(("CEM-ATM", "cnAtmInterfaceMaxConfigVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMinConfigVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMinActualVpiBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMinConfigVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMinActualVciBits"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVpc"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVpc"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigVcc"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualVcc"),
        ("CEM-ATM", "cnAtmInterfaceServiceCatSupported"),
        ("CEM-ATM", "cnAtmInterfaceCbrBf"),
        ("CEM-ATM", "cnAtmInterfaceRtVbrBf"),
        ("CEM-ATM", "cnAtmInterfaceNrtVbrBf"),
        ("CEM-ATM", "cnAtmInterfaceUbrBf"),
        ("CEM-ATM", "cnAtmInterfaceGfrBf"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualRxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceMaxActualTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceAvailableRxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceAvailableTxBandwidth"),
        ("CEM-ATM", "cnAtmInterfaceCellScrambling"),
        ("CEM-ATM", "cnAtmInterfaceRowStatus"),
        ("CEM-ATM", "cnAtmNodeQos1Clr0"),
        ("CEM-ATM", "cnAtmNodeQos2Clr0"),
        ("CEM-ATM", "cnAtmNodeQos1Clr1"),
        ("CEM-ATM", "cnAtmNodeQos2Clr1"),
        ("CEM-ATM", "cnAtmNodeQos3Clr1"),
        ("CEM-ATM", "cnAtmNodeQos1Cdv"),
        ("CEM-ATM", "cnAtmNodeQos2Cdv"),
        ("CEM-ATM", "cnAtmNodeQos3Cdv"),
        ("CEM-ATM", "cnAtmNodeQos4Cdv"),
        ("CEM-ATM", "cnAtmNodeQos1MaxCtd"),
        ("CEM-ATM", "cnAtmNodeQos2MaxCtd"),
        ("CEM-ATM", "cnDefaultAtmTrafficDescrParamIndex"),
        ("CEM-ATM", "cnAtmF5EPType"),
        ("CEM-ATM", "cnAtmF5EPConnectionState"),
        ("CEM-ATM", "cnAtmF5EPContinuityCheck"),
        ("CEM-ATM", "cnAtmF5EPLaunchLoopback"),
        ("CEM-ATM", "cnAtmF5EPTraps"),
        ("CEM-ATM", "cnAtmUpstreamCgtnDcrdClp0"),
        ("CEM-ATM", "cnAtmUpstreamCgtnDcrdClp1"),
        ("CEM-ATM", "cnAtmDownstreamCgtnDcrdClp0"),
        ("CEM-ATM", "cnAtmInterfaceMaxConfigRxBandwidth"),
        ("CEM-ATM", "cnAtmDownstreamCgtnDcrdClp1"),
        ("CEM-ATM", "cnAtmNodeQos4Clr1"),
        ("CEM-ATM", "cnAtmIntfInCells"),
        ("CEM-ATM", "cnAtmIntfOutCells"),
        ("CEM-ATM", "cnAtmIntfInErrors"),
        ("CEM-ATM", "cnAtmIntfInUnknownProtos"),
        ("CEM-ATM", "cnAtmIntfInDiscards"),
        ("CEM-ATM", "cnAtmIntfOutDiscards"),
        ("CEM-ATM", "cnAtmVclTotalCongDiscards"),
        ("CEM-ATM", "cnAtmPvcUpstreamPolicing"),
        ("CEM-ATM", "cnAtmInterfacePvcUpstreamPolicing"),
        ("CEM-ATM", "cnAtmVclClp0CongDiscards"),
        ("CEM-ATM", "cnAtmInterfaceIntervalStats"),
        ("CEM-ATM", "cnAtmIntfIntervalInCells"),
        ("CEM-ATM", "cnAtmIntfIntervalOutCells"),
        ("CEM-ATM", "cnAtmIntfIntervalInErrors"),
        ("CEM-ATM", "cnAtmIntfIntervalInUnknownProtos"),
        ("CEM-ATM", "cnAtmIntfIntervalInDiscards"),
        ("CEM-ATM", "cnAtmIntfIntervalOutDiscards"),
        ("CEM-ATM", "cnAtmIntfIntervalValidData"))
)
if mibBuilder.loadTexts:
    cn1KATMObjectGroup.setStatus("current")


# Notification objects

cnAtmF5LoopbackTestPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 4, 2, 1)
)
cnAtmF5LoopbackTestPassed.setObjects(
    ("CEM-ATM", "cnAtmF5EPLaunchLoopback")
)
if mibBuilder.loadTexts:
    cnAtmF5LoopbackTestPassed.setStatus(
        "current"
    )

cnAtmF5AisClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 4, 2, 2)
)
cnAtmF5AisClear.setObjects(
    ("CEM-ATM", "cnAtmF5EPConnectionState")
)
if mibBuilder.loadTexts:
    cnAtmF5AisClear.setStatus(
        "current"
    )

cnAtmF5AisRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 4, 2, 3)
)
cnAtmF5AisRaise.setObjects(
    ("CEM-ATM", "cnAtmF5EPConnectionState")
)
if mibBuilder.loadTexts:
    cnAtmF5AisRaise.setStatus(
        "current"
    )

cnAtmF5LoopbackTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 4, 2, 4)
)
cnAtmF5LoopbackTestFailed.setObjects(
    ("CEM-ATM", "cnAtmF5EPLaunchLoopback")
)
if mibBuilder.loadTexts:
    cnAtmF5LoopbackTestFailed.setStatus(
        "current"
    )


# Notifications groups

cnx511ATMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3, 1, 4)
)
cnx511ATMNotificationGroup.setObjects(
      *(("CEM-ATM", "cnAtmF5LoopbackTestPassed"),
        ("CEM-ATM", "cnAtmF5AisClear"),
        ("CEM-ATM", "cnAtmF5AisRaise"),
        ("CEM-ATM", "cnAtmF5LoopbackTestFailed"))
)
if mibBuilder.loadTexts:
    cnx511ATMNotificationGroup.setStatus(
        "current"
    )

cn1KATMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 4, 3, 1, 5)
)
cn1KATMNotificationGroup.setObjects(
      *(("CEM-ATM", "cnAtmF5LoopbackTestPassed"),
        ("CEM-ATM", "cnAtmF5AisClear"),
        ("CEM-ATM", "cnAtmF5AisRaise"),
        ("CEM-ATM", "cnAtmF5LoopbackTestFailed"))
)
if mibBuilder.loadTexts:
    cn1KATMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-ATM",
    **{"CnAtmLaunchLoopbackControlType": CnAtmLaunchLoopbackControlType,
       "CnAtmLaunchLoopbackStatusType": CnAtmLaunchLoopbackStatusType,
       "CnAtmPvcUpstreamPolicingControl": CnAtmPvcUpstreamPolicingControl,
       "cnAtmMIB": cnAtmMIB,
       "cnAtmObjects": cnAtmObjects,
       "cnAtmTrafficDescriptorTypes": cnAtmTrafficDescriptorTypes,
       "cnAtmNoClpNoScrMcr": cnAtmNoClpNoScrMcr,
       "cnAtmNoClpTaggingNoScrMcr": cnAtmNoClpTaggingNoScrMcr,
       "cnAtmNoClpNoScrMdcrCdvt": cnAtmNoClpNoScrMdcrCdvt,
       "cnAtmNoClpTaggingNoScrMdcrCdvt": cnAtmNoClpTaggingNoScrMdcrCdvt,
       "cnAtmClpNoScrMcrCdvt": cnAtmClpNoScrMcrCdvt,
       "cnAtmClpTaggingNoScrMcrCdvt": cnAtmClpTaggingNoScrMcrCdvt,
       "cnAtmInterfaceConfTable": cnAtmInterfaceConfTable,
       "cnAtmInterfaceConfEntry": cnAtmInterfaceConfEntry,
       "cnAtmInterfaceMaxConfigVpiBits": cnAtmInterfaceMaxConfigVpiBits,
       "cnAtmInterfaceMaxActualVpiBits": cnAtmInterfaceMaxActualVpiBits,
       "cnAtmInterfaceMinConfigVpiBits": cnAtmInterfaceMinConfigVpiBits,
       "cnAtmInterfaceMinActualVpiBits": cnAtmInterfaceMinActualVpiBits,
       "cnAtmInterfaceMaxConfigVciBits": cnAtmInterfaceMaxConfigVciBits,
       "cnAtmInterfaceMaxActualVciBits": cnAtmInterfaceMaxActualVciBits,
       "cnAtmInterfaceMinConfigVciBits": cnAtmInterfaceMinConfigVciBits,
       "cnAtmInterfaceMinActualVciBits": cnAtmInterfaceMinActualVciBits,
       "cnAtmInterfaceMaxConfigVpc": cnAtmInterfaceMaxConfigVpc,
       "cnAtmInterfaceMaxActualVpc": cnAtmInterfaceMaxActualVpc,
       "cnAtmInterfaceMaxConfigVcc": cnAtmInterfaceMaxConfigVcc,
       "cnAtmInterfaceMaxActualVcc": cnAtmInterfaceMaxActualVcc,
       "cnAtmInterfaceServiceCatSupported": cnAtmInterfaceServiceCatSupported,
       "cnAtmInterfaceCbrBf": cnAtmInterfaceCbrBf,
       "cnAtmInterfaceRtVbrBf": cnAtmInterfaceRtVbrBf,
       "cnAtmInterfaceNrtVbrBf": cnAtmInterfaceNrtVbrBf,
       "cnAtmInterfaceUbrBf": cnAtmInterfaceUbrBf,
       "cnAtmInterfaceUbrPlusBf": cnAtmInterfaceUbrPlusBf,
       "cnAtmInterfaceMaxConfigRxBandwidth": cnAtmInterfaceMaxConfigRxBandwidth,
       "cnAtmInterfaceGfrBf": cnAtmInterfaceGfrBf,
       "cnAtmInterfaceMaxConfigTxBandwidth": cnAtmInterfaceMaxConfigTxBandwidth,
       "cnAtmInterfaceMaxActualRxBandwidth": cnAtmInterfaceMaxActualRxBandwidth,
       "cnAtmInterfaceMaxActualTxBandwidth": cnAtmInterfaceMaxActualTxBandwidth,
       "cnAtmInterfaceAvailableRxBandwidth": cnAtmInterfaceAvailableRxBandwidth,
       "cnAtmInterfaceAvailableTxBandwidth": cnAtmInterfaceAvailableTxBandwidth,
       "cnAtmInterfaceCellScrambling": cnAtmInterfaceCellScrambling,
       "cnAtmInterfaceIntervalStats": cnAtmInterfaceIntervalStats,
       "cnAtmInterfaceRowStatus": cnAtmInterfaceRowStatus,
       "cnAtmInterfacePvcUpstreamPolicing": cnAtmInterfacePvcUpstreamPolicing,
       "cnAtmNode": cnAtmNode,
       "cnAtmNodeQos1Clr0": cnAtmNodeQos1Clr0,
       "cnAtmNodeQos2Clr0": cnAtmNodeQos2Clr0,
       "cnAtmNodeQos3Clr0": cnAtmNodeQos3Clr0,
       "cnAtmNodeQos4Clr0": cnAtmNodeQos4Clr0,
       "cnAtmNodeQos1Clr1": cnAtmNodeQos1Clr1,
       "cnAtmNodeQos2Clr1": cnAtmNodeQos2Clr1,
       "cnAtmNodeQos3Clr1": cnAtmNodeQos3Clr1,
       "cnAtmNodeQos4Clr1": cnAtmNodeQos4Clr1,
       "cnAtmNodeQos1Cdv": cnAtmNodeQos1Cdv,
       "cnAtmNodeQos2Cdv": cnAtmNodeQos2Cdv,
       "cnAtmNodeQos3Cdv": cnAtmNodeQos3Cdv,
       "cnAtmNodeQos4Cdv": cnAtmNodeQos4Cdv,
       "cnAtmNodeQos1MaxCtd": cnAtmNodeQos1MaxCtd,
       "cnAtmNodeQos2MaxCtd": cnAtmNodeQos2MaxCtd,
       "cnDefaultAtmTrafficDescrParamIndex": cnDefaultAtmTrafficDescrParamIndex,
       "cnAtmEndPointTable": cnAtmEndPointTable,
       "cnAtmEndPointEntry": cnAtmEndPointEntry,
       "cnAtmF5EPType": cnAtmF5EPType,
       "cnAtmF5EPConnectionState": cnAtmF5EPConnectionState,
       "cnAtmF5EPContinuityCheck": cnAtmF5EPContinuityCheck,
       "cnAtmF5EPLaunchLoopback": cnAtmF5EPLaunchLoopback,
       "cnAtmF5EPTraps": cnAtmF5EPTraps,
       "cnAtmEPType": cnAtmEPType,
       "cnAtmSysStats": cnAtmSysStats,
       "cnAtmUpstreamCgtnDcrdClp0": cnAtmUpstreamCgtnDcrdClp0,
       "cnAtmUpstreamCgtnDcrdClp1": cnAtmUpstreamCgtnDcrdClp1,
       "cnAtmDownstreamCgtnDcrdClp0": cnAtmDownstreamCgtnDcrdClp0,
       "cnAtmDownstreamCgtnDcrdClp1": cnAtmDownstreamCgtnDcrdClp1,
       "cnAtmInterfaceStatsTable": cnAtmInterfaceStatsTable,
       "cnAtmInterfaceStatsEntry": cnAtmInterfaceStatsEntry,
       "cnAtmIntfInCells": cnAtmIntfInCells,
       "cnAtmIntfOutCells": cnAtmIntfOutCells,
       "cnAtmIntfInErrors": cnAtmIntfInErrors,
       "cnAtmIntfInUnknownProtos": cnAtmIntfInUnknownProtos,
       "cnAtmIntfInDiscards": cnAtmIntfInDiscards,
       "cnAtmIntfOutDiscards": cnAtmIntfOutDiscards,
       "cnAtmIntfLastUnknownVpi": cnAtmIntfLastUnknownVpi,
       "cnAtmIntfLastUnknownVci": cnAtmIntfLastUnknownVci,
       "cnAtmVclStatTable": cnAtmVclStatTable,
       "cnAtmVclStatEntry": cnAtmVclStatEntry,
       "cnAtmVclTotalCongDiscards": cnAtmVclTotalCongDiscards,
       "cnAtmVclClp0CongDiscards": cnAtmVclClp0CongDiscards,
       "cnAtmInterfaceIntervalStatsTable": cnAtmInterfaceIntervalStatsTable,
       "cnAtmInterfaceIntervalStatsEntry": cnAtmInterfaceIntervalStatsEntry,
       "cnAtmIntfIntervalNumber": cnAtmIntfIntervalNumber,
       "cnAtmIntfIntervalInCells": cnAtmIntfIntervalInCells,
       "cnAtmIntfIntervalOutCells": cnAtmIntfIntervalOutCells,
       "cnAtmIntfIntervalInErrors": cnAtmIntfIntervalInErrors,
       "cnAtmIntfIntervalInUnknownProtos": cnAtmIntfIntervalInUnknownProtos,
       "cnAtmIntfIntervalInDiscards": cnAtmIntfIntervalInDiscards,
       "cnAtmIntfIntervalOutDiscards": cnAtmIntfIntervalOutDiscards,
       "cnAtmIntfIntervalValidData": cnAtmIntfIntervalValidData,
       "cnAtmVcCrossConnectTable": cnAtmVcCrossConnectTable,
       "cnAtmVcCrossConnectEntry": cnAtmVcCrossConnectEntry,
       "cnAtmPvcUpstreamPolicing": cnAtmPvcUpstreamPolicing,
       "cnAtmDSPvcTag": cnAtmDSPvcTag,
       "cnAtmUSPvcTag": cnAtmUSPvcTag,
       "cnAtmPvcServiceType": cnAtmPvcServiceType,
       "cnAtmTDScopeTable": cnAtmTDScopeTable,
       "cnAtmTDScopeEntry": cnAtmTDScopeEntry,
       "cnAtmTDScope": cnAtmTDScope,
       "cnAtmTrafficDescrGlobalParamIndexNext": cnAtmTrafficDescrGlobalParamIndexNext,
       "cnAtmTDDistListTable": cnAtmTDDistListTable,
       "cnAtmTDDistListEntry": cnAtmTDDistListEntry,
       "cnAtmTDDistListIndex": cnAtmTDDistListIndex,
       "cnAtmVpCrossConnectTable": cnAtmVpCrossConnectTable,
       "cnAtmVpCrossConnectEntry": cnAtmVpCrossConnectEntry,
       "cnAtmPvpServiceType": cnAtmPvpServiceType,
       "cnAtmDSPvpTag": cnAtmDSPvpTag,
       "cnAtmUSPvpTag": cnAtmUSPvpTag,
       "cnAtmNotifications": cnAtmNotifications,
       "cnAtmF5LoopbackTestPassed": cnAtmF5LoopbackTestPassed,
       "cnAtmF5AisClear": cnAtmF5AisClear,
       "cnAtmF5AisRaise": cnAtmF5AisRaise,
       "cnAtmF5LoopbackTestFailed": cnAtmF5LoopbackTestFailed,
       "cnAtmModuleConformance": cnAtmModuleConformance,
       "cnAtmGroups": cnAtmGroups,
       "cnx510ATMObjectGroup": cnx510ATMObjectGroup,
       "cnx511ATMObjectGroup": cnx511ATMObjectGroup,
       "cn1KATMObjectGroup": cn1KATMObjectGroup,
       "cnx511ATMNotificationGroup": cnx511ATMNotificationGroup,
       "cn1KATMNotificationGroup": cn1KATMNotificationGroup}
)
